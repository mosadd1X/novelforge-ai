"""
Database manager for the NovelForge AI system.
Handles book metadata, cover storage, and generation tracking.
"""

import sqlite3
import os
import json
import base64
from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
from pathlib import Path
from rich.console import Console

console = Console()


class DatabaseManager:
    """
    Manages the SQLite database for book metadata and cover storage.
    """

    def __init__(self, db_path: str = "data/novelforge_ai.db"):
        """
        Initialize the database manager.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self.ensure_database_directory()
        self.init_database()

    def ensure_database_directory(self) -> None:
        """Ensure the database directory exists."""
        db_dir = os.path.dirname(self.db_path)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)

    def get_connection(self) -> sqlite3.Connection:
        """Get a database connection with proper configuration."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Enable dict-like access to rows
        return conn

    def init_database(self) -> None:
        """Initialize the database with required tables."""
        # First, handle schema migration if needed
        self._handle_schema_migration()

        with self.get_connection() as conn:
            # Create books table with enhanced storage
            conn.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    book_id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    author TEXT,
                    genre TEXT,
                    target_audience TEXT,
                    description TEXT,
                    series_info TEXT,  -- JSON string for series information
                    cover_base64 TEXT,  -- Base64 encoded cover image
                    cover_filename TEXT,  -- Original filename for reference
                    epub_base64 TEXT,  -- Base64 encoded EPUB file
                    epub_filename TEXT,  -- Original EPUB filename
                    epub_size_bytes INTEGER DEFAULT 0,  -- Original EPUB file size
                    epub_compressed_size INTEGER DEFAULT 0,  -- Compressed size in database
                    novel_data_json TEXT,  -- Complete novel_data.json as JSON
                    generation_status TEXT DEFAULT 'planned',  -- planned, generating, completed, failed
                    word_count INTEGER DEFAULT 0,
                    chapter_count INTEGER DEFAULT 0,
                    file_path TEXT,  -- Legacy: Path to the book files (for migration)
                    json_path TEXT,  -- Legacy: Path to novel_data.json (for migration)
                    epub_path TEXT,  -- Legacy: Path to EPUB file (for migration)
                    storage_mode TEXT DEFAULT 'database',  -- database, filesystem, hybrid
                    compression_ratio REAL DEFAULT 1.0,  -- Compression efficiency ratio
                    checksum TEXT,  -- File integrity checksum
                    created_date TEXT,
                    updated_date TEXT,
                    last_accessed TEXT,  -- Track when book was last accessed
                    access_count INTEGER DEFAULT 0,  -- Track how often book is accessed
                    metadata TEXT  -- Additional metadata as JSON
                )
            """)

            # Create indexes for better performance
            conn.execute("CREATE INDEX IF NOT EXISTS idx_books_genre ON books(genre)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_books_status ON books(generation_status)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_books_created ON books(created_date)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_books_series ON books(series_info)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_books_storage_mode ON books(storage_mode)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_books_last_accessed ON books(last_accessed)")
            conn.execute("CREATE INDEX IF NOT EXISTS idx_books_access_count ON books(access_count)")

            # Create database metadata table
            conn.execute("""
                CREATE TABLE IF NOT EXISTS database_metadata (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    updated_date TEXT
                )
            """)

            # Set database version
            self.set_metadata("version", "1.0")
            self.set_metadata("schema_version", "2.0")  # Current enhanced schema
            self.set_metadata("created_date", datetime.now().isoformat())

            conn.commit()

    def _handle_schema_migration(self) -> None:
        """Handle database schema migration if needed."""
        try:
            from src.database.schema_migrator import migrate_database_if_needed
            migrate_database_if_needed(self.db_path)
        except ImportError:
            # Schema migrator not available, continue with basic initialization
            pass
        except Exception as e:
            console.print(f"[yellow]Warning: Schema migration failed: {str(e)}[/yellow]")
            console.print("[yellow]Continuing with current schema...[/yellow]")

    def set_metadata(self, key: str, value: str) -> None:
        """Set a metadata value in the database."""
        with self.get_connection() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO database_metadata (key, value, updated_date)
                VALUES (?, ?, ?)
            """, (key, value, datetime.now().isoformat()))
            conn.commit()

    def get_metadata(self, key: str) -> Optional[str]:
        """Get a metadata value from the database."""
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT value FROM database_metadata WHERE key = ?", (key,))
            row = cursor.fetchone()
            return row["value"] if row else None

    def add_book(self, book_data: Dict[str, Any]) -> str:
        """
        Add a new book to the database.

        Args:
            book_data: Dictionary containing book information

        Returns:
            The book_id of the added book
        """
        book_id = book_data.get("book_id") or self.generate_book_id(book_data["title"])

        # Prepare series info as JSON
        series_info = book_data.get("series_info", {})
        series_info_json = json.dumps(series_info) if series_info else None

        # Prepare additional metadata as JSON
        metadata = book_data.get("metadata", {})
        metadata_json = json.dumps(metadata) if metadata else None

        with self.get_connection() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO books (
                    book_id, title, author, genre, target_audience, description,
                    series_info, cover_base64, cover_filename, generation_status,
                    word_count, chapter_count, file_path, json_path, epub_path,
                    created_date, updated_date, metadata
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                book_id,
                book_data["title"],
                book_data.get("author", ""),
                book_data.get("genre", ""),
                book_data.get("target_audience", ""),
                book_data.get("description", ""),
                series_info_json,
                book_data.get("cover_base64"),
                book_data.get("cover_filename"),
                book_data.get("generation_status", "planned"),
                book_data.get("word_count", 0),
                book_data.get("chapter_count", 0),
                book_data.get("file_path", ""),
                book_data.get("json_path", ""),
                book_data.get("epub_path", ""),
                book_data.get("created_date", datetime.now().isoformat()),
                datetime.now().isoformat(),
                metadata_json
            ))
            conn.commit()

        return book_id

    def get_book(self, book_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a book by its ID.

        Args:
            book_id: The book ID to retrieve

        Returns:
            Dictionary containing book data or None if not found
        """
        with self.get_connection() as conn:
            cursor = conn.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
            row = cursor.fetchone()

            if row:
                return self._row_to_dict(row)
            return None

    def get_books(self, genre: Optional[str] = None, status: Optional[str] = None,
                  limit: Optional[int] = None, offset: int = 0) -> List[Dict[str, Any]]:
        """
        Get books with optional filtering.

        Args:
            genre: Filter by genre
            status: Filter by generation status
            limit: Maximum number of books to return
            offset: Number of books to skip

        Returns:
            List of book dictionaries
        """
        query = "SELECT * FROM books WHERE 1=1"
        params = []

        if genre:
            query += " AND genre = ?"
            params.append(genre)

        if status:
            query += " AND generation_status = ?"
            params.append(status)

        query += " ORDER BY created_date DESC"

        if limit:
            query += " LIMIT ? OFFSET ?"
            params.extend([limit, offset])

        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            rows = cursor.fetchall()

            return [self._row_to_dict(row) for row in rows]

    def update_book(self, book_id: str, updates: Dict[str, Any]) -> bool:
        """
        Update a book's information.

        Args:
            book_id: The book ID to update
            updates: Dictionary of fields to update

        Returns:
            True if update was successful, False otherwise
        """
        if not updates:
            return False

        # Handle special JSON fields
        if "series_info" in updates and isinstance(updates["series_info"], dict):
            updates["series_info"] = json.dumps(updates["series_info"])

        if "metadata" in updates and isinstance(updates["metadata"], dict):
            updates["metadata"] = json.dumps(updates["metadata"])

        # Add updated_date
        updates["updated_date"] = datetime.now().isoformat()

        # Build update query
        set_clause = ", ".join([f"{key} = ?" for key in updates.keys()])
        query = f"UPDATE books SET {set_clause} WHERE book_id = ?"
        params = list(updates.values()) + [book_id]

        with self.get_connection() as conn:
            cursor = conn.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0

    def update_book_descriptions(self, book_id: str, descriptions: Dict[str, str]) -> bool:
        """
        Update book descriptions (short, back cover, tagline, etc.).

        Args:
            book_id: The book ID to update
            descriptions: Dictionary containing description fields

        Returns:
            True if successful, False otherwise
        """
        try:
            updates = {}

            # Map description fields
            if "short_description" in descriptions:
                updates["short_description"] = descriptions["short_description"]

            if "back_cover_description" in descriptions:
                updates["back_cover_description"] = descriptions["back_cover_description"]

            if "tagline" in descriptions:
                updates["back_cover_tagline"] = descriptions["tagline"]

            if "marketing_description" in descriptions:
                updates["marketing_description"] = descriptions["marketing_description"]

            # Set flags and timestamp
            updates["description_enhanced"] = 1
            updates["description_generation_date"] = datetime.now().isoformat()

            return self.update_book(book_id, updates)

        except Exception as e:
            print(f"Error updating book descriptions for {book_id}: {e}")
            return False

    def mark_back_cover_generated(self, book_id: str, style: str = "default") -> bool:
        """
        Mark that back cover has been generated for a book.

        Args:
            book_id: The book ID
            style: Back cover style used

        Returns:
            True if successful, False otherwise
        """
        updates = {
            "back_cover_generated": 1,
            "back_cover_style": style
        }

        return self.update_book(book_id, updates)

    def get_books_needing_descriptions(self) -> list:
        """
        Get books that need description generation.

        Returns:
            List of books that need descriptions generated
        """
        with self.get_connection() as conn:
            cursor = conn.execute("""
                SELECT * FROM books
                WHERE generation_status = 'completed'
                AND (description_enhanced IS NULL OR description_enhanced = 0)
                ORDER BY created_date DESC
            """)
            rows = cursor.fetchall()
            return [self._row_to_dict(row) for row in rows]

    def get_books_needing_back_covers(self) -> list:
        """
        Get books that need back cover generation.

        Returns:
            List of books that need back covers generated
        """
        with self.get_connection() as conn:
            cursor = conn.execute("""
                SELECT * FROM books
                WHERE generation_status = 'completed'
                AND (back_cover_generated IS NULL OR back_cover_generated = 0)
                ORDER BY created_date DESC
            """)
            rows = cursor.fetchall()
            return [self._row_to_dict(row) for row in rows]

    def delete_book(self, book_id: str) -> bool:
        """
        Delete a book from the database.

        Args:
            book_id: The book ID to delete

        Returns:
            True if deletion was successful, False otherwise
        """
        with self.get_connection() as conn:
            cursor = conn.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
            conn.commit()
            return cursor.rowcount > 0

    def generate_book_id(self, title: str) -> str:
        """
        Generate a unique book ID based on title and timestamp.

        Args:
            title: Book title

        Returns:
            Unique book ID
        """
        # Sanitize title for ID
        sanitized = "".join(c for c in title if c.isalnum() or c in " -_").strip()
        sanitized = sanitized.replace(" ", "_").lower()

        # Add timestamp for uniqueness
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        return f"{sanitized}_{timestamp}"

    def _row_to_dict(self, row: sqlite3.Row) -> Dict[str, Any]:
        """
        Convert a database row to a dictionary with proper JSON parsing.

        Args:
            row: SQLite row object

        Returns:
            Dictionary representation of the row
        """
        data = dict(row)

        # Parse JSON fields
        if data.get("series_info"):
            try:
                data["series_info"] = json.loads(data["series_info"])
            except json.JSONDecodeError:
                data["series_info"] = {}

        if data.get("metadata"):
            try:
                data["metadata"] = json.loads(data["metadata"])
            except json.JSONDecodeError:
                data["metadata"] = {}

        return data

    def get_database_stats(self) -> Dict[str, Any]:
        """
        Get database statistics.

        Returns:
            Dictionary containing database statistics
        """
        with self.get_connection() as conn:
            # Total books
            cursor = conn.execute("SELECT COUNT(*) as total FROM books")
            total_books = cursor.fetchone()["total"]

            # Books by status
            cursor = conn.execute("""
                SELECT generation_status, COUNT(*) as count
                FROM books
                GROUP BY generation_status
            """)
            status_counts = {row["generation_status"]: row["count"] for row in cursor.fetchall()}

            # Books by genre
            cursor = conn.execute("""
                SELECT genre, COUNT(*) as count
                FROM books
                WHERE genre IS NOT NULL AND genre != ''
                GROUP BY genre
                ORDER BY count DESC
            """)
            genre_counts = {row["genre"]: row["count"] for row in cursor.fetchall()}

            # Storage usage (covers)
            cursor = conn.execute("""
                SELECT COUNT(*) as covers_count,
                       SUM(LENGTH(cover_base64)) as total_cover_size
                FROM books
                WHERE cover_base64 IS NOT NULL
            """)
            cover_stats = cursor.fetchone()

            # Storage usage (EPUBs)
            cursor = conn.execute("""
                SELECT COUNT(*) as epubs_count,
                       SUM(LENGTH(epub_base64)) as total_epub_size,
                       SUM(epub_size_bytes) as total_original_size,
                       AVG(compression_ratio) as avg_compression_ratio,
                       COUNT(CASE WHEN storage_mode = 'database' THEN 1 END) as database_stored,
                       COUNT(CASE WHEN storage_mode = 'filesystem' THEN 1 END) as filesystem_stored
                FROM books
                WHERE epub_base64 IS NOT NULL
            """)
            epub_stats = cursor.fetchone()

            # Access statistics
            cursor = conn.execute("""
                SELECT AVG(access_count) as avg_access_count,
                       MAX(access_count) as max_access_count,
                       COUNT(CASE WHEN last_accessed IS NOT NULL THEN 1 END) as accessed_books
                FROM books
            """)
            access_stats = cursor.fetchone()

            # Database file size
            db_size = os.path.getsize(self.db_path) if os.path.exists(self.db_path) else 0

            return {
                "total_books": total_books,
                "status_counts": status_counts,
                "genre_counts": genre_counts,
                "covers_stored": cover_stats["covers_count"] or 0,
                "total_cover_size_bytes": cover_stats["total_cover_size"] or 0,
                "epubs_stored": epub_stats["epubs_count"] or 0,
                "total_epub_size_bytes": epub_stats["total_epub_size"] or 0,
                "total_original_epub_size_bytes": epub_stats["total_original_size"] or 0,
                "avg_compression_ratio": epub_stats["avg_compression_ratio"] or 1.0,
                "database_stored_count": epub_stats["database_stored"] or 0,
                "filesystem_stored_count": epub_stats["filesystem_stored"] or 0,
                "avg_access_count": access_stats["avg_access_count"] or 0,
                "max_access_count": access_stats["max_access_count"] or 0,
                "accessed_books_count": access_stats["accessed_books"] or 0,
                "database_size_bytes": db_size,
                "database_path": self.db_path
            }


# Global database manager instance
_db_manager = None

def get_database_manager() -> DatabaseManager:
    """Get the global database manager instance."""
    global _db_manager
    if _db_manager is None:
        _db_manager = DatabaseManager()
    return _db_manager
