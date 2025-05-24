"""
Biography Genre Recommendations

Provides style variants for biography writing, each offering different
approaches to Life stories of notable individuals.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a biography profile variant by style.

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
            "description": "Biography mastery with comprehensive research",
            "writing_approach": {
                "genre_focus": "Life stories of notable individuals",
                "style_emphasis": "master_approach",
                "target_approach": "biography mastery with comprehensive research"
            },
            "specialties": [
                "Biography mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Biography readers seeking master approach",
            "chapter_approach": "Master-focused biography development"
        },
        "Innovator": {
            "name": "Dr Patricia Blackwell (Innovator Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Innovator",
            "description": "Fresh biographical approaches and perspectives",
            "writing_approach": {
                "genre_focus": "Life stories of notable individuals",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh biographical approaches and perspectives"
            },
            "specialties": [
                "Biography mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Biography readers seeking innovator approach",
            "chapter_approach": "Innovator-focused biography development"
        },
        "Storyteller": {
            "name": "Dr Patricia Blackwell (Storyteller Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Storyteller",
            "description": "Compelling biographical narratives",
            "writing_approach": {
                "genre_focus": "Life stories of notable individuals",
                "style_emphasis": "storyteller_approach",
                "target_approach": "compelling biographical narratives"
            },
            "specialties": [
                "Biography mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Biography readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused biography development"
        },
        "Craftsperson": {
            "name": "Dr Patricia Blackwell (Craftsperson Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in biographical writing",
            "writing_approach": {
                "genre_focus": "Life stories of notable individuals",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in biographical writing"
            },
            "specialties": [
                "Biography mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Biography readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused biography development"
        },
        "Commercial": {
            "name": "Dr Patricia Blackwell (Commercial Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Commercial",
            "description": "Popular biography with mass appeal",
            "writing_approach": {
                "genre_focus": "Life stories of notable individuals",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular biography with mass appeal"
            },
            "specialties": [
                "Biography mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Biography readers seeking commercial approach",
            "chapter_approach": "Commercial-focused biography development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Biography mastery with comprehensive research",
        "Innovator": "Fresh biographical approaches and perspectives",
        "Storyteller": "Compelling biographical narratives",
        "Craftsperson": "Technical excellence in biographical writing",
        "Commercial": "Popular biography with mass appeal",
    }