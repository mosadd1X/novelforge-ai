"""
Main entry point for the Ebook Generator system.

This module serves as the primary entry point for the Ebook Generator application.
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
from typing import Dict, List, Any, Optional

# Third-party imports
import questionary
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.table import Table
from rich.live import Live
from rich import box

# Local application imports
from src.core.novel_generator import NovelGenerator
from src.formatters.epub_formatter import EpubFormatter
from src.utils.file_handler import create_output_directory, save_novel_json, create_series_directory
from src.core.series_manager import SeriesManager
from src.core.series_generator import SeriesGenerator
from src.utils.logger import init_logger, get_logger, close_logger, log_info, log_error, log_debug, log_warning
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
    display_character_development,
    display_plot_arcs,
    display_timeline,
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


def should_generate_characters(genre: str) -> bool:
    """
    Determine if character generation is needed for a given genre.

    Args:
        genre: The genre of the book

    Returns:
        bool: True if characters should be generated, False otherwise
    """
    # Fiction genres that need characters (narrative content)
    fiction_genres = [
        "literary fiction", "commercial fiction", "mystery", "mystery thriller",
        "thriller", "romance", "fantasy", "epic fantasy", "science fiction",
        "historical fiction", "horror", "young adult", "middle grade",
        "children's chapter books", "speculative fiction", "alternate history",
        "contemporary fiction", "paranormal romance", "urban fantasy", "dystopian",
        "test"  # Include test genre for development
    ]

    # Non-fiction genres that don't need characters (informational content)
    non_fiction_genres = [
        "memoir", "biography", "history", "self help", "business",
        "popular science", "academic", "travel", "cookbook", "how to",
        "philosophy", "true crime"
    ]

    # Special formats that don't need traditional characters
    special_format_genres = [
        "short story collection", "novella", "graphic novel",
        "essay collection", "poetry collection", "creative non fiction"
    ]

    # Normalize genre name for comparison
    genre_normalized = genre.lower().strip()

    # Check if it's a fiction genre that needs characters
    # First check for exact matches
    for fiction_genre in fiction_genres:
        if fiction_genre.lower() == genre_normalized:
            return True

    # Then check for partial matches, but be very careful
    for fiction_genre in fiction_genres:
        # Only allow partial matches if the genre is clearly contained
        if genre_normalized in fiction_genre.lower() and len(genre_normalized) > 3:
            # Avoid false positives like "history" matching fiction genres
            if genre_normalized == "history" and ("historical" in fiction_genre.lower() or "alternate" in fiction_genre.lower()):
                continue
            if genre_normalized == "science" and "science fiction" in fiction_genre.lower():
                continue
            return True

    # All other genres (non-fiction and special formats) don't need characters
    return False


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

        # Check API connection before starting
        console.print("[bold cyan]Checking API connection...[/bold cyan]")
        api_status = generator.gemini.check_api_connection(check_all_keys=True)

        if not api_status["success"]:
            console.print("[bold red]Error: Unable to connect to the Gemini API.[/bold red]")
            console.print("[yellow]Please check your internet connection and API keys before trying again.[/yellow]")
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

        # Generate writer profile
        log_info("Starting writer profile generation", genre=novel_info["genre"])
        console.print("[bold cyan]Generating writer profile...[/bold cyan]")
        try:
            writer_profile = generator.generate_writer_profile()
            log_info("Writer profile generated successfully", profile_length=len(writer_profile) if writer_profile else 0)
            console.print("[bold green]✓[/bold green] Writer profile generated successfully")
        except Exception as e:
            log_error("Failed to generate writer profile", exception=e)
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
            console.print(f"[bold yellow]⏭️[/bold yellow] Skipping character generation (not needed for {novel_info['genre']})")
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
            from rich.columns import Columns
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
            "outline": chapter_outlines,
            "characters": characters,
            "chapters": chapters,
            "word_count": memory_manager.structure["current_word_count"]
        }

        # Save novel as JSON
        save_novel_json(novel, output_dir)

        # Generate cover with manual selection for single novels
        cover_path = generate_cover(novel, output_dir, auto_mode=False)

        # Format and save as EPUB
        console.print("[bold cyan]Formatting EPUB...[/bold cyan]")
        formatter = EpubFormatter(novel)
        epub_path = formatter.save_epub(output_dir, cover_path)

        # Stop the timer
        generation_timer.stop()

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

            console.print("[bold cyan]Welcome to the Novel Generation System![/bold cyan]")
            console.print("You can generate a single novel, work with a series of novels, or manage your book library.\n")

            menu_choices = []
            if series_management_menu:
                menu_choices.append("Series Management Menu")
            if book_management_menu:
                menu_choices.append("Book Management Menu")
            menu_choices.extend(["Generate Single Book (Classic)", "Exit"])

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
            elif selected_menu == "Exit":
                console.print("[bold cyan]Thank you for using the Novel Generation System![/bold cyan]")
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
