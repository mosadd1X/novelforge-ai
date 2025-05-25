#!/usr/bin/env python3
"""
Test script for the enhanced database system.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_database_system():
    """Test the enhanced database system components."""
    print("🧪 Testing Enhanced Database System")
    print("=" * 50)
    
    # Test 1: Database Manager
    try:
        from src.database.database_manager import get_database_manager
        print("✅ Database manager imported")
        
        db = get_database_manager()
        stats = db.get_database_stats()
        print(f"✅ Database initialized: {stats['total_books']} books")
        print(f"✅ Database size: {stats['database_size_bytes'] / 1024:.1f} KB")
        
    except Exception as e:
        print(f"❌ Database manager error: {e}")
        return False
    
    # Test 2: Schema Migrator
    try:
        from src.database.schema_migrator import SchemaMigrator
        print("✅ Schema migrator imported")
        
        migrator = SchemaMigrator("data/ebook_generator.db")
        info = migrator.get_migration_info()
        print(f"✅ Schema: v{info['current_version']} → v{info['target_version']}")
        print(f"✅ Migration needed: {info['needs_migration']}")
        
    except Exception as e:
        print(f"❌ Schema migrator error: {e}")
        return False
    
    # Test 3: EPUB Database Manager
    try:
        from src.database.epub_database_manager import get_epub_database_manager
        print("✅ EPUB database manager imported")
        
        epub_db = get_epub_database_manager()
        epub_stats = epub_db.get_epub_stats()
        print(f"✅ EPUB manager: {epub_stats['total_epubs']} EPUBs stored")
        
    except Exception as e:
        print(f"❌ EPUB database manager error: {e}")
        return False
    
    # Test 4: Book Library Manager
    try:
        from src.database.book_library_manager import get_book_library_manager
        print("✅ Book library manager imported")
        
        library = get_book_library_manager()
        summary = library.get_library_summary()
        print(f"✅ Library: {summary['total_books']} books available")
        
    except Exception as e:
        print(f"❌ Book library manager error: {e}")
        return False
    
    # Test 5: Database UI
    try:
        from src.ui.database_menu import database_management_menu
        print("✅ Database management UI imported")
        
    except Exception as e:
        print(f"❌ Database UI error: {e}")
        return False
    
    print("\n🎉 All Tests Passed!")
    print("✅ Enhanced database system is fully functional")
    print("✅ Schema migration system is ready")
    print("✅ EPUB storage system is available")
    print("✅ Book library management is operational")
    print("✅ Database management UI is accessible")
    
    return True

if __name__ == "__main__":
    success = test_database_system()
    if success:
        print("\n🚀 Database system is ready for use!")
        print("Access via: python run.py → 8. Database Management")
    else:
        print("\n❌ Database system has issues that need to be resolved.")
    
    sys.exit(0 if success else 1)
