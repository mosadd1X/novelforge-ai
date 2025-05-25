"""
Migration manager for converting existing file-based data to database storage.
"""

import os
import json
import glob
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
from rich.console import Console
from rich.progress import Progress, TaskID
from rich.table import Table

from src.database.database_manager import get_database_manager
from src.database.cover_database_manager import get_cover_database_manager
from src.database.epub_database_manager import get_epub_database_manager
from src.utils.file_handler import load_novel_json

console = Console()


class MigrationManager:
    """
    Manages migration of existing books and covers to the database system.
    """

    def __init__(self):
        """Initialize the migration manager."""
        self.db_manager = get_database_manager()
        self.cover_db_manager = get_cover_database_manager()
        self.epub_db_manager = get_epub_database_manager()
        self.output_dir = "output"
        self.covers_dir = "covers"

    def migrate_all_data(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Migrate all existing books and covers to the database.

        Args:
            dry_run: If True, only analyze what would be migrated without making changes

        Returns:
            Dictionary containing migration results
        """
        console.print(f"[bold cyan]{'Analyzing' if dry_run else 'Starting'} Data Migration to Database[/bold cyan]\n")

        results = {
            "books_found": 0,
            "books_migrated": 0,
            "covers_found": 0,
            "covers_migrated": 0,
            "epubs_found": 0,
            "epubs_migrated": 0,
            "novel_data_migrated": 0,
            "series_found": 0,
            "series_migrated": 0,
            "total_storage_saved_mb": 0.0,
            "errors": []
        }

        # Migrate individual books
        book_results = self.migrate_individual_books(dry_run)
        results.update(book_results)

        # Migrate series books
        series_results = self.migrate_series_books(dry_run)
        results["series_found"] = series_results["series_found"]
        results["series_migrated"] = series_results["series_migrated"]
        results["books_found"] += series_results["books_found"]
        results["books_migrated"] += series_results["books_migrated"]
        results["covers_found"] += series_results["covers_found"]
        results["covers_migrated"] += series_results["covers_migrated"]
        results["errors"].extend(series_results["errors"])

        # Migrate standalone covers
        cover_results = self.migrate_standalone_covers(dry_run)
        results["covers_found"] += cover_results["covers_found"]
        results["covers_migrated"] += cover_results["covers_migrated"]
        results["errors"].extend(cover_results["errors"])

        # Display results
        self._display_migration_results(results, dry_run)

        return results

    def migrate_individual_books(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Migrate individual (non-series) books to the database.

        Args:
            dry_run: If True, only analyze without making changes

        Returns:
            Dictionary containing migration results
        """
        results = {
            "books_found": 0,
            "books_migrated": 0,
            "covers_found": 0,
            "covers_migrated": 0,
            "epubs_found": 0,
            "epubs_migrated": 0,
            "novel_data_migrated": 0,
            "total_storage_saved_mb": 0.0,
            "errors": []
        }

        if not os.path.exists(self.output_dir):
            return results

        # Find individual book directories (not in series folder)
        book_dirs = []
        for item in os.listdir(self.output_dir):
            item_path = os.path.join(self.output_dir, item)
            if os.path.isdir(item_path) and item != "series":
                # Check if it contains a novel_data.json file
                json_path = os.path.join(item_path, "novel_data.json")
                if os.path.exists(json_path):
                    book_dirs.append(item_path)

        results["books_found"] = len(book_dirs)

        if not book_dirs:
            return results

        console.print(f"[bold green]Found {len(book_dirs)} individual books[/bold green]")

        with Progress() as progress:
            task = progress.add_task("Migrating individual books...", total=len(book_dirs))

            for book_dir in book_dirs:
                try:
                    book_result = self._migrate_single_book(book_dir, dry_run)
                    if book_result["migrated"]:
                        results["books_migrated"] += 1
                    if book_result["cover_migrated"]:
                        results["covers_migrated"] += 1
                    if book_result["cover_found"]:
                        results["covers_found"] += 1
                    if book_result["epub_migrated"]:
                        results["epubs_migrated"] += 1
                    if book_result["epub_found"]:
                        results["epubs_found"] += 1
                    if book_result["novel_data_migrated"]:
                        results["novel_data_migrated"] += 1
                    results["total_storage_saved_mb"] += book_result.get("storage_saved_mb", 0.0)

                except Exception as e:
                    error_msg = f"Error migrating book in {book_dir}: {str(e)}"
                    results["errors"].append(error_msg)
                    console.print(f"[bold red]✗[/bold red] {error_msg}")

                progress.update(task, advance=1)

        return results

    def migrate_series_books(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Migrate series books to the database.

        Args:
            dry_run: If True, only analyze without making changes

        Returns:
            Dictionary containing migration results
        """
        results = {
            "series_found": 0,
            "series_migrated": 0,
            "books_found": 0,
            "books_migrated": 0,
            "covers_found": 0,
            "covers_migrated": 0,
            "errors": []
        }

        series_dir = os.path.join(self.output_dir, "series")
        if not os.path.exists(series_dir):
            return results

        # Find series directories
        series_dirs = []
        for item in os.listdir(series_dir):
            item_path = os.path.join(series_dir, item)
            if os.path.isdir(item_path):
                series_dirs.append(item_path)

        results["series_found"] = len(series_dirs)

        if not series_dirs:
            return results

        console.print(f"[bold green]Found {len(series_dirs)} series[/bold green]")

        with Progress() as progress:
            task = progress.add_task("Migrating series...", total=len(series_dirs))

            for series_path in series_dirs:
                try:
                    series_result = self._migrate_single_series(series_path, dry_run)
                    if series_result["migrated"]:
                        results["series_migrated"] += 1
                    results["books_found"] += series_result["books_found"]
                    results["books_migrated"] += series_result["books_migrated"]
                    results["covers_found"] += series_result["covers_found"]
                    results["covers_migrated"] += series_result["covers_migrated"]
                    results["errors"].extend(series_result["errors"])

                except Exception as e:
                    error_msg = f"Error migrating series in {series_path}: {str(e)}"
                    results["errors"].append(error_msg)
                    console.print(f"[bold red]✗[/bold red] {error_msg}")

                progress.update(task, advance=1)

        return results

    def migrate_standalone_covers(self, dry_run: bool = False) -> Dict[str, Any]:
        """
        Migrate covers from the covers/ folder that don't have associated books yet.

        Args:
            dry_run: If True, only analyze without making changes

        Returns:
            Dictionary containing migration results
        """
        results = {
            "covers_found": 0,
            "covers_migrated": 0,
            "errors": []
        }

        if not os.path.exists(self.covers_dir):
            return results

        # Find cover directories
        cover_dirs = []
        for item in os.listdir(self.covers_dir):
            item_path = os.path.join(self.covers_dir, item)
            if os.path.isdir(item_path):
                cover_dirs.append(item_path)

        if not cover_dirs:
            return results

        console.print(f"[bold green]Found {len(cover_dirs)} cover directories[/bold green]")

        # This would be implemented to handle orphaned covers
        # For now, we'll focus on covers associated with books

        return results

    def _migrate_single_book(self, book_dir: str, dry_run: bool = False) -> Dict[str, Any]:
        """
        Migrate a single book to the database.

        Args:
            book_dir: Path to the book directory
            dry_run: If True, only analyze without making changes

        Returns:
            Dictionary containing migration results for this book
        """
        result = {
            "migrated": False,
            "cover_found": False,
            "cover_migrated": False,
            "epub_found": False,
            "epub_migrated": False,
            "novel_data_migrated": False,
            "storage_saved_mb": 0.0,
            "errors": []
        }

        try:
            # Load novel data
            json_path = os.path.join(book_dir, "novel_data.json")
            novel_data = load_novel_json(json_path)

            # Extract book information
            metadata = novel_data.get("metadata", {})

            # Generate book ID
            book_id = self.db_manager.generate_book_id(metadata.get("title", "Untitled"))

            # Prepare book data for database
            book_data = {
                "book_id": book_id,
                "title": metadata.get("title", "Untitled"),
                "author": metadata.get("author", ""),
                "genre": metadata.get("genre", ""),
                "target_audience": metadata.get("target_audience", ""),
                "description": metadata.get("description", ""),
                "series_info": metadata.get("series", {}),
                "generation_status": "completed",  # Existing books are completed
                "word_count": metadata.get("word_count", 0),
                "chapter_count": len(novel_data.get("chapters", [])),
                "file_path": book_dir,
                "json_path": json_path,
                "epub_path": self._find_epub_file(book_dir),
                "created_date": metadata.get("created_at", ""),
                "metadata": novel_data
            }

            if not dry_run:
                # Add book to database
                self.db_manager.add_book(book_data)
                result["migrated"] = True
                result["novel_data_migrated"] = True

            # Look for EPUB files
            epub_path = self._find_epub_file(book_dir)
            if epub_path:
                result["epub_found"] = True
                if not dry_run:
                    # Store EPUB and novel data in database
                    if self.epub_db_manager.store_epub_from_file(book_id, epub_path, novel_data):
                        result["epub_migrated"] = True

                        # Calculate storage savings
                        original_size = os.path.getsize(epub_path)
                        book_record = self.db_manager.get_book(book_id)
                        if book_record:
                            compressed_size = book_record.get("epub_compressed_size", original_size)
                            storage_saved = original_size - compressed_size
                            result["storage_saved_mb"] = storage_saved / (1024 * 1024)

            # Look for cover images
            cover_path = self._find_cover_image(book_dir)
            if cover_path:
                result["cover_found"] = True
                if not dry_run:
                    # Store cover in database
                    if self.cover_db_manager.store_cover_from_file(book_id, cover_path):
                        result["cover_migrated"] = True

        except Exception as e:
            result["errors"].append(str(e))

        return result

    def _migrate_single_series(self, series_path: str, dry_run: bool = False) -> Dict[str, Any]:
        """
        Migrate a single series to the database.

        Args:
            series_path: Path to the series directory
            dry_run: If True, only analyze without making changes

        Returns:
            Dictionary containing migration results for this series
        """
        result = {
            "migrated": False,
            "books_found": 0,
            "books_migrated": 0,
            "covers_found": 0,
            "covers_migrated": 0,
            "errors": []
        }

        try:
            # Find book directories in the series
            book_dirs = []
            for item in os.listdir(series_path):
                item_path = os.path.join(series_path, item)
                if os.path.isdir(item_path) and item.startswith("book_"):
                    json_path = os.path.join(item_path, "novel_data.json")
                    if os.path.exists(json_path):
                        book_dirs.append(item_path)

            result["books_found"] = len(book_dirs)

            # Migrate each book in the series
            for book_dir in book_dirs:
                book_result = self._migrate_single_book(book_dir, dry_run)
                if book_result["migrated"]:
                    result["books_migrated"] += 1
                if book_result["cover_found"]:
                    result["covers_found"] += 1
                if book_result["cover_migrated"]:
                    result["covers_migrated"] += 1
                result["errors"].extend(book_result["errors"])

            if result["books_migrated"] > 0 or dry_run:
                result["migrated"] = True

        except Exception as e:
            result["errors"].append(str(e))

        return result

    def _find_epub_file(self, book_dir: str) -> str:
        """Find the EPUB file in a book directory."""
        epub_files = glob.glob(os.path.join(book_dir, "*.epub"))
        return epub_files[0] if epub_files else ""

    def _find_cover_image(self, book_dir: str) -> Optional[str]:
        """Find a cover image in a book directory."""
        image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.bmp']

        for ext in image_extensions:
            images = glob.glob(os.path.join(book_dir, ext))
            if images:
                return images[0]

        return None

    def _display_migration_results(self, results: Dict[str, Any], dry_run: bool) -> None:
        """Display migration results in a formatted table."""
        table = Table(title=f"Migration {'Analysis' if dry_run else 'Results'}")
        table.add_column("Category", style="cyan")
        table.add_column("Found", style="green")
        table.add_column("Migrated", style="blue")
        table.add_column("Status", style="yellow")

        # Books
        book_status = "✓ Ready" if dry_run else ("✓ Complete" if results["books_migrated"] == results["books_found"] else "⚠ Partial")
        table.add_row("Books", str(results["books_found"]), str(results["books_migrated"]), book_status)

        # Covers
        cover_status = "✓ Ready" if dry_run else ("✓ Complete" if results["covers_migrated"] == results["covers_found"] else "⚠ Partial")
        table.add_row("Covers", str(results["covers_found"]), str(results["covers_migrated"]), cover_status)

        # EPUBs
        epub_status = "✓ Ready" if dry_run else ("✓ Complete" if results["epubs_migrated"] == results["epubs_found"] else "⚠ Partial")
        table.add_row("EPUBs", str(results["epubs_found"]), str(results["epubs_migrated"]), epub_status)

        # Novel Data
        novel_data_status = "✓ Ready" if dry_run else ("✓ Complete" if results["novel_data_migrated"] > 0 else "⚠ None")
        table.add_row("Novel Data", str(results["novel_data_migrated"]), str(results["novel_data_migrated"]), novel_data_status)

        # Series
        series_status = "✓ Ready" if dry_run else ("✓ Complete" if results["series_migrated"] == results["series_found"] else "⚠ Partial")
        table.add_row("Series", str(results["series_found"]), str(results["series_migrated"]), series_status)

        console.print(table)

        # Display storage savings if any
        if results.get("total_storage_saved_mb", 0) > 0:
            console.print(f"\n[bold green]Storage Savings:[/bold green] [cyan]{results['total_storage_saved_mb']:.1f} MB[/cyan] saved through compression")

        # Display errors if any
        if results["errors"]:
            console.print(f"\n[bold red]Errors encountered ({len(results['errors'])}):[/bold red]")
            for error in results["errors"][:5]:  # Show first 5 errors
                console.print(f"  • {error}")
            if len(results["errors"]) > 5:
                console.print(f"  ... and {len(results['errors']) - 5} more errors")


# Global migration manager instance
_migration_manager = None

def get_migration_manager() -> MigrationManager:
    """Get the global migration manager instance."""
    global _migration_manager
    if _migration_manager is None:
        _migration_manager = MigrationManager()
    return _migration_manager
