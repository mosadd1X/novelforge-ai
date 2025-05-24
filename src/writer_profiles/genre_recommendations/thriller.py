"""
Thriller Genre Recommendations

Provides style variants for thriller writing, each offering different
approaches to High-stakes suspense and tension.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a thriller profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Marcus Steele (Master Style)",
            "base_profile": "marcus_steele",
            "style_variant": "Master",
            "description": "Classic thriller mastery with expert pacing",
            "writing_approach": {
                "genre_focus": "High-stakes suspense and tension",
                "style_emphasis": "master_approach",
                "target_approach": "classic thriller mastery with expert pacing"
            },
            "specialties": [
                "Thriller mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Thriller readers seeking master approach",
            "chapter_approach": "Master-focused thriller development"
        },
        "Innovator": {
            "name": "Marcus Steele (Innovator Style)",
            "base_profile": "marcus_steele",
            "style_variant": "Innovator",
            "description": "Modern thriller with innovative suspense techniques",
            "writing_approach": {
                "genre_focus": "High-stakes suspense and tension",
                "style_emphasis": "innovator_approach",
                "target_approach": "modern thriller with innovative suspense techniques"
            },
            "specialties": [
                "Thriller mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Thriller readers seeking innovator approach",
            "chapter_approach": "Innovator-focused thriller development"
        },
        "Storyteller": {
            "name": "Marcus Steele (Storyteller Style)",
            "base_profile": "marcus_steele",
            "style_variant": "Storyteller",
            "description": "Compelling thriller narratives with strong tension",
            "writing_approach": {
                "genre_focus": "High-stakes suspense and tension",
                "style_emphasis": "storyteller_approach",
                "target_approach": "compelling thriller narratives with strong tension"
            },
            "specialties": [
                "Thriller mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Thriller readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused thriller development"
        },
        "Craftsperson": {
            "name": "Marcus Steele (Craftsperson Style)",
            "base_profile": "marcus_steele",
            "style_variant": "Craftsperson",
            "description": "Technical thriller excellence with precise pacing",
            "writing_approach": {
                "genre_focus": "High-stakes suspense and tension",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical thriller excellence with precise pacing"
            },
            "specialties": [
                "Thriller mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Thriller readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused thriller development"
        },
        "Commercial": {
            "name": "Marcus Steele (Commercial Style)",
            "base_profile": "marcus_steele",
            "style_variant": "Commercial",
            "description": "Popular thriller with broad entertainment value",
            "writing_approach": {
                "genre_focus": "High-stakes suspense and tension",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular thriller with broad entertainment value"
            },
            "specialties": [
                "Thriller mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Thriller readers seeking commercial approach",
            "chapter_approach": "Commercial-focused thriller development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Classic thriller mastery with expert pacing",
        "Innovator": "Modern thriller with innovative suspense techniques",
        "Storyteller": "Compelling thriller narratives with strong tension",
        "Craftsperson": "Technical thriller excellence with precise pacing",
        "Commercial": "Popular thriller with broad entertainment value",
    }