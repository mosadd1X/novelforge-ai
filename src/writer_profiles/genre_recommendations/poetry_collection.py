"""
Poetry Collection Genre Recommendations

Provides style variants for poetry collection writing, each offering different
approaches to Curated collections of poetry.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a poetry collection profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Kavya Nair (Master Style)",
            "base_profile": "kavya_nair",
            "style_variant": "Master",
            "description": "Poetry mastery with literary depth",
            "writing_approach": {
                "genre_focus": "Curated collections of poetry",
                "style_emphasis": "master_approach",
                "target_approach": "poetry mastery with literary depth"
            },
            "specialties": [
                "Poetry Collection mastery",
                "Master approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Poetry Collection readers seeking master approach",
            "chapter_approach": "Master-focused poetry collection development"
        },
        "Innovator": {
            "name": "Kavya Nair (Innovator Style)",
            "base_profile": "kavya_nair",
            "style_variant": "Innovator",
            "description": "Experimental poetry approaches and forms",
            "writing_approach": {
                "genre_focus": "Curated collections of poetry",
                "style_emphasis": "innovator_approach",
                "target_approach": "experimental poetry approaches and forms"
            },
            "specialties": [
                "Poetry Collection mastery",
                "Innovator approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Poetry Collection readers seeking innovator approach",
            "chapter_approach": "Innovator-focused poetry collection development"
        },
        "Storyteller": {
            "name": "Kavya Nair (Storyteller Style)",
            "base_profile": "kavya_nair",
            "style_variant": "Storyteller",
            "description": "Narrative poetry and spoken word",
            "writing_approach": {
                "genre_focus": "Curated collections of poetry",
                "style_emphasis": "storyteller_approach",
                "target_approach": "narrative poetry and spoken word"
            },
            "specialties": [
                "Poetry Collection mastery",
                "Storyteller approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Poetry Collection readers seeking storyteller approach",
            "chapter_approach": "Storyteller-focused poetry collection development"
        },
        "Craftsperson": {
            "name": "Kavya Nair (Craftsperson Style)",
            "base_profile": "kavya_nair",
            "style_variant": "Craftsperson",
            "description": "Technical poetry excellence and craft",
            "writing_approach": {
                "genre_focus": "Curated collections of poetry",
                "style_emphasis": "craftsperson_approach",
                "target_approach": "technical poetry excellence and craft"
            },
            "specialties": [
                "Poetry Collection mastery",
                "Craftsperson approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Poetry Collection readers seeking craftsperson approach",
            "chapter_approach": "Craftsperson-focused poetry collection development"
        },
        "Commercial": {
            "name": "Kavya Nair (Commercial Style)",
            "base_profile": "kavya_nair",
            "style_variant": "Commercial",
            "description": "Accessible poetry with broad appeal",
            "writing_approach": {
                "genre_focus": "Curated collections of poetry",
                "style_emphasis": "commercial_approach",
                "target_approach": "accessible poetry with broad appeal"
            },
            "specialties": [
                "Poetry Collection mastery",
                "Commercial approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "Poetry Collection readers seeking commercial approach",
            "chapter_approach": "Commercial-focused poetry collection development"
        },
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Poetry mastery with literary depth",
        "Innovator": "Experimental poetry approaches and forms",
        "Storyteller": "Narrative poetry and spoken word",
        "Craftsperson": "Technical poetry excellence and craft",
        "Commercial": "Accessible poetry with broad appeal",
    }