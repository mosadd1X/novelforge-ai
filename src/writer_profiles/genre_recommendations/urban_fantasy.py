"""
Urban Fantasy Genre Recommendations

Provides style variants for urban fantasy writing, each offering different
approaches to Fantasy in modern urban settings.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a urban fantasy profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Zara Blackthorn (Master Style)",
            "base_profile": "zara_blackthorn",
            "style_variant": "Master",
            "description": "Urban fantasy mastery with city magic",
            "writing_approach": {
                "genre_focus": "Fantasy in modern urban settings",
                "style_emphasis": "master_approach",
                "target_approach": "urban fantasy mastery with city magic"
            },
            "specialties": [
                "Urban Fantasy mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Urban Fantasy readers seeking master approach",
            "chapter_approach": "Master-focused urban fantasy development"
        },
        "Innovator": {
            "name": "Zara Blackthorn (Innovator Style)",
            "base_profile": "zara_blackthorn",
            "style_variant": "Innovator",
            "description": "Fresh urban fantasy concepts",
            "writing_approach": {
                "genre_focus": "Fantasy in modern urban settings",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh urban fantasy concepts"
            },
            "specialties": [
                "Urban Fantasy mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Urban Fantasy readers seeking innovator approach",
            "chapter_approach": "Innovator-focused urban fantasy development"
        },
        "Storyteller": {
            "name": "Zara Blackthorn (Storyteller Style)",
            "base_profile": "zara_blackthorn",
            "style_variant": "Storyteller",
            "description": "Engaging urban fantasy narratives",
            "writing_approach": {
                "genre_focus": "Fantasy in modern urban settings",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging urban fantasy narratives"
            },
            "specialties": [
                "Urban Fantasy mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Urban Fantasy readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused urban fantasy development"
        },
        "Craftsperson": {
            "name": "Zara Blackthorn (Craftsperson Style)",
            "base_profile": "zara_blackthorn",
            "style_variant": "Craftsperson",
            "description": "Technical urban fantasy excellence",
            "writing_approach": {
                "genre_focus": "Fantasy in modern urban settings",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical urban fantasy excellence"
            },
            "specialties": [
                "Urban Fantasy mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Urban Fantasy readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused urban fantasy development"
        },
        "Commercial": {
            "name": "Zara Blackthorn (Commercial Style)",
            "base_profile": "zara_blackthorn",
            "style_variant": "Commercial",
            "description": "Popular urban fantasy with broad appeal",
            "writing_approach": {
                "genre_focus": "Fantasy in modern urban settings",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular urban fantasy with broad appeal"
            },
            "specialties": [
                "Urban Fantasy mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Urban Fantasy readers seeking commercial approach",
            "chapter_approach": "Commercial-focused urban fantasy development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Urban fantasy mastery with city magic",
        "Innovator": "Fresh urban fantasy concepts",
        "Storyteller": "Engaging urban fantasy narratives",
        "Craftsperson": "Technical urban fantasy excellence",
        "Commercial": "Popular urban fantasy with broad appeal",
    }