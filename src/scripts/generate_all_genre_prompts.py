"""
Automated script to generate all remaining genre-specific prompt files using Gemini.
"""

import os
import sys
import time
sys.path.append('src')

from src.core.gemini_client import GeminiClient

# All 38 genres (excluding the 3 we already created manually)
ALL_GENRES = [
    "literary_fiction",
    "commercial_fiction", 
    "mystery",
    "mystery_thriller",
    "thriller",
    "romance",
    "fantasy",
    "epic_fantasy",
    "science_fiction",
    "historical_fiction",
    "horror",
    "young_adult",
    "middle_grade",
    "children_s_chapter_books",
    "short_story_collection",
    "novella",
    "graphic_novel",
    "memoir",
    "biography",
    "history",
    "self_help",
    "business",
    "popular_science",
    "academic",
    "travel",
    "cookbook",
    "how_to",
    "essay_collection",
    "philosophy",
    "true_crime",
    "poetry_collection",
    "creative_non_fiction",
    "speculative_fiction",
    "alternate_history",
    "contemporary_fiction",
    "paranormal_romance",
    "urban_fantasy",
    "dystopian"
]

# Genres we already have (skip these)
EXISTING_GENRES = ["fantasy", "mystery", "romance"]

# Genres to generate
GENRES_TO_GENERATE = [genre for genre in ALL_GENRES if genre not in EXISTING_GENRES]

def format_genre_name(genre_key: str) -> str:
    """Convert genre key to proper display name."""
    name_mappings = {
        "literary_fiction": "Literary Fiction",
        "commercial_fiction": "Commercial Fiction",
        "mystery_thriller": "Mystery Thriller", 
        "thriller": "Thriller",
        "epic_fantasy": "Epic Fantasy",
        "science_fiction": "Science Fiction",
        "historical_fiction": "Historical Fiction",
        "horror": "Horror",
        "young_adult": "Young Adult",
        "middle_grade": "Middle Grade",
        "children_s_chapter_books": "Children's Chapter Books",
        "short_story_collection": "Short Story Collection",
        "novella": "Novella",
        "graphic_novel": "Graphic Novel",
        "memoir": "Memoir",
        "biography": "Biography",
        "history": "History",
        "self_help": "Self-Help",
        "business": "Business",
        "popular_science": "Popular Science",
        "academic": "Academic",
        "travel": "Travel",
        "cookbook": "Cookbook",
        "how_to": "How-To",
        "essay_collection": "Essay Collection",
        "philosophy": "Philosophy",
        "true_crime": "True Crime",
        "poetry_collection": "Poetry Collection",
        "creative_non_fiction": "Creative Non-Fiction",
        "speculative_fiction": "Speculative Fiction",
        "alternate_history": "Alternate History",
        "contemporary_fiction": "Contemporary Fiction",
        "paranormal_romance": "Paranormal Romance",
        "urban_fantasy": "Urban Fantasy",
        "dystopian": "Dystopian"
    }
    return name_mappings.get(genre_key, genre_key.replace("_", " ").title())

def format_class_name(genre_key: str) -> str:
    """Convert genre key to class name."""
    return "".join(word.capitalize() for word in genre_key.split("_")) + "Prompts"

def create_genre_prompt_template(genre_key: str, genre_name: str, class_name: str) -> str:
    """Create the prompt template for generating a genre file."""
    return f"""
You are an expert in genre-specific writing and novel generation. Create a comprehensive prompt module for the {genre_name} genre, following this EXACT structure and quality standard:

REQUIRED STRUCTURE:
```python
from .base_prompts import BasePrompts

class {class_name}(BasePrompts):
    GENRE_NAME = "{genre_name}"
    GENRE_DESCRIPTION = "A detailed description of the {genre_name.lower()} genre"
    
    GENRE_CHARACTERISTICS = [
        "First characteristic specific to {genre_name.lower()}",
        "Second characteristic...",
        # Include 8-10 detailed, specific characteristics
    ]
    
    TYPICAL_ELEMENTS = [
        "First typical element in {genre_name.lower()}",
        "Second element...", 
        # Include 10-12 concrete, actionable elements
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        {genre_key}_additions = '''
## {genre_name}-Specific Writing Considerations
- **Key Aspect 1**: Detailed explanation relevant to {genre_name.lower()}
- **Key Aspect 2**: Another important consideration
# Include 6-8 detailed writing considerations
'''
        return base_prompt + {genre_key}_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        {genre_key}_additions = '''
## {genre_name}-Specific Outline Requirements
- **Structure Element 1**: How this applies to {genre_name.lower()}
- **Structure Element 2**: Another structural consideration
# Include detailed outline guidance
'''
        return base_prompt + {genre_key}_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        {genre_key}_additions = '''
## {genre_name}-Specific Character Development
- **Character Aspect 1**: How characters work in {genre_name.lower()}
- **Character Aspect 2**: Another character consideration
# Include detailed character guidance
'''
        return base_prompt + {genre_key}_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        {genre_key}_additions = '''
## {genre_name}-Specific Chapter Writing
- **Writing Technique 1**: How to write {genre_name.lower()} chapters
- **Writing Technique 2**: Another technique
# Include detailed chapter writing guidance
'''
        return base_prompt + {genre_key}_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return {class_name}.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return {class_name}.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return {class_name}.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return {class_name}.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return {class_name}.get_enhancement_prompt(**kwargs)
```

CRITICAL REQUIREMENTS:
1. Follow the EXACT structure shown above
2. Make all content specific to {genre_name} - no generic content
3. Include 8-10 detailed GENRE_CHARACTERISTICS
4. Include 10-12 concrete TYPICAL_ELEMENTS  
5. Each prompt method must have substantial, genre-specific additions
6. Use professional, detailed writing throughout
7. Include all convenience functions at the end
8. Make variable names use {genre_key} format consistently

Generate the complete {genre_key}.py file content now. Return ONLY the Python code, no markdown formatting or explanations.
"""

def generate_genre_file(gemini: GeminiClient, genre_key: str) -> bool:
    """Generate a single genre prompt file."""
    
    genre_name = format_genre_name(genre_key)
    class_name = format_class_name(genre_key)
    
    print(f"  📝 Generating {genre_name} ({genre_key}.py)...")
    
    try:
        # Create the prompt
        prompt = create_genre_prompt_template(genre_key, genre_name, class_name)
        
        # Generate the content
        response = gemini.generate_content(prompt, temperature=0.3, max_tokens=8000)
        
        # Clean up the response (remove markdown if present)
        content = response.strip()
        if content.startswith("```python"):
            content = content[9:]
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()
        
        # Save the file
        file_path = f"src/prompts/{genre_key}.py"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f'"""\n{genre_name} genre-specific prompts for novel generation.\n"""\n\n')
            f.write(content)
        
        print(f"    ✓ Generated {genre_name} successfully ({len(content)} chars)")
        return True
        
    except Exception as e:
        print(f"    ✗ Failed to generate {genre_name}: {str(e)}")
        return False

def main():
    """Generate all genre prompt files."""
    
    print("🚀 Automated Genre Prompt Generation")
    print("=" * 50)
    
    try:
        # Initialize Gemini
        gemini = GeminiClient()
        print(f"✓ Gemini client initialized")
        
        # Count genres to generate
        total_genres = len(GENRES_TO_GENERATE)
        print(f"📊 Generating {total_genres} genre prompt files...")
        print(f"⏭️  Skipping existing: {', '.join(EXISTING_GENRES)}")
        
        # Generate each genre
        successful = 0
        failed = 0
        
        for i, genre_key in enumerate(GENRES_TO_GENERATE, 1):
            print(f"\n[{i}/{total_genres}] Processing {genre_key}...")
            
            if generate_genre_file(gemini, genre_key):
                successful += 1
            else:
                failed += 1
            
            # Add a small delay to avoid rate limiting
            if i < total_genres:
                time.sleep(1)
        
        # Summary
        print("\n" + "=" * 50)
        print(f"📊 Generation Complete!")
        print(f"✓ Successful: {successful}")
        print(f"✗ Failed: {failed}")
        print(f"📁 Total files: {successful + len(EXISTING_GENRES)} / {len(ALL_GENRES)}")
        
        if failed == 0:
            print("\n🎉 All genre prompt files generated successfully!")
            print("🔧 The prompt system is now complete and ready to use.")
        else:
            print(f"\n⚠️  {failed} files failed to generate. You may need to create them manually.")
            
    except Exception as e:
        print(f"\n❌ Critical error: {str(e)}")
        print("Manual generation may be required.")

if __name__ == "__main__":
    main()
