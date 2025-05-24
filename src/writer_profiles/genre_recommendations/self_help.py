"""
Self Help Genre Recommendations

Provides style variants for self help writing, each offering different
approaches to Personal development and improvement.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a self help profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Dr Malcolm Sterling (Master Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Master",
            "description": "Self-help mastery with proven methodologies",
            "writing_approach": {
                "genre_focus": "Personal development and improvement",
                "style_emphasis": "master_approach",
                "target_approach": "self-help mastery with proven methodologies"
            },
            "specialties": [
                "Self Help mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Self Help readers seeking master approach",
            "chapter_approach": "Master-focused self help development"
        },
        "Innovator": {
            "name": "Dr Malcolm Sterling (Innovator Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Innovator",
            "description": "Fresh approaches to personal development",
            "writing_approach": {
                "genre_focus": "Personal development and improvement",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh approaches to personal development"
            },
            "specialties": [
                "Self Help mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Self Help readers seeking innovator approach",
            "chapter_approach": "Innovator-focused self help development"
        },
        "Storyteller": {
            "name": "Dr Malcolm Sterling (Storyteller Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Storyteller",
            "description": "Engaging self-improvement narratives",
            "writing_approach": {
                "genre_focus": "Personal development and improvement",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging self-improvement narratives"
            },
            "specialties": [
                "Self Help mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Self Help readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused self help development"
        },
        "Craftsperson": {
            "name": "Dr Malcolm Sterling (Craftsperson Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in instructional writing",
            "writing_approach": {
                "genre_focus": "Personal development and improvement",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in instructional writing"
            },
            "specialties": [
                "Self Help mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Self Help readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused self help development"
        },
        "Commercial": {
            "name": "Dr Malcolm Sterling (Commercial Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Commercial",
            "description": "Popular self-help with mass market appeal",
            "writing_approach": {
                "genre_focus": "Personal development and improvement",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular self-help with mass market appeal"
            },
            "specialties": [
                "Self Help mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Self Help readers seeking commercial approach",
            "chapter_approach": "Commercial-focused self help development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Self-help mastery with proven methodologies",
        "Innovator": "Fresh approaches to personal development",
        "Storyteller": "Engaging self-improvement narratives",
        "Craftsperson": "Technical excellence in instructional writing",
        "Commercial": "Popular self-help with mass market appeal",
    }