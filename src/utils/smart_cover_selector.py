"""
Smart cover selection utility for EPUB generation.
Checks for existing covers first, falls back to programmatic generation.
"""

import os
from typing import Optional, Dict, Any
from rich.console import Console

from src.utils.cover_folder_manager import CoverFolderManager
from src.database.cover_database_manager import get_cover_database_manager
from src.database.database_manager import get_database_manager
from src.ui.terminal_ui import generate_cover

console = Console()


class SmartCoverSelector:
    """
    Handles intelligent cover selection for EPUB generation.
    Prioritizes existing covers over programmatic generation.
    """

    def __init__(self):
        """Initialize the smart cover selector."""
        self.folder_manager = CoverFolderManager()
        self.cover_db_manager = get_cover_database_manager()
        self.db_manager = get_database_manager()

    def get_cover_for_epub(self, novel_data: Dict[str, Any], output_dir: str,
                          auto_mode: bool = True) -> Optional[str]:
        """
        Get the best available cover for EPUB generation.

        Args:
            novel_data: Novel data containing metadata
            output_dir: Output directory for the book
            auto_mode: Whether to run in automatic mode

        Returns:
            Path to cover image or None if no cover available
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")

        # Check if this is part of a series
        series_info = None
        if "series" in metadata and metadata["series"].get("is_part_of_series"):
            series_info = metadata["series"]

        # Step 1: Check for covers in database first
        database_cover = self._find_database_cover(title, series_info, output_dir)
        if database_cover:
            console.print(f"[bold green]✓[/bold green] Using database cover: [bold cyan]{os.path.basename(database_cover)}[/bold cyan]")
            return database_cover

        # Step 2: Check for existing covers in covers/ folder
        existing_cover = self._find_existing_cover(title, series_info)
        if existing_cover:
            console.print(f"[bold green]✓[/bold green] Using existing cover: [bold cyan]{os.path.basename(existing_cover)}[/bold cyan]")
            return existing_cover

        # Step 3: Fall back to programmatic cover generation
        console.print("[dim]No existing cover found, generating programmatic cover...[/dim]")
        return self._generate_programmatic_cover(novel_data, output_dir, auto_mode)

    def _find_database_cover(self, title: str, series_info: Optional[Dict[str, Any]] = None, output_dir: str = "temp") -> Optional[str]:
        """
        Find cover images stored in the database.

        Args:
            title: Book or series title
            series_info: Optional series information

        Returns:
            Path to extracted cover file or None if not found
        """
        try:
            # Try to find a book in the database that matches this title/series
            if series_info and series_info.get("is_part_of_series"):
                # For series books, look for books with matching series info
                all_books = self.db_manager.get_books(status="completed")
                for book in all_books:
                    book_series = book.get("series_info", {})
                    if (book_series.get("series_title") == series_info.get("series_title") and
                        book_series.get("book_number") == series_info.get("book_number")):

                        if self.cover_db_manager.has_cover(book["book_id"]):
                            # Extract cover to temporary file
                            temp_cover_path = os.path.join(output_dir, f"temp_cover_{book['book_id']}.jpg")
                            if self.cover_db_manager.get_cover_as_file(book["book_id"], temp_cover_path):
                                return temp_cover_path
            else:
                # For standalone books, look for exact title match
                all_books = self.db_manager.get_books(status="completed")
                for book in all_books:
                    if book.get("title") == title:
                        if self.cover_db_manager.has_cover(book["book_id"]):
                            # Extract cover to temporary file
                            temp_cover_path = os.path.join(output_dir, f"temp_cover_{book['book_id']}.jpg")
                            if self.cover_db_manager.get_cover_as_file(book["book_id"], temp_cover_path):
                                return temp_cover_path

            return None

        except Exception as e:
            console.print(f"[yellow]Warning: Error checking database covers: {str(e)}[/yellow]")
            return None

    def _find_existing_cover(self, title: str, series_info: Optional[Dict[str, Any]] = None) -> Optional[str]:
        """
        Find existing cover images in the covers/ folder.

        Args:
            title: Book or series title
            series_info: Optional series information

        Returns:
            Path to existing cover or None if not found
        """
        try:
            # Use the folder manager to scan for covers
            found_images = self.folder_manager.scan_for_cover_images(title, series_info)

            if found_images:
                # Validate the first found image
                for image_path in found_images:
                    is_valid, message = self.folder_manager.validate_cover_image(image_path)
                    if is_valid:
                        return image_path
                    else:
                        console.print(f"[yellow]Warning: Invalid cover found - {message}[/yellow]")

            return None

        except Exception as e:
            console.print(f"[yellow]Warning: Error checking for existing covers: {str(e)}[/yellow]")
            return None

    def _generate_programmatic_cover(self, novel_data: Dict[str, Any], output_dir: str,
                                   auto_mode: bool) -> Optional[str]:
        """
        Generate a programmatic cover as fallback.

        Args:
            novel_data: Novel data containing metadata
            output_dir: Output directory for the book
            auto_mode: Whether to run in automatic mode

        Returns:
            Path to generated cover or None if generation failed
        """
        try:
            # Use the existing cover generation function
            return generate_cover(novel_data, output_dir, auto_mode=auto_mode)

        except Exception as e:
            console.print(f"[bold red]Error generating programmatic cover: {str(e)}[/bold red]")
            return None

    def show_cover_status(self, title: str, series_info: Optional[Dict[str, Any]] = None) -> None:
        """
        Display the current cover status for a book.

        Args:
            title: Book or series title
            series_info: Optional series information
        """
        existing_cover = self._find_existing_cover(title, series_info)

        if existing_cover:
            console.print(f"[bold green]✓[/bold green] Existing cover found: [bold cyan]{existing_cover}[/bold cyan]")

            # Show cover details
            is_valid, message = self.folder_manager.validate_cover_image(existing_cover)
            if is_valid:
                console.print(f"[bold green]✓[/bold green] Cover is valid and ready to use")
            else:
                console.print(f"[bold red]✗[/bold red] Cover validation failed: {message}")
        else:
            console.print("[yellow]No existing cover found[/yellow]")
            console.print("[dim]Will generate programmatic cover during EPUB creation[/dim]")

            # Show expected cover location
            expected_path = self.folder_manager.get_expected_cover_path(title, series_info)
            console.print(f"[dim]Expected cover location: {expected_path}[/dim]")


def get_smart_cover_for_epub(novel_data: Dict[str, Any], output_dir: str,
                           auto_mode: bool = True) -> Optional[str]:
    """
    Convenience function to get a smart cover for EPUB generation.

    Args:
        novel_data: Novel data containing metadata
        output_dir: Output directory for the book
        auto_mode: Whether to run in automatic mode

    Returns:
        Path to cover image or None if no cover available
    """
    selector = SmartCoverSelector()
    return selector.get_cover_for_epub(novel_data, output_dir, auto_mode)
