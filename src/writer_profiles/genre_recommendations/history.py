"""
History Genre Recommendations

Provides style variants for history writing, each offering different
approaches to Historical events and analysis.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a history profile variant by style.

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
            "description": "Historical writing mastery with scholarly depth",
            "writing_approach": {
                "genre_focus": "Historical events and analysis",
                "style_emphasis": "master_approach",
                "target_approach": "historical writing mastery with scholarly depth"
            },
            "specialties": [
                "History mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "History readers seeking master approach",
            "chapter_approach": "Master-focused history development"
        },
        "Innovator": {
            "name": "Dr Patricia Blackwell (Innovator Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Innovator",
            "description": "Fresh historical perspectives and analysis",
            "writing_approach": {
                "genre_focus": "Historical events and analysis",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh historical perspectives and analysis"
            },
            "specialties": [
                "History mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "History readers seeking innovator approach",
            "chapter_approach": "Innovator-focused history development"
        },
        "Storyteller": {
            "name": "Dr Patricia Blackwell (Storyteller Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Storyteller",
            "description": "Engaging historical narratives",
            "writing_approach": {
                "genre_focus": "Historical events and analysis",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging historical narratives"
            },
            "specialties": [
                "History mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "History readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused history development"
        },
        "Craftsperson": {
            "name": "Dr Patricia Blackwell (Craftsperson Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in historical writing",
            "writing_approach": {
                "genre_focus": "Historical events and analysis",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in historical writing"
            },
            "specialties": [
                "History mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "History readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused history development"
        },
        "Commercial": {
            "name": "Dr Patricia Blackwell (Commercial Style)",
            "base_profile": "dr_patricia_blackwell",
            "style_variant": "Commercial",
            "description": "Accessible history with broad appeal",
            "writing_approach": {
                "genre_focus": "Historical events and analysis",
                "style_emphasis": "commercial_approach",
                "target_approach": "accessible history with broad appeal"
            },
            "specialties": [
                "History mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "History readers seeking commercial approach",
            "chapter_approach": "Commercial-focused history development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Historical writing mastery with scholarly depth",
        "Innovator": "Fresh historical perspectives and analysis",
        "Storyteller": "Engaging historical narratives",
        "Craftsperson": "Technical excellence in historical writing",
        "Commercial": "Accessible history with broad appeal",
    }