"""
Creative Non Fiction Genre Recommendations

Provides style variants for creative non fiction writing, each offering different
approaches to Literary non-fiction with creative elements.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a creative non fiction profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Elena Thornfield (Master Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Master",
            "description": "Creative non-fiction mastery with literary quality",
            "writing_approach": {
                "genre_focus": "Literary non-fiction with creative elements",
                "style_emphasis": "master_approach",
                "target_approach": "creative non-fiction mastery with literary quality"
            },
            "specialties": [
                "Creative Non Fiction mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Creative Non Fiction readers seeking master approach",
            "chapter_approach": "Master-focused creative non fiction development"
        },
        "Innovator": {
            "name": "Elena Thornfield (Innovator Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Innovator",
            "description": "Fresh creative non-fiction approaches",
            "writing_approach": {
                "genre_focus": "Literary non-fiction with creative elements",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh creative non-fiction approaches"
            },
            "specialties": [
                "Creative Non Fiction mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Creative Non Fiction readers seeking innovator approach",
            "chapter_approach": "Innovator-focused creative non fiction development"
        },
        "Storyteller": {
            "name": "Elena Thornfield (Storyteller Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Storyteller",
            "description": "Engaging creative non-fiction narratives",
            "writing_approach": {
                "genre_focus": "Literary non-fiction with creative elements",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging creative non-fiction narratives"
            },
            "specialties": [
                "Creative Non Fiction mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Creative Non Fiction readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused creative non fiction development"
        },
        "Craftsperson": {
            "name": "Elena Thornfield (Craftsperson Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in creative non-fiction",
            "writing_approach": {
                "genre_focus": "Literary non-fiction with creative elements",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in creative non-fiction"
            },
            "specialties": [
                "Creative Non Fiction mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Creative Non Fiction readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused creative non fiction development"
        },
        "Commercial": {
            "name": "Elena Thornfield (Commercial Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Commercial",
            "description": "Accessible creative non-fiction",
            "writing_approach": {
                "genre_focus": "Literary non-fiction with creative elements",
                "style_emphasis": "commercial_approach",
                "target_approach": "accessible creative non-fiction"
            },
            "specialties": [
                "Creative Non Fiction mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Creative Non Fiction readers seeking commercial approach",
            "chapter_approach": "Commercial-focused creative non fiction development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Creative non-fiction mastery with literary quality",
        "Innovator": "Fresh creative non-fiction approaches",
        "Storyteller": "Engaging creative non-fiction narratives",
        "Craftsperson": "Technical excellence in creative non-fiction",
        "Commercial": "Accessible creative non-fiction",
    }