"""
Utility functions for file operations.
"""
import os
import json
import zipfile
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path

# Import SeriesManager conditionally to avoid circular imports
try:
    from src.core.series_manager import SeriesManager
except ImportError:
    SeriesManager = None


def sanitize_filename(filename: str) -> str:
    """
    Sanitize a string to be used as a filename.

    Args:
        filename: The string to sanitize

    Returns:
        A sanitized filename
    """
    # Replace invalid characters with underscores
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


def create_series_directory(series_title: str) -> str:
    """
    Create an output directory for a series.

    Args:
        series_title: The title of the series

    Returns:
        Path to the created directory
    """
    # Sanitize the title for use as a directory name
    dir_name = sanitize_filename(series_title)

    # Create the series directory
    output_dir = os.path.join("output", "series", dir_name)

    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    return output_dir

def create_output_directory(novel_title: str, series_manager=None, book_number: int = None) -> str:
    """
    Create an output directory for the novel.

    Args:
        novel_title: The title of the novel
        series_manager: Optional SeriesManager instance if this book is part of a series
        book_number: Book number in the series (if part of a series)

    Returns:
        Path to the created directory
    """
    # Sanitize the title for use as a directory name
    dir_name = sanitize_filename(novel_title)

    # Add timestamp to make it unique
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # If this is part of a series, organize it in the series directory
    if series_manager and book_number:
        # Create series directory
        series_dir = create_series_directory(series_manager.series_title)

        # Create book directory within series directory
        output_dir = os.path.join(series_dir, f"book_{book_number:02d}_{dir_name}")
    else:
        # Standard output directory
        output_dir = f"output/{dir_name}_{timestamp}"

    # Create the directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    return output_dir


def save_novel_json(novel_data: Dict[str, Any], output_dir: str) -> str:
    """
    Save novel data as JSON.

    Args:
        novel_data: Dictionary containing novel data
        output_dir: Directory to save the file in

    Returns:
        Path to the saved file
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Save the novel data as JSON
    json_path = os.path.join(output_dir, "novel_data.json")
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(novel_data, f, indent=2, ensure_ascii=False)

    return json_path


def save_chapter_text(chapter_num: int, chapter_title: str, chapter_text: str, output_dir: str) -> str:
    """
    Save a chapter as a text file.

    Args:
        chapter_num: Chapter number
        chapter_title: Chapter title
        chapter_text: Chapter content
        output_dir: Directory to save the file in

    Returns:
        Path to the saved file
    """
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create a filename
    filename = f"chapter_{chapter_num:02d}_{sanitize_filename(chapter_title)}.txt"
    file_path = os.path.join(output_dir, filename)

    # Save the chapter
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(f"Chapter {chapter_num}: {chapter_title}\n\n")
        f.write(chapter_text)

    return file_path


def load_novel_json(json_path: str) -> Dict[str, Any]:
    """
    Load novel data from a JSON file.

    Args:
        json_path: Path to the JSON file

    Returns:
        Dictionary containing novel data
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        novel_data = json.load(f)

    return novel_data


def get_series_files(series_dir: str, include_formats: List[str] = None) -> Dict[str, List[str]]:
    """
    Get all files for a series organized by book.

    Args:
        series_dir: Path to the series directory
        include_formats: List of file extensions to include (e.g., ['.epub', '.pdf', '.json'])
                        If None, includes all files

    Returns:
        Dictionary with book directories as keys and lists of file paths as values
    """
    if include_formats is None:
        include_formats = ['.epub', '.pdf', '.mobi', '.azw3', '.docx', '.html', '.json', '.jpg', '.png']

    # Convert to lowercase for case-insensitive matching
    include_formats = [fmt.lower() if fmt.startswith('.') else f'.{fmt.lower()}' for fmt in include_formats]

    series_files = {}

    if not os.path.exists(series_dir):
        return series_files

    # Walk through the series directory
    for root, dirs, files in os.walk(series_dir):
        # Skip the root series directory itself
        if root == series_dir:
            continue

        # Get the book directory name
        book_dir_name = os.path.basename(root)

        # Only process book directories (those starting with "book_")
        if not book_dir_name.startswith("book_"):
            continue

        book_files = []
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[1].lower()

            # Include file if it matches the desired formats
            if file_ext in include_formats:
                book_files.append(file_path)

        if book_files:
            series_files[book_dir_name] = book_files

    return series_files


def zip_series_books(series_dir: str, output_path: str, include_formats: List[str] = None,
                    progress_callback: callable = None) -> Tuple[bool, str]:
    """
    Create a zip archive of all books in a series.

    Args:
        series_dir: Path to the series directory
        output_path: Path where the zip file should be created
        include_formats: List of file extensions to include (e.g., ['.epub', '.pdf'])
                        If None, includes common ebook formats
        progress_callback: Optional callback function to report progress

    Returns:
        Tuple of (success: bool, message: str)
    """
    try:
        # Default formats if none specified
        if include_formats is None:
            include_formats = ['.epub', '.pdf', '.mobi', '.azw3', '.json']

        # Get all series files
        series_files = get_series_files(series_dir, include_formats)

        if not series_files:
            return False, "No files found to zip with the specified formats."

        # Count total files for progress tracking
        total_files = sum(len(files) for files in series_files.values())
        processed_files = 0

        # Create the zip file
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add series info file if it exists
            series_info_path = os.path.join(series_dir, "series_info.json")
            if os.path.exists(series_info_path):
                zipf.write(series_info_path, "series_info.json")
                if progress_callback:
                    progress_callback(1, total_files + 1, "Adding series info...")

            # Process each book
            for book_dir_name, book_files in sorted(series_files.items()):
                # Extract book number for proper sorting
                try:
                    book_num = int(book_dir_name.split('_')[1])
                    book_folder_name = f"Book_{book_num:02d}"
                except (IndexError, ValueError):
                    book_folder_name = book_dir_name

                # Add each file to the zip
                for file_path in book_files:
                    file_name = os.path.basename(file_path)
                    # Create organized structure in zip: Book_01/filename.ext
                    zip_path = f"{book_folder_name}/{file_name}"

                    zipf.write(file_path, zip_path)
                    processed_files += 1

                    if progress_callback:
                        progress_callback(processed_files, total_files, f"Adding {file_name}...")

        return True, f"Successfully created zip archive with {total_files} files."

    except Exception as e:
        return False, f"Error creating zip archive: {str(e)}"
