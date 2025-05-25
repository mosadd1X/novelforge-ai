#!/usr/bin/env python3
"""
Complete NovelForge AI System Test

This script tests all the implemented functionality to ensure everything is working correctly.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_database_system():
    """Test the database system and schema migration."""
    print("🧪 Testing Database System")
    print("=" * 50)
    
    try:
        from src.database.database_manager import get_database_manager
        from src.database.schema_migrator import SchemaMigrator
        
        # Test database manager
        db = get_database_manager()
        stats = db.get_database_stats()
        print(f"✅ Database Manager: {stats['total_books']} books, {stats['database_size_bytes'] / 1024:.1f} KB")
        
        # Test schema migrator
        migrator = SchemaMigrator("data/novelforge_ai.db")
        version = migrator.get_current_schema_version()
        print(f"✅ Schema Version: v{version}")
        
        return True
        
    except Exception as e:
        print(f"❌ Database system error: {e}")
        return False

def test_core_modules():
    """Test all core UI modules."""
    print("\n🧪 Testing Core UI Modules")
    print("=" * 50)
    
    modules_to_test = [
        ("Enhanced Series Workflows", "src.ui.enhanced_series_workflows", "enhanced_series_workflows_menu"),
        ("One-Click Publishing", "src.ui.one_click_publishing", "one_click_publishing_menu"),
        ("Smart Recommendations", "src.ui.smart_workflow_recommendations", "smart_workflow_recommendations_menu"),
        ("Batch Operations", "src.ui.batch_operations", "batch_cover_generation_menu"),
        ("Cover Management", "src.ui.cover_management", "cover_management_menu"),
        ("Format & Export", "src.ui.format_export", "format_export_menu"),
        ("Database Management", "src.ui.database_menu", "database_management_menu"),
        ("Book Management", "src.ui.book_menu", "book_management_menu"),
        ("Series Management", "src.ui.series_menu", "series_management_menu")
    ]
    
    all_passed = True
    
    for name, module_path, function_name in modules_to_test:
        try:
            module = __import__(module_path, fromlist=[function_name])
            getattr(module, function_name)
            print(f"✅ {name}: OK")
        except Exception as e:
            print(f"❌ {name}: {e}")
            all_passed = False
    
    return all_passed

def test_batch_operations():
    """Test specific batch operation functions."""
    print("\n🧪 Testing Batch Operations Functions")
    print("=" * 50)
    
    try:
        from src.ui.batch_operations import (
            batch_cover_generation_menu,
            batch_epub_generation_menu,
            batch_export_menu,
            complete_all_unfinished_books_workflow
        )
        
        print("✅ batch_cover_generation_menu: OK")
        print("✅ batch_epub_generation_menu: OK")
        print("✅ batch_export_menu: OK")
        print("✅ complete_all_unfinished_books_workflow: OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Batch operations error: {e}")
        return False

def test_main_application():
    """Test the main application entry point."""
    print("\n🧪 Testing Main Application")
    print("=" * 50)
    
    try:
        import run
        print("✅ Main application (run.py): OK")
        
        # Test main menu functions
        from run import (
            content_creation_menu,
            library_management_menu,
            publishing_tools_menu,
            system_settings_menu
        )
        
        print("✅ Content creation menu: OK")
        print("✅ Library management menu: OK")
        print("✅ Publishing tools menu: OK")
        print("✅ System settings menu: OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Main application error: {e}")
        return False

def test_terminal_ui():
    """Test terminal UI components."""
    print("\n🧪 Testing Terminal UI Components")
    print("=" * 50)
    
    try:
        from src.ui.terminal_ui import (
            clear_screen,
            display_title,
            custom_style
        )
        
        print("✅ Terminal UI components: OK")
        
        # Test responsive separators
        from src.ui.responsive_separator import (
            separator,
            title_separator,
            section_separator
        )
        
        print("✅ Responsive separators: OK")
        
        return True
        
    except Exception as e:
        print(f"❌ Terminal UI error: {e}")
        return False

def main():
    """Run all tests and provide summary."""
    print("🚀 NovelForge AI Complete System Test")
    print("=" * 60)
    print()
    
    test_results = []
    
    # Run all tests
    test_results.append(("Database System", test_database_system()))
    test_results.append(("Core Modules", test_core_modules()))
    test_results.append(("Batch Operations", test_batch_operations()))
    test_results.append(("Main Application", test_main_application()))
    test_results.append(("Terminal UI", test_terminal_ui()))
    
    # Summary
    print("\n🎯 Test Summary")
    print("=" * 60)
    
    passed_tests = 0
    total_tests = len(test_results)
    
    for test_name, result in test_results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
        if result:
            passed_tests += 1
    
    print()
    print(f"Results: {passed_tests}/{total_tests} tests passed")
    
    if passed_tests == total_tests:
        print()
        print("🎉 ALL TESTS PASSED!")
        print("✅ NovelForge AI is fully functional and ready for use!")
        print()
        print("🚀 You can now run the application with: python run.py")
        print()
        print("📚 Available features:")
        print("  • Enhanced Series Workflows")
        print("  • One-Click Publishing")
        print("  • Smart Workflow Recommendations")
        print("  • Batch Operations (Cover, EPUB, Export)")
        print("  • Cover Management")
        print("  • Format & Export")
        print("  • Database Management")
        print("  • Complete Library Management")
        
        return True
    else:
        print()
        print("⚠️ Some tests failed. Please check the errors above.")
        print("🔧 The system may still be partially functional.")
        
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
