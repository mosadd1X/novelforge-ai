"""
Travel Genre Recommendations

Provides style variants for travel writing, each offering different
approaches to Travel experiences and destination guides.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a travel profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Gabriel Montoya (Master Style)",
            "base_profile": "gabriel_montoya",
            "style_variant": "Master",
            "description": "Travel writing mastery with cultural insight",
            "writing_approach": {
                "genre_focus": "Travel experiences and destination guides",
                "style_emphasis": "master_approach",
                "target_approach": "travel writing mastery with cultural insight"
            },
            "specialties": [
                "Travel mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Travel readers seeking master approach",
            "chapter_approach": "Master-focused travel development"
        },
        "Innovator": {
            "name": "Gabriel Montoya (Innovator Style)",
            "base_profile": "gabriel_montoya",
            "style_variant": "Innovator",
            "description": "Fresh travel perspectives and approaches",
            "writing_approach": {
                "genre_focus": "Travel experiences and destination guides",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh travel perspectives and approaches"
            },
            "specialties": [
                "Travel mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Travel readers seeking innovator approach",
            "chapter_approach": "Innovator-focused travel development"
        },
        "Storyteller": {
            "name": "Gabriel Montoya (Storyteller Style)",
            "base_profile": "gabriel_montoya",
            "style_variant": "Storyteller",
            "description": "Engaging travel narratives and adventures",
            "writing_approach": {
                "genre_focus": "Travel experiences and destination guides",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging travel narratives and adventures"
            },
            "specialties": [
                "Travel mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Travel readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused travel development"
        },
        "Craftsperson": {
            "name": "Gabriel Montoya (Craftsperson Style)",
            "base_profile": "gabriel_montoya",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in travel writing",
            "writing_approach": {
                "genre_focus": "Travel experiences and destination guides",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in travel writing"
            },
            "specialties": [
                "Travel mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Travel readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused travel development"
        },
        "Commercial": {
            "name": "Gabriel Montoya (Commercial Style)",
            "base_profile": "gabriel_montoya",
            "style_variant": "Commercial",
            "description": "Popular travel guides with mass appeal",
            "writing_approach": {
                "genre_focus": "Travel experiences and destination guides",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular travel guides with mass appeal"
            },
            "specialties": [
                "Travel mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Travel readers seeking commercial approach",
            "chapter_approach": "Commercial-focused travel development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Travel writing mastery with cultural insight",
        "Innovator": "Fresh travel perspectives and approaches",
        "Storyteller": "Engaging travel narratives and adventures",
        "Craftsperson": "Technical excellence in travel writing",
        "Commercial": "Popular travel guides with mass appeal",
    }