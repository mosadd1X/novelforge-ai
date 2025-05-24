"""
Middle Grade Genre Recommendations

Provides style variants for middle grade writing, each offering different
approaches to Stories for middle-grade readers (ages 8-12).
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a middle grade profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Luna Brightwater (Master Style)",
            "base_profile": "luna_brightwater",
            "style_variant": "Master",
            "description": "Middle grade mastery with age-appropriate depth",
            "writing_approach": {
                "genre_focus": "Stories for middle-grade readers (ages 8-12)",
                "style_emphasis": "master_approach",
                "target_approach": "middle grade mastery with age-appropriate depth"
            },
            "specialties": [
                "Middle Grade mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Middle Grade readers seeking master approach",
            "chapter_approach": "Master-focused middle grade development"
        },
        "Innovator": {
            "name": "Luna Brightwater (Innovator Style)",
            "base_profile": "luna_brightwater",
            "style_variant": "Innovator",
            "description": "Fresh approaches to middle grade storytelling",
            "writing_approach": {
                "genre_focus": "Stories for middle-grade readers (ages 8-12)",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh approaches to middle grade storytelling"
            },
            "specialties": [
                "Middle Grade mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Middle Grade readers seeking innovator approach",
            "chapter_approach": "Innovator-focused middle grade development"
        },
        "Storyteller": {
            "name": "Luna Brightwater (Storyteller Style)",
            "base_profile": "luna_brightwater",
            "style_variant": "Storyteller",
            "description": "Engaging narratives for young readers",
            "writing_approach": {
                "genre_focus": "Stories for middle-grade readers (ages 8-12)",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging narratives for young readers"
            },
            "specialties": [
                "Middle Grade mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Middle Grade readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused middle grade development"
        },
        "Craftsperson": {
            "name": "Luna Brightwater (Craftsperson Style)",
            "base_profile": "luna_brightwater",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in children's literature",
            "writing_approach": {
                "genre_focus": "Stories for middle-grade readers (ages 8-12)",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in children's literature"
            },
            "specialties": [
                "Middle Grade mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Middle Grade readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused middle grade development"
        },
        "Commercial": {
            "name": "Luna Brightwater (Commercial Style)",
            "base_profile": "luna_brightwater",
            "style_variant": "Commercial",
            "description": "Popular middle grade with broad appeal",
            "writing_approach": {
                "genre_focus": "Stories for middle-grade readers (ages 8-12)",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular middle grade with broad appeal"
            },
            "specialties": [
                "Middle Grade mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Middle Grade readers seeking commercial approach",
            "chapter_approach": "Commercial-focused middle grade development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Middle grade mastery with age-appropriate depth",
        "Innovator": "Fresh approaches to middle grade storytelling",
        "Storyteller": "Engaging narratives for young readers",
        "Craftsperson": "Technical excellence in children's literature",
        "Commercial": "Popular middle grade with broad appeal",
    }