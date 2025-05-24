"""
Historical Fiction Genre Recommendations

Provides style variants for historical fiction writing, each offering different
approaches to Historical periods with authentic detail.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a historical fiction profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Dr Patricia Blackwell (Master Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Master",
            "description": "Historical fiction mastery with period authenticity",
            "writing_approach": {
                "genre_focus": "Historical periods with authentic detail",
                "style_emphasis": "master_approach",
                "target_approach": "historical fiction mastery with period authenticity"
            },
            "specialties": [
                "Historical Fiction mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Historical Fiction readers seeking master approach",
            "chapter_approach": "Master-focused historical fiction development"
        },
        "Innovator": {
            "name": "Dr Patricia Blackwell (Innovator Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Innovator",
            "description": "Fresh perspectives on historical periods",
            "writing_approach": {
                "genre_focus": "Historical periods with authentic detail",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh perspectives on historical periods"
            },
            "specialties": [
                "Historical Fiction mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Historical Fiction readers seeking innovator approach",
            "chapter_approach": "Innovator-focused historical fiction development"
        },
        "Storyteller": {
            "name": "Dr Patricia Blackwell (Storyteller Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Storyteller",
            "description": "Compelling historical narratives with human drama",
            "writing_approach": {
                "genre_focus": "Historical periods with authentic detail",
                "style_emphasis": "storyteller_approach",
                "target_approach": "compelling historical narratives with human drama"
            },
            "specialties": [
                "Historical Fiction mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Historical Fiction readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused historical fiction development"
        },
        "Craftsperson": {
            "name": "Dr Patricia Blackwell (Craftsperson Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Craftsperson",
            "description": "Technical historical accuracy with literary quality",
            "writing_approach": {
                "genre_focus": "Historical periods with authentic detail",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical historical accuracy with literary quality"
            },
            "specialties": [
                "Historical Fiction mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Historical Fiction readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused historical fiction development"
        },
        "Commercial": {
            "name": "Dr Patricia Blackwell (Commercial Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Commercial",
            "description": "Popular historical fiction with broad appeal",
            "writing_approach": {
                "genre_focus": "Historical periods with authentic detail",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular historical fiction with broad appeal"
            },
            "specialties": [
                "Historical Fiction mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Historical Fiction readers seeking commercial approach",
            "chapter_approach": "Commercial-focused historical fiction development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Historical fiction mastery with period authenticity",
        "Innovator": "Fresh perspectives on historical periods",
        "Storyteller": "Compelling historical narratives with human drama",
        "Craftsperson": "Technical historical accuracy with literary quality",
        "Commercial": "Popular historical fiction with broad appeal",
    }