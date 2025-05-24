"""
Series generator for auto-generating a complete series of novels.
"""
import os
import json
from typing import Dict, List, Any
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

from src.core.novel_generator import NovelGenerator
from src.formatters.epub_formatter import EpubFormatter
from src.utils.file_handler import create_output_directory, save_novel_json, create_series_directory
from src.ui.terminal_ui import generate_cover
from src.core.series_manager import SeriesManager
from src.utils.genre_defaults import get_genre_defaults
from src.prompts import get_prompt
from src.utils.series_continuity import SeriesContinuityManager
from src.utils.series_prompt_manager import SeriesPromptManager

console = Console(markup=True)


class SeriesGenerator:
    """
    Generator for auto-generating a complete series of novels.
    """

    def __init__(self):
        """Initialize the series generator."""
        self.series_manager = None
        self.novel_generator = NovelGenerator()
        self.series_metadata = {}
        self.book_templates = []
        self.generation_options = None
        self.continuity_manager = None
        self.series_prompt_manager = None

    def initialize_series(
        self, series_title: str, series_description: str, genre: str, target_audience: str,
        planned_books: int, author: str
    ) -> SeriesManager:
        """
        Initialize a new series with basic information.

        Args:
            series_title: Series title
            series_description: Brief description of the series
            genre: Genre of the series
            target_audience: Target audience for the series
            planned_books: Number of planned books in the series
            author: Author name

        Returns:
            SeriesManager instance for the series
        """
        # Create series manager
        self.series_manager = SeriesManager(series_title)

        # Update series metadata
        self.series_manager.update_metadata(
            description=series_description,
            genre=genre,
            target_audience=target_audience,
            planned_books=planned_books,
            creator=author
        )

        # Store series metadata for later use
        self.series_metadata = {
            "title": series_title,
            "description": series_description,
            "genre": genre,
            "target_audience": target_audience,
            "planned_books": planned_books,
            "author": author
        }

        # Initialize continuity management
        series_dir = create_series_directory(series_title)
        self.continuity_manager = SeriesContinuityManager(series_title, series_dir)
        self.continuity_manager.total_books_planned = planned_books
        self.series_prompt_manager = SeriesPromptManager(self.continuity_manager)

        return self.series_manager

    def generate_series_plan(self) -> List[Dict[str, Any]]:
        """
        Generate a plan for the entire series.

        Returns:
            List of book templates for the series
        """
        if not self.series_manager:
            raise ValueError("Series not initialized. Call initialize_series first.")

        # Get series metadata
        series_title = self.series_metadata["title"]
        series_description = self.series_metadata["description"]
        genre = self.series_metadata["genre"]
        target_audience = self.series_metadata["target_audience"]
        planned_books = self.series_metadata["planned_books"]

        console.print("[bold cyan]Generating enhanced series plan with continuity tracking...[/bold cyan]")

        # Use enhanced series prompt manager for better continuity
        if self.series_prompt_manager:
            prompt = self.series_prompt_manager.get_enhanced_series_plan_prompt(
                genre=genre,
                series_title=series_title,
                series_description=series_description,
                planned_books=planned_books,
                target_audience=target_audience
            )
        else:
            # Fallback to basic genre-specific prompt
            prompt = get_prompt(
                genre=genre,
                prompt_type="series_plan",
                series_title=series_title,
                series_description=series_description,
                planned_books=planned_books,
                target_audience=target_audience
            )

        # Final fallback to generic prompt if nothing else works
        if not prompt:
            console.print("[bold yellow]Enhanced series prompt not available, using fallback...[/bold yellow]")
            prompt = f"""
            Create a detailed plan for a {genre} book series titled "{series_title}" for {target_audience} audience.

            Series description: {series_description}

            The series will consist of {planned_books} books. For each book, provide:
            1. Book title
            2. Brief description (2-3 sentences)
            3. Main plot arc for this book
            4. How this book fits into the overall series arc
            5. Key character developments in this book

            Format your response as a JSON array of book objects with these fields:
            - title: The book title
            - description: Brief description
            - main_plot: Main plot arc for this book
            - series_connection: How this book fits into the overall series
            - character_developments: Key character developments

            Also include a "series_arcs" array with the major plot arcs that span the entire series.
            """

        # Generate the series plan
        response = self.novel_generator.gemini.generate_content(prompt, temperature=0.7)

        # Try to parse the response as JSON
        try:
            # Find JSON content in the response
            start_idx = response.find('[')
            end_idx = response.rfind(']') + 1

            if start_idx >= 0 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                book_templates = json.loads(json_str)

                # Store the book templates
                self.book_templates = book_templates

                # Extract series arcs if available
                if isinstance(book_templates, dict) and "series_arcs" in book_templates:
                    series_arcs = book_templates["series_arcs"]
                    book_templates = book_templates["books"]

                    # Add series arcs to the series manager
                    for arc in series_arcs:
                        self.series_manager.add_series_arc(arc)

                console.print(f"[bold green]✓[/bold green] Series plan with {len(book_templates)} books generated successfully")

                return book_templates
            else:
                # If JSON parsing fails, create a structured list
                return self._fallback_series_plan(planned_books)

        except json.JSONDecodeError:
            # If JSON parsing fails, create a structured list
            return self._fallback_series_plan(planned_books)

    def _fallback_series_plan(self, planned_books: int) -> List[Dict[str, Any]]:
        """
        Create a fallback series plan when JSON parsing fails.

        Args:
            planned_books: Number of planned books

        Returns:
            List of book templates
        """
        console.print("[bold yellow]Using fallback series plan generation...[/bold yellow]")

        # Create a basic template for each book
        book_templates = []

        for i in range(1, planned_books + 1):
            book_template = {
                "title": f"{self.series_metadata['title']} - Book {i}",
                "description": f"Book {i} in the {self.series_metadata['title']} series.",
                "main_plot": f"Main plot for book {i}.",
                "series_connection": f"Connection to the overall series arc for book {i}.",
                "character_developments": f"Character developments in book {i}."
            }
            book_templates.append(book_template)

        # Store the book templates
        self.book_templates = book_templates

        console.print(f"[bold green]✓[/bold green] Fallback series plan with {len(book_templates)} books generated")

        return book_templates

    def generate_book(self, book_template: Dict[str, Any], book_number: int) -> str:
        """
        Generate a single book in the series.

        Args:
            book_template: Template for the book
            book_number: Book number in the series

        Returns:
            Path to the generated EPUB file
        """
        if not self.series_manager:
            raise ValueError("Series not initialized. Call initialize_series first.")

        # Get book information from template
        book_title = book_template["title"]
        book_description = book_template["description"]

        console.print(f"\n[bold cyan]Generating Book {book_number}: {book_title}[/bold cyan]")

        # Initialize continuity tracking for this book
        if self.continuity_manager:
            self.continuity_manager.start_new_book(book_number)
            console.print("[bold cyan]Continuity tracking initialized for this book[/bold cyan]")

        # Create output directory for this book
        output_dir = create_output_directory(
            book_title,
            series_manager=self.series_manager,
            book_number=book_number
        )

        # Initialize novel generator with output directory for memory files
        # Use placeholder author initially - will be replaced by fictional author selection
        memory_manager = self.novel_generator.initialize_novel(
            title=book_title,
            author="AI Author",  # Placeholder - will be replaced by fictional author
            description=book_description,
            genre=self.series_metadata["genre"],
            target_audience=self.series_metadata["target_audience"],
            output_dir=output_dir,
            series_manager=self.series_manager,
            book_number=book_number
        )

        # Get generation options based on genre
        if not self.generation_options:
            self.generation_options = get_genre_defaults(self.series_metadata["genre"])

        # Set generation options
        self.novel_generator.set_generation_options(self.generation_options)

        # Set series prompt manager for enhanced prompts
        if self.series_prompt_manager:
            self.novel_generator.set_series_prompt_manager(self.series_prompt_manager)

        # Automatically select fictional author for series
        console.print("[bold cyan]Automatically selecting fictional author for series...[/bold cyan]")

        # Initialize writer profile manager for automatic selection
        from src.utils.writer_profile_manager import WriterProfileManager
        profile_manager = WriterProfileManager()

        # Get series themes for enhancement
        series_themes = self.series_metadata.get("themes", [])
        book_count = len(self.series_plan) if hasattr(self, 'series_plan') else 1

        # Automatically select and enhance fictional author profile for series
        writer_profile = profile_manager.get_auto_selected_profile_for_series(
            genre=self.series_metadata["genre"],
            series_themes=series_themes,
            book_count=book_count
        )

        if writer_profile:
            author_name = writer_profile.get("name", "Unknown Author")
            console.print(f"[bold green]✓[/bold green] Selected fictional author for series: [bold cyan]{author_name}[/bold cyan]")

            # Update the memory manager with the selected fictional author
            memory_manager.metadata["author"] = author_name

            # Check if profile was enhanced for series
            if "_series_enhancement" in writer_profile:
                console.print("[bold green]Profile enhanced with AI for series writing")
        else:
            # Fallback to traditional generation
            console.print("[bold yellow]No fictional author available, generating custom profile...")
            writer_profile = self.novel_generator.generate_writer_profile()
            console.print("[bold green]✓[/bold green] Custom writer profile generated successfully")

        # Generate novel outline
        console.print("[bold cyan]Generating novel outline...[/bold cyan]")
        chapter_outlines, chapter_count = self.novel_generator.generate_novel_outline(writer_profile)
        console.print(f"[bold green]✓[/bold green] Novel outline with {chapter_count} chapters generated successfully")

        # Generate characters only for content types that need them
        from src.utils.genre_utils import should_generate_characters
        characters = []
        genre = self.series_metadata["genre"]

        if should_generate_characters(genre):
            console.print("[bold cyan]Generating characters...[/bold cyan]")
            characters = self.novel_generator.generate_characters()
            console.print(f"[bold green]✓[/bold green] {len(characters)} characters generated successfully")
        else:
            console.print(f"[bold yellow]Skipping character generation (not needed for {genre})")
            # Create empty character list for non-fiction and special formats
            characters = []

        # Generate chapters
        console.print("[bold cyan]Generating and enhancing chapters...[/bold cyan]")
        chapters = []

        # Create a progress bar for chapter generation and enhancement
        with Progress(
            SpinnerColumn(),
            TextColumn("[bold cyan]Processing chapters: {task.completed}/{task.total}"),
            BarColumn(),
            TextColumn("[bold cyan]{task.percentage:>3.0f}%"),
            TimeElapsedColumn()
        ) as progress:
            task = progress.add_task("Processing chapters", total=chapter_count)

            # Process one chapter at a time (generate, enhance, then move to next)

            for chapter_num in range(1, chapter_count + 1):
                # Get chapter title
                chapter_title = "Chapter"
                if chapter_num <= len(chapter_outlines):
                    outline = chapter_outlines[chapter_num - 1]
                    if " - " in outline:
                        chapter_title = outline.split(" - ")[0]
                    else:
                        chapter_title = outline

                # Generate current chapter
                console.print(f"[bold cyan]Generating Chapter {chapter_num}: {chapter_title}[/bold cyan]")
                current_chapter_text = self.novel_generator.generate_chapter(chapter_num)



                # Enhance the current chapter
                console.print(f"[bold cyan]Enhancing Chapter {chapter_num}: {chapter_title}[/bold cyan]")
                enhanced_text = self.novel_generator.enhance_chapter(
                    current_chapter_text,
                    chapter_num,
                    chapter_title
                )

                # Add enhanced chapter to list
                chapters.append({
                    "number": chapter_num,
                    "title": chapter_title,
                    "content": enhanced_text
                })

                # Update progress
                progress.update(task, advance=1)

                console.print(f"[bold green]✓[/bold green] Chapter {chapter_num} completed")

        console.print(f"[bold green]✓[/bold green] All {chapter_count} chapters generated and enhanced successfully")

        # Display final word count information
        current_word_count = memory_manager.structure["current_word_count"]
        target_word_count = memory_manager.structure["target_word_count"]

        console.print(f"[bold green]✓[/bold green] Final word count: {current_word_count} words (Target: {target_word_count} words)")

        # Compile novel information
        novel = {
            "metadata": memory_manager.metadata,
            "writer_profile": writer_profile,
            "generation_options": self.generation_options or {},
            "outline": chapter_outlines,
            "characters": characters,
            "chapters": chapters,
            "word_count": memory_manager.structure["current_word_count"]
        }

        # Save novel as JSON
        save_novel_json(novel, output_dir)

        # Generate cover prompt for series book
        self._generate_series_cover_prompt(novel, output_dir, book_number)

        # Update continuity tracking with completed book data
        if self.series_prompt_manager:
            try:
                console.print("[bold cyan]Updating series continuity tracking...[/bold cyan]")
                self.series_prompt_manager.update_continuity_from_book(novel, book_number)
                console.print("[bold green]✓[/bold green] Series continuity updated")
            except Exception as e:
                console.print(f"[bold yellow]Warning: Series continuity tracking failed: {str(e)}[/bold yellow]")
                console.print("[dim]Continuing with book generation...[/dim]")

        # Generate cover automatically in series mode
        cover_path = generate_cover(novel, output_dir, auto_mode=True)

        # Format and save as EPUB with writer profile
        console.print("[bold cyan]Formatting EPUB...[/bold cyan]")
        formatter = EpubFormatter(novel, writer_profile=writer_profile)
        epub_path = formatter.save_epub(output_dir, cover_path, writer_profile)

        # Display completion message with absolute path
        abs_path = os.path.abspath(epub_path)
        console.print(f"[bold green]✓[/bold green] Book {book_number}: {book_title} saved to: [bold cyan]{abs_path}[/bold cyan]")

        return abs_path

    def _generate_series_cover_prompt(self, novel: Dict[str, Any], output_dir: str, book_number: int) -> None:
        """
        Generate cover prompt for a series book.

        Args:
            novel: Complete novel data
            output_dir: Output directory for the book
            book_number: Book number in the series
        """
        try:
            from src.utils.cover_prompt_generator import CoverPromptGenerator

            # Get series information
            series_info = {
                "series_title": self.series_metadata["title"],
                "book_number": book_number
            }

            # Generate the cover prompt
            console.print("[bold cyan]Generating cover prompt...[/bold cyan]")
            prompt_generator = CoverPromptGenerator()
            prompt_path = prompt_generator.generate_cover_prompt(
                novel_data=novel,
                output_dir=output_dir,
                series_info=series_info
            )

            console.print(f"[bold green]✓[/bold green] Cover prompt saved to: [bold cyan]{prompt_path}[/bold cyan]")

        except Exception as e:
            console.print(f"[bold yellow]Warning: Could not generate cover prompt: {str(e)}[/bold yellow]")
