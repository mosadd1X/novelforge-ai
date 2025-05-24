"""
Cookbook Genre Recommendations

Provides style variants for cookbook writing, each offering different
approaches to Culinary recipes and food culture.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a cookbook profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Ananya Desai (Master Style)",
            "base_profile": "ananya_desai",
            "style_variant": "Master",
            "description": "Cookbook mastery with culinary expertise",
            "writing_approach": {
                "genre_focus": "Culinary recipes and food culture",
                "style_emphasis": "master_approach",
                "target_approach": "cookbook mastery with culinary expertise"
            },
            "specialties": [
                "Cookbook mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Cookbook readers seeking master approach",
            "chapter_approach": "Master-focused cookbook development"
        },
        "Innovator": {
            "name": "Ananya Desai (Innovator Style)",
            "base_profile": "ananya_desai",
            "style_variant": "Innovator",
            "description": "Fresh culinary approaches and techniques",
            "writing_approach": {
                "genre_focus": "Culinary recipes and food culture",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh culinary approaches and techniques"
            },
            "specialties": [
                "Cookbook mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Cookbook readers seeking innovator approach",
            "chapter_approach": "Innovator-focused cookbook development"
        },
        "Storyteller": {
            "name": "Ananya Desai (Storyteller Style)",
            "base_profile": "ananya_desai",
            "style_variant": "Storyteller",
            "description": "Engaging food narratives and stories",
            "writing_approach": {
                "genre_focus": "Culinary recipes and food culture",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging food narratives and stories"
            },
            "specialties": [
                "Cookbook mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Cookbook readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused cookbook development"
        },
        "Craftsperson": {
            "name": "Ananya Desai (Craftsperson Style)",
            "base_profile": "ananya_desai",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in recipe writing",
            "writing_approach": {
                "genre_focus": "Culinary recipes and food culture",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in recipe writing"
            },
            "specialties": [
                "Cookbook mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Cookbook readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused cookbook development"
        },
        "Commercial": {
            "name": "Ananya Desai (Commercial Style)",
            "base_profile": "ananya_desai",
            "style_variant": "Commercial",
            "description": "Popular cookbooks with broad appeal",
            "writing_approach": {
                "genre_focus": "Culinary recipes and food culture",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular cookbooks with broad appeal"
            },
            "specialties": [
                "Cookbook mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Cookbook readers seeking commercial approach",
            "chapter_approach": "Commercial-focused cookbook development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Cookbook mastery with culinary expertise",
        "Innovator": "Fresh culinary approaches and techniques",
        "Storyteller": "Engaging food narratives and stories",
        "Craftsperson": "Technical excellence in recipe writing",
        "Commercial": "Popular cookbooks with broad appeal",
    }