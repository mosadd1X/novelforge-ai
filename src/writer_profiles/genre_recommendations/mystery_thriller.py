"""
Mystery Thriller Genre Recommendations

Provides style variants for mystery thriller writing, each offering different
approaches to Fast-paced investigation with thriller elements.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a mystery thriller profile variant by style.

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
            "description": "Expert blend of mystery and thriller elements",
            "writing_approach": {
                "genre_focus": "Fast-paced investigation with thriller elements",
                "style_emphasis": "master_approach",
                "target_approach": "expert blend of mystery and thriller elements"
            },
            "specialties": [
                "Mystery Thriller mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery Thriller readers seeking master approach",
            "chapter_approach": "Master-focused mystery thriller development"
        },
        "Innovator": {
            "name": "Detective Marcus Kane (Innovator Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Innovator",
            "description": "Contemporary thriller-mystery with fresh twists",
            "writing_approach": {
                "genre_focus": "Fast-paced investigation with thriller elements",
                "style_emphasis": "innovator_approach",
                "target_approach": "contemporary thriller-mystery with fresh twists"
            },
            "specialties": [
                "Mystery Thriller mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery Thriller readers seeking innovator approach",
            "chapter_approach": "Innovator-focused mystery thriller development"
        },
        "Storyteller": {
            "name": "Detective Marcus Kane (Storyteller Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Storyteller",
            "description": "Gripping narratives with mystery and suspense",
            "writing_approach": {
                "genre_focus": "Fast-paced investigation with thriller elements",
                "style_emphasis": "storyteller_approach",
                "target_approach": "gripping narratives with mystery and suspense"
            },
            "specialties": [
                "Mystery Thriller mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery Thriller readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused mystery thriller development"
        },
        "Craftsperson": {
            "name": "Detective Marcus Kane (Craftsperson Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Craftsperson",
            "description": "Sophisticated thriller-mystery construction",
            "writing_approach": {
                "genre_focus": "Fast-paced investigation with thriller elements",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "sophisticated thriller-mystery construction"
            },
            "specialties": [
                "Mystery Thriller mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery Thriller readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused mystery thriller development"
        },
        "Commercial": {
            "name": "Detective Marcus Kane (Commercial Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Commercial",
            "description": "Popular thriller-mystery with mass appeal",
            "writing_approach": {
                "genre_focus": "Fast-paced investigation with thriller elements",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular thriller-mystery with mass appeal"
            },
            "specialties": [
                "Mystery Thriller mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery Thriller readers seeking commercial approach",
            "chapter_approach": "Commercial-focused mystery thriller development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Expert blend of mystery and thriller elements",
        "Innovator": "Contemporary thriller-mystery with fresh twists",
        "Storyteller": "Gripping narratives with mystery and suspense",
        "Craftsperson": "Sophisticated thriller-mystery construction",
        "Commercial": "Popular thriller-mystery with mass appeal",
    }