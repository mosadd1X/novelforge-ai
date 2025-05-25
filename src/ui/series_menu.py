"""
Interactive menu system for series management.
"""
import os
import json
import subprocess
from typing import Dict, List, Any, Optional
from rich.table import Table
from rich import box
import questionary

from src.core.series_manager import SeriesManager
from src.core.series_generator import SeriesGenerator
from src.core.ideas_manager import IdeasManager
from src.utils.file_handler import create_series_directory, sanitize_filename, zip_series_books, get_series_files
from src.formatters.epub_formatter import EpubFormatter
from src.utils.genre_defaults import get_all_genres
from src.ui.terminal_ui import (
    clear_screen,
    display_title,
    display_series_info,
    display_api_key_status,
    generation_timer,
    generate_cover,
    custom_style,
    console
)
from src.core.gemini_client import GeminiClient

def get_existing_series() -> List[str]:
    """
    Get a list of existing series.

    Returns:
        List of series names
    """
    series_dir = os.path.join("output", "series")
    os.makedirs(series_dir, exist_ok=True)

    existing_series = []
    for file in os.listdir(series_dir):
        if file.startswith("series_") and file.endswith(".json"):
            series_name = file[7:-5]  # Remove "series_" prefix and ".json" suffix
            series_name = series_name.replace("_", " ")
            existing_series.append(series_name)

    return existing_series

def create_new_series() -> SeriesManager:
    """
    Create a new series.

    Returns:
        SeriesManager instance
    """
    # Get series title
    series_title = questionary.text(
        "What is the title of your series?",
        validate=lambda text: len(text) > 0,
        style=custom_style
    ).ask()

    # Get series description
    series_description = questionary.text(
        "Provide a brief description of your series:",
        validate=lambda text: len(text) > 10,
        style=custom_style
    ).ask()

    # Get all available genres
    all_genres = get_all_genres()

    # Common genres to show in the main selection
    common_genres = [
        "Literary Fiction",
        "Commercial Fiction",
        "Mystery/Thriller",
        "Romance",
        "Contemporary Romance",
        "Fantasy",
        "Science Fiction",
        "Historical Fiction",
        "Horror",
        "Young Adult",
        "Middle Grade",
        "Children's Chapter Books",
        "Memoir",
        "Biography",
        "Self-Help",
        "Test",
        "Other (Search)"
    ]

    # Get genre
    genre = questionary.select(
        "Select a genre:",
        choices=common_genres,
        style=custom_style
    ).ask()

    # If other, show a searchable selection
    if genre == "Other (Search)":
        # Create a function to filter genres based on user input
        def genre_filter(text, genres):
            if not text:
                return []
            text = text.lower()
            return [g for g in genres if text in g.lower()]

        # Use autocomplete to allow searching through all genres
        genre = questionary.autocomplete(
            "Type to search for a genre:",
            choices=all_genres,
            match_middle=True,
            validate=lambda text: len(text) > 0 and (text in all_genres or text.title() in all_genres),
            style=custom_style
        ).ask()

    # Get target audience
    target_audience = questionary.select(
        "Select a target audience:",
        choices=[
            "Children (8-12)",
            "Middle Grade (10-14)",
            "Young Adult (12-18)",
            "New Adult (18-25)",
            "Adult (18+)",
            "All Ages"
        ],
        style=custom_style
    ).ask()

    # Get planned number of books
    planned_books = questionary.text(
        "How many books do you plan for this series? (Enter a number)",
        validate=lambda text: text.isdigit() and int(text) > 0,
        style=custom_style
    ).ask()

    # Author will be automatically selected based on genre and series requirements
    # This is now handled by the fictional author system during series generation
    author = "AI Author"  # Placeholder - will be replaced by fictional author during generation

    # Create series manager
    series_manager = SeriesManager(series_title)

    # Update series metadata
    series_manager.update_metadata(
        description=series_description,
        genre=genre,
        target_audience=target_audience,
        planned_books=int(planned_books),
        creator=author
    )

    # Get book information for each planned book
    books = []
    for i in range(1, int(planned_books) + 1):
        console.print(f"\n[bold cyan]Book {i} Information[/bold cyan]")

        # Get book title
        book_title = questionary.text(
            f"What is the title of Book {i}?",
            validate=lambda text: len(text) > 0,
            style=custom_style
        ).ask()

        # Get book description
        book_description = questionary.text(
            f"Provide a brief description of Book {i}:",
            validate=lambda text: len(text) > 10,
            style=custom_style
        ).ask()

        # Add book to list
        books.append({
            "title": book_title,
            "description": book_description,
            "author": author,
            "genre": genre,
            "target_audience": target_audience
        })

    # Store book templates
    series_manager.book_templates = books

    # Save series
    series_manager.save_series()

    console.print(f"[bold green]✓[/bold green] Series '{series_title}' created successfully with {planned_books} planned books")

    return series_manager

def create_series_from_idea() -> Optional[SeriesManager]:
    """
    Create a new series from a pre-defined idea.

    Returns:
        SeriesManager instance or None if cancelled
    """
    clear_screen()
    display_title()

    console.print("[bold cyan]Import Series from Ideas[/bold cyan]\n")

    # Initialize ideas manager
    ideas_manager = IdeasManager()

    # Select a series idea
    selected_idea = ideas_manager.select_series_idea()
    if not selected_idea:
        return None

    # Display the selected idea
    console.print()
    ideas_manager.display_selected_series_idea(selected_idea)

    # Confirm the selection
    confirm = questionary.confirm(
        "Would you like to create a series using this idea?",
        default=True,
        style=custom_style
    ).ask()

    if not confirm:
        return None

    # Get additional information from user
    console.print("\n[bold cyan]Additional Series Information[/bold cyan]")
    console.print("[dim]Note: Fictional authors will be automatically selected for each book based on the genre.[/dim]")

    # Get series creator/publisher name (not the fictional author)
    author = questionary.text(
        "Series Creator/Publisher name (for metadata):",
        default="AI Generated",
        style=custom_style
    ).ask()

    if not author:
        return None

    # Get target audience
    target_audience = questionary.select(
        "Target audience:",
        choices=[
            "Children (8-12)",
            "Middle Grade (10-14)",
            "Young Adult (12-18)",
            "New Adult (18-25)",
            "Adult (18+)",
            "All Ages"
        ],
        default="Adult (18+)",
        style=custom_style
    ).ask()

    if not target_audience:
        return None

    # Allow user to modify the series title if desired
    original_title = selected_idea.get('title', 'Untitled Series')
    series_title = questionary.text(
        "Series title:",
        default=original_title,
        style=custom_style
    ).ask()

    if not series_title:
        return None

    # Allow user to modify the series description if desired
    original_description = selected_idea.get('description', '')
    series_description = questionary.text(
        "Series description:",
        default=original_description,
        style=custom_style
    ).ask()

    if not series_description:
        return None

    # Convert genre format
    genre = selected_idea.get('genre', 'literary_fiction')
    genre_display = genre.replace('_', ' ').title()

    # Get book count from idea
    planned_books = selected_idea.get('book_count', len(selected_idea.get('books', [])))

    # Allow user to modify the book count if desired
    book_count_str = questionary.text(
        "Number of books in series:",
        default=str(planned_books),
        validate=lambda text: text.isdigit() and int(text) > 0,
        style=custom_style
    ).ask()

    if not book_count_str:
        return None

    planned_books = int(book_count_str)

    # Create series manager
    series_manager = SeriesManager(series_title)

    # Update series metadata
    series_manager.update_metadata(
        description=series_description,
        genre=genre_display,
        target_audience=target_audience,
        planned_books=planned_books,
        creator=author
    )

    # Get book information from the idea
    idea_books = selected_idea.get('books', [])
    books = []

    # Use books from idea if available, otherwise ask user for book details
    for i in range(planned_books):
        console.print(f"\n[bold cyan]Book {i+1} Information[/bold cyan]")

        if i < len(idea_books):
            # Use book from idea as default
            idea_book = idea_books[i]
            default_title = idea_book.get('title', f'Book {i+1}')
            default_description = idea_book.get('description', '')
        else:
            # No idea book available, use generic defaults
            default_title = f'Book {i+1}'
            default_description = ''

        # Get book title (with default from idea)
        book_title = questionary.text(
            f"Title for Book {i+1}:",
            default=default_title,
            style=custom_style
        ).ask()

        if not book_title:
            return None

        # Get book description (with default from idea)
        book_description = questionary.text(
            f"Description for Book {i+1}:",
            default=default_description,
            style=custom_style
        ).ask()

        if not book_description:
            return None

        # Add book to list (fictional author will be auto-selected during generation)
        books.append({
            "title": book_title,
            "description": book_description,
            "author": author,  # This is the series creator, not the fictional author
            "genre": genre_display,
            "target_audience": target_audience
        })

    # Store book templates
    series_manager.book_templates = books

    # Save series
    series_manager.save_series()

    console.print(f"[bold green]✓[/bold green] Series '{series_title}' created successfully with {planned_books} planned books")
    console.print(f"[bold green]✓ Based on idea:[/bold green] [bold cyan]{selected_idea.get('title', 'Unknown')}[/bold cyan]")

    return series_manager

def select_existing_series() -> Optional[SeriesManager]:
    """
    Select an existing series.

    Returns:
        SeriesManager instance or None if cancelled
    """
    existing_series = get_existing_series()

    if not existing_series:
        console.print("[yellow]No existing series found.[/yellow]")
        return None

    # Add a "Back" option
    choices = existing_series + ["← Back"]

    selected = questionary.select(
        "Select a series:",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "← Back":
        return None

    # Load the selected series
    series_manager = SeriesManager(selected)

    console.print(f"[bold green]✓[/bold green] Series '{selected}' loaded successfully")

    return series_manager

def auto_generate_series(series_manager: SeriesManager) -> None:
    """
    Auto-generate all books in a series.

    Args:
        series_manager: SeriesManager instance
    """
    # Initialize series generator
    series_generator = SeriesGenerator()

    # Get series metadata
    series_title = series_manager.metadata["title"]
    series_description = series_manager.metadata.get("description", "")
    genre = series_manager.metadata.get("genre", "")
    target_audience = series_manager.metadata.get("target_audience", "")
    planned_books = series_manager.metadata.get("planned_books", 1)
    author = series_manager.metadata.get("creator", "")

    # Initialize series in the generator
    series_generator.initialize_series(
        series_title=series_title,
        series_description=series_description,
        genre=genre,
        target_audience=target_audience,
        planned_books=planned_books,
        author=author
    )

    # Use book templates if available
    if hasattr(series_manager, "book_templates") and series_manager.book_templates:
        book_templates = series_manager.book_templates
    else:
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

def generate_book_by_book(series_manager: SeriesManager) -> None:
    """
    Generate books one by one in a series.

    Args:
        series_manager: SeriesManager instance
    """
    # Initialize series generator
    series_generator = SeriesGenerator()

    # Get series metadata
    series_title = series_manager.metadata["title"]
    series_description = series_manager.metadata.get("description", "")
    genre = series_manager.metadata.get("genre", "")
    target_audience = series_manager.metadata.get("target_audience", "")
    planned_books = series_manager.metadata.get("planned_books", 1)
    author = series_manager.metadata.get("creator", "")

    # Initialize series in the generator
    series_generator.initialize_series(
        series_title=series_title,
        series_description=series_description,
        genre=genre,
        target_audience=target_audience,
        planned_books=planned_books,
        author=author
    )

    # Use book templates if available
    if hasattr(series_manager, "book_templates") and series_manager.book_templates:
        book_templates = series_manager.book_templates
    else:
        # Generate series plan
        console.print("[bold cyan]Generating series plan...[/bold cyan]")
        book_templates = series_generator.generate_series_plan()
        console.print(f"[bold green]✓[/bold green] Series plan generated with {len(book_templates)} books")

    # Display books to generate
    console.print("\n[bold cyan]Books to Generate:[/bold cyan]")
    for i, book in enumerate(book_templates, 1):
        console.print(f"[bold green]Book {i}:[/bold green] {book.get('title', f'Book {i}')}")

    # Ask which book to generate
    book_choices = [f"Book {i}: {book.get('title', f'Book {i}')}" for i, book in enumerate(book_templates, 1)]
    book_choices.append("← Back")

    selected = questionary.select(
        "Which book would you like to generate?",
        choices=book_choices,
        style=custom_style
    ).ask()

    if selected == "← Back":
        return

    # Extract book number
    book_number = int(selected.split(":")[0].replace("Book ", ""))

    # Start generation timer
    generation_timer.start()

    # Generate the selected book
    console.print(f"\n[bold cyan]Generating {selected}[/bold cyan]")
    epub_path = series_generator.generate_book(book_templates[book_number - 1], book_number)

    # Display completion message
    console.print("\n[bold green]Book generation complete![/bold green]")
    console.print(f"[bold green]Generation time:[/bold green] [bold cyan]{generation_timer.get_elapsed_time()}[/bold cyan]")
    console.print(f"[bold green]Book saved to:[/bold green] [bold cyan]{epub_path}[/bold cyan]")

def create_covers(series_manager: SeriesManager) -> None:
    """
    Create covers for books in a series.

    Args:
        series_manager: SeriesManager instance
    """
    console.print("[yellow]Cover creation feature is not yet implemented.[/yellow]")
    console.print("[yellow]This would use an image generation API to create covers for each book in the series.[/yellow]")

def check_api_key_status() -> None:
    """Check and display API key status."""
    try:
        # Initialize the Gemini client
        gemini_client = GeminiClient()

        # Display API key status
        display_api_key_status(gemini_client)
    except Exception as e:
        console.print(f"[bold red]Error checking API key status: {str(e)}[/bold red]")
        console.print("[yellow]Make sure your API keys are properly configured in the .env file.[/yellow]")
        input("\nPress Enter to continue...")

def generate_series_covers(series_manager: SeriesManager) -> None:
    """
    Generate covers for books in a series.

    Args:
        series_manager: SeriesManager instance
    """
    # Scan for existing books that might not be in the metadata
    series_manager.scan_for_existing_books()

    if not series_manager or not series_manager.books:
        console.print("[bold yellow]No books found in this series.[/bold yellow]")
        return

    # Display books in the series
    console.print("[bold cyan]Books in this Series[/bold cyan]")

    books_table = Table(box=box.ROUNDED)
    books_table.add_column("#", style="cyan")
    books_table.add_column("Title", style="white")
    books_table.add_column("Description", style="white")

    for book in series_manager.books:
        book_num = book.get("book_number", "?")
        title = book.get("title", "Untitled")
        description = book.get("description", "")
        books_table.add_row(str(book_num), title, description[:50] + "..." if len(description) > 50 else description)

    console.print(books_table)

    # Ask which book to generate a cover for
    book_choices = [f"Book {book.get('book_number', '?')}: {book.get('title', 'Untitled')}" for book in series_manager.books]
    book_choices.append("Generate covers for all books")
    book_choices.append("← Back")

    selected_option = questionary.select(
        "Select a book to generate a cover for:",
        choices=book_choices,
        style=custom_style
    ).ask()

    if selected_option == "← Back":
        return

    # Get the series directory
    series_dir = create_series_directory(series_manager.series_title)

    if selected_option == "Generate covers for all books":
        # Generate covers for all books
        for book in series_manager.books:
            book_num = book.get("book_number", 1)
            title = book.get("title", "Untitled")
            book_dir = os.path.join(series_dir, f"book_{book_num:02d}_{sanitize_filename(title)}")

            # Check if the book directory exists
            if not os.path.exists(book_dir):
                console.print(f"[yellow]Book directory not found for Book {book_num}: {title}[/yellow]")
                continue

            # Check if novel_data.json exists
            json_path = os.path.join(book_dir, "novel_data.json")
            if not os.path.exists(json_path):
                console.print(f"[yellow]Novel data not found for Book {book_num}: {title}[/yellow]")
                continue

            # Load the novel data
            with open(json_path, 'r', encoding='utf-8') as f:
                novel_data = json.load(f)

            # Generate cover
            console.print(f"[bold cyan]Generating cover for Book {book_num}: {title}...[/bold cyan]")
            cover_path = generate_cover(novel_data, book_dir)

            # Update EPUB with cover if requested
            if cover_path:
                epub_path = os.path.join(book_dir, f"{sanitize_filename(title)}.epub")
                if os.path.exists(epub_path):
                    console.print(f"[bold cyan]Updating EPUB with new cover...[/bold cyan]")
                    formatter = EpubFormatter(novel_data)
                    formatter.save_epub(book_dir, cover_path)
                    console.print(f"[bold green]✓[/bold green] EPUB updated with new cover")

def manage_series_cover_images(series_manager: SeriesManager) -> None:
    """
    Manage cover images for books in a series.

    Args:
        series_manager: SeriesManager instance
    """
    try:
        from src.utils.cover_image_manager import CoverImageManager

        # Scan for existing books
        series_manager.scan_for_existing_books()

        if not series_manager.books:
            console.print("[yellow]No books found in this series.[/yellow]")
            input("\nPress Enter to continue...")
            return

        # Display books and let user select one or manage all
        console.print("\n[bold cyan]Select a book to manage cover images:[/bold cyan]")

        book_choices = []
        for book in series_manager.books:
            book_num = book.get("book_number", "?")
            title = book.get("title", "Untitled")
            book_choices.append(f"Book {book_num}: {title}")

        book_choices.append("Manage All Books Covers")
        book_choices.append("← Back")

        selected = questionary.select(
            "Select a book:",
            choices=book_choices,
            style=custom_style
        ).ask()

        if selected == "← Back":
            return

        if selected == "Manage All Books Covers":
            manage_all_books_covers(series_manager)
            return

        # Extract book number and find the book
        book_num = int(selected.split(":")[0].replace("Book ", "").strip())
        selected_book = None

        for book in series_manager.books:
            if book.get("book_number", 0) == book_num:
                selected_book = book
                break

        if not selected_book:
            console.print("[bold red]Error: Book not found.[/bold red]")
            input("\nPress Enter to continue...")
            return

        # Create book info structure
        title = selected_book.get("title", "Untitled")
        series_dir = create_series_directory(series_manager.series_title)
        book_dir = os.path.join(series_dir, f"book_{book_num:02d}_{sanitize_filename(title)}")

        book_info = {
            "title": title,
            "book_number": book_num,
            "directory": book_dir,
            "json_path": os.path.join(book_dir, "novel_data.json")
        }

        # Check if book directory and files exist
        if not os.path.exists(book_dir):
            console.print(f"[yellow]Book directory not found: {book_dir}[/yellow]")
            input("\nPress Enter to continue...")
            return

        if not os.path.exists(book_info["json_path"]):
            console.print(f"[yellow]Book data not found: {book_info['json_path']}[/yellow]")
            input("\nPress Enter to continue...")
            return

        # Use the cover image manager
        cover_manager = CoverImageManager()
        cover_manager.manage_series_cover_images(series_manager, book_info)

    except Exception as e:
        console.print(f"[bold red]Error managing series cover images: {str(e)}[/bold red]")
        input("\nPress Enter to continue...")

def manage_all_books_covers(series_manager: SeriesManager) -> None:
    """
    Manage cover images for all books in a series at once.

    Args:
        series_manager: SeriesManager instance
    """
    try:
        from src.utils.cover_image_manager import CoverImageManager
        from src.utils.cover_folder_manager import CoverFolderManager

        console.print("\n[bold cyan]Managing All Books Covers[/bold cyan]")

        # Get series info
        series_info = {
            'series_title': series_manager.series_title,
            'is_part_of_series': True
        }

        # Initialize managers
        cover_manager = CoverImageManager()
        folder_manager = CoverFolderManager()

        # Get series cover folder info
        series_folder_info = folder_manager.get_cover_folder_structure_info(
            series_manager.series_title, series_info
        )

        console.print(f"[bold green]Series Cover Folder:[/bold green] [cyan]{series_folder_info['cover_folder']}[/cyan]")

        # Display all books status
        console.print("\n[bold cyan]Books Cover Status:[/bold cyan]")

        books_table = Table(box=box.ROUNDED)
        books_table.add_column("Book", style="cyan", width=8)
        books_table.add_column("Title", style="white", width=30)
        books_table.add_column("Cover Status", style="yellow", width=15)
        books_table.add_column("EPUB Status", style="green", width=15)

        valid_books = []
        for book in series_manager.books:
            book_num = book.get("book_number", "?")
            title = book.get("title", "Untitled")

            # Check for cover images
            book_series_info = {**series_info, 'book_number': book_num}
            found_images = folder_manager.scan_for_cover_images(title, book_series_info)
            cover_status = f"Yes ({len(found_images)})" if found_images else "No"

            # Check for EPUB file
            series_dir = create_series_directory(series_manager.series_title)
            book_dir = os.path.join(series_dir, f"book_{book_num:02d}_{sanitize_filename(title)}")
            epub_files = []
            if os.path.exists(book_dir):
                epub_files = [f for f in os.listdir(book_dir) if f.endswith(".epub")]
            epub_status = "Ready" if epub_files else "Missing"

            books_table.add_row(f"Book {book_num}", title[:28] + "..." if len(title) > 28 else title, cover_status, epub_status)

            # Add to valid books if directory exists
            if os.path.exists(book_dir):
                valid_books.append({
                    'book': book,
                    'book_dir': book_dir,
                    'book_num': book_num,
                    'title': title,
                    'has_covers': len(found_images) > 0,
                    'has_epub': len(epub_files) > 0
                })

        console.print(books_table)

        if not valid_books:
            console.print("[yellow]No valid books found with generated content.[/yellow]")
            input("\nPress Enter to continue...")
            return

        # Show management options
        while True:
            choices = [
                "View All Cover Prompts",
                "Check All Cover Images",
                "Show Series Folder Structure",
                "Apply Covers to All EPUBs",
                "Generate Cover Status Report",
                "← Back"
            ]

            selected = questionary.select(
                "What would you like to do with all books?",
                choices=choices,
                style=custom_style
            ).ask()

            if selected == "← Back":
                break
            elif selected == "View All Cover Prompts":
                view_all_cover_prompts(valid_books)
            elif selected == "Check All Cover Images":
                check_all_cover_images(valid_books, folder_manager, series_info)
            elif selected == "Show Series Folder Structure":
                show_series_folder_structure(series_folder_info, valid_books)
            elif selected == "Apply Covers to All EPUBs":
                apply_covers_to_all_epubs(valid_books, folder_manager, series_info)
            elif selected == "Generate Cover Status Report":
                generate_cover_status_report(valid_books, folder_manager, series_info)

    except Exception as e:
        console.print(f"[bold red]Error managing all books covers: {str(e)}[/bold red]")
        input("\nPress Enter to continue...")

def view_all_cover_prompts(valid_books: list) -> None:
    """View cover prompts for all books."""
    console.print("\n[bold cyan]Cover Prompts for All Books[/bold cyan]")

    for book_info in valid_books:
        book_num = book_info['book_num']
        title = book_info['title']
        book_dir = book_info['book_dir']

        console.print(f"\n[bold green]Book {book_num}: {title}[/bold green]")

        # Check for cover prompt file
        prompt_file = os.path.join(book_dir, "cover_prompt.md")
        if os.path.exists(prompt_file):
            console.print(f"[green]✓[/green] Cover prompt available: [cyan]{prompt_file}[/cyan]")
        else:
            console.print(f"[red]✗[/red] No cover prompt found")

    input("\nPress Enter to continue...")

def check_all_cover_images(valid_books: list, folder_manager, series_info: dict) -> None:
    """Check cover images for all books."""
    console.print("\n[bold cyan]Cover Images Status for All Books[/bold cyan]")

    total_images = 0
    for book_info in valid_books:
        book_num = book_info['book_num']
        title = book_info['title']

        # Check for cover images
        book_series_info = {**series_info, 'book_number': book_num}
        found_images = folder_manager.scan_for_cover_images(title, book_series_info)

        console.print(f"\n[bold green]Book {book_num}: {title}[/bold green]")
        if found_images:
            console.print(f"[green]Found {len(found_images)} cover image(s):[/green]")
            for img in found_images:
                console.print(f"  • [cyan]{os.path.basename(img)}[/cyan]")
            total_images += len(found_images)
        else:
            console.print(f"[red]No cover images found[/red]")
            expected_path = folder_manager.get_expected_cover_path(title, book_series_info)
            console.print(f"  Expected: [yellow]{expected_path}[/yellow]")

    console.print(f"\n[bold cyan]Total cover images found: {total_images}[/bold cyan]")
    input("\nPress Enter to continue...")

def show_series_folder_structure(series_folder_info: dict, valid_books: list) -> None:
    """Show the series folder structure."""
    console.print("\n[bold cyan]Series Cover Folder Structure[/bold cyan]")

    console.print(f"\n[bold green]Series Cover Folder:[/bold green]")
    console.print(f"[cyan]{series_folder_info['cover_folder']}[/cyan]")

    console.print(f"\n[bold green]Expected Cover Files:[/bold green]")
    for book_info in valid_books:
        book_num = book_info['book_num']
        title = book_info['title']
        expected_filename = f"Book{book_num}.jpg"
        console.print(f"  • [yellow]{expected_filename}[/yellow] - {title}")

    console.print(f"\n[bold green]Supported Formats:[/bold green]")
    for fmt in series_folder_info['supported_formats']:
        console.print(f"  • [cyan]{fmt}[/cyan]")

    input("\nPress Enter to continue...")

def apply_covers_to_all_epubs(valid_books: list, folder_manager, series_info: dict) -> None:
    """Apply covers to all EPUB files."""
    console.print("\n[bold cyan]Applying Covers to All EPUBs[/bold cyan]")

    from src.formatters.epub_formatter import EpubFormatter
    from src.utils.file_handler import load_novel_json

    applied_count = 0
    skipped_count = 0

    for book_info in valid_books:
        book_num = book_info['book_num']
        title = book_info['title']
        book_dir = book_info['book_dir']

        console.print(f"\n[bold green]Processing Book {book_num}: {title}[/bold green]")

        # Check for EPUB file
        if not book_info['has_epub']:
            console.print(f"[yellow]⚠[/yellow] No EPUB file found - skipping")
            skipped_count += 1
            continue

        # Check for cover images
        book_series_info = {**series_info, 'book_number': book_num}
        found_images = folder_manager.scan_for_cover_images(title, book_series_info)

        if not found_images:
            console.print(f"[yellow]⚠[/yellow] No cover images found - skipping")
            skipped_count += 1
            continue

        # Use the first found image
        selected_image = found_images[0]
        console.print(f"[cyan]Using cover:[/cyan] {os.path.basename(selected_image)}")

        try:
            # Load novel data
            json_path = os.path.join(book_dir, "novel_data.json")
            novel_data = load_novel_json(json_path)

            # Apply cover to EPUB
            formatter = EpubFormatter(novel_data)
            epub_path = formatter.save_epub(book_dir, selected_image)

            console.print(f"[green]Cover applied successfully[/green]")
            applied_count += 1

        except Exception as e:
            console.print(f"[red]✗[/red] Error applying cover: {str(e)}")
            skipped_count += 1

    console.print(f"\n[bold cyan]Summary:[/bold cyan]")
    console.print(f"[green]✓[/green] Covers applied: {applied_count}")
    console.print(f"[yellow]⚠[/yellow] Skipped: {skipped_count}")

    input("\nPress Enter to continue...")

def generate_cover_status_report(valid_books: list, folder_manager, series_info: dict) -> None:
    """Generate a detailed cover status report."""
    console.print("\n[bold cyan]Cover Status Report[/bold cyan]")

    # Statistics
    total_books = len(valid_books)
    books_with_covers = sum(1 for book in valid_books if book['has_covers'])
    books_with_epubs = sum(1 for book in valid_books if book['has_epub'])
    books_ready_for_covers = sum(1 for book in valid_books if book['has_epub'] and book['has_covers'])

    # Summary table
    summary_table = Table(box=box.ROUNDED, title="Series Cover Summary")
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Count", style="white")
    summary_table.add_column("Percentage", style="yellow")

    summary_table.add_row("Total Books", str(total_books), "100%")
    summary_table.add_row("Books with Covers", str(books_with_covers), f"{(books_with_covers/total_books)*100:.1f}%")
    summary_table.add_row("Books with EPUBs", str(books_with_epubs), f"{(books_with_epubs/total_books)*100:.1f}%")
    summary_table.add_row("Ready for Cover Application", str(books_ready_for_covers), f"{(books_ready_for_covers/total_books)*100:.1f}%")

    console.print(summary_table)

    # Detailed status
    console.print("\n[bold cyan]Detailed Status:[/bold cyan]")

    for book_info in valid_books:
        book_num = book_info['book_num']
        title = book_info['title']

        # Check cover images
        book_series_info = {**series_info, 'book_number': book_num}
        found_images = folder_manager.scan_for_cover_images(title, book_series_info)

        status_parts = []
        if book_info['has_epub']:
            status_parts.append("[green]EPUB Ready[/green]")
        else:
            status_parts.append("[red]EPUB Missing[/red]")

        if found_images:
            status_parts.append(f"[green]Cover Ready ({len(found_images)})[/green]")
        else:
            status_parts.append("[red]Cover Missing[/red]")

        status = " ".join(status_parts)
        console.print(f"[bold]Book {book_num}:[/bold] {title[:40]}{'...' if len(title) > 40 else ''} - {status}")

    # Recommendations
    console.print("\n[bold cyan]Recommendations:[/bold cyan]")

    if books_with_covers < total_books:
        missing_covers = total_books - books_with_covers
        console.print(f"• Generate covers for {missing_covers} book(s) without cover images")

    if books_with_epubs < total_books:
        missing_epubs = total_books - books_with_epubs
        console.print(f"• Generate EPUB files for {missing_epubs} book(s)")

    if books_ready_for_covers > 0:
        console.print(f"• Apply covers to {books_ready_for_covers} book(s) that have both covers and EPUBs")

    if books_with_covers == total_books and books_with_epubs == total_books:
        console.print("• [green]All books are ready! All covers and EPUBs are available.[/green]")

    input("\nPress Enter to continue...")

def validate_epub_file(epub_path: str) -> bool:
    """
    Validate an EPUB file to check if it's properly formatted.

    Args:
        epub_path: Path to the EPUB file

    Returns:
        True if valid, False otherwise
    """
    try:
        import zipfile

        # Check if file exists and is readable
        if not os.path.exists(epub_path):
            return False

        # Check if it's a valid zip file (EPUB is a zip)
        with zipfile.ZipFile(epub_path, 'r') as zip_file:
            # Check for required EPUB files
            file_list = zip_file.namelist()

            # Must have mimetype file
            if 'mimetype' not in file_list:
                return False

            # Must have META-INF directory
            meta_inf_files = [f for f in file_list if f.startswith('META-INF/')]
            if not meta_inf_files:
                return False

            # Check mimetype content
            mimetype_content = zip_file.read('mimetype').decode('utf-8').strip()
            if mimetype_content != 'application/epub+zip':
                return False

        return True

    except Exception:
        return False

def show_calibre_installation_help() -> None:
    """Show detailed Calibre installation and troubleshooting help."""
    console.print("\n[bold cyan]Calibre Installation and Troubleshooting Guide[/bold cyan]")
    console.print("=" * 50)

    console.print("\n[bold yellow]1. Install Calibre:[/bold yellow]")
    console.print("   • Download from: https://calibre-ebook.com/download")
    console.print("   • Choose the version for your operating system")
    console.print("   • Run the installer with administrator privileges")

    console.print("\n[bold yellow]2. Verify Installation:[/bold yellow]")
    console.print("   • Open Command Prompt/Terminal")
    console.print("   • Type: ebook-convert --version")
    console.print("   • You should see version information")

    console.print("\n[bold yellow]3. Common Issues:[/bold yellow]")
    console.print("   • [bold red]'ebook-convert' is not recognized:[/bold red]")
    console.print("     - Calibre is not in your system PATH")
    console.print("     - Try restarting your terminal/command prompt")
    console.print("     - On Windows, restart your computer after installation")

    console.print("   • [bold red]Exit status 1 errors:[/bold red]")
    console.print("     - EPUB files may be corrupted or invalid")
    console.print("     - Insufficient disk space")
    console.print("     - File permission issues")
    console.print("     - Antivirus software blocking the conversion")

    console.print("\n[bold yellow]4. Manual PATH Setup (if needed):[/bold yellow]")
    console.print("   • Windows: Add Calibre installation folder to PATH")
    console.print("     (Usually: C:\\Program Files\\Calibre2\\)")
    console.print("   • macOS/Linux: Calibre usually adds itself to PATH")

    console.print("\n[bold yellow]5. Alternative Solutions:[/bold yellow]")
    console.print("   • Use Calibre's GUI application for manual conversion")
    console.print("   • Check if EPUB files open properly in other readers")
    console.print("   • Try converting one file at a time to isolate issues")

    input("\nPress Enter to continue...")

def export_books(series_manager: SeriesManager) -> None:
    """
    Export books to different formats using Calibre.

    Args:
        series_manager: SeriesManager instance
    """
    # Check if Calibre is installed
    try:
        result = subprocess.run(["ebook-convert", "--version"], capture_output=True, check=False)
        if result.returncode != 0:
            console.print("[bold red]Error: Calibre's ebook-convert tool not working properly.[/bold red]")
            console.print("[yellow]Please reinstall Calibre from https://calibre-ebook.com/download[/yellow]")
            console.print(f"[dim]Error details: {result.stderr.decode() if result.stderr else 'Unknown error'}[/dim]")
            return
    except FileNotFoundError:
        console.print("[bold red]Error: Calibre's ebook-convert tool not found.[/bold red]")
        console.print("[yellow]Please install Calibre from https://calibre-ebook.com/download[/yellow]")
        console.print("[yellow]Make sure Calibre is added to your system PATH.[/yellow]")

        show_help = questionary.confirm(
            "Would you like to see detailed installation and troubleshooting help?",
            default=True,
            style=custom_style
        ).ask()

        if show_help:
            show_calibre_installation_help()
        return

    # Get series directory
    series_dir = create_series_directory(series_manager.series_title)

    # Find all EPUB files in the series directory and its subdirectories
    epub_files = []
    for root, _, files in os.walk(series_dir):
        for file in files:
            if file.endswith(".epub"):
                epub_files.append(os.path.join(root, file))

    # Display found EPUB files or indicate none found
    if epub_files:
        console.print("\n[bold cyan]Found EPUB Files:[/bold cyan]")
        for i, path in enumerate(epub_files, 1):
            console.print(f"[bold green]{i}.[/bold green] {os.path.basename(path)}")
    else:
        console.print("\n[yellow]No EPUB files found for this series.[/yellow]")
        console.print("[dim]You can still generate EPUBs by selecting the EPUB format option below.[/dim]")

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
        if not epub_files:
            console.print("[bold cyan]No existing EPUB files found. Generating EPUBs from book data...[/bold cyan]")

            # Find all book directories with novel_data.json files
            book_dirs = []
            for item in os.listdir(series_dir):
                item_path = os.path.join(series_dir, item)
                if os.path.isdir(item_path) and item.startswith("book_"):
                    json_path = os.path.join(item_path, "novel_data.json")
                    if os.path.exists(json_path):
                        book_dirs.append(item_path)

            if not book_dirs:
                console.print("[yellow]No book data found to generate EPUBs from.[/yellow]")
                console.print("[dim]Please generate some books first using the series generation options.[/dim]")
                return

            console.print(f"[bold cyan]Found {len(book_dirs)} books to generate EPUBs for...[/bold cyan]")
        else:
            console.print(f"[bold cyan]Regenerating {len(epub_files)} EPUB files with updated content...[/bold cyan]")

        from src.utils.file_handler import load_novel_json

        regenerated_count = 0
        failed_count = 0

        # Process existing EPUB files or generate new ones
        files_to_process = epub_files if epub_files else book_dirs

        for file_path in files_to_process:
            if epub_files:
                # Processing existing EPUB files
                book_dir = os.path.dirname(file_path)
                book_name = os.path.basename(book_dir)
            else:
                # Processing book directories to generate new EPUBs
                book_dir = file_path
                book_name = os.path.basename(book_dir)

            console.print(f"[cyan]Processing: {book_name}[/cyan]")

            try:
                # Load novel data from JSON
                json_path = os.path.join(book_dir, "novel_data.json")

                if not os.path.exists(json_path):
                    console.print(f"  [red]Error: novel_data.json not found[/red]")
                    failed_count += 1
                    continue

                novel_data = load_novel_json(json_path)

                # Extract writer profile from novel data
                writer_profile = novel_data.get("writer_profile")

                # Use smart cover selection (checks for existing covers first, then fallback)
                from src.utils.smart_cover_selector import get_smart_cover_for_epub
                cover_path = get_smart_cover_for_epub(novel_data, book_dir, auto_mode=True)

                # Regenerate EPUB with proper content and writer profile
                formatter = EpubFormatter(novel_data, writer_profile=writer_profile)
                new_epub_path = formatter.save_epub(book_dir, cover_path, writer_profile)

                console.print(f"  [green]Regenerated successfully[/green]")
                regenerated_count += 1

            except Exception as e:
                console.print(f"  [red]Error: {str(e)}[/red]")
                failed_count += 1

        # Summary
        total_processed = len(files_to_process)
        if epub_files:
            console.print(f"\n[bold green]EPUB Regeneration Complete![/bold green]")
        else:
            console.print(f"\n[bold green]EPUB Generation Complete![/bold green]")
        console.print(f"[bold green]Successfully processed: {regenerated_count}/{total_processed} files[/bold green]")
        if failed_count > 0:
            console.print(f"[bold red]Failed: {failed_count} files[/bold red]")

        return

    # Map user-friendly format names to Calibre format names and file extensions
    format_mapping = {
        "PDF": {"calibre_format": "pdf", "extension": "pdf"},
        "MOBI": {"calibre_format": "mobi", "extension": "mobi"},
        "AZW3": {"calibre_format": "azw3", "extension": "azw3"},
        "DOCX": {"calibre_format": "docx", "extension": "docx"}
    }

    # Check if we have EPUB files for conversion to other formats
    if not epub_files:
        console.print("[yellow]No EPUB files found to convert to other formats.[/yellow]")
        console.print("[dim]Please generate EPUBs first by selecting the EPUB format option.[/dim]")
        return

    # Determine which formats to convert to
    if selected_format == "All Formats":
        formats_to_convert = list(format_mapping.keys())
        console.print(f"[bold cyan]Converting to all formats: {', '.join(formats_to_convert)}[/bold cyan]")
    else:
        formats_to_convert = [selected_format]

    # Convert each EPUB file to selected format(s)
    total_conversions = len(epub_files) * len(formats_to_convert)
    successful_conversions = 0
    conversion_count = 0

    for epub_path in epub_files:
        for format_name in formats_to_convert:
            conversion_count += 1
            format_info = format_mapping[format_name]
            file_extension = format_info["extension"]
            output_path = epub_path.replace(".epub", f".{file_extension}")

            if selected_format == "All Formats":
                console.print(f"[bold cyan]Converting {os.path.basename(epub_path)} to {format_name} ({conversion_count}/{total_conversions})...[/bold cyan]")
            else:
                console.print(f"[bold cyan]Converting {os.path.basename(epub_path)} to {format_name}...[/bold cyan]")

            try:
                # Normalize paths for Windows compatibility
                epub_path_normalized = os.path.normpath(epub_path)
                output_path_normalized = os.path.normpath(output_path)

                # Check if input file exists
                if not os.path.exists(epub_path_normalized):
                    console.print(f"[bold red]Error: Input file not found: {epub_path_normalized}[/bold red]")
                    continue

                # Validate EPUB file
                if not validate_epub_file(epub_path_normalized):
                    console.print(f"[bold red]Error: Invalid EPUB file: {os.path.basename(epub_path)}[/bold red]")
                    console.print(f"[dim]The EPUB file may be corrupted or improperly formatted[/dim]")
                    continue

                # Run the conversion with detailed error capture
                # Calibre determines output format from file extension
                result = subprocess.run(
                    ["ebook-convert", epub_path_normalized, output_path_normalized],
                    capture_output=True,
                    text=True,
                    timeout=300  # 5 minute timeout
                )

                if result.returncode == 0:
                    console.print(f"[bold green]Converted to: [bold cyan]{output_path_normalized}[/bold cyan][/bold green]")
                    successful_conversions += 1
                else:
                    console.print(f"[bold red]Error converting {os.path.basename(epub_path)} to {format_name}[/bold red]")
                    if result.stderr:
                        console.print(f"[dim]Error details: {result.stderr.strip()}[/dim]")
                    if result.stdout:
                        console.print(f"[dim]Output: {result.stdout.strip()}[/dim]")

            except subprocess.TimeoutExpired:
                console.print(f"[bold red]Error: Conversion timed out for {os.path.basename(epub_path)} to {format_name}[/bold red]")
            except subprocess.CalledProcessError as e:
                console.print(f"[bold red]Error converting {os.path.basename(epub_path)} to {format_name}: {e}[/bold red]")
                if hasattr(e, 'stderr') and e.stderr:
                    console.print(f"[dim]Error details: {e.stderr}[/dim]")
            except Exception as e:
                console.print(f"[bold red]Unexpected error converting {os.path.basename(epub_path)} to {format_name}: {e}[/bold red]")

    # Summary
    format_text = "all formats" if selected_format == "All Formats" else selected_format
    if successful_conversions == total_conversions:
        console.print(f"\n[bold green]Export to {format_text} complete! ({successful_conversions}/{total_conversions} conversions successful)[/bold green]")
    elif successful_conversions > 0:
        console.print(f"\n[bold yellow]Export to {format_text} partially complete. ({successful_conversions}/{total_conversions} conversions successful)[/bold yellow]")
    else:
        console.print(f"\n[bold red]Export to {format_text} failed. No conversions were successful.[/bold red]")
        console.print("[yellow]Common issues:[/yellow]")
        console.print("[yellow]  • Calibre not properly installed or not in PATH[/yellow]")
        console.print("[yellow]  • EPUB files may be corrupted or invalid[/yellow]")
        console.print("[yellow]  • Insufficient disk space[/yellow]")
        console.print("[yellow]  • File permissions issues[/yellow]")

        show_help = questionary.confirm(
            "Would you like to see detailed troubleshooting help?",
            default=True,
            style=custom_style
        ).ask()

        if show_help:
            show_calibre_installation_help()

def zip_series_books_menu(series_manager: SeriesManager) -> None:
    """
    Create a zip archive of all books in a series.

    Args:
        series_manager: SeriesManager instance
    """
    # Get series directory
    series_dir = create_series_directory(series_manager.series_title)

    # Check if series has any books
    series_files = get_series_files(series_dir)
    if not series_files:
        console.print("[yellow]No books found in this series to zip.[/yellow]")
        return

    # Display available files
    console.print("\n[bold cyan]Available Files in Series:[/bold cyan]")
    all_formats = set()
    total_files = 0

    for book_dir, files in sorted(series_files.items()):
        book_num = book_dir.split('_')[1] if '_' in book_dir else '?'
        console.print(f"\n[bold green]Book {book_num}:[/bold green]")
        for file_path in files:
            file_name = os.path.basename(file_path)
            file_ext = os.path.splitext(file_name)[1].lower()
            all_formats.add(file_ext)
            console.print(f"  • {file_name}")
            total_files += 1

    console.print(f"\n[bold cyan]Total files found: {total_files}[/bold cyan]")

    # Ask user which formats to include
    format_choices = []
    for fmt in sorted(all_formats):
        if fmt:  # Skip empty extensions
            format_choices.append(fmt.upper())

    # Add preset options
    preset_choices = [
        "EPUB only",
        "All ebook formats (EPUB, PDF, MOBI, AZW3, DOCX)",
        "Everything (all files)",
        "Custom selection"
    ]

    format_selection = questionary.select(
        "What files would you like to include in the zip?",
        choices=preset_choices,
        style=custom_style
    ).ask()

    # Determine which formats to include
    include_formats = None
    if format_selection == "EPUB only":
        include_formats = ['.epub']
    elif format_selection == "All ebook formats (EPUB, PDF, MOBI, AZW3, DOCX)":
        include_formats = ['.epub', '.pdf', '.mobi', '.azw3', '.docx']
    elif format_selection == "Everything (all files)":
        include_formats = None  # Include all
    elif format_selection == "Custom selection":
        if format_choices:
            selected_formats = questionary.checkbox(
                "Select file formats to include:",
                choices=format_choices,
                style=custom_style
            ).ask()
            include_formats = [f'.{fmt.lower()}' for fmt in selected_formats]
        else:
            console.print("[yellow]No file formats available for selection.[/yellow]")
            return

    # Ask for output location
    default_zip_name = f"{sanitize_filename(series_manager.series_title)}_series.zip"

    zip_name = questionary.text(
        "Enter zip file name:",
        default=default_zip_name,
        validate=lambda text: len(text) > 0 and text.endswith('.zip'),
        style=custom_style
    ).ask()

    # Ask for output directory
    output_choices = [
        "Same as series directory",
        "Desktop",
        "Downloads",
        "Custom location"
    ]

    output_location = questionary.select(
        "Where would you like to save the zip file?",
        choices=output_choices,
        style=custom_style
    ).ask()

    # Determine output path
    if output_location == "Same as series directory":
        output_path = os.path.join(series_dir, zip_name)
    elif output_location == "Desktop":
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        output_path = os.path.join(desktop_path, zip_name)
    elif output_location == "Downloads":
        downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
        output_path = os.path.join(downloads_path, zip_name)
    else:  # Custom location
        custom_dir = questionary.path(
            "Enter the directory path:",
            style=custom_style
        ).ask()
        if custom_dir:
            output_path = os.path.join(custom_dir, zip_name)
        else:
            console.print("[yellow]No directory selected. Cancelling zip creation.[/yellow]")
            return

    # Create progress callback
    def progress_callback(current: int, total: int, message: str):
        percentage = (current / total) * 100 if total > 0 else 0
        console.print(f"[bold cyan]Progress: {current}/{total} ({percentage:.1f}%) - {message}[/bold cyan]")

    # Create the zip file
    console.print(f"\n[bold cyan]Creating zip archive...[/bold cyan]")
    console.print(f"[bold cyan]Output: {output_path}[/bold cyan]")

    success, message = zip_series_books(
        series_dir=series_dir,
        output_path=output_path,
        include_formats=include_formats,
        progress_callback=progress_callback
    )

    if success:
        console.print(f"\n[bold green]{message}[/bold green]")
        console.print(f"[bold green]Zip file saved to: {output_path}[/bold green]")

        # Show file size
        try:
            file_size = os.path.getsize(output_path)
            size_mb = file_size / (1024 * 1024)
            console.print(f"[bold green]File size: {size_mb:.2f} MB[/bold green]")
        except:
            pass
    else:
        console.print(f"\n[bold red]{message}[/bold red]")

def series_management_menu() -> None:
    """Main series management menu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Series Management[/bold cyan]")

        # Main menu options
        choices = [
            "Create New Series",
            "Import Series from Ideas",
            "Work with Existing Series",
            "Exit"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Create New Series":
            series_manager = create_new_series()
            if series_manager:
                series_options_menu(series_manager)

        elif selected == "Import Series from Ideas":
            series_manager = create_series_from_idea()
            if series_manager:
                series_options_menu(series_manager)

        elif selected == "Work with Existing Series":
            series_manager = select_existing_series()
            if series_manager:
                series_options_menu(series_manager)

        elif selected == "Exit":
            break

def series_options_menu(series_manager: SeriesManager) -> None:
    """
    Menu for working with a specific series.

    Args:
        series_manager: SeriesManager instance
    """
    while True:
        clear_screen()
        display_title()

        # Display series information
        display_series_info(series_manager)

        # Series options
        choices = [
            "Auto-Generate Entire Series",
            "Generate Books One by One",
            "Create Covers for Books",
            "Manage Cover Images",
            "Export Books to Different Formats",
            "Zip Series Books",
            "API Key Status",
            "← Back to Main Menu"
        ]

        selected = questionary.select(
            "What would you like to do with this series?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Auto-Generate Entire Series":
            auto_generate_series(series_manager)
            input("\nPress Enter to continue...")

        elif selected == "Generate Books One by One":
            generate_book_by_book(series_manager)
            input("\nPress Enter to continue...")

        elif selected == "Create Covers for Books":
            generate_series_covers(series_manager)
            input("\nPress Enter to continue...")

        elif selected == "Manage Cover Images":
            manage_series_cover_images(series_manager)

        elif selected == "Export Books to Different Formats":
            export_books(series_manager)
            input("\nPress Enter to continue...")

        elif selected == "Zip Series Books":
            zip_series_books_menu(series_manager)
            input("\nPress Enter to continue...")

        elif selected == "API Key Status":
            check_api_key_status()

        elif selected == "← Back to Main Menu":
            break
