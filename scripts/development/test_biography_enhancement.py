#!/usr/bin/env python3
"""
Test Biography Enhancement - Process 3 profiles first
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

def test_biography_enhancement():
    """Test biography enhancement with 3 profiles."""
    
    print("🧪 Testing Biography Enhancement System")
    print("=" * 50)
    
    # Initialize Gemini
    try:
        gemini_client = GeminiClient()
        print("✓ Gemini AI client initialized")
    except Exception as e:
        print(f"❌ Failed to initialize Gemini AI: {e}")
        return
    
    # Test with 3 specific profiles
    test_profiles = [
        "catherine_fairfax",
        "ananya_desai", 
        "hiroshi_nakamura"
    ]
    
    profiles_dir = Path("src/writer_profiles/master_profiles")
    
    for profile_name in test_profiles:
        print(f"\n📝 Testing: {profile_name}")
        
        try:
            # Load the profile
            module_name = f"src.writer_profiles.master_profiles.{profile_name}"
            module = importlib.import_module(module_name)
            profile_data = module.get_profile()
            
            print(f"  ✓ Profile loaded: {profile_data.get('name')}")
            
            # Create biography prompt
            name = profile_data.get("name", "Unknown Author")
            description = profile_data.get("description", "")
            cultural_background = profile_data.get("cultural_background", "")
            era = profile_data.get("era", "")
            primary_genres = profile_data.get("primary_genres", [])
            biographical_context = profile_data.get("biographical_context", "")
            
            profile_data_details = profile_data.get("profile_data", {})
            writing_style = profile_data_details.get("writing_style", "")
            literary_influences = profile_data_details.get("literary_influences", [])
            
            prompt = f"""
            Create a compelling, humanized author biography for the fictional writer "{name}". 
            Transform the technical profile data into an engaging 2-3 paragraph biographical narrative 
            suitable for the "About the Author" section of a book.

            WRITER PROFILE DATA:
            - Name: {name}
            - Cultural Background: {cultural_background}
            - Era: {era}
            - Primary Genres: {', '.join(primary_genres)}
            - Current Description: {description[:200]}...
            - Biographical Context: {biographical_context}
            - Writing Style: {writing_style[:200]}...
            - Literary Influences: {', '.join(literary_influences[:3]) if isinstance(literary_influences, list) else str(literary_influences)[:200]}

            REQUIREMENTS:
            1. Write in third person as a professional author biography
            2. Create 2-3 substantial paragraphs (150-250 words total)
            3. Include literary background, influences, and writing journey
            4. Reflect cultural authenticity and historical context
            5. Make it engaging for readers while maintaining the fictional nature
            6. Include specific details about their writing style and themes
            7. Mention their literary achievements and recognition (fictional but believable)
            8. Connect their personal background to their writing themes

            Generate ONLY the biography text, no additional commentary or formatting.
            """
            
            print(f"  📤 Sending prompt to Gemini AI...")
            
            # Generate biography
            response = gemini_client.generate_content(prompt)
            
            if response and len(response.strip()) > 100:
                biography = response.strip()
                print(f"  ✓ Biography generated ({len(biography)} characters)")
                
                # Display the biography
                print(f"\n📖 Generated Biography for {name}:")
                print("-" * 40)
                print(biography)
                print("-" * 40)
                
                # Test adding to file (dry run)
                file_path = profiles_dir / f"{profile_name}.py"
                print(f"\n🔧 Testing file modification for {file_path.name}...")
                
                # Read current content
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if function already exists
                if "def get_author_biography" in content:
                    print(f"  ⚠️  get_author_biography function already exists")
                else:
                    print(f"  ✓ Ready to add get_author_biography function")
                
                print(f"  ✓ File modification test successful")
                
            else:
                print(f"  ❌ Invalid response from Gemini")
                
        except Exception as e:
            print(f"  ❌ Error processing {profile_name}: {e}")
    
    print(f"\n🎉 Test completed! Ready to proceed with full enhancement.")

if __name__ == "__main__":
    test_biography_enhancement()
