#!/usr/bin/env python3
"""
Quick Validation Test for NovelForge AI

This script performs a rapid validation of the NovelForge AI system
to ensure all recent changes are working correctly.
"""

import sys
import os
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_basic_imports():
    """Test basic system imports."""
    print("🧪 Testing Basic Imports...")
    
    try:
        # Test terminal UI
        from src.ui.terminal_ui import clear_screen, display_title, custom_style
        print("  ✅ Terminal UI: OK")
        
        # Test database system
        from src.database.database_manager import get_database_manager
        from src.database.schema_migrator import SchemaMigrator
        print("  ✅ Database system: OK")
        
        # Test core generators
        from src.core.novel_generator import NovelGenerator
        from src.core.series_generator import SeriesGenerator
        print("  ✅ Core generators: OK")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Import error: {e}")
        return False

def test_new_modules():
    """Test newly implemented modules."""
    print("\n🧪 Testing New Modules...")
    
    modules_to_test = [
        ("Cover Management", "src.ui.cover_management", "cover_management_menu"),
        ("Format & Export", "src.ui.format_export", "format_export_menu"),
        ("Enhanced Series Workflows", "src.ui.enhanced_series_workflows", "enhanced_series_workflows_menu"),
        ("One-Click Publishing", "src.ui.one_click_publishing", "one_click_publishing_menu"),
        ("Smart Recommendations", "src.ui.smart_workflow_recommendations", "smart_workflow_recommendations_menu"),
        ("Batch Operations", "src.ui.batch_operations", "batch_cover_generation_menu")
    ]
    
    all_passed = True
    
    for name, module_path, function_name in modules_to_test:
        try:
            module = __import__(module_path, fromlist=[function_name])
            getattr(module, function_name)
            print(f"  ✅ {name}: OK")
        except Exception as e:
            print(f"  ❌ {name}: {e}")
            all_passed = False
    
    return all_passed

def test_database_system():
    """Test database system and schema."""
    print("\n🧪 Testing Database System...")
    
    try:
        # Test database manager
        from src.database.database_manager import get_database_manager
        db_manager = get_database_manager()
        stats = db_manager.get_database_stats()
        print(f"  ✅ Database Manager: {stats['total_books']} books")
        
        # Test schema version
        from src.database.schema_migrator import SchemaMigrator
        migrator = SchemaMigrator("data/novelforge_ai.db")
        version = migrator.get_current_schema_version()
        print(f"  ✅ Schema Version: v{version}")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Database error: {e}")
        return False

def test_main_application():
    """Test main application entry point."""
    print("\n🧪 Testing Main Application...")
    
    try:
        import run
        from run import content_creation_menu, library_management_menu
        print("  ✅ Main application: OK")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Main application error: {e}")
        return False

def test_batch_operations():
    """Test specific batch operation functions."""
    print("\n🧪 Testing Batch Operations...")
    
    try:
        from src.ui.batch_operations import (
            batch_cover_generation_menu,
            batch_epub_generation_menu,
            batch_export_menu,
            complete_all_unfinished_books_workflow
        )
        print("  ✅ All batch operation functions: OK")
        
        return True
        
    except Exception as e:
        print(f"  ❌ Batch operations error: {e}")
        return False

def main():
    """Run quick validation tests."""
    print("🚀 NovelForge AI Quick Validation Test")
    print("=" * 50)
    
    # Run all tests
    test_results = []
    
    test_results.append(("Basic Imports", test_basic_imports()))
    test_results.append(("New Modules", test_new_modules()))
    test_results.append(("Database System", test_database_system()))
    test_results.append(("Main Application", test_main_application()))
    test_results.append(("Batch Operations", test_batch_operations()))
    
    # Calculate results
    passed_tests = sum(1 for _, result in test_results if result)
    total_tests = len(test_results)
    success_rate = (passed_tests / total_tests) * 100
    
    # Display summary
    print("\n" + "=" * 50)
    print("🎯 Test Summary")
    print("=" * 50)
    
    for test_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\nResults: {passed_tests}/{total_tests} tests passed ({success_rate:.1f}%)")
    
    if success_rate == 100:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ NovelForge AI is ready for use!")
        print("\n📚 Available features:")
        print("  • Enhanced Series Workflows")
        print("  • One-Click Publishing")
        print("  • Smart Workflow Recommendations")
        print("  • Batch Operations (Cover, EPUB, Export)")
        print("  • Cover Management")
        print("  • Format & Export")
        print("  • Database Management v2.1")
        print("  • Complete Library Management")
        print("\n🚀 Run the application with: python run.py")
    else:
        print("\n⚠️ Some tests failed. Please check the errors above.")
        print("🔧 The system may still be partially functional.")
    
    return success_rate == 100

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
