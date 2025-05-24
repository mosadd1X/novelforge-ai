"""
Dystopian Genre Recommendations

Provides style variants for dystopian writing, each offering different
approaches to Dark future societies and social commentary.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a dystopian profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Dr Sophia Chronos (Master Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Master",
            "description": "Dystopian mastery with social insight",
            "writing_approach": {
                "genre_focus": "Dark future societies and social commentary",
                "style_emphasis": "master_approach",
                "target_approach": "dystopian mastery with social insight"
            },
            "specialties": [
                "Dystopian mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Dystopian readers seeking master approach",
            "chapter_approach": "Master-focused dystopian development"
        },
        "Innovator": {
            "name": "Dr Sophia Chronos (Innovator Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Innovator",
            "description": "Fresh dystopian concepts and warnings",
            "writing_approach": {
                "genre_focus": "Dark future societies and social commentary",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh dystopian concepts and warnings"
            },
            "specialties": [
                "Dystopian mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Dystopian readers seeking innovator approach",
            "chapter_approach": "Innovator-focused dystopian development"
        },
        "Storyteller": {
            "name": "Dr Sophia Chronos (Storyteller Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Storyteller",
            "description": "Compelling dystopian narratives",
            "writing_approach": {
                "genre_focus": "Dark future societies and social commentary",
                "style_emphasis": "storyteller_approach",
                "target_approach": "compelling dystopian narratives"
            },
            "specialties": [
                "Dystopian mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Dystopian readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused dystopian development"
        },
        "Craftsperson": {
            "name": "Dr Sophia Chronos (Craftsperson Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Craftsperson",
            "description": "Technical dystopian excellence",
            "writing_approach": {
                "genre_focus": "Dark future societies and social commentary",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical dystopian excellence"
            },
            "specialties": [
                "Dystopian mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Dystopian readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused dystopian development"
        },
        "Commercial": {
            "name": "Dr Sophia Chronos (Commercial Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Commercial",
            "description": "Popular dystopian fiction with broad appeal",
            "writing_approach": {
                "genre_focus": "Dark future societies and social commentary",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular dystopian fiction with broad appeal"
            },
            "specialties": [
                "Dystopian mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Dystopian readers seeking commercial approach",
            "chapter_approach": "Commercial-focused dystopian development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Dystopian mastery with social insight",
        "Innovator": "Fresh dystopian concepts and warnings",
        "Storyteller": "Compelling dystopian narratives",
        "Craftsperson": "Technical dystopian excellence",
        "Commercial": "Popular dystopian fiction with broad appeal",
    }