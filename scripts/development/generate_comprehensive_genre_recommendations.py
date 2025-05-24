#!/usr/bin/env python3
"""
Comprehensive Genre Recommendations Generator

This script generates all 38 genre recommendation modules with style variants
for the writer profiles system.
"""

import sys
from pathlib import Path
from typing import Dict, Any

# Add src to path
sys.path.append('src')

# All 38 genres with their characteristics
GENRE_CONFIGURATIONS = {
    # Fiction Genres
    "mystery": {
        "base_profile": "detective_marcus_kane",
        "focus": "Investigation, suspense, puzzle-solving",
        "styles": {
            "Master": "Classic detective mastery with logical deduction",
            "Innovator": "Modern mystery with fresh investigative approaches",
            "Storyteller": "Engaging mystery narratives with compelling plots",
            "Craftsperson": "Technical excellence in mystery construction",
            "Commercial": "Popular mystery with broad market appeal"
        }
    },
    "mystery_thriller": {
        "base_profile": "detective_marcus_kane",
        "focus": "Fast-paced investigation with thriller elements",
        "styles": {
            "Master": "Expert blend of mystery and thriller elements",
            "Innovator": "Contemporary thriller-mystery with fresh twists",
            "Storyteller": "Gripping narratives with mystery and suspense",
            "Craftsperson": "Sophisticated thriller-mystery construction",
            "Commercial": "Popular thriller-mystery with mass appeal"
        }
    },
    "thriller": {
        "base_profile": "marcus_steele",
        "focus": "High-stakes suspense and tension",
        "styles": {
            "Master": "Classic thriller mastery with expert pacing",
            "Innovator": "Modern thriller with innovative suspense techniques",
            "Storyteller": "Compelling thriller narratives with strong tension",
            "Craftsperson": "Technical thriller excellence with precise pacing",
            "Commercial": "Popular thriller with broad entertainment value"
        }
    },
    "fantasy": {
        "base_profile": "professor_aldrich_quantum",
        "focus": "Magical worlds and fantastical elements",
        "styles": {
            "Master": "Classic fantasy mastery with rich world-building",
            "Innovator": "Modern fantasy with fresh magical concepts",
            "Storyteller": "Engaging fantasy narratives with compelling quests",
            "Craftsperson": "Technical fantasy excellence with detailed magic systems",
            "Commercial": "Popular fantasy with broad appeal and adventure"
        }
    },
    "epic_fantasy": {
        "base_profile": "professor_aldrich_quantum",
        "focus": "Grand-scale fantasy with complex world-building",
        "styles": {
            "Master": "Epic fantasy mastery with vast, detailed worlds",
            "Innovator": "Modern epic fantasy with innovative scope",
            "Storyteller": "Sweeping epic narratives with grand adventures",
            "Craftsperson": "Technical epic fantasy with complex systems",
            "Commercial": "Popular epic fantasy with mass market appeal"
        }
    },
    "science_fiction": {
        "base_profile": "dr_sophia_chronos",
        "focus": "Futuristic concepts and scientific speculation",
        "styles": {
            "Master": "Classic sci-fi mastery with hard science foundation",
            "Innovator": "Cutting-edge sci-fi with fresh technological concepts",
            "Storyteller": "Engaging sci-fi narratives with human elements",
            "Craftsperson": "Technical sci-fi excellence with scientific accuracy",
            "Commercial": "Popular sci-fi with accessible concepts and adventure"
        }
    },
    "historical_fiction": {
        "base_profile": "dr_patricia_blackwell",
        "focus": "Historical periods with authentic detail",
        "styles": {
            "Master": "Historical fiction mastery with period authenticity",
            "Innovator": "Fresh perspectives on historical periods",
            "Storyteller": "Compelling historical narratives with human drama",
            "Craftsperson": "Technical historical accuracy with literary quality",
            "Commercial": "Popular historical fiction with broad appeal"
        }
    },
    "horror": {
        "base_profile": "sebastian_darkmore",
        "focus": "Fear, suspense, and supernatural elements",
        "styles": {
            "Master": "Classic horror mastery with psychological depth",
            "Innovator": "Modern horror with fresh frightening concepts",
            "Storyteller": "Compelling horror narratives with sustained tension",
            "Craftsperson": "Technical horror excellence with atmospheric mastery",
            "Commercial": "Popular horror with broad entertainment appeal"
        }
    },
    "young_adult": {
        "base_profile": "luna_brightwater",
        "focus": "Coming-of-age themes for teen readers",
        "styles": {
            "Master": "YA mastery with authentic teen voice and themes",
            "Innovator": "Modern YA with fresh perspectives on teen issues",
            "Storyteller": "Engaging YA narratives with compelling character growth",
            "Craftsperson": "Technical YA excellence with sophisticated themes",
            "Commercial": "Popular YA with broad teen and crossover appeal"
        }
    },
    "commercial_fiction": {
        "base_profile": "catherine_fairfax",
        "focus": "Mainstream appeal with engaging storytelling",
        "styles": {
            "Master": "Commercial fiction mastery with broad appeal",
            "Innovator": "Fresh approaches to mainstream storytelling",
            "Storyteller": "Compelling narratives with mass market appeal",
            "Craftsperson": "Technical excellence in accessible storytelling",
            "Commercial": "Optimized for maximum market appeal and readability"
        }
    },
    "contemporary_fiction": {
        "base_profile": "elena_thornfield",
        "focus": "Modern life and contemporary themes",
        "styles": {
            "Master": "Contemporary fiction mastery with modern insights",
            "Innovator": "Fresh perspectives on contemporary life",
            "Storyteller": "Engaging contemporary narratives",
            "Craftsperson": "Technical excellence in modern storytelling",
            "Commercial": "Popular contemporary fiction with broad appeal"
        }
    },
    "paranormal_romance": {
        "base_profile": "raven_nightshade",
        "focus": "Romance with supernatural elements",
        "styles": {
            "Master": "Paranormal romance mastery with supernatural depth",
            "Innovator": "Fresh supernatural romance concepts",
            "Storyteller": "Compelling paranormal love stories",
            "Craftsperson": "Technical excellence in supernatural romance",
            "Commercial": "Popular paranormal romance with mass appeal"
        }
    },
    "urban_fantasy": {
        "base_profile": "zara_blackthorn",
        "focus": "Fantasy in modern urban settings",
        "styles": {
            "Master": "Urban fantasy mastery with city magic",
            "Innovator": "Fresh urban fantasy concepts",
            "Storyteller": "Engaging urban fantasy narratives",
            "Craftsperson": "Technical urban fantasy excellence",
            "Commercial": "Popular urban fantasy with broad appeal"
        }
    },
    "dystopian": {
        "base_profile": "dr_sophia_chronos",
        "focus": "Dark future societies and social commentary",
        "styles": {
            "Master": "Dystopian mastery with social insight",
            "Innovator": "Fresh dystopian concepts and warnings",
            "Storyteller": "Compelling dystopian narratives",
            "Craftsperson": "Technical dystopian excellence",
            "Commercial": "Popular dystopian fiction with broad appeal"
        }
    },
    "speculative_fiction": {
        "base_profile": "dr_sophia_chronos",
        "focus": "Speculative concepts and future possibilities",
        "styles": {
            "Master": "Speculative fiction mastery with deep concepts",
            "Innovator": "Cutting-edge speculative ideas",
            "Storyteller": "Engaging speculative narratives",
            "Craftsperson": "Technical speculative excellence",
            "Commercial": "Accessible speculative fiction"
        }
    },
    "alternate_history": {
        "base_profile": "dr_patricia_blackwell",
        "focus": "Alternative historical timelines",
        "styles": {
            "Master": "Alternate history mastery with historical depth",
            "Innovator": "Fresh alternate history concepts",
            "Storyteller": "Compelling alternate history narratives",
            "Craftsperson": "Technical alternate history excellence",
            "Commercial": "Popular alternate history with broad appeal"
        }
    },
    # Additional Fiction Genres
    "middle_grade": {
        "base_profile": "luna_brightwater",
        "focus": "Stories for middle-grade readers (ages 8-12)",
        "styles": {
            "Master": "Middle grade mastery with age-appropriate depth",
            "Innovator": "Fresh approaches to middle grade storytelling",
            "Storyteller": "Engaging narratives for young readers",
            "Craftsperson": "Technical excellence in children's literature",
            "Commercial": "Popular middle grade with broad appeal"
        }
    },
    "children_s_chapter_books": {
        "base_profile": "luna_brightwater",
        "focus": "Chapter books for early readers",
        "styles": {
            "Master": "Children's literature mastery with educational value",
            "Innovator": "Fresh approaches to early reader engagement",
            "Storyteller": "Compelling stories for developing readers",
            "Craftsperson": "Technical excellence in age-appropriate writing",
            "Commercial": "Popular children's books with broad appeal"
        }
    },
    "short_story_collection": {
        "base_profile": "elena_thornfield",
        "focus": "Curated collections of short fiction",
        "styles": {
            "Master": "Short story mastery with thematic coherence",
            "Innovator": "Experimental short fiction approaches",
            "Storyteller": "Compelling short narratives",
            "Craftsperson": "Technical short story excellence",
            "Commercial": "Accessible short story collections"
        }
    },
    "novella": {
        "base_profile": "elena_thornfield",
        "focus": "Extended short fiction with focused narrative",
        "styles": {
            "Master": "Novella mastery with concentrated storytelling",
            "Innovator": "Fresh novella formats and approaches",
            "Storyteller": "Compelling medium-length narratives",
            "Craftsperson": "Technical novella excellence",
            "Commercial": "Popular novellas with broad appeal"
        }
    },
    "graphic_novel": {
        "base_profile": "hiroshi_nakamura",
        "focus": "Visual storytelling with sequential art",
        "styles": {
            "Master": "Graphic novel mastery with visual narrative",
            "Innovator": "Fresh graphic storytelling techniques",
            "Storyteller": "Compelling visual narratives",
            "Craftsperson": "Technical graphic novel excellence",
            "Commercial": "Popular graphic novels with mass appeal"
        }
    },
    # Non-Fiction Genres
    "memoir": {
        "base_profile": "grace_washington",
        "focus": "Personal life stories and experiences",
        "styles": {
            "Master": "Memoir mastery with authentic personal narrative",
            "Innovator": "Fresh approaches to personal storytelling",
            "Storyteller": "Compelling personal narratives",
            "Craftsperson": "Technical excellence in memoir writing",
            "Commercial": "Popular memoir with broad appeal"
        }
    },
    "biography": {
        "base_profile": "dr_patricia_blackwell",
        "focus": "Life stories of notable individuals",
        "styles": {
            "Master": "Biography mastery with comprehensive research",
            "Innovator": "Fresh biographical approaches and perspectives",
            "Storyteller": "Compelling biographical narratives",
            "Craftsperson": "Technical excellence in biographical writing",
            "Commercial": "Popular biography with mass appeal"
        }
    },
    "history": {
        "base_profile": "dr_patricia_blackwell",
        "focus": "Historical events and analysis",
        "styles": {
            "Master": "Historical writing mastery with scholarly depth",
            "Innovator": "Fresh historical perspectives and analysis",
            "Storyteller": "Engaging historical narratives",
            "Craftsperson": "Technical excellence in historical writing",
            "Commercial": "Accessible history with broad appeal"
        }
    },
    "self_help": {
        "base_profile": "dr_malcolm_sterling",
        "focus": "Personal development and improvement",
        "styles": {
            "Master": "Self-help mastery with proven methodologies",
            "Innovator": "Fresh approaches to personal development",
            "Storyteller": "Engaging self-improvement narratives",
            "Craftsperson": "Technical excellence in instructional writing",
            "Commercial": "Popular self-help with mass market appeal"
        }
    },
    "business": {
        "base_profile": "rajesh_malhotra",
        "focus": "Business strategy and professional development",
        "styles": {
            "Master": "Business writing mastery with strategic insight",
            "Innovator": "Fresh business concepts and approaches",
            "Storyteller": "Engaging business narratives and case studies",
            "Craftsperson": "Technical excellence in business writing",
            "Commercial": "Popular business books with broad appeal"
        }
    },
    "popular_science": {
        "base_profile": "dr_samuel_voss",
        "focus": "Scientific concepts for general audiences",
        "styles": {
            "Master": "Science writing mastery with clear explanation",
            "Innovator": "Fresh approaches to science communication",
            "Storyteller": "Engaging scientific narratives",
            "Craftsperson": "Technical excellence in science writing",
            "Commercial": "Accessible science with mass appeal"
        }
    },
    "academic": {
        "base_profile": "professor_elena_vasquez",
        "focus": "Scholarly research and academic discourse",
        "styles": {
            "Master": "Academic writing mastery with scholarly rigor",
            "Innovator": "Fresh academic approaches and methodologies",
            "Storyteller": "Engaging academic narratives",
            "Craftsperson": "Technical excellence in scholarly writing",
            "Commercial": "Accessible academic writing for broader audiences"
        }
    },
    "travel": {
        "base_profile": "gabriel_montoya",
        "focus": "Travel experiences and destination guides",
        "styles": {
            "Master": "Travel writing mastery with cultural insight",
            "Innovator": "Fresh travel perspectives and approaches",
            "Storyteller": "Engaging travel narratives and adventures",
            "Craftsperson": "Technical excellence in travel writing",
            "Commercial": "Popular travel guides with mass appeal"
        }
    },
    "cookbook": {
        "base_profile": "ananya_desai",
        "focus": "Culinary recipes and food culture",
        "styles": {
            "Master": "Cookbook mastery with culinary expertise",
            "Innovator": "Fresh culinary approaches and techniques",
            "Storyteller": "Engaging food narratives and stories",
            "Craftsperson": "Technical excellence in recipe writing",
            "Commercial": "Popular cookbooks with broad appeal"
        }
    },
    "how_to": {
        "base_profile": "dr_malcolm_sterling",
        "focus": "Instructional guides and skill development",
        "styles": {
            "Master": "How-to mastery with clear instruction",
            "Innovator": "Fresh instructional approaches and methods",
            "Storyteller": "Engaging instructional narratives",
            "Craftsperson": "Technical excellence in instructional writing",
            "Commercial": "Popular how-to guides with mass appeal"
        }
    },
    "essay_collection": {
        "base_profile": "elena_thornfield",
        "focus": "Curated collections of essays and commentary",
        "styles": {
            "Master": "Essay mastery with intellectual depth",
            "Innovator": "Fresh essay approaches and perspectives",
            "Storyteller": "Engaging essay narratives",
            "Craftsperson": "Technical excellence in essay writing",
            "Commercial": "Accessible essay collections"
        }
    },
    "philosophy": {
        "base_profile": "professor_elena_vasquez",
        "focus": "Philosophical inquiry and thought",
        "styles": {
            "Master": "Philosophy mastery with rigorous analysis",
            "Innovator": "Fresh philosophical approaches and questions",
            "Storyteller": "Engaging philosophical narratives",
            "Craftsperson": "Technical excellence in philosophical writing",
            "Commercial": "Accessible philosophy for general readers"
        }
    },
    "true_crime": {
        "base_profile": "detective_marcus_kane",
        "focus": "Real criminal cases and investigations",
        "styles": {
            "Master": "True crime mastery with investigative depth",
            "Innovator": "Fresh true crime approaches and perspectives",
            "Storyteller": "Compelling true crime narratives",
            "Craftsperson": "Technical excellence in crime reporting",
            "Commercial": "Popular true crime with mass appeal"
        }
    },
    "poetry_collection": {
        "base_profile": "kavya_nair",
        "focus": "Curated collections of poetry",
        "styles": {
            "Master": "Poetry mastery with literary depth",
            "Innovator": "Experimental poetry approaches and forms",
            "Storyteller": "Narrative poetry and spoken word",
            "Craftsperson": "Technical poetry excellence and craft",
            "Commercial": "Accessible poetry with broad appeal"
        }
    },
    "creative_non_fiction": {
        "base_profile": "elena_thornfield",
        "focus": "Literary non-fiction with creative elements",
        "styles": {
            "Master": "Creative non-fiction mastery with literary quality",
            "Innovator": "Fresh creative non-fiction approaches",
            "Storyteller": "Engaging creative non-fiction narratives",
            "Craftsperson": "Technical excellence in creative non-fiction",
            "Commercial": "Accessible creative non-fiction"
        }
    }
}

def generate_genre_module(genre_key: str, config: Dict[str, Any]) -> str:
    """Generate a complete genre recommendation module."""

    genre_display = genre_key.replace("_", " ").title()

    module_content = f'''"""
{genre_display} Genre Recommendations

Provides style variants for {genre_key.replace("_", " ")} writing, each offering different
approaches to {config["focus"]}.
"""

from typing import Dict, Any, Optional, List

def get_profile_by_style(style: str) -> Optional[Dict[str, Any]]:
    """
    Get a {genre_key.replace("_", " ")} profile variant by style.

    Args:
        style: Style variant (Master, Innovator, Storyteller, Craftsperson, Commercial)

    Returns:
        Profile data optimized for the specified style
    """
    profiles = {{'''

    for style, description in config["styles"].items():
        module_content += f'''
        "{style}": {{
            "name": "{config['base_profile'].replace('_', ' ').title()} ({style} Style)",
            "base_profile": "{config['base_profile']}",
            "style_variant": "{style}",
            "description": "{description}",
            "writing_approach": {{
                "genre_focus": "{config['focus']}",
                "style_emphasis": "{style.lower()}_approach",
                "target_approach": "{description.lower()}"
            }},
            "specialties": [
                "{genre_display} mastery",
                "{style} approach techniques",
                "Genre-specific expertise",
                "Style-optimized methods"
            ],
            "target_audience": "{genre_display} readers seeking {style.lower()} approach",
            "chapter_approach": "{style}-focused {genre_key.replace('_', ' ')} development"
        }},'''

    module_content += '''
    }

    return profiles.get(style)

def get_available_styles() -> List[str]:
    """Get list of available style variants."""
    return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

def get_style_descriptions() -> Dict[str, str]:
    """Get descriptions of each style variant."""
    return {'''

    for style, description in config["styles"].items():
        module_content += f'''
        "{style}": "{description}",'''

    module_content += '''
    }'''

    return module_content

def main():
    """Generate all genre recommendation modules."""

    # Create output directory
    output_dir = Path("src/writer_profiles/genre_recommendations")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("🚀 Generating comprehensive genre recommendations...")

    # Generate modules for configured genres
    for genre_key, config in GENRE_CONFIGURATIONS.items():
        module_path = output_dir / f"{genre_key}.py"
        module_content = generate_genre_module(genre_key, config)

        with open(module_path, 'w', encoding='utf-8') as f:
            f.write(module_content)

        print(f"✅ Generated {genre_key}.py")

    print(f"\n🎉 Generated {len(GENRE_CONFIGURATIONS)} genre recommendation modules!")
    print("📁 Location: src/writer_profiles/genre_recommendations/")

if __name__ == "__main__":
    main()
