"""
Test script to evaluate if Gemini can generate genre-specific prompts
in the same style and quality as the manually created examples.
"""

import os
import sys
sys.path.append('src')

from src.core.gemini_client import GeminiClient

def test_gemini_prompt_generation():
    """Test if Gemini can generate high-quality genre prompts."""
    
    try:
        # Initialize Gemini client
        gemini = GeminiClient()
        print("✓ Gemini client initialized successfully")
        
        # Test prompt for generating a science fiction prompt file
        test_prompt = """
You are an expert in genre-specific writing and novel generation. I need you to create a comprehensive prompt module for the Science Fiction genre, following the exact same structure and quality as these examples:

EXAMPLE STRUCTURE (from fantasy.py):
```python
from .base_prompts import BasePrompts

class ScienceFictionPrompts(BasePrompts):
    GENRE_NAME = "Science Fiction"
    GENRE_DESCRIPTION = "A genre that explores futuristic concepts, advanced technology, and scientific possibilities"
    
    GENRE_CHARACTERISTICS = [
        "Advanced technology and scientific concepts",
        "Exploration of future societies and civilizations",
        # ... more characteristics
    ]
    
    TYPICAL_ELEMENTS = [
        "Futuristic technology and gadgets",
        "Space travel and alien civilizations", 
        # ... more elements
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        scifi_additions = '''
## Science Fiction-Specific Writing Considerations
- **Scientific Accuracy**: Balance scientific plausibility with narrative needs
- **Technology Integration**: Show how advanced tech affects society and characters
# ... more considerations
'''
        return base_prompt + scifi_additions

    # Similar methods for get_outline_prompt, get_character_prompt, get_chapter_prompt
```

REQUIREMENTS:
1. Follow the EXACT same structure as the examples
2. Include 8-10 GENRE_CHARACTERISTICS that are specific and detailed
3. Include 10-12 TYPICAL_ELEMENTS that are concrete and actionable
4. Create genre-specific additions for each prompt type that are:
   - Detailed and comprehensive
   - Specific to science fiction
   - Professionally written
   - Practical for novel generation

5. Include convenience functions at the end
6. Make it comprehensive and professional quality

Generate the complete science_fiction.py file content now:
"""

        print("\n🧪 Testing Gemini's ability to generate genre prompts...")
        print("Generating Science Fiction prompt file...")
        
        # Generate the content
        response = gemini.generate_content(test_prompt, temperature=0.3, max_tokens=8000)
        
        print(f"\n📝 Generated content length: {len(response)} characters")
        
        # Save the test output
        with open("test_scifi_output.py", "w", encoding="utf-8") as f:
            f.write(response)
        
        print("✓ Test output saved to test_scifi_output.py")
        
        # Analyze the quality
        print("\n🔍 Quality Analysis:")
        
        # Check for required components
        checks = {
            "Has class definition": "class ScienceFictionPrompts" in response,
            "Has GENRE_NAME": "GENRE_NAME" in response,
            "Has GENRE_CHARACTERISTICS": "GENRE_CHARACTERISTICS" in response,
            "Has TYPICAL_ELEMENTS": "TYPICAL_ELEMENTS" in response,
            "Has writer_profile_prompt": "get_writer_profile_prompt" in response,
            "Has outline_prompt": "get_outline_prompt" in response,
            "Has character_prompt": "get_character_prompt" in response,
            "Has chapter_prompt": "get_chapter_prompt" in response,
            "Has convenience functions": "def get_writer_profile_prompt" in response,
            "Proper imports": "from .base_prompts import BasePrompts" in response
        }
        
        passed_checks = 0
        for check, result in checks.items():
            status = "✓" if result else "✗"
            print(f"  {status} {check}")
            if result:
                passed_checks += 1
        
        quality_score = (passed_checks / len(checks)) * 100
        print(f"\n📊 Quality Score: {quality_score:.1f}% ({passed_checks}/{len(checks)} checks passed)")
        
        # Determine if Gemini is suitable for automation
        if quality_score >= 80:
            print("\n🎉 RESULT: Gemini can generate high-quality genre prompts!")
            print("✓ Automation recommended - Gemini can handle the remaining 35 genres")
            return True
        else:
            print("\n⚠️  RESULT: Gemini quality is insufficient for automation")
            print("✗ Manual creation recommended for consistent quality")
            return False
            
    except Exception as e:
        print(f"\n❌ Error testing Gemini: {str(e)}")
        print("✗ Manual creation required due to technical issues")
        return False

if __name__ == "__main__":
    print("🚀 Testing Gemini's ability to generate genre-specific prompts...")
    print("=" * 60)
    
    can_automate = test_gemini_prompt_generation()
    
    print("\n" + "=" * 60)
    if can_automate:
        print("🤖 RECOMMENDATION: Use Gemini to generate the remaining 35 genre files")
        print("This will save significant time while maintaining quality")
    else:
        print("✍️  RECOMMENDATION: Manually create the remaining 35 genre files")
        print("This ensures consistent quality and structure")
