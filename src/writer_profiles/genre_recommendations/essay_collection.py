"""
Essay Collection Genre Recommendations

Provides style variants for essay collection writing, each offering different
approaches to Curated collections of essays and commentary.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a essay collection profile variant by style.

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
            "description": "Essay mastery with intellectual depth",
            "writing_approach": {
                "genre_focus": "Curated collections of essays and commentary",
                "style_emphasis": "master_approach",
                "target_approach": "essay mastery with intellectual depth"
            },
            "specialties": [
                "Essay Collection mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Essay Collection readers seeking master approach",
            "chapter_approach": "Master-focused essay collection development"
        },
        "Innovator": {
            "name": "Elena Thornfield (Innovator Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Innovator",
            "description": "Fresh essay approaches and perspectives",
            "writing_approach": {
                "genre_focus": "Curated collections of essays and commentary",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh essay approaches and perspectives"
            },
            "specialties": [
                "Essay Collection mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Essay Collection readers seeking innovator approach",
            "chapter_approach": "Innovator-focused essay collection development"
        },
        "Storyteller": {
            "name": "Elena Thornfield (Storyteller Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Storyteller",
            "description": "Engaging essay narratives",
            "writing_approach": {
                "genre_focus": "Curated collections of essays and commentary",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging essay narratives"
            },
            "specialties": [
                "Essay Collection mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Essay Collection readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused essay collection development"
        },
        "Craftsperson": {
            "name": "Elena Thornfield (Craftsperson Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in essay writing",
            "writing_approach": {
                "genre_focus": "Curated collections of essays and commentary",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in essay writing"
            },
            "specialties": [
                "Essay Collection mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Essay Collection readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused essay collection development"
        },
        "Commercial": {
            "name": "Elena Thornfield (Commercial Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Commercial",
            "description": "Accessible essay collections",
            "writing_approach": {
                "genre_focus": "Curated collections of essays and commentary",
                "style_emphasis": "commercial_approach",
                "target_approach": "accessible essay collections"
            },
            "specialties": [
                "Essay Collection mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Essay Collection readers seeking commercial approach",
            "chapter_approach": "Commercial-focused essay collection development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Essay mastery with intellectual depth",
        "Innovator": "Fresh essay approaches and perspectives",
        "Storyteller": "Engaging essay narratives",
        "Craftsperson": "Technical excellence in essay writing",
        "Commercial": "Accessible essay collections",
    }