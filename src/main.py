"""
Main entry point for the NovelForge AI system.

This module serves as the primary entry point for the NovelForge AI application.
It handles the novel generation process, from collecting user input to generating
the final EPUB file. It also provides integration with the series management system
when available.

Usage:
    python -m src.main
    python -m src.main --series-menu
    python -m src.main --auto-series
"""
# Standard library imports
import os
import sys
import json
import datetime
from typing import Dict, Any

# Third-party imports
import questionary
from rich.console import Console
from rich.table import Table
from rich import box

# Local application imports
from src.core.novel_generator import NovelGenerator
from src.formatters.epub_formatter import EpubFormatter
from src.utils.file_handler import create_output_directory, save_novel_json
from src.core.series_manager import SeriesManager
from src.core.series_generator import SeriesGenerator
from src.utils.logger import init_logger, get_logger, close_logger, log_info, log_error, log_debug, log_warning, log_critical
from src.ui.terminal_ui import (
    clear_screen,
    display_title,
    get_novel_info,
    get_series_info,
    display_series_info,
    display_generation_complete,
    confirm_generation,
    get_custom_generation_options,
    generation_timer,

    generate_cover,
    custom_style
)


# Optional imports
try:
    from src.ui.series_menu import series_management_menu
except ImportError:
    series_management_menu = None

# Create console with markup enabled
console = Console(markup=True)


# Character generation function moved to src.utils.genre_utils
from src.utils.genre_utils import should_generate_characters


def main_with_advanced_options(advanced_options: Dict[str, Any]) -> None:
    """
    Generate a novel using advanced generation options.

    This function takes the results from the advanced generation options
    and uses them to create a novel with the specified parameters.

    Args:
        advanced_options: Dictionary containing advanced generation parameters
    """
    # Initialize logging system
    logger = init_logger("DEBUG")

    try:
        log_info("=== ADVANCED GENERATION SESSION STARTED ===")
        log_info("Starting advanced generation with preset options", mode=advanced_options.get("mode"))

        # Clear screen and display title
        clear_screen()
        display_title()

        # Display the advanced generation mode
        mode = advanced_options.get("mode", "unknown")
        mode_display = {
            "surprise_me": "Surprise Me Mode",
            "author_focus": "Author Focus Mode",
            "cultural_journey": "Cultural Journey Mode",
            "genre_fusion": "Genre Fusion Mode"
        }

        console.print(f"[bold cyan]{mode_display.get(mode, 'Advanced Generation')}[/bold cyan]")
        console.print("Generating your book with the selected advanced options...\n")

        # Extract novel information from advanced options
        novel_info = {
            "title": advanced_options.get("title", "Advanced Generated Novel"),
            "author": advanced_options.get("author", "AI Author"),
            "description": advanced_options.get("description", "An AI-generated novel."),
            "genre": advanced_options.get("genre", "Literary Fiction"),
            "target_audience": "Adult (18+)"  # Default for advanced options
        }

        # Extract generation options
        generation_options = {
            "themes": advanced_options.get("themes", []),
            "writing_style": advanced_options.get("writing_style", "descriptive"),
            "target_length": advanced_options.get("target_length", "medium")
        }

        # Display the selected options
        console.print(f"[bold green]Selected Options:[/bold green]")
        console.print(f"  Title: [cyan]{novel_info['title']}[/cyan]")
        console.print(f"  Genre: [cyan]{novel_info['genre']}[/cyan]")
        console.print(f"  Author: [cyan]{novel_info['author']}[/cyan]")
        console.print(f"  Themes: [cyan]{', '.join(generation_options['themes'])}[/cyan]")
        console.print(f"  Style: [cyan]{generation_options['writing_style']}[/cyan]")
        console.print(f"  Length: [cyan]{generation_options['target_length']}[/cyan]")

        # Show mode-specific information
        if mode == "author_focus":
            console.print(f"  Focus Author: [cyan]{advanced_options.get('focus_author')}[/cyan]")
        elif mode == "cultural_journey":
            console.print(f"  Cultural Region: [cyan]{advanced_options.get('cultural_region')}[/cyan]")
            console.print(f"  Cultural Background: [cyan]{advanced_options.get('cultural_background')}[/cyan]")
        elif mode == "genre_fusion":
            console.print(f"  Fusion Type: [cyan]{advanced_options.get('fusion_type')}[/cyan]")
            console.print(f"  Primary Genre: [cyan]{advanced_options.get('primary_genre')}[/cyan]")
            console.print(f"  Secondary Genre: [cyan]{advanced_options.get('secondary_genre')}[/cyan]")

        # Create output directory
        output_dir = create_output_directory(novel_info["title"])
        output_dir = output_dir.replace('\\', '/')

        # Initialize novel generator
        generator = NovelGenerator()
        memory_manager = generator.initialize_novel(
            title=novel_info["title"],
            author=novel_info["author"],
            description=novel_info["description"],
            genre=novel_info["genre"],
            target_audience=novel_info["target_audience"],
            output_dir=output_dir
        )

        # Set generation options
        generator.set_generation_options(generation_options)

        # Check API connection
        console.print("\n[bold cyan]Checking API connection...[/bold cyan]")
        api_status = generator.gemini.check_api_connection(check_all_keys=True)

        if not api_status["success"]:
            console.print("[bold red]Error: Unable to connect to the Gemini API.[/bold red]")
            return

        console.print(f"[bold green]✓[/bold green] API connection successful!")

        # Start generation timer
        generation_timer.start()
        console.print("\n[bold cyan]Advanced generation started![/bold cyan]")

        # Use the pre-selected writer profile from advanced options
        writer_profile = advanced_options.get("selected_profile")
        if writer_profile:
            author_name = writer_profile.get("name", "Unknown Author")
            console.print(f"[bold green]✓[/bold green] Using fictional author: [bold cyan]{author_name}[/bold cyan]")
        else:
            # Fallback to automatic selection
            from src.utils.writer_profile_manager import WriterProfileManager
            profile_manager = WriterProfileManager()
            writer_profile = profile_manager.get_auto_selected_profile_for_book(
                genre=novel_info["genre"],
                themes=generation_options.get("themes"),
                writing_style=generation_options.get("writing_style"),
                target_length=generation_options.get("target_length")
            )

            if writer_profile:
                author_name = writer_profile.get("name", "Unknown Author")
                console.print(f"[bold green]✓[/bold green] Auto-selected fictional author: [bold cyan]{author_name}[/bold cyan]")
            else:
                console.print("[bold yellow]Using fallback profile generation...")
                writer_profile = generator.generate_writer_profile()

        # Continue with the standard generation process
        # (The rest follows the same pattern as the main() function)

        # Generate novel outline
        console.print("[bold cyan]Generating novel outline...[/bold cyan]")
        chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)

        if chapter_count == 0 or not chapter_outlines:
            console.print("[bold red]Failed to generate a proper novel outline.[/bold red]")
            return

        console.print(f"[bold green]✓[/bold green] Novel outline with {chapter_count} chapters generated")

        # Generate characters if needed
        characters = []
        if should_generate_characters(novel_info["genre"]):
            console.print("[bold cyan]Generating characters...[/bold cyan]")
            characters = generator.generate_characters()
            console.print(f"[bold green]✓[/bold green] {len(characters)} characters generated")
        else:
            console.print(f"[bold yellow]Skipping character generation (not needed for {novel_info['genre']})")

        # Continue with full chapter generation process
        console.print("\n[bold cyan]Generating and enhancing chapters...[/bold cyan]")
        chapters = []

        # Start the generation timer
        start_time = datetime.datetime.now()

        # Create a dictionary to store word counts
        chapter_word_counts = {}

        # Generate chapters with progress display
        from rich.live import Live
        from rich.table import Table

        def generate_chapter_display():
            current_time = datetime.datetime.now()
            elapsed = current_time - start_time
            elapsed_str = str(elapsed).split('.')[0]

            table = Table(title=f"Chapter Generation Progress - {elapsed_str}")
            table.add_column("Chapter", style="cyan", width=8)
            table.add_column("Title", style="green", width=30)
            table.add_column("Status", style="yellow", width=12)
            table.add_column("Words", style="magenta", width=8)

            for i in range(1, chapter_count + 1):
                if i <= len(chapters):
                    chapter = chapters[i-1]
                    title = chapter.get("title", "Untitled")[:27] + "..." if len(chapter.get("title", "")) > 30 else chapter.get("title", "Untitled")
                    status = "Complete"
                    words = str(chapter_word_counts.get(i, 0))
                elif i == len(chapters) + 1:
                    title = chapter_outlines[i-1].get("title", "Generating...")[:27] + "..." if len(chapter_outlines[i-1].get("title", "")) > 30 else chapter_outlines[i-1].get("title", "Generating...")
                    status = "Writing..."
                    words = "-"
                else:
                    title = chapter_outlines[i-1].get("title", "Pending")[:27] + "..." if len(chapter_outlines[i-1].get("title", "")) > 30 else chapter_outlines[i-1].get("title", "Pending")
                    status = "Pending"
                    words = "-"

                table.add_row(f"Ch {i}", title, status, words)

            return table

        # Generate chapters with live progress display
        with Live(generate_chapter_display(), refresh_per_second=1) as live:
            for i, chapter_outline in enumerate(chapter_outlines, 1):
                try:
                    live.update(generate_chapter_display())

                    chapter = generator.generate_chapter(
                        chapter_outline=chapter_outline,
                        chapter_number=i,
                        writer_profile=writer_profile,
                        characters=characters
                    )

                    if chapter:
                        chapters.append(chapter)
                        word_count = len(chapter.get("content", "").split())
                        chapter_word_counts[i] = word_count
                        log_info(f"Chapter {i} generated successfully",
                                chapter_number=i,
                                word_count=word_count,
                                title=chapter.get("title", "Untitled"))
                    else:
                        log_error(f"Failed to generate chapter {i}")
                        console.print(f"[bold red]Failed to generate chapter {i}[/bold red]")
                        break

                    live.update(generate_chapter_display())

                except Exception as e:
                    log_error(f"Error generating chapter {i}", exception=e, chapter_number=i)
                    console.print(f"[bold red]Error generating chapter {i}: {e}[/bold red]")
                    break

        # Check if all chapters were generated
        if len(chapters) != chapter_count:
            console.print(f"[bold red]Generation incomplete: {len(chapters)}/{chapter_count} chapters generated[/bold red]")
            return

        # Calculate total word count
        total_words = sum(chapter_word_counts.values())
        console.print(f"\n[bold green]✓[/bold green] All {chapter_count} chapters generated successfully!")
        console.print(f"[bold cyan]Total word count:[/bold cyan] {total_words:,} words")

        # Format and save the novel
        console.print("\n[bold cyan]Formatting and saving novel...[/bold cyan]")

        # Create EPUB
        epub_path = os.path.join(output_dir, f"{novel_info['title']}.epub")

        try:
            from src.core.epub_formatter import EPUBFormatter
            formatter = EPUBFormatter()

            formatter.create_epub(
                title=novel_info["title"],
                author=novel_info["author"],
                chapters=chapters,
                output_path=epub_path,
                description=novel_info["description"],
                genre=novel_info["genre"],
                target_audience=novel_info["target_audience"]
            )

            console.print(f"[bold green]✓[/bold green] EPUB created: {epub_path}")

        except Exception as e:
            log_error("EPUB creation failed", exception=e)
            console.print(f"[bold red]Failed to create EPUB: {e}[/bold red]")

        # Stop the timer
        generation_timer.stop()

        # Register content for quality tracking and offer feedback
        try:
            from src.quality.content_quality_system import quality_system, ContentMetadata
            from src.ui.feedback_system import feedback_ui
            import hashlib

            # Create content ID
            content_id = hashlib.md5(f"{novel_info['title']}_{datetime.datetime.now().isoformat()}".encode()).hexdigest()[:16]

            # Register content metadata
            metadata = ContentMetadata(
                content_id=content_id,
                title=novel_info["title"],
                fictional_author=writer_profile.get("name", "Unknown Author"),
                genre=novel_info["genre"],
                themes=generation_options.get("themes", []),
                writing_style=generation_options.get("writing_style", ""),
                target_length=generation_options.get("target_length", ""),
                word_count=total_words,
                generation_time=generation_timer.elapsed_time,
                enhancement_used=bool("_enhancement" in writer_profile),
                timestamp=datetime.datetime.now()
            )

            quality_system.register_content(metadata)

            # Assess content quality
            console.print("[bold cyan]Analyzing content quality...[/bold cyan]")
            full_content = "\n\n".join(chapter.get("content", "") for chapter in chapters)
            quality_assessment = quality_system.assess_content_quality(
                content_id=content_id,
                content=full_content,
                fictional_author=writer_profile.get("name", "Unknown Author"),
                genre=novel_info["genre"]
            )
            console.print("[bold green]✓[/bold green] Quality analysis completed")

            # Offer feedback collection
            console.print(f"\n[bold cyan]Content Feedback[/bold cyan]")
            collect_feedback = questionary.confirm(
                "Would you like to provide feedback on this generated content?",
                default=True,
                style=custom_style
            ).ask()

            if collect_feedback:
                feedback_ui.collect_content_feedback(
                    content_id=content_id,
                    title=novel_info["title"],
                    fictional_author=writer_profile.get("name", "Unknown Author"),
                    genre=novel_info["genre"]
                )
            else:
                # Offer quick rating as alternative
                quick_rating = questionary.confirm(
                    "Would you like to give a quick 1-5 star rating?",
                    default=True,
                    style=custom_style
                ).ask()

                if quick_rating:
                    feedback_ui.quick_rating(content_id, novel_info["title"])

        except Exception as e:
            console.print(f"[yellow]Note: Quality tracking unavailable: {e}[/yellow]")

        # Display completion message
        abs_path = os.path.abspath(epub_path)
        console.print(f"\n[bold green]Advanced generation mode '{mode}' completed successfully![/bold green]")
        console.print(f"[bold green]✓ Novel saved to:[/bold green] [bold cyan]{abs_path}[/bold cyan]")
        console.print(f"[bold green]✓ Total generation time:[/bold green] [bold cyan]{generation_timer.get_elapsed_time()}[/bold cyan]")
        console.print(f"[bold green]✓ Total word count:[/bold green] [bold cyan]{total_words:,} words[/bold cyan]")

        log_info("Advanced generation completed successfully",
                mode=mode,
                title=novel_info["title"],
                total_words=total_words,
                generation_time=generation_timer.elapsed_time)

    except Exception as e:
        log_error("Advanced generation failed", exception=e, mode=advanced_options.get("mode"))
        console.print(f"[bold red]Advanced generation failed: {e}[/bold red]")
        raise
    finally:
        try:
            close_logger()
        except:
            pass

def auto_generate_series() -> None:
    """
    Auto-generate a complete series without user interaction.

    This function automatically generates a complete series of novels without
    requiring user input at each step. It's useful for testing the series
    generation pipeline or for batch generation of content.

    The function:
    1. Initializes a series with predefined parameters
    2. Generates a series plan
    3. Creates each book in the series
    4. Saves the generated books as EPUB files

    Note: This uses hardcoded values for testing purposes.

    Returns:
        None
    """
    try:
        # Clear screen and display title
        clear_screen()
        display_title()

        console.print("[bold cyan]Auto-Generating Series[/bold cyan]")
        console.print("This will generate a complete series without further user input.\n")

        # Initialize series generator
        series_generator = SeriesGenerator()

        # Set series information
        series_title = "The Chronicles of Eldoria"
        series_description = "An epic fantasy series set in the magical world of Eldoria, where ancient powers awaken and heroes rise to face a growing darkness."
        genre = "Fantasy"
        target_audience = "Adult (18+)"
        planned_books = 3  # Limit to 3 books for testing
        author = "AI Author"

        # Initialize series
        console.print("[bold cyan]Initializing series...[/bold cyan]")
        series_manager = series_generator.initialize_series(
            series_title=series_title,
            series_description=series_description,
            genre=genre,
            target_audience=target_audience,
            planned_books=planned_books,
            author=author
        )
        console.print(f"[bold green]✓[/bold green] Series initialized: {series_title}")

        # Display series information
        display_series_info(series_manager)

        # Generate series plan
        console.print("[bold cyan]Generating series plan...[/bold cyan]")
        book_templates = series_generator.generate_series_plan()
        console.print(f"[bold green]✓[/bold green] Series plan generated with {len(book_templates)} books")

        # Start generation timer
        generation_timer.start()

        # Generate each book in the series
        generated_books = []
        for i, book_template in enumerate(book_templates, 1):
            console.print(f"\n[bold cyan]Generating Book {i} of {len(book_templates)}[/bold cyan]")
            epub_path = series_generator.generate_book(book_template, i)
            generated_books.append(epub_path)

        # Display completion message
        console.print("\n[bold green]✓ Series generation complete![/bold green]")
        console.print(f"[bold green]✓ Total generation time:[/bold green] [bold cyan]{generation_timer.get_elapsed_time()}[/bold cyan]")

        # Display generated books
        console.print("\n[bold cyan]Generated Books:[/bold cyan]")
        for i, path in enumerate(generated_books, 1):
            console.print(f"[bold green]Book {i}:[/bold green] [bold cyan]{path}[/bold cyan]")

        # Display series visualizations
        display_series_info(series_manager, show_visualizations=True)

    except Exception as e:
        console.print(f"[bold red]Error during series generation: {e}[/bold red]")
        import traceback
        console.print(traceback.format_exc())


def main() -> None:
    """
    Main function for generating a single novel.

    This function guides the user through the novel generation process:
    1. Collects basic novel information (title, author, genre, etc.)
    2. Initializes the novel generator
    3. Generates a writer profile
    4. Creates a novel outline
    5. Develops characters
    6. Generates chapters
    7. Formats and saves the novel as an EPUB file

    The function handles series integration if the novel is part of a series,
    and provides detailed progress information throughout the generation process.

    Returns:
        None
    """
    # Initialize logging system
    logger = init_logger("DEBUG")

    try:
        log_info("=== NOVEL GENERATION SESSION STARTED ===")
        log_info("Initializing main novel generation function")

        # Clear screen and display title
        clear_screen()
        display_title()

        log_debug("UI initialized, screen cleared and title displayed")

        console.print("[bold cyan]Let's create your novel![/bold cyan]")
        console.print("Please provide some basic information to get started.\n")

        # Get series information first
        log_debug("Getting series information from user")
        series_info = get_series_info()
        log_info("Series information collected", is_series=series_info.get("is_series", False))

        # Initialize series manager if needed
        series_manager = None
        book_number = None

        if series_info["is_series"]:
            if series_info["use_existing"]:
                # Load existing series
                series_title = series_info["selected_series"]
                series_manager = SeriesManager(series_title)
                console.print(f"[bold green]Loaded existing series: {series_title}[/bold green]")

                # Display series information
                display_series_info(series_manager)

                # This will be the next book in the series
                book_number = None  # Will be assigned when adding to series
            else:
                # Create new series
                series_title = series_info["series_title"]
                series_manager = SeriesManager(series_title)
                series_manager.update_metadata(
                    description=series_info["series_description"],
                    planned_books=series_info["planned_books"],
                    creator=os.environ.get("USERNAME", "Unknown")
                )
                console.print(f"[bold green]Created new series: {series_title}[/bold green]")

                # Display series information
                display_series_info(series_manager)

                # This will be the first book in the series
                book_number = None  # Will be assigned when adding to series

        # Get novel information from user
        log_debug("Getting novel information from user")
        novel_info = get_novel_info(series_info)
        log_info("Novel information collected",
                title=novel_info.get("title", "Unknown"),
                genre=novel_info.get("genre", "Unknown"),
                target_audience=novel_info.get("target_audience", "Unknown"))

        # Create output directory early
        output_dir = create_output_directory(
            novel_info["title"],
            series_manager=series_manager,
            book_number=book_number
        )

        # Ensure output directory uses forward slashes for consistency
        output_dir = output_dir.replace('\\', '/')

        # Initialize novel generator with output directory for memory files
        generator = NovelGenerator()
        memory_manager = generator.initialize_novel(
            title=novel_info["title"],
            author=novel_info["author"],
            description=novel_info["description"],
            genre=novel_info["genre"],
            target_audience=novel_info["target_audience"],
            output_dir=output_dir,
            series_manager=series_manager,
            book_number=book_number
        )

        # Get custom generation options
        generation_options = get_custom_generation_options(novel_info["genre"])

        # Set generation options
        generator.set_generation_options(generation_options)

        # Confirm generation
        if not confirm_generation():
            console.print("[bold yellow]Novel generation cancelled.[/bold yellow]")
            return

        # Check API connection and network status before starting
        console.print("[bold cyan]Checking API connection and network status...[/bold cyan]")

        # Initialize network resilience system
        try:
            from src.utils.network_resilience import get_network_manager
            network_manager = get_network_manager()

            # Force a connectivity check
            is_connected = network_manager.force_connectivity_check()
            if not is_connected:
                console.print("[bold yellow]⚠️ Network connectivity issues detected[/bold yellow]")
                console.print("[yellow]The system will use enhanced retry logic and queue failed requests[/yellow]")
            else:
                console.print("[bold green]✅ Network connection is stable[/bold green]")
        except Exception as e:
            console.print(f"[yellow]Warning: Could not initialize network resilience: {e}[/yellow]")

        api_status = generator.gemini.check_api_connection(check_all_keys=True)

        if not api_status["success"]:
            console.print("[bold red]Error: Unable to connect to the Gemini API.[/bold red]")
            console.print("[yellow]This could be due to network issues or API key problems.[/yellow]")
            console.print("[yellow]The system will automatically retry when network connectivity improves.[/yellow]")

            # Show network troubleshooting tips
            console.print("\n[bold cyan]💡 Troubleshooting Tips:[/bold cyan]")
            console.print("• Check your internet connection")
            console.print("• Verify your API keys are correct")
            console.print("• Try moving closer to your WiFi router")
            console.print("• Wait a few minutes and try again")
            return

        # Display API key information
        console.print(f"[bold green]✓[/bold green] API connection successful!")
        console.print(f"[bold cyan]Active API keys:[/bold cyan] {api_status['active_keys']}")
        console.print(f"[bold cyan]Working API keys:[/bold cyan] {api_status['working_keys']}")

        # If we have multiple keys, show that we're using key rotation
        if api_status['active_keys'] > 1:
            console.print("[bold green]Multiple API keys detected - will automatically rotate keys if rate limits are encountered.[/bold green]")

        # Start the generation timer
        generation_timer.start()
        console.print("\n[bold cyan]Generation started![/bold cyan]")
        console.print(f"[dim]Started: {generation_timer.get_start_datetime()}[/dim]", justify="right")

        # Automatic fictional author selection and enhancement
        log_info("Starting automatic fictional author selection", genre=novel_info["genre"])
        console.print("[bold cyan]Automatically selecting fictional author...[/bold cyan]")

        # Initialize writer profile manager for automatic selection
        from src.utils.writer_profile_manager import WriterProfileManager
        profile_manager = WriterProfileManager()

        # Get generation options for enhancement
        themes = generation_options.get('themes', []) if generation_options else []
        writing_style = generation_options.get('writing_style') if generation_options else None
        target_length = generation_options.get('target_length') if generation_options else None

        # Automatically select and enhance fictional author profile
        writer_profile = profile_manager.get_auto_selected_profile_for_book(
            genre=novel_info["genre"],
            themes=themes,
            writing_style=writing_style,
            target_length=target_length
        )

        if writer_profile:
            author_name = writer_profile.get("name", "Unknown Author")
            console.print(f"[bold green]✓[/bold green] Selected fictional author: [bold cyan]{author_name}[/bold cyan]")

            # Update the novel_info with the selected fictional author
            novel_info["author"] = author_name

            # Check if profile was enhanced
            if "_enhancement" in writer_profile:
                console.print("[bold green]Profile enhanced with AI for this specific book")

            # Log the automatic selection
            log_info("Fictional author automatically selected",
                    author=author_name,
                    genre=novel_info["genre"],
                    enhanced=bool("_enhancement" in writer_profile))
        else:
            # Fallback to traditional generation if no fictional author available
            console.print("[bold yellow]No fictional author available, generating custom profile...")
            try:
                writer_profile = generator.generate_writer_profile()
                log_info("Custom writer profile generated as fallback", profile_length=len(writer_profile) if writer_profile else 0)
                console.print("[bold green]✓[/bold green] Custom writer profile generated successfully")
            except Exception as e:
                log_error("Failed to generate fallback writer profile", exception=e)
                raise

        # Generate novel outline
        log_info("Starting novel outline generation", genre=novel_info["genre"])
        console.print("[bold cyan]Generating novel outline...[/bold cyan]")
        try:
            chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)
            log_info("Novel outline generation completed",
                    chapter_count=chapter_count,
                    outlines_length=len(chapter_outlines) if chapter_outlines else 0)
        except Exception as e:
            log_error("Failed to generate novel outline", exception=e)
            raise

        # Check if we have a valid chapter count
        if chapter_count == 0 or not chapter_outlines:
            log_error("Invalid novel outline generated",
                     chapter_count=chapter_count,
                     has_outlines=bool(chapter_outlines),
                     outlines_length=len(chapter_outlines) if chapter_outlines else 0)
            console.print("[bold red]Failed to generate a proper novel outline.[/bold red]")
            console.print("[bold yellow]Please try again with more specific details about your novel.[/bold yellow]")
            return

        log_info("Novel outline validation passed", chapter_count=chapter_count)
        console.print(f"[bold green]✓[/bold green] Novel outline with {chapter_count} chapters generated successfully")

        # Generate characters only for content types that need them
        characters = []
        if should_generate_characters(novel_info["genre"]):
            console.print("[bold cyan]Generating characters...[/bold cyan]")
            characters = generator.generate_characters()
            console.print(f"[bold green]✓[/bold green] {len(characters)} characters generated successfully")
        else:
            console.print(f"[bold yellow]Skipping character generation (not needed for {novel_info['genre']})")
            # Create empty character list for non-fiction and special formats
            characters = []

        # Confirm generation again after seeing outline and characters
        if not confirm_generation():
            console.print("[bold yellow]Novel generation cancelled.[/bold yellow]")
            return

        # Generate chapters
        console.print("\n[bold cyan]Generating and enhancing chapters...[/bold cyan]")
        chapters = []

        # Start the generation timer
        generation_timer.start()
        start_time = datetime.datetime.now()

        # Create a dictionary to store word counts
        chapter_word_counts = {}

        # Create a live display for the table
        from rich.live import Live

        # Create a function to generate the progress display
        def generate_chapter_display():
            # Calculate elapsed time - force update every second
            current_time = datetime.datetime.now()
            elapsed = current_time - start_time
            elapsed_str = str(elapsed).split('.')[0]  # Remove microseconds

            # Create a more compact display for many chapters
            if chapter_count > 20:
                return generate_compact_progress(elapsed_str)
            else:
                return generate_table_progress(elapsed_str)

        def generate_compact_progress(elapsed_str):
            """Generate a compact progress display for many chapters."""
            from rich.panel import Panel
            from rich.text import Text

            # Calculate statistics
            completed = sum(1 for status in chapter_status.values() if "Completed" in status)
            generating = sum(1 for status in chapter_status.values() if "Generating" in status or "Enhancing" in status)
            errors = sum(1 for status in chapter_status.values() if "Error" in status)
            pending = chapter_count - completed - generating - errors

            total_words = sum(chapter_word_counts.values())

            # Create progress bar
            progress_percentage = (completed / chapter_count) * 100 if chapter_count > 0 else 0
            progress_bar_width = 40
            filled_width = int((progress_percentage / 100) * progress_bar_width)
            progress_bar = "█" * filled_width + "░" * (progress_bar_width - filled_width)

            # Create status summary
            status_text = Text()
            status_text.append(f"Progress: {completed}/{chapter_count} chapters ({progress_percentage:.1f}%)\n", style="bold cyan")
            status_text.append(f"[{progress_bar}]\n\n", style="green")
            status_text.append(f"✅ Completed: {completed}  ", style="green")
            status_text.append(f"⚡ Generating: {generating}  ", style="cyan")
            status_text.append(f"⏳ Pending: {pending}  ", style="yellow")
            if errors > 0:
                status_text.append(f"❌ Errors: {errors}", style="red")
            status_text.append(f"\n📝 Total Words: {total_words:,}")

            # Show current chapter details
            current_chapter = None
            for ch_num, status in chapter_status.items():
                if "Generating" in status or "Enhancing" in status:
                    current_chapter = ch_num
                    break

            if current_chapter:
                ch_title = "Chapter"
                if current_chapter <= len(chapter_outlines):
                    outline = chapter_outlines[current_chapter - 1]
                    if " - " in outline:
                        ch_title = outline.split(" - ")[0]
                    else:
                        ch_title = outline

                current_text = Text()
                current_text.append(f"\n🔄 Currently Working On:\n", style="bold yellow")
                current_text.append(f"Chapter {current_chapter}: {ch_title}\n", style="white")
                current_text.append(f"Status: {chapter_status[current_chapter]}", style="cyan")
                status_text.append(current_text)

            # Show recent completions (last 5)
            recent_completed = [ch for ch, status in chapter_status.items() if "Completed" in status]
            if recent_completed:
                recent = recent_completed[-5:]  # Last 5 completed
                recent_text = Text()
                recent_text.append(f"\n\n📚 Recently Completed:\n", style="bold green")
                for ch_num in recent:
                    ch_title = "Chapter"
                    if ch_num <= len(chapter_outlines):
                        outline = chapter_outlines[ch_num - 1]
                        if " - " in outline:
                            ch_title = outline.split(" - ")[0]
                        else:
                            ch_title = outline
                    words = chapter_word_counts.get(ch_num, 0)
                    recent_text.append(f"  ✅ Ch {ch_num}: {ch_title} ({words:,} words)\n", style="dim green")
                status_text.append(recent_text)

            return Panel(
                status_text,
                title=f"[bold cyan]Chapter Generation Progress[/bold cyan] - Elapsed: [bold yellow]{elapsed_str}[/bold yellow]",
                border_style="cyan",
                expand=False
            )

        def generate_table_progress(elapsed_str):
            """Generate traditional table progress for smaller chapter counts."""
            table = Table(box=box.ROUNDED)
            table.add_column("Chapter", style="cyan")
            table.add_column("Status", style="green")
            table.add_column("Word Count", style="yellow")

            # Add a title with timer
            table.title = f"[bold cyan]Chapter Generation Progress[/bold cyan] - Elapsed Time: [bold yellow]{elapsed_str}[/bold yellow]"

            for i in range(1, chapter_count + 1):
                ch_title = "Chapter"
                if i <= len(chapter_outlines):
                    outline = chapter_outlines[i - 1]
                    if " - " in outline:
                        ch_title = outline.split(" - ")[0]
                    else:
                        ch_title = outline

                # Get status and word count
                status = "Pending"
                word_count = chapter_word_counts.get(i, 0)

                if i in chapter_status:
                    status = chapter_status[i]

                table.add_row(f"{i}: {ch_title}", status, str(word_count))

            return table

        # Dictionary to track chapter status
        chapter_status = {}

        # Initialize all chapters as pending
        for i in range(1, chapter_count + 1):
            chapter_status[i] = "Pending"
            chapter_word_counts[i] = 0

        # Create the live display with higher refresh rate to ensure timer updates every second
        with Live(generate_chapter_display(), refresh_per_second=4, screen=True) as live:
            # Process one chapter at a time (generate, enhance, then move to next)

            # Create a function to update the timer during long operations
            def update_timer_during_operation():
                """Force update the timer display during long operations"""
                live.update(generate_chapter_display())

            for chapter_num in range(1, chapter_count + 1):
                # Get chapter title
                chapter_title = "Chapter"
                if chapter_num <= len(chapter_outlines):
                    outline = chapter_outlines[chapter_num - 1]
                    if " - " in outline:
                        chapter_title = outline.split(" - ")[0]
                    else:
                        chapter_title = outline

                # Update status to generating
                chapter_status[chapter_num] = "[bold cyan]Generating...[/bold cyan]"
                live.update(generate_chapter_display())

                try:
                    # Generate current chapter with periodic timer updates
                    start_gen = datetime.datetime.now()
                    current_chapter_text = generator.generate_chapter(chapter_num)
                    # Force timer update if generation took more than 2 seconds
                    if (datetime.datetime.now() - start_gen).total_seconds() > 2:
                        update_timer_during_operation()

                    # Update status to enhancing
                    chapter_status[chapter_num] = "[bold cyan]Enhancing...[/bold cyan]"
                    live.update(generate_chapter_display())



                    # Enhance the current chapter with periodic timer updates
                    start_enhance = datetime.datetime.now()
                    enhanced_text = generator.enhance_chapter(
                        current_chapter_text,
                        chapter_num,
                        chapter_title
                    )
                    # Force timer update if enhancement took more than 2 seconds
                    if (datetime.datetime.now() - start_enhance).total_seconds() > 2:
                        update_timer_during_operation()

                    # Add enhanced chapter to list
                    chapters.append({
                        "number": chapter_num,
                        "title": chapter_title,
                        "content": enhanced_text
                    })

                    # Calculate word count and store it in memory manager
                    word_count = len(enhanced_text.split())
                    chapter_word_counts[chapter_num] = word_count

                    # Add chapter summary to memory manager with word count
                    try:
                        memory_manager.add_chapter_summary(
                            chapter_num=chapter_num,
                            summary=f"Chapter {chapter_num}: {chapter_title}",
                            word_count=word_count
                        )
                    except Exception as e:
                        console.print(f"[yellow]Warning: Could not update memory manager: {e}[/yellow]")

                    # Update status to completed
                    chapter_status[chapter_num] = "[bold green]Completed[/bold green]"
                    live.update(generate_chapter_display())

                except json.JSONDecodeError as e:
                    console.print(f"[bold red]Error parsing JSON in chapter {chapter_num}: {e}[/bold red]")
                    console.print("[yellow]Attempting to continue with partial data...[/yellow]")

                    # Add placeholder chapter if needed
                    if len(chapters) < chapter_num:
                        chapters.append({
                            "number": chapter_num,
                            "title": chapter_title,
                            "content": f"Chapter {chapter_num}: {chapter_title}\n\n[Content generation failed due to technical issues]"
                        })

                    # Update status to error
                    chapter_status[chapter_num] = "[bold red]Error[/bold red]"
                    live.update(generate_chapter_display())

                except Exception as e:
                    console.print(f"[bold red]Error generating chapter {chapter_num}: {e}[/bold red]")

                    # Add placeholder chapter
                    chapters.append({
                        "number": chapter_num,
                        "title": chapter_title,
                        "content": f"Chapter {chapter_num}: {chapter_title}\n\n[Content generation failed due to technical issues]"
                    })

                    # Update status to error
                    chapter_status[chapter_num] = "[bold red]Error[/bold red]"
                    live.update(generate_chapter_display())

        console.print(f"[bold green]✓[/bold green] All {chapter_count} chapters generated and enhanced successfully")

        # Compile novel information
        novel = {
            "metadata": memory_manager.metadata,
            "writer_profile": writer_profile,
            "generation_options": generation_options,
            "outline": chapter_outlines,
            "characters": characters,
            "chapters": chapters,
            "word_count": memory_manager.structure["current_word_count"]
        }

        # Save novel as JSON
        save_novel_json(novel, output_dir)

        # Use smart cover selection (checks for existing covers first, then fallback)
        from src.utils.smart_cover_selector import get_smart_cover_for_epub
        cover_path = get_smart_cover_for_epub(novel, output_dir, auto_mode=False)

        # Format and save as EPUB with writer profile
        console.print("[bold cyan]Formatting EPUB with front/back matter...[/bold cyan]")
        formatter = EpubFormatter(novel, writer_profile=writer_profile)
        epub_path = formatter.save_epub(output_dir, cover_path, writer_profile)

        # Stop the timer
        generation_timer.stop()

        # Register content for quality tracking and offer feedback
        try:
            from src.quality.content_quality_system import quality_system, ContentMetadata
            from src.ui.feedback_system import feedback_ui
            import hashlib

            # Create content ID
            content_id = hashlib.md5(f"{novel_info['title']}_{datetime.now().isoformat()}".encode()).hexdigest()[:16]

            # Calculate total word count
            total_word_count = sum(len(chapter.get("content", "").split()) for chapter in chapters)

            # Register content metadata
            metadata = ContentMetadata(
                content_id=content_id,
                title=novel_info["title"],
                fictional_author=writer_profile.get("name", "Unknown Author"),
                genre=novel_info["genre"],
                themes=generation_options.get("themes", []) if generation_options else [],
                writing_style=generation_options.get("writing_style", "") if generation_options else "",
                target_length=generation_options.get("target_length", "") if generation_options else "",
                word_count=total_word_count,
                generation_time=generation_timer.elapsed_time,
                enhancement_used=bool("_enhancement" in writer_profile),
                timestamp=datetime.now()
            )

            quality_system.register_content(metadata)

            # Assess content quality
            console.print("[bold cyan]📊 Analyzing content quality...[/bold cyan]")
            full_content = "\n\n".join(chapter.get("content", "") for chapter in chapters)
            quality_assessment = quality_system.assess_content_quality(
                content_id=content_id,
                content=full_content,
                fictional_author=writer_profile.get("name", "Unknown Author"),
                genre=novel_info["genre"]
            )
            console.print("[bold green]✓[/bold green] Quality analysis completed")

            # Offer feedback collection
            console.print(f"\n[bold cyan]📝 Content Feedback[/bold cyan]")
            collect_feedback = questionary.confirm(
                "Would you like to provide feedback on this generated content?",
                default=True,
                style=custom_style
            ).ask()

            if collect_feedback:
                feedback_ui.collect_content_feedback(
                    content_id=content_id,
                    title=novel_info["title"],
                    fictional_author=writer_profile.get("name", "Unknown Author"),
                    genre=novel_info["genre"]
                )
            else:
                # Offer quick rating as alternative
                quick_rating = questionary.confirm(
                    "Would you like to give a quick 1-5 star rating?",
                    default=True,
                    style=custom_style
                ).ask()

                if quick_rating:
                    feedback_ui.quick_rating(content_id, novel_info["title"])

        except Exception as e:
            console.print(f"[yellow]Note: Quality tracking unavailable: {e}[/yellow]")

        # Display completion message with absolute path
        abs_path = os.path.abspath(epub_path)

        # Check if this is part of a series
        is_part_of_series = False
        series_title = None
        book_number = None

        if memory_manager.series_manager:
            is_part_of_series = True
            series_title = memory_manager.series_manager.series_title
            book_number = memory_manager.book_number

        display_generation_complete(
            abs_path,
            is_part_of_series=is_part_of_series,
            series_title=series_title,
            book_number=book_number
        )

    except KeyboardInterrupt:
        log_warning("Novel generation cancelled by user (KeyboardInterrupt)")
        console.print("\n[bold yellow]Novel generation cancelled by user.[/bold yellow]")
        close_logger()
        sys.exit(0)
    except Exception as e:
        log_critical("Fatal error during novel generation", exception=e)
        console.print(f"\n[bold red]Error: {str(e)}[/bold red]")
        console.print(f"\n[bold yellow]Check the log file for detailed error information: {get_logger().get_log_file_path()}[/bold yellow]")
        close_logger()
        sys.exit(1)
    finally:
        # Ensure logger is closed even if no exception occurs
        try:
            log_info("=== NOVEL GENERATION SESSION COMPLETED ===")
            close_logger()
        except:
            pass


def parse_args():
    """
    Parse command line arguments for the application.

    This function sets up the argument parser and defines the available
    command-line options for the Ebook Generator:

    --auto-series: Automatically generate a series without user interaction
    --series-menu: Open the series management menu directly

    Returns:
        argparse.Namespace: The parsed command-line arguments
    """
    import argparse
    parser = argparse.ArgumentParser(description="Ebook Generator System")
    parser.add_argument("--auto-series", action="store_true",
                       help="Auto-generate a complete series without user interaction")
    parser.add_argument("--series-menu", action="store_true",
                       help="Open the series management menu")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    if args.auto_series:
        auto_generate_series()
    elif args.series_menu and series_management_menu:
        series_management_menu()
    else:
        # Import book management menu
        try:
            from src.ui.book_menu import book_management_menu
        except ImportError:
            book_management_menu = None

        # Ask if user wants to use menus or the standard flow
        if series_management_menu or book_management_menu:
            clear_screen()
            display_title()

            console.print("[bold cyan]Welcome to NovelForge AI![/bold cyan]")
            console.print("You can generate a single novel, work with a series of novels, or manage your book library.\n")

            menu_choices = []
            if series_management_menu:
                menu_choices.append("Series Management Menu")
            if book_management_menu:
                menu_choices.append("Book Management Menu")
            menu_choices.extend([
                "Generate Single Book (Classic)",
                "Advanced Generation Options",
                "Content Quality & Feedback",
                "API Key Management",
                "Exit"
            ])

            selected_menu = questionary.select(
                "What would you like to do?",
                choices=menu_choices,
                style=custom_style
            ).ask()

            if selected_menu == "Series Management Menu":
                series_management_menu()
            elif selected_menu == "Book Management Menu":
                book_management_menu()
            elif selected_menu == "Generate Single Book (Classic)":
                try:
                    main()
                except Exception as e:
                    try:
                        log_critical("Uncaught exception in main menu", exception=e)
                        close_logger()
                    except:
                        pass
                    raise
            elif "Advanced Generation Options" in selected_menu:
                try:
                    from src.ui.advanced_generation_options import advanced_options
                    advanced_result = advanced_options.show_advanced_options_menu()

                    if advanced_result:
                        # Use the advanced options to generate a book
                        console.print(f"\n[bold green]Starting Advanced Generation![/bold green]")
                        try:
                            main_with_advanced_options(advanced_result)
                        except Exception as e:
                            try:
                                log_critical("Uncaught exception in advanced generation", exception=e)
                                close_logger()
                            except:
                                pass
                            raise
                except ImportError:
                    console.print("[red]Advanced generation options not available[/red]")
                except Exception as e:
                    console.print(f"[red]Error accessing advanced options: {e}[/red]")
            elif selected_menu == "Content Quality & Feedback":
                try:
                    from src.ui.feedback_system import feedback_ui
                    feedback_ui.feedback_menu()
                except ImportError:
                    console.print("[red]Feedback system not available[/red]")
                except Exception as e:
                    console.print(f"[red]Error accessing feedback system: {e}[/red]")
            elif selected_menu == "API Key Management":
                try:
                    from src.utils.api_key_manager import show_api_key_management_menu
                    show_api_key_management_menu()
                except ImportError:
                    console.print("[red]API Key Management system not available[/red]")
                except Exception as e:
                    console.print(f"[red]Error accessing API Key Management: {e}[/red]")
            elif selected_menu == "Exit":
                console.print("[bold cyan]Thank you for using NovelForge AI![/bold cyan]")
        else:
            try:
                main()
            except Exception as e:
                try:
                    log_critical("Uncaught exception in main", exception=e)
                    close_logger()
                except:
                    pass
                raise
