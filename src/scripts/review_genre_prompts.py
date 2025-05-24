"""
Comprehensive review script to check all genre prompt files for quality and consistency.
"""

import os
import sys
import importlib
from typing import Dict, Any

# Add src to path
sys.path.append('src')

# All 38 genres
ALL_GENRES = [
    "literary_fiction", "commercial_fiction", "mystery", "mystery_thriller", "thriller",
    "romance", "fantasy", "epic_fantasy", "science_fiction", "historical_fiction",
    "horror", "young_adult", "middle_grade", "children_s_chapter_books",
    "short_story_collection", "novella", "graphic_novel", "memoir", "biography",
    "history", "self_help", "business", "popular_science", "academic", "travel",
    "cookbook", "how_to", "essay_collection", "philosophy", "true_crime",
    "poetry_collection", "creative_non_fiction", "speculative_fiction",
    "alternate_history", "contemporary_fiction", "paranormal_romance",
    "urban_fantasy", "dystopian"
]

def check_file_structure(genre: str) -> Dict[str, Any]:
    """Check the structure and quality of a genre prompt file."""
    
    result = {
        "genre": genre,
        "file_exists": False,
        "imports_correctly": False,
        "has_class": False,
        "has_genre_name": False,
        "has_description": False,
        "has_characteristics": False,
        "has_elements": False,
        "has_writer_profile": False,
        "has_outline": False,
        "has_character": False,
        "has_chapter": False,
        "has_enhancement": False,
        "has_convenience_functions": False,
        "characteristics_count": 0,
        "elements_count": 0,
        "file_size": 0,
        "errors": []
    }
    
    file_path = f"src/prompts/{genre}.py"
    
    # Check if file exists
    if not os.path.exists(file_path):
        result["errors"].append("File does not exist")
        return result
    
    result["file_exists"] = True
    result["file_size"] = os.path.getsize(file_path)
    
    try:
        # Try to import the module
        module_name = f"src.prompts.{genre}"
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result["imports_correctly"] = True
        
        # Check for class
        class_name = "".join(word.capitalize() for word in genre.split("_")) + "Prompts"
        if hasattr(module, class_name):
            result["has_class"] = True
            prompt_class = getattr(module, class_name)
            
            # Check class attributes
            if hasattr(prompt_class, "GENRE_NAME"):
                result["has_genre_name"] = True
            
            if hasattr(prompt_class, "GENRE_DESCRIPTION"):
                result["has_description"] = True
            
            if hasattr(prompt_class, "GENRE_CHARACTERISTICS"):
                result["has_characteristics"] = True
                characteristics = getattr(prompt_class, "GENRE_CHARACTERISTICS")
                if isinstance(characteristics, list):
                    result["characteristics_count"] = len(characteristics)
            
            if hasattr(prompt_class, "TYPICAL_ELEMENTS"):
                result["has_elements"] = True
                elements = getattr(prompt_class, "TYPICAL_ELEMENTS")
                if isinstance(elements, list):
                    result["elements_count"] = len(elements)
            
            # Check methods
            if hasattr(prompt_class, "get_writer_profile_prompt"):
                result["has_writer_profile"] = True
            
            if hasattr(prompt_class, "get_outline_prompt"):
                result["has_outline"] = True
            
            if hasattr(prompt_class, "get_character_prompt"):
                result["has_character"] = True
            
            if hasattr(prompt_class, "get_chapter_prompt"):
                result["has_chapter"] = True
            
            if hasattr(prompt_class, "get_enhancement_prompt"):
                result["has_enhancement"] = True
        
        # Check convenience functions
        convenience_functions = [
            "get_writer_profile_prompt",
            "get_outline_prompt", 
            "get_character_prompt",
            "get_chapter_prompt",
            "get_enhancement_prompt"
        ]
        
        convenience_count = sum(1 for func in convenience_functions if hasattr(module, func))
        result["has_convenience_functions"] = convenience_count == len(convenience_functions)
        
    except Exception as e:
        result["errors"].append(f"Import/execution error: {str(e)}")
    
    return result

def calculate_quality_score(result: Dict[str, Any]) -> float:
    """Calculate a quality score for a genre file."""
    
    if not result["file_exists"]:
        return 0.0
    
    checks = [
        result["imports_correctly"],
        result["has_class"],
        result["has_genre_name"],
        result["has_description"],
        result["has_characteristics"],
        result["has_elements"],
        result["has_writer_profile"],
        result["has_outline"],
        result["has_character"],
        result["has_chapter"],
        result["has_enhancement"],
        result["has_convenience_functions"],
        result["characteristics_count"] >= 8,
        result["elements_count"] >= 10,
        result["file_size"] > 5000,  # Reasonable file size
        len(result["errors"]) == 0
    ]
    
    return (sum(checks) / len(checks)) * 100

def review_all_genres():
    """Review all genre prompt files."""
    
    print("🔍 Comprehensive Genre Prompt File Review")
    print("=" * 60)
    
    results = []
    total_score = 0
    perfect_files = 0
    
    for genre in ALL_GENRES:
        print(f"\n📋 Reviewing {genre}...")
        result = check_file_structure(genre)
        quality_score = calculate_quality_score(result)
        result["quality_score"] = quality_score
        results.append(result)
        total_score += quality_score
        
        if quality_score == 100.0:
            perfect_files += 1
            print(f"  ✅ Perfect (100%)")
        elif quality_score >= 90.0:
            print(f"  🟢 Excellent ({quality_score:.1f}%)")
        elif quality_score >= 80.0:
            print(f"  🟡 Good ({quality_score:.1f}%)")
        elif quality_score >= 60.0:
            print(f"  🟠 Needs improvement ({quality_score:.1f}%)")
        else:
            print(f"  🔴 Poor ({quality_score:.1f}%)")
        
        # Show errors if any
        if result["errors"]:
            for error in result["errors"]:
                print(f"    ❌ {error}")
    
    # Summary
    average_score = total_score / len(ALL_GENRES)
    print("\n" + "=" * 60)
    print("📊 REVIEW SUMMARY")
    print("=" * 60)
    print(f"Total files reviewed: {len(ALL_GENRES)}")
    print(f"Perfect files (100%): {perfect_files}")
    print(f"Average quality score: {average_score:.1f}%")
    
    # Detailed breakdown
    score_ranges = {
        "Perfect (100%)": 0,
        "Excellent (90-99%)": 0,
        "Good (80-89%)": 0,
        "Needs improvement (60-79%)": 0,
        "Poor (<60%)": 0
    }
    
    for result in results:
        score = result["quality_score"]
        if score == 100.0:
            score_ranges["Perfect (100%)"] += 1
        elif score >= 90.0:
            score_ranges["Excellent (90-99%)"] += 1
        elif score >= 80.0:
            score_ranges["Good (80-89%)"] += 1
        elif score >= 60.0:
            score_ranges["Needs improvement (60-79%)"] += 1
        else:
            score_ranges["Poor (<60%)"] += 1
    
    print("\n📈 Quality Distribution:")
    for category, count in score_ranges.items():
        percentage = (count / len(ALL_GENRES)) * 100
        print(f"  {category}: {count} files ({percentage:.1f}%)")
    
    # Files needing attention
    problem_files = [r for r in results if r["quality_score"] < 90.0]
    if problem_files:
        print(f"\n⚠️  Files needing attention ({len(problem_files)}):")
        for result in problem_files:
            print(f"  📄 {result['genre']}: {result['quality_score']:.1f}%")
            for error in result["errors"]:
                print(f"    ❌ {error}")
    else:
        print("\n🎉 All files are in excellent condition!")
    
    # Recommendations
    print("\n💡 RECOMMENDATIONS:")
    if average_score >= 95.0:
        print("✅ The prompt system is excellent and ready for production use!")
    elif average_score >= 85.0:
        print("🟢 The prompt system is very good with minor improvements needed.")
    elif average_score >= 75.0:
        print("🟡 The prompt system is good but needs some improvements.")
    else:
        print("🔴 The prompt system needs significant improvements before use.")
    
    return results

if __name__ == "__main__":
    review_all_genres()
