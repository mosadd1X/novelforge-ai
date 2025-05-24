#!/usr/bin/env python3
"""
Recommended Collections Generator

This script generates comprehensive curated profile collections for the
writer profiles recommendation system.
"""

import sys
import json
from pathlib import Path
from typing import Dict, Any, List

# Add src to path
sys.path.append('src')

# Collection configurations
COLLECTION_CONFIGS = {
    "genre_specialists": {
        "name": "Genre Specialists",
        "description": "Master authors who excel in specific genres with deep expertise and authentic voice",
        "category": "Genre-Specific",
        "target_audience": "Authors seeking genre mastery and authentic voice",
        "profiles": [
            {
                "profile_id": "professor_aldrich_quantum",
                "name": "Professor Aldrich Quantum",
                "priority": 1,
                "genres": ["Fantasy", "Epic Fantasy", "Middle Grade"],
                "specialization": "Fantasy world-building and mythological storytelling"
            },
            {
                "profile_id": "dr_sophia_chronos",
                "name": "Dr. Sophia Chronos",
                "priority": 2,
                "genres": ["Science Fiction", "Speculative Fiction", "Dystopian"],
                "specialization": "Hard science fiction and temporal narratives"
            },
            {
                "profile_id": "sebastian_darkmore",
                "name": "Sebastian Darkmore",
                "priority": 3,
                "genres": ["Horror", "Gothic Fiction", "Dark Fantasy"],
                "specialization": "Psychological horror and atmospheric storytelling"
            },
            {
                "profile_id": "raven_nightshade",
                "name": "Raven Nightshade",
                "priority": 4,
                "genres": ["Paranormal Romance", "Urban Fantasy", "Dark Romance"],
                "specialization": "Supernatural romance and dark fantasy elements"
            },
            {
                "profile_id": "zara_blackthorn",
                "name": "Zara Blackthorn",
                "priority": 5,
                "genres": ["Urban Fantasy", "Contemporary Fantasy", "Supernatural Fiction"],
                "specialization": "Modern fantasy and supernatural urban settings"
            }
        ]
    },
    
    "debut_authors": {
        "name": "Debut Author Success",
        "description": "Profiles optimized for first-time authors with accessible approaches and proven debut strategies",
        "category": "Experience-Based",
        "target_audience": "First-time authors and debut novelists",
        "profiles": [
            {
                "profile_id": "luna_brightwater",
                "name": "Luna Brightwater",
                "priority": 1,
                "genres": ["Young Adult", "Middle Grade", "Coming-of-Age"],
                "debut_strengths": ["Clear voice", "Accessible storytelling", "Strong character development"]
            },
            {
                "profile_id": "catherine_fairfax",
                "name": "Catherine Fairfax",
                "priority": 2,
                "genres": ["Commercial Fiction", "Contemporary Fiction", "Women's Fiction"],
                "debut_strengths": ["Market awareness", "Broad appeal", "Professional approach"]
            },
            {
                "profile_id": "gabriel_montoya",
                "name": "Gabriel Montoya",
                "priority": 3,
                "genres": ["Travel", "Adventure", "Cultural Fiction"],
                "debut_strengths": ["Authentic voice", "Cultural insight", "Engaging narrative"]
            }
        ]
    },
    
    "innovative_voices": {
        "name": "Innovative Voices",
        "description": "Authors pushing boundaries with experimental techniques and fresh perspectives",
        "category": "Literary-Focused",
        "target_audience": "Authors seeking innovation and experimental approaches",
        "profiles": [
            {
                "profile_id": "elena_thornfield",
                "name": "Elena Thornfield",
                "priority": 1,
                "genres": ["Literary Fiction", "Experimental Fiction", "Stream of Consciousness"],
                "innovation_focus": ["Narrative experimentation", "Psychological realism", "Modernist techniques"]
            },
            {
                "profile_id": "hiroshi_nakamura",
                "name": "Hiroshi Nakamura",
                "priority": 2,
                "genres": ["Graphic Novel", "Visual Storytelling", "Multimedia Narrative"],
                "innovation_focus": ["Visual narrative", "Format innovation", "Cultural fusion"]
            },
            {
                "profile_id": "kavya_nair",
                "name": "Kavya Nair",
                "priority": 3,
                "genres": ["Poetry Collection", "Prose Poetry", "Lyrical Fiction"],
                "innovation_focus": ["Poetic narrative", "Cultural voice", "Lyrical innovation"]
            }
        ]
    },
    
    "international_voices": {
        "name": "International Voices",
        "description": "Diverse cultural perspectives and authentic international storytelling",
        "category": "Cultural-Diverse",
        "target_audience": "Authors seeking cultural authenticity and diverse perspectives",
        "profiles": [
            {
                "profile_id": "priya_sharma",
                "name": "Priya Sharma",
                "priority": 1,
                "genres": ["Contemporary Romance", "Cultural Fiction", "Family Drama"],
                "cultural_focus": "Indian culture and contemporary relationships"
            },
            {
                "profile_id": "hiroshi_nakamura",
                "name": "Hiroshi Nakamura",
                "priority": 2,
                "genres": ["Graphic Novel", "Cultural Narrative", "Visual Storytelling"],
                "cultural_focus": "Japanese culture and visual storytelling traditions"
            },
            {
                "profile_id": "gabriel_montoya",
                "name": "Gabriel Montoya",
                "priority": 3,
                "genres": ["Travel", "Cultural Exploration", "Adventure"],
                "cultural_focus": "Latin American culture and travel narratives"
            },
            {
                "profile_id": "ananya_desai",
                "name": "Ananya Desai",
                "priority": 4,
                "genres": ["Cookbook", "Cultural Food", "Culinary Memoir"],
                "cultural_focus": "Indian culinary traditions and food culture"
            }
        ]
    },
    
    "non_fiction_experts": {
        "name": "Non-Fiction Experts",
        "description": "Specialists in various non-fiction genres with expertise and authority",
        "category": "Genre-Specific",
        "target_audience": "Non-fiction authors seeking expertise and credibility",
        "profiles": [
            {
                "profile_id": "dr_malcolm_sterling",
                "name": "Dr. Malcolm Sterling",
                "priority": 1,
                "genres": ["Self-Help", "Psychology", "Personal Development"],
                "expertise": "Psychological insight and practical guidance"
            },
            {
                "profile_id": "dr_samuel_voss",
                "name": "Dr. Samuel Voss",
                "priority": 2,
                "genres": ["Popular Science", "Scientific Writing", "Research Communication"],
                "expertise": "Scientific communication and research translation"
            },
            {
                "profile_id": "rajesh_malhotra",
                "name": "Rajesh Malhotra",
                "priority": 3,
                "genres": ["Business", "Entrepreneurship", "Professional Development"],
                "expertise": "Business strategy and entrepreneurial insight"
            },
            {
                "profile_id": "dr_patricia_blackwell",
                "name": "Dr. Patricia Blackwell",
                "priority": 4,
                "genres": ["History", "Biography", "Historical Research"],
                "expertise": "Historical research and biographical narrative"
            }
        ]
    }
}

def generate_collection_file(collection_key: str, config: Dict[str, Any]) -> Dict[str, Any]:
    """Generate a complete collection JSON structure."""
    
    collection_data = {
        "collection_name": config["name"],
        "description": config["description"],
        "category": config["category"],
        "target_audience": config["target_audience"],
        "use_cases": [
            f"Authors working in {config['category'].lower()} contexts",
            f"Writers seeking {config['name'].lower()} approach",
            "Publishers looking for specialized expertise",
            "Readers interested in authentic genre representation"
        ],
        "created_date": "2024-05-24",
        "last_updated": "2024-05-24",
        "selection_criteria": [
            "Proven expertise in target areas",
            "Authentic voice and perspective",
            "Strong track record in genre/category",
            "Distinctive approach and style",
            "Reader engagement and satisfaction"
        ],
        "profiles": []
    }
    
    # Add profiles with enhanced metadata
    for profile in config["profiles"]:
        enhanced_profile = {
            "profile_id": profile["profile_id"],
            "name": profile["name"],
            "priority": profile["priority"],
            "genres": profile["genres"],
            "target_demographics": [f"{genre} readers" for genre in profile["genres"]],
            "recommended_for": [f"{genre} writing" for genre in profile["genres"]]
        }
        
        # Add category-specific fields
        if "specialization" in profile:
            enhanced_profile["specialization"] = profile["specialization"]
        if "debut_strengths" in profile:
            enhanced_profile["debut_strengths"] = profile["debut_strengths"]
        if "innovation_focus" in profile:
            enhanced_profile["innovation_focus"] = profile["innovation_focus"]
        if "cultural_focus" in profile:
            enhanced_profile["cultural_focus"] = profile["cultural_focus"]
        if "expertise" in profile:
            enhanced_profile["expertise"] = profile["expertise"]
            
        collection_data["profiles"].append(enhanced_profile)
    
    # Add usage guidelines
    collection_data["usage_guidelines"] = {
        "best_for": [
            f"Authors seeking {config['name'].lower()}",
            f"Projects requiring {config['category'].lower()} expertise",
            "Specialized genre development",
            "Authentic voice development"
        ],
        "considerations": [
            "Match profile expertise to project needs",
            "Consider target audience alignment",
            "Evaluate genre compatibility",
            "Balance specialization with accessibility"
        ]
    }
    
    return collection_data

def main():
    """Generate all recommended collection files."""
    
    # Create output directory
    output_dir = Path("src/writer_profiles/recommended")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("🚀 Generating recommended profile collections...")
    
    # Generate collection files
    for collection_key, config in COLLECTION_CONFIGS.items():
        collection_data = generate_collection_file(collection_key, config)
        
        output_path = output_dir / f"{collection_key}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(collection_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Generated {collection_key}.json")
    
    print(f"\n🎉 Generated {len(COLLECTION_CONFIGS)} recommended collections!")
    print("📁 Location: src/writer_profiles/recommended/")

if __name__ == "__main__":
    main()
