"""
Terminal UI components for the novel generation system.
"""
import os
import time
import datetime
from typing import Dict, List, Any, Optional, Callable, Union
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table
from rich.markdown import Markdown
from rich.align import Align
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich import box
import questionary
from questionary import Style
from src.utils.cover_generator import CoverGenerator

# Import SeriesManager conditionally to avoid circular imports
try:
    from src.core.series_manager import SeriesManager
except ImportError:
    SeriesManager = None

# Import series visualizer conditionally to avoid circular imports
try:
    from src.ui.series_visualizer import (
        visualize_character_development,
        visualize_plot_arcs,
        visualize_timeline,
        visualize_series_data
    )
except ImportError:
    visualize_character_development = None
    visualize_plot_arcs = None
    visualize_timeline = None
    visualize_series_data = None


class GenerationTimer:
    """Timer class to track generation time."""

    def __init__(self):
        """Initialize the timer."""
        self.start_time = None
        self.is_running = False
        self.live_display = None
        self._stop_update = False

    def start(self):
        """Start the timer."""
        self.start_time = time.time()
        self.is_running = True
        self._stop_update = False

    def stop(self):
        """Stop the timer updates."""
        self._stop_update = True
        if self.live_display:
            self.live_display.stop()

    def get_elapsed_time(self):
        """Get the elapsed time as a formatted string."""
        if not self.is_running:
            return "00:00:00"

        elapsed_seconds = int(time.time() - self.start_time)
        return str(datetime.timedelta(seconds=elapsed_seconds))

    def get_start_datetime(self):
        """Get the start time as a formatted datetime string."""
        if not self.start_time:
            return "Not started"

        start_datetime = datetime.datetime.fromtimestamp(self.start_time)
        return start_datetime.strftime("%Y-%m-%d %H:%M:%S")

    def create_timer_display(self):
        """Create a renderable for the timer display."""
        from rich.console import Group
        from rich.text import Text

        start_time = self.get_start_datetime()
        elapsed_time = self.get_elapsed_time()

        start_text = Text(f"Started: {start_time}", style="dim")
        elapsed_text = Text(f"Elapsed: {elapsed_time}", style="dim")

        return Group(
            Text("", justify="right"),  # Empty line for spacing
            Text.assemble(start_text, justify="right"),
            Text.assemble(elapsed_text, justify="right")
        )

    def start_live_display(self):
        """Start a live updating timer display."""
        from rich.live import Live
        import threading

        # Make sure any existing live display is stopped
        self.stop()
        self._stop_update = False
        self.is_running = True

        def update_timer():
            try:
                with Live(self.create_timer_display(), refresh_per_second=1, transient=True) as live:
                    self.live_display = live
                    while self.is_running and not self._stop_update:
                        live.update(self.create_timer_display())
                        time.sleep(1)
            except Exception as e:
                # Silently handle any display errors
                pass

        # Start timer in a separate thread
        timer_thread = threading.Thread(target=update_timer)
        timer_thread.daemon = True
        timer_thread.start()


# Create a global timer instance
generation_timer = GenerationTimer()

from src.utils.genre_defaults import get_genre_defaults, get_all_genres

# Create console with markup enabled for Rich formatting
console = Console(markup=True)

def display_api_key_status(gemini_client) -> None:
    """
    Display API key status information.

    Args:
        gemini_client: GeminiClient instance
    """
    clear_screen()
    display_title()

    console.print("[bold cyan]API Key Status[/bold cyan]")

    # Check all API keys
    console.print("\n[bold cyan]Checking API keys...[/bold cyan]")
    api_status = gemini_client.check_api_connection(check_all_keys=True)

    # Create a table for API key status
    table = Table(box=box.ROUNDED)
    table.add_column("Status", style="cyan")
    table.add_column("Value", style="white")

    # Add general information
    table.add_row("Total API Keys", str(api_status["active_keys"]))
    table.add_row("Working API Keys", str(api_status["working_keys"]))
    table.add_row("Rate Limited Keys", str(len(gemini_client.rate_limited_keys)))
    table.add_row("Current API Key", f"Key {gemini_client.current_key_index + 1}/{len(gemini_client.api_keys)}")

    console.print(table)

    # Get usage statistics
    usage_stats = gemini_client.get_api_key_usage_stats()

    # Create a table for API key usage
    usage_table = Table(title="API Key Usage", box=box.ROUNDED)
    usage_table.add_column("API Key", style="cyan")
    usage_table.add_column("Requests", style="white", justify="right")
    usage_table.add_column("Percentage", style="white", justify="right")
    usage_table.add_column("Status", style="green")

    # Add rows for each API key
    for key, stats in usage_stats["usage_by_key"].items():
        # Determine if this key is rate limited
        is_rate_limited = key in [f"{k[:4]}...{k[-4:]}" for k in gemini_client.rate_limited_keys]
        status = "[bold red]Rate Limited[/bold red]" if is_rate_limited else "[bold green]Available[/bold green]"

        # Add row
        usage_table.add_row(
            key,
            str(stats["count"]),
            f"{stats['percentage']}%",
            status
        )

    console.print(usage_table)

    # Display key rotation information
    if api_status["active_keys"] > 1:
        console.print("\n[bold green]Multiple API keys detected[/bold green]")
        console.print("The system will automatically rotate keys if rate limits are encountered.")
        console.print("Keys are rotated in sequence, and rate-limited keys are skipped until all keys are exhausted.")
    else:
        console.print("\n[bold yellow]Only one API key detected[/bold yellow]")
        console.print("Consider adding more API keys to handle rate limits for long generations.")

    console.print("\n[bold cyan]API Key Management Tips:[/bold cyan]")
    console.print("1. Add more API keys in your .env file (GEMINI_API_KEY_1, GEMINI_API_KEY_2, etc.)")
    console.print("2. If all keys are rate limited, wait for the quota to reset (usually hourly or daily)")
    console.print("3. Monitor your API usage in the Google AI Studio dashboard")

    # Wait for user input
    console.print("\nPress Enter to return to the main menu...")
    input()

# Custom questionary style
custom_style = Style([
    ('qmark', 'fg:cyan bold'),
    ('question', 'fg:white bold'),
    ('answer', 'fg:green bold'),
    ('pointer', 'fg:cyan bold'),
    ('highlighted', 'fg:cyan bold'),
    ('selected', 'fg:green bold'),
    ('separator', 'fg:cyan'),
    ('instruction', 'fg:white'),
    ('text', 'fg:white'),
    ('disabled', 'fg:gray'),
])


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def display_title() -> None:
    """Display the application title."""
    console.print(Panel("Ebook Generator", style="cyan bold", expand=False))
    console.print()


def get_series_info() -> Dict[str, Any]:
    """
    Get series information from the user.

    Returns:
        Dictionary containing series information and whether to use an existing series
    """
    # Ask if this book is part of a series
    is_series = questionary.confirm(
        "Is this book part of a series?",
        default=False,
        style=custom_style
    ).ask()

    if not is_series:
        return {"is_series": False}

    # Check if there are existing series
    series_dir = os.path.join("output", "series")
    os.makedirs(series_dir, exist_ok=True)

    existing_series = []
    for file in os.listdir(series_dir):
        if file.startswith("series_") and file.endswith(".json"):
            series_name = file[7:-5]  # Remove "series_" prefix and ".json" suffix
            series_name = series_name.replace("_", " ")
            existing_series.append(series_name)

    # Ask if user wants to use an existing series
    use_existing = False
    selected_series = None

    if existing_series:
        use_existing = questionary.confirm(
            "Do you want to use an existing series?",
            default=True,
            style=custom_style
        ).ask()

        if use_existing:
            selected_series = questionary.select(
                "Select a series:",
                choices=existing_series,
                style=custom_style
            ).ask()

    # If not using existing series, get new series info
    if not use_existing:
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

        # Get planned number of books
        planned_books = questionary.text(
            "How many books do you plan for this series? (Enter a number)",
            validate=lambda text: text.isdigit() and int(text) > 0,
            style=custom_style
        ).ask()

        return {
            "is_series": True,
            "use_existing": False,
            "series_title": series_title,
            "series_description": series_description,
            "planned_books": int(planned_books)
        }
    else:
        return {
            "is_series": True,
            "use_existing": True,
            "selected_series": selected_series
        }

def get_novel_info(series_info: Dict[str, Any] = None) -> Dict[str, str]:
    """
    Get basic novel information from the user.

    Args:
        series_info: Optional dictionary containing series information

    Returns:
        Dictionary containing novel information
    """
    # Get title
    title = questionary.text(
        "What is the title of your novel?",
        validate=lambda text: len(text) > 0,
        style=custom_style
    ).ask()

    # Get author
    author = questionary.text(
        "Who is the author?",
        validate=lambda text: len(text) > 0,
        style=custom_style
    ).ask()

    # Get description
    description = questionary.text(
        "Provide a brief description of your novel:",
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

    # Create result dictionary
    result = {
        "title": title,
        "author": author,
        "description": description,
        "genre": genre,
        "target_audience": target_audience
    }

    # Add series information if provided
    if series_info and series_info.get("is_series", False):
        result["is_part_of_series"] = True
        result["series_info"] = series_info
    else:
        result["is_part_of_series"] = False

    return result


def display_writer_profile(writer_profile: Dict[str, Any]) -> None:
    """
    Display the generated writer profile.

    Args:
        writer_profile: Dictionary containing writer profile information
    """
    console.print("\n[bold cyan]Writer Profile[/bold cyan]")

    table = Table(box=box.ROUNDED)
    table.add_column("Attribute", style="cyan")
    table.add_column("Description", style="white")

    for key, value in writer_profile.items():
        if key != "raw_response":  # Skip raw response
            # Convert value to string to ensure it's renderable
            if isinstance(value, (dict, list)):
                value_str = str(value)
            else:
                value_str = str(value)
            table.add_row(key.replace("_", " ").title(), value_str)

    console.print(table)
    console.print()


def display_novel_outline(chapter_outlines: List[str], chapter_count: int) -> None:
    """
    Display the generated novel outline.

    Args:
        chapter_outlines: List of chapter outlines
        chapter_count: Total number of chapters
    """
    console.print("\n[bold cyan]Novel Outline[/bold cyan]")
    console.print(f"Total chapters: [bold]{chapter_count}[/bold]\n")

    # For many chapters, use a more compact display
    if chapter_count > 20:
        display_compact_outline(chapter_outlines, chapter_count)
    else:
        display_table_outline(chapter_outlines)

def display_compact_outline(chapter_outlines: List[str], chapter_count: int) -> None:
    """Display outline in a compact format for many chapters."""
    from rich.panel import Panel
    from rich.text import Text
    from rich.columns import Columns

    # Show first 5 chapters
    console.print("[bold yellow]📖 First 5 Chapters:[/bold yellow]")
    for i in range(min(5, len(chapter_outlines))):
        outline = chapter_outlines[i]
        console.print(f"[cyan]Chapter {i+1}:[/cyan] {outline}")

    # Show middle sample if there are many chapters
    if chapter_count > 15:
        console.print(f"\n[dim]... {chapter_count - 10} more chapters ...[/dim]")

        # Show last 5 chapters
        console.print("\n[bold yellow]📚 Last 5 Chapters:[/bold yellow]")
        start_idx = max(5, len(chapter_outlines) - 5)
        for i in range(start_idx, len(chapter_outlines)):
            outline = chapter_outlines[i]
            console.print(f"[cyan]Chapter {i+1}:[/cyan] {outline}")

    # Show summary statistics
    total_words = sum(len(outline.split()) for outline in chapter_outlines)
    avg_words = total_words / len(chapter_outlines) if chapter_outlines else 0

    summary_text = Text()
    summary_text.append(f"\n📊 Outline Summary:\n", style="bold cyan")
    summary_text.append(f"  • Total Chapters: {chapter_count}\n", style="white")
    summary_text.append(f"  • Outline Words: {total_words:,}\n", style="white")
    summary_text.append(f"  • Avg per Chapter: {avg_words:.0f} words\n", style="white")

    console.print(Panel(summary_text, title="[bold cyan]Outline Overview[/bold cyan]", border_style="cyan"))
    console.print()

def display_table_outline(chapter_outlines: List[str]) -> None:
    """Display outline in traditional table format for smaller chapter counts."""
    table = Table(box=box.ROUNDED)
    table.add_column("Chapter", style="cyan")
    table.add_column("Description", style="white")

    for i, outline in enumerate(chapter_outlines, 1):
        table.add_row(f"Chapter {i}", outline)

    console.print(table)
    console.print()


def display_characters(characters: List[Dict[str, Any]]) -> None:
    """
    Display the generated characters.

    Args:
        characters: List of character dictionaries
    """
    console.print("\n[bold cyan]Characters[/bold cyan]")

    for character in characters:
        name = character.get("name", "Unknown")
        role = character.get("role", "")

        panel_content = []
        for key, value in character.items():
            if key not in ["name", "raw_response"] and value:
                # Convert value to string to ensure it's renderable
                if isinstance(value, (dict, list)):
                    value_str = str(value)
                else:
                    value_str = str(value)
                panel_content.append(f"[bold]{key.replace('_', ' ').title()}[/bold]: {value_str}")

        console.print(Panel(
            "\n".join(panel_content),
            title=f"[bold]{name}[/bold] ({role})",
            border_style="cyan",
            expand=False
        ))

    console.print()


def display_chapter_progress(chapter_num: int, total_chapters: int) -> None:
    """
    Display chapter generation progress.

    Args:
        chapter_num: Current chapter number
        total_chapters: Total number of chapters
    """
    console.print(f"\n[bold cyan]Generating Chapter {chapter_num}/{total_chapters}[/bold cyan]")

    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        BarColumn(),
        TextColumn("[bold cyan]{task.percentage:>3.0f}%"),
        TimeElapsedColumn()
    ) as progress:
        task = progress.add_task(f"Generating Chapter {chapter_num}", total=100)

        # Simulate progress
        for i in range(1, 101):
            time.sleep(0.05)
            progress.update(task, completed=i)

    console.print(f"[bold green]Chapter {chapter_num} generated successfully![/bold green]\n")


def display_timer_info():
    """Display timer information in the right corner."""
    if generation_timer.is_running:
        start_time = generation_timer.get_start_datetime()
        elapsed_time = generation_timer.get_elapsed_time()
        console.print(f"[dim]Started: {start_time}[/dim]", justify="right")
        console.print(f"[dim]Elapsed: {elapsed_time}[/dim]", justify="right")


def display_series_info(series_manager, show_visualizations: bool = False) -> None:
    """
    Display information about a series.

    Args:
        series_manager: SeriesManager instance
        show_visualizations: Whether to show detailed visualizations
    """
    if not series_manager:
        return

    console.print("\n[bold cyan]Series Information[/bold cyan]")

    # Create a table for series metadata
    table = Table(box=box.ROUNDED)
    table.add_column("Attribute", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("Series Title", series_manager.metadata["title"])
    table.add_row("Description", series_manager.metadata.get("description", ""))
    table.add_row("Book Count", str(series_manager.metadata["book_count"]))
    table.add_row("Planned Books", str(series_manager.metadata.get("planned_books", "Unknown")))
    table.add_row("Created", series_manager.metadata["created_at"].split("T")[0])
    table.add_row("Last Updated", series_manager.metadata["last_updated"].split("T")[0])

    console.print(table)

    # Display books in the series
    if series_manager.books:
        console.print("\n[bold cyan]Books in this Series[/bold cyan]")

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

    # Show visualizations if requested and we have more than one book
    if show_visualizations and series_manager.metadata["book_count"] > 0:
        # Check if we have the visualization functions
        if visualize_series_data:
            # Ask if user wants to see visualizations
            show_viz = questionary.confirm(
                "Would you like to see detailed series visualizations?",
                default=True,
                style=custom_style
            ).ask()

            if show_viz:
                visualize_series_data(series_manager)
        else:
            console.print("[yellow]Series visualizations not available.[/yellow]")

    console.print()


def display_character_development(series_manager) -> None:
    """
    Display character development visualization for a series.

    Args:
        series_manager: SeriesManager instance
    """
    if not series_manager:
        return

    if visualize_character_development:
        visualize_character_development(series_manager)
    else:
        console.print("[yellow]Character development visualization not available.[/yellow]")


def display_plot_arcs(series_manager) -> None:
    """
    Display plot arc visualization for a series.

    Args:
        series_manager: SeriesManager instance
    """
    if not series_manager:
        return

    if visualize_plot_arcs:
        visualize_plot_arcs(series_manager)
    else:
        console.print("[yellow]Plot arc visualization not available.[/yellow]")


def display_timeline(series_manager) -> None:
    """
    Display timeline visualization for a series.

    Args:
        series_manager: SeriesManager instance
    """
    if not series_manager:
        return

    if visualize_timeline:
        visualize_timeline(series_manager)
    else:
        console.print("[yellow]Timeline visualization not available.[/yellow]")

def generate_cover(novel_data: Dict[str, Any], output_dir: str, auto_mode: bool = False) -> Optional[str]:
    """
    Generate a cover for a novel.

    Args:
        novel_data: Dictionary containing novel data
        output_dir: Directory to save the cover in
        auto_mode: If True, generates cover automatically without user input

    Returns:
        Path to the generated cover image or None if generation was cancelled
    """
    # If not in auto mode, ask if user wants to generate a cover
    if not auto_mode:
        generate_cover = questionary.confirm(
            "Would you like to generate a cover for your novel?",
            default=True,
            style=custom_style
        ).ask()

        if not generate_cover:
            return None

    # Extract novel information
    title = novel_data["metadata"]["title"]
    author = novel_data["metadata"]["author"]
    genre = novel_data["metadata"]["genre"]

    # Check if this is part of a series
    series_info = None
    if "series_info" in novel_data["metadata"]:
        series_info = {
            "series_title": novel_data["metadata"]["series_info"]["series_title"],
            "book_number": novel_data["metadata"]["series_info"]["book_number"]
        }

    # Create cover generator
    cover_generator = CoverGenerator(output_dir=output_dir)

    # Determine design style
    design_style = None
    if not auto_mode:
        # Ask for design style if not in auto mode
        design_style = questionary.select(
            "Select a cover design style:",
            choices=[
                "gradient",
                "geometric",
                "minimalist",
                "textured",
                "abstract",
                "classic",
                "modern",
                "artistic",
                "dramatic",
                "elegant",
                "vintage",
                "bold",
                "sophisticated",
                "cinematic",
                "editorial",
                "random"
            ],
            style=custom_style
        ).ask()

        # If random, set to None to use random selection
        if design_style == "random":
            design_style = None
    else:
        # In auto mode, select design style based on genre with enhanced styles
        genre_style_map = {
            # Fiction genres
            "thriller": "dramatic",
            "mystery": "vintage",
            "mystery/thriller": "bold",
            "science fiction": "modern",
            "fantasy": "artistic",
            "epic fantasy": "dramatic",
            "romance": "elegant",
            "paranormal romance": "artistic",
            "literary fiction": "minimalist",
            "commercial fiction": "modern",
            "contemporary fiction": "modern",
            "historical fiction": "vintage",
            "alternate history": "vintage",
            "horror": "dramatic",
            "young adult": "bold",
            "middle grade": "geometric",
            "children's chapter books": "gradient",
            "urban fantasy": "modern",
            "dystopian": "dramatic",
            "speculative fiction": "modern",
            "novella": "elegant",
            "graphic novel": "artistic",
            "short story collection": "minimalist",

            # Non-fiction genres
            "memoir": "elegant",
            "biography": "classic",
            "history": "vintage",
            "self-help": "modern",
            "business": "minimalist",
            "popular science": "geometric",
            "academic": "minimalist",
            "travel": "artistic",
            "cookbook": "gradient",
            "how-to": "geometric",
            "essay collection": "elegant",
            "philosophy": "minimalist",
            "true crime": "dramatic",
            "poetry collection": "artistic",
            "creative non-fiction": "elegant",

            # Test genre
            "test": "minimalist"
        }

        # Get style based on genre or use random if genre not in map
        design_style = genre_style_map.get(genre.lower(), None)

    # Generate cover
    if not auto_mode:
        console.print("[bold cyan]Generating cover...[/bold cyan]")

    # Check if there's a subtitle
    subtitle = None
    if "subtitle" in novel_data["metadata"]:
        subtitle = novel_data["metadata"]["subtitle"]

    # Get description for enhanced cover generation
    description = novel_data["metadata"].get("description", "")

    # Generate the enhanced cover
    cover_path = cover_generator.generate_cover(
        title=title,
        author=author,
        genre=genre,
        subtitle=subtitle,
        series_info=series_info,
        design_style=design_style,
        description=description
    )

    if not auto_mode:
        console.print(f"[bold green]✓[/bold green] Cover generated successfully: [bold cyan]{cover_path}[/bold cyan]")

        # Ask if user wants to attach the cover to the EPUB
        attach_to_epub = questionary.confirm(
            "Would you like to attach this cover to your EPUB file?",
            default=True,
            style=custom_style
        ).ask()

        if attach_to_epub:
            return cover_path
        else:
            return None
    else:
        # In auto mode, always attach the cover
        return cover_path

def display_generation_complete(output_path: str, is_part_of_series: bool = False, series_title: str = None, book_number: int = None) -> None:
    """
    Display generation complete message.

    Args:
        output_path: Path to the generated EPUB file
        is_part_of_series: Whether the book is part of a series
        series_title: Title of the series (if part of a series)
        book_number: Book number in the series (if part of a series)
    """
    # Get final elapsed time
    elapsed_time = generation_timer.get_elapsed_time()

    console.print("\n[bold green]✓ Novel generation complete![/bold green]")
    console.print(f"[bold green]✓ Your novel has been saved to:[/bold green] [bold cyan]{output_path}[/bold cyan]")
    console.print(f"[bold green]✓ Total generation time:[/bold green] [bold cyan]{elapsed_time}[/bold cyan]")

    if is_part_of_series and series_title and book_number:
        console.print(f"[bold green]✓ This is Book {book_number} in the [/bold green][bold cyan]{series_title}[/bold cyan][bold green] series[/bold green]")


def confirm_generation() -> bool:
    """
    Confirm novel generation.

    Returns:
        True if user confirms, False otherwise
    """
    return questionary.confirm(
        "Ready to generate your novel?",
        default=True,
        style=custom_style
    ).ask()


def display_chapter_preview(chapter_text: str, chapter_num: int, chapter_title: str) -> None:
    """
    Display a preview of a generated chapter.

    Args:
        chapter_text: The chapter text
        chapter_num: Chapter number
        chapter_title: Chapter title
    """
    # Limit preview to first 500 characters
    preview = chapter_text[:500] + "..." if len(chapter_text) > 500 else chapter_text

    console.print(f"\n[bold cyan]Chapter {chapter_num}: {chapter_title}[/bold cyan]")
    console.print(Panel(preview, border_style="cyan", expand=False))
    console.print()


def display_loading_spinner(message: str, duration: float = 2.0) -> None:
    """
    Display a loading spinner with a message.

    Args:
        message: Message to display
        duration: Duration in seconds
    """
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold cyan]{task.description}"),
        TimeElapsedColumn()
    ) as progress:
        task = progress.add_task(message, total=None)
        time.sleep(duration)


def get_custom_generation_options(genre: str) -> Dict[str, Any]:
    """
    Get custom generation options from the user.

    Args:
        genre: The genre of the novel

    Returns:
        Dictionary containing custom options
    """
    console.print("\n[bold cyan]Generation Options[/bold cyan]")

    # Ask if user wants to use recommended settings
    use_recommended = questionary.confirm(
        f"Would you like to use recommended settings for {genre}?",
        default=True,
        style=custom_style
    ).ask()

    if use_recommended:
        # Get recommended settings based on genre
        defaults = get_genre_defaults(genre)

        # Display the recommended settings
        console.print("\n[bold green]Using recommended settings:[/bold green]")

        table = Table(box=box.ROUNDED)
        table.add_column("Setting", style="cyan")
        table.add_column("Value", style="green")

        table.add_row("Target Length", defaults["target_length"].title())
        table.add_row("Writing Style", defaults["writing_style"])
        table.add_row("Point of View", defaults["pov"])
        table.add_row("Themes", ", ".join(defaults["themes"]))
        table.add_row("Recommended Chapter Count", str(defaults["chapter_count"]))
        table.add_row("Target Word Count", f"{defaults['target_word_count']:,}")

        console.print(table)
        console.print()

        return defaults
    else:
        console.print("\n[bold cyan]Custom Generation Options[/bold cyan]")

        # Get target length
        target_length = questionary.select(
            "Select target novel length:",
            choices=["Short", "Medium", "Long"],
            style=custom_style
        ).ask().lower()

        # Get writing style preference
        writing_style = questionary.select(
            "Select writing style preference:",
            choices=[
                "Descriptive and detailed",
                "Concise and direct",
                "Poetic and lyrical",
                "Conversational and casual",
                "Technical and precise"
            ],
            style=custom_style
        ).ask()

        # Get POV preference
        pov = questionary.select(
            "Select point of view:",
            choices=[
                "First person",
                "Third person limited",
                "Third person omniscient",
                "Multiple POVs"
            ],
            style=custom_style
        ).ask()

        # Get theme preference
        themes = questionary.checkbox(
            "Select themes to include:",
            choices=[
                "Coming of age",
                "Love and relationships",
                "Good vs. evil",
                "Identity and self-discovery",
                "Power and corruption",
                "Survival",
                "Redemption",
                "Family",
                "Justice",
                "Technology and society"
            ],
            style=custom_style
        ).ask()

        return {
            "target_length": target_length,
            "writing_style": writing_style,
            "pov": pov,
            "themes": themes
        }
