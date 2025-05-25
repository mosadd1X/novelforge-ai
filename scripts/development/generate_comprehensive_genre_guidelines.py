#!/usr/bin/env python3
"""
Development Script: Generate Comprehensive Genre Guidelines for Back Cover Descriptions

This script uses Gemini AI to generate detailed, professional guidelines for all 38 genres
supported by the ebook generation system. Each genre gets specific guidelines for:
- Language style and tone
- Key elements to emphasize
- Target audience considerations
- Marketing hooks and emotional triggers
- Visual styling preferences for back covers
"""

import sys
import os
import json
from pathlib import Path
from typing import Dict, List, Any

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.core.resilient_gemini_client import ResilientGeminiClient
from src.utils.genre_defaults import get_all_genres
from rich.console import Console
from rich.progress import Progress, TaskID

console = Console()


class GenreGuidelinesGenerator:
    """
    Generates comprehensive genre-specific guidelines for back cover descriptions.
    """
    
    def __init__(self):
        """Initialize the generator."""
        self.gemini_client = ResilientGeminiClient()
        self.output_file = project_root / "src" / "utils" / "comprehensive_genre_guidelines.py"
        self.guidelines = {}
        
    def generate_all_guidelines(self) -> bool:
        """
        Generate guidelines for all 38 genres.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            console.print("[bold cyan]🎯 Generating Comprehensive Genre Guidelines[/bold cyan]")
            console.print(f"📁 Output file: {self.output_file}")
            
            # Get all genres
            all_genres = get_all_genres()
            console.print(f"📚 Processing {len(all_genres)} genres")
            
            with Progress() as progress:
                task = progress.add_task("[cyan]Generating guidelines...", total=len(all_genres))
                
                for genre in all_genres:
                    if genre.lower() == "test":
                        # Skip test genre
                        progress.advance(task)
                        continue
                        
                    console.print(f"\n🔄 Processing: {genre}")
                    
                    guidelines = self._generate_genre_guidelines(genre)
                    if guidelines:
                        self.guidelines[genre.lower()] = guidelines
                        console.print(f"✅ {genre} guidelines generated")
                    else:
                        console.print(f"⚠️ Failed to generate guidelines for {genre}")
                    
                    progress.advance(task)
            
            # Generate the Python file
            self._create_guidelines_file()
            
            console.print(f"\n🎉 Successfully generated guidelines for {len(self.guidelines)} genres!")
            console.print(f"📄 File saved: {self.output_file}")
            
            return True
            
        except Exception as e:
            console.print(f"❌ Error generating guidelines: {e}")
            return False
    
    def _generate_genre_guidelines(self, genre: str) -> Dict[str, Any]:
        """
        Generate comprehensive guidelines for a specific genre.
        
        Args:
            genre: Genre name
            
        Returns:
            Dictionary with genre guidelines
        """
        try:
            prompt = f"""
You are a professional book marketing expert specializing in back cover copy and genre-specific marketing.

Generate comprehensive guidelines for writing compelling back cover descriptions for {genre} books.

GENRE: {genre}

Provide detailed guidelines in the following format:

LANGUAGE_STYLE:
[Describe the specific language style, tone, and voice that works best for this genre]

KEY_ELEMENTS:
[List 5-7 key elements that should be emphasized in back cover descriptions for this genre]

EMOTIONAL_HOOKS:
[Describe the primary emotional triggers and hooks that attract readers of this genre]

MARKETING_FOCUS:
[Explain what aspects should be highlighted to market effectively to this genre's audience]

TARGET_AUDIENCE_CONSIDERATIONS:
[Describe the typical reader expectations and what they're looking for]

VISUAL_STYLE_PREFERENCES:
[Suggest color schemes, imagery, and visual elements for back cover design]

AVOID:
[List things to avoid when writing descriptions for this genre]

EXAMPLE_PHRASES:
[Provide 5-10 example phrases or sentence starters that work well for this genre]

Make your response specific to {genre} and avoid generic advice. Focus on what makes this genre unique and what specifically appeals to its readers.
"""
            
            response = self.gemini_client.generate_content(prompt, temperature=0.7, max_tokens=2000)
            
            if not response:
                return None
            
            # Parse the response into structured data
            return self._parse_guidelines_response(response)
            
        except Exception as e:
            console.print(f"❌ Error generating guidelines for {genre}: {e}")
            return None
    
    def _parse_guidelines_response(self, response: str) -> Dict[str, Any]:
        """
        Parse Gemini's response into structured guidelines.
        
        Args:
            response: Raw response from Gemini
            
        Returns:
            Structured guidelines dictionary
        """
        guidelines = {}
        
        sections = [
            "LANGUAGE_STYLE", "KEY_ELEMENTS", "EMOTIONAL_HOOKS", 
            "MARKETING_FOCUS", "TARGET_AUDIENCE_CONSIDERATIONS",
            "VISUAL_STYLE_PREFERENCES", "AVOID", "EXAMPLE_PHRASES"
        ]
        
        for i, section in enumerate(sections):
            # Find the section content
            start_pattern = f"{section}:"
            if i < len(sections) - 1:
                end_pattern = f"{sections[i + 1]}:"
            else:
                end_pattern = None
            
            start_idx = response.find(start_pattern)
            if start_idx == -1:
                continue
                
            start_idx += len(start_pattern)
            
            if end_pattern:
                end_idx = response.find(end_pattern, start_idx)
                if end_idx == -1:
                    content = response[start_idx:].strip()
                else:
                    content = response[start_idx:end_idx].strip()
            else:
                content = response[start_idx:].strip()
            
            # Clean up the content
            content = content.strip()
            if content.startswith('[') and content.endswith(']'):
                content = content[1:-1].strip()
            
            guidelines[section.lower()] = content
        
        return guidelines
    
    def _create_guidelines_file(self) -> None:
        """Create the comprehensive genre guidelines Python file."""
        
        file_content = '''"""
Comprehensive Genre Guidelines for Back Cover Descriptions

This module contains detailed, AI-generated guidelines for all 38 supported genres.
Each genre has specific guidelines for language style, key elements, emotional hooks,
marketing focus, target audience considerations, and visual preferences.

Generated automatically by scripts/development/generate_comprehensive_genre_guidelines.py
"""

from typing import Dict, Any


class ComprehensiveGenreGuidelines:
    """
    Comprehensive guidelines for all supported genres.
    """
    
    # All genre guidelines generated by Gemini AI
    GUIDELINES = {
'''
        
        # Add all guidelines
        for genre, guidelines in self.guidelines.items():
            file_content += f'        "{genre}": {{\n'
            for key, value in guidelines.items():
                # Escape quotes and format properly
                escaped_value = value.replace('"', '\\"').replace('\n', '\\n')
                file_content += f'            "{key}": "{escaped_value}",\n'
            file_content += '        },\n'
        
        file_content += '''    }
    
    @classmethod
    def get_guidelines(cls, genre: str) -> Dict[str, str]:
        """
        Get comprehensive guidelines for a specific genre.
        
        Args:
            genre: Genre name
            
        Returns:
            Dictionary with genre guidelines
        """
        genre_key = genre.lower().strip()
        
        # Direct match
        if genre_key in cls.GUIDELINES:
            return cls.GUIDELINES[genre_key]
        
        # Fuzzy matching for variations
        for key in cls.GUIDELINES:
            if genre_key in key or key in genre_key:
                return cls.GUIDELINES[key]
        
        # Return generic guidelines if no match
        return {
            "language_style": "Clear, engaging, and accessible language appropriate for the target audience",
            "key_elements": "Compelling characters, engaging plot, emotional stakes, clear conflict, satisfying resolution",
            "emotional_hooks": "Universal themes of growth, challenge, discovery, and human connection",
            "marketing_focus": "Character development, plot intrigue, emotional journey, and reader satisfaction",
            "target_audience_considerations": "Readers seeking engaging stories with relatable characters and meaningful themes",
            "visual_style_preferences": "Clean, professional design with colors that reflect the book's tone and mood",
            "avoid": "Generic descriptions, spoilers, overly complex language, misleading promises",
            "example_phrases": "A compelling journey, Unforgettable characters, A story that will stay with you, Masterful storytelling, An emotional rollercoaster"
        }
    
    @classmethod
    def get_language_style(cls, genre: str) -> str:
        """Get language style guidelines for a genre."""
        guidelines = cls.get_guidelines(genre)
        return guidelines.get("language_style", "Clear and engaging language")
    
    @classmethod
    def get_key_elements(cls, genre: str) -> str:
        """Get key elements to emphasize for a genre."""
        guidelines = cls.get_guidelines(genre)
        return guidelines.get("key_elements", "Compelling characters and engaging plot")
    
    @classmethod
    def get_emotional_hooks(cls, genre: str) -> str:
        """Get emotional hooks for a genre."""
        guidelines = cls.get_guidelines(genre)
        return guidelines.get("emotional_hooks", "Universal themes and human connection")
    
    @classmethod
    def get_marketing_focus(cls, genre: str) -> str:
        """Get marketing focus for a genre."""
        guidelines = cls.get_guidelines(genre)
        return guidelines.get("marketing_focus", "Character development and plot intrigue")
    
    @classmethod
    def get_visual_preferences(cls, genre: str) -> str:
        """Get visual style preferences for a genre."""
        guidelines = cls.get_guidelines(genre)
        return guidelines.get("visual_style_preferences", "Clean, professional design")
    
    @classmethod
    def get_example_phrases(cls, genre: str) -> str:
        """Get example phrases for a genre."""
        guidelines = cls.get_guidelines(genre)
        return guidelines.get("example_phrases", "A compelling journey, Unforgettable characters")


def get_comprehensive_genre_guidelines(genre: str) -> str:
    """
    Get comprehensive genre-specific guidelines for back cover descriptions.
    
    Args:
        genre: Book genre
        
    Returns:
        Formatted guidelines string for use in prompts
    """
    guidelines = ComprehensiveGenreGuidelines.get_guidelines(genre)
    
    return f"""
LANGUAGE STYLE: {guidelines.get('language_style', 'Clear and engaging')}

KEY ELEMENTS TO EMPHASIZE:
{guidelines.get('key_elements', 'Compelling characters and plot')}

EMOTIONAL HOOKS:
{guidelines.get('emotional_hooks', 'Universal themes')}

MARKETING FOCUS:
{guidelines.get('marketing_focus', 'Character and plot development')}

TARGET AUDIENCE CONSIDERATIONS:
{guidelines.get('target_audience_considerations', 'General readers')}

EXAMPLE PHRASES:
{guidelines.get('example_phrases', 'Compelling, engaging, unforgettable')}

AVOID:
{guidelines.get('avoid', 'Generic descriptions and spoilers')}
"""
'''
        
        # Write the file
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(file_content)


def main():
    """Main function to generate comprehensive genre guidelines."""
    console.print("[bold blue]🚀 Comprehensive Genre Guidelines Generator[/bold blue]")
    console.print("=" * 60)
    
    generator = GenreGuidelinesGenerator()
    
    # Check if Gemini client is available
    try:
        test_response = generator.gemini_client.generate_content("Test", max_tokens=10)
        if not test_response:
            console.print("❌ Gemini client not available. Please check your API keys.")
            return False
    except Exception as e:
        console.print(f"❌ Gemini client error: {e}")
        return False
    
    # Generate guidelines
    success = generator.generate_all_guidelines()
    
    if success:
        console.print("\n🎉 Genre guidelines generation completed successfully!")
        console.print("\n📋 Next Steps:")
        console.print("  1. Review the generated guidelines file")
        console.print("  2. Update back_cover_generator.py to use comprehensive guidelines")
        console.print("  3. Test with different genres")
        console.print("  4. Adjust guidelines as needed")
    else:
        console.print("\n❌ Genre guidelines generation failed.")
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
