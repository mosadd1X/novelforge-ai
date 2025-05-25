#!/usr/bin/env python3
"""
Simple test to check NovelForge AI modules
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test basic imports"""
    print("Testing basic imports...")
    
    try:
        print("1. Testing terminal_ui...")
        from src.ui.terminal_ui import clear_screen, display_title, custom_style
        print("   ✅ terminal_ui: OK")
    except Exception as e:
        print(f"   ❌ terminal_ui: {e}")
        return False
    
    try:
        print("2. Testing responsive_separator...")
        from src.ui.responsive_separator import separator, title_separator
        print("   ✅ responsive_separator: OK")
    except Exception as e:
        print(f"   ❌ responsive_separator: {e}")
        return False
    
    try:
        print("3. Testing database_manager...")
        from src.database.database_manager import get_database_manager
        print("   ✅ database_manager: OK")
    except Exception as e:
        print(f"   ❌ database_manager: {e}")
        return False
    
    try:
        print("4. Testing enhanced_series_workflows...")
        from src.ui.enhanced_series_workflows import enhanced_series_workflows_menu
        print("   ✅ enhanced_series_workflows: OK")
    except Exception as e:
        print(f"   ❌ enhanced_series_workflows: {e}")
        return False
    
    try:
        print("5. Testing one_click_publishing...")
        from src.ui.one_click_publishing import one_click_publishing_menu
        print("   ✅ one_click_publishing: OK")
    except Exception as e:
        print(f"   ❌ one_click_publishing: {e}")
        return False
    
    try:
        print("6. Testing smart_workflow_recommendations...")
        from src.ui.smart_workflow_recommendations import smart_workflow_recommendations_menu
        print("   ✅ smart_workflow_recommendations: OK")
    except Exception as e:
        print(f"   ❌ smart_workflow_recommendations: {e}")
        return False
    
    try:
        print("7. Testing batch_operations...")
        from src.ui.batch_operations import batch_cover_generation_menu
        print("   ✅ batch_operations: OK")
    except Exception as e:
        print(f"   ❌ batch_operations: {e}")
        return False
    
    try:
        print("8. Testing cover_management...")
        from src.ui.cover_management import cover_management_menu
        print("   ✅ cover_management: OK")
    except Exception as e:
        print(f"   ❌ cover_management: {e}")
        return False
    
    try:
        print("9. Testing format_export...")
        from src.ui.format_export import format_export_menu
        print("   ✅ format_export: OK")
    except Exception as e:
        print(f"   ❌ format_export: {e}")
        return False
    
    return True

def test_database():
    """Test database functionality"""
    print("\nTesting database functionality...")
    
    try:
        from src.database.database_manager import get_database_manager
        from src.database.schema_migrator import SchemaMigrator
        
        # Test database manager
        db = get_database_manager()
        stats = db.get_database_stats()
        print(f"   ✅ Database: {stats['total_books']} books")
        
        # Test schema version
        migrator = SchemaMigrator("data/novelforge_ai.db")
        version = migrator.get_current_schema_version()
        print(f"   ✅ Schema version: v{version}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Database error: {e}")
        return False

def main():
    """Run simple tests"""
    print("🧪 NovelForge AI Simple Test")
    print("=" * 40)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test database
    database_ok = test_database()
    
    print("\n" + "=" * 40)
    if imports_ok and database_ok:
        print("🎉 All tests passed!")
        print("✅ NovelForge AI is ready!")
    else:
        print("⚠️ Some tests failed")
    
    return imports_ok and database_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
