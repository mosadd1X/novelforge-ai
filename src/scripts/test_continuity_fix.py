#!/usr/bin/env python3
"""
Test script to verify the series continuity tracking fix.
Tests various character data formats to ensure robust handling.
"""

import sys
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.series_continuity import SeriesContinuityManager
from src.utils.series_prompt_manager import SeriesPromptManager

def test_character_data_formats():
    """Test various character data formats that could cause the dictionary update error."""
    
    print("🧪 Testing Series Continuity Tracking Fix")
    print("=" * 50)
    
    # Create a temporary test directory
    test_dir = Path("test_output")
    test_dir.mkdir(exist_ok=True)
    
    # Initialize continuity manager
    continuity_manager = SeriesContinuityManager("Test Series", str(test_dir))
    prompt_manager = SeriesPromptManager(continuity_manager)
    
    # Test cases with different character data formats
    test_cases = [
        {
            "name": "String Relationships Format",
            "book_data": {
                "characters": [
                    {
                        "name": "Alice",
                        "role": "protagonist",
                        "relationships": "Close friend to Bob, rival to Carol",  # String format
                        "abilities": "Magic, Swordsmanship",  # String format
                        "personality": "Brave and determined"
                    }
                ]
            }
        },
        {
            "name": "Dictionary Relationships Format",
            "book_data": {
                "characters": [
                    {
                        "name": "Bob",
                        "role": "supporting",
                        "relationships": {"Alice": "friend", "Carol": "neutral"},  # Dict format
                        "abilities": ["Healing", "Archery"],  # List format
                        "personality": "Kind and loyal"
                    }
                ]
            }
        },
        {
            "name": "List Relationships Format",
            "book_data": {
                "characters": [
                    {
                        "name": "Carol",
                        "role": "antagonist",
                        "relationships": ["Enemy of Alice", "Distrusts Bob"],  # List format
                        "abilities": [],  # Empty list
                        "personality": "Cunning and ambitious"
                    }
                ]
            }
        },
        {
            "name": "Mixed/Problematic Format",
            "book_data": {
                "characters": [
                    {
                        "name": "Dave",
                        "role": "minor",
                        "relationships": None,  # None value
                        "abilities": None,  # None value
                        "personality": ""  # Empty string
                    }
                ]
            }
        },
        {
            "name": "Missing Fields Format",
            "book_data": {
                "characters": [
                    {
                        "name": "Eve",
                        "role": "mysterious"
                        # Missing relationships, abilities, personality
                    }
                ]
            }
        }
    ]
    
    # Run tests
    passed_tests = 0
    total_tests = len(test_cases)
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📋 Test {i}: {test_case['name']}")
        print("-" * 30)
        
        try:
            # This should not crash anymore
            prompt_manager.update_continuity_from_book(test_case["book_data"], i)
            print(f"✅ PASSED - No errors during continuity update")
            passed_tests += 1
            
            # Verify character was added
            char_name = test_case["book_data"]["characters"][0]["name"]
            if char_name in continuity_manager.characters:
                char = continuity_manager.characters[char_name]
                print(f"   Character '{char_name}' successfully added to continuity tracking")
                print(f"   Relationships: {char.relationships}")
                print(f"   Abilities: {char.abilities}")
            else:
                print(f"   Warning: Character '{char_name}' not found in continuity tracking")
                
        except Exception as e:
            print(f"❌ FAILED - Error: {e}")
            print(f"   This indicates the fix may not be complete")
    
    # Summary
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print("🎉 ALL TESTS PASSED! The continuity tracking fix is working correctly.")
        print("✅ The series generation should now handle various character data formats without crashing.")
    else:
        print("❌ Some tests failed. The fix may need additional work.")
    
    # Cleanup
    try:
        continuity_file = test_dir / "series_continuity.json"
        if continuity_file.exists():
            continuity_file.unlink()
        print(f"\n🧹 Cleaned up test files")
    except Exception as e:
        print(f"Warning: Could not clean up test files: {e}")

if __name__ == "__main__":
    test_character_data_formats()
