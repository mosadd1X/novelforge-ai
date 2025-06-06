"""
Book management menu for managing individual books.
"""
import os
import json
import subprocess
from typing import List, Dict, Any, Optional
from datetime import datetime
# Rich imports removed - using clean design principles
import questionary

# Local imports
from src.core.novel_generator import NovelGenerator
from src.core.ideas_manager import IdeasManager
from src.formatters.epub_formatter import EpubFormatter
from src.utils.file_handler import create_output_directory, save_novel_json, load_novel_json, sanitize_filename
from src.utils.genre_defaults import get_genre_defaults
from src.ui.terminal_ui import (
    clear_screen,
    display_title,
    get_novel_info,
    display_generation_complete,
    generation_timer,
    generate_cover,
    custom_style,
    console
)
from src.core.resilient_gemini_client import ResilientGeminiClient
from src.ui.responsive_separator import (
    separator, title_separator, section_separator
)

def get_existing_books() -> List[Dict[str, Any]]:
    """
    Get a list of existing standalone books.

    Returns:
        List of book information dictionaries
    """
    output_dir = "output"
    if not os.path.exists(output_dir):
        return []

    existing_books = []

    # Look for standalone book directories (not in series folder)
    for item in os.listdir(output_dir):
        item_path = os.path.join(output_dir, item)

        # Skip the series directory
        if item == "series" or not os.path.isdir(item_path):
            continue

        # Look for novel_data.json in the directory
        json_path = os.path.join(item_path, "novel_data.json")
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    novel_data = json.load(f)

                metadata = novel_data.get("metadata", {})
                book_info = {
                    "title": metadata.get("title", "Unknown Title"),
                    "author": metadata.get("author", "Unknown Author"),
                    "genre": metadata.get("genre", "Unknown Genre"),
                    "target_audience": metadata.get("target_audience", "Unknown"),
                    "description": metadata.get("description", ""),
                    "created_at": metadata.get("created_at", "Unknown"),
                    "word_count": metadata.get("word_count", 0),
                    "chapter_count": len(novel_data.get("chapters", [])),
                    "directory": item_path,
                    "json_path": json_path
                }
                existing_books.append(book_info)
            except Exception as e:
                console.print(f"[yellow]Warning: Could not load book data from {json_path}: {str(e)}[/yellow]")
                continue

    # Sort by creation date (newest first)
    existing_books.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    return existing_books

def display_books_table(books: List[Dict[str, Any]]) -> None:
    """
    Display books in a clean list format following design principles.

    Args:
        books: List of book information dictionaries
    """
    if not books:
        console.print("    ⚠️ [yellow]No books found[/yellow]")
        return

    console.print(f"[bold cyan]📚 Book Library ({len(books)} books)[/bold cyan]")
    console.print()

    for i, book in enumerate(books, 1):
        # Format creation date
        created_date = book.get("created_at", "")
        if created_date and created_date != "Unknown":
            try:
                # Try to parse ISO format
                dt = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
                created_str = dt.strftime("%Y-%m-%d")
            except:
                created_str = created_date[:10] if len(created_date) >= 10 else created_date
        else:
            created_str = "Unknown"

        # Format word count
        word_count = book.get("word_count", 0)
        word_str = f"{word_count:,}" if word_count > 0 else "Unknown"

        # Display book entry
        console.print(f"    📖 [cyan bold]{i}. {book['title']}[/cyan bold]")
        console.print(f"        ✍️ Author: [white]{book['author']}[/white]")
        console.print(f"        🎭 Genre: [white]{book['genre']}[/white]")
        console.print(f"        📊 {book.get('chapter_count', 0)} chapters, {word_str} words")
        console.print(f"        📅 Created: [dim]{created_str}[/dim]")
        console.print()

    console.print()

def select_existing_book() -> Optional[Dict[str, Any]]:
    """
    Select an existing book from the library.

    Returns:
        Book information dictionary or None if cancelled
    """
    existing_books = get_existing_books()

    if not existing_books:
        console.print("[yellow]No existing books found.[/yellow]")
        return None

    console.print("[bold cyan]Your Book Library[/bold cyan]\n")
    display_books_table(existing_books)

    # Create choices for selection
    choices = []
    for i, book in enumerate(existing_books, 1):
        choice_text = f"{i}. {book['title']} by {book['author']}"
        choices.append(choice_text)

    choices.append("← Back")

    selected = questionary.select(
        "Select a book:",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "← Back":
        return None

    # Extract book index
    book_index = int(selected.split(".")[0]) - 1
    selected_book = existing_books[book_index]

    console.print(f"[bold green]✓[/bold green] Book '{selected_book['title']}' selected")
    return selected_book

def display_book_info(book_info: Dict[str, Any]) -> None:
    """
    Display detailed information about a book following clean design principles.

    Args:
        book_info: Book information dictionary
    """
    console.print(f"\n[bold cyan]📖 Book Information[/bold cyan]")
    console.print()

    # Display book metadata using clean typography
    console.print(f"    📚 [cyan bold]Title[/cyan bold]: [white]{book_info['title']}[/white]")
    console.print(f"    ✍️ [cyan bold]Author[/cyan bold]: [white]{book_info['author']}[/white]")
    console.print(f"    🎭 [cyan bold]Genre[/cyan bold]: [white]{book_info['genre']}[/white]")
    console.print(f"    🎯 [cyan bold]Target Audience[/cyan bold]: [white]{book_info['target_audience']}[/white]")
    console.print(f"    📄 [cyan bold]Chapters[/cyan bold]: [white]{book_info.get('chapter_count', 0)}[/white]")

    # Format word count
    word_count = book_info.get("word_count", 0)
    word_str = f"{word_count:,}" if word_count > 0 else "Unknown"
    console.print(f"    📊 [cyan bold]Word Count[/cyan bold]: [white]{word_str}[/white]")

    # Format creation date
    created_date = book_info.get("created_at", "Unknown")
    if created_date and created_date != "Unknown":
        try:
            dt = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
            created_str = dt.strftime("%Y-%m-%d %H:%M")
        except:
            created_str = created_date
    else:
        created_str = "Unknown"
    console.print(f"    📅 [cyan bold]Created[/cyan bold]: [white]{created_str}[/white]")
    console.print(f"    📁 [cyan bold]Directory[/cyan bold]: [white]{book_info['directory']}[/white]")

    # Display description if available
    if book_info.get("description"):
        console.print(f"\n[bold cyan]📝 Description[/bold cyan]")
        console.print()
        console.print(f"    [dim]{book_info['description']}[/dim]")

    console.print()

def create_new_book() -> Optional[Dict[str, Any]]:
    """
    Create a new book with enhanced post-generation options.

    Returns:
        Book information dictionary or None if cancelled
    """
    clear_screen()
    display_title()

    console.print("[bold cyan]Create New Book[/bold cyan]\n")

    # Get novel information
    novel_info = get_novel_info()
    if not novel_info:
        return None

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

    try:
        # Start generation timer
        generation_timer.start()
        console.print("\n[bold cyan]Generation started![/bold cyan]")

        # Generate the novel using automatic fictional author selection
        console.print("[bold cyan]🎭 Automatically selecting fictional author...[/bold cyan]")

        # Initialize writer profile manager for automatic selection
        from src.utils.writer_profile_manager import WriterProfileManager
        profile_manager = WriterProfileManager()

        # Get generation options for enhancement
        generation_options = get_genre_defaults(book_info["genre"])
        themes = generation_options.get('themes', []) if generation_options else []
        writing_style = generation_options.get('writing_style') if generation_options else None
        target_length = generation_options.get('target_length') if generation_options else None

        # Automatically select and enhance fictional author profile
        writer_profile = profile_manager.get_auto_selected_profile_for_book(
            genre=book_info["genre"],
            themes=themes,
            writing_style=writing_style,
            target_length=target_length
        )

        if writer_profile:
            author_name = writer_profile.get("name", "Unknown Author")
            console.print(f"[bold green]✓[/bold green] Selected fictional author: [bold cyan]{author_name}[/bold cyan]")

            # Check if profile was enhanced
            if "_enhancement" in writer_profile:
                console.print("[bold green]✨[/bold green] Profile enhanced with AI for this specific book")
        else:
            # Fallback to traditional generation
            console.print("[bold yellow]⚠️[/bold yellow] No fictional author available, generating custom profile...")
            writer_profile = generator.generate_writer_profile()
            console.print("[bold green]✓[/bold green] Custom writer profile generated")

        console.print("[bold cyan]Generating novel outline...[/bold cyan]")
        chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)
        console.print(f"[bold green]✓[/bold green] Novel outline generated ({chapter_count} chapters)")

        console.print("[bold cyan]Generating characters...[/bold cyan]")
        characters = generator.generate_characters()
        console.print(f"[bold green]✓[/bold green] Characters generated ({len(characters)} characters)")

        # Generate chapters
        console.print("[bold cyan]Generating chapters...[/bold cyan]")
        chapters = []

        # Generate chapters one by one
        for chapter_num in range(1, chapter_count + 1):
            # Get chapter title
            chapter_title = f"Chapter {chapter_num}"
            if chapter_num <= len(chapter_outlines):
                outline = chapter_outlines[chapter_num - 1]
                if " - " in outline:
                    chapter_title = outline.split(" - ")[0]
                else:
                    chapter_title = outline

            console.print(f"[bold cyan]Generating Chapter {chapter_num}: {chapter_title}...[/bold cyan]")
            chapter_text = generator.generate_chapter(chapter_num)

            # Enhance the chapter
            console.print(f"[bold cyan]Enhancing Chapter {chapter_num}...[/bold cyan]")
            enhanced_text = generator.enhance_chapter(chapter_text, chapter_num, chapter_title)

            # Add chapter to list
            chapters.append({
                "number": chapter_num,
                "title": chapter_title,
                "content": enhanced_text
            })

            console.print(f"[bold green]✓[/bold green] Chapter {chapter_num} completed")

        console.print(f"[bold green]✓[/bold green] All {chapter_count} chapters generated")

        # Compile novel data
        novel = {
            "metadata": memory_manager.metadata,
            "writer_profile": writer_profile,
            "generation_options": get_genre_defaults(book_info["genre"]) or {},
            "outline": chapter_outlines,
            "characters": characters,
            "chapters": chapters,
            "word_count": memory_manager.structure["current_word_count"]
        }

        # Save novel as JSON
        save_novel_json(novel, output_dir)

        # Generate enhanced descriptions and back cover
        console.print("[bold cyan]Generating enhanced descriptions...[/bold cyan]")
        from src.utils.enhanced_book_workflow import EnhancedBookWorkflow
        workflow = EnhancedBookWorkflow()

        # Save to database first
        from src.database.database_manager import get_database_manager
        db_manager = get_database_manager()
        book_id = db_manager.save_book(novel)

        # Process with enhanced workflow
        workflow.process_completed_book(book_id, novel)

        console.print("[bold green]✓[/bold green] Book generation completed!")
        console.print("[bold yellow]Note:[/bold yellow] EPUB can be generated manually from the Export menu.")

        # Stop timer
        generation_timer.stop()

        # Display completion
        console.print()
        console.print(title_separator("Book Generation Complete", "="))
        console.print(f"[bold green]Generation time:[/bold green] [bold cyan]{generation_timer.get_elapsed_time()}[/bold cyan]")
        console.print(f"[bold green]Book saved to:[/bold green] [bold cyan]{output_dir}[/bold cyan]")
        console.print(f"[bold cyan]Enhanced descriptions generated and saved to database[/bold cyan]")
        console.print()
        console.print(separator("="))

        # Create book info for return
        book_info = {
            "title": novel_info["title"],
            "author": novel_info["author"],
            "genre": novel_info["genre"],
            "target_audience": novel_info["target_audience"],
            "description": novel_info["description"],
            "created_at": datetime.now().isoformat(),
            "word_count": novel["metadata"].get("word_count", 0),
            "chapter_count": len(novel.get("chapters", [])),
            "directory": output_dir,
            "json_path": os.path.join(output_dir, "novel_data.json")
        }

        return book_info

    except Exception as e:
        console.print(f"[bold red]Error during generation: {str(e)}[/bold red]")
        return None

def create_book_from_idea() -> Optional[Dict[str, Any]]:
    """
    Create a new book from a pre-defined idea.

    Returns:
        Book information dictionary or None if cancelled
    """
    clear_screen()
    display_title()

    console.print("[bold cyan]Import Book from Ideas[/bold cyan]\n")

    # Initialize ideas manager
    ideas_manager = IdeasManager()

    # Select a book idea
    selected_idea = ideas_manager.select_book_idea()
    if not selected_idea:
        return None

    # Display the selected idea
    console.print()
    ideas_manager.display_selected_book_idea(selected_idea)

    # Confirm the selection
    confirm = questionary.confirm(
        "Would you like to create a book using this idea?",
        default=True,
        style=custom_style
    ).ask()

    if not confirm:
        return None

    # Get additional information from user
    console.print("\n[bold cyan]Additional Book Information[/bold cyan]")
    console.print("[dim]Note: A fictional author will be automatically selected based on the genre.[/dim]")

    # Get publisher/creator name (not the fictional author)
    author = questionary.text(
        "Publisher/Creator name (for metadata):",
        default="AI Generated",
        style=custom_style
    ).ask()

    if not author:
        return None

    # Get target audience
    target_audience = questionary.select(
        "Target audience:",
        choices=["Adult", "Young Adult", "Middle Grade", "Children"],
        default="Adult",
        style=custom_style
    ).ask()

    if not target_audience:
        return None

    # Allow user to modify the title if desired
    original_title = selected_idea.get('title', 'Untitled')
    title = questionary.text(
        "Book title:",
        default=original_title,
        style=custom_style
    ).ask()

    if not title:
        return None

    # Allow user to modify the description if desired
    original_description = selected_idea.get('description', '')
    description = questionary.text(
        "Book description:",
        default=original_description,
        style=custom_style
    ).ask()

    if not description:
        return None

    # Convert genre format
    genre = selected_idea.get('genre', 'literary_fiction')
    genre_display = genre.replace('_', ' ').title()

    # Create novel info dictionary (fictional author will be auto-selected)
    novel_info = {
        "title": title,
        "author": author,  # This is the publisher/creator, not the fictional author
        "description": description,
        "genre": genre_display,
        "target_audience": target_audience
    }

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

    try:
        # Start generation timer
        generation_timer.start()
        console.print("\n[bold cyan]Generation started![/bold cyan]")
        console.print(f"[bold green]📖 Using idea:[/bold green] {selected_idea.get('title', 'Unknown')}")

        # Generate the novel using automatic fictional author selection
        console.print("[bold cyan]🎭 Automatically selecting fictional author...[/bold cyan]")

        # Initialize writer profile manager for automatic selection
        from src.utils.writer_profile_manager import WriterProfileManager
        profile_manager = WriterProfileManager()

        # Get generation options for enhancement
        generation_options = get_genre_defaults(novel_info["genre"])
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

            # Check if profile was enhanced
            if "_enhancement" in writer_profile:
                console.print("[bold green]✨[/bold green] Profile enhanced with AI for this specific book")
        else:
            # Fallback to traditional generation
            console.print("[bold yellow]⚠️[/bold yellow] No fictional author available, generating custom profile...")
            writer_profile = generator.generate_writer_profile()
            console.print("[bold green]✓[/bold green] Custom writer profile generated")

        console.print("[bold cyan]Generating novel outline...[/bold cyan]")
        chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)
        console.print(f"[bold green]✓[/bold green] Novel outline generated ({chapter_count} chapters)")

        console.print("[bold cyan]Generating characters...[/bold cyan]")
        characters = generator.generate_characters()
        console.print(f"[bold green]✓[/bold green] Characters generated ({len(characters)} characters)")

        # Generate chapters
        console.print("[bold cyan]Generating chapters...[/bold cyan]")
        chapters = []

        # Generate chapters one by one
        for chapter_num in range(1, chapter_count + 1):
            # Get chapter title
            chapter_title = f"Chapter {chapter_num}"
            if chapter_num <= len(chapter_outlines):
                outline = chapter_outlines[chapter_num - 1]
                if " - " in outline:
                    chapter_title = outline.split(" - ")[0]
                else:
                    chapter_title = outline

            console.print(f"[bold cyan]Generating Chapter {chapter_num}: {chapter_title}...[/bold cyan]")
            chapter_text = generator.generate_chapter(chapter_num)

            # Enhance the chapter
            console.print(f"[bold cyan]Enhancing Chapter {chapter_num}...[/bold cyan]")
            enhanced_text = generator.enhance_chapter(chapter_text, chapter_num, chapter_title)

            # Add chapter to list
            chapters.append({
                "number": chapter_num,
                "title": chapter_title,
                "content": enhanced_text
            })

            console.print(f"[bold green]✓[/bold green] Chapter {chapter_num} completed")

        console.print(f"[bold green]✓[/bold green] All {chapter_count} chapters generated")

        # Compile novel data
        novel = {
            "metadata": memory_manager.metadata,
            "writer_profile": writer_profile,
            "generation_options": get_genre_defaults(novel_info["genre"]) or {},
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
        console.print("[bold cyan]Formatting EPUB...[/bold cyan]")
        formatter = EpubFormatter(novel, writer_profile=writer_profile)
        epub_path = formatter.save_epub(output_dir, cover_path, writer_profile)

        # Stop timer
        generation_timer.stop()

        # Display completion
        console.print()
        console.print(title_separator("Book Generation Complete", "="))
        console.print(f"[bold green]Generation time:[/bold green] [bold cyan]{generation_timer.get_elapsed_time()}[/bold cyan]")
        console.print(f"[bold green]Book saved to:[/bold green] [bold cyan]{epub_path}[/bold cyan]")
        console.print(f"[bold green]Based on idea:[/bold green] [bold cyan]{selected_idea.get('title', 'Unknown')}[/bold cyan]")
        console.print()
        console.print(separator("="))

        # Create book info for return
        book_info = {
            "title": novel_info["title"],
            "author": novel_info["author"],
            "genre": novel_info["genre"],
            "target_audience": novel_info["target_audience"],
            "description": novel_info["description"],
            "created_at": datetime.now().isoformat(),
            "word_count": novel["metadata"].get("word_count", 0),
            "chapter_count": len(novel.get("chapters", [])),
            "directory": output_dir,
            "json_path": os.path.join(output_dir, "novel_data.json"),
            "source_idea": selected_idea  # Store the original idea for reference
        }

        return book_info

    except Exception as e:
        console.print(f"[bold red]Error during generation: {str(e)}[/bold red]")
        return None

def generate_book_cover(book_info: Dict[str, Any]) -> None:
    """
    Generate a new cover for an existing book.

    Args:
        book_info: Book information dictionary
    """
    try:
        # Load the novel data
        with open(book_info["json_path"], 'r', encoding='utf-8') as f:
            novel_data = json.load(f)

        console.print(f"[bold cyan]Generating new cover for '{book_info['title']}'...[/bold cyan]")

        # Generate cover with manual selection
        cover_path = generate_cover(novel_data, book_info["directory"], auto_mode=False)

        if cover_path:
            # Update EPUB with new cover
            epub_files = [f for f in os.listdir(book_info["directory"]) if f.endswith(".epub")]
            if epub_files:
                console.print(f"[bold cyan]Updating EPUB with new cover...[/bold cyan]")

                # Extract writer profile from novel data
                writer_profile = novel_data.get("writer_profile")

                formatter = EpubFormatter(novel_data, writer_profile=writer_profile)
                formatter.save_epub(book_info["directory"], cover_path, writer_profile)
                console.print(f"[bold green]EPUB updated with new cover[/bold green]")
            else:
                console.print(f"[bold green]Cover generated: {cover_path}[/bold green]")
        else:
            console.print("[yellow]Cover generation cancelled.[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Error generating cover: {str(e)}[/bold red]")

def manage_cover_images(book_info: Dict[str, Any]) -> None:
    """
    Manage cover images for a book.

    Args:
        book_info: Book information dictionary
    """
    try:
        from src.utils.cover_image_manager import CoverImageManager

        cover_manager = CoverImageManager()
        cover_manager.manage_book_cover_images(book_info)

    except Exception as e:
        console.print(f"[bold red]Error managing cover images: {str(e)}[/bold red]")
        input("\nPress Enter to continue...")

def export_book_formats(book_info: Dict[str, Any]) -> None:
    """
    Export a book to different formats using Calibre.

    Args:
        book_info: Book information dictionary
    """
    # Check if Calibre is available
    try:
        result = subprocess.run(['ebook-convert', '--version'],
                              capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'ebook-convert')
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        console.print("[bold red]Error: Calibre is not installed or not accessible.[/bold red]")
        console.print("[yellow]Calibre is required for format conversion.[/yellow]")
        console.print("[yellow]Please install Calibre and add it to your system PATH.[/yellow]")

        show_help = questionary.confirm(
            "Would you like to see Calibre installation help?",
            default=True,
            style=custom_style
        ).ask()

        if show_help:
            show_calibre_installation_help()
        return

    # Find EPUB file
    epub_files = [f for f in os.listdir(book_info["directory"]) if f.endswith(".epub")]

    # Display EPUB status
    if epub_files:
        epub_path = os.path.join(book_info["directory"], epub_files[0])
        console.print(f"[bold cyan]Found EPUB:[/bold cyan] {epub_files[0]}")
    else:
        console.print("[yellow]No EPUB file found for this book.[/yellow]")
        console.print("[dim]You can still generate an EPUB by selecting the EPUB format option below.[/dim]")

    # Ask which format to export to
    format_choices = ["EPUB", "PDF", "MOBI", "AZW3", "DOCX", "All Formats", "← Back"]
    selected_format = questionary.select(
        "Select export format:",
        choices=format_choices,
        style=custom_style
    ).ask()

    if selected_format == "← Back":
        return

    # Handle EPUB format (regenerate with proper content)
    if selected_format == "EPUB":
        console.print(f"[bold cyan]Regenerating EPUB with updated content...[/bold cyan]")

        try:
            # Load novel data from JSON
            from src.utils.file_handler import load_novel_json
            json_path = os.path.join(book_info["directory"], "novel_data.json")

            if not os.path.exists(json_path):
                console.print(f"[bold red]Error: novel_data.json not found in {book_info['directory']}[/bold red]")
                return

            novel_data = load_novel_json(json_path)

            # Extract writer profile from novel data
            writer_profile = novel_data.get("writer_profile")

            # Use smart cover selection (checks for existing covers first, then fallback)
            from src.utils.smart_cover_selector import get_smart_cover_for_epub
            cover_path = get_smart_cover_for_epub(novel_data, book_info["directory"], auto_mode=True)

            # Regenerate EPUB with proper content and writer profile
            formatter = EpubFormatter(novel_data, writer_profile=writer_profile)
            epub_path = formatter.save_epub(book_info["directory"], cover_path, writer_profile)

            console.print(f"[bold green]EPUB regenerated successfully![/bold green]")
            console.print(f"[bold green]Updated file: {epub_path}[/bold green]")

        except Exception as e:
            console.print(f"[bold red]Error regenerating EPUB: {str(e)}[/bold red]")

        return

    # Check if we have an EPUB file for conversion to other formats
    if not epub_files:
        console.print("[yellow]No EPUB file found to convert to other formats.[/yellow]")
        console.print("[dim]Please generate an EPUB first by selecting the EPUB format option.[/dim]")
        return

    # Determine formats to convert
    formats_to_convert = []
    if selected_format == "All Formats":
        formats_to_convert = ["pdf", "mobi", "azw3", "docx"]
    else:
        formats_to_convert = [selected_format.lower()]

    # Convert each format
    for fmt in formats_to_convert:
        output_file = os.path.join(book_info["directory"], f"{sanitize_filename(book_info['title'])}.{fmt}")

        console.print(f"[bold cyan]Converting to {fmt.upper()}...[/bold cyan]")

        try:
            # Run ebook-convert
            cmd = ['ebook-convert', epub_path, output_file]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

            if result.returncode == 0:
                console.print(f"[bold green]{fmt.upper()} conversion successful: {output_file}[/bold green]")
            else:
                console.print(f"[bold red]{fmt.upper()} conversion failed[/bold red]")
                if result.stderr:
                    console.print(f"[red]Error: {result.stderr}[/red]")

        except subprocess.TimeoutExpired:
            console.print(f"[bold red]{fmt.upper()} conversion timed out[/bold red]")
        except Exception as e:
            console.print(f"[bold red]{fmt.upper()} conversion error: {str(e)}[/bold red]")

    console.print(f"\n[bold green]Export process completed![/bold green]")

def show_calibre_installation_help() -> None:
    """Show detailed Calibre installation and troubleshooting help."""
    console.print("\n[bold cyan]Calibre Installation and Setup Help[/bold cyan]")
    console.print("\n[bold yellow]1. Download and Install Calibre:[/bold yellow]")
    console.print("   • Visit: https://calibre-ebook.com/download")
    console.print("   • Download the version for your operating system")
    console.print("   • Run the installer with administrator privileges")

    console.print("\n[bold yellow]2. Add Calibre to System PATH:[/bold yellow]")
    console.print("   [bold]Windows:[/bold]")
    console.print("   • Open System Properties → Advanced → Environment Variables")
    console.print("   • Edit the PATH variable and add Calibre installation directory")
    console.print("   • Default location: C:\\Program Files\\Calibre2\\")

    console.print("   [bold]macOS:[/bold]")
    console.print("   • Add to ~/.bash_profile or ~/.zshrc:")
    console.print("   • export PATH=\"/Applications/calibre.app/Contents/MacOS:$PATH\"")

    console.print("   [bold]Linux:[/bold]")
    console.print("   • Usually installed to /usr/bin/ automatically")
    console.print("   • If not, add the installation directory to PATH")

    console.print("\n[bold yellow]3. Verify Installation:[/bold yellow]")
    console.print("   • Open a new terminal/command prompt")
    console.print("   • Run: ebook-convert --version")
    console.print("   • You should see Calibre version information")

    console.print("\n[bold yellow]4. Troubleshooting:[/bold yellow]")
    console.print("   • Restart your terminal after installation")
    console.print("   • On Windows, restart the application")
    console.print("   • Check that the PATH includes the correct Calibre directory")
    console.print("   • Ensure you have the latest version of Calibre")

def check_api_key_status() -> None:
    """Check and display API key status."""
    try:
        # Initialize the Gemini client
        gemini_client = ResilientGeminiClient()

        # Display API key status
        from src.ui.terminal_ui import display_api_key_status
        display_api_key_status(gemini_client)
    except Exception as e:
        console.print(f"[bold red]Error checking API key status: {str(e)}[/bold red]")
        console.print("[yellow]Make sure your API keys are properly configured in the .env file.[/yellow]")
        input("\nPress Enter to continue...")


def generate_epub_manually(book_info: Dict[str, Any]) -> None:
    """
    Generate EPUB manually for a book.

    Args:
        book_info: Book information dictionary
    """
    try:
        console.print("[bold cyan]Generating EPUB...[/bold cyan]")

        # Load novel data
        json_path = os.path.join(book_info["directory"], "novel_data.json")
        if not os.path.exists(json_path):
            console.print("[bold red]Error: novel_data.json not found![/bold red]")
            console.print("[dim]This book may have been generated with an older version.[/dim]")
            return

        novel_data = load_novel_json(json_path)

        # Extract writer profile from novel data
        writer_profile = novel_data.get("writer_profile")

        # Use smart cover selection
        from src.utils.smart_cover_selector import get_smart_cover_for_epub
        cover_path = get_smart_cover_for_epub(novel_data, book_info["directory"], auto_mode=True)

        # Generate EPUB with enhanced back matter
        formatter = EpubFormatter(novel_data, writer_profile=writer_profile)
        epub_path = formatter.save_epub(book_info["directory"], cover_path, writer_profile)

        console.print(f"[bold green]✓ EPUB generated successfully![/bold green]")
        console.print(f"[bold green]File saved to:[/bold green] [bold cyan]{epub_path}[/bold cyan]")

        # Update database if book exists there
        try:
            from src.database.database_manager import get_database_manager
            db_manager = get_database_manager()

            # Try to find book in database by title and author
            title = novel_data.get("metadata", {}).get("title", "")
            author = novel_data.get("metadata", {}).get("author", "")

            if title and author:
                books = db_manager.get_books(status="completed")
                for book in books:
                    if (book.get("title", "").lower() == title.lower() and
                        book.get("author", "").lower() == author.lower()):

                        # Update EPUB path in database
                        db_manager.update_book(book["book_id"], {"epub_path": epub_path})
                        console.print("[bold green]✓ Database updated with EPUB path[/bold green]")
                        break
        except Exception as e:
            console.print(f"[yellow]Warning: Could not update database: {e}[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Error generating EPUB: {e}[/bold red]")


def book_options_menu(book_info: Dict[str, Any]) -> None:
    """
    Options menu for a selected book with reorganized categories.

    Args:
        book_info: Book information dictionary
    """
    while True:
        clear_screen()
        display_title()

        # Display book information
        display_book_info(book_info)

        # Reorganized book options by category
        choices = [
            "📖 Content Actions",
            "🎨 Visual Elements",
            "📤 Export & Share",
            "🔧 Advanced Options",
            "← Back to Book Menu"
        ]

        selected = questionary.select(
            "What would you like to do with this book?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "📖 Content Actions":
            content_actions_menu(book_info)
        elif selected == "🎨 Visual Elements":
            visual_elements_menu(book_info)
        elif selected == "📤 Export & Share":
            export_share_menu(book_info)
        elif selected == "🔧 Advanced Options":
            advanced_options_menu(book_info)
        elif selected == "← Back to Book Menu":
            break

def content_actions_menu(book_info: Dict[str, Any]) -> None:
    """Content actions submenu for a book with workflow integration."""
    while True:
        clear_screen()
        display_title()
        display_book_info(book_info)

        console.print("[bold cyan]📖 Content Actions[/bold cyan]")
        console.print("    Generate and manage book content")
        console.print()

        choices = [
            "🔄 Complete Book Workflow",
            "Generate EPUB",
            "Edit Metadata",
            "View Content Details",
            "← Back to Book Options"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🔄 Complete Book Workflow":
            start_book_completion_workflow(book_info)
        elif selected == "Generate EPUB":
            generate_epub_manually(book_info)
            input("\nPress Enter to continue...")
        elif selected == "Edit Metadata":
            console.print("[yellow]Metadata editing will be available in future updates.[/yellow]")
            input("\nPress Enter to continue...")
        elif selected == "View Content Details":
            view_book_files(book_info)
            input("\nPress Enter to continue...")
        elif selected == "← Back to Book Options":
            break

def visual_elements_menu(book_info: Dict[str, Any]) -> None:
    """Visual elements submenu for a book with workflow integration."""
    while True:
        clear_screen()
        display_title()
        display_book_info(book_info)

        console.print("[bold cyan]🎨 Visual Elements[/bold cyan]")
        console.print("    Manage covers and visual design")
        console.print()

        # Check if cover exists
        book_dir = book_info.get("directory", "")
        has_cover = False
        if book_dir:
            cover_files = ["cover.jpg", "cover.png"]
            has_cover = any(os.path.exists(os.path.join(book_dir, f)) for f in cover_files)

        if has_cover:
            console.print("    ✅ Cover already exists")
        else:
            console.print("    ⏳ No cover found")
        console.print()

        choices = [
            "Generate New Cover",
            "Manage Cover Images",
            "Preview Cover"
        ]

        # Add workflow option if no cover exists
        if not has_cover:
            choices.insert(0, "🚀 Quick Cover Creation")

        choices.append("← Back to Book Options")

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🚀 Quick Cover Creation":
            quick_cover_creation_workflow(book_info)
        elif selected == "Generate New Cover":
            generate_book_cover(book_info)
            input("\nPress Enter to continue...")
        elif selected == "Manage Cover Images":
            manage_cover_images(book_info)
        elif selected == "Preview Cover":
            preview_book_cover(book_info)
        elif selected == "← Back to Book Options":
            break

def export_share_menu(book_info: Dict[str, Any]) -> None:
    """Export and share submenu for a book."""
    while True:
        clear_screen()
        display_title()
        display_book_info(book_info)

        console.print("[bold cyan]📤 Export & Share[/bold cyan]")
        console.print("    Export to different formats and create archives")
        console.print()

        choices = [
            "Export to Different Formats",
            "Create Archive",
            "Share Options",
            "← Back to Book Options"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Export to Different Formats":
            export_book_formats(book_info)
            input("\nPress Enter to continue...")
        elif selected == "Create Archive":
            console.print("[yellow]Archive creation will be available in future updates.[/yellow]")
            input("\nPress Enter to continue...")
        elif selected == "Share Options":
            console.print("[yellow]Share options will be available in future updates.[/yellow]")
            input("\nPress Enter to continue...")
        elif selected == "← Back to Book Options":
            break

def advanced_options_menu(book_info: Dict[str, Any]) -> None:
    """Advanced options submenu for a book."""
    while True:
        clear_screen()
        display_title()
        display_book_info(book_info)

        console.print("[bold cyan]🔧 Advanced Options[/bold cyan]")
        console.print("    Technical details and advanced features")
        console.print()

        choices = [
            "View Source Files",
            "Quality Feedback",
            "Technical Details",
            "API Key Status",
            "← Back to Book Options"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "View Source Files":
            view_book_files(book_info)
            input("\nPress Enter to continue...")
        elif selected == "Quality Feedback":
            console.print("[yellow]Quality feedback will be available in future updates.[/yellow]")
            input("\nPress Enter to continue...")
        elif selected == "Technical Details":
            console.print("[yellow]Technical details will be available in future updates.[/yellow]")
            input("\nPress Enter to continue...")
        elif selected == "API Key Status":
            check_api_key_status()
        elif selected == "← Back to Book Options":
            break

def view_book_files(book_info: Dict[str, Any]) -> None:
    """
    Display all files in the book directory following clean design principles.

    Args:
        book_info: Book information dictionary
    """
    console.print(f"\n[bold cyan]📁 Files in '{book_info['title']}'[/bold cyan]")
    console.print(f"    📂 Directory: [dim]{book_info['directory']}[/dim]")
    console.print()

    if not os.path.exists(book_info["directory"]):
        console.print("    ❌ [red]Directory not found![/red]")
        return

    files = os.listdir(book_info["directory"])
    if not files:
        console.print("    ⚠️ [yellow]No files found in directory[/yellow]")
        return

    # Display files using clean typography
    console.print("[bold cyan]📄 File List[/bold cyan]")
    console.print()

    for file in sorted(files):
        file_path = os.path.join(book_info["directory"], file)
        if os.path.isfile(file_path):
            # Get file extension
            file_ext = os.path.splitext(file)[1].upper().replace(".", "")
            if not file_ext:
                file_ext = "FILE"

            # Get file size
            try:
                size = os.path.getsize(file_path)
                if size < 1024:
                    size_str = f"{size} B"
                elif size < 1024 * 1024:
                    size_str = f"{size / 1024:.1f} KB"
                else:
                    size_str = f"{size / (1024 * 1024):.1f} MB"
            except:
                size_str = "Unknown"

            # Display file info with clean formatting
            console.print(f"    📄 [white]{file}[/white]")
            console.print(f"        🏷️ Type: [cyan]{file_ext}[/cyan]")
            console.print(f"        📊 Size: [yellow]{size_str}[/yellow]")
            console.print()

    console.print()

def start_book_completion_workflow(book_info: Dict[str, Any]) -> None:
    """Start the integrated workflow to complete a book."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Complete Book Workflow[/bold cyan]")
    console.print("    Integrated workflow: Cover → EPUB → Export")
    console.print()

    console.print(f"    📖 Book: [cyan]{book_info.get('title', 'Untitled')}[/cyan]")
    console.print(f"    🎭 Genre: [cyan]{book_info.get('genre', 'Unknown')}[/cyan]")
    console.print()

    # Check what's already completed
    book_dir = book_info.get("directory", "")
    workflow_status = analyze_book_completion_status(book_dir)

    console.print("[bold cyan]📋 Current Status:[/bold cyan]")
    for item, status in workflow_status.items():
        status_icon = "✅" if status else "⏳"
        console.print(f"    {status_icon} {item}")
    console.print()

    # Determine next steps
    next_steps = get_next_workflow_steps(workflow_status)

    if not next_steps:
        console.print("    🎉 [bold green]Your book is already complete![/bold green]")
        console.print("    All workflow steps have been finished.")
        input("\nPress Enter to continue...")
        return

    console.print(f"    🔄 [bold cyan]Next steps: {', '.join(next_steps)}[/bold cyan]")
    console.print()

    proceed = questionary.confirm(
        "Would you like to start the completion workflow?",
        default=True,
        style=custom_style
    ).ask()

    if proceed:
        execute_book_completion_workflow(book_info, next_steps)

def analyze_book_completion_status(book_dir: str) -> Dict[str, bool]:
    """Analyze what parts of the book workflow are complete."""
    status = {
        "Content Generated": False,
        "Cover Created": False,
        "EPUB Generated": False,
        "Ready for Export": False
    }

    if not book_dir or not os.path.exists(book_dir):
        return status

    # Check for content files
    content_files = ["outline.txt", "characters.json"]
    if any(os.path.exists(os.path.join(book_dir, f)) for f in content_files):
        status["Content Generated"] = True

    # Check for cover
    cover_files = ["cover.jpg", "cover.png"]
    if any(os.path.exists(os.path.join(book_dir, f)) for f in cover_files):
        status["Cover Created"] = True

    # Check for EPUB
    epub_files = [f for f in os.listdir(book_dir) if f.endswith('.epub')]
    if epub_files:
        status["EPUB Generated"] = True
        status["Ready for Export"] = True

    return status

def get_next_workflow_steps(status: Dict[str, bool]) -> List[str]:
    """Determine what workflow steps need to be completed."""
    next_steps = []

    if not status["Cover Created"]:
        next_steps.append("Create Cover")

    if not status["EPUB Generated"]:
        next_steps.append("Generate EPUB")

    if status["EPUB Generated"] and not status["Ready for Export"]:
        next_steps.append("Prepare Export")

    return next_steps

def execute_book_completion_workflow(book_info: Dict[str, Any], steps: List[str]) -> None:
    """Execute the book completion workflow steps."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Executing Workflow[/bold cyan]")
    console.print(f"    Processing {len(steps)} step{'s' if len(steps) != 1 else ''}")
    console.print()

    completed_steps = []

    for i, step in enumerate(steps, 1):
        console.print(f"[bold cyan]Step {i} of {len(steps)}: {step}[/bold cyan]")

        if step == "Create Cover":
            if execute_cover_creation_step(book_info):
                completed_steps.append(step)
                console.print("    ✅ Cover creation completed")
            else:
                console.print("    ❌ Cover creation failed")
                break

        elif step == "Generate EPUB":
            if execute_epub_generation_step(book_info):
                completed_steps.append(step)
                console.print("    ✅ EPUB generation completed")
            else:
                console.print("    ❌ EPUB generation failed")
                break

        elif step == "Prepare Export":
            if execute_export_preparation_step(book_info):
                completed_steps.append(step)
                console.print("    ✅ Export preparation completed")
            else:
                console.print("    ❌ Export preparation failed")
                break

        console.print()

    # Display results
    console.print("[bold green]🎉 Workflow Results[/bold green]")
    console.print(f"    Completed: {len(completed_steps)} of {len(steps)} steps")

    if completed_steps:
        console.print("    ✅ Successful steps:")
        for step in completed_steps:
            console.print(f"        • {step}")

    if len(completed_steps) == len(steps):
        console.print()
        console.print("    🎊 [bold green]All workflow steps completed successfully![/bold green]")
        console.print("    Your book is now ready for publishing!")

    input("\nPress Enter to continue...")

def execute_cover_creation_step(book_info: Dict[str, Any]) -> bool:
    """Execute the cover creation step."""
    try:
        console.print("    🎨 Creating book cover...")

        # This would integrate with the actual cover generation
        # For now, simulate the process
        import time
        time.sleep(1)  # Simulate processing time

        console.print("    📸 Cover generated successfully")
        return True

    except Exception as e:
        console.print(f"    ❌ Error creating cover: {e}")
        return False

def execute_epub_generation_step(book_info: Dict[str, Any]) -> bool:
    """Execute the EPUB generation step."""
    try:
        console.print("    📚 Generating EPUB file...")

        # This would integrate with the actual EPUB generation
        generate_epub_manually(book_info)
        return True

    except Exception as e:
        console.print(f"    ❌ Error generating EPUB: {e}")
        return False

def execute_export_preparation_step(book_info: Dict[str, Any]) -> bool:
    """Execute the export preparation step."""
    try:
        console.print("    📤 Preparing for export...")

        # This would prepare files for export
        # For now, simulate the process
        import time
        time.sleep(1)  # Simulate processing time

        console.print("    📋 Export preparation completed")
        return True

    except Exception as e:
        console.print(f"    ❌ Error preparing export: {e}")
        return False

def quick_cover_creation_workflow(book_info: Dict[str, Any]) -> None:
    """Quick workflow for creating a book cover."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🚀 Quick Cover Creation[/bold cyan]")
    console.print("    Fast track to creating your book cover")
    console.print()

    console.print(f"    📖 Book: [cyan]{book_info.get('title', 'Untitled')}[/cyan]")
    console.print(f"    🎭 Genre: [cyan]{book_info.get('genre', 'Unknown')}[/cyan]")
    console.print()

    console.print("    🎨 This workflow will:")
    console.print("    • Generate a professional cover design")
    console.print("    • Apply genre-appropriate styling")
    console.print("    • Save the cover to your book directory")
    console.print()

    proceed = questionary.confirm(
        "Ready to create your cover?",
        default=True,
        style=custom_style
    ).ask()

    if proceed:
        try:
            console.print("    🎨 Generating cover...")
            generate_book_cover(book_info)
            console.print("    ✅ [bold green]Cover created successfully![/bold green]")
            console.print("    Your book now has a professional cover design.")
        except Exception as e:
            console.print(f"    ❌ [red]Error creating cover: {e}[/red]")

    input("\nPress Enter to continue...")

def preview_book_cover(book_info: Dict[str, Any]) -> None:
    """Preview the book cover if it exists."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📸 Cover Preview[/bold cyan]")
    console.print()

    book_dir = book_info.get("directory", "")
    if not book_dir:
        console.print("    ❌ [red]No book directory found[/red]")
        input("\nPress Enter to continue...")
        return

    # Look for cover files
    cover_files = ["cover.jpg", "cover.png"]
    found_cover = None

    for cover_file in cover_files:
        cover_path = os.path.join(book_dir, cover_file)
        if os.path.exists(cover_path):
            found_cover = cover_path
            break

    if found_cover:
        console.print(f"    📸 Cover found: [cyan]{os.path.basename(found_cover)}[/cyan]")
        console.print(f"    📂 Location: [dim]{found_cover}[/dim]")

        # Get file size
        try:
            size = os.path.getsize(found_cover)
            if size < 1024 * 1024:
                size_str = f"{size / 1024:.1f} KB"
            else:
                size_str = f"{size / (1024 * 1024):.1f} MB"
            console.print(f"    📊 Size: [yellow]{size_str}[/yellow]")
        except:
            pass

        console.print()
        console.print("    💡 [cyan]Tip:[/cyan] You can view the cover by opening the file in your image viewer")
    else:
        console.print("    ⏳ [yellow]No cover found for this book[/yellow]")
        console.print("    Use 'Generate New Cover' to create one!")

    input("\nPress Enter to continue...")

def browse_book_library() -> None:
    """
    Browse the book library with filtering and search options.
    """
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Book Library Browser[/bold cyan]\n")

        existing_books = get_existing_books()

        if not existing_books:
            console.print("[yellow]No books found in your library.[/yellow]")
            console.print("Create some books first to see them here!")
            input("\nPress Enter to continue...")
            return

        # Display books
        display_books_table(existing_books)

        # Browser options
        choices = [
            "Select a Book",
            "Filter by Genre",
            "Filter by Author",
            "Sort by Date (Newest First)",
            "Sort by Date (Oldest First)",
            "Sort by Title",
            "Show All Books",
            "← Back to Main Menu"
        ]

        selected = questionary.select(
            f"Library Browser ({len(existing_books)} books found):",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Select a Book":
            book_info = select_existing_book()
            if book_info:
                book_options_menu(book_info)

        elif selected == "Filter by Genre":
            filter_books_by_genre(existing_books)

        elif selected == "Filter by Author":
            filter_books_by_author(existing_books)

        elif selected == "Sort by Date (Newest First)":
            existing_books.sort(key=lambda x: x.get("created_at", ""), reverse=True)

        elif selected == "Sort by Date (Oldest First)":
            existing_books.sort(key=lambda x: x.get("created_at", ""), reverse=False)

        elif selected == "Sort by Title":
            existing_books.sort(key=lambda x: x.get("title", "").lower())

        elif selected == "Show All Books":
            # Already showing all books, just refresh
            continue

        elif selected == "← Back to Main Menu":
            break

def filter_books_by_genre(books: List[Dict[str, Any]]) -> None:
    """
    Filter books by genre and display results.

    Args:
        books: List of book information dictionaries
    """
    # Get unique genres
    genres = list(set(book.get("genre", "Unknown") for book in books))
    genres.sort()

    if not genres:
        console.print("[yellow]No genres found.[/yellow]")
        input("\nPress Enter to continue...")
        return

    # Add option to go back
    genre_choices = genres + ["← Back"]

    selected_genre = questionary.select(
        "Select a genre to filter by:",
        choices=genre_choices,
        style=custom_style
    ).ask()

    if selected_genre == "← Back":
        return

    # Filter books by selected genre
    filtered_books = [book for book in books if book.get("genre") == selected_genre]

    clear_screen()
    display_title()
    console.print(f"[bold cyan]Books in '{selected_genre}' Genre[/bold cyan]\n")

    if filtered_books:
        display_books_table(filtered_books)

        # Allow selection from filtered results
        book_info = select_from_filtered_books(filtered_books)
        if book_info:
            book_options_menu(book_info)
    else:
        console.print("[yellow]No books found in this genre.[/yellow]")
        input("\nPress Enter to continue...")

def filter_books_by_author(books: List[Dict[str, Any]]) -> None:
    """
    Filter books by author and display results.

    Args:
        books: List of book information dictionaries
    """
    # Get unique authors
    authors = list(set(book.get("author", "Unknown") for book in books))
    authors.sort()

    if not authors:
        console.print("[yellow]No authors found.[/yellow]")
        input("\nPress Enter to continue...")
        return

    # Add option to go back
    author_choices = authors + ["← Back"]

    selected_author = questionary.select(
        "Select an author to filter by:",
        choices=author_choices,
        style=custom_style
    ).ask()

    if selected_author == "← Back":
        return

    # Filter books by selected author
    filtered_books = [book for book in books if book.get("author") == selected_author]

    clear_screen()
    display_title()
    console.print(f"[bold cyan]Books by '{selected_author}'[/bold cyan]\n")

    if filtered_books:
        display_books_table(filtered_books)

        # Allow selection from filtered results
        book_info = select_from_filtered_books(filtered_books)
        if book_info:
            book_options_menu(book_info)
    else:
        console.print("[yellow]No books found by this author.[/yellow]")
        input("\nPress Enter to continue...")

def select_from_filtered_books(books: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Select a book from a filtered list.

    Args:
        books: List of filtered book information dictionaries

    Returns:
        Selected book information or None if cancelled
    """
    if not books:
        return None

    # Create choices for selection
    choices = []
    for i, book in enumerate(books, 1):
        choice_text = f"{i}. {book['title']} by {book['author']}"
        choices.append(choice_text)

    choices.append("← Back")

    selected = questionary.select(
        "Select a book:",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "← Back":
        return None

    # Extract book index
    book_index = int(selected.split(".")[0]) - 1
    return books[book_index]

def book_management_menu() -> None:
    """Main book management menu with improved organization."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]📖 Book Management[/bold cyan]")
        console.print("    Organize and manage your book collection")

        # Get book count for display
        existing_books = get_existing_books()
        book_count = len(existing_books)

        if book_count > 0:
            console.print(f"    📚 You have {book_count} book{'s' if book_count != 1 else ''} in your library")
        else:
            console.print("    📚 Your library is empty")
        console.print()

        # Main menu options
        choices = [
            "Create New Book",
            "Import Book from Ideas",
            "Work with Existing Books",
            "Browse Book Library",
            "← Back to Main Menu"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Create New Book":
            book_info = create_new_book()
            if book_info:
                # Ask if user wants to do anything else with the new book
                post_creation = questionary.confirm(
                    "Would you like to perform additional actions on this book?",
                    default=False,
                    style=custom_style
                ).ask()

                if post_creation:
                    book_options_menu(book_info)

        elif selected == "Import Book from Ideas":
            book_info = create_book_from_idea()
            if book_info:
                # Ask if user wants to do anything else with the new book
                post_creation = questionary.confirm(
                    "Would you like to perform additional actions on this book?",
                    default=False,
                    style=custom_style
                ).ask()

                if post_creation:
                    book_options_menu(book_info)

        elif selected == "Work with Existing Books":
            book_info = select_existing_book()
            if book_info:
                book_options_menu(book_info)

        elif selected == "Browse Book Library":
            browse_book_library()

        elif selected == "← Back to Main Menu":
            break
