"""
How To Genre Recommendations

Provides style variants for how to writing, each offering different
approaches to Instructional guides and skill development.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a how to profile variant by style.

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
            "description": "How-to mastery with clear instruction",
            "writing_approach": {
                "genre_focus": "Instructional guides and skill development",
                "style_emphasis": "master_approach",
                "target_approach": "how-to mastery with clear instruction"
            },
            "specialties": [
                "How To mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "How To readers seeking master approach",
            "chapter_approach": "Master-focused how to development"
        },
        "Innovator": {
            "name": "Dr Malcolm Sterling (Innovator Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Innovator",
            "description": "Fresh instructional approaches and methods",
            "writing_approach": {
                "genre_focus": "Instructional guides and skill development",
                "style_emphasis": "innovator_approach",
                "target_approach": "fresh instructional approaches and methods"
            },
            "specialties": [
                "How To mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "How To readers seeking innovator approach",
            "chapter_approach": "Innovator-focused how to development"
        },
        "Storyteller": {
            "name": "Dr Malcolm Sterling (Storyteller Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Storyteller",
            "description": "Engaging instructional narratives",
            "writing_approach": {
                "genre_focus": "Instructional guides and skill development",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging instructional narratives"
            },
            "specialties": [
                "How To mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "How To readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused how to development"
        },
        "Craftsperson": {
            "name": "Dr Malcolm Sterling (Craftsperson Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Craftsperson",
            "description": "Technical excellence in instructional writing",
            "writing_approach": {
                "genre_focus": "Instructional guides and skill development",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical excellence in instructional writing"
            },
            "specialties": [
                "How To mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "How To readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused how to development"
        },
        "Commercial": {
            "name": "Dr Malcolm Sterling (Commercial Style)",
            "base_profile": "dr_malcolm_sterling",
            "style_variant": "Commercial",
            "description": "Popular how-to guides with mass appeal",
            "writing_approach": {
                "genre_focus": "Instructional guides and skill development",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular how-to guides with mass appeal"
            },
            "specialties": [
                "How To mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "How To readers seeking commercial approach",
            "chapter_approach": "Commercial-focused how to development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "How-to mastery with clear instruction",
        "Innovator": "Fresh instructional approaches and methods",
        "Storyteller": "Engaging instructional narratives",
        "Craftsperson": "Technical excellence in instructional writing",
        "Commercial": "Popular how-to guides with mass appeal",
    }