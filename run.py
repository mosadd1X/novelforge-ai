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

def main_menu():
    """
    Display the main menu and handle user input.

    This function presents the main application menu with options for
    generating books, managing series, checking API key status, and exiting.
    It handles user selection and routes to the appropriate functionality.

    The menu runs in a loop until the user chooses to exit.

    Returns:
        None
    """
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Welcome to NovelForge AI![/bold cyan]")
        console.print("Please select an option from the menu below:\n")

        choices = [
            "1. Generate a Book",
            "2. Generate a Series",
            "3. Manage Books",
            "4. Advanced Generation Options",
            "5. Content Quality & Feedback",
            "6. API Key Management",
            "7. Network Status & Diagnostics",
            "8. Database Management",
            "9. Fast Testing System",
            "10. Exit"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "1. Generate a Book":
            generate_book()
        elif selected == "2. Generate a Series":
            generate_series()
        elif selected == "3. Manage Books":
            manage_books()
        elif selected == "4. Advanced Generation Options":
            advanced_generation()
        elif selected == "5. Content Quality & Feedback":
            quality_and_feedback()
        elif selected == "6. API Key Management":
            api_key_management()
        elif selected == "7. Network Status & Diagnostics":
            network_status_and_diagnostics()
        elif selected == "8. Database Management":
            database_management()
        elif selected == "9. Fast Testing System":
            fast_testing_system()
        elif selected == "10. Exit":
            console.print("[bold green]Thank you for using the Ebook Generator. Goodbye![/bold green]")
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
