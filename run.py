#!/usr/bin/env python3
"""
Unified command-line interface for the NovelForge AI application.

This script provides a user-friendly main menu system to access all the
functionality of NovelForge AI, including book generation, series
management, and API key status checking. It serves as the recommended
entry point for most users.

Usage:
    python run.py
"""
# Standard library imports
import os
import sys

# Third-party imports
import questionary
from rich.console import Console

# Local application imports
from src.main import main
from src.ui.terminal_ui import (
    clear_screen,
    display_title,
    custom_style
)

# Import series menu
try:
    from src.ui.series_menu import series_management_menu
except ImportError:
    series_management_menu = None

# Import book management menu
try:
    from src.ui.book_menu import book_management_menu
except ImportError:
    book_management_menu = None

# Import advanced generation options
try:
    from src.ui.advanced_generation_options import advanced_options
except ImportError:
    advanced_options = None

# Import feedback system
try:
    from src.ui.feedback_system import feedback_ui
except ImportError:
    feedback_ui = None

# Import database management
try:
    from src.ui.database_menu import database_management_menu
except ImportError:
    database_management_menu = None

# Create console with markup enabled
console = Console(markup=True)

def generate_book():
    """
    Run the book generation functionality.

    This function calls the main entry point in src.main to start the
    book generation process, which guides the user through creating
    a single novel.

    Returns:
        None
    """
    main()

def generate_series():
    """
    Run the series generation functionality.

    This function calls the series management menu to start the
    series generation process, which guides the user through creating
    a series of novels with consistent characters and plot arcs.

    If the series management functionality is not available, it displays
    an error message with troubleshooting information.

    Returns:
        None
    """
    if series_management_menu:
        series_management_menu()
    else:
        console.print("[bold red]Error: Series management functionality not available.[/bold red]")
        input("\nPress Enter to continue...")

def manage_books():
    """
    Run the book management functionality.

    This function calls the book management menu to start the
    book management process, which allows users to work with
    existing books, browse their library, and perform various
    book-related operations.

    If the book management functionality is not available, it displays
    an error message with troubleshooting information.

    Returns:
        None
    """
    if book_management_menu:
        book_management_menu()
    else:
        console.print("[bold red]Error: Book management functionality not available.[/bold red]")
        input("\nPress Enter to continue...")

def advanced_generation():
    """
    Run the advanced generation options functionality.

    This function provides access to smart generation presets including:
    - Surprise Me Mode (full automation)
    - Author Focus Mode (explore specific fictional authors)
    - Cultural Journey Mode (explore different cultural perspectives)
    - Genre Fusion Mode (blend multiple genres)

    If the advanced generation functionality is not available, it displays
    an error message with troubleshooting information.

    Returns:
        None
    """
    if advanced_options:
        try:
            # Get advanced generation options from user
            advanced_result = advanced_options.show_advanced_options_menu()

            if advanced_result:
                # Use the advanced options to generate a book
                console.print(f"\n[bold green]Starting Advanced Generation![/bold green]")

                # Import the advanced generation function
                from src.main import main_with_advanced_options
                main_with_advanced_options(advanced_result)

        except Exception as e:
            console.print(f"[bold red]Error in advanced generation: {str(e)}[/bold red]")
            input("\nPress Enter to continue...")
    else:
        console.print("[bold red]Error: Advanced generation functionality not available.[/bold red]")
        input("\nPress Enter to continue...")

def quality_and_feedback():
    """
    Run the content quality and feedback functionality.

    This function provides access to:
    - Content quality metrics and analytics
    - User feedback collection and analysis
    - Author performance comparisons
    - Quality improvement recommendations

    If the feedback functionality is not available, it displays
    an error message with troubleshooting information.

    Returns:
        None
    """
    if feedback_ui:
        try:
            feedback_ui.feedback_menu()
        except Exception as e:
            console.print(f"[bold red]Error in feedback system: {str(e)}[/bold red]")
            input("\nPress Enter to continue...")
    else:
        console.print("[bold red]Error: Feedback system functionality not available.[/bold red]")
        input("\nPress Enter to continue...")

def api_key_management():
    """
    Run the API Key Management functionality.

    This function provides access to comprehensive API key management including:
    - Adding new API keys with automatic rotation
    - Viewing all configured API keys
    - Removing backup API keys
    - Promoting backup keys to main
    - Testing API key functionality
    - Real-time status monitoring

    The function handles exceptions gracefully and provides helpful
    error messages if the API key management system is not available.

    Returns:
        None
    """
    try:
        # Import the API key management menu
        from src.utils.api_key_manager import show_api_key_management_menu

        # Show the API key management menu
        show_api_key_management_menu()

    except ImportError:
        console.print("[bold red]Error: API Key Management system not available.[/bold red]")
        console.print("[yellow]The API key management functionality could not be loaded.[/yellow]")
        input("\nPress Enter to continue...")
    except Exception as e:
        console.print(f"[bold red]Error in API Key Management: {str(e)}[/bold red]")
        console.print("[yellow]Make sure your system is properly configured.[/yellow]")
        input("\nPress Enter to continue...")

def network_status_and_diagnostics():
    """
    Run the Network Status and Diagnostics functionality.

    This function provides access to comprehensive network monitoring including:
    - Real-time network status monitoring
    - Connection history and metrics
    - Network diagnostics and troubleshooting
    - Circuit breaker status
    - Live monitoring capabilities
    - Network resilience configuration

    The function handles exceptions gracefully and provides helpful
    error messages if the network monitoring system is not available.

    Returns:
        None
    """
    try:
        # Import the network status UI
        from src.ui.network_status_ui import NetworkStatusUI

        # Create and show the network status menu
        network_ui = NetworkStatusUI()
        network_ui.interactive_menu()

    except ImportError:
        console.print("[bold red]Error: Network Status system not available.[/bold red]")
        console.print("[yellow]The network monitoring functionality could not be loaded.[/yellow]")
        console.print("[yellow]Make sure the required dependencies are installed:[/yellow]")
        console.print("• pip install requests psutil")
        input("\nPress Enter to continue...")
    except Exception as e:
        console.print(f"[bold red]Error in Network Status system: {str(e)}[/bold red]")
        console.print("[yellow]Make sure your system is properly configured.[/yellow]")
        input("\nPress Enter to continue...")

def test_responsive_separators():
    """Test and demonstrate responsive separator functionality."""
    clear_screen()
    display_title()

    try:
        from src.ui.responsive_separator import (
            separator, title_separator, section_separator,
            equals_separator, dash_separator, get_terminal_width
        )

        console.print("[bold cyan]🧪 Responsive Separator Testing[/bold cyan]")
        console.print("    Test how separators adapt to terminal width")
        console.print()

        current_width = get_terminal_width()
        console.print(f"    📏 Current terminal width: [cyan]{current_width}[/cyan] characters")
        console.print()

        console.print("1. Full equals separator:")
        console.print(equals_separator())
        console.print()

        console.print("2. Title separator:")
        console.print(title_separator("NovelForge AI"))
        console.print()

        console.print("3. Section separator:")
        console.print(section_separator("API Configuration", "-", "simple"))
        console.print()

        console.print("4. Centered separator:")
        console.print(separator("*", "centered"))
        console.print()

        console.print("5. Padded separator:")
        console.print(separator("-", "padded"))
        console.print()

        console.print("[bold green]✅ Responsive separators working correctly![/bold green]")
        console.print()
        console.print("[bold cyan]💡 Try This:[/bold cyan]")
        console.print("    • Resize your terminal window")
        console.print("    • Run this test again to see separators adapt")
        console.print("    • Separators automatically adjust to new width")

    except ImportError:
        console.print("[red]Error: Responsive separator module not available[/red]")
    except Exception as e:
        console.print(f"[red]Error testing separators: {e}[/red]")

    input("\nPress Enter to continue...")

def database_management():
    """
    Run the Database Management functionality.

    This function provides access to comprehensive database management including:
    - Database statistics and monitoring
    - Data migration from file system to database
    - Book display settings and filtering
    - Database maintenance and optimization
    - Data export and backup operations

    The function handles exceptions gracefully and provides helpful
    error messages if the database management system is not available.

    Returns:
        None
    """
    if database_management_menu:
        try:
            database_management_menu()
        except Exception as e:
            console.print(f"[bold red]Error in Database Management: {str(e)}[/bold red]")
            input("\nPress Enter to continue...")
    else:
        console.print("[bold red]Error: Database Management functionality not available.[/bold red]")
        input("\nPress Enter to continue...")

def fast_testing_system() -> None:
    """
    Run the fast testing system for development and debugging.

    Returns:
        None
    """
    try:
        clear_screen()
        display_title()

        console.print("[bold cyan]Fast Testing System[/bold cyan]")
        console.print("This system provides rapid testing of the ebook generation workflow")
        console.print("with optimized settings for development and debugging.\n")

        # Test mode options
        test_options = [
            "1. Run All Tests (Standard Mode)",
            "2. Run All Tests (Mock API Mode - Fastest)",
            "3. Single Book Test Only",
            "4. Series Test Only",
            "5. Performance Benchmarks Only",
            "6. Back to Main Menu"
        ]

        selected = questionary.select(
            "Select testing mode:",
            choices=test_options,
            style=custom_style
        ).ask()

        if selected == "6. Back to Main Menu":
            return

        # Import and run the fast testing system
        from src.testing.fast_test_system import FastTestSystem

        use_mock_api = "Mock API" in selected

        console.print(f"\n[bold yellow]Starting fast testing system...[/bold yellow]")
        console.print(f"Mock API: {'Enabled' if use_mock_api else 'Disabled'}")
        console.print("This may take 5-10 minutes depending on the selected tests.\n")

        # Confirm before starting
        proceed = questionary.confirm(
            "Do you want to proceed with the testing?",
            default=True,
            style=custom_style
        ).ask()

        if not proceed:
            console.print("[bold yellow]Testing cancelled.[/bold yellow]")
            input("\nPress Enter to continue...")
            return

        # Initialize and run tests
        test_system = FastTestSystem(use_mock_api=use_mock_api)

        if "All Tests" in selected:
            results = test_system.run_comprehensive_tests()
        elif "Single Book" in selected:
            results = {"Single Book Test": test_system._test_single_book_standard()}
        elif "Series Test" in selected:
            results = {"Series Test": test_system._test_series_generation()}
        elif "Performance" in selected:
            results = {"Performance Test": test_system._test_performance_benchmarks()}
        else:
            results = test_system.run_comprehensive_tests()

        console.print(f"\n[bold green]Testing completed![/bold green]")
        console.print("Check the test_reports directory for detailed results.")

        input("\nPress Enter to continue...")

    except ImportError as e:
        console.print(f"[bold red]Error: Fast testing system not available: {e}[/bold red]")
        input("\nPress Enter to continue...")
    except Exception as e:
        console.print(f"[bold red]Error in fast testing system: {str(e)}[/bold red]")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")
        input("\nPress Enter to continue...")

def get_content_creation_suggestions():
    """Get context-aware suggestions for content creation."""
    suggestions = []

    try:
        # Import here to avoid circular imports
        from src.ui.book_menu import get_existing_books

        existing_books = get_existing_books()

        # Suggest creating covers for books without them
        books_without_covers = []
        for book in existing_books:
            cover_path = os.path.join(book.get("directory", ""), "cover.jpg")
            if not os.path.exists(cover_path):
                books_without_covers.append(book)

        if books_without_covers:
            suggestions.append({
                "type": "missing_covers",
                "count": len(books_without_covers),
                "books": books_without_covers[:3]  # Show first 3
            })

        # Suggest creating series if user has multiple books in same genre
        genre_counts = {}
        for book in existing_books:
            genre = book.get("genre", "Unknown")
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

        for genre, count in genre_counts.items():
            if count >= 2 and genre != "Unknown":
                suggestions.append({
                    "type": "series_opportunity",
                    "genre": genre,
                    "count": count
                })
                break  # Only suggest one series opportunity

        # Suggest continuing if there are incomplete generations
        # This would be implemented based on your generation tracking system

    except Exception as e:
        # Silently handle errors to avoid breaking the menu
        pass

    return suggestions

def show_content_creation_suggestions(suggestions):
    """Display context-aware suggestions to the user."""
    clear_screen()
    display_title()

    console.print("[bold cyan]💡 Smart Suggestions[/bold cyan]")
    console.print("    Personalized recommendations based on your library")
    console.print()

    choices = []

    for suggestion in suggestions:
        if suggestion["type"] == "missing_covers":
            count = suggestion["count"]
            choices.append(f"🎨 Create covers for {count} book{'s' if count != 1 else ''} without covers")
        elif suggestion["type"] == "series_opportunity":
            genre = suggestion["genre"]
            count = suggestion["count"]
            choices.append(f"📚 Create a {genre} series from your {count} existing books")

    choices.append("← Back to Content Creation")

    if not choices[:-1]:  # Only back option available
        console.print("    ℹ️ No suggestions available at this time")
        input("\nPress Enter to continue...")
        return

    selected = questionary.select(
        "Choose a suggestion:",
        choices=choices,
        style=custom_style
    ).ask()

    if selected and "Create covers" in selected:
        # Navigate to cover creation workflow
        console.print("[yellow]Cover creation workflow will be implemented in the next phase.[/yellow]")
        input("\nPress Enter to continue...")
    elif selected and "Create a" in selected and "series" in selected:
        # Navigate to series creation workflow
        console.print("[yellow]Series creation workflow will be implemented in the next phase.[/yellow]")
        input("\nPress Enter to continue...")

def quick_start_wizard():
    """Quick Start wizard for new users - guided first book generation."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🚀 Quick Start Wizard[/bold cyan]")
    console.print("    Welcome! Let's create your first book together")
    console.print()

    console.print("[bold green]Step 1 of 5: Welcome[/bold green]")
    console.print()
    console.print("    This wizard will guide you through creating your first book with NovelForge AI.")
    console.print("    We'll help you choose a genre, set up your preferences, and generate a complete book.")
    console.print()

    proceed = questionary.confirm(
        "Ready to start your publishing journey?",
        default=True,
        style=custom_style
    ).ask()

    if not proceed:
        return

    # Step 2: Genre Selection
    genre = quick_start_genre_selection()
    if not genre:
        return

    # Step 3: Book Preferences
    preferences = quick_start_preferences(genre)
    if not preferences:
        return

    # Step 4: Confirmation
    if not quick_start_confirmation(genre, preferences):
        return

    # Step 5: Generation with integrated workflow
    quick_start_generation(genre, preferences)

def quick_start_genre_selection():
    """Step 2: Genre selection for Quick Start wizard."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🚀 Quick Start Wizard[/bold cyan]")
    console.print("[bold green]Step 2 of 5: Choose Your Genre[/bold green]")
    console.print()

    # Popular genres for beginners
    popular_genres = [
        "Romance",
        "Mystery",
        "Science Fiction",
        "Fantasy",
        "Thriller",
        "Adventure",
        "Historical Fiction",
        "Contemporary Fiction"
    ]

    console.print("    📖 Let's start with a popular genre that's perfect for beginners:")
    console.print()

    choices = popular_genres + ["🎲 Surprise me!", "📋 See all genres", "← Back to Content Creation"]

    selected = questionary.select(
        "Which genre interests you most?",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "← Back to Content Creation":
        return None
    elif selected == "🎲 Surprise me!":
        import random
        return random.choice(popular_genres)
    elif selected == "📋 See all genres":
        # Show full genre list
        try:
            from src.core.genre_config import get_all_genres
            all_genres = get_all_genres()
            selected = questionary.select(
                "Choose from all available genres:",
                choices=all_genres + ["← Back"],
                style=custom_style
            ).ask()
            return selected if selected != "← Back" else None
        except ImportError:
            return questionary.select(
                "Choose a genre:",
                choices=popular_genres + ["← Back"],
                style=custom_style
            ).ask()
    else:
        return selected

def quick_start_preferences(genre):
    """Step 3: Book preferences for Quick Start wizard."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🚀 Quick Start Wizard[/bold cyan]")
    console.print("[bold green]Step 3 of 5: Book Preferences[/bold green]")
    console.print()

    console.print(f"    📚 Great choice! You've selected: [cyan]{genre}[/cyan]")
    console.print()

    # Book length
    console.print("    📏 How long would you like your book to be?")
    length = questionary.select(
        "Book length:",
        choices=[
            "Short (5-10 chapters, quick read)",
            "Medium (10-15 chapters, standard novel)",
            "Long (15-20 chapters, epic story)",
            "← Back to genre selection"
        ],
        style=custom_style
    ).ask()

    if length == "← Back to genre selection":
        return None

    # Writing style
    console.print()
    console.print("    ✍️ What writing style do you prefer?")
    style = questionary.select(
        "Writing style:",
        choices=[
            "Descriptive (rich details and imagery)",
            "Conversational (easy to read, engaging)",
            "Dramatic (intense and emotional)",
            "Classic (traditional literary style)",
            "← Back to length selection"
        ],
        style=custom_style
    ).ask()

    if style == "← Back to length selection":
        return None

    # Target audience
    console.print()
    console.print("    🎯 Who is your target audience?")
    audience = questionary.select(
        "Target audience:",
        choices=[
            "Young Adult",
            "Adult",
            "General Audience",
            "← Back to style selection"
        ],
        style=custom_style
    ).ask()

    if audience == "← Back to style selection":
        return None

    return {
        "length": length,
        "style": style,
        "audience": audience
    }

def quick_start_confirmation(genre, preferences):
    """Step 4: Confirmation for Quick Start wizard."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🚀 Quick Start Wizard[/bold cyan]")
    console.print("[bold green]Step 4 of 5: Confirmation[/bold green]")
    console.print()

    console.print("    ✨ Perfect! Here's what we'll create for you:")
    console.print()
    console.print(f"    📖 Genre: [cyan]{genre}[/cyan]")
    console.print(f"    📏 Length: [cyan]{preferences['length']}[/cyan]")
    console.print(f"    ✍️ Style: [cyan]{preferences['style']}[/cyan]")
    console.print(f"    🎯 Audience: [cyan]{preferences['audience']}[/cyan]")
    console.print()

    console.print("    🔄 The complete workflow will include:")
    console.print("    • Generate your book content")
    console.print("    • Create a professional cover")
    console.print("    • Generate EPUB format")
    console.print("    • Export for publishing")
    console.print()

    return questionary.confirm(
        "Ready to create your book?",
        default=True,
        style=custom_style
    ).ask()

def quick_start_generation(genre, preferences):
    """Step 5: Generation with integrated workflow for Quick Start wizard."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🚀 Quick Start Wizard[/bold cyan]")
    console.print("[bold green]Step 5 of 5: Creating Your Book[/bold green]")
    console.print()

    console.print("    🎉 Excellent! Let's create your book with our integrated workflow.")
    console.print()

    # For now, redirect to standard book generation
    # In a full implementation, this would use the integrated workflow
    console.print("    📝 Starting book generation...")
    console.print()

    try:
        # This would be replaced with the integrated workflow
        generate_book()

        console.print()
        console.print("    🎊 [bold green]Congratulations![/bold green]")
        console.print("    Your first book has been created successfully!")
        console.print()
        console.print("    💡 [bold cyan]Next steps you might want to try:[/bold cyan]")
        console.print("    • Create a cover for your book")
        console.print("    • Generate an EPUB file")
        console.print("    • Create more books in the same genre")
        console.print("    • Start a book series")
        console.print()

    except Exception as e:
        console.print(f"    ❌ [red]Error during generation: {e}[/red]")
        console.print("    Don't worry! You can try again from the main menu.")

    input("\nPress Enter to continue...")

def content_creation_menu():
    """Display the Content Creation submenu with workflow integration."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]📚 Content Creation[/bold cyan]")
        console.print("    Generate books and series with AI-powered creativity")
        console.print()

        # Check for context-aware suggestions
        context_suggestions = get_content_creation_suggestions()

        choices = [
            "🚀 Quick Start Wizard",
            "📖 Generate a Book",
            "📚 Generate a Series",
            "📚 Enhanced Series Workflows",
            "🎨 Creative Generation Modes",
            "⚡ One-Click Publishing"
        ]

        # Add context-aware suggestions if available
        if context_suggestions:
            choices.insert(-1, "💡 Smart Suggestions")

        choices.append("← Back to Main Menu")

        selected = questionary.select(
            "What would you like to create?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🚀 Quick Start Wizard":
            quick_start_wizard()
        elif selected == "📖 Generate a Book":
            generate_book()
        elif selected == "📚 Generate a Series":
            generate_series()
        elif selected == "📚 Enhanced Series Workflows":
            try:
                from src.ui.enhanced_series_workflows import enhanced_series_workflows_menu
                enhanced_series_workflows_menu()
            except ImportError:
                console.print("[red]Error: Enhanced series workflows module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "🎨 Creative Generation Modes":
            advanced_generation()
        elif selected == "⚡ One-Click Publishing":
            try:
                from src.ui.one_click_publishing import one_click_publishing_menu
                one_click_publishing_menu()
            except ImportError:
                console.print("[red]Error: One-click publishing module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "💡 Smart Suggestions":
            show_content_creation_suggestions(context_suggestions)
        elif selected == "← Back to Main Menu":
            break

def get_library_context():
    """Get context information about the user's library."""
    context = {
        "total_books": 0,
        "recent_books": [],
        "incomplete_books": [],
        "books_without_covers": [],
        "books_without_epub": []
    }

    try:
        from src.ui.book_menu import get_existing_books
        existing_books = get_existing_books()

        context["total_books"] = len(existing_books)

        # Sort by creation date to get recent books
        sorted_books = sorted(existing_books,
                            key=lambda x: x.get("created_at", ""),
                            reverse=True)
        context["recent_books"] = sorted_books[:3]  # Last 3 books

        # Check for incomplete books (this would be based on your status tracking)
        for book in existing_books:
            # Check if book directory exists but is incomplete
            book_dir = book.get("directory", "")
            if book_dir and os.path.exists(book_dir):
                # Check for missing files that indicate incomplete generation
                expected_files = ["outline.txt", "characters.json"]
                missing_files = [f for f in expected_files
                               if not os.path.exists(os.path.join(book_dir, f))]
                if missing_files:
                    context["incomplete_books"].append(book)

                # Check for missing covers
                cover_path = os.path.join(book_dir, "cover.jpg")
                if not os.path.exists(cover_path):
                    context["books_without_covers"].append(book)

                # Check for missing EPUB
                epub_path = os.path.join(book_dir, f"{book.get('title', 'book')}.epub")
                if not os.path.exists(epub_path):
                    context["books_without_epub"].append(book)

    except Exception as e:
        # Silently handle errors to avoid breaking the menu
        pass

    return context

def continue_recent_work(recent_books):
    """Allow user to continue working on recent books."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Continue Recent Work[/bold cyan]")
    console.print("    Pick up where you left off with your recent books")
    console.print()

    if not recent_books:
        console.print("    ℹ️ No recent books found")
        input("\nPress Enter to continue...")
        return

    choices = []
    for book in recent_books:
        title = book.get("title", "Untitled")
        genre = book.get("genre", "Unknown")
        choices.append(f"📖 {title} ({genre})")

    choices.append("← Back to Library Management")

    selected = questionary.select(
        "Which book would you like to continue working on?",
        choices=choices,
        style=custom_style
    ).ask()

    if selected and selected != "← Back to Library Management":
        # Extract book index and open book options
        book_index = choices.index(selected)
        selected_book = recent_books[book_index]

        # Import and call book options menu
        try:
            from src.ui.book_menu import book_options_menu
            book_options_menu(selected_book)
        except ImportError:
            console.print("[red]Error: Could not load book management functions[/red]")
            input("\nPress Enter to continue...")

def complete_unfinished_books(incomplete_books):
    """Help user complete unfinished book generations."""
    clear_screen()
    display_title()

    console.print("[bold cyan]⚠️ Complete Unfinished Books[/bold cyan]")
    console.print("    Finish books that were interrupted during generation")
    console.print()

    if not incomplete_books:
        console.print("    ✅ All your books are complete!")
        input("\nPress Enter to continue...")
        return

    console.print(f"    Found {len(incomplete_books)} incomplete book{'s' if len(incomplete_books) != 1 else ''}:")
    console.print()

    choices = []
    for book in incomplete_books:
        title = book.get("title", "Untitled")
        genre = book.get("genre", "Unknown")
        choices.append(f"⚠️ {title} ({genre})")

    choices.extend([
        "🔄 Complete All Books",
        "← Back to Library Management"
    ])

    selected = questionary.select(
        "Which book would you like to complete?",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "🔄 Complete All Books":
        console.print("[yellow]Batch completion workflow will be implemented in the next phase.[/yellow]")
        input("\nPress Enter to continue...")
    elif selected and selected != "← Back to Library Management":
        # Extract book index and open book options
        book_index = next(i for i, choice in enumerate(choices)
                         if choice == selected and choice.startswith("⚠️"))
        selected_book = incomplete_books[book_index]

        # Import and call book options menu
        try:
            from src.ui.book_menu import book_options_menu
            book_options_menu(selected_book)
        except ImportError:
            console.print("[red]Error: Could not load book management functions[/red]")
            input("\nPress Enter to continue...")

def library_management_menu():
    """Display the Library Management submenu with context-aware features."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]📖 Library Management[/bold cyan]")
        console.print("    Organize and manage your book collection")
        console.print()

        # Get context-aware information
        library_context = get_library_context()

        # Display library status
        if library_context["total_books"] > 0:
            console.print(f"    📚 Your library: {library_context['total_books']} books")
            if library_context["recent_books"]:
                recent_book = library_context["recent_books"][0]
                console.print(f"    📖 Most recent: [cyan]{recent_book['title']}[/cyan]")
        else:
            console.print("    📚 Your library is empty - time to create your first book!")
        console.print()

        choices = [
            "📚 Manage Books",
            "🔍 Browse Library",
            "💡 Import from Ideas"
        ]

        # Add context-aware options
        if library_context["recent_books"]:
            choices.insert(1, "🔄 Continue Recent Work")

        if library_context["incomplete_books"]:
            choices.insert(-1, "⚠️ Complete Unfinished Books")

        choices.append("← Back to Main Menu")

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "📚 Manage Books":
            manage_books()
        elif selected == "🔍 Browse Library":
            manage_books()  # Same functionality for now
        elif selected == "💡 Import from Ideas":
            manage_books()  # Will be enhanced in future
        elif selected == "🔄 Continue Recent Work":
            continue_recent_work(library_context["recent_books"])
        elif selected == "⚠️ Complete Unfinished Books":
            try:
                from src.ui.batch_operations import complete_all_unfinished_books_workflow
                complete_all_unfinished_books_workflow()
            except ImportError:
                complete_unfinished_books(library_context["incomplete_books"])
        elif selected == "← Back to Main Menu":
            break

def publishing_tools_menu():
    """Display the Publishing Tools submenu with batch operations."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]🎨 Publishing Tools[/bold cyan]")
        console.print("    Professional publishing and quality control tools")
        console.print()

        choices = [
            "🎨 Cover Management",
            "📤 Format & Export",
            "📱 Telegram Publishing",
            "🔄 Batch Operations",
            "✅ Quality Control & Reviews",
            "← Back to Main Menu"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🎨 Cover Management":
            try:
                from src.ui.cover_management import cover_management_menu
                cover_management_menu()
            except ImportError:
                console.print("[red]Error: Cover management module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "📤 Format & Export":
            try:
                from src.ui.format_export import format_export_menu
                format_export_menu()
            except ImportError:
                console.print("[red]Error: Format & export module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "📱 Telegram Publishing":
            try:
                from src.ui.telegram_publishing import telegram_publishing_menu
                telegram_publishing_menu()
            except ImportError:
                console.print("[red]Error: Telegram publishing module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "🔄 Batch Operations":
            batch_operations_menu()
        elif selected == "✅ Quality Control & Reviews":
            quality_and_feedback()
        elif selected == "← Back to Main Menu":
            break

def batch_operations_menu():
    """Display the Batch Operations submenu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]🔄 Batch Operations[/bold cyan]")
        console.print("    Process multiple books efficiently with automated workflows")
        console.print()

        choices = [
            "🎨 Batch Cover Generation",
            "📚 Batch EPUB Generation",
            "📤 Batch Export Operations",
            "🔄 Complete All Unfinished Books",
            "← Back to Publishing Tools"
        ]

        selected = questionary.select(
            "What batch operation would you like to perform?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🎨 Batch Cover Generation":
            try:
                from src.ui.batch_operations import batch_cover_generation_menu
                batch_cover_generation_menu()
            except ImportError:
                console.print("[red]Error: Batch operations module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "📚 Batch EPUB Generation":
            try:
                from src.ui.batch_operations import batch_epub_generation_menu
                batch_epub_generation_menu()
            except ImportError:
                console.print("[red]Error: Batch operations module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "📤 Batch Export Operations":
            try:
                from src.ui.batch_operations import batch_export_menu
                batch_export_menu()
            except ImportError:
                console.print("[red]Error: Batch operations module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "🔄 Complete All Unfinished Books":
            try:
                from src.ui.batch_operations import complete_all_unfinished_books_workflow
                complete_all_unfinished_books_workflow()
            except ImportError:
                console.print("[red]Error: Batch operations module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "← Back to Publishing Tools":
            break

def system_settings_menu():
    """Display the System Settings submenu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]⚙️ System Settings[/bold cyan]")
        console.print("    Configure and manage system components")
        console.print()

        choices = [
            "🔑 API Key Management",
            "💾 Data & Storage",
            "🌐 Connection & Performance",
            "🧠 Smart Recommendations",
            "🧪 Test Responsive Separators",
            "← Back to Main Menu"
        ]

        selected = questionary.select(
            "What would you like to configure?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🔑 API Key Management":
            api_key_management()
        elif selected == "💾 Data & Storage":
            database_management()
        elif selected == "🌐 Connection & Performance":
            network_status_and_diagnostics()
        elif selected == "🧠 Smart Recommendations":
            try:
                from src.ui.smart_workflow_recommendations import smart_workflow_recommendations_menu
                smart_workflow_recommendations_menu()
            except ImportError:
                console.print("[red]Error: Smart recommendations module not available[/red]")
                input("\nPress Enter to continue...")
        elif selected == "🧪 Test Responsive Separators":
            test_responsive_separators()
        elif selected == "← Back to Main Menu":
            break

def developer_tools_menu():
    """Display the Developer Tools submenu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]🧪 Developer Tools[/bold cyan]")
        console.print("    Testing and development utilities")
        console.print()

        choices = [
            "Fast Testing System",
            "← Back to Main Menu"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Fast Testing System":
            fast_testing_system()
        elif selected == "← Back to Main Menu":
            break

def main_menu():
    """
    Display the main menu and handle user input.

    This function presents the main application menu with a reorganized
    category-based structure for better user experience and workflow integration.
    It handles user selection and routes to the appropriate functionality.

    The menu runs in a loop until the user chooses to exit.

    Returns:
        None
    """
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Welcome to NovelForge AI![/bold cyan]")
        console.print("    Your AI-powered publishing platform for creating professional ebooks")
        console.print()

        choices = [
            "📚 Content Creation",
            "📖 Library Management",
            "🎨 Publishing Tools",
            "⚙️ System Settings",
            "🧪 Developer Tools",
            "Exit"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "📚 Content Creation":
            content_creation_menu()
        elif selected == "📖 Library Management":
            library_management_menu()
        elif selected == "🎨 Publishing Tools":
            publishing_tools_menu()
        elif selected == "⚙️ System Settings":
            system_settings_menu()
        elif selected == "🧪 Developer Tools":
            developer_tools_menu()
        elif selected == "Exit":
            console.print("\n[bold green]Thank you for using NovelForge AI. Goodbye![/bold green]")
            sys.exit(0)

if __name__ == "__main__":
    """
    Main entry point when script is run directly.

    Handles exceptions gracefully, including keyboard interrupts
    and unexpected errors, providing appropriate user feedback.
    """
    try:
        main_menu()
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Program terminated by user.[/bold yellow]")
        sys.exit(0)
    except Exception as e:
        console.print(f"\n[bold red]Error: {str(e)}[/bold red]")
        sys.exit(1)
