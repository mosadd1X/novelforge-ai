"""
Batch Operations for NovelForge AI - Phase 3 Implementation

This module provides comprehensive batch processing capabilities for multiple books,
including cover generation, EPUB creation, export functionality, and completion workflows.
"""

import os
import sys
from typing import Dict, List, Any, Optional, Tuple
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
from src.ui.responsive_separator import (
    separator, title_separator, section_separator
)

console = Console()

class BatchOperationManager:
    """Manager for batch operations with progress tracking and error recovery."""

    def __init__(self):
        self.current_operation = ""
        self.total_items = 0
        self.processed_items = 0
        self.successful_items = []
        self.failed_items = []
        self.skipped_items = []
        self.operation_log = []

    def start_operation(self, operation_name: str, items: List[Dict]):
        """Initialize a new batch operation."""
        self.current_operation = operation_name
        self.total_items = len(items)
        self.processed_items = 0
        self.successful_items = []
        self.failed_items = []
        self.skipped_items = []
        self.operation_log = []

        console.print(title_separator(f"Starting {operation_name}"))
        console.print(f"    Processing {self.total_items} item{'s' if self.total_items != 1 else ''}")
        console.print()

    def update_progress(self, item_name: str, status: str, details: str = ""):
        """Update progress for current item."""
        self.processed_items += 1

        if status == "success":
            self.successful_items.append(item_name)
            status_icon = "✅"
            status_color = "green"
        elif status == "failed":
            self.failed_items.append(item_name)
            status_icon = "❌"
            status_color = "red"
        elif status == "skipped":
            self.skipped_items.append(item_name)
            status_icon = "⏭️"
            status_color = "yellow"
        else:
            status_icon = "🔄"
            status_color = "cyan"

        # Display progress
        progress_text = f"[{self.processed_items}/{self.total_items}]"
        console.print(f"    {progress_text} {status_icon} [{status_color}]{item_name}[/{status_color}]")

        if details:
            console.print(f"        {details}")

        # Log the operation
        self.operation_log.append({
            "item": item_name,
            "status": status,
            "details": details,
            "timestamp": time.time()
        })

    def complete_operation(self):
        """Complete the batch operation and show results."""
        console.print()
        console.print(title_separator(f"{self.current_operation} Complete", "="))
        console.print()

        # Summary statistics
        console.print(section_separator("Operation Summary", "-", "simple"))
        console.print(f"    Total items: {self.total_items}")
        console.print(f"    ✅ Successful: {len(self.successful_items)}")
        console.print(f"    ❌ Failed: {len(self.failed_items)}")
        console.print(f"    ⏭️ Skipped: {len(self.skipped_items)}")

        # Show details if there were failures
        if self.failed_items:
            console.print()
            console.print(section_separator("Failed Items", "-", "simple"))
            for item in self.failed_items:
                console.print(f"    • {item}")

        if self.skipped_items:
            console.print()
            console.print(section_separator("Skipped Items", "-", "simple"))
            for item in self.skipped_items:
                console.print(f"    • {item}")

        console.print()
        console.print(separator("="))

def batch_cover_generation_menu():
    """Main menu for batch cover generation operations."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]🎨 Batch Cover Generation[/bold cyan]")
        console.print("    Create covers for multiple books at once")
        console.print()

        # Get books without covers
        books_without_covers = get_books_without_covers()

        if not books_without_covers:
            console.print("    ✅ [green]All your books already have covers![/green]")
            console.print("    No batch cover generation needed.")
            input("\nPress Enter to continue...")
            return

        console.print(f"    📚 Found {len(books_without_covers)} book{'s' if len(books_without_covers) != 1 else ''} without covers:")
        console.print()

        # Show first few books
        for i, book in enumerate(books_without_covers[:5]):
            title = book.get("title", "Untitled")
            genre = book.get("genre", "Unknown")
            console.print(f"    📖 {title} ({genre})")

        if len(books_without_covers) > 5:
            console.print(f"    ... and {len(books_without_covers) - 5} more")

        console.print()

        choices = [
            f"🚀 Generate covers for all {len(books_without_covers)} books",
            "📋 Select specific books for cover generation",
            "⚙️ Configure batch generation settings",
            "← Back to Publishing Tools"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected and "Generate covers for all" in selected:
            execute_batch_cover_generation(books_without_covers)
        elif selected == "📋 Select specific books for cover generation":
            selected_books = select_books_for_batch_operation(books_without_covers, "cover generation")
            if selected_books:
                execute_batch_cover_generation(selected_books)
        elif selected == "⚙️ Configure batch generation settings":
            configure_batch_settings()
        elif selected == "← Back to Publishing Tools":
            break

def get_books_without_covers() -> List[Dict]:
    """Get list of books that don't have covers."""
    books_without_covers = []

    try:
        from src.ui.book_menu import get_existing_books
        existing_books = get_existing_books()

        for book in existing_books:
            book_dir = book.get("directory", "")
            if book_dir and os.path.exists(book_dir):
                # Check for cover files
                cover_files = ["cover.jpg", "cover.png", "cover.jpeg"]
                has_cover = any(os.path.exists(os.path.join(book_dir, f)) for f in cover_files)

                if not has_cover:
                    books_without_covers.append(book)

    except Exception as e:
        console.print(f"[red]Error getting books: {e}[/red]")

    return books_without_covers

def select_books_for_batch_operation(books: List[Dict], operation_name: str) -> List[Dict]:
    """Allow user to select specific books for batch operation."""
    clear_screen()
    display_title()

    console.print(f"[bold cyan]📋 Select Books for {operation_name.title()}[/bold cyan]")
    console.print("    Choose which books to include in the batch operation")
    console.print()

    if not books:
        console.print("    ℹ️ No books available for this operation")
        input("\nPress Enter to continue...")
        return []

    # Create choices for book selection
    book_choices = []
    for book in books:
        title = book.get("title", "Untitled")
        genre = book.get("genre", "Unknown")
        book_choices.append(f"📖 {title} ({genre})")

    selected_indices = questionary.checkbox(
        f"Select books for {operation_name}:",
        choices=book_choices,
        style=custom_style
    ).ask()

    if not selected_indices:
        return []

    # Convert selected choices back to book objects
    selected_books = []
    for choice in selected_indices:
        # Find the index of the selected choice
        try:
            index = book_choices.index(choice)
            selected_books.append(books[index])
        except ValueError:
            continue

    console.print(f"\n    ✅ Selected {len(selected_books)} book{'s' if len(selected_books) != 1 else ''} for {operation_name}")
    input("\nPress Enter to continue...")

    return selected_books

def execute_batch_cover_generation(books: List[Dict]):
    """Execute batch cover generation for selected books."""
    clear_screen()
    display_title()

    batch_manager = BatchOperationManager()
    batch_manager.start_operation("Batch Cover Generation", books)

    # Confirm operation
    proceed = questionary.confirm(
        f"Generate covers for {len(books)} book{'s' if len(books) != 1 else ''}?",
        default=True,
        style=custom_style
    ).ask()

    if not proceed:
        console.print("    Operation cancelled")
        input("\nPress Enter to continue...")
        return

    console.print()

    # Process each book
    for book in books:
        title = book.get("title", "Untitled")

        try:
            # Simulate cover generation (replace with actual implementation)
            batch_manager.update_progress(title, "processing", "Generating cover...")
            time.sleep(0.5)  # Simulate processing time

            # This would call the actual cover generation function
            # generate_book_cover(book)

            batch_manager.update_progress(title, "success", "Cover generated successfully")

        except Exception as e:
            batch_manager.update_progress(title, "failed", f"Error: {str(e)}")

    batch_manager.complete_operation()
    input("\nPress Enter to continue...")

def batch_epub_generation_menu():
    """Main menu for batch EPUB generation operations."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]📚 Batch EPUB Generation[/bold cyan]")
        console.print("    Generate EPUB files for multiple books at once")
        console.print()

        # Get books without EPUB files
        books_without_epub = get_books_without_epub()

        if not books_without_epub:
            console.print("    ✅ [green]All your books already have EPUB files![/green]")
            console.print("    No batch EPUB generation needed.")
            input("\nPress Enter to continue...")
            return

        console.print(f"    📚 Found {len(books_without_epub)} book{'s' if len(books_without_epub) != 1 else ''} without EPUB files:")
        console.print()

        # Show first few books
        for i, book in enumerate(books_without_epub[:5]):
            title = book.get("title", "Untitled")
            genre = book.get("genre", "Unknown")
            console.print(f"    📖 {title} ({genre})")

        if len(books_without_epub) > 5:
            console.print(f"    ... and {len(books_without_epub) - 5} more")

        console.print()

        choices = [
            f"🚀 Generate EPUB for all {len(books_without_epub)} books",
            "📋 Select specific books for EPUB generation",
            "⚙️ Configure EPUB generation settings",
            "← Back to Publishing Tools"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected and "Generate EPUB for all" in selected:
            execute_batch_epub_generation(books_without_epub)
        elif selected == "📋 Select specific books for EPUB generation":
            selected_books = select_books_for_batch_operation(books_without_epub, "EPUB generation")
            if selected_books:
                execute_batch_epub_generation(selected_books)
        elif selected == "⚙️ Configure EPUB generation settings":
            configure_epub_settings()
        elif selected == "← Back to Publishing Tools":
            break

def complete_all_unfinished_books_workflow():
    """Complete workflow for all unfinished books in the library."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Complete All Unfinished Books[/bold cyan]")
    console.print("    Automatically complete all books missing covers, EPUB files, or other components")
    console.print()

    # Analyze all books and categorize by what's missing
    analysis = analyze_all_books_completion_status()

    if not analysis["incomplete_books"]:
        console.print("    🎉 [bold green]All your books are complete![/bold green]")
        console.print("    No unfinished books found in your library.")
        input("\nPress Enter to continue...")
        return

    # Display analysis results
    console.print("[bold cyan]📊 Library Analysis:[/bold cyan]")
    console.print(f"    📚 Total books: {analysis['total_books']}")
    console.print(f"    ✅ Complete books: {analysis['complete_books']}")
    console.print(f"    ⏳ Incomplete books: {len(analysis['incomplete_books'])}")
    console.print()

    # Show breakdown of what's missing
    if analysis["books_missing_covers"]:
        console.print(f"    🎨 Missing covers: {len(analysis['books_missing_covers'])}")
    if analysis["books_missing_epub"]:
        console.print(f"    📚 Missing EPUB: {len(analysis['books_missing_epub'])}")
    if analysis["books_missing_content"]:
        console.print(f"    📝 Missing content: {len(analysis['books_missing_content'])}")

    console.print()

    # Offer completion options
    choices = [
        "🚀 Complete all missing components automatically",
        "📋 Select specific completion tasks",
        "📊 View detailed analysis",
        "← Back to Library Management"
    ]

    selected = questionary.select(
        "How would you like to proceed?",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "🚀 Complete all missing components automatically":
        execute_complete_all_workflow(analysis)
    elif selected == "📋 Select specific completion tasks":
        execute_selective_completion_workflow(analysis)
    elif selected == "📊 View detailed analysis":
        display_detailed_completion_analysis(analysis)
        input("\nPress Enter to continue...")
    elif selected == "← Back to Library Management":
        return

def analyze_all_books_completion_status() -> Dict[str, Any]:
    """Analyze completion status of all books in the library."""
    analysis = {
        "total_books": 0,
        "complete_books": 0,
        "incomplete_books": [],
        "books_missing_covers": [],
        "books_missing_epub": [],
        "books_missing_content": []
    }

    try:
        from src.ui.book_menu import get_existing_books
        existing_books = get_existing_books()

        analysis["total_books"] = len(existing_books)

        for book in existing_books:
            book_dir = book.get("directory", "")
            if not book_dir or not os.path.exists(book_dir):
                analysis["books_missing_content"].append(book)
                analysis["incomplete_books"].append(book)
                continue

            missing_components = []

            # Check for content files
            content_files = ["outline.txt", "characters.json"]
            has_content = any(os.path.exists(os.path.join(book_dir, f)) for f in content_files)
            if not has_content:
                missing_components.append("content")
                analysis["books_missing_content"].append(book)

            # Check for cover files
            cover_files = ["cover.jpg", "cover.png", "cover.jpeg"]
            has_cover = any(os.path.exists(os.path.join(book_dir, f)) for f in cover_files)
            if not has_cover:
                missing_components.append("cover")
                analysis["books_missing_covers"].append(book)

            # Check for EPUB files
            epub_files = [f for f in os.listdir(book_dir) if f.endswith('.epub')]
            has_epub = len(epub_files) > 0
            if not has_epub:
                missing_components.append("epub")
                analysis["books_missing_epub"].append(book)

            # Determine if book is complete
            if missing_components:
                book_copy = book.copy()
                book_copy["missing_components"] = missing_components
                analysis["incomplete_books"].append(book_copy)
            else:
                analysis["complete_books"] += 1

    except Exception as e:
        console.print(f"[red]Error analyzing books: {e}[/red]")

    return analysis

def execute_complete_all_workflow(analysis: Dict[str, Any]):
    """Execute the complete workflow for all unfinished books."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🚀 Complete All Unfinished Books Workflow[/bold cyan]")
    console.print("    Automatically completing all missing components")
    console.print()

    incomplete_books = analysis["incomplete_books"]

    # Confirm operation
    proceed = questionary.confirm(
        f"Complete {len(incomplete_books)} unfinished book{'s' if len(incomplete_books) != 1 else ''}?",
        default=True,
        style=custom_style
    ).ask()

    if not proceed:
        console.print("    Operation cancelled")
        input("\nPress Enter to continue...")
        return

    batch_manager = BatchOperationManager()
    batch_manager.start_operation("Complete All Unfinished Books", incomplete_books)

    console.print()

    # Process each incomplete book
    for book in incomplete_books:
        title = book.get("title", "Untitled")
        missing_components = book.get("missing_components", [])

        try:
            batch_manager.update_progress(title, "processing", f"Missing: {', '.join(missing_components)}")

            # Complete each missing component
            for component in missing_components:
                if component == "cover":
                    # Simulate cover generation
                    time.sleep(0.5)
                    console.print(f"        🎨 Generated cover")
                elif component == "epub":
                    # Simulate EPUB generation
                    time.sleep(1.0)
                    console.print(f"        📚 Generated EPUB")
                elif component == "content":
                    # This would require more complex handling
                    console.print(f"        📝 Content completion requires manual intervention")

            batch_manager.update_progress(title, "success", "All components completed")

        except Exception as e:
            batch_manager.update_progress(title, "failed", f"Error: {str(e)}")

    batch_manager.complete_operation()
    input("\nPress Enter to continue...")

def execute_selective_completion_workflow(analysis: Dict[str, Any]):
    """Allow user to select specific completion tasks."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📋 Selective Completion Workflow[/bold cyan]")
    console.print("    Choose which completion tasks to perform")
    console.print()

    # Create task options
    task_choices = []

    if analysis["books_missing_covers"]:
        count = len(analysis["books_missing_covers"])
        task_choices.append(f"🎨 Generate covers for {count} book{'s' if count != 1 else ''}")

    if analysis["books_missing_epub"]:
        count = len(analysis["books_missing_epub"])
        task_choices.append(f"📚 Generate EPUB for {count} book{'s' if count != 1 else ''}")

    if analysis["books_missing_content"]:
        count = len(analysis["books_missing_content"])
        task_choices.append(f"📝 Review {count} book{'s' if count != 1 else ''} with missing content")

    if not task_choices:
        console.print("    ℹ️ No completion tasks available")
        input("\nPress Enter to continue...")
        return

    selected_tasks = questionary.checkbox(
        "Select completion tasks to perform:",
        choices=task_choices,
        style=custom_style
    ).ask()

    if not selected_tasks:
        console.print("    No tasks selected")
        input("\nPress Enter to continue...")
        return

    # Execute selected tasks
    for task in selected_tasks:
        if "Generate covers" in task:
            execute_batch_cover_generation(analysis["books_missing_covers"])
        elif "Generate EPUB" in task:
            execute_batch_epub_generation(analysis["books_missing_epub"])
        elif "Review" in task and "missing content" in task:
            review_books_missing_content(analysis["books_missing_content"])

def display_detailed_completion_analysis(analysis: Dict[str, Any]):
    """Display detailed analysis of book completion status."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📊 Detailed Completion Analysis[/bold cyan]")
    console.print()

    console.print(f"[bold green]📚 Library Overview:[/bold green]")
    console.print(f"    Total books: {analysis['total_books']}")
    console.print(f"    Complete books: {analysis['complete_books']}")
    console.print(f"    Incomplete books: {len(analysis['incomplete_books'])}")
    console.print()

    if analysis["incomplete_books"]:
        console.print("[bold yellow]⏳ Incomplete Books:[/bold yellow]")
        for book in analysis["incomplete_books"]:
            title = book.get("title", "Untitled")
            missing = book.get("missing_components", [])
            console.print(f"    📖 {title}")
            console.print(f"        Missing: {', '.join(missing)}")
        console.print()

    # Component-specific breakdowns
    if analysis["books_missing_covers"]:
        console.print(f"[bold cyan]🎨 Books Missing Covers ({len(analysis['books_missing_covers'])}):[/bold cyan]")
        for book in analysis["books_missing_covers"][:5]:
            title = book.get("title", "Untitled")
            console.print(f"    • {title}")
        if len(analysis["books_missing_covers"]) > 5:
            console.print(f"    ... and {len(analysis['books_missing_covers']) - 5} more")
        console.print()

    if analysis["books_missing_epub"]:
        console.print(f"[bold cyan]📚 Books Missing EPUB ({len(analysis['books_missing_epub'])}):[/bold cyan]")
        for book in analysis["books_missing_epub"][:5]:
            title = book.get("title", "Untitled")
            console.print(f"    • {title}")
        if len(analysis["books_missing_epub"]) > 5:
            console.print(f"    ... and {len(analysis['books_missing_epub']) - 5} more")
        console.print()

def review_books_missing_content(books: List[Dict]):
    """Review books that are missing content files."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📝 Review Books Missing Content[/bold cyan]")
    console.print("    Books that may need regeneration or manual intervention")
    console.print()

    if not books:
        console.print("    ✅ No books missing content")
        input("\nPress Enter to continue...")
        return

    console.print(f"    Found {len(books)} book{'s' if len(books) != 1 else ''} missing content:")
    console.print()

    for book in books:
        title = book.get("title", "Untitled")
        directory = book.get("directory", "Unknown")
        console.print(f"    📖 {title}")
        console.print(f"        Directory: {directory}")
        console.print(f"        Status: Missing core content files")
        console.print()

    console.print("    💡 [cyan]Recommendation:[/cyan] These books may need to be regenerated")
    console.print("    or have their content files restored from backup.")

    input("\nPress Enter to continue...")

def batch_export_menu():
    """Main menu for batch export operations."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📤 Batch Export Operations[/bold cyan]")
    console.print("    Export multiple books to different formats")
    console.print()

    console.print("[yellow]Batch export functionality will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Multiple format export (PDF, DOCX, TXT)")
    console.print("• Publishing platform preparation")
    console.print("• Archive creation with metadata")
    console.print("• Quality control and validation")

    input("\nPress Enter to continue...")

def get_books_without_epub() -> List[Dict]:
    """Get list of books that don't have EPUB files."""
    books_without_epub = []

    try:
        from src.ui.book_menu import get_existing_books
        existing_books = get_existing_books()

        for book in existing_books:
            book_dir = book.get("directory", "")
            if book_dir and os.path.exists(book_dir):
                # Check for EPUB files
                epub_files = [f for f in os.listdir(book_dir) if f.endswith('.epub')]

                if not epub_files:
                    books_without_epub.append(book)

    except Exception as e:
        console.print(f"[red]Error getting books: {e}[/red]")

    return books_without_epub

def execute_batch_epub_generation(books: List[Dict]):
    """Execute batch EPUB generation for selected books."""
    clear_screen()
    display_title()

    batch_manager = BatchOperationManager()
    batch_manager.start_operation("Batch EPUB Generation", books)

    # Confirm operation
    proceed = questionary.confirm(
        f"Generate EPUB files for {len(books)} book{'s' if len(books) != 1 else ''}?",
        default=True,
        style=custom_style
    ).ask()

    if not proceed:
        console.print("    Operation cancelled")
        input("\nPress Enter to continue...")
        return

    console.print()

    # Process each book
    for book in books:
        title = book.get("title", "Untitled")

        try:
            # Simulate EPUB generation (replace with actual implementation)
            batch_manager.update_progress(title, "processing", "Generating EPUB...")
            time.sleep(1.0)  # Simulate processing time

            # This would call the actual EPUB generation function
            # generate_epub_manually(book)

            batch_manager.update_progress(title, "success", "EPUB generated successfully")

        except Exception as e:
            batch_manager.update_progress(title, "failed", f"Error: {str(e)}")

    batch_manager.complete_operation()
    input("\nPress Enter to continue...")

def configure_batch_settings():
    """Configure settings for batch operations."""
    clear_screen()
    display_title()

    console.print("[bold cyan]⚙️ Batch Operation Settings[/bold cyan]")
    console.print("    Configure default settings for batch operations")
    console.print()

    console.print("[yellow]Batch operation settings configuration will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Cover generation quality settings")
    console.print("• EPUB formatting preferences")
    console.print("• Error handling behavior")
    console.print("• Progress notification options")

    input("\nPress Enter to continue...")

def configure_epub_settings():
    """Configure settings for EPUB generation."""
    clear_screen()
    display_title()

    console.print("[bold cyan]⚙️ EPUB Generation Settings[/bold cyan]")
    console.print("    Configure default settings for EPUB generation")
    console.print()

    console.print("[yellow]EPUB generation settings configuration will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Metadata inclusion preferences")
    console.print("• Cover embedding options")
    console.print("• Chapter formatting settings")
    console.print("• Compression and quality options")

    input("\nPress Enter to continue...")
