"""
Utility for setting default generation options based on genre.
"""
import re
from typing import Dict, Any, List, Optional, Tuple, Set


def get_genre_defaults(genre: str) -> Dict[str, Any]:
    """
    Get default generation options based on genre.

    Args:
        genre: The genre of the novel

    Returns:
        Dictionary containing default options
    """
    # Default options if genre not found
    default_options = {
        "target_length": "medium",
        "writing_style": "Descriptive and detailed",
        "pov": "Third person limited",
        "themes": ["Identity and self-discovery", "Relationships"],
        "chapter_count": 20,
        "target_word_count": 80000,
        "chapter_length": 4000,
        "min_chapter_length": 4000,  # Increased minimum words per chapter to avoid extensions
    }

    # Genre-specific defaults
    genre_defaults = {
        "test": {
            "target_length": "short",
            "writing_style": "Concise and direct",
            "pov": "Third person limited",
            "themes": ["Simple plot", "Basic character development"],
            "chapter_count": 4,
            "target_word_count": 12000,
            "chapter_length": 3500,
            "min_chapter_length": 3500,
        },
        # Fiction genres
        "literary fiction": {
            "target_length": "medium",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person limited",
            "themes": ["Identity and self-discovery", "Family", "Society"],
            "chapter_count": 15,
            "target_word_count": 85000,
            "chapter_length": 5500,
            "min_chapter_length": 3500,
        },
        "commercial fiction": {
            "target_length": "medium",
            "writing_style": "Conversational and casual",
            "pov": "Third person limited",
            "themes": ["Relationships", "Personal growth", "Overcoming obstacles"],
            "chapter_count": 30,
            "target_word_count": 90000,
            "chapter_length": 3000,
            "min_chapter_length": 3000,
        },
        "mystery": {
            "target_length": "medium",
            "writing_style": "Concise and direct",
            "pov": "First person",
            "themes": ["Justice", "Secrets", "Deception"],
            "chapter_count": 40,
            "target_word_count": 80000,
            "chapter_length": 2000,
            "min_chapter_length": 2000,
        },
        "mystery/thriller": {
            "target_length": "medium",
            "writing_style": "Concise and direct",
            "pov": "First person",
            "themes": ["Justice", "Secrets", "Deception", "Survival"],
            "chapter_count": 40,
            "target_word_count": 80000,
            "chapter_length": 2000,
            "min_chapter_length": 2000,
        },
        "thriller": {
            "target_length": "medium",
            "writing_style": "Concise and direct",
            "pov": "Third person limited",
            "themes": ["Survival", "Power and corruption", "Justice"],
            "chapter_count": 40,
            "target_word_count": 80000,
            "chapter_length": 2000,
            "min_chapter_length": 2000,
        },
        "romance": {
            "target_length": "medium",
            "writing_style": "Descriptive and detailed",
            "pov": "Alternating POVs",
            "themes": ["Love and relationships", "Personal growth", "Identity and self-discovery"],
            "chapter_count": 25,
            "target_word_count": 70000,
            "chapter_length": 2800,
            "min_chapter_length": 2800,
            "pov_structure": "alternating",  # Alternating between main characters
            "pov_characters": ["protagonist", "love interest"],  # Will be replaced with actual character names
        },
        "fantasy": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person limited",
            "themes": ["Good vs. evil", "Power", "Identity and self-discovery"],
            "chapter_count": 35,
            "target_word_count": 120000,
            "chapter_length": 3400,
            "min_chapter_length": 3400,
        },
        "epic fantasy": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Multiple POVs",
            "themes": ["Good vs. evil", "Power", "Politics", "War"],
            "chapter_count": 50,
            "target_word_count": 180000,
            "chapter_length": 3600,
            "min_chapter_length": 3600,
        },
        "science fiction": {
            "target_length": "long",
            "writing_style": "Technical and precise",
            "pov": "Third person limited",
            "themes": ["Technology and society", "Identity", "Ethics"],
            "chapter_count": 32,
            "target_word_count": 105000,
            "chapter_length": 3300,
            "min_chapter_length": 3300,
        },
        "historical fiction": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person limited",
            "themes": ["Society", "Politics", "Personal growth"],
            "chapter_count": 30,
            "target_word_count": 100000,
            "chapter_length": 3300,
            "min_chapter_length": 3300,
        },
        "horror": {
            "target_length": "medium",
            "writing_style": "Descriptive and detailed",
            "pov": "First person",
            "themes": ["Fear", "Survival", "Psychological"],
            "chapter_count": 25,
            "target_word_count": 70000,
            "chapter_length": 2800,
            "min_chapter_length": 2800,
        },
        "young adult": {
            "target_length": "medium",
            "writing_style": "Conversational and casual",
            "pov": "First person",
            "themes": ["Coming of age", "Identity and self-discovery", "Relationships"],
            "chapter_count": 28,
            "target_word_count": 65000,
            "chapter_length": 2300,
            "min_chapter_length": 2300,
        },
        "middle grade": {
            "target_length": "short",
            "writing_style": "Conversational and casual",
            "pov": "First person",
            "themes": ["Friendship", "Adventure", "Family"],
            "chapter_count": 20,
            "target_word_count": 40000,
            "chapter_length": 2000,
            "min_chapter_length": 2000,
        },
        "children's chapter books": {
            "target_length": "short",
            "writing_style": "Conversational and casual",
            "pov": "Third person limited",
            "themes": ["Friendship", "Adventure", "Learning"],
            "chapter_count": 10,
            "target_word_count": 15000,
            "chapter_length": 1500,
            "min_chapter_length": 1000,
        },
        "short story collection": {
            "target_length": "medium",
            "writing_style": "Varied",
            "pov": "Varied",
            "themes": ["Varied themes", "Connected elements"],
            "chapter_count": 14,
            "target_word_count": 60000,
            "chapter_length": 4000,
            "min_chapter_length": 3000,
        },
        "novella": {
            "target_length": "short",
            "writing_style": "Concise and focused",
            "pov": "Third person limited",
            "themes": ["Focused plot", "Limited characters"],
            "chapter_count": 10,
            "target_word_count": 30000,
            "chapter_length": 3000,
            "min_chapter_length": 2500,
        },
        "graphic novel": {
            "target_length": "short",
            "writing_style": "Visual and dialogue-focused",
            "pov": "Third person limited",
            "themes": ["Visual storytelling", "Dialogue-driven"],
            "chapter_count": 8,
            "target_word_count": 25000,
            "chapter_length": 3000,
            "min_chapter_length": 2000,
        },
        # Non-fiction genres
        "memoir": {
            "target_length": "medium",
            "writing_style": "Personal and reflective",
            "pov": "First person",
            "themes": ["Personal growth", "Life experiences", "Reflection"],
            "chapter_count": 16,
            "target_word_count": 80000,
            "chapter_length": 5000,
            "min_chapter_length": 3500,
        },
        "biography": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person limited",
            "themes": ["Life story", "Historical context", "Personal impact"],
            "chapter_count": 20,
            "target_word_count": 100000,
            "chapter_length": 5000,
            "min_chapter_length": 3500,
        },
        "history": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person omniscient",
            "themes": ["Historical events", "Cultural context", "Analysis"],
            "chapter_count": 15,
            "target_word_count": 100000,
            "chapter_length": 6500,
            "min_chapter_length": 4000,
        },
        "self-help": {
            "target_length": "medium",
            "writing_style": "Conversational and casual",
            "pov": "Second person",
            "themes": ["Personal growth", "Practical advice", "Actionable steps"],
            "chapter_count": 12,
            "target_word_count": 55000,
            "chapter_length": 4500,
            "min_chapter_length": 3000,
        },
        "business": {
            "target_length": "medium",
            "writing_style": "Concise and direct",
            "pov": "Third person",
            "themes": ["Business strategies", "Case studies", "Practical applications"],
            "chapter_count": 12,
            "target_word_count": 65000,
            "chapter_length": 5400,
            "min_chapter_length": 3500,
        },
        "popular science": {
            "target_length": "medium",
            "writing_style": "Conversational and educational",
            "pov": "Third person",
            "themes": ["Scientific concepts", "Explanations", "Real-world applications"],
            "chapter_count": 12,
            "target_word_count": 75000,
            "chapter_length": 6200,
            "min_chapter_length": 4000,
        },
        "academic": {
            "target_length": "long",
            "writing_style": "Technical and precise",
            "pov": "Third person",
            "themes": ["Research", "Analysis", "Theoretical frameworks"],
            "chapter_count": 15,
            "target_word_count": 115000,
            "chapter_length": 7600,
            "min_chapter_length": 5000,
        },
        "travel": {
            "target_length": "medium",
            "writing_style": "Descriptive and personal",
            "pov": "First person",
            "themes": ["Exploration", "Cultural experiences", "Personal journey"],
            "chapter_count": 12,
            "target_word_count": 60000,
            "chapter_length": 5000,
            "min_chapter_length": 3000,
        },
        "cookbook": {
            "target_length": "medium",
            "writing_style": "Instructional and personal",
            "pov": "First person",
            "themes": ["Food", "Techniques", "Cultural context"],
            "chapter_count": 10,
            "target_word_count": 50000,
            "chapter_length": 5000,
            "min_chapter_length": 3000,
        },
        "how-to": {
            "target_length": "medium",
            "writing_style": "Instructional and clear",
            "pov": "Second person",
            "themes": ["Instructions", "Techniques", "Practical applications"],
            "chapter_count": 12,
            "target_word_count": 55000,
            "chapter_length": 4500,
            "min_chapter_length": 3000,
        },
        "essay collection": {
            "target_length": "medium",
            "writing_style": "Varied and thoughtful",
            "pov": "First person",
            "themes": ["Varied themes", "Personal perspective", "Analysis"],
            "chapter_count": 16,
            "target_word_count": 65000,
            "chapter_length": 4000,
            "min_chapter_length": 2500,
        },
        "philosophy": {
            "target_length": "medium",
            "writing_style": "Technical and precise",
            "pov": "Third person",
            "themes": ["Concepts", "Arguments", "Analysis"],
            "chapter_count": 12,
            "target_word_count": 75000,
            "chapter_length": 6200,
            "min_chapter_length": 4000,
        },
        "true crime": {
            "target_length": "medium",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person",
            "themes": ["Investigation", "Psychology", "Justice"],
            "chapter_count": 20,
            "target_word_count": 85000,
            "chapter_length": 4200,
            "min_chapter_length": 3500,
        },
        # Hybrid/Specialized genres
        "poetry collection": {
            "target_length": "short",
            "writing_style": "Poetic and lyrical",
            "pov": "Varied",
            "themes": ["Varied themes", "Emotional depth", "Imagery"],
            "chapter_count": 70,
            "target_word_count": 35000,
            "chapter_length": 500,
            "min_chapter_length": 300,
        },
        "creative non-fiction": {
            "target_length": "medium",
            "writing_style": "Descriptive and literary",
            "pov": "First person",
            "themes": ["Personal experiences", "Factual content", "Literary techniques"],
            "chapter_count": 20,
            "target_word_count": 75000,
            "chapter_length": 3750,
            "min_chapter_length": 3000,
        },
        "speculative fiction": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person limited",
            "themes": ["Concept exploration", "Social commentary", "What-if scenarios"],
            "chapter_count": 30,
            "target_word_count": 100000,
            "chapter_length": 3300,
            "min_chapter_length": 3000,
        },
        "alternate history": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Third person limited",
            "themes": ["Historical divergence", "Social impact", "Political consequences"],
            "chapter_count": 30,
            "target_word_count": 105000,
            "chapter_length": 3500,
            "min_chapter_length": 3000,
        },
        "contemporary fiction": {
            "target_length": "medium",
            "writing_style": "Conversational and casual",
            "pov": "Third person limited",
            "themes": ["Current social issues", "Relationships", "Personal growth"],
            "chapter_count": 25,
            "target_word_count": 80000,
            "chapter_length": 3200,
            "min_chapter_length": 3000,
        },
        "paranormal romance": {
            "target_length": "medium",
            "writing_style": "Descriptive and detailed",
            "pov": "Alternating POVs",
            "themes": ["Supernatural elements", "Romance", "Personal growth"],
            "chapter_count": 30,
            "target_word_count": 85000,
            "chapter_length": 2800,
            "min_chapter_length": 2500,
            "pov_structure": "alternating",
            "pov_characters": ["protagonist", "love interest"],
        },
        "urban fantasy": {
            "target_length": "medium",
            "writing_style": "Descriptive and detailed",
            "pov": "First person",
            "themes": ["Magic in modern world", "Hidden societies", "Personal power"],
            "chapter_count": 32,
            "target_word_count": 90000,
            "chapter_length": 2800,
            "min_chapter_length": 2500,
        },
        "dystopian": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "First person",
            "themes": ["Social commentary", "Survival", "Resistance"],
            "chapter_count": 28,
            "target_word_count": 100000,
            "chapter_length": 3500,
            "min_chapter_length": 3000,
        }
    }

    # Find the closest matching genre
    for key in genre_defaults:
        if key.lower() in genre.lower() or genre.lower() in key.lower():
            return genre_defaults[key]

    # If no match found, try to extract from genre_guideline.md
    try:
        defaults = extract_from_guidelines(genre)
        if defaults:
            return defaults
    except Exception:
        pass

    return default_options


def extract_from_guidelines(genre: str) -> Optional[Dict[str, Any]]:
    """
    Extract default options from genre_guideline.md.

    Args:
        genre: The genre to look for

    Returns:
        Dictionary with default options or None if not found
    """
    try:
        with open("genre_guideline.md", "r", encoding="utf-8") as f:
            content = f.read()

        # Extract the table rows
        table_pattern = r"\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|"
        matches = re.findall(table_pattern, content)

        # Search for the genre
        for match in matches:
            genre_name = match[0].strip()
            if genre.lower() in genre_name.lower() or genre_name.lower() in genre.lower():
                # Extract chapter range
                chapter_range_str = match[2].strip()
                chapter_min, chapter_max = map(int, re.findall(r'\d+', chapter_range_str))
                chapter_count = (chapter_min + chapter_max) // 2

                # Extract word count range
                word_count_str = match[3].strip()
                word_count_min, word_count_max = map(
                    lambda x: int(x.replace(',', '')),
                    re.findall(r'\d+', word_count_str)
                )
                target_word_count = (word_count_min + word_count_max) // 2

                # Calculate chapter length
                chapter_length = target_word_count // chapter_count

                # Determine target length
                if target_word_count < 60000:
                    target_length = "short"
                elif target_word_count > 100000:
                    target_length = "long"
                else:
                    target_length = "medium"

                # Determine POV and writing style from additional sections
                pov = determine_pov_from_guidelines(genre, content)
                writing_style = determine_writing_style_from_genre(genre)
                themes = determine_themes_from_genre(genre)

                return {
                    "target_length": target_length,
                    "writing_style": writing_style,
                    "pov": pov,
                    "themes": themes,
                    "chapter_count": chapter_count,
                    "target_word_count": target_word_count,
                    "chapter_length": chapter_length,
                }

        return None

    except Exception as e:
        print(f"Error extracting from guidelines: {e}")
        return None


def determine_pov_from_guidelines(genre: str, content: str) -> str:
    """
    Determine POV from guidelines content.

    Args:
        genre: The genre to look for
        content: The content of the guidelines file

    Returns:
        Recommended POV
    """
    # Look for POV patterns section
    pov_section_match = re.search(r"### POV Patterns by Genre(.*?)###", content, re.DOTALL)

    if pov_section_match:
        pov_section = pov_section_match.group(1)

        # Check for genre-specific POV
        for line in pov_section.split('\n'):
            if genre.lower() in line.lower():
                if "first person" in line.lower():
                    return "First person"
                elif "multiple" in line.lower():
                    return "Multiple POVs"
                elif "third" in line.lower():
                    return "Third person limited"

    # Default POVs by genre type
    if any(g in genre.lower() for g in ["mystery", "thriller", "horror", "young adult"]):
        return "First person"
    elif any(g in genre.lower() for g in ["romance", "epic fantasy"]):
        return "Multiple POVs"
    else:
        return "Third person limited"


def determine_writing_style_from_genre(genre: str) -> str:
    """
    Determine writing style based on genre.

    Args:
        genre: The genre

    Returns:
        Recommended writing style
    """
    if any(g in genre.lower() for g in ["literary fiction", "fantasy", "historical fiction"]):
        return "Descriptive and detailed"
    elif any(g in genre.lower() for g in ["mystery", "thriller", "horror"]):
        return "Concise and direct"
    elif any(g in genre.lower() for g in ["young adult", "middle grade", "commercial fiction"]):
        return "Conversational and casual"
    elif any(g in genre.lower() for g in ["science fiction", "academic"]):
        return "Technical and precise"
    else:
        return "Descriptive and detailed"


def determine_themes_from_genre(genre: str) -> List[str]:
    """
    Determine common themes based on genre.

    Args:
        genre: The genre

    Returns:
        List of recommended themes
    """
    genre_themes = {
        "literary fiction": ["Identity and self-discovery", "Family", "Society"],
        "mystery": ["Justice", "Secrets", "Deception"],
        "thriller": ["Survival", "Power and corruption", "Justice"],
        "romance": ["Love and relationships", "Personal growth"],
        "fantasy": ["Good vs. evil", "Power", "Identity and self-discovery"],
        "science fiction": ["Technology and society", "Identity", "Ethics"],
        "historical fiction": ["Society", "Politics", "Personal growth"],
        "horror": ["Fear", "Survival", "Psychological"],
        "young adult": ["Coming of age", "Identity and self-discovery", "Relationships"],
        "middle grade": ["Friendship", "Adventure", "Family"],
    }

    # Find the closest matching genre
    for key in genre_themes:
        if key.lower() in genre.lower() or genre.lower() in key:
            return genre_themes[key]

    return ["Identity and self-discovery", "Relationships"]


def get_all_genres() -> List[str]:
    """
    Get a list of all available genres.

    Returns:
        List of all genre names, properly capitalized
    """
    # Get the genre defaults dictionary
    genre_defaults = {
        "test": {},
        # Fiction genres
        "literary fiction": {},
        "commercial fiction": {},
        "mystery": {},
        "mystery/thriller": {},
        "thriller": {},
        "romance": {},
        "fantasy": {},
        "epic fantasy": {},
        "science fiction": {},
        "historical fiction": {},
        "horror": {},
        "young adult": {},
        "middle grade": {},
        "children's chapter books": {},
        "short story collection": {},
        "novella": {},
        "graphic novel": {},
        # Non-fiction genres
        "memoir": {},
        "biography": {},
        "history": {},
        "self-help": {},
        "business": {},
        "popular science": {},
        "academic": {},
        "travel": {},
        "cookbook": {},
        "how-to": {},
        "essay collection": {},
        "philosophy": {},
        "true crime": {},
        # Hybrid/Specialized genres
        "poetry collection": {},
        "creative non-fiction": {},
        "speculative fiction": {},
        "alternate history": {},
        "contemporary fiction": {},
        "paranormal romance": {},
        "urban fantasy": {},
        "dystopian": {},
    }

    # Return a list of properly capitalized genre names
    return [genre.title() for genre in genre_defaults.keys()]
