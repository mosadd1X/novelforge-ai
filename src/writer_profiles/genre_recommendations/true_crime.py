"""
True Crime Genre Recommendations

Provides style variants for true crime writing, each offering different
approaches to Real criminal cases and investigations.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a true crime profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Detective Marcus Kane (Master Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Master",
            "description": "True crime mastery with investigative depth",
            "writing_approach": {
                "genre_focus": "Real criminal cases and investigations",
                "style_emphasis": "master_approach",
                "target_approach": "true crime mastery with investigative depth"
            },
            "specialties": [
                "True Crime mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "True Crime readers seeking master approach",
            "chapter_approach": "Master-focused true crime development"
        },
        "Innovator": {
            "name": "Detective Marcus Kane (Innovator Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Innovator",
            "description": "Fresh true crime approaches and perspectives",
            "writing_approach": {
                "genre_focus": "Real criminal cases and investigations",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh true crime approaches and perspectives"
            },
            "specialties": [
                "True Crime mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "True Crime readers seeking innovator approach",
            "chapter_approach": "Innovator-focused true crime development"
        },
        "Storyteller": {
            "name": "Detective Marcus Kane (Storyteller Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Storyteller",
            "description": "Compelling true crime narratives",
            "writing_approach": {
                "genre_focus": "Real criminal cases and investigations",
                "style_emphasis": "storyteller_approach",
                "target_approach": "compelling true crime narratives"
            },
            "specialties": [
                "True Crime mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "True Crime readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused true crime development"
        },
        "Craftsperson": {
            "name": "Detective Marcus Kane (Craftsperson Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in crime reporting",
            "writing_approach": {
                "genre_focus": "Real criminal cases and investigations",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in crime reporting"
            },
            "specialties": [
                "True Crime mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "True Crime readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused true crime development"
        },
        "Commercial": {
            "name": "Detective Marcus Kane (Commercial Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Commercial",
            "description": "Popular true crime with mass appeal",
            "writing_approach": {
                "genre_focus": "Real criminal cases and investigations",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular true crime with mass appeal"
            },
            "specialties": [
                "True Crime mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "True Crime readers seeking commercial approach",
            "chapter_approach": "Commercial-focused true crime development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "True crime mastery with investigative depth",
        "Innovator": "Fresh true crime approaches and perspectives",
        "Storyteller": "Compelling true crime narratives",
        "Craftsperson": "Technical excellence in crime reporting",
        "Commercial": "Popular true crime with mass appeal",
    }