"""
Utility functions for planning chapters based on genre.
"""
import os
import re
from typing import Dict, Tuple, List


def get_genre_guidelines(genre: str) -> Dict[str, any]:
    """
    Get chapter and word count guidelines for a specific genre.

    Args:
        genre: The genre to get guidelines for

    Returns:
        Dictionary with chapter_range and word_count_range
    """
    # Default values if genre not found
    default_guidelines = {
        "chapter_range": (20, 30),
        "word_count_range": (70000, 90000),
        "chapter_length": (3500, 4500),  # Increased to avoid extensions
        "notes": "Standard novel format"
    }

    # Try to find the genre in the guidelines file
    try:
        guidelines_path = os.path.join("docs", "genere_guideline.md")
        with open(guidelines_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract the table rows
        table_pattern = r"\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|"
        matches = re.findall(table_pattern, content)

        # Search for the genre
        for match in matches:
            genre_name = match[0].strip()
            if genre.lower() in genre_name.lower():
                # Extract chapter range
                chapter_range_str = match[2].strip()
                chapter_min, chapter_max = map(int, re.findall(r'\d+', chapter_range_str))

                # Extract word count range
                word_count_str = match[3].strip()
                word_count_min, word_count_max = map(
                    lambda x: int(x.replace(',', '')),
                    re.findall(r'\d+', word_count_str)
                )

                # Calculate average chapter length
                avg_min = word_count_min // chapter_max
                avg_max = word_count_max // chapter_min

                return {
                    "chapter_range": (chapter_min, chapter_max),
                    "word_count_range": (word_count_min, word_count_max),
                    "chapter_length": (avg_min, avg_max),
                    "notes": match[4].strip()
                }

        # If genre not found, return default
        return default_guidelines

    except Exception as e:
        print(f"Error reading genre guidelines: {e}")
        return default_guidelines


def recommend_chapter_count(genre: str, target_length: str = "medium") -> int:
    """
    Recommend a chapter count based on genre and desired length.

    Args:
        genre: The genre of the novel
        target_length: "short", "medium", or "long"

    Returns:
        Recommended number of chapters
    """
    guidelines = get_genre_guidelines(genre)
    chapter_min, chapter_max = guidelines["chapter_range"]

    if target_length == "short":
        return chapter_min
    elif target_length == "long":
        return chapter_max
    else:  # medium
        return (chapter_min + chapter_max) // 2


def recommend_word_count(genre: str, target_length: str = "medium") -> int:
    """
    Recommend a word count based on genre and desired length.

    Args:
        genre: The genre of the novel
        target_length: "short", "medium", or "long"

    Returns:
        Recommended word count
    """
    guidelines = get_genre_guidelines(genre)
    word_min, word_max = guidelines["word_count_range"]

    if target_length == "short":
        return word_min
    elif target_length == "long":
        return word_max
    else:  # medium
        return (word_min + word_max) // 2


def get_chapter_structure_by_genre(genre: str) -> Dict[str, any]:
    """
    Get recommended chapter structure based on genre.

    Args:
        genre: The genre of the novel

    Returns:
        Dictionary with structure recommendations
    """
    # Default structure
    default_structure = {
        "pov_style": "Single POV, third person",
        "chapter_length": "Medium (3,500-4,500 words)",  # Increased to avoid extensions
        "pacing": "Balanced",
        "special_elements": []
    }

    # Genre-specific structures
    structures = {
        "mystery": {
            "pov_style": "Limited POV, often first person or close third",
            "chapter_length": "Short (1,500-3,000 words) for pacing",
            "pacing": "Fast, with cliffhangers",
            "special_elements": ["Red herrings", "Clues", "Reveals"]
        },
        "thriller": {
            "pov_style": "Limited POV, often first person or close third",
            "chapter_length": "Short (1,500-3,000 words) for pacing",
            "pacing": "Fast, with cliffhangers",
            "special_elements": ["Tension", "Danger", "Time pressure"]
        },
        "romance": {
            "pov_style": "Dual POV, alternating chapters",
            "chapter_length": "Medium (2,500-4,000 words)",
            "pacing": "Emotional arcs",
            "special_elements": ["Meet", "Obstacle", "Growth", "Resolution"]
        },
        "fantasy": {
            "pov_style": "Multiple POVs possible",
            "chapter_length": "Medium to long (4,000-7,000 words)",
            "pacing": "Varied, with world-building",
            "special_elements": ["World-building", "Magic system", "Character journeys"]
        },
        "science fiction": {
            "pov_style": "Varied, often third person",
            "chapter_length": "Medium to long (3,000-6,000 words)",
            "pacing": "Concept exploration",
            "special_elements": ["Technology", "Societal implications", "Exploration"]
        },
        "literary fiction": {
            "pov_style": "Varied, often deep POV",
            "chapter_length": "Variable (3,000-7,000 words)",
            "pacing": "Character-driven",
            "special_elements": ["Internal conflict", "Thematic development"]
        },
        "young adult": {
            "pov_style": "Predominantly first person, limited POVs",
            "chapter_length": "Medium (3,500-4,500 words)",  # Increased to avoid extensions
            "pacing": "Fast, engaging",
            "special_elements": ["Coming of age", "Identity", "Relationships"]
        }
    }

    # Find the closest matching genre
    for key in structures:
        if key in genre.lower():
            return structures[key]

    return default_structure
