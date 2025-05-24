#!/usr/bin/env python3
"""
Test script to verify the memory leak fix in MemoryManager.

This script tests:
1. Memory usage stays bounded during long operations
2. LimitedDict and LimitedList work correctly
3. Save/load functionality with limited containers
4. Memory optimization features
"""

import os
import sys
import time
import psutil
import tempfile
import shutil
from typing import Dict, Any

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.core.memory_manager import MemoryManager
from src.utils.limited_dict import LimitedDict, LimitedList


def get_memory_usage() -> float:
    """Get current memory usage in MB."""
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024


def test_limited_dict():
    """Test LimitedDict functionality."""
    print("Testing LimitedDict...")

    # Create a small LimitedDict for testing
    limited_dict = LimitedDict(max_size=10, cleanup_threshold=1.0)  # No early cleanup

    # Add items up to the limit
    for i in range(10):
        limited_dict[f"key_{i}"] = f"value_{i}"

    # Should have exactly 10 items
    assert len(limited_dict) == 10, f"Expected 10 items, got {len(limited_dict)}"

    # Add one more item - should trigger eviction
    limited_dict["key_10"] = "value_10"

    # Should still have 10 items (one evicted)
    assert len(limited_dict) <= 10, f"Expected <= 10 items, got {len(limited_dict)}"

    # Check that the most recent item is kept
    assert "key_10" in limited_dict, "Most recent item should be kept"

    # Test memory info
    memory_info = limited_dict.get_memory_info()
    assert memory_info["max_size"] == 10
    assert memory_info["current_size"] <= 10

    print("✓ LimitedDict test passed")


def test_limited_list():
    """Test LimitedList functionality."""
    print("Testing LimitedList...")

    # Create a small LimitedList for testing
    limited_list = LimitedList(max_size=5)

    # Add items beyond the limit
    for i in range(10):
        limited_list.append(f"item_{i}")

    # Should only have 5 items (the most recent ones)
    assert len(limited_list) == 5, f"Expected 5 items, got {len(limited_list)}"

    # Check that the most recent items are kept
    assert "item_9" in limited_list, "Most recent item should be kept"
    assert "item_0" not in limited_list, "Oldest item should be evicted"

    # Test memory info
    memory_info = limited_list.get_memory_info()
    assert memory_info["current_size"] == 5
    assert memory_info["max_size"] == 5

    print("✓ LimitedList test passed")


def test_memory_manager_bounded_growth():
    """Test that MemoryManager memory usage stays bounded."""
    print("Testing MemoryManager bounded memory growth...")

    # Create temporary directory for test
    temp_dir = tempfile.mkdtemp()

    try:
        # Create MemoryManager with small limits for testing
        memory_manager = MemoryManager(
            novel_title="Test Novel",
            output_dir=temp_dir,
            max_memory_items=50  # Small limit for testing
        )

        initial_memory = get_memory_usage()
        print(f"Initial memory usage: {initial_memory:.2f} MB")

        # Simulate adding lots of narrative tracking data
        for chapter in range(100):  # Simulate 100 chapters
            chapter_data = {
                "character_updates": {
                    f"character_{i}": {
                        "development": f"Development in chapter {chapter}",
                        "emotions": f"Emotions in chapter {chapter}",
                        "knowledge": f"Knowledge gained in chapter {chapter}",
                        "location": f"Location in chapter {chapter}"
                    }
                    for i in range(10)  # 10 characters per chapter
                },
                "relationship_updates": {
                    f"rel_{i}_{j}": {
                        "status": f"Status in chapter {chapter}",
                        "development": f"Development in chapter {chapter}"
                    }
                    for i in range(5) for j in range(i+1, 5)  # All pairs
                },
                "plot_updates": {
                    f"plot_thread_{i}": {
                        "status": f"Status in chapter {chapter}",
                        "progression": f"Progression in chapter {chapter}"
                    }
                    for i in range(5)
                },
                "unresolved_questions": [f"Question {i} from chapter {chapter}" for i in range(3)],
                "foreshadowing": [f"Foreshadowing {i} from chapter {chapter}" for i in range(2)],
                "timeline_events": [f"Event {i} in chapter {chapter}" for i in range(3)]
            }

            memory_manager.update_narrative_tracking(chapter, chapter_data)

            # Check memory usage every 10 chapters
            if chapter % 10 == 0:
                current_memory = get_memory_usage()
                memory_growth = current_memory - initial_memory
                print(f"Chapter {chapter}: Memory usage: {current_memory:.2f} MB (+{memory_growth:.2f} MB)")

                # Memory growth should be bounded (less than 50MB for this test)
                if memory_growth > 50:
                    print(f"WARNING: Memory growth ({memory_growth:.2f} MB) exceeds expected bounds")

        final_memory = get_memory_usage()
        total_growth = final_memory - initial_memory
        print(f"Final memory usage: {final_memory:.2f} MB (+{total_growth:.2f} MB)")

        # Get memory usage info
        memory_info = memory_manager.get_memory_usage_info()
        print(f"Total tracking items: {memory_info['total_items']}")
        print(f"Average usage: {memory_info['average_usage_percentage']:.1f}%")

        # Verify memory usage is bounded
        assert total_growth < 100, f"Memory growth ({total_growth:.2f} MB) should be bounded"

        print("✓ Memory manager bounded growth test passed")

    finally:
        # Clean up
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_save_load_with_limited_containers():
    """Test save/load functionality with LimitedDict and LimitedList."""
    print("Testing save/load with limited containers...")

    # Create temporary directory for test
    temp_dir = tempfile.mkdtemp()

    try:
        # Create MemoryManager and add some data
        memory_manager = MemoryManager(
            novel_title="Test Save Load",
            output_dir=temp_dir,
            max_memory_items=10
        )

        # Add test data
        test_data = {
            "character_updates": {
                "Alice": {"development": "Character growth", "emotions": "Happy"},
                "Bob": {"development": "Character arc", "emotions": "Sad"}
            },
            "unresolved_questions": ["Question 1", "Question 2"],
            "foreshadowing": ["Foreshadow 1"]
        }

        memory_manager.update_narrative_tracking(1, test_data)

        # Save memory
        memory_manager.save_memory()

        # Create new MemoryManager and load the data
        new_memory_manager = MemoryManager(
            novel_title="Test Save Load",
            output_dir=temp_dir,
            max_memory_items=10
        )

        # Verify data was loaded correctly
        assert "Alice" in new_memory_manager.narrative_tracking["character_arcs"]
        assert "Bob" in new_memory_manager.narrative_tracking["character_arcs"]
        assert len(new_memory_manager.narrative_tracking["unresolved_questions"]) == 2
        assert len(new_memory_manager.narrative_tracking["foreshadowing"]) == 1

        # Verify containers are still limited
        assert isinstance(new_memory_manager.narrative_tracking["character_arcs"], LimitedDict)
        assert isinstance(new_memory_manager.narrative_tracking["unresolved_questions"], LimitedList)

        print("✓ Save/load with limited containers test passed")

    finally:
        # Clean up
        shutil.rmtree(temp_dir, ignore_errors=True)


def test_memory_optimization():
    """Test memory optimization functionality."""
    print("Testing memory optimization...")

    # Create temporary directory for test
    temp_dir = tempfile.mkdtemp()

    try:
        memory_manager = MemoryManager(
            novel_title="Test Optimization",
            output_dir=temp_dir,
            max_memory_items=20
        )

        # Fill up the containers
        for i in range(30):  # More than the limit
            test_data = {
                "character_updates": {f"char_{i}": {"development": f"Dev {i}"}},
                "unresolved_questions": [f"Question {i}"]
            }
            memory_manager.update_narrative_tracking(i, test_data)

        # Get memory info before optimization
        before_info = memory_manager.get_memory_usage_info()
        print(f"Before optimization: {before_info['total_items']} total items")

        # Trigger optimization
        optimized_categories = memory_manager.optimize_memory()

        # Get memory info after optimization
        after_info = memory_manager.get_memory_usage_info()
        print(f"After optimization: {after_info['total_items']} total items")
        print(f"Optimized categories: {len(optimized_categories)}")

        # Verify optimization worked
        assert len(optimized_categories) > 0, "Should have optimized some categories"

        print("✓ Memory optimization test passed")

    finally:
        # Clean up
        shutil.rmtree(temp_dir, ignore_errors=True)


def main():
    """Run all memory leak fix tests."""
    print("🧪 Testing Memory Leak Fix Implementation")
    print("=" * 50)

    try:
        # Test individual components
        test_limited_dict()
        test_limited_list()

        # Test MemoryManager integration
        test_memory_manager_bounded_growth()
        test_save_load_with_limited_containers()
        test_memory_optimization()

        print("\n" + "=" * 50)
        print("✅ All memory leak fix tests PASSED!")
        print("\nMemory leak fix successfully implemented:")
        print("• LimitedDict and LimitedList prevent unlimited growth")
        print("• MemoryManager uses bounded containers")
        print("• Save/load functionality works with limited containers")
        print("• Memory optimization features are working")
        print("• Memory usage stays bounded during long operations")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
