"""
Popular Science Genre Recommendations

Provides style variants for popular science writing, each offering different
approaches to Scientific concepts for general audiences.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a popular science profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Dr Samuel Voss (Master Style)",
            "base_profile": "dr_samuel_voss",
            "style_variant": "Master",
            "description": "Science writing mastery with clear explanation",
            "writing_approach": {
                "genre_focus": "Scientific concepts for general audiences",
                "style_emphasis": "master_approach",
                "target_approach": "science writing mastery with clear explanation"
            },
            "specialties": [
                "Popular Science mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Popular Science readers seeking master approach",
            "chapter_approach": "Master-focused popular science development"
        },
        "Innovator": {
            "name": "Dr Samuel Voss (Innovator Style)",
            "base_profile": "dr_samuel_voss",
            "style_variant": "Innovator",
            "description": "Fresh approaches to science communication",
            "writing_approach": {
                "genre_focus": "Scientific concepts for general audiences",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh approaches to science communication"
            },
            "specialties": [
                "Popular Science mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Popular Science readers seeking innovator approach",
            "chapter_approach": "Innovator-focused popular science development"
        },
        "Storyteller": {
            "name": "Dr Samuel Voss (Storyteller Style)",
            "base_profile": "dr_samuel_voss",
            "style_variant": "Storyteller",
            "description": "Engaging scientific narratives",
            "writing_approach": {
                "genre_focus": "Scientific concepts for general audiences",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging scientific narratives"
            },
            "specialties": [
                "Popular Science mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Popular Science readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused popular science development"
        },
        "Craftsperson": {
            "name": "Dr Samuel Voss (Craftsperson Style)",
            "base_profile": "dr_samuel_voss",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in science writing",
            "writing_approach": {
                "genre_focus": "Scientific concepts for general audiences",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in science writing"
            },
            "specialties": [
                "Popular Science mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Popular Science readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused popular science development"
        },
        "Commercial": {
            "name": "Dr Samuel Voss (Commercial Style)",
            "base_profile": "dr_samuel_voss",
            "style_variant": "Commercial",
            "description": "Accessible science with mass appeal",
            "writing_approach": {
                "genre_focus": "Scientific concepts for general audiences",
                "style_emphasis": "commercial_approach",
                "target_approach": "accessible science with mass appeal"
            },
            "specialties": [
                "Popular Science mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Popular Science readers seeking commercial approach",
            "chapter_approach": "Commercial-focused popular science development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Science writing mastery with clear explanation",
        "Innovator": "Fresh approaches to science communication",
        "Storyteller": "Engaging scientific narratives",
        "Craftsperson": "Technical excellence in science writing",
        "Commercial": "Accessible science with mass appeal",
    }