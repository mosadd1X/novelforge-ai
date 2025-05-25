"""
EPUB database manager for storing and retrieving complete EPUB files.
Handles compression, validation, and on-demand extraction.
"""

import os
import base64
import gzip
import hashlib
import tempfile
import shutil
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime
from rich.console import Console

from src.database.database_manager import get_database_manager

console = Console()


class EpubDatabaseManager:
    """
    Manages complete EPUB files stored in the database.
    Provides compression, validation, and on-demand extraction.
    """
    
    def __init__(self):
        """Initialize the EPUB database manager."""
        self.db_manager = get_database_manager()
        self.temp_dir = tempfile.gettempdir()
        self.max_epub_size = 50 * 1024 * 1024  # 50MB limit for safety
    
    def store_epub_from_file(self, book_id: str, epub_path: str, 
                           novel_data: Optional[Dict[str, Any]] = None) -> bool:
        """
        Store an EPUB file from disk into the database.
        
        Args:
            book_id: The book ID to associate the EPUB with
            epub_path: Path to the EPUB file
            novel_data: Optional novel data to store alongside
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not os.path.exists(epub_path):
                console.print(f"[bold red]EPUB file not found: {epub_path}[/bold red]")
                return False
            
            # Check file size
            file_size = os.path.getsize(epub_path)
            if file_size > self.max_epub_size:
                console.print(f"[bold red]EPUB file too large: {file_size / (1024*1024):.1f}MB (max: {self.max_epub_size / (1024*1024):.1f}MB)[/bold red]")
                return False
            
            # Read and validate EPUB
            with open(epub_path, 'rb') as f:
                epub_data = f.read()
            
            if not self._validate_epub_data(epub_data):
                console.print(f"[bold red]Invalid EPUB file: {epub_path}[/bold red]")
                return False
            
            # Compress the EPUB data
            compressed_data = gzip.compress(epub_data)
            compression_ratio = len(compressed_data) / len(epub_data)
            
            # Generate checksum for integrity
            checksum = hashlib.sha256(epub_data).hexdigest()
            
            # Convert to base64 for database storage
            epub_base64 = base64.b64encode(compressed_data).decode('utf-8')
            
            # Prepare novel data JSON
            novel_data_json = None
            if novel_data:
                import json
                novel_data_json = json.dumps(novel_data)
            
            # Get filename
            epub_filename = os.path.basename(epub_path)
            
            # Update book record
            updates = {
                "epub_base64": epub_base64,
                "epub_filename": epub_filename,
                "epub_size_bytes": file_size,
                "epub_compressed_size": len(compressed_data),
                "compression_ratio": compression_ratio,
                "checksum": checksum,
                "storage_mode": "database"
            }
            
            if novel_data_json:
                updates["novel_data_json"] = novel_data_json
            
            success = self.db_manager.update_book(book_id, updates)
            
            if success:
                console.print(f"[bold green]✓[/bold green] EPUB stored in database: {epub_filename}")
                console.print(f"[dim]Original: {file_size / 1024:.1f}KB, Compressed: {len(compressed_data) / 1024:.1f}KB ({compression_ratio:.1%} ratio)[/dim]")
                return True
            else:
                console.print(f"[bold red]Failed to update book record: {book_id}[/bold red]")
                return False
                
        except Exception as e:
            console.print(f"[bold red]Error storing EPUB: {str(e)}[/bold red]")
            return False
    
    def get_epub_as_file(self, book_id: str, output_path: str) -> bool:
        """
        Extract an EPUB from the database and save it as a file.
        
        Args:
            book_id: The book ID to get the EPUB for
            output_path: Path where to save the EPUB file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Get book data
            book_data = self.db_manager.get_book(book_id)
            if not book_data or not book_data.get("epub_base64"):
                return False
            
            # Decode and decompress EPUB data
            compressed_data = base64.b64decode(book_data["epub_base64"])
            epub_data = gzip.decompress(compressed_data)
            
            # Verify integrity if checksum exists
            if book_data.get("checksum"):
                calculated_checksum = hashlib.sha256(epub_data).hexdigest()
                if calculated_checksum != book_data["checksum"]:
                    console.print(f"[bold red]EPUB integrity check failed for book: {book_id}[/bold red]")
                    return False
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write EPUB file
            with open(output_path, 'wb') as f:
                f.write(epub_data)
            
            # Update access statistics
            self._update_access_stats(book_id)
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error extracting EPUB: {str(e)}[/bold red]")
            return False
    
    def get_epub_as_temp_file(self, book_id: str) -> Optional[str]:
        """
        Extract an EPUB to a temporary file and return the path.
        
        Args:
            book_id: The book ID to get the EPUB for
            
        Returns:
            Path to temporary EPUB file or None if failed
        """
        try:
            # Get book data for filename
            book_data = self.db_manager.get_book(book_id)
            if not book_data:
                return None
            
            # Create temporary file with proper extension
            epub_filename = book_data.get("epub_filename", f"{book_id}.epub")
            temp_path = os.path.join(self.temp_dir, f"temp_{book_id}_{epub_filename}")
            
            if self.get_epub_as_file(book_id, temp_path):
                return temp_path
            
            return None
            
        except Exception as e:
            console.print(f"[bold red]Error creating temporary EPUB: {str(e)}[/bold red]")
            return None
    
    def has_epub(self, book_id: str) -> bool:
        """
        Check if a book has an EPUB stored in the database.
        
        Args:
            book_id: The book ID to check
            
        Returns:
            True if EPUB exists, False otherwise
        """
        book_data = self.db_manager.get_book(book_id)
        return book_data is not None and book_data.get("epub_base64") is not None
    
    def remove_epub(self, book_id: str) -> bool:
        """
        Remove the EPUB for a book from the database.
        
        Args:
            book_id: The book ID to remove the EPUB for
            
        Returns:
            True if successful, False otherwise
        """
        return self.db_manager.update_book(book_id, {
            "epub_base64": None,
            "epub_filename": None,
            "epub_size_bytes": 0,
            "epub_compressed_size": 0,
            "compression_ratio": 1.0,
            "checksum": None,
            "storage_mode": "filesystem"
        })
    
    def get_novel_data(self, book_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the novel data JSON for a book.
        
        Args:
            book_id: The book ID to get novel data for
            
        Returns:
            Novel data dictionary or None if not found
        """
        book_data = self.db_manager.get_book(book_id)
        if book_data and book_data.get("novel_data_json"):
            try:
                import json
                return json.loads(book_data["novel_data_json"])
            except json.JSONDecodeError:
                console.print(f"[yellow]Warning: Invalid novel data JSON for book: {book_id}[/yellow]")
        return None
    
    def get_books_with_epubs(self) -> List[Dict[str, Any]]:
        """
        Get all books that have EPUBs stored in the database.
        
        Returns:
            List of book dictionaries with EPUBs
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute("""
                SELECT * FROM books 
                WHERE epub_base64 IS NOT NULL 
                ORDER BY last_accessed DESC, updated_date DESC
            """)
            rows = cursor.fetchall()
            
            return [self.db_manager._row_to_dict(row) for row in rows]
    
    def get_epub_stats(self) -> Dict[str, Any]:
        """
        Get statistics about EPUBs stored in the database.
        
        Returns:
            Dictionary containing EPUB statistics
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute("""
                SELECT 
                    COUNT(*) as total_epubs,
                    SUM(epub_size_bytes) as total_original_size,
                    SUM(epub_compressed_size) as total_compressed_size,
                    AVG(compression_ratio) as avg_compression_ratio,
                    MIN(compression_ratio) as best_compression,
                    MAX(compression_ratio) as worst_compression,
                    SUM(access_count) as total_accesses,
                    AVG(access_count) as avg_accesses
                FROM books 
                WHERE epub_base64 IS NOT NULL
            """)
            stats = cursor.fetchone()
            
            # Calculate storage savings
            original_size = stats["total_original_size"] or 0
            compressed_size = stats["total_compressed_size"] or 0
            storage_saved = original_size - compressed_size
            
            return {
                "total_epubs": stats["total_epubs"] or 0,
                "total_original_size_bytes": original_size,
                "total_compressed_size_bytes": compressed_size,
                "storage_saved_bytes": storage_saved,
                "storage_saved_mb": storage_saved / (1024 * 1024),
                "avg_compression_ratio": stats["avg_compression_ratio"] or 1.0,
                "best_compression_ratio": stats["best_compression"] or 1.0,
                "worst_compression_ratio": stats["worst_compression"] or 1.0,
                "total_accesses": stats["total_accesses"] or 0,
                "avg_accesses_per_book": stats["avg_accesses"] or 0
            }
    
    def _validate_epub_data(self, epub_data: bytes) -> bool:
        """
        Validate that the data is a valid EPUB file.
        
        Args:
            epub_data: Raw EPUB data bytes
            
        Returns:
            True if valid EPUB, False otherwise
        """
        try:
            # EPUB files are ZIP archives, check for ZIP signature
            if len(epub_data) < 4:
                return False
            
            # Check for ZIP file signature (PK)
            if epub_data[:2] != b'PK':
                return False
            
            # Additional validation could be added here
            # (checking for mimetype file, META-INF directory, etc.)
            
            return True
            
        except Exception:
            return False
    
    def _update_access_stats(self, book_id: str) -> None:
        """
        Update access statistics for a book.
        
        Args:
            book_id: The book ID to update stats for
        """
        try:
            # Get current access count
            book_data = self.db_manager.get_book(book_id)
            if book_data:
                current_count = book_data.get("access_count", 0)
                
                # Update access statistics
                self.db_manager.update_book(book_id, {
                    "access_count": current_count + 1,
                    "last_accessed": datetime.now().isoformat()
                })
        except Exception:
            pass  # Don't fail the main operation if stats update fails
    
    def cleanup_temp_files(self, book_id: Optional[str] = None) -> int:
        """
        Clean up temporary EPUB files.
        
        Args:
            book_id: Optional specific book ID to clean up, or None for all
            
        Returns:
            Number of files cleaned up
        """
        try:
            cleaned_count = 0
            temp_pattern = f"temp_{book_id}_" if book_id else "temp_"
            
            for filename in os.listdir(self.temp_dir):
                if filename.startswith(temp_pattern) and filename.endswith('.epub'):
                    temp_path = os.path.join(self.temp_dir, filename)
                    try:
                        os.remove(temp_path)
                        cleaned_count += 1
                    except Exception:
                        pass
            
            return cleaned_count
            
        except Exception:
            return 0


# Global EPUB database manager instance
_epub_db_manager = None

def get_epub_database_manager() -> EpubDatabaseManager:
    """Get the global EPUB database manager instance."""
    global _epub_db_manager
    if _epub_db_manager is None:
        _epub_db_manager = EpubDatabaseManager()
    return _epub_db_manager
