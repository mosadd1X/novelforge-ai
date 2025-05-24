"""
Epic Fantasy Genre Recommendations

Provides style variants for epic fantasy writing, each offering different
approaches to Grand-scale fantasy with complex world-building.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a epic fantasy profile variant by style.

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
            "description": "Epic fantasy mastery with vast, detailed worlds",
            "writing_approach": {
                "genre_focus": "Grand-scale fantasy with complex world-building",
                "style_emphasis": "master_approach",
                "target_approach": "epic fantasy mastery with vast, detailed worlds"
            },
            "specialties": [
                "Epic Fantasy mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Epic Fantasy readers seeking master approach",
            "chapter_approach": "Master-focused epic fantasy development"
        },
        "Innovator": {
            "name": "Professor Aldrich Quantum (Innovator Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Innovator",
            "description": "Modern epic fantasy with innovative scope",
            "writing_approach": {
                "genre_focus": "Grand-scale fantasy with complex world-building",
                "style_emphasis": "innovator_approach",
                "target_approach": "modern epic fantasy with innovative scope"
            },
            "specialties": [
                "Epic Fantasy mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Epic Fantasy readers seeking innovator approach",
            "chapter_approach": "Innovator-focused epic fantasy development"
        },
        "Storyteller": {
            "name": "Professor Aldrich Quantum (Storyteller Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Storyteller",
            "description": "Sweeping epic narratives with grand adventures",
            "writing_approach": {
                "genre_focus": "Grand-scale fantasy with complex world-building",
                "style_emphasis": "storyteller_approach",
                "target_approach": "sweeping epic narratives with grand adventures"
            },
            "specialties": [
                "Epic Fantasy mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Epic Fantasy readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused epic fantasy development"
        },
        "Craftsperson": {
            "name": "Professor Aldrich Quantum (Craftsperson Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Craftsperson",
            "description": "Technical epic fantasy with complex systems",
            "writing_approach": {
                "genre_focus": "Grand-scale fantasy with complex world-building",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical epic fantasy with complex systems"
            },
            "specialties": [
                "Epic Fantasy mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Epic Fantasy readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused epic fantasy development"
        },
        "Commercial": {
            "name": "Professor Aldrich Quantum (Commercial Style)",
            "base_profile": "professor_aldrich_quantum",
            "style_variant": "Commercial",
            "description": "Popular epic fantasy with mass market appeal",
            "writing_approach": {
                "genre_focus": "Grand-scale fantasy with complex world-building",
                "style_emphasis": "commercial_approach",
                "target_approach": "popular epic fantasy with mass market appeal"
            },
            "specialties": [
                "Epic Fantasy mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Epic Fantasy readers seeking commercial approach",
            "chapter_approach": "Commercial-focused epic fantasy development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Epic fantasy mastery with vast, detailed worlds",
        "Innovator": "Modern epic fantasy with innovative scope",
        "Storyteller": "Sweeping epic narratives with grand adventures",
        "Craftsperson": "Technical epic fantasy with complex systems",
        "Commercial": "Popular epic fantasy with mass market appeal",
    }