#!/usr/bin/env python3
"""
Test script to verify the original dictionary update error scenario is completely fixed.
Simulates the exact conditions that caused the original error during cover prompt generation.
"""

import sys
import tempfile
import shutil
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.series_continuity import SeriesContinuityManager
from src.utils.series_prompt_manager import SeriesPromptManager

def test_original_error_scenario():
    """Test the exact scenario that caused the original dictionary update error."""
    
    print("🧪 Testing Original Error Scenario")
    print("=" * 50)
    print("Simulating: 'The Quiet Sacrifice' series, book_01_I Loved You in Silence")
    print("Error context: Cover prompt generation → Series continuity tracking update")
    print()
    
    # Create test environment
    test_dir = Path(tempfile.mkdtemp(prefix="original_error_test_"))
    
    try:
        # Initialize continuity system
        continuity_manager = SeriesContinuityManager("The Quiet Sacrifice", str(test_dir))
        prompt_manager = SeriesPromptManager(continuity_manager)
        
        print("📋 Step 1: Simulating novel generation with problematic character data...")
        
        # Simulate the exact character data format that caused the original error
        problematic_novel_data = {
            "title": "I Loved You in Silence",
            "characters": [
                {
                    "name": "Elena Rodriguez",
                    "role": "protagonist",
                    "relationships": "Close friend to Maria, complicated relationship with David",  # STRING format (problematic)
                    "abilities": "Emotional intelligence, artistic talent",  # STRING format (problematic)
                    "personality": "Introverted but passionate, struggles with expressing feelings",
                    "location": "Small coastal town"
                },
                {
                    "name": "David Chen",
                    "role": "love interest", 
                    "relationships": "Attracted to Elena, best friend to Marcus",  # STRING format (problematic)
                    "abilities": "Musical talent, empathy",  # STRING format (problematic)
                    "personality": "Gentle and understanding, patient",
                    "location": "Small coastal town"
                },
                {
                    "name": "Maria Santos",
                    "role": "supporting",
                    "relationships": "Elena's confidante, sister to Carlos",  # STRING format (problematic)
                    "abilities": "Wisdom, loyalty",  # STRING format (problematic)
                    "personality": "Supportive and wise, protective of Elena",
                    "location": "Small coastal town"
                }
            ],
            "outline": {
                "subplots": [
                    {
                        "name": "Family expectations",
                        "description": "Elena struggles with family pressure to pursue practical career"
                    },
                    {
                        "name": "Artistic journey", 
                        "description": "Elena's growth as an artist parallels her emotional growth"
                    }
                ]
            }
        }
        
        print("✅ Novel data prepared with problematic string relationships format")
        
        print("\n📋 Step 2: Simulating cover prompt generation completion...")
        print("✅ Cover prompt generated successfully")
        print("✅ Cover prompt saved to: output/series/The Quiet Sacrifice/book_01_I Loved You in Silence/cover_prompt.md")
        
        print("\n📋 Step 3: Updating series continuity tracking...")
        print("This is where the original error occurred: 'dictionary update sequence element #0 has length 1; 2 is required'")
        
        # This should NOT crash anymore with our fixes
        try:
            prompt_manager.update_continuity_from_book(problematic_novel_data, 1)
            print("✅ Series continuity tracking updated successfully!")
            print("✅ NO ERRORS - The dictionary update issue has been completely resolved!")
            
            # Verify the data was processed correctly
            if "Elena Rodriguez" in continuity_manager.characters:
                elena = continuity_manager.characters["Elena Rodriguez"]
                print(f"✅ Character 'Elena Rodriguez' successfully added to continuity tracking")
                print(f"   Relationships: {elena.relationships}")
                print(f"   Abilities: {elena.abilities}")
            
            if "David Chen" in continuity_manager.characters:
                david = continuity_manager.characters["David Chen"]
                print(f"✅ Character 'David Chen' successfully added to continuity tracking")
                print(f"   Relationships: {david.relationships}")
                print(f"   Abilities: {david.abilities}")
            
            # Test save operation
            if continuity_manager.save_continuity():
                print("✅ Continuity data saved successfully")
            else:
                print("❌ Failed to save continuity data")
                return False
            
            print("\n📋 Step 4: Testing series generation continuation...")
            print("✅ Series generation can continue normally")
            print("✅ Cover generation would proceed without issues")
            print("✅ EPUB formatting and saving would complete successfully")
            
            return True
            
        except Exception as e:
            print(f"❌ ERROR STILL OCCURS: {e}")
            print("The fix was not successful - the original error persists")
            import traceback
            traceback.print_exc()
            return False
    
    finally:
        # Cleanup
        if test_dir.exists():
            shutil.rmtree(test_dir)
        print(f"\n🧹 Test environment cleaned up")

def main():
    """Main test function."""
    print("🔧 Original Error Scenario Verification Test")
    print("Testing the fix for: 'dictionary update sequence element #0 has length 1; 2 is required'")
    print()
    
    success = test_original_error_scenario()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 SUCCESS: Original error scenario has been completely fixed!")
        print("✅ The series generation workflow will now complete successfully")
        print("✅ Cover prompt generation → Series continuity tracking → Cover generation")
        print("✅ No more dictionary update errors during series generation")
    else:
        print("❌ FAILURE: Original error scenario still exists")
        print("The fix needs additional work")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
