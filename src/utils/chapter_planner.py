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

        # Extract the table rows - only match complete rows with exactly 5 columns
        # Split into lines and process each line individually to avoid regex issues
        lines = content.split('\n')
        matches = []

        for line in lines:
            # Skip lines that don't look like table rows
            if not line.strip().startswith('|') or line.count('|') != 6:
                continue

            # Extract the 5 columns from the line
            parts = line.split('|')[1:6]  # Skip first empty part and take 5 columns
            if len(parts) == 5:
                matches.append(tuple(part.strip() for part in parts))

        # Search for the genre - prioritize exact matches
        exact_match = None
        partial_match = None

        for match in matches:
            # Skip header rows and section dividers
            if len(match) != 5:
                continue

            genre_name = match[0].strip()

            # Skip rows that are headers or section dividers
            if (genre_name.startswith('**') or
                genre_name.lower() in ['genre', 'fiction', 'non-fiction', 'hybrid/specialized', 'testing'] or
                'range' in genre_name.lower()):
                continue

            # Check for exact match first
            if genre.lower() == genre_name.lower():
                exact_match = match
                break
            # Check for partial match (genre is contained in genre_name)
            elif genre.lower() in genre_name.lower() and len(genre) > 3:
                if partial_match is None:  # Take the first partial match
                    partial_match = match

        # Use exact match if found, otherwise use partial match
        selected_match = exact_match or partial_match
        if selected_match:
            # Extract chapter range
            chapter_range_str = selected_match[2].strip()
            chapter_numbers = re.findall(r'\d+', chapter_range_str)
            if len(chapter_numbers) >= 2:
                chapter_min, chapter_max = map(int, chapter_numbers[:2])

                # Extract word count range - look for numbers with commas first
                word_count_str = selected_match[3].strip()
                # First try to find numbers with commas (e.g., "50,000-90,000")
                word_count_with_commas = re.findall(r'\d{1,3}(?:,\d{3})+', word_count_str)
                if len(word_count_with_commas) >= 2:
                    word_count_min = int(word_count_with_commas[0].replace(',', ''))
                    word_count_max = int(word_count_with_commas[1].replace(',', ''))
                else:
                    # Fallback to regular number extraction
                    word_count_numbers = re.findall(r'\d+', word_count_str)
                    if len(word_count_numbers) >= 2:
                        word_count_min, word_count_max = map(int, word_count_numbers[:2])
                    else:
                        # Use defaults if parsing fails
                        word_count_min, word_count_max = 70000, 90000

                # Calculate average chapter length
                avg_min = word_count_min // chapter_max
                avg_max = word_count_max // chapter_min

                return {
                    "chapter_range": (chapter_min, chapter_max),
                    "word_count_range": (word_count_min, word_count_max),
                    "chapter_length": (avg_min, avg_max),
                    "notes": selected_match[4].strip()
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
