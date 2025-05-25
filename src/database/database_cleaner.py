"""
Database cleaning and reset system for the ebook generator.
Provides safe options to clear database content with multiple safety levels.
"""

import os
import shutil
import sqlite3
from typing import Dict, Any, List, Optional
from datetime import datetime
from rich.console import Console
from rich.progress import Progress

from src.database.database_manager import get_database_manager

console = Console()


class DatabaseCleaner:
    """
    Manages safe database cleaning and reset operations.
    Provides multiple levels of clearing with safety backups.
    """
    
    def __init__(self):
        """Initialize the database cleaner."""
        self.db_manager = get_database_manager()
        self.backup_dir = "database_backups"
    
    def get_database_info(self) -> Dict[str, Any]:
        """
        Get current database information before cleaning.
        
        Returns:
            Dictionary containing database statistics
        """
        try:
            stats = self.db_manager.get_database_stats()
            
            # Get additional details
            with self.db_manager.get_connection() as conn:
                # Count records by type
                cursor = conn.execute("SELECT COUNT(*) FROM books WHERE epub_base64 IS NOT NULL")
                books_with_epubs = cursor.fetchone()[0]
                
                cursor = conn.execute("SELECT COUNT(*) FROM books WHERE cover_base64 IS NOT NULL")
                books_with_covers = cursor.fetchone()[0]
                
                cursor = conn.execute("SELECT COUNT(*) FROM books WHERE novel_data_json IS NOT NULL")
                books_with_novel_data = cursor.fetchone()[0]
            
            return {
                "total_books": stats["total_books"],
                "books_with_epubs": books_with_epubs,
                "books_with_covers": books_with_covers,
                "books_with_novel_data": books_with_novel_data,
                "database_size_mb": stats["database_size_bytes"] / (1024 * 1024),
                "epub_storage_mb": stats.get("total_epub_size_bytes", 0) / (1024 * 1024),
                "cover_storage_mb": stats.get("total_cover_size_bytes", 0) / (1024 * 1024),
                "database_path": stats["database_path"]
            }
            
        except Exception as e:
            console.print(f"[bold red]Error getting database info: {str(e)}[/bold red]")
            return {}
    
    def create_backup_before_clear(self, operation_type: str) -> Optional[str]:
        """
        Create a backup before clearing operations.
        
        Args:
            operation_type: Type of operation for backup naming
            
        Returns:
            Path to backup file or None if failed
        """
        try:
            # Ensure backup directory exists
            os.makedirs(self.backup_dir, exist_ok=True)
            
            # Create timestamped backup
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"before_{operation_type}_{timestamp}.db"
            backup_path = os.path.join(self.backup_dir, backup_filename)
            
            # Copy database file
            shutil.copy2(self.db_manager.db_path, backup_path)
            
            backup_size = os.path.getsize(backup_path) / (1024 * 1024)
            console.print(f"[bold green]✓[/bold green] Backup created: [cyan]{backup_path}[/cyan] ({backup_size:.1f} MB)")
            
            return backup_path
            
        except Exception as e:
            console.print(f"[bold red]Failed to create backup: {str(e)}[/bold red]")
            return None
    
    def clear_book_metadata_only(self, create_backup: bool = True) -> bool:
        """
        Clear only book metadata, keeping EPUBs and covers.
        
        Args:
            create_backup: Whether to create backup before clearing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if create_backup:
                backup_path = self.create_backup_before_clear("metadata_clear")
                if not backup_path:
                    console.print("[bold red]Backup failed, operation cancelled for safety[/bold red]")
                    return False
            
            console.print("[bold cyan]Clearing book metadata only...[/bold cyan]")
            
            with self.db_manager.get_connection() as conn:
                # Clear metadata fields but keep EPUBs and covers
                conn.execute("""
                    UPDATE books SET 
                        title = 'Cleared Book',
                        author = '',
                        genre = '',
                        target_audience = '',
                        description = '',
                        series_info = NULL,
                        novel_data_json = NULL,
                        generation_status = 'cleared',
                        word_count = 0,
                        chapter_count = 0,
                        file_path = '',
                        json_path = '',
                        epub_path = '',
                        metadata = NULL,
                        updated_date = ?
                """, (datetime.now().isoformat(),))
                
                conn.commit()
                
                # Get count of affected records
                cursor = conn.execute("SELECT COUNT(*) FROM books")
                affected_count = cursor.fetchone()[0]
            
            console.print(f"[bold green]✓[/bold green] Metadata cleared for {affected_count} books")
            console.print("[bold green]✓[/bold green] EPUBs and covers preserved")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error clearing metadata: {str(e)}[/bold red]")
            return False
    
    def clear_epub_storage_only(self, create_backup: bool = True) -> bool:
        """
        Clear only EPUB storage, keeping metadata and covers.
        
        Args:
            create_backup: Whether to create backup before clearing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if create_backup:
                backup_path = self.create_backup_before_clear("epub_clear")
                if not backup_path:
                    console.print("[bold red]Backup failed, operation cancelled for safety[/bold red]")
                    return False
            
            console.print("[bold cyan]Clearing EPUB storage only...[/bold cyan]")
            
            with self.db_manager.get_connection() as conn:
                # Get storage stats before clearing
                cursor = conn.execute("""
                    SELECT COUNT(*) as count, 
                           SUM(epub_size_bytes) as total_size,
                           SUM(epub_compressed_size) as compressed_size
                    FROM books 
                    WHERE epub_base64 IS NOT NULL
                """)
                stats = cursor.fetchone()
                
                # Clear EPUB storage fields
                conn.execute("""
                    UPDATE books SET 
                        epub_base64 = NULL,
                        epub_filename = NULL,
                        epub_size_bytes = 0,
                        epub_compressed_size = 0,
                        novel_data_json = NULL,
                        compression_ratio = 1.0,
                        checksum = NULL,
                        storage_mode = 'filesystem',
                        updated_date = ?
                """, (datetime.now().isoformat(),))
                
                conn.commit()
            
            if stats and stats[0] > 0:
                freed_mb = (stats[2] or 0) / (1024 * 1024)
                console.print(f"[bold green]✓[/bold green] EPUB storage cleared for {stats[0]} books")
                console.print(f"[bold green]✓[/bold green] Freed {freed_mb:.1f} MB of storage")
            else:
                console.print("[bold yellow]No EPUB storage found to clear[/bold yellow]")
            
            console.print("[bold green]✓[/bold green] Book metadata and covers preserved")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error clearing EPUB storage: {str(e)}[/bold red]")
            return False
    
    def clear_cover_storage_only(self, create_backup: bool = True) -> bool:
        """
        Clear only cover storage, keeping metadata and EPUBs.
        
        Args:
            create_backup: Whether to create backup before clearing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if create_backup:
                backup_path = self.create_backup_before_clear("cover_clear")
                if not backup_path:
                    console.print("[bold red]Backup failed, operation cancelled for safety[/bold red]")
                    return False
            
            console.print("[bold cyan]Clearing cover storage only...[/bold cyan]")
            
            with self.db_manager.get_connection() as conn:
                # Get cover stats before clearing
                cursor = conn.execute("""
                    SELECT COUNT(*) as count, 
                           SUM(LENGTH(cover_base64)) as total_size
                    FROM books 
                    WHERE cover_base64 IS NOT NULL
                """)
                stats = cursor.fetchone()
                
                # Clear cover storage fields
                conn.execute("""
                    UPDATE books SET 
                        cover_base64 = NULL,
                        cover_filename = NULL,
                        updated_date = ?
                """, (datetime.now().isoformat(),))
                
                conn.commit()
            
            if stats and stats[0] > 0:
                freed_mb = (stats[1] or 0) / (1024 * 1024)
                console.print(f"[bold green]✓[/bold green] Cover storage cleared for {stats[0]} books")
                console.print(f"[bold green]✓[/bold green] Freed {freed_mb:.1f} MB of storage")
            else:
                console.print("[bold yellow]No cover storage found to clear[/bold yellow]")
            
            console.print("[bold green]✓[/bold green] Book metadata and EPUBs preserved")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error clearing cover storage: {str(e)}[/bold red]")
            return False
    
    def clear_all_book_data(self, create_backup: bool = True) -> bool:
        """
        Clear all book data but keep database structure.
        
        Args:
            create_backup: Whether to create backup before clearing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if create_backup:
                backup_path = self.create_backup_before_clear("all_data_clear")
                if not backup_path:
                    console.print("[bold red]Backup failed, operation cancelled for safety[/bold red]")
                    return False
            
            console.print("[bold cyan]Clearing all book data...[/bold cyan]")
            
            # Get stats before clearing
            info = self.get_database_info()
            
            with self.db_manager.get_connection() as conn:
                # Delete all book records
                conn.execute("DELETE FROM books")
                
                # Reset any auto-increment counters
                conn.execute("DELETE FROM sqlite_sequence WHERE name='books'")
                
                # Update metadata
                conn.execute("""
                    INSERT OR REPLACE INTO database_metadata (key, value, updated_date)
                    VALUES ('last_cleared', ?, ?)
                """, (datetime.now().isoformat(), datetime.now().isoformat()))
                
                conn.commit()
            
            console.print(f"[bold green]✓[/bold green] All book data cleared")
            console.print(f"[bold green]✓[/bold green] Removed {info.get('total_books', 0)} books")
            console.print(f"[bold green]✓[/bold green] Freed {info.get('database_size_mb', 0):.1f} MB of storage")
            console.print("[bold green]✓[/bold green] Database structure preserved")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error clearing all data: {str(e)}[/bold red]")
            return False
    
    def reset_database_completely(self, create_backup: bool = True) -> bool:
        """
        Completely reset database to fresh state.
        
        Args:
            create_backup: Whether to create backup before resetting
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if create_backup:
                backup_path = self.create_backup_before_clear("complete_reset")
                if not backup_path:
                    console.print("[bold red]Backup failed, operation cancelled for safety[/bold red]")
                    return False
            
            console.print("[bold cyan]Completely resetting database...[/bold cyan]")
            
            # Get current database info
            info = self.get_database_info()
            
            # Close any existing connections
            try:
                self.db_manager._db_manager = None  # Reset singleton
            except:
                pass
            
            # Delete the database file
            if os.path.exists(self.db_manager.db_path):
                os.remove(self.db_manager.db_path)
                console.print("[bold green]✓[/bold green] Database file deleted")
            
            # Reinitialize database with fresh schema
            from src.database.database_manager import DatabaseManager
            new_db = DatabaseManager(self.db_manager.db_path)
            
            console.print(f"[bold green]✓[/bold green] Fresh database created")
            console.print(f"[bold green]✓[/bold green] Removed {info.get('total_books', 0)} books")
            console.print(f"[bold green]✓[/bold green] Freed {info.get('database_size_mb', 0):.1f} MB of storage")
            console.print("[bold green]✓[/bold green] Database reset to factory state")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error resetting database: {str(e)}[/bold red]")
            return False
    
    def clear_by_genre(self, genre: str, create_backup: bool = True) -> bool:
        """
        Clear books of a specific genre only.
        
        Args:
            genre: Genre to clear
            create_backup: Whether to create backup before clearing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if create_backup:
                backup_path = self.create_backup_before_clear(f"genre_{genre}_clear")
                if not backup_path:
                    console.print("[bold red]Backup failed, operation cancelled for safety[/bold red]")
                    return False
            
            console.print(f"[bold cyan]Clearing books in genre: {genre}...[/bold cyan]")
            
            with self.db_manager.get_connection() as conn:
                # Get count before deletion
                cursor = conn.execute("SELECT COUNT(*) FROM books WHERE genre = ?", (genre,))
                count_before = cursor.fetchone()[0]
                
                if count_before == 0:
                    console.print(f"[bold yellow]No books found in genre: {genre}[/bold yellow]")
                    return True
                
                # Delete books of specified genre
                conn.execute("DELETE FROM books WHERE genre = ?", (genre,))
                conn.commit()
                
                # Get count after deletion
                cursor = conn.execute("SELECT COUNT(*) FROM books")
                total_remaining = cursor.fetchone()[0]
            
            console.print(f"[bold green]✓[/bold green] Removed {count_before} books from genre: {genre}")
            console.print(f"[bold green]✓[/bold green] {total_remaining} books remaining in database")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error clearing genre {genre}: {str(e)}[/bold red]")
            return False
    
    def clear_old_books(self, days_old: int, create_backup: bool = True) -> bool:
        """
        Clear books older than specified days.
        
        Args:
            days_old: Remove books older than this many days
            create_backup: Whether to create backup before clearing
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if create_backup:
                backup_path = self.create_backup_before_clear(f"old_books_{days_old}days_clear")
                if not backup_path:
                    console.print("[bold red]Backup failed, operation cancelled for safety[/bold red]")
                    return False
            
            console.print(f"[bold cyan]Clearing books older than {days_old} days...[/bold cyan]")
            
            # Calculate cutoff date
            from datetime import timedelta
            cutoff_date = (datetime.now() - timedelta(days=days_old)).isoformat()
            
            with self.db_manager.get_connection() as conn:
                # Get count before deletion
                cursor = conn.execute("""
                    SELECT COUNT(*) FROM books 
                    WHERE created_date < ? OR created_date IS NULL
                """, (cutoff_date,))
                count_before = cursor.fetchone()[0]
                
                if count_before == 0:
                    console.print(f"[bold yellow]No books older than {days_old} days found[/bold yellow]")
                    return True
                
                # Delete old books
                conn.execute("""
                    DELETE FROM books 
                    WHERE created_date < ? OR created_date IS NULL
                """, (cutoff_date,))
                conn.commit()
                
                # Get count after deletion
                cursor = conn.execute("SELECT COUNT(*) FROM books")
                total_remaining = cursor.fetchone()[0]
            
            console.print(f"[bold green]✓[/bold green] Removed {count_before} books older than {days_old} days")
            console.print(f"[bold green]✓[/bold green] {total_remaining} books remaining in database")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error clearing old books: {str(e)}[/bold red]")
            return False
    
    def list_available_backups(self) -> List[Dict[str, Any]]:
        """
        List all available database backups.
        
        Returns:
            List of backup information dictionaries
        """
        backups = []
        
        try:
            if not os.path.exists(self.backup_dir):
                return backups
            
            for filename in os.listdir(self.backup_dir):
                if filename.endswith('.db'):
                    backup_path = os.path.join(self.backup_dir, filename)
                    stat = os.stat(backup_path)
                    
                    backups.append({
                        "filename": filename,
                        "path": backup_path,
                        "size_mb": stat.st_size / (1024 * 1024),
                        "created_date": datetime.fromtimestamp(stat.st_ctime).isoformat(),
                        "modified_date": datetime.fromtimestamp(stat.st_mtime).isoformat()
                    })
            
            # Sort by creation date (newest first)
            backups.sort(key=lambda x: x["created_date"], reverse=True)
            
        except Exception as e:
            console.print(f"[yellow]Warning: Could not list backups: {str(e)}[/yellow]")
        
        return backups
    
    def restore_from_backup(self, backup_path: str) -> bool:
        """
        Restore database from a backup file.
        
        Args:
            backup_path: Path to backup file to restore
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not os.path.exists(backup_path):
                console.print(f"[bold red]Backup file not found: {backup_path}[/bold red]")
                return False
            
            console.print(f"[bold cyan]Restoring database from backup...[/bold cyan]")
            
            # Create backup of current database before restore
            current_backup = self.create_backup_before_clear("before_restore")
            
            # Copy backup file to database location
            shutil.copy2(backup_path, self.db_manager.db_path)
            
            # Reset database manager to use restored database
            try:
                self.db_manager._db_manager = None  # Reset singleton
            except:
                pass
            
            # Verify restored database
            restored_db = get_database_manager()
            stats = restored_db.get_database_stats()
            
            console.print(f"[bold green]✓[/bold green] Database restored successfully")
            console.print(f"[bold green]✓[/bold green] Restored {stats['total_books']} books")
            console.print(f"[bold green]✓[/bold green] Database size: {stats['database_size_bytes'] / (1024*1024):.1f} MB")
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error restoring backup: {str(e)}[/bold red]")
            return False


# Global database cleaner instance
_database_cleaner = None

def get_database_cleaner() -> DatabaseCleaner:
    """Get the global database cleaner instance."""
    global _database_cleaner
    if _database_cleaner is None:
        _database_cleaner = DatabaseCleaner()
    return _database_cleaner
