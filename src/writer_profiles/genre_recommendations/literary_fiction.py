"""
Literary Fiction Genre Recommendations

Provides style variants for literary fiction writing, each offering different
approaches to character development, narrative structure, and thematic exploration.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a literary fiction profile variant by style.
    
    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)
        
    Returns:
        Profile data optimized for the specified style
    """
    profiles = {
        "Master": {
            "name": "Elena Thornfield (Master Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Master",
            "description": "Established literary mastery with psychological depth and experimental techniques",
            "writing_approach": {
                "narrative_style": "Stream of consciousness with psychological realism",
                "character_focus": "Deep psychological exploration and interior monologue",
                "thematic_emphasis": "Universal human experiences and existential questions",
                "prose_style": "Lyrical, introspective, with complex sentence structures",
                "pacing": "Deliberate, contemplative, allowing for reflection"
            },
            "specialties": [
                "Psychological character studies",
                "Experimental narrative techniques",
                "Philosophical themes",
                "Complex temporal structures",
                "Unreliable narrators"
            ],
            "target_audience": "Literary readers seeking intellectual and emotional depth",
            "chapter_approach": "Character-driven with emphasis on internal conflict and growth"
        },
        
        "Innovator": {
            "name": "Elena Thornfield (Innovator Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Innovator",
            "description": "Experimental literary approach pushing boundaries of form and narrative",
            "writing_approach": {
                "narrative_style": "Non-linear, fragmented, multi-perspective",
                "character_focus": "Deconstructed identity and fluid consciousness",
                "thematic_emphasis": "Postmodern concerns and meta-fictional elements",
                "prose_style": "Experimental, genre-blending, unconventional structure",
                "pacing": "Variable, deliberately disruptive of expectations"
            },
            "specialties": [
                "Meta-fictional techniques",
                "Genre-blending narratives",
                "Unconventional structures",
                "Postmodern themes",
                "Experimental prose forms"
            ],
            "target_audience": "Avant-garde readers open to experimental literature",
            "chapter_approach": "Non-traditional structure with experimental narrative techniques"
        },
        
        "Storyteller": {
            "name": "Elena Thornfield (Storyteller Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Storyteller",
            "description": "Narrative-focused literary fiction with compelling character arcs",
            "writing_approach": {
                "narrative_style": "Clear, engaging storytelling with literary depth",
                "character_focus": "Relatable characters with universal struggles",
                "thematic_emphasis": "Human connections and transformative experiences",
                "prose_style": "Accessible yet sophisticated, emotionally resonant",
                "pacing": "Balanced between reflection and forward momentum"
            },
            "specialties": [
                "Character-driven narratives",
                "Emotional storytelling",
                "Universal themes",
                "Accessible literary style",
                "Compelling plot development"
            ],
            "target_audience": "General literary readers seeking engaging stories with depth",
            "chapter_approach": "Story-driven with strong character development and clear progression"
        },
        
        "Craftsperson": {
            "name": "Elena Thornfield (Craftsperson Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Craftsperson",
            "description": "Technical literary excellence with meticulous attention to craft",
            "writing_approach": {
                "narrative_style": "Precisely crafted with attention to every detail",
                "character_focus": "Carefully constructed character psychology",
                "thematic_emphasis": "Subtle, layered themes requiring careful reading",
                "prose_style": "Polished, precise, with careful word choice and rhythm",
                "pacing": "Controlled, with deliberate build-up and resolution"
            },
            "specialties": [
                "Precise prose craftsmanship",
                "Subtle thematic development",
                "Technical narrative mastery",
                "Layered symbolism",
                "Careful structural design"
            ],
            "target_audience": "Discerning readers who appreciate literary craftsmanship",
            "chapter_approach": "Meticulously crafted with attention to structure and literary devices"
        },
        
        "Commercial": {
            "name": "Elena Thornfield (Commercial Style)",
            "base_profile": "elena_thornfield",
            "style_variant": "Commercial",
            "description": "Literary fiction with broader appeal and accessible themes",
            "writing_approach": {
                "narrative_style": "Engaging storytelling with literary quality",
                "character_focus": "Relatable characters with clear motivations",
                "thematic_emphasis": "Universal themes with contemporary relevance",
                "prose_style": "Sophisticated yet accessible, emotionally engaging",
                "pacing": "Reader-friendly with good momentum and clear structure"
            },
            "specialties": [
                "Accessible literary fiction",
                "Contemporary themes",
                "Broad appeal narratives",
                "Clear character arcs",
                "Engaging plot development"
            ],
            "target_audience": "Mainstream readers seeking quality literary fiction",
            "chapter_approach": "Reader-friendly structure with literary depth and commercial appeal"
        }
    }
    
    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants for literary fiction."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {
        "Master": "Established literary mastery with psychological depth",
        "Innovator": "Experimental approach pushing narrative boundaries",
        "Storyteller": "Narrative-focused with compelling character arcs",
        "Craftsperson": "Technical excellence with meticulous attention to craft",
        "Commercial": "Literary quality with broader market appeal"
    }
