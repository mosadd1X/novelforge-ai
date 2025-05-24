"""
Science Fiction Genre Recommendations

Provides style variants for science fiction writing, each offering different
approaches to Futuristic concepts and scientific speculation.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a science fiction profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Dr Sophia Chronos (Master Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Master",
            "description": "Classic sci-fi mastery with hard science foundation",
            "writing_approach": {
                "genre_focus": "Futuristic concepts and scientific speculation",
                "style_emphasis": "master_approach",
                "target_approach": "classic sci-fi mastery with hard science foundation"
            },
            "specialties": [
                "Science Fiction mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Science Fiction readers seeking master approach",
            "chapter_approach": "Master-focused science fiction development"
        },
        "Innovator": {
            "name": "Dr Sophia Chronos (Innovator Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Innovator",
            "description": "Cutting-edge sci-fi with fresh technological concepts",
            "writing_approach": {
                "genre_focus": "Futuristic concepts and scientific speculation",
                "style_emphasis": "innovator_approach",
                "target_approach": "cutting-edge sci-fi with fresh technological concepts"
            },
            "specialties": [
                "Science Fiction mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Science Fiction readers seeking innovator approach",
            "chapter_approach": "Innovator-focused science fiction development"
        },
        "Storyteller": {
            "name": "Dr Sophia Chronos (Storyteller Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Storyteller",
            "description": "Engaging sci-fi narratives with human elements",
            "writing_approach": {
                "genre_focus": "Futuristic concepts and scientific speculation",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging sci-fi narratives with human elements"
            },
            "specialties": [
                "Science Fiction mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Science Fiction readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused science fiction development"
        },
        "Craftsperson": {
            "name": "Dr Sophia Chronos (Craftsperson Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Craftsperson",
            "description": "Technical sci-fi excellence with scientific accuracy",
            "writing_approach": {
                "genre_focus": "Futuristic concepts and scientific speculation",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical sci-fi excellence with scientific accuracy"
            },
            "specialties": [
                "Science Fiction mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Science Fiction readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused science fiction development"
        },
        "Commercial": {
            "name": "Dr Sophia Chronos (Commercial Style)",
            "base_profile": "dr_sophia_chronos",
            "style_variant": "Commercial",
            "description": "Popular sci-fi with accessible concepts and adventure",
            "writing_approach": {
                "genre_focus": "Futuristic concepts and scientific speculation",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular sci-fi with accessible concepts and adventure"
            },
            "specialties": [
                "Science Fiction mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Science Fiction readers seeking commercial approach",
            "chapter_approach": "Commercial-focused science fiction development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Classic sci-fi mastery with hard science foundation",
        "Innovator": "Cutting-edge sci-fi with fresh technological concepts",
        "Storyteller": "Engaging sci-fi narratives with human elements",
        "Craftsperson": "Technical sci-fi excellence with scientific accuracy",
        "Commercial": "Popular sci-fi with accessible concepts and adventure",
    }