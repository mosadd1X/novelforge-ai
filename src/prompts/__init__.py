"""
Genre-specific prompts for novel generation.

This module provides a comprehensive prompt system with specialized prompts
for each supported genre. Each genre has its own module with tailored prompts
for different stages of novel generation.
"""

from typing import Dict, Any, Optional
import importlib
import os

# List of all supported genres
SUPPORTED_GENRES = [
    "literary_fiction",
    "commercial_fiction", 
    "mystery",
    "mystery_thriller",
    "thriller",
    "romance",
    "fantasy",
    "epic_fantasy",
    "science_fiction",
    "historical_fiction",
    "horror",
    "young_adult",
    "middle_grade",
    "children_s_chapter_books",
    "short_story_collection",
    "novella",
    "graphic_novel",
    "memoir",
    "biography",
    "history",
    "self_help",
    "business",
    "popular_science",
    "academic",
    "travel",
    "cookbook",
    "how_to",
    "essay_collection",
    "philosophy",
    "true_crime",
    "poetry_collection",
    "creative_non_fiction",
    "speculative_fiction",
    "alternate_history",
    "contemporary_fiction",
    "paranormal_romance",
    "urban_fantasy",
    "dystopian"
]

def get_genre_prompts(genre: str) -> Optional[Any]:
    """
    Get the prompt module for a specific genre.
    
    Args:
        genre: The genre name (e.g., "fantasy", "mystery", etc.)
        
    Returns:
        The genre prompt module or None if not found
    """
    # Normalize genre name
    normalized_genre = genre.lower().replace(" ", "_").replace("/", "_").replace("-", "_")
    
    # Map common variations to our standard names
    genre_mappings = {
        "mystery_thriller": "mystery_thriller",
        "epic_fantasy": "epic_fantasy", 
        "science_fiction": "science_fiction",
        "historical_fiction": "historical_fiction",
        "young_adult": "young_adult",
        "middle_grade": "middle_grade",
        "children_s_chapter_books": "children_s_chapter_books",
        "short_story_collection": "short_story_collection",
        "graphic_novel": "graphic_novel",
        "self_help": "self_help",
        "popular_science": "popular_science",
        "how_to": "how_to",
        "essay_collection": "essay_collection",
        "true_crime": "true_crime",
        "poetry_collection": "poetry_collection",
        "creative_non_fiction": "creative_non_fiction",
        "speculative_fiction": "speculative_fiction",
        "alternate_history": "alternate_history",
        "contemporary_fiction": "contemporary_fiction",
        "paranormal_romance": "paranormal_romance",
        "urban_fantasy": "urban_fantasy",
        # Common variations
        "sci_fi": "science_fiction",
        "scifi": "science_fiction",
        "ya": "young_adult",
        "mg": "middle_grade",
        "literary": "literary_fiction",
        "commercial": "commercial_fiction",
        "hist_fic": "historical_fiction",
        "historical": "historical_fiction",
        "non_fiction": "creative_non_fiction",
        "nonfiction": "creative_non_fiction"
    }
    
    # Use mapping if available, otherwise use normalized genre
    final_genre = genre_mappings.get(normalized_genre, normalized_genre)
    
    # Check if genre is supported
    if final_genre not in SUPPORTED_GENRES:
        return None
    
    try:
        # Import the genre-specific prompt module
        module_name = f"prompts.{final_genre}"
        return importlib.import_module(module_name)
    except ImportError:
        return None

def get_prompt(genre: str, prompt_type: str, **kwargs) -> Optional[str]:
    """
    Get a specific prompt for a genre and prompt type.
    
    Args:
        genre: The genre name
        prompt_type: Type of prompt (e.g., "outline", "character", "chapter")
        **kwargs: Additional parameters for prompt formatting
        
    Returns:
        The formatted prompt string or None if not found
    """
    genre_module = get_genre_prompts(genre)
    if not genre_module:
        return None
    
    # Try to get the specific prompt function
    prompt_function_name = f"get_{prompt_type}_prompt"
    if hasattr(genre_module, prompt_function_name):
        prompt_function = getattr(genre_module, prompt_function_name)
        return prompt_function(**kwargs)
    
    return None

def list_available_genres() -> list:
    """
    List all available genres with prompt support.
    
    Returns:
        List of genre names that have prompt modules
    """
    available_genres = []
    prompts_dir = os.path.dirname(__file__)
    
    for genre in SUPPORTED_GENRES:
        genre_file = os.path.join(prompts_dir, f"{genre}.py")
        if os.path.exists(genre_file):
            available_genres.append(genre)
    
    return available_genres

def get_genre_info(genre: str) -> Optional[Dict[str, Any]]:
    """
    Get information about a specific genre's prompt capabilities.
    
    Args:
        genre: The genre name
        
    Returns:
        Dictionary with genre information or None if not found
    """
    genre_module = get_genre_prompts(genre)
    if not genre_module:
        return None
    
    info = {
        "genre": genre,
        "available_prompts": [],
        "description": getattr(genre_module, "GENRE_DESCRIPTION", ""),
        "characteristics": getattr(genre_module, "GENRE_CHARACTERISTICS", []),
        "typical_elements": getattr(genre_module, "TYPICAL_ELEMENTS", [])
    }
    
    # Check for available prompt types
    prompt_types = ["outline", "character", "chapter", "enhancement", "writer_profile"]
    for prompt_type in prompt_types:
        if hasattr(genre_module, f"get_{prompt_type}_prompt"):
            info["available_prompts"].append(prompt_type)
    
    return info
