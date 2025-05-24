"""
Business Genre Recommendations

Provides style variants for business writing, each offering different
approaches to Business strategy and professional development.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a business profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Rajesh Malhotra (Master Style)",
            "base_profile": "rajesh_malhotra",
            "style_variant": "Master",
            "description": "Business writing mastery with strategic insight",
            "writing_approach": {
                "genre_focus": "Business strategy and professional development",
                "style_emphasis": "master_approach",
                "target_approach": "business writing mastery with strategic insight"
            },
            "specialties": [
                "Business mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Business readers seeking master approach",
            "chapter_approach": "Master-focused business development"
        },
        "Innovator": {
            "name": "Rajesh Malhotra (Innovator Style)",
            "base_profile": "rajesh_malhotra",
            "style_variant": "Innovator",
            "description": "Fresh business concepts and approaches",
            "writing_approach": {
                "genre_focus": "Business strategy and professional development",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh business concepts and approaches"
            },
            "specialties": [
                "Business mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Business readers seeking innovator approach",
            "chapter_approach": "Innovator-focused business development"
        },
        "Storyteller": {
            "name": "Rajesh Malhotra (Storyteller Style)",
            "base_profile": "rajesh_malhotra",
            "style_variant": "Storyteller",
            "description": "Engaging business narratives and case studies",
            "writing_approach": {
                "genre_focus": "Business strategy and professional development",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging business narratives and case studies"
            },
            "specialties": [
                "Business mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Business readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused business development"
        },
        "Craftsperson": {
            "name": "Rajesh Malhotra (Craftsperson Style)",
            "base_profile": "rajesh_malhotra",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in business writing",
            "writing_approach": {
                "genre_focus": "Business strategy and professional development",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in business writing"
            },
            "specialties": [
                "Business mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Business readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused business development"
        },
        "Commercial": {
            "name": "Rajesh Malhotra (Commercial Style)",
            "base_profile": "rajesh_malhotra",
            "style_variant": "Commercial",
            "description": "Popular business books with broad appeal",
            "writing_approach": {
                "genre_focus": "Business strategy and professional development",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular business books with broad appeal"
            },
            "specialties": [
                "Business mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Business readers seeking commercial approach",
            "chapter_approach": "Commercial-focused business development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Business writing mastery with strategic insight",
        "Innovator": "Fresh business concepts and approaches",
        "Storyteller": "Engaging business narratives and case studies",
        "Craftsperson": "Technical excellence in business writing",
        "Commercial": "Popular business books with broad appeal",
    }