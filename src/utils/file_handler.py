"""
Utility functions for file operations.
"""
import os
import json
from typing import Dict, Any, List, Optional
from datetime import datetime

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
