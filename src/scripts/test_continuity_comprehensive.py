#!/usr/bin/env python3
"""
Comprehensive test suite for the enhanced series continuity tracking system.
Tests all critical functionality including validation, error handling, and edge cases.
"""

import sys
import json
import tempfile
import shutil
from pathlib import Path
from typing import Dict

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.utils.series_continuity import SeriesContinuityManager
from src.utils.series_prompt_manager import SeriesPromptManager

class ContinuityTestSuite:
    """Comprehensive test suite for series continuity tracking."""

    def __init__(self):
        self.test_dir = None
        self.continuity_manager = None
        self.prompt_manager = None
        self.passed_tests = 0
        self.total_tests = 0

    def setup_test_environment(self):
        """Set up a temporary test environment."""
        self.test_dir = Path(tempfile.mkdtemp(prefix="continuity_test_"))
        self.continuity_manager = SeriesContinuityManager("Test Series", str(self.test_dir))
        self.prompt_manager = SeriesPromptManager(self.continuity_manager)
        print(f"🧪 Test environment created: {self.test_dir}")

    def cleanup_test_environment(self):
        """Clean up the test environment."""
        if self.test_dir and self.test_dir.exists():
            shutil.rmtree(self.test_dir)
            print(f"🧹 Test environment cleaned up")

    def run_test(self, test_name: str, test_func):
        """Run a single test with error handling."""
        self.total_tests += 1
        print(f"\n📋 Test {self.total_tests}: {test_name}")
        print("-" * 50)

        try:
            result = test_func()
            if result:
                print(f"✅ PASSED")
                self.passed_tests += 1
            else:
                print(f"❌ FAILED")
        except Exception as e:
            print(f"❌ FAILED with exception: {e}")
            import traceback
            traceback.print_exc()

    def test_input_validation(self) -> bool:
        """Test input validation for all add methods."""
        print("Testing input validation...")

        # Test invalid character inputs
        char1 = self.continuity_manager.add_character("", "alive", "home")  # Empty name
        char2 = self.continuity_manager.add_character(None, "alive", "home")  # None name
        char3 = self.continuity_manager.add_character("Valid", "", "home")  # Empty status
        char4 = self.continuity_manager.add_character("Valid", "alive", "")  # Empty location

        if char1 is not None or char2 is not None or char3 is not None or char4 is not None:
            print("Character validation failed - invalid inputs were accepted")
            return False

        # Test invalid plot thread inputs
        thread1 = self.continuity_manager.add_plot_thread("", "name", "desc")  # Empty ID
        thread2 = self.continuity_manager.add_plot_thread("id", "", "desc")  # Empty name
        thread3 = self.continuity_manager.add_plot_thread("id", "name", "")  # Empty description
        thread4 = self.continuity_manager.add_plot_thread("id", "name", "desc", "invalid")  # Invalid importance

        if thread1 is not None or thread2 is not None or thread3 is not None or thread4 is not None:
            print("Plot thread validation failed - invalid inputs were accepted")
            return False

        # Test invalid world element inputs
        element1 = self.continuity_manager.add_world_element("", "name", "type", "desc")  # Empty ID
        element2 = self.continuity_manager.add_world_element("id", "", "type", "desc")  # Empty name
        element3 = self.continuity_manager.add_world_element("id", "name", "", "desc")  # Empty type
        element4 = self.continuity_manager.add_world_element("id", "name", "type", "")  # Empty description

        if element1 is not None or element2 is not None or element3 is not None or element4 is not None:
            print("World element validation failed - invalid inputs were accepted")
            return False

        print("All input validation tests passed")
        return True

    def test_valid_data_creation(self) -> bool:
        """Test creation of valid data objects."""
        print("Testing valid data creation...")

        # Test valid character creation
        char = self.continuity_manager.add_character("Alice", "alive", "Castle", 1)
        if not char or char.name != "Alice":
            print("Valid character creation failed")
            return False

        # Test valid plot thread creation
        thread = self.continuity_manager.add_plot_thread("main_quest", "The Main Quest", "Save the world", "major", 1)
        if not thread or thread.thread_id != "main_quest":
            print("Valid plot thread creation failed")
            return False

        # Test valid world element creation
        element = self.continuity_manager.add_world_element("castle", "Royal Castle", "location", "A grand castle", 1)
        if not element or element.element_id != "castle":
            print("Valid world element creation failed")
            return False

        print("All valid data creation tests passed")
        return True

    def test_save_load_cycle(self) -> bool:
        """Test save and load functionality."""
        print("Testing save/load cycle...")

        # Add some test data
        self.continuity_manager.add_character("Bob", "alive", "Village", 1)
        self.continuity_manager.add_plot_thread("subplot", "Romance", "Love story", "minor", 1)
        self.continuity_manager.add_world_element("village", "Peaceful Village", "location", "A quiet place", 1)

        # Save data
        if not self.continuity_manager.save_continuity():
            print("Save operation failed")
            return False

        # Create new manager and load data
        new_manager = SeriesContinuityManager("Test Series", str(self.test_dir))
        if not new_manager.load_continuity():
            print("Load operation failed")
            return False

        # Verify data was loaded correctly
        if "Bob" not in new_manager.characters:
            print("Character data not loaded correctly")
            return False

        if "subplot" not in new_manager.plot_threads:
            print("Plot thread data not loaded correctly")
            return False

        if "village" not in new_manager.world_elements:
            print("World element data not loaded correctly")
            return False

        print("Save/load cycle test passed")
        return True

    def test_corrupted_data_recovery(self) -> bool:
        """Test recovery from corrupted data files."""
        print("Testing corrupted data recovery...")

        # Create valid data first
        self.continuity_manager.add_character("Carol", "alive", "Forest", 1)
        self.continuity_manager.save_continuity()

        # Corrupt the data file
        continuity_file = self.test_dir / "series_continuity.json"
        with open(continuity_file, 'w') as f:
            f.write("{ invalid json content }")

        # Try to load corrupted data
        new_manager = SeriesContinuityManager("Test Series", str(self.test_dir))
        result = new_manager.load_continuity()

        # Should either recover from backup or create minimal state
        if result is False:
            print("Recovery mechanism failed completely")
            return False

        print("Corrupted data recovery test passed")
        return True

    def test_character_data_formats(self) -> bool:
        """Test handling of various character data formats in prompt manager."""
        print("Testing character data format handling...")

        test_cases = [
            {
                "name": "String relationships",
                "characters": [{
                    "name": "Dave",
                    "relationships": "Friend to Alice, enemy to Bob",
                    "abilities": "Magic, Swordsmanship"
                }]
            },
            {
                "name": "Dict relationships",
                "characters": [{
                    "name": "Eve",
                    "relationships": {"Alice": "friend", "Bob": "enemy"},
                    "abilities": ["Magic", "Healing"]
                }]
            },
            {
                "name": "None values",
                "characters": [{
                    "name": "Frank",
                    "relationships": None,
                    "abilities": None
                }]
            }
        ]

        for i, test_case in enumerate(test_cases, 1):
            try:
                book_data = {"characters": test_case["characters"]}
                self.prompt_manager.update_continuity_from_book(book_data, i)
                print(f"  ✓ {test_case['name']} format handled correctly")
            except Exception as e:
                print(f"  ✗ {test_case['name']} format failed: {e}")
                return False

        print("Character data format handling test passed")
        return True

    def test_memory_management(self) -> bool:
        """Test memory management with large datasets."""
        print("Testing memory management...")

        # Create a fresh manager for this test to avoid contamination
        import tempfile
        fresh_test_dir = Path(tempfile.mkdtemp(prefix="memory_test_"))
        fresh_manager = SeriesContinuityManager("Memory Test Series", str(fresh_test_dir))

        try:
            # Create a large number of characters, plot threads, and world elements
            for i in range(100):
                char = fresh_manager.add_character(f"Character_{i}", "alive", f"Location_{i}", 1)
                thread = fresh_manager.add_plot_thread(f"thread_{i}", f"Thread {i}", f"Description {i}", "minor", 1)
                element = fresh_manager.add_world_element(f"element_{i}", f"Element {i}", "location", f"Description {i}", 1)

                if not char or not thread or not element:
                    print(f"Failed to create objects at iteration {i}")
                    return False

            # Test save/load with large dataset
            if not fresh_manager.save_continuity():
                print("Failed to save large dataset")
                return False

            # Verify all data is present
            if len(fresh_manager.characters) != 100:
                print(f"Expected 100 characters, got {len(fresh_manager.characters)}")
                return False

            if len(fresh_manager.plot_threads) != 100:
                print(f"Expected 100 plot threads, got {len(fresh_manager.plot_threads)}")
                return False

            if len(fresh_manager.world_elements) != 100:
                print(f"Expected 100 world elements, got {len(fresh_manager.world_elements)}")
                return False

            print("Memory management test passed")
            return True

        finally:
            # Clean up the fresh test directory
            if fresh_test_dir.exists():
                shutil.rmtree(fresh_test_dir)

    def test_atomic_save_operations(self) -> bool:
        """Test atomic save operations and backup creation."""
        print("Testing atomic save operations...")

        # Add initial data
        self.continuity_manager.add_character("Test", "alive", "Home", 1)
        self.continuity_manager.save_continuity()

        # Verify backup directory is created
        backup_dir = self.test_dir / "backups"
        if not backup_dir.exists():
            print("Backup directory not created")
            return False

        # Verify main file exists
        continuity_file = self.test_dir / "series_continuity.json"
        if not continuity_file.exists():
            print("Main continuity file not created")
            return False

        # Verify file content is valid JSON
        try:
            with open(continuity_file, 'r') as f:
                data = json.load(f)
            if 'characters' not in data:
                print("Saved data structure is invalid")
                return False
        except json.JSONDecodeError:
            print("Saved file is not valid JSON")
            return False

        print("Atomic save operations test passed")
        return True

    def run_all_tests(self):
        """Run all tests in the suite."""
        print("🧪 Starting Comprehensive Series Continuity Test Suite")
        print("=" * 60)

        self.setup_test_environment()

        try:
            # Run all tests
            self.run_test("Input Validation", self.test_input_validation)
            self.run_test("Valid Data Creation", self.test_valid_data_creation)
            self.run_test("Save/Load Cycle", self.test_save_load_cycle)
            self.run_test("Corrupted Data Recovery", self.test_corrupted_data_recovery)
            self.run_test("Character Data Formats", self.test_character_data_formats)
            self.run_test("Memory Management", self.test_memory_management)
            self.run_test("Atomic Save Operations", self.test_atomic_save_operations)

            # Summary
            print("\n" + "=" * 60)
            print(f"📊 Test Results: {self.passed_tests}/{self.total_tests} tests passed")

            if self.passed_tests == self.total_tests:
                print("🎉 ALL TESTS PASSED! The enhanced continuity system is working correctly.")
                print("✅ The series generation should now be robust against all tested edge cases.")
                return True
            else:
                print("❌ Some tests failed. The system may need additional fixes.")
                return False

        finally:
            self.cleanup_test_environment()

if __name__ == "__main__":
    test_suite = ContinuityTestSuite()
    success = test_suite.run_all_tests()
    sys.exit(0 if success else 1)
