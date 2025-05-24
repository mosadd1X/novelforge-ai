"""
Utility for setting default generation options based on genre.

This module provides default settings for various novel genres, including:

Target Length Options:
- short: For shorter works like novellas, children's books (typically under 60,000 words)
- medium: For standard-length novels (typically 60,000-100,000 words)
- long: For longer works like epics, fantasy series (typically over 100,000 words)

Writing Style Options:
- Descriptive and detailed: Rich descriptions, elaborate prose (literary fiction, fantasy)
- Concise and direct: Straightforward, action-oriented prose (thrillers, mysteries)
- Conversational and casual: Informal, accessible language (YA, contemporary fiction)
- Technical and precise: Specialized terminology, accurate descriptions (sci-fi, academic)
- Various other styles specific to certain genres

POV (Point of View) Options:
- First person: Narrated from "I" perspective
- Third person limited: Focuses on one character's perspective at a time
- Third person omniscient: All-knowing narrator with access to multiple characters' thoughts
- Multiple POVs: Alternating between different character perspectives
- Alternating POVs: Enhanced flexible system that switches based on story needs
- Second person: Rare, uses "you" as the narrative voice (common in self-help)

Enhanced POV Features (for Alternating POVs):
- pov_structure: "flexible_alternating" enables story-driven POV switching
- pov_pattern: "story_driven" assigns POV based on chapter content and character relevance
- pov_strategy: "balanced_with_story_focus" maintains gender balance while prioritizing story needs
- Gender Detection: Automatically detects character gender from names and descriptions
- Supports both Western and Indian names for accurate gender identification
- Context-Aware Assignment: POV switches based on chapter outline and character involvement
- Flexible Alternating: Not rigid odd/even chapters but adapts to narrative requirements

Theme Options:
- Each genre has recommended themes that work well for that type of story
- Themes include concepts like "Identity and self-discovery", "Good vs. evil", etc.
- Multiple themes can be combined for more complex narratives

Chapter Parameters:
- chapter_count: Recommended number of chapters for the genre
- target_word_count: Total word count target for the entire book
- chapter_length: Average words per chapter
- min_chapter_length: Minimum words per chapter to avoid excessive chapter splitting
"""
import re
from typing import Dict, Any, List, Optional, Tuple


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
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Alternating POVs",
            # "themes": [ "Unspoken love and silent longing", "Grief and the weight of memory", "Emotional sacrifice and selflessness", "Love shaped by loss", "The fragility of human connection", "Identity beyond the past", "Forgiveness — of others and oneself", "Healing without forgetting", "The silence between words unsaid", "Ambition vs. emotional fulfillment", "Time as both healer and destroyer", "The complexity of second chances", "Cultural expectations and personal choices", "Mental health and invisible wounds", "The quiet power of presence" ],
            # "themes": ["Unspoken Love", "Emotional Sacrifice", "Mental Health Struggles", "Longing Without Receiving", "Love That Goes Unnoticed", "Letting Go When It Hurts the Most"],
            "themes": ["Unspoken love and silent longing","Emotional sacrifice and selflessness","Communication beyond words","Faith, spirituality, and inner peace","Cultural identity and family expectations","Personal growth through pain","The complexity of saying 'No' and meaning 'Not now'","Love that evolves without possession","Introversion and finding voice in silence","Dreams vs. duty"],
            "chapter_count": 22,  # Reduced from 25 to align with optimized chapter length (22 × 5000 = 110,000 words)
            "target_word_count": 110000,  # Increased to match aggressive chapter length targets
            "chapter_length": 5000,  # High target to ensure 4,000+ word generation on first attempt
            "min_chapter_length": 4000,  # Extension threshold - no extension needed if ≥4,000 words
            "pov_structure": "flexible_alternating",
            "pov_pattern": "story_driven",
            "pov_characters": ["male_protagonist", "female_protagonist"],
            "pov_strategy": "balanced_with_story_focus",
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
            "chapter_count": 6,  # Sections, not individual poems (AI determines actual count: 5-8 for short)
            "target_word_count": 5000,  # More realistic for poetry collections
            "chapter_length": 800,  # Average words per section
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
        "contemporary romance": {
            "target_length": "long",
            "writing_style": "Emotionally rich and culturally authentic",
            "pov": "Alternating POVs",
            "themes": ["Modern Love", "Cultural Identity", "Career vs. Relationships", "Family Expectations", "Personal Growth Through Love", "Contemporary Social Issues"],
            "chapter_count": 22,  # Optimized for efficient generation (22 × 5000 = 110,000 words)
            "target_word_count": 110000,  # Contemporary Romance novel length
            "chapter_length": 5000,  # High target to ensure 4,000+ word generation on first attempt
            "min_chapter_length": 4000,  # Extension threshold - no extension needed if ≥4,000 words
            "pov_structure": "flexible_alternating",
            "pov_pattern": "story_driven",
            "pov_characters": ["male_protagonist", "female_protagonist"],
            "pov_strategy": "balanced_with_story_focus",
        },
        "paranormal romance": {
            "target_length": "long",
            "writing_style": "Descriptive and detailed",
            "pov": "Alternating POVs",
            "themes": ["Supernatural elements", "Romance", "Personal growth"],
            "chapter_count": 30,
            "target_word_count": 85000,
            "chapter_length": 2800,
            "min_chapter_length": 2500,
            "pov_structure": "flexible_alternating",
            "pov_pattern": "story_driven",
            "pov_characters": ["male_protagonist", "female_protagonist"],
            "pov_strategy": "balanced_with_story_focus",
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
        "contemporary romance": {},
        "paranormal romance": {},
        "urban fantasy": {},
        "dystopian": {},
    }

    # Return a list of properly capitalized genre names
    return [genre.title() for genre in genre_defaults.keys()]


def create_flexible_pov_structure(characters: List[Dict[str, Any]], generation_options: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a flexible POV structure based on characters and generation options.

    Args:
        characters: List of character dictionaries
        generation_options: Generation options including POV settings

    Returns:
        Dictionary containing POV structure information
    """
    pov_structure = {
        "type": "flexible_alternating",
        "strategy": generation_options.get("pov_strategy", "balanced_with_story_focus"),
        "pattern": generation_options.get("pov_pattern", "story_driven"),
        "characters": [],
        "chapter_assignments": {},
        "gender_balance": True
    }

    # Identify POV characters and their genders
    pov_characters = []
    for char in characters:
        if char.get("pov_character") is True or char.get("pov_character") == "true":
            # Try to determine gender from character description
            gender = determine_character_gender(char)
            char["gender"] = gender
            pov_characters.append(char)

    # Sort by POV order if available, otherwise by gender for balance
    pov_characters.sort(key=lambda x: (x.get("pov_order", 999), x.get("gender", "unknown")))

    pov_structure["characters"] = pov_characters
    return pov_structure


def determine_character_gender(character: Dict[str, Any]) -> str:
    """
    Determine character gender from their description and name.

    Args:
        character: Character dictionary

    Returns:
        "male", "female", or "unknown"
    """
    name = character.get("name", "").lower()
    description = character.get("appearance", "").lower()
    personality = character.get("personality", "").lower()
    background = character.get("background", "").lower()

    # Combine all text for analysis
    full_text = f"{name} {description} {personality} {background}".lower()

    # Gender indicators
    male_indicators = [
        "he", "him", "his", "man", "male", "boy", "guy", "gentleman", "father", "dad",
        "brother", "son", "husband", "boyfriend", "king", "prince", "lord", "sir"
    ]

    female_indicators = [
        "she", "her", "hers", "woman", "female", "girl", "lady", "mother", "mom",
        "sister", "daughter", "wife", "girlfriend", "queen", "princess", "lady", "miss", "mrs"
    ]

    # Common male names (Western + Indian)
    male_names = [
        # Western names
        "alex", "alexander", "andrew", "anthony", "benjamin", "brad", "brian", "bruce",
        "charles", "chris", "christopher", "daniel", "david", "edward", "eric", "frank",
        "george", "henry", "jack", "james", "jason", "john", "joseph", "kevin", "mark",
        "matthew", "michael", "paul", "peter", "richard", "robert", "ryan", "stephen",
        "steven", "thomas", "william", "adam", "adrian", "alan", "austin", "blake",
        "brandon", "caleb", "cameron", "connor", "derek", "ethan", "evan", "gabriel",
        "ian", "jacob", "jordan", "joshua", "justin", "kyle", "logan", "lucas", "mason",
        "nathan", "nicholas", "noah", "owen", "samuel", "sean", "tyler", "zachary",
        # Indian male names
        "aarav", "aditya", "akash", "amit", "anand", "ankit", "anuj", "arjun", "ashish",
        "ashwin", "ayaan", "deepak", "dev", "dhruv", "gaurav", "harsh", "karan", "kartik", "kunal",
        "manish", "nikhil", "nitin", "pradeep", "prakash", "pranav", "rahul", "raj", "rajesh",
        "ravi", "rohit", "sachin", "sagar", "sahil", "sandeep", "sanjay", "shubham", "siddharth",
        "suresh", "tushar", "varun", "vikash", "vikram", "vinay", "vishal", "yash", "yogesh",
        "abhishek", "ajay", "akshay", "aman", "amitabh", "arun", "bharat", "chandan", "dinesh",
        "girish", "gopal", "hari", "hemant", "jagdish", "jayesh", "kamal", "krishna", "mahesh",
        "mukesh", "naresh", "pankaj", "pawan", "raghav", "ramesh", "ritesh", "shailesh", "shyam",
        "subhash", "sumit", "sunil", "surya", "umesh", "vijay", "vivek", "yogi"
    ]

    # Common female names (Western + Indian)
    female_names = [
        # Western names
        "alexandra", "amanda", "amy", "angela", "anna", "ashley", "barbara", "betty",
        "brenda", "carol", "carolyn", "catherine", "christine", "deborah", "diana",
        "donna", "dorothy", "elizabeth", "emily", "emma", "helen", "jennifer", "jessica",
        "karen", "kimberly", "laura", "linda", "lisa", "maria", "mary", "michelle",
        "nancy", "patricia", "rebecca", "ruth", "sandra", "sarah", "sharon", "stephanie",
        "susan", "abigail", "alyssa", "andrea", "brooke", "chloe", "claire", "grace",
        "hailey", "hannah", "isabella", "jasmine", "julia", "kayla", "lauren", "madison",
        "megan", "natalie", "nicole", "olivia", "rachel", "samantha", "sophia", "taylor",
        "victoria", "zoe",
        # Indian female names
        "aadhya", "aisha", "ananya", "anika", "anya","anjali", "anushka", "aparna", "arpita", "avni",
        "deepika", "diya", "divya", "gauri", "ishita", "jyoti", "kavya", "kiara", "kriti",
        "meera", "naina", "neha", "nisha", "pooja", "priya", "riya", "sakshi", "shreya",
        "simran", "sneha", "sonia", "swati", "tanvi", "tanya", "vaishali", "vidya", "zara",
        "aditi", "akshara", "alka", "amrita", "arya", "bhavana", "chitra", "devika", "garima",
        "harsha", "indira", "janvi", "kalpana", "lakshmi", "madhuri", "namrata", "pallavi",
        "rachna", "radha", "rashmi", "ritu", "sadhana", "sangeeta", "shanti", "shilpa",
        "sita", "sonal", "sunita", "sushma", "usha", "vandana", "veena", "yamini",
        "aarti", "archana", "geeta", "hema", "kiran", "lata", "mala", "nita", "poonam",
        "rekha", "renu", "rita", "ruby", "seema", "shobha", "sudha", "suman", "uma"
    ]

    # Count indicators
    male_score = 0
    female_score = 0

    # Check name
    first_name = name.split()[0] if name.split() else ""
    if first_name in male_names:
        male_score += 3
    elif first_name in female_names:
        female_score += 3

    # Check text indicators
    for indicator in male_indicators:
        if indicator in full_text:
            male_score += 1

    for indicator in female_indicators:
        if indicator in full_text:
            female_score += 1

    # Determine gender
    if male_score > female_score:
        return "male"
    elif female_score > male_score:
        return "female"
    else:
        return "unknown"


def assign_chapter_pov(chapter_num: int, pov_structure: Dict[str, Any],
                      chapter_outline: str = "", story_context: Dict[str, Any] = None) -> Optional[Dict[str, Any]]:
    """
    Assign POV character for a specific chapter based on story needs.

    Args:
        chapter_num: Chapter number (1-based)
        pov_structure: POV structure information
        chapter_outline: Chapter outline/description for context
        story_context: Additional story context

    Returns:
        POV character dictionary or None
    """
    if not pov_structure.get("characters"):
        return None

    strategy = pov_structure.get("strategy", "balanced_with_story_focus")
    pattern = pov_structure.get("pattern", "story_driven")
    characters = pov_structure["characters"]

    # If only one POV character, use that one
    if len(characters) == 1:
        return characters[0]

    # Story-driven POV assignment
    if pattern == "story_driven" and chapter_outline:
        # Analyze chapter outline for character focus
        outline_lower = chapter_outline.lower()

        # Score each character based on their presence/relevance in the outline
        character_scores = []
        for char in characters:
            score = 0
            name = char.get("name", "").lower()
            gender = char.get("gender", "unknown")

            # Check if character name appears in outline
            if name in outline_lower:
                score += 5

            # Check for gender-specific content
            if gender == "male":
                male_keywords = ["his", "he", "him", "man", "male", "father", "brother", "husband"]
                score += sum(1 for keyword in male_keywords if keyword in outline_lower)
            elif gender == "female":
                female_keywords = ["her", "she", "woman", "female", "mother", "sister", "wife"]
                score += sum(1 for keyword in female_keywords if keyword in outline_lower)

            character_scores.append((char, score))

        # Sort by score and return highest scoring character
        character_scores.sort(key=lambda x: x[1], reverse=True)
        if character_scores[0][1] > 0:
            return character_scores[0][0]

    # Fallback to balanced alternating
    if strategy == "balanced_with_story_focus":
        # Try to maintain gender balance while considering story needs
        male_chars = [c for c in characters if c.get("gender") == "male"]
        female_chars = [c for c in characters if c.get("gender") == "female"]

        # Simple alternating with preference for balance
        if male_chars and female_chars:
            # Alternate between male and female, but allow flexibility
            if chapter_num % 2 == 1:
                return male_chars[0] if male_chars else female_chars[0]
            else:
                return female_chars[0] if female_chars else male_chars[0]

    # Default: simple alternating by order
    char_index = (chapter_num - 1) % len(characters)
    return characters[char_index]


def get_pov_options() -> List[str]:
    """
    Get available POV options for the UI.

    Returns:
        List of POV option strings
    """
    return [
        "First person",
        "Third person limited",
        "Third person omniscient",
        "Alternating POVs",
        "Multiple POVs",
        "Second person"
    ]
