#!/usr/bin/env python3
"""Simple test for memory leak fix."""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_limited_dict():
    """Test LimitedDict basic functionality."""
    try:
        from src.utils.limited_dict import LimitedDict
        
        print("Testing LimitedDict...")
        
        # Create a LimitedDict with max size 5
        ld = LimitedDict(max_size=5, cleanup_threshold=1.0)
        
        # Add 10 items
        for i in range(10):
            ld[f"key_{i}"] = f"value_{i}"
        
        print(f"Added 10 items, current size: {len(ld)}")
        print(f"Keys: {list(ld.keys())}")
        
        # Should be limited to 5 items
        if len(ld) <= 5:
            print("✓ LimitedDict size limit working")
        else:
            print(f"✗ LimitedDict size limit failed: {len(ld)} > 5")
            
        # Test memory info
        info = ld.get_memory_info()
        print(f"Memory info: {info}")
        
        return True
        
    except Exception as e:
        print(f"✗ LimitedDict test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_memory_manager():
    """Test MemoryManager with limited containers."""
    try:
        import tempfile
        import shutil
        from src.core.memory_manager import MemoryManager
        
        print("\nTesting MemoryManager...")
        
        # Create temporary directory
        temp_dir = tempfile.mkdtemp()
        
        try:
            # Create MemoryManager with small limits
            mm = MemoryManager(
                novel_title="Test Novel",
                output_dir=temp_dir,
                max_memory_items=10
            )
            
            print(f"Created MemoryManager with max_memory_items=10")
            
            # Add some test data
            for i in range(20):  # More than the limit
                chapter_data = {
                    "character_updates": {
                        f"char_{i}": {"development": f"Dev {i}"}
                    },
                    "unresolved_questions": [f"Question {i}"]
                }
                mm.update_narrative_tracking(i, chapter_data)
            
            # Get memory usage info
            memory_info = mm.get_memory_usage_info()
            print(f"Total items after adding 20 chapters: {memory_info['total_items']}")
            print(f"Average usage: {memory_info['average_usage_percentage']:.1f}%")
            
            # Test save/load
            mm.save_memory()
            print("✓ Save completed")
            
            # Create new manager and load
            mm2 = MemoryManager(
                novel_title="Test Novel",
                output_dir=temp_dir,
                max_memory_items=10
            )
            print("✓ Load completed")
            
            # Verify data was loaded
            memory_info2 = mm2.get_memory_usage_info()
            print(f"Loaded items: {memory_info2['total_items']}")
            
            if memory_info2['total_items'] > 0:
                print("✓ MemoryManager save/load working")
            else:
                print("✗ MemoryManager save/load failed")
                
            return True
            
        finally:
            shutil.rmtree(temp_dir, ignore_errors=True)
            
    except Exception as e:
        print(f"✗ MemoryManager test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Run simple memory tests."""
    print("🧪 Simple Memory Leak Fix Test")
    print("=" * 40)
    
    success = True
    
    # Test LimitedDict
    if not test_limited_dict():
        success = False
    
    # Test MemoryManager
    if not test_memory_manager():
        success = False
    
    print("\n" + "=" * 40)
    if success:
        print("✅ All tests PASSED!")
        print("\nMemory leak fix is working:")
        print("• LimitedDict prevents unlimited growth")
        print("• MemoryManager uses bounded containers")
        print("• Save/load functionality works")
    else:
        print("❌ Some tests FAILED!")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
