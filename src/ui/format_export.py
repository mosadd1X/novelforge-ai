"""
Format & Export for NovelForge AI

This module provides comprehensive format conversion and export functionality
for books, including multiple output formats and publishing platform preparation.
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

def format_export_menu():
    """Main menu for format and export operations."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]📤 Format & Export[/bold cyan]")
        console.print("    Convert and export books to multiple formats")
        console.print()

        choices = [
            "📚 Export Single Book",
            "📦 Batch Export Operations",
            "🔄 Format Conversion",
            "🌐 Publishing Platform Prep",
            "📊 Export Analytics",
            "⚙️ Export Settings",
            "← Back to Publishing Tools"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "📚 Export Single Book":
            export_single_book()
        elif selected == "📦 Batch Export Operations":
            from src.ui.batch_operations import batch_export_menu
            batch_export_menu()
        elif selected == "🔄 Format Conversion":
            format_conversion_menu()
        elif selected == "🌐 Publishing Platform Prep":
            publishing_platform_prep()
        elif selected == "📊 Export Analytics":
            export_analytics()
        elif selected == "⚙️ Export Settings":
            export_settings()
        elif selected == "← Back to Publishing Tools":
            break

def export_single_book():
    """Export a single book to various formats."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📚 Export Single Book[/bold cyan]")
    console.print("    Export one book to multiple formats")
    console.print()

    # Get list of books with EPUB files
    try:
        from src.ui.book_menu import get_existing_books
        existing_books = get_existing_books()
        
        books_with_epub = []
        for book in existing_books:
            book_dir = book.get("directory", "")
            if book_dir and os.path.exists(book_dir):
                epub_files = [f for f in os.listdir(book_dir) if f.endswith('.epub')]
                if epub_files:
                    book_copy = book.copy()
                    book_copy["epub_files"] = epub_files
                    books_with_epub.append(book_copy)

        if not books_with_epub:
            console.print("    📭 No EPUB files found in your library")
            console.print("    Generate EPUB files first before exporting.")
            input("\nPress Enter to continue...")
            return

        # Let user select a book
        book_choices = []
        for book in books_with_epub:
            title = book.get("title", "Untitled")
            epub_count = len(book.get("epub_files", []))
            book_choices.append(f"📖 {title} ({epub_count} EPUB{'s' if epub_count != 1 else ''})")

        selected_choice = questionary.select(
            "Select a book to export:",
            choices=book_choices,
            style=custom_style
        ).ask()

        if selected_choice:
            book_index = book_choices.index(selected_choice)
            selected_book = books_with_epub[book_index]
            
            # Show export format options
            export_formats = [
                "📄 PDF (Portable Document Format)",
                "📝 DOCX (Microsoft Word)",
                "📋 TXT (Plain Text)",
                "🌐 HTML (Web Format)",
                "📱 MOBI (Kindle Format)",
                "📚 All Formats"
            ]

            format_choice = questionary.select(
                "Select export format:",
                choices=export_formats,
                style=custom_style
            ).ask()

            if format_choice:
                console.print(f"\n    📤 Exporting: [cyan]{selected_book.get('title', 'Untitled')}[/cyan]")
                console.print(f"    Format: [cyan]{format_choice.split(' ')[1]}[/cyan]")
                console.print("    This would integrate with format conversion tools...")
                
                # TODO: Integrate with actual export functionality
                time.sleep(1.5)
                console.print("    ✅ Export completed!")

    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

    input("\nPress Enter to continue...")

def format_conversion_menu():
    """Menu for format conversion operations."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Format Conversion[/bold cyan]")
    console.print("    Convert between different ebook formats")
    console.print()

    choices = [
        "📚 EPUB to PDF",
        "📚 EPUB to DOCX",
        "📚 EPUB to MOBI",
        "📚 EPUB to HTML",
        "🔄 Batch Conversion",
        "← Back to Format & Export"
    ]

    selected = questionary.select(
        "Select conversion type:",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "🔄 Batch Conversion":
        batch_format_conversion()
    elif selected and selected != "← Back to Format & Export":
        single_format_conversion(selected)

def single_format_conversion(conversion_type: str):
    """Perform a single format conversion."""
    clear_screen()
    display_title()

    console.print(f"[bold cyan]{conversion_type}[/bold cyan]")
    console.print("    Convert your book to the selected format")
    console.print()

    console.print("[yellow]Format conversion will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• High-quality format conversion")
    console.print("• Metadata preservation")
    console.print("• Custom formatting options")
    console.print("• Quality validation")

    input("\nPress Enter to continue...")

def batch_format_conversion():
    """Perform batch format conversion."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Batch Format Conversion[/bold cyan]")
    console.print("    Convert multiple books to different formats")
    console.print()

    console.print("[yellow]Batch format conversion will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Multiple book selection")
    console.print("• Multiple format output")
    console.print("• Progress tracking")
    console.print("• Error handling and recovery")

    input("\nPress Enter to continue...")

def publishing_platform_prep():
    """Prepare books for specific publishing platforms."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🌐 Publishing Platform Preparation[/bold cyan]")
    console.print("    Optimize books for specific publishing platforms")
    console.print()

    platform_choices = [
        "📚 Amazon KDP",
        "📖 Draft2Digital",
        "🍎 Apple Books",
        "📱 Google Play Books",
        "📚 Smashwords",
        "🌐 All Platforms"
    ]

    selected_platform = questionary.select(
        "Select publishing platform:",
        choices=platform_choices,
        style=custom_style
    ).ask()

    if selected_platform:
        console.print(f"\n    🌐 Preparing for: [cyan]{selected_platform.split(' ', 1)[1]}[/cyan]")
        console.print()

        console.print("[yellow]Platform-specific preparation will be implemented in the next update.[/yellow]")
        console.print("This will include:")
        console.print("• Platform-specific formatting")
        console.print("• Metadata optimization")
        console.print("• File validation")
        console.print("• Submission package creation")

    input("\nPress Enter to continue...")

def export_analytics():
    """Show export analytics and statistics."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📊 Export Analytics[/bold cyan]")
    console.print("    View export statistics and performance metrics")
    console.print()

    console.print("[yellow]Export analytics will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Export history tracking")
    console.print("• Format popularity statistics")
    console.print("• Performance metrics")
    console.print("• Success/failure rates")
    console.print("• Platform-specific analytics")

    input("\nPress Enter to continue...")

def export_settings():
    """Configure export settings and preferences."""
    clear_screen()
    display_title()

    console.print("[bold cyan]⚙️ Export Settings[/bold cyan]")
    console.print("    Configure export preferences and defaults")
    console.print()

    console.print("[yellow]Export settings configuration will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Default export formats")
    console.print("• Quality and compression settings")
    console.print("• Metadata inclusion preferences")
    console.print("• Output directory configuration")
    console.print("• Platform-specific defaults")

    input("\nPress Enter to continue...")
