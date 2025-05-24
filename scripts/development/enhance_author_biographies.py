#!/usr/bin/env python3
"""
Author Biography Enhancement System

This script analyzes all 27 fictional writer profiles and generates compelling
biographical narratives using Gemini AI, then adds them to each profile's Python file.
"""

import sys
import os
import importlib
import re
from pathlib import Path
from typing import Dict, Any, List, Optional

# Add src to path for imports
sys.path.append('src')

from core.gemini_client import GeminiClient

class AuthorBiographyEnhancer:
    """
    Enhances author profiles with compelling biographical narratives.
    """
    
    def __init__(self):
        """Initialize the biography enhancer."""
        self.profiles_dir = Path("src/writer_profiles/master_profiles")
        self.gemini_client = None
        self.enhanced_profiles = []
        
    def initialize_gemini(self):
        """Initialize Gemini AI client."""
        try:
            self.gemini_client = GeminiClient()
            print("✓ Gemini AI client initialized")
            return True
        except Exception as e:
            print(f"❌ Failed to initialize Gemini AI: {e}")
            return False
    
    def load_all_profiles(self) -> List[Dict[str, Any]]:
        """Load all writer profiles from the master_profiles directory."""
        profiles = []
        
        # Get all Python files in the directory
        profile_files = list(self.profiles_dir.glob("*.py"))
        profile_files = [f for f in profile_files if not f.name.startswith("__")]
        
        print(f"📚 Found {len(profile_files)} profile files")
        
        for profile_file in profile_files:
            try:
                # Import the module
                module_name = f"src.writer_profiles.master_profiles.{profile_file.stem}"
                module = importlib.import_module(module_name)
                
                # Get the profile data
                profile_data = module.get_profile()
                profile_data["_module_name"] = profile_file.stem
                profile_data["_file_path"] = profile_file
                
                profiles.append(profile_data)
                print(f"  ✓ Loaded: {profile_data.get('name', 'Unknown')}")
                
            except Exception as e:
                print(f"  ❌ Failed to load {profile_file.name}: {e}")
                continue
        
        return profiles
    
    def create_biography_prompt(self, profile: Dict[str, Any]) -> str:
        """Create a Gemini AI prompt for generating author biography."""
        
        name = profile.get("name", "Unknown Author")
        description = profile.get("description", "")
        cultural_background = profile.get("cultural_background", "")
        era = profile.get("era", "")
        primary_genres = profile.get("primary_genres", [])
        secondary_genres = profile.get("secondary_genres", [])
        biographical_context = profile.get("biographical_context", "")
        
        # Extract profile data details
        profile_data = profile.get("profile_data", {})
        writing_style = profile_data.get("writing_style", "")
        literary_influences = profile_data.get("literary_influences", [])
        thematic_focuses = profile_data.get("thematic_focuses", [])
        
        prompt = f"""
        Create a compelling, humanized author biography for the fictional writer "{name}". 
        Transform the technical profile data into an engaging 2-3 paragraph biographical narrative 
        suitable for the "About the Author" section of a book.

        WRITER PROFILE DATA:
        - Name: {name}
        - Cultural Background: {cultural_background}
        - Era: {era}
        - Primary Genres: {', '.join(primary_genres)}
        - Secondary Genres: {', '.join(secondary_genres)}
        - Current Description: {description}
        - Biographical Context: {biographical_context}
        - Writing Style: {writing_style}
        - Literary Influences: {', '.join(literary_influences) if isinstance(literary_influences, list) else str(literary_influences)}
        - Thematic Focuses: {', '.join(thematic_focuses) if isinstance(thematic_focuses, list) else str(thematic_focuses)}

        REQUIREMENTS:
        1. Write in third person as a professional author biography
        2. Create 2-3 substantial paragraphs (150-250 words total)
        3. Include literary background, influences, and writing journey
        4. Reflect cultural authenticity and historical context
        5. Make it engaging for readers while maintaining the fictional nature
        6. Include specific details about their writing style and themes
        7. Mention their literary achievements and recognition (fictional but believable)
        8. Connect their personal background to their writing themes

        STYLE GUIDELINES:
        - Professional but engaging tone
        - Specific and vivid details
        - Cultural sensitivity and authenticity
        - Literary sophistication appropriate for the genre
        - Avoid overly technical language
        - Make the author feel real and compelling

        Generate ONLY the biography text, no additional commentary or formatting.
        """
        
        return prompt
    
    def generate_biography(self, profile: Dict[str, Any]) -> Optional[str]:
        """Generate a biography for a single profile using Gemini AI."""
        
        if not self.gemini_client:
            print("❌ Gemini client not initialized")
            return None
        
        name = profile.get("name", "Unknown")
        print(f"📝 Generating biography for {name}...")
        
        try:
            prompt = self.create_biography_prompt(profile)
            response = self.gemini_client.generate_content(prompt)
            
            if response and len(response.strip()) > 100:
                print(f"  ✓ Biography generated ({len(response)} characters)")
                return response.strip()
            else:
                print(f"  ❌ Invalid response from Gemini")
                return None
                
        except Exception as e:
            print(f"  ❌ Error generating biography: {e}")
            return None
    
    def add_biography_to_profile(self, profile: Dict[str, Any], biography: str) -> bool:
        """Add the generated biography to the profile's Python file."""
        
        file_path = profile.get("_file_path")
        if not file_path or not file_path.exists():
            print(f"❌ Profile file not found: {file_path}")
            return False
        
        try:
            # Read the current file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Escape quotes in biography for Python string
            escaped_biography = biography.replace('"', '\\"').replace("'", "\\'")
            
            # Create the new function to add
            biography_function = f'''

def get_author_biography() -> str:
    """Returns a compelling author biography for the 'About the Author' section."""
    return """{escaped_biography}"""
'''
            
            # Check if the function already exists
            if "def get_author_biography" in content:
                # Replace existing function
                pattern = r'def get_author_biography\(\).*?return """.*?"""'
                replacement = f'def get_author_biography() -> str:\n    """Returns a compelling author biography for the \'About the Author\' section."""\n    return """{escaped_biography}"""'
                content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            else:
                # Add new function at the end of the file
                content += biography_function
            
            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✓ Biography added to {file_path.name}")
            return True
            
        except Exception as e:
            print(f"  ❌ Error updating file {file_path.name}: {e}")
            return False
    
    def enhance_all_profiles(self) -> Dict[str, Any]:
        """Enhance all profiles with biographical content."""
        
        print("🎭 Author Biography Enhancement System")
        print("=" * 60)
        
        # Initialize Gemini
        if not self.initialize_gemini():
            return {"success": False, "error": "Failed to initialize Gemini AI"}
        
        # Load all profiles
        profiles = self.load_all_profiles()
        if not profiles:
            return {"success": False, "error": "No profiles found"}
        
        print(f"\n📝 Generating biographies for {len(profiles)} authors...")
        
        results = {
            "total_profiles": len(profiles),
            "successful": 0,
            "failed": 0,
            "enhanced_authors": [],
            "failed_authors": []
        }
        
        for i, profile in enumerate(profiles, 1):
            name = profile.get("name", f"Profile {i}")
            print(f"\n[{i}/{len(profiles)}] Processing: {name}")
            
            # Generate biography
            biography = self.generate_biography(profile)
            
            if biography:
                # Add to profile file
                if self.add_biography_to_profile(profile, biography):
                    results["successful"] += 1
                    results["enhanced_authors"].append(name)
                    
                    # Store for summary
                    self.enhanced_profiles.append({
                        "name": name,
                        "biography": biography,
                        "cultural_background": profile.get("cultural_background", ""),
                        "era": profile.get("era", ""),
                        "genres": profile.get("primary_genres", [])
                    })
                else:
                    results["failed"] += 1
                    results["failed_authors"].append(name)
            else:
                results["failed"] += 1
                results["failed_authors"].append(name)
        
        results["success"] = True
        return results
    
    def create_summary_report(self, results: Dict[str, Any]) -> None:
        """Create a summary report of the enhancement process."""
        
        print(f"\n{'='*60}")
        print("BIOGRAPHY ENHANCEMENT COMPLETE")
        print(f"{'='*60}")
        
        print(f"📊 Total profiles: {results['total_profiles']}")
        print(f"✅ Successfully enhanced: {results['successful']}")
        print(f"❌ Failed: {results['failed']}")
        print(f"🎯 Success rate: {results['successful']/results['total_profiles']*100:.1f}%")
        
        if results["enhanced_authors"]:
            print(f"\n✅ Enhanced Authors:")
            for author in results["enhanced_authors"]:
                print(f"  • {author}")
        
        if results["failed_authors"]:
            print(f"\n❌ Failed Authors:")
            for author in results["failed_authors"]:
                print(f"  • {author}")
        
        # Create detailed summary file
        summary_content = f"""# Author Biography Enhancement Summary

## Results Overview
- **Total Profiles**: {results['total_profiles']}
- **Successfully Enhanced**: {results['successful']}
- **Failed**: {results['failed']}
- **Success Rate**: {results['successful']/results['total_profiles']*100:.1f}%

## Enhanced Authors
"""
        
        for profile in self.enhanced_profiles:
            summary_content += f"""
### {profile['name']}
- **Cultural Background**: {profile['cultural_background']}
- **Era**: {profile['era']}
- **Genres**: {', '.join(profile['genres'])}

**Biography Preview**:
{profile['biography'][:200]}...

---
"""
        
        # Save summary to file
        summary_path = Path("author_biography_enhancement_summary.md")
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(summary_content)
        
        print(f"\n📄 Detailed summary saved to: {summary_path}")

def main():
    """Main function to run the biography enhancement process."""
    
    enhancer = AuthorBiographyEnhancer()
    results = enhancer.enhance_all_profiles()
    
    if results["success"]:
        enhancer.create_summary_report(results)
        
        if results["successful"] > 0:
            print(f"\n🎉 Biography enhancement completed successfully!")
            print(f"✅ {results['successful']} authors now have compelling biographies")
            print(f"📚 Ready for integration with back matter system")
        else:
            print(f"\n⚠️ No biographies were generated successfully")
    else:
        print(f"\n❌ Enhancement process failed: {results.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
