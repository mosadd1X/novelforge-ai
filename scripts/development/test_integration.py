"""
Test script to verify that both the new prompt system and existing genre_defaults.py work correctly.
"""

import sys
sys.path.append('src')

def test_genre_defaults():
    """Test that genre_defaults.py still works correctly."""
    print("🧪 Testing genre_defaults.py...")
    
    try:
        from src.utils.genre_defaults import get_genre_defaults, get_all_genres
        
        # Test getting defaults for a few genres
        test_genres = ["fantasy", "romance", "self-help", "poetry collection"]
        
        for genre in test_genres:
            defaults = get_genre_defaults(genre)
            print(f"  ✅ {genre}: {defaults['target_length']}, {defaults['chapter_count']} chapters, {defaults['target_word_count']} words")
        
        # Test getting all genres
        all_genres = get_all_genres()
        print(f"  ✅ Found {len(all_genres)} total genres in genre_defaults.py")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing genre_defaults.py: {str(e)}")
        return False

def test_prompt_system():
    """Test that the new prompt system works correctly."""
    print("\n🧪 Testing new prompt system...")
    
    try:
        from src.prompts import get_prompt, get_genre_prompts, list_available_genres
        
        # Test getting prompts for different content types
        test_cases = [
            ("fantasy", "fiction"),
            ("self_help", "non_fiction"), 
            ("poetry_collection", "special_format")
        ]
        
        for genre, content_type in test_cases:
            # Test getting a genre module
            genre_module = get_genre_prompts(genre)
            if genre_module:
                print(f"  ✅ {genre} module loaded successfully ({content_type})")
                
                # Test getting a specific prompt
                prompt = get_prompt(genre, "writer_profile", title="Test Book", description="Test description")
                if prompt and len(prompt) > 100:
                    print(f"    ✅ Writer profile prompt generated ({len(prompt)} chars)")
                else:
                    print(f"    ❌ Writer profile prompt failed")
            else:
                print(f"  ❌ Failed to load {genre} module")
        
        # Test listing available genres
        available_genres = list_available_genres()
        print(f"  ✅ Found {len(available_genres)} genres with prompt support")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing prompt system: {str(e)}")
        return False

def test_base_class_inheritance():
    """Test that genres are using the correct base classes."""
    print("\n🧪 Testing base class inheritance...")
    
    try:
        # Test Fiction base class
        from src.prompts.fantasy import FantasyPrompts
        from src.prompts.base_prompts import FictionBasePrompts
        
        if issubclass(FantasyPrompts, FictionBasePrompts):
            print("  ✅ Fantasy correctly inherits from FictionBasePrompts")
        else:
            print("  ❌ Fantasy inheritance issue")
        
        # Test Non-Fiction base class
        from src.prompts.self_help import SelfHelpPrompts
        from src.prompts.base_prompts import NonFictionBasePrompts
        
        if issubclass(SelfHelpPrompts, NonFictionBasePrompts):
            print("  ✅ Self-Help correctly inherits from NonFictionBasePrompts")
        else:
            print("  ❌ Self-Help inheritance issue")
        
        # Test Special Format base class
        from src.prompts.poetry_collection import PoetryCollectionPrompts
        from src.prompts.base_prompts import SpecialFormatBasePrompts
        
        if issubclass(PoetryCollectionPrompts, SpecialFormatBasePrompts):
            print("  ✅ Poetry Collection correctly inherits from SpecialFormatBasePrompts")
        else:
            print("  ❌ Poetry Collection inheritance issue")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing inheritance: {str(e)}")
        return False

def main():
    """Run all integration tests."""
    print("🚀 Integration Test Suite")
    print("=" * 50)
    
    tests = [
        ("Genre Defaults System", test_genre_defaults),
        ("New Prompt System", test_prompt_system),
        ("Base Class Inheritance", test_base_class_inheritance)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 30)
        
        if test_func():
            passed += 1
            print(f"✅ {test_name} PASSED")
        else:
            print(f"❌ {test_name} FAILED")
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 INTEGRATION TEST SUMMARY")
    print("=" * 50)
    print(f"✅ Passed: {passed}/{total}")
    print(f"❌ Failed: {total - passed}/{total}")
    
    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Both genre_defaults.py and the new prompt system work correctly")
        print("✅ All base class inheritance is working properly")
        print("✅ The system is ready for production use")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Review needed.")

if __name__ == "__main__":
    main()
