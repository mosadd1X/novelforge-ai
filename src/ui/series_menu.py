"""
Interactive menu system for series management.
"""
import os
import sys
import json
import subprocess
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
import questionary
from questionary import Style

from src.core.series_manager import SeriesManager
from src.core.series_generator import SeriesGenerator
from src.utils.file_handler import create_output_directory, create_series_directory, sanitize_filename, zip_series_books, get_series_files
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

    # Get author name
    author = questionary.text(
        "Who is the author?",
        validate=lambda text: len(text) > 0,
        style=custom_style
    ).ask()

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
    console.print("\n[bold green]✓ Book generation complete![/bold green]")
    console.print(f"[bold green]✓ Generation time:[/bold green] [bold cyan]{generation_timer.get_elapsed_time()}[/bold cyan]")
    console.print(f"[bold green]✓ Book saved to:[/bold green] [bold cyan]{epub_path}[/bold cyan]")

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
    else:
        # Extract book number from selection
        book_num = int(selected_option.split(":")[0].replace("Book ", "").strip())

        # Find the selected book
        selected_book = None
        for book in series_manager.books:
            if book.get("book_number", 0) == book_num:
                selected_book = book
                break

        if not selected_book:
            console.print("[bold red]Error: Book not found.[/bold red]")
            return

        title = selected_book.get("title", "Untitled")
        book_dir = os.path.join(series_dir, f"book_{book_num:02d}_{sanitize_filename(title)}")

        # Check if the book directory exists
        if not os.path.exists(book_dir):
            console.print(f"[yellow]Book directory not found for Book {book_num}: {title}[/yellow]")
            return

        # Check if novel_data.json exists
        json_path = os.path.join(book_dir, "novel_data.json")
        if not os.path.exists(json_path):
            console.print(f"[yellow]Novel data not found for Book {book_num}: {title}[/yellow]")
            return

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

    if not epub_files:
        console.print("[yellow]No EPUB files found for this series.[/yellow]")
        return

    # Display found EPUB files
    console.print("\n[bold cyan]Found EPUB Files:[/bold cyan]")
    for i, path in enumerate(epub_files, 1):
        console.print(f"[bold green]{i}.[/bold green] {os.path.basename(path)}")

    # Ask which format to export to
    format_choices = ["PDF", "MOBI", "AZW3", "DOCX", "HTML", "← Back"]
    selected_format = questionary.select(
        "Select export format:",
        choices=format_choices,
        style=custom_style
    ).ask()

    if selected_format == "← Back":
        return

    # Convert each EPUB file
    successful_conversions = 0
    total_conversions = len(epub_files)

    for epub_path in epub_files:
        output_path = epub_path.replace(".epub", f".{selected_format.lower()}")

        console.print(f"[bold cyan]Converting {os.path.basename(epub_path)} to {selected_format}...[/bold cyan]")

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
            result = subprocess.run(
                ["ebook-convert", epub_path_normalized, output_path_normalized],
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            if result.returncode == 0:
                console.print(f"[bold green]✓[/bold green] Converted to: [bold cyan]{output_path_normalized}[/bold cyan]")
                successful_conversions += 1
            else:
                console.print(f"[bold red]Error converting {os.path.basename(epub_path)}[/bold red]")
                if result.stderr:
                    console.print(f"[dim]Error details: {result.stderr.strip()}[/dim]")
                if result.stdout:
                    console.print(f"[dim]Output: {result.stdout.strip()}[/dim]")

        except subprocess.TimeoutExpired:
            console.print(f"[bold red]Error: Conversion timed out for {os.path.basename(epub_path)}[/bold red]")
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Error converting {os.path.basename(epub_path)}: {e}[/bold red]")
            if hasattr(e, 'stderr') and e.stderr:
                console.print(f"[dim]Error details: {e.stderr}[/dim]")
        except Exception as e:
            console.print(f"[bold red]Unexpected error converting {os.path.basename(epub_path)}: {e}[/bold red]")

    # Summary
    if successful_conversions == total_conversions:
        console.print(f"\n[bold green]✓ Export to {selected_format} complete! ({successful_conversions}/{total_conversions} files converted)[/bold green]")
    elif successful_conversions > 0:
        console.print(f"\n[bold yellow]⚠ Export to {selected_format} partially complete. ({successful_conversions}/{total_conversions} files converted)[/bold yellow]")
    else:
        console.print(f"\n[bold red]✗ Export to {selected_format} failed. No files were converted successfully.[/bold red]")
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
        "All ebook formats (EPUB, PDF, MOBI, AZW3)",
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
    elif format_selection == "All ebook formats (EPUB, PDF, MOBI, AZW3)":
        include_formats = ['.epub', '.pdf', '.mobi', '.azw3']
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
        console.print(f"\n[bold green]✓ {message}[/bold green]")
        console.print(f"[bold green]✓ Zip file saved to: {output_path}[/bold green]")

        # Show file size
        try:
            file_size = os.path.getsize(output_path)
            size_mb = file_size / (1024 * 1024)
            console.print(f"[bold green]✓ File size: {size_mb:.2f} MB[/bold green]")
        except:
            pass
    else:
        console.print(f"\n[bold red]✗ {message}[/bold red]")

def series_management_menu() -> None:
    """Main series management menu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Series Management[/bold cyan]")

        # Main menu options
        choices = [
            "Create New Series",
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
