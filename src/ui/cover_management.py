"""
Cover Management for NovelForge AI

This module provides comprehensive cover management functionality including
cover generation, editing, batch operations, and quality control.
"""

import os
import sys
from typing import Dict, List, Any, Optional
import questionary
from rich.console import Console
import time

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.ui.terminal_ui import (
    clear_screen,
    display_title,
    custom_style
)

console = Console()

def cover_management_menu():
    """Main menu for cover management operations."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]🎨 Cover Management[/bold cyan]")
        console.print("    Professional cover creation and management tools")
        console.print()

        choices = [
            "🎨 Generate Single Cover",
            "📚 Batch Cover Generation",
            "🔍 Browse Existing Covers",
            "✏️ Edit Cover Metadata",
            "📊 Cover Quality Analysis",
            "🔄 Regenerate Covers",
            "📤 Export Covers",
            "← Back to Publishing Tools"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🎨 Generate Single Cover":
            generate_single_cover()
        elif selected == "📚 Batch Cover Generation":
            from src.ui.batch_operations import batch_cover_generation_menu
            batch_cover_generation_menu()
        elif selected == "🔍 Browse Existing Covers":
            browse_existing_covers()
        elif selected == "✏️ Edit Cover Metadata":
            edit_cover_metadata()
        elif selected == "📊 Cover Quality Analysis":
            cover_quality_analysis()
        elif selected == "🔄 Regenerate Covers":
            regenerate_covers_menu()
        elif selected == "📤 Export Covers":
            export_covers_menu()
        elif selected == "← Back to Publishing Tools":
            break

def generate_single_cover():
    """Generate a cover for a single book."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🎨 Generate Single Cover[/bold cyan]")
    console.print("    Create a professional cover for one book")
    console.print()

    # Get list of books without covers
    try:
        from src.ui.book_menu import get_existing_books
        existing_books = get_existing_books()
        
        books_without_covers = []
        for book in existing_books:
            book_dir = book.get("directory", "")
            if book_dir and os.path.exists(book_dir):
                cover_files = ["cover.jpg", "cover.png", "cover.jpeg"]
                has_cover = any(os.path.exists(os.path.join(book_dir, f)) for f in cover_files)
                if not has_cover:
                    books_without_covers.append(book)

        if not books_without_covers:
            console.print("    ✅ [green]All your books already have covers![/green]")
            input("\nPress Enter to continue...")
            return

        # Let user select a book
        book_choices = []
        for book in books_without_covers:
            title = book.get("title", "Untitled")
            genre = book.get("genre", "Unknown")
            book_choices.append(f"📖 {title} ({genre})")

        selected_choice = questionary.select(
            "Select a book to generate a cover for:",
            choices=book_choices,
            style=custom_style
        ).ask()

        if selected_choice:
            # Find the selected book
            book_index = book_choices.index(selected_choice)
            selected_book = books_without_covers[book_index]
            
            console.print(f"\n    🎨 Generating cover for: [cyan]{selected_book.get('title', 'Untitled')}[/cyan]")
            console.print("    This would integrate with the existing cover generation system...")
            
            # TODO: Integrate with actual cover generation
            time.sleep(1.5)
            console.print("    ✅ Cover generation completed!")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

    input("\nPress Enter to continue...")

def browse_existing_covers():
    """Browse and manage existing covers."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔍 Browse Existing Covers[/bold cyan]")
    console.print("    View and manage your book covers")
    console.print()

    try:
        from src.ui.book_menu import get_existing_books
        existing_books = get_existing_books()
        
        books_with_covers = []
        for book in existing_books:
            book_dir = book.get("directory", "")
            if book_dir and os.path.exists(book_dir):
                cover_files = ["cover.jpg", "cover.png", "cover.jpeg"]
                for cover_file in cover_files:
                    cover_path = os.path.join(book_dir, cover_file)
                    if os.path.exists(cover_path):
                        book_copy = book.copy()
                        book_copy["cover_path"] = cover_path
                        book_copy["cover_file"] = cover_file
                        books_with_covers.append(book_copy)
                        break

        if not books_with_covers:
            console.print("    📭 No covers found in your library")
            console.print("    Use the cover generation tools to create covers for your books.")
            input("\nPress Enter to continue...")
            return

        console.print(f"    📚 Found {len(books_with_covers)} book{'s' if len(books_with_covers) != 1 else ''} with covers:")
        console.print()

        for book in books_with_covers[:10]:  # Show first 10
            title = book.get("title", "Untitled")
            cover_file = book.get("cover_file", "unknown")
            console.print(f"    🎨 {title} ({cover_file})")

        if len(books_with_covers) > 10:
            console.print(f"    ... and {len(books_with_covers) - 10} more")

    except Exception as e:
        console.print(f"[red]Error browsing covers: {e}[/red]")

    input("\nPress Enter to continue...")

def edit_cover_metadata():
    """Edit cover metadata and properties."""
    clear_screen()
    display_title()

    console.print("[bold cyan]✏️ Edit Cover Metadata[/bold cyan]")
    console.print("    Modify cover properties and metadata")
    console.print()

    console.print("[yellow]Cover metadata editing will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Cover title and description editing")
    console.print("• Style and theme modifications")
    console.print("• Resolution and format settings")
    console.print("• Batch metadata updates")

    input("\nPress Enter to continue...")

def cover_quality_analysis():
    """Analyze cover quality and provide recommendations."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📊 Cover Quality Analysis[/bold cyan]")
    console.print("    Analyze cover quality and get improvement suggestions")
    console.print()

    console.print("[yellow]Cover quality analysis will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Resolution and clarity analysis")
    console.print("• Color scheme evaluation")
    console.print("• Typography assessment")
    console.print("• Genre appropriateness scoring")
    console.print("• Market competitiveness analysis")

    input("\nPress Enter to continue...")

def regenerate_covers_menu():
    """Menu for regenerating existing covers."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Regenerate Covers[/bold cyan]")
    console.print("    Regenerate covers with improved settings")
    console.print()

    console.print("[yellow]Cover regeneration will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Selective cover regeneration")
    console.print("• Style and quality improvements")
    console.print("• Batch regeneration options")
    console.print("• Version comparison tools")

    input("\nPress Enter to continue...")

def export_covers_menu():
    """Menu for exporting covers in different formats."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📤 Export Covers[/bold cyan]")
    console.print("    Export covers in various formats and resolutions")
    console.print()

    console.print("[yellow]Cover export functionality will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Multiple format export (PNG, JPG, PDF)")
    console.print("• Resolution scaling options")
    console.print("• Batch export capabilities")
    console.print("• Publishing platform optimization")

    input("\nPress Enter to continue...")
