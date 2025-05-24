"""
Academic Genre Recommendations

Provides style variants for academic writing, each offering different
approaches to Scholarly research and academic discourse.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a academic profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Professor Elena Vasquez (Master Style)",
            "base_profile": "professor_elena_vasquez",
            "style_variant": "Master",
            "description": "Academic writing mastery with scholarly rigor",
            "writing_approach": {
                "genre_focus": "Scholarly research and academic discourse",
                "style_emphasis": "master_approach",
                "target_approach": "academic writing mastery with scholarly rigor"
            },
            "specialties": [
                "Academic mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Academic readers seeking master approach",
            "chapter_approach": "Master-focused academic development"
        },
        "Innovator": {
            "name": "Professor Elena Vasquez (Innovator Style)",
            "base_profile": "professor_elena_vasquez",
            "style_variant": "Innovator",
            "description": "Fresh academic approaches and methodologies",
            "writing_approach": {
                "genre_focus": "Scholarly research and academic discourse",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh academic approaches and methodologies"
            },
            "specialties": [
                "Academic mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Academic readers seeking innovator approach",
            "chapter_approach": "Innovator-focused academic development"
        },
        "Storyteller": {
            "name": "Professor Elena Vasquez (Storyteller Style)",
            "base_profile": "professor_elena_vasquez",
            "style_variant": "Storyteller",
            "description": "Engaging academic narratives",
            "writing_approach": {
                "genre_focus": "Scholarly research and academic discourse",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging academic narratives"
            },
            "specialties": [
                "Academic mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Academic readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused academic development"
        },
        "Craftsperson": {
            "name": "Professor Elena Vasquez (Craftsperson Style)",
            "base_profile": "professor_elena_vasquez",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in scholarly writing",
            "writing_approach": {
                "genre_focus": "Scholarly research and academic discourse",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in scholarly writing"
            },
            "specialties": [
                "Academic mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Academic readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused academic development"
        },
        "Commercial": {
            "name": "Professor Elena Vasquez (Commercial Style)",
            "base_profile": "professor_elena_vasquez",
            "style_variant": "Commercial",
            "description": "Accessible academic writing for broader audiences",
            "writing_approach": {
                "genre_focus": "Scholarly research and academic discourse",
                "style_emphasis": "commercial_approach",
                "target_approach": "accessible academic writing for broader audiences"
            },
            "specialties": [
                "Academic mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Academic readers seeking commercial approach",
            "chapter_approach": "Commercial-focused academic development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Academic writing mastery with scholarly rigor",
        "Innovator": "Fresh academic approaches and methodologies",
        "Storyteller": "Engaging academic narratives",
        "Craftsperson": "Technical excellence in scholarly writing",
        "Commercial": "Accessible academic writing for broader audiences",
    }