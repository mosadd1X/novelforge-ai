#!/usr/bin/env python3
"""
Unified command-line interface for the Ebook Generator application.

This script provides a user-friendly main menu system to access all the
functionality of the Ebook Generator, including book generation, series
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
    display_api_key_status,
    custom_style
)
from src.core.gemini_client import GeminiClient

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

# Create console
console = Console()

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

def check_api_key_status():
    """
    Check and display API key status.

    This function displays information about all configured API keys,
    including their validity, usage statistics, and rate limit status.
    It helps users troubleshoot API key issues and monitor usage.

    The function handles exceptions gracefully and provides helpful
    error messages if API keys are not properly configured.

    Returns:
        None
    """
    try:
        # Initialize the Gemini client
        gemini_client = GeminiClient()

        # Display API key status
        display_api_key_status(gemini_client)
    except Exception as e:
        console.print(f"[bold red]Error checking API key status: {str(e)}[/bold red]")
        console.print("[yellow]Make sure your API keys are properly configured in the .env file.[/yellow]")
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

        console.print("[bold cyan]Welcome to the Ebook Generator![/bold cyan]")
        console.print("Please select an option from the menu below:\n")

        choices = [
            "1. Generate a Book",
            "2. Generate a Series",
            "3. Manage Books",
            "4. API Key Status",
            "5. Exit"
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
        elif selected == "4. API Key Status":
            check_api_key_status()
        elif selected == "5. Exit":
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
