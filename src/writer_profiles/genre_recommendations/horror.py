"""
Horror Genre Recommendations

Provides style variants for horror writing, each offering different
approaches to Fear, suspense, and supernatural elements.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a horror profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Sebastian Darkmore (Master Style)",
            "base_profile": "sebastian_darkmore",
            "style_variant": "Master",
            "description": "Classic horror mastery with psychological depth",
            "writing_approach": {
                "genre_focus": "Fear, suspense, and supernatural elements",
                "style_emphasis": "master_approach",
                "target_approach": "classic horror mastery with psychological depth"
            },
            "specialties": [
                "Horror mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Horror readers seeking master approach",
            "chapter_approach": "Master-focused horror development"
        },
        "Innovator": {
            "name": "Sebastian Darkmore (Innovator Style)",
            "base_profile": "sebastian_darkmore",
            "style_variant": "Innovator",
            "description": "Modern horror with fresh frightening concepts",
            "writing_approach": {
                "genre_focus": "Fear, suspense, and supernatural elements",
                "style_emphasis": "innovator_approach",
                "target_approach": "modern horror with fresh frightening concepts"
            },
            "specialties": [
                "Horror mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Horror readers seeking innovator approach",
            "chapter_approach": "Innovator-focused horror development"
        },
        "Storyteller": {
            "name": "Sebastian Darkmore (Storyteller Style)",
            "base_profile": "sebastian_darkmore",
            "style_variant": "Storyteller",
            "description": "Compelling horror narratives with sustained tension",
            "writing_approach": {
                "genre_focus": "Fear, suspense, and supernatural elements",
                "style_emphasis": "storyteller_approach",
                "target_approach": "compelling horror narratives with sustained tension"
            },
            "specialties": [
                "Horror mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Horror readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused horror development"
        },
        "Craftsperson": {
            "name": "Sebastian Darkmore (Craftsperson Style)",
            "base_profile": "sebastian_darkmore",
            "style_variant": "Craftsperson",
            "description": "Technical horror excellence with atmospheric mastery",
            "writing_approach": {
                "genre_focus": "Fear, suspense, and supernatural elements",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical horror excellence with atmospheric mastery"
            },
            "specialties": [
                "Horror mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Horror readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused horror development"
        },
        "Commercial": {
            "name": "Sebastian Darkmore (Commercial Style)",
            "base_profile": "sebastian_darkmore",
            "style_variant": "Commercial",
            "description": "Popular horror with broad entertainment appeal",
            "writing_approach": {
                "genre_focus": "Fear, suspense, and supernatural elements",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular horror with broad entertainment appeal"
            },
            "specialties": [
                "Horror mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Horror readers seeking commercial approach",
            "chapter_approach": "Commercial-focused horror development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Classic horror mastery with psychological depth",
        "Innovator": "Modern horror with fresh frightening concepts",
        "Storyteller": "Compelling horror narratives with sustained tension",
        "Craftsperson": "Technical horror excellence with atmospheric mastery",
        "Commercial": "Popular horror with broad entertainment appeal",
    }