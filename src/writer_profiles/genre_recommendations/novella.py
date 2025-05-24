"""
Novella Genre Recommendations

Provides style variants for novella writing, each offering different
approaches to Extended short fiction with focused narrative.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a novella profile variant by style.

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
            "description": "Novella mastery with concentrated storytelling",
            "writing_approach": {
                "genre_focus": "Extended short fiction with focused narrative",
                "style_emphasis": "master_approach",
                "target_approach": "novella mastery with concentrated storytelling"
            },
            "specialties": [
                "Novella mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Novella readers seeking master approach",
            "chapter_approach": "Master-focused novella development"
        },
        "Innovator": {
            "name": "Elena Thornfield (Innovator Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Innovator",
            "description": "Fresh novella formats and approaches",
            "writing_approach": {
                "genre_focus": "Extended short fiction with focused narrative",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh novella formats and approaches"
            },
            "specialties": [
                "Novella mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Novella readers seeking innovator approach",
            "chapter_approach": "Innovator-focused novella development"
        },
        "Storyteller": {
            "name": "Elena Thornfield (Storyteller Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Storyteller",
            "description": "Compelling medium-length narratives",
            "writing_approach": {
                "genre_focus": "Extended short fiction with focused narrative",
                "style_emphasis": "storyteller_approach",
                "target_approach": "compelling medium-length narratives"
            },
            "specialties": [
                "Novella mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Novella readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused novella development"
        },
        "Craftsperson": {
            "name": "Elena Thornfield (Craftsperson Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Craftsperson",
            "description": "Technical novella excellence",
            "writing_approach": {
                "genre_focus": "Extended short fiction with focused narrative",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical novella excellence"
            },
            "specialties": [
                "Novella mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Novella readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused novella development"
        },
        "Commercial": {
            "name": "Elena Thornfield (Commercial Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Commercial",
            "description": "Popular novellas with broad appeal",
            "writing_approach": {
                "genre_focus": "Extended short fiction with focused narrative",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular novellas with broad appeal"
            },
            "specialties": [
                "Novella mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Novella readers seeking commercial approach",
            "chapter_approach": "Commercial-focused novella development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Novella mastery with concentrated storytelling",
        "Innovator": "Fresh novella formats and approaches",
        "Storyteller": "Compelling medium-length narratives",
        "Craftsperson": "Technical novella excellence",
        "Commercial": "Popular novellas with broad appeal",
    }