"""
Mystery Genre Recommendations

Provides style variants for mystery writing, each offering different
approaches to Investigation, suspense, puzzle-solving.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a mystery profile variant by style.

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
            "description": "Classic detective mastery with logical deduction",
            "writing_approach": {
                "genre_focus": "Investigation, suspense, puzzle-solving",
                "style_emphasis": "master_approach",
                "target_approach": "classic detective mastery with logical deduction"
            },
            "specialties": [
                "Mystery mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery readers seeking master approach",
            "chapter_approach": "Master-focused mystery development"
        },
        "Innovator": {
            "name": "Detective Marcus Kane (Innovator Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Innovator",
            "description": "Modern mystery with fresh investigative approaches",
            "writing_approach": {
                "genre_focus": "Investigation, suspense, puzzle-solving",
                "style_emphasis": "innovator_approach",
                "target_approach": "modern mystery with fresh investigative approaches"
            },
            "specialties": [
                "Mystery mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery readers seeking innovator approach",
            "chapter_approach": "Innovator-focused mystery development"
        },
        "Storyteller": {
            "name": "Detective Marcus Kane (Storyteller Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Storyteller",
            "description": "Engaging mystery narratives with compelling plots",
            "writing_approach": {
                "genre_focus": "Investigation, suspense, puzzle-solving",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging mystery narratives with compelling plots"
            },
            "specialties": [
                "Mystery mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused mystery development"
        },
        "Craftsperson": {
            "name": "Detective Marcus Kane (Craftsperson Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in mystery construction",
            "writing_approach": {
                "genre_focus": "Investigation, suspense, puzzle-solving",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in mystery construction"
            },
            "specialties": [
                "Mystery mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused mystery development"
        },
        "Commercial": {
            "name": "Detective Marcus Kane (Commercial Style)",
            "base_profile": "detective_marcus_kane",
            "style_variant": "Commercial",
            "description": "Popular mystery with broad market appeal",
            "writing_approach": {
                "genre_focus": "Investigation, suspense, puzzle-solving",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular mystery with broad market appeal"
            },
            "specialties": [
                "Mystery mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Mystery readers seeking commercial approach",
            "chapter_approach": "Commercial-focused mystery development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Classic detective mastery with logical deduction",
        "Innovator": "Modern mystery with fresh investigative approaches",
        "Storyteller": "Engaging mystery narratives with compelling plots",
        "Craftsperson": "Technical excellence in mystery construction",
        "Commercial": "Popular mystery with broad market appeal",
    }