"""
Book management menu for managing individual books.
"""
import os
import json
import subprocess
from typing import List, Dict, Any, Optional
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box
import questionary

# Local imports
from src.core.novel_generator import NovelGenerator
from src.formatters.epub_formatter import EpubFormatter
from src.utils.file_handler import create_output_directory, save_novel_json, sanitize_filename, load_novel_json
from src.utils.genre_defaults import get_all_genres
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
from src.core.gemini_client import GeminiClient

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
    Display books in a formatted table.

    Args:
        books: List of book information dictionaries
    """
    if not books:
        console.print("[yellow]No books found.[/yellow]")
        return

    table = Table(box=box.ROUNDED)
    table.add_column("#", style="cyan", width=3)
    table.add_column("Title", style="white", width=25)
    table.add_column("Author", style="green", width=20)
    table.add_column("Genre", style="blue", width=15)
    table.add_column("Chapters", style="yellow", width=8)
    table.add_column("Words", style="magenta", width=8)
    table.add_column("Created", style="dim", width=12)

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

        table.add_row(
            str(i),
            book["title"][:23] + "..." if len(book["title"]) > 25 else book["title"],
            book["author"][:18] + "..." if len(book["author"]) > 20 else book["author"],
            book["genre"][:13] + "..." if len(book["genre"]) > 15 else book["genre"],
            str(book.get("chapter_count", 0)),
            word_str,
            created_str
        )

    console.print(table)

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
    Display detailed information about a book.

    Args:
        book_info: Book information dictionary
    """
    console.print(f"\n[bold cyan]Book Information[/bold cyan]")

    info_table = Table(box=box.ROUNDED, show_header=False)
    info_table.add_column("Property", style="cyan", width=15)
    info_table.add_column("Value", style="white")

    info_table.add_row("Title", book_info["title"])
    info_table.add_row("Author", book_info["author"])
    info_table.add_row("Genre", book_info["genre"])
    info_table.add_row("Target Audience", book_info["target_audience"])
    info_table.add_row("Chapters", str(book_info.get("chapter_count", 0)))

    word_count = book_info.get("word_count", 0)
    word_str = f"{word_count:,}" if word_count > 0 else "Unknown"
    info_table.add_row("Word Count", word_str)

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
    info_table.add_row("Created", created_str)

    info_table.add_row("Directory", book_info["directory"])

    console.print(info_table)

    # Display description if available
    if book_info.get("description"):
        console.print(f"\n[bold cyan]Description:[/bold cyan]")
        console.print(f"[dim]{book_info['description']}[/dim]")

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

        # Generate the novel (using the same process as main())
        console.print("[bold cyan]Generating writer profile...[/bold cyan]")
        writer_profile = generator.generate_writer_profile()
        console.print("[bold green]✓[/bold green] Writer profile generated")

        console.print("[bold cyan]Generating novel outline...[/bold cyan]")
        chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)
        console.print(f"[bold green]✓[/bold green] Novel outline generated ({chapter_count} chapters)")

        console.print("[bold cyan]Generating characters...[/bold cyan]")
        characters = generator.generate_characters()
        console.print(f"[bold green]✓[/bold green] Characters generated ({len(characters)} characters)")

        # Generate chapters
        chapters = generator.generate_complete_novel()
        console.print(f"[bold green]✓[/bold green] All chapters generated")

        # Compile novel data
        novel = memory_manager.compile_novel_data()

        # Save novel as JSON
        save_novel_json(novel, output_dir)

        # Generate cover
        cover_path = generate_cover(novel, output_dir, auto_mode=False)

        # Format and save as EPUB
        console.print("[bold cyan]Formatting EPUB...[/bold cyan]")
        formatter = EpubFormatter(novel)
        epub_path = formatter.save_epub(output_dir, cover_path)

        # Stop timer
        generation_timer.stop()

        # Display completion
        console.print("\n[bold green]✓ Book generation complete![/bold green]")
        console.print(f"[bold green]✓ Generation time:[/bold green] [bold cyan]{generation_timer.get_elapsed_time()}[/bold cyan]")
        console.print(f"[bold green]✓ Book saved to:[/bold green] [bold cyan]{epub_path}[/bold cyan]")

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
                formatter = EpubFormatter(novel_data)
                formatter.save_epub(book_info["directory"], cover_path)
                console.print(f"[bold green]✓[/bold green] EPUB updated with new cover")
            else:
                console.print(f"[bold green]✓[/bold green] Cover generated: {cover_path}")
        else:
            console.print("[yellow]Cover generation cancelled.[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Error generating cover: {str(e)}[/bold red]")

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
    if not epub_files:
        console.print("[yellow]No EPUB file found for this book.[/yellow]")
        return

    epub_path = os.path.join(book_info["directory"], epub_files[0])
    console.print(f"[bold cyan]Found EPUB:[/bold cyan] {epub_files[0]}")

    # Ask which format to export to
    format_choices = ["PDF", "MOBI", "AZW3", "DOCX", "All Formats", "← Back"]
    selected_format = questionary.select(
        "Select export format:",
        choices=format_choices,
        style=custom_style
    ).ask()

    if selected_format == "← Back":
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
                console.print(f"[bold green]✓[/bold green] {fmt.upper()} conversion successful: {output_file}")
            else:
                console.print(f"[bold red]✗[/bold red] {fmt.upper()} conversion failed")
                if result.stderr:
                    console.print(f"[red]Error: {result.stderr}[/red]")

        except subprocess.TimeoutExpired:
            console.print(f"[bold red]✗[/bold red] {fmt.upper()} conversion timed out")
        except Exception as e:
            console.print(f"[bold red]✗[/bold red] {fmt.upper()} conversion error: {str(e)}")

    console.print(f"\n[bold green]✓ Export process completed![/bold green]")

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
        gemini_client = GeminiClient()

        # Display API key status
        from src.ui.terminal_ui import display_api_key_status
        display_api_key_status(gemini_client)
    except Exception as e:
        console.print(f"[bold red]Error checking API key status: {str(e)}[/bold red]")
        console.print("[yellow]Make sure your API keys are properly configured in the .env file.[/yellow]")
        input("\nPress Enter to continue...")

def book_options_menu(book_info: Dict[str, Any]) -> None:
    """
    Options menu for a selected book.

    Args:
        book_info: Book information dictionary
    """
    while True:
        clear_screen()
        display_title()

        # Display book information
        display_book_info(book_info)

        # Book options
        choices = [
            "Generate New Cover",
            "Export to Different Formats",
            "View Book Files",
            "API Key Status",
            "← Back to Book Menu"
        ]

        selected = questionary.select(
            "What would you like to do with this book?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Generate New Cover":
            generate_book_cover(book_info)
            input("\nPress Enter to continue...")

        elif selected == "Export to Different Formats":
            export_book_formats(book_info)
            input("\nPress Enter to continue...")

        elif selected == "View Book Files":
            view_book_files(book_info)
            input("\nPress Enter to continue...")

        elif selected == "API Key Status":
            check_api_key_status()

        elif selected == "← Back to Book Menu":
            break

def view_book_files(book_info: Dict[str, Any]) -> None:
    """
    Display all files in the book directory.

    Args:
        book_info: Book information dictionary
    """
    console.print(f"\n[bold cyan]Files in '{book_info['title']}'[/bold cyan]")
    console.print(f"[dim]Directory: {book_info['directory']}[/dim]\n")

    if not os.path.exists(book_info["directory"]):
        console.print("[red]Directory not found![/red]")
        return

    files = os.listdir(book_info["directory"])
    if not files:
        console.print("[yellow]No files found in directory.[/yellow]")
        return

    # Create table for files
    files_table = Table(box=box.ROUNDED)
    files_table.add_column("File", style="white", width=40)
    files_table.add_column("Type", style="cyan", width=10)
    files_table.add_column("Size", style="yellow", width=10)

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

            files_table.add_row(file, file_ext, size_str)

    console.print(files_table)

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
    """Main book management menu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Book Management[/bold cyan]")

        # Get book count for display
        existing_books = get_existing_books()
        book_count = len(existing_books)

        if book_count > 0:
            console.print(f"[dim]You have {book_count} book{'s' if book_count != 1 else ''} in your library[/dim]\n")
        else:
            console.print("[dim]Your library is empty[/dim]\n")

        # Main menu options
        choices = [
            "Create New Book",
            "Work with Existing Books",
            "Browse Book Library",
            "Exit"
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

        elif selected == "Work with Existing Books":
            book_info = select_existing_book()
            if book_info:
                book_options_menu(book_info)

        elif selected == "Browse Book Library":
            browse_book_library()

        elif selected == "Exit":
            break
