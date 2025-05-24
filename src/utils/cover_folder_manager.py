"""
Cover folder manager for organizing cover assets and managing folder structure.
"""
import os
import shutil
from typing import Dict, Any, List, Optional, Tuple
from rich.console import Console

from src.utils.file_handler import sanitize_filename

console = Console(markup=True)


class CoverFolderManager:
    """
    Manages folder structure and organization for cover assets.
    """

    def __init__(self):
        """Initialize the cover folder manager."""
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.webp']
        self.cover_folder_name = "covers"

    def create_cover_folder(self, title: str,
                          series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Create a cover folder for a book or series in the root covers directory.

        Args:
            title: Book or series title
            series_info: Optional series information

        Returns:
            Path to the created cover folder
        """
        if series_info:
            # For series, create folder in root covers directory
            series_title = series_info.get('series_title', title)
            folder_name = sanitize_filename(series_title)

            # Use root covers directory structure: covers/Series Name/
            cover_folder = os.path.join(self.cover_folder_name, folder_name)
        else:
            # For single books, create folder in root covers directory
            folder_name = sanitize_filename(title)

            # Use root covers directory structure: covers/Book Name/
            cover_folder = os.path.join(self.cover_folder_name, folder_name)

        # Create the directory
        os.makedirs(cover_folder, exist_ok=True)

        console.print(f"[bold green]✓[/bold green] Cover folder created: [bold cyan]{cover_folder}[/bold cyan]")

        return cover_folder

    def get_expected_cover_path(self, title: str,
                              series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Get the expected path for a cover image in the root covers directory.

        Args:
            title: Book or series title
            series_info: Optional series information

        Returns:
            Expected path for the cover image
        """
        cover_folder = self.create_cover_folder(title, series_info)

        if series_info:
            # For series: Book1.jpg, Book2.jpg, etc.
            book_number = series_info.get('book_number', 1)
            filename = f"Book{book_number}.jpg"
        else:
            # For single books: Cover.jpg
            filename = "Cover.jpg"

        return os.path.join(cover_folder, filename)

    def scan_for_cover_images(self, title: str,
                            series_info: Optional[Dict[str, Any]] = None) -> List[str]:
        """
        Scan for existing cover images in the root covers directory.

        Args:
            title: Book or series title
            series_info: Optional series information

        Returns:
            List of found cover image paths
        """
        found_images = []

        # Check the cover folder
        cover_folder = self.create_cover_folder(title, series_info)

        if os.path.exists(cover_folder):
            for file in os.listdir(cover_folder):
                file_path = os.path.join(cover_folder, file)
                if os.path.isfile(file_path):
                    file_ext = os.path.splitext(file)[1].lower()
                    if file_ext in self.supported_formats:
                        found_images.append(file_path)

        return found_images

    def get_naming_convention_info(self, series_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Get information about the naming convention for cover images.

        Args:
            series_info: Optional series information

        Returns:
            Dictionary with naming convention information
        """
        if series_info:
            book_number = series_info.get('book_number', 1)
            return {
                "type": "series",
                "filename": f"Book{book_number}.jpg",
                "pattern": "Book{number}.jpg (e.g., Book1.jpg, Book2.jpg)",
                "description": f"For series books, use Book{book_number}.jpg"
            }
        else:
            return {
                "type": "single",
                "filename": "Cover.jpg",
                "pattern": "Cover.jpg",
                "description": "For single books, use Cover.jpg"
            }

    def validate_cover_image(self, image_path: str) -> Tuple[bool, str]:
        """
        Validate a cover image file.

        Args:
            image_path: Path to the image file

        Returns:
            Tuple of (is_valid, message)
        """
        if not os.path.exists(image_path):
            return False, "File does not exist"

        if not os.path.isfile(image_path):
            return False, "Path is not a file"

        file_ext = os.path.splitext(image_path)[1].lower()
        if file_ext not in self.supported_formats:
            supported = ", ".join(self.supported_formats)
            return False, f"Unsupported format. Supported formats: {supported}"

        # Check file size (should be reasonable for a cover image)
        try:
            file_size = os.path.getsize(image_path)
            if file_size < 1024:  # Less than 1KB
                return False, "File is too small to be a valid image"
            if file_size > 50 * 1024 * 1024:  # More than 50MB
                return False, "File is too large (max 50MB)"
        except OSError:
            return False, "Cannot read file size"

        return True, "Valid cover image"

    def copy_cover_to_expected_location(self, source_path: str, title: str,
                                      series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Copy a cover image to the expected location in the root covers directory.

        Args:
            source_path: Path to the source image
            title: Book or series title
            series_info: Optional series information

        Returns:
            Path to the copied image
        """
        # Validate the source image
        is_valid, message = self.validate_cover_image(source_path)
        if not is_valid:
            raise ValueError(f"Invalid cover image: {message}")

        # Get the expected destination path
        expected_path = self.get_expected_cover_path(title, series_info)

        # Create the directory if it doesn't exist
        os.makedirs(os.path.dirname(expected_path), exist_ok=True)

        # Copy the file
        shutil.copy2(source_path, expected_path)

        console.print(f"[bold green]✓[/bold green] Cover image copied to: [bold cyan]{expected_path}[/bold cyan]")

        return expected_path

    def get_cover_folder_structure_info(self, title: str,
                                      series_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Get information about the cover folder structure in the root covers directory.

        Args:
            title: Book or series title
            series_info: Optional series information

        Returns:
            Dictionary with folder structure information
        """
        cover_folder = self.create_cover_folder(title, series_info)
        expected_path = self.get_expected_cover_path(title, series_info)
        naming_info = self.get_naming_convention_info(series_info)

        return {
            "cover_folder": cover_folder,
            "expected_path": expected_path,
            "naming_convention": naming_info,
            "supported_formats": self.supported_formats,
            "folder_exists": os.path.exists(cover_folder)
        }

    def cleanup_legacy_covers(self, book_dir: str) -> List[str]:
        """
        Clean up legacy cover files from the book directory.

        Args:
            book_dir: Directory where the book is stored

        Returns:
            List of cleaned up file paths
        """
        cleaned_files = []

        if not os.path.exists(book_dir):
            return cleaned_files

        for file in os.listdir(book_dir):
            if file.lower().startswith('cover') and os.path.isfile(os.path.join(book_dir, file)):
                file_ext = os.path.splitext(file)[1].lower()
                if file_ext in self.supported_formats:
                    file_path = os.path.join(book_dir, file)
                    try:
                        os.remove(file_path)
                        cleaned_files.append(file_path)
                        console.print(f"[bold yellow]Cleaned up legacy cover:[/bold yellow] {file}")
                    except OSError as e:
                        console.print(f"[bold red]Failed to remove {file}: {str(e)}[/bold red]")

        return cleaned_files
