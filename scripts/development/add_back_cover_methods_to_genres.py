#!/usr/bin/env python3
"""
Development Script: Add Back Cover Description Methods to All Genre Files

This script automatically adds comprehensive back cover description methods to all genre files
in the src/prompts/ directory. It uses Gemini AI to generate genre-specific guidelines for:
- Back cover description prompts
- Short description prompts
- Marketing tagline prompts
- Visual styling preferences
- Genre-specific language and tone

The script will:
1. Scan all existing genre files in src/prompts/
2. Generate comprehensive back cover methods for each genre
3. Add the methods to each genre file
4. Create any missing genre files for complete 38-genre coverage
"""

import sys
import os
import re
import time
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add the project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.core.resilient_gemini_client import ResilientGeminiClient
from src.utils.genre_defaults import get_all_genres
from rich.console import Console
from rich.progress import Progress, TaskID

console = Console()


class GenreBackCoverMethodsGenerator:
    """
    Adds comprehensive back cover description methods to all genre files.
    """

    def __init__(self):
        """Initialize the generator."""
        self.gemini_client = ResilientGeminiClient()
        self.prompts_dir = project_root / "src" / "prompts"
        self.processed_genres = []
        self.created_files = []
        self.updated_files = []

    def process_all_genres(self) -> bool:
        """
        Process all genres and add back cover methods.

        Returns:
            True if successful, False otherwise
        """
        try:
            console.print("[bold cyan]🎯 Adding Back Cover Methods to All Genre Files[/bold cyan]")
            console.print(f"📁 Prompts directory: {self.prompts_dir}")

            # Get all genres
            all_genres = get_all_genres()
            console.print(f"📚 Processing {len(all_genres)} genres")

            with Progress() as progress:
                task = progress.add_task("[cyan]Processing genres...", total=len(all_genres))

                for genre in all_genres:
                    if genre.lower() == "test":
                        # Skip test genre
                        progress.advance(task)
                        continue

                    console.print(f"\n🔄 Processing: {genre}")

                    # Add delay to handle rate limits
                    if len(self.processed_genres) > 0:
                        console.print("⏳ Waiting 3 seconds to avoid rate limits...")
                        time.sleep(3)

                    success = self._process_genre(genre)
                    if success:
                        self.processed_genres.append(genre)
                        console.print(f"✅ {genre} processed successfully")
                    else:
                        console.print(f"⚠️ Failed to process {genre}")

                    progress.advance(task)

            # Summary
            console.print(f"\n🎉 Processing Complete!")
            console.print(f"✅ Processed genres: {len(self.processed_genres)}")
            console.print(f"📝 Updated files: {len(self.updated_files)}")
            console.print(f"🆕 Created files: {len(self.created_files)}")

            return True

        except Exception as e:
            console.print(f"❌ Error processing genres: {e}")
            return False

    def _process_genre(self, genre: str) -> bool:
        """
        Process a single genre and add back cover methods.

        Args:
            genre: Genre name

        Returns:
            True if successful, False otherwise
        """
        try:
            # Convert genre name to filename
            filename = self._genre_to_filename(genre)
            file_path = self.prompts_dir / f"{filename}.py"

            if file_path.exists():
                # Update existing file
                return self._update_existing_file(file_path, genre)
            else:
                # Create new file
                return self._create_new_file(file_path, genre)

        except Exception as e:
            console.print(f"❌ Error processing {genre}: {e}")
            return False

    def _genre_to_filename(self, genre: str) -> str:
        """Convert genre name to filename format."""
        # Handle special cases with exact mappings
        special_mappings = {
            "Mystery/Thriller": "mystery_thriller",
            "Children'S Chapter Books": "children_s_chapter_books",
            "Self-Help": "self_help",
            "How-To": "how_to",
            "Creative Non-Fiction": "creative_non_fiction"
        }

        if genre in special_mappings:
            return special_mappings[genre]

        # Convert to lowercase and replace spaces/special chars with underscores
        filename = re.sub(r'[^a-zA-Z0-9\s]', '', genre.lower())
        filename = re.sub(r'\s+', '_', filename)
        return filename

    def _update_existing_file(self, file_path: Path, genre: str) -> bool:
        """
        Update an existing genre file with back cover methods.

        Args:
            file_path: Path to the genre file
            genre: Genre name

        Returns:
            True if successful, False otherwise
        """
        try:
            # Read existing file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if back cover methods already exist
            if 'get_back_cover_prompt' in content:
                console.print(f"  ℹ️ {genre} already has back cover methods")
                return True

            # Generate back cover methods
            back_cover_methods = self._generate_back_cover_methods(genre)
            if not back_cover_methods:
                return False

            # Find insertion point (before convenience functions)
            insertion_point = content.find('# Convenience functions for direct access')
            if insertion_point == -1:
                # Fallback: insert before last class method
                insertion_point = content.rfind('    @classmethod')
                if insertion_point != -1:
                    # Find end of last method
                    insertion_point = content.find('\n\n', insertion_point)
                    if insertion_point != -1:
                        insertion_point += 2

            if insertion_point == -1:
                console.print(f"  ⚠️ Could not find insertion point for {genre}")
                return False

            # Insert back cover methods
            new_content = (
                content[:insertion_point] +
                back_cover_methods +
                '\n' +
                content[insertion_point:]
            )

            # Add convenience functions for back cover methods
            convenience_functions = self._generate_convenience_functions()

            # Find where to add convenience functions
            conv_insertion = new_content.find('def get_enhancement_prompt(**kwargs) -> str:')
            if conv_insertion != -1:
                # Find end of enhancement function
                conv_insertion = new_content.find('\n\n', conv_insertion)
                if conv_insertion != -1:
                    new_content = (
                        new_content[:conv_insertion] +
                        '\n' +
                        convenience_functions +
                        new_content[conv_insertion:]
                    )

            # Write updated file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            self.updated_files.append(str(file_path))
            console.print(f"  ✅ Updated {file_path.name}")
            return True

        except Exception as e:
            console.print(f"  ❌ Error updating {file_path.name}: {e}")
            return False

    def _create_new_file(self, file_path: Path, genre: str) -> bool:
        """
        Create a new genre file with back cover methods.

        Args:
            file_path: Path for the new file
            genre: Genre name

        Returns:
            True if successful, False otherwise
        """
        try:
            console.print(f"  🆕 Creating new file for {genre}")

            # Generate complete file content
            file_content = self._generate_complete_genre_file(genre)
            if not file_content:
                return False

            # Write new file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_content)

            self.created_files.append(str(file_path))
            console.print(f"  ✅ Created {file_path.name}")
            return True

        except Exception as e:
            console.print(f"  ❌ Error creating {file_path.name}: {e}")
            return False

    def _generate_back_cover_methods(self, genre: str) -> Optional[str]:
        """
        Generate back cover description methods for a genre.

        Args:
            genre: Genre name

        Returns:
            Generated methods as string or None if failed
        """
        try:
            prompt = f"""
You are a professional book marketing expert specializing in back cover copy and genre-specific marketing.

Generate Python class methods for the {genre} genre that will be used to create compelling back cover descriptions.

GENRE: {genre}

Generate the following methods for a Python class (use proper indentation with 4 spaces):

1. get_back_cover_prompt() - Main method for generating back cover descriptions
2. get_short_description_prompt() - For 2-3 line book recommendations
3. get_marketing_tagline_prompt() - For punchy marketing taglines
4. get_visual_style_preferences() - For back cover visual design

Each method should:
- Be a @classmethod
- Take **kwargs parameter
- Return a detailed, genre-specific prompt string
- Include specific guidelines for {genre}
- Focus on what makes {genre} unique and appealing to its readers

Format your response as complete Python methods with proper docstrings and genre-specific content.
Make the prompts detailed and actionable for AI content generation.

Focus on {genre}-specific language, themes, emotional hooks, and marketing strategies.
"""

            # Try multiple times with increasing delays for rate limits
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = self.gemini_client.generate_content(prompt, temperature=0.7, max_tokens=3000)

                    if response:
                        # Clean up and format the response
                        methods = self._format_generated_methods(response, genre)
                        return methods
                    else:
                        console.print(f"  ⚠️ No response from Gemini for {genre} (attempt {attempt + 1})")

                except Exception as api_error:
                    console.print(f"  ⚠️ API error for {genre} (attempt {attempt + 1}): {api_error}")

                    if "rate limit" in str(api_error).lower() or "quota" in str(api_error).lower():
                        wait_time = (attempt + 1) * 10  # 10, 20, 30 seconds
                        console.print(f"  ⏳ Rate limit detected, waiting {wait_time} seconds...")
                        time.sleep(wait_time)
                    else:
                        time.sleep(2)  # Short delay for other errors

                if attempt < max_retries - 1:
                    console.print(f"  🔄 Retrying {genre}...")

            console.print(f"  ❌ Failed to generate methods for {genre} after {max_retries} attempts")
            return None

        except Exception as e:
            console.print(f"❌ Error generating back cover methods for {genre}: {e}")
            return None

    def _format_generated_methods(self, response: str, genre: str) -> str:
        """
        Format the generated methods properly.

        Args:
            response: Raw response from Gemini
            genre: Genre name

        Returns:
            Formatted methods string
        """
        # Basic formatting and cleanup
        methods = response.strip()

        # Ensure proper indentation
        lines = methods.split('\n')
        formatted_lines = []

        for line in lines:
            if line.strip():
                # Add proper class method indentation
                if line.strip().startswith('@classmethod') or line.strip().startswith('def '):
                    formatted_lines.append('    ' + line.strip())
                elif line.strip().startswith('"""') or line.strip().startswith("'''"):
                    formatted_lines.append('        ' + line.strip())
                elif line.strip().startswith('return '):
                    formatted_lines.append('        ' + line.strip())
                else:
                    # Content lines
                    formatted_lines.append('        ' + line.strip())
            else:
                formatted_lines.append('')

        return '\n'.join(formatted_lines)

    def _generate_convenience_functions(self) -> str:
        """Generate convenience functions for back cover methods."""
        return """
def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)
"""

    def _generate_complete_genre_file(self, genre: str) -> Optional[str]:
        """
        Generate a complete genre file for new genres.

        Args:
            genre: Genre name

        Returns:
            Complete file content or None if failed
        """
        # This would be a more complex implementation
        # For now, return None to focus on updating existing files
        console.print(f"  ⚠️ Creating new genre files not implemented yet for {genre}")
        return None


def main():
    """Main function to add back cover methods to all genre files."""
    console.print("[bold blue]🚀 Genre Back Cover Methods Generator[/bold blue]")
    console.print("=" * 60)

    generator = GenreBackCoverMethodsGenerator()

    # Check if Gemini client is available
    try:
        test_response = generator.gemini_client.generate_content("Test", max_tokens=10)
        if not test_response:
            console.print("❌ Gemini client not available. Please check your API keys.")
            return False
    except Exception as e:
        console.print(f"❌ Gemini client error: {e}")
        return False

    # Process all genres
    success = generator.process_all_genres()

    if success:
        console.print("\n🎉 Back cover methods generation completed successfully!")
        console.print("\n📋 Next Steps:")
        console.print("  1. Review the updated genre files")
        console.print("  2. Test back cover generation with different genres")
        console.print("  3. Update back_cover_generator.py to use genre-specific methods")
        console.print("  4. Make back cover image generation automatic")
    else:
        console.print("\n❌ Back cover methods generation failed.")

    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
