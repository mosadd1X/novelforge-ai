"""
Fantasy Genre Recommendations

Provides style variants for fantasy writing, each offering different
approaches to Magical worlds and fantastical elements.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a fantasy profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Professor Aldrich Quantum (Master Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Master",
            "description": "Classic fantasy mastery with rich world-building",
            "writing_approach": {
                "genre_focus": "Magical worlds and fantastical elements",
                "style_emphasis": "master_approach",
                "target_approach": "classic fantasy mastery with rich world-building"
            },
            "specialties": [
                "Fantasy mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Fantasy readers seeking master approach",
            "chapter_approach": "Master-focused fantasy development"
        },
        "Innovator": {
            "name": "Professor Aldrich Quantum (Innovator Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Innovator",
            "description": "Modern fantasy with fresh magical concepts",
            "writing_approach": {
                "genre_focus": "Magical worlds and fantastical elements",
                "style_emphasis": "innovator_approach",
                "target_approach": "modern fantasy with fresh magical concepts"
            },
            "specialties": [
                "Fantasy mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Fantasy readers seeking innovator approach",
            "chapter_approach": "Innovator-focused fantasy development"
        },
        "Storyteller": {
            "name": "Professor Aldrich Quantum (Storyteller Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Storyteller",
            "description": "Engaging fantasy narratives with compelling quests",
            "writing_approach": {
                "genre_focus": "Magical worlds and fantastical elements",
                "style_emphasis": "storyteller_approach",
                "target_approach": "engaging fantasy narratives with compelling quests"
            },
            "specialties": [
                "Fantasy mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Fantasy readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused fantasy development"
        },
        "Craftsperson": {
            "name": "Professor Aldrich Quantum (Craftsperson Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Craftsperson",
            "description": "Technical fantasy excellence with detailed magic systems",
            "writing_approach": {
                "genre_focus": "Magical worlds and fantastical elements",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical fantasy excellence with detailed magic systems"
            },
            "specialties": [
                "Fantasy mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Fantasy readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused fantasy development"
        },
        "Commercial": {
            "name": "Professor Aldrich Quantum (Commercial Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Commercial",
            "description": "Popular fantasy with broad appeal and adventure",
            "writing_approach": {
                "genre_focus": "Magical worlds and fantastical elements",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular fantasy with broad appeal and adventure"
            },
            "specialties": [
                "Fantasy mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Fantasy readers seeking commercial approach",
            "chapter_approach": "Commercial-focused fantasy development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Classic fantasy mastery with rich world-building",
        "Innovator": "Modern fantasy with fresh magical concepts",
        "Storyteller": "Engaging fantasy narratives with compelling quests",
        "Craftsperson": "Technical fantasy excellence with detailed magic systems",
        "Commercial": "Popular fantasy with broad appeal and adventure",
    }