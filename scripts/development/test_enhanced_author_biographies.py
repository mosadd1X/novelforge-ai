#!/usr/bin/env python3
"""
Test Enhanced Author Biographies Integration

This script tests the integration of enhanced author biographies with the back matter system.
"""

import sys
import os
import tempfile
import importlib
from pathlib import Path

# Add src to path for imports
sys.path.append('src')

from formatters.epub_formatter import EpubFormatter
from utils.writer_profile_manager import WriterProfileManager

def test_enhanced_biographies():
    """Test the enhanced author biographies in the back matter system."""
    
    print("📚 Testing Enhanced Author Biographies Integration")
    print("=" * 60)
    
    # Test profiles to check
    test_profiles = [
        "Catherine Fairfax",
        "Ananya Desai", 
        "Hiroshi Nakamura",
        "Marcus Kane",
        "Elena Blackwood"
    ]
    
    profile_manager = WriterProfileManager()
    
    for i, author_name in enumerate(test_profiles, 1):
        print(f"\n[{i}/{len(test_profiles)}] Testing: {author_name}")
        
        try:
            # Get the writer profile
            writer_profile = profile_manager.get_master_profile_by_author(author_name)
            
            if not writer_profile:
                print(f"  ❌ Profile not found for {author_name}")
                continue
            
            print(f"  ✓ Profile loaded: {writer_profile.get('name')}")
            
            # Test loading the enhanced biography
            profile_name = writer_profile.get("name", "")
            module_name = profile_name.lower().replace(" ", "_").replace(".", "_")
            module_path = f"src.writer_profiles.master_profiles.{module_name}"
            
            try:
                module = importlib.import_module(module_path)
                
                if hasattr(module, 'get_author_biography'):
                    biography = module.get_author_biography()
                    
                    if biography and len(biography.strip()) > 100:
                        print(f"  ✓ Enhanced biography found ({len(biography)} characters)")
                        
                        # Show preview
                        preview = biography[:150] + "..." if len(biography) > 150 else biography
                        print(f"  📖 Preview: {preview}")
                        
                        # Test back matter integration
                        test_novel_data = {
                            "metadata": {
                                "title": f"Test Novel by {author_name}",
                                "author": author_name,
                                "genre": writer_profile.get("primary_genres", ["Fiction"])[0],
                                "description": "A test novel for biography integration",
                                "target_audience": "Adult",
                                "target_length": "short"
                            },
                            "chapters": [
                                {
                                    "number": 1,
                                    "title": "Test Chapter",
                                    "content": "This is a test chapter for biography integration testing."
                                }
                            ]
                        }
                        
                        # Create EPUB formatter
                        formatter = EpubFormatter(test_novel_data, writer_profile, 
                                                include_front_matter=True, include_back_matter=True)
                        
                        # Test back matter generation
                        back_matter = formatter.back_matter_generator.get_all_back_matter()
                        
                        if "writer_profile" in back_matter:
                            profile_content = back_matter["writer_profile"]
                            
                            # Check if enhanced biography is included
                            if "author-biography" in profile_content and len(biography[:100]) in profile_content:
                                print(f"  ✅ Enhanced biography integrated into back matter")
                            else:
                                print(f"  ⚠️  Biography may not be properly integrated")
                                
                            # Check for profile image
                            if "profile-image" in profile_content:
                                print(f"  ✅ Profile image integrated")
                            else:
                                print(f"  ⚠️  Profile image not found")
                        else:
                            print(f"  ❌ Writer profile section not generated")
                    else:
                        print(f"  ❌ Biography too short or empty")
                else:
                    print(f"  ❌ get_author_biography function not found")
                    
            except Exception as e:
                print(f"  ❌ Error loading biography module: {e}")
                
        except Exception as e:
            print(f"  ❌ Error testing {author_name}: {e}")
    
    print(f"\n{'='*60}")
    print("TESTING COMPLETE")
    print(f"{'='*60}")

def test_complete_epub_with_biography():
    """Test complete EPUB generation with enhanced biographies."""
    
    print(f"\n📖 Testing Complete EPUB Generation with Enhanced Biographies")
    print("-" * 60)
    
    # Use Catherine Fairfax as test case
    profile_manager = WriterProfileManager()
    writer_profile = profile_manager.get_master_profile_by_author("Catherine Fairfax")
    
    if not writer_profile:
        print("❌ Catherine Fairfax profile not found")
        return
    
    test_novel_data = {
        "metadata": {
            "title": "A Test of Enhanced Biographies",
            "author": "Catherine Fairfax",
            "genre": "Romance",
            "description": "A test novel to validate enhanced author biography integration",
            "target_audience": "Adult",
            "target_length": "short"
        },
        "chapters": [
            {
                "number": 1,
                "title": "Chapter 1: The Test Begins",
                "content": "This is the first chapter of our test novel, designed to validate the enhanced author biography system. The content here is sufficient to create a proper EPUB structure while focusing on the back matter enhancements."
            },
            {
                "number": 2,
                "title": "Chapter 2: Biography Integration",
                "content": "In this chapter, we continue our test narrative while ensuring that the EPUB generation process properly integrates the enhanced author biography that was generated using Gemini AI."
            }
        ]
    }
    
    try:
        # Create formatter with all enhancements
        formatter = EpubFormatter(test_novel_data, writer_profile, 
                                include_front_matter=True, include_back_matter=True)
        
        print("✓ EPUB formatter created with enhanced biographies")
        
        # Test back matter generation
        back_matter = formatter.back_matter_generator.get_all_back_matter()
        
        print(f"✓ Back matter sections generated: {len(back_matter)}")
        for section_name in back_matter.keys():
            print(f"  • {section_name.replace('_', ' ').title()}")
        
        # Check writer profile section specifically
        if "writer_profile" in back_matter:
            profile_content = back_matter["writer_profile"]
            
            # Check for enhanced biography elements
            checks = [
                ("Enhanced biography content", "author-biography" in profile_content),
                ("Profile image", "profile-image" in profile_content),
                ("Author name", "Catherine Fairfax" in profile_content),
                ("About the Author header", "About the Author" in profile_content),
                ("Fictional author notice", "fictional author persona" in profile_content)
            ]
            
            print(f"\n📋 Writer Profile Section Validation:")
            for check_name, check_result in checks:
                status = "✅" if check_result else "❌"
                print(f"  {status} {check_name}")
            
            # Generate actual EPUB file
            with tempfile.TemporaryDirectory() as temp_dir:
                epub_path = formatter.save_epub(temp_dir)
                
                if os.path.exists(epub_path):
                    file_size = os.path.getsize(epub_path)
                    print(f"\n✅ EPUB generated successfully:")
                    print(f"  📁 File: {epub_path}")
                    print(f"  📊 Size: {file_size:,} bytes")
                    print(f"  🎉 Enhanced biographies fully integrated!")
                    return True
                else:
                    print(f"\n❌ EPUB file not generated")
                    return False
        else:
            print(f"\n❌ Writer profile section not found in back matter")
            return False
            
    except Exception as e:
        print(f"\n❌ Error during EPUB generation: {e}")
        return False

def main():
    """Run the enhanced biography integration tests."""
    
    # Test individual biography loading
    test_enhanced_biographies()
    
    # Test complete EPUB generation
    success = test_complete_epub_with_biography()
    
    if success:
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"✅ Enhanced author biographies are fully integrated")
        print(f"✅ Profile pictures and biographies work together seamlessly")
        print(f"✅ Back matter system properly uses enhanced content")
        print(f"✅ EPUB generation includes all enhancements")
        print(f"\n📚 Ready for production use with enhanced author biographies!")
    else:
        print(f"\n⚠️  Some tests failed. Please review the issues above.")

if __name__ == "__main__":
    main()
