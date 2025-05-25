"""
Database schema migration system for NovelForge AI.
Handles safe upgrades of existing databases to new schema versions.
"""

import sqlite3
import os
from typing import Dict, Any, List
from datetime import datetime
from rich.console import Console

console = Console()


class SchemaMigrator:
    """
    Handles database schema migrations safely and efficiently.
    """

    def __init__(self, db_path: str):
        """
        Initialize the schema migrator.

        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self.current_version = "2.1"  # Enhanced schema version with back cover support
        self.migrations = {
            "1.0": self._migrate_to_v1_0,
            "2.0": self._migrate_to_v2_0,
            "2.1": self._migrate_to_v2_1
        }

    def get_connection(self) -> sqlite3.Connection:
        """Get a database connection."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def get_current_schema_version(self) -> str:
        """
        Get the current schema version from the database.

        Returns:
            Schema version string or "0.0" if not found
        """
        try:
            with self.get_connection() as conn:
                # Check if database_metadata table exists
                cursor = conn.execute("""
                    SELECT name FROM sqlite_master
                    WHERE type='table' AND name='database_metadata'
                """)

                if not cursor.fetchone():
                    return "0.0"  # No metadata table = original schema

                # Get schema version
                cursor = conn.execute("""
                    SELECT value FROM database_metadata
                    WHERE key = 'schema_version'
                """)
                row = cursor.fetchone()

                return row["value"] if row else "1.0"  # Has metadata table but no version = v1.0

        except Exception as e:
            console.print(f"[yellow]Warning: Could not determine schema version: {str(e)}[/yellow]")
            return "0.0"

    def needs_migration(self) -> bool:
        """
        Check if the database needs migration.

        Returns:
            True if migration is needed, False otherwise
        """
        current_version = self.get_current_schema_version()
        return current_version != self.current_version

    def migrate_database(self) -> bool:
        """
        Migrate the database to the latest schema version.

        Returns:
            True if migration was successful, False otherwise
        """
        try:
            current_version = self.get_current_schema_version()

            if current_version == self.current_version:
                console.print("[bold green]Database schema is already up to date[/bold green]")
                return True

            console.print(f"[bold cyan]Migrating database schema from v{current_version} to v{self.current_version}[/bold cyan]")

            # Create backup before migration
            backup_path = self._create_backup()
            if backup_path:
                console.print(f"[bold green]✓[/bold green] Database backup created: [cyan]{backup_path}[/cyan]")

            # Apply migrations in order
            if current_version == "0.0":
                # Migrate from original schema to v1.0
                if not self._migrate_to_v1_0():
                    return False
                current_version = "1.0"

            if current_version == "1.0":
                # Migrate from v1.0 to v2.0
                if not self._migrate_to_v2_0():
                    return False
                current_version = "2.0"

            if current_version == "2.0":
                # Migrate from v2.0 to v2.1
                if not self._migrate_to_v2_1():
                    return False
                current_version = "2.1"

            # Update schema version
            self._set_schema_version(self.current_version)

            console.print(f"[bold green]✓[/bold green] Database migration completed successfully!")
            return True

        except Exception as e:
            console.print(f"[bold red]Database migration failed: {str(e)}[/bold red]")
            return False

    def _migrate_to_v1_0(self) -> bool:
        """
        Migrate to schema version 1.0 (basic database with books and metadata tables).

        Returns:
            True if successful, False otherwise
        """
        try:
            with self.get_connection() as conn:
                # Create database_metadata table if it doesn't exist
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS database_metadata (
                        key TEXT PRIMARY KEY,
                        value TEXT,
                        updated_date TEXT
                    )
                """)

                # Create basic books table with core columns
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
                        generation_status TEXT DEFAULT 'planned',  -- planned, generating, completed, failed
                        word_count INTEGER DEFAULT 0,
                        chapter_count INTEGER DEFAULT 0,
                        file_path TEXT,  -- Legacy: Path to the book files (for migration)
                        json_path TEXT,  -- Legacy: Path to novel_data.json (for migration)
                        epub_path TEXT,  -- Legacy: Path to EPUB file (for migration)
                        created_date TEXT,
                        updated_date TEXT,
                        metadata TEXT  -- Additional metadata as JSON
                    )
                """)

                # Create basic indexes
                conn.execute("CREATE INDEX IF NOT EXISTS idx_books_genre ON books(genre)")
                conn.execute("CREATE INDEX IF NOT EXISTS idx_books_status ON books(generation_status)")
                conn.execute("CREATE INDEX IF NOT EXISTS idx_books_created ON books(created_date)")
                conn.execute("CREATE INDEX IF NOT EXISTS idx_books_series ON books(series_info)")

                # Set initial metadata
                conn.execute("""
                    INSERT OR REPLACE INTO database_metadata (key, value, updated_date)
                    VALUES ('schema_version', '1.0', ?)
                """, (datetime.now().isoformat(),))

                conn.execute("""
                    INSERT OR REPLACE INTO database_metadata (key, value, updated_date)
                    VALUES ('created_date', ?, ?)
                """, (datetime.now().isoformat(), datetime.now().isoformat()))

                conn.commit()

            console.print("[bold green]✓[/bold green] Migrated to schema v1.0")
            return True

        except Exception as e:
            console.print(f"[bold red]Failed to migrate to v1.0: {str(e)}[/bold red]")
            return False

    def _migrate_to_v2_0(self) -> bool:
        """
        Migrate to schema version 2.0 (enhanced schema with EPUB storage).

        Returns:
            True if successful, False otherwise
        """
        try:
            with self.get_connection() as conn:
                # First ensure the books table exists
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                        book_id TEXT PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT,
                        genre TEXT,
                        target_audience TEXT,
                        description TEXT,
                        series_info TEXT,
                        cover_base64 TEXT,
                        cover_filename TEXT,
                        generation_status TEXT DEFAULT 'planned',
                        word_count INTEGER DEFAULT 0,
                        chapter_count INTEGER DEFAULT 0,
                        file_path TEXT,
                        json_path TEXT,
                        epub_path TEXT,
                        created_date TEXT,
                        updated_date TEXT,
                        metadata TEXT
                    )
                """)

                # Check which columns already exist
                cursor = conn.execute("PRAGMA table_info(books)")
                existing_columns = {row["name"] for row in cursor.fetchall()}

                # Add new columns if they don't exist
                new_columns = [
                    ("epub_base64", "TEXT"),
                    ("epub_filename", "TEXT"),
                    ("epub_size_bytes", "INTEGER DEFAULT 0"),
                    ("epub_compressed_size", "INTEGER DEFAULT 0"),
                    ("novel_data_json", "TEXT"),
                    ("storage_mode", "TEXT DEFAULT 'database'"),
                    ("compression_ratio", "REAL DEFAULT 1.0"),
                    ("checksum", "TEXT"),
                    ("last_accessed", "TEXT"),
                    ("access_count", "INTEGER DEFAULT 0")
                ]

                for column_name, column_type in new_columns:
                    if column_name not in existing_columns:
                        try:
                            conn.execute(f"ALTER TABLE books ADD COLUMN {column_name} {column_type}")
                            console.print(f"[bold green]✓[/bold green] Added column: {column_name}")
                        except sqlite3.OperationalError as e:
                            if "duplicate column name" not in str(e).lower():
                                raise e

                # Create new indexes
                new_indexes = [
                    "CREATE INDEX IF NOT EXISTS idx_books_storage_mode ON books(storage_mode)",
                    "CREATE INDEX IF NOT EXISTS idx_books_last_accessed ON books(last_accessed)",
                    "CREATE INDEX IF NOT EXISTS idx_books_access_count ON books(access_count)"
                ]

                for index_sql in new_indexes:
                    try:
                        conn.execute(index_sql)
                    except sqlite3.OperationalError:
                        pass  # Index might already exist

                conn.commit()

            console.print("[bold green]✓[/bold green] Migrated to schema v2.0")
            return True

        except Exception as e:
            console.print(f"[bold red]Failed to migrate to v2.0: {str(e)}[/bold red]")
            return False

    def _migrate_to_v2_1(self) -> bool:
        """
        Migrate to schema version 2.1 (back cover and enhanced descriptions).

        Returns:
            True if successful, False otherwise
        """
        try:
            with self.get_connection() as conn:
                # First ensure the books table exists with all v2.0 columns
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS books (
                        book_id TEXT PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT,
                        genre TEXT,
                        target_audience TEXT,
                        description TEXT,
                        series_info TEXT,
                        cover_base64 TEXT,
                        cover_filename TEXT,
                        epub_base64 TEXT,
                        epub_filename TEXT,
                        epub_size_bytes INTEGER DEFAULT 0,
                        epub_compressed_size INTEGER DEFAULT 0,
                        novel_data_json TEXT,
                        generation_status TEXT DEFAULT 'planned',
                        word_count INTEGER DEFAULT 0,
                        chapter_count INTEGER DEFAULT 0,
                        file_path TEXT,
                        json_path TEXT,
                        epub_path TEXT,
                        storage_mode TEXT DEFAULT 'database',
                        compression_ratio REAL DEFAULT 1.0,
                        checksum TEXT,
                        created_date TEXT,
                        updated_date TEXT,
                        last_accessed TEXT,
                        access_count INTEGER DEFAULT 0,
                        metadata TEXT
                    )
                """)

                # Check which columns already exist
                cursor = conn.execute("PRAGMA table_info(books)")
                existing_columns = {row["name"] for row in cursor.fetchall()}

                # Add new columns for back cover and enhanced descriptions
                new_columns = [
                    ("short_description", "TEXT"),  # 2-3 line description for recommendations
                    ("back_cover_description", "TEXT"),  # Attractive back cover description
                    ("back_cover_tagline", "TEXT"),  # Short tagline for back cover
                    ("marketing_description", "TEXT"),  # Enhanced marketing description
                    ("back_cover_generated", "INTEGER DEFAULT 0"),  # Flag for back cover generation
                    ("description_enhanced", "INTEGER DEFAULT 0"),  # Flag for description enhancement
                    ("description_generation_date", "TEXT"),  # When descriptions were generated
                    ("back_cover_style", "TEXT DEFAULT 'default'"),  # Back cover style/theme

                    # Telegram publishing fields
                    ("telegram_published", "INTEGER DEFAULT 0"),  # Flag for Telegram publication
                    ("telegram_message_id", "TEXT"),  # Telegram message ID for tracking
                    ("telegram_publish_date", "TEXT"),  # When published to Telegram
                    ("telegram_channel_id", "TEXT"),  # Which channel it was published to
                    ("telegram_post_type", "TEXT"),  # 'book', 'series_announcement', 'series_update'
                    ("telegram_engagement_stats", "TEXT"),  # JSON with views, reactions, etc.
                    ("telegram_file_hosting", "TEXT"),  # JSON with file hosting details
                    ("telegram_scheduled_date", "TEXT"),  # For scheduled publishing
                    ("telegram_auto_publish", "INTEGER DEFAULT 1"),  # Auto-publish flag
                    ("telegram_publication_status", "TEXT DEFAULT 'pending'")  # pending, published, failed, skipped
                ]

                for column_name, column_type in new_columns:
                    if column_name not in existing_columns:
                        try:
                            conn.execute(f"ALTER TABLE books ADD COLUMN {column_name} {column_type}")
                            console.print(f"[bold green]✓[/bold green] Added column: {column_name}")
                        except sqlite3.OperationalError as e:
                            if "duplicate column name" not in str(e).lower():
                                raise e

                # Create new indexes for better query performance
                new_indexes = [
                    "CREATE INDEX IF NOT EXISTS idx_books_back_cover_generated ON books(back_cover_generated)",
                    "CREATE INDEX IF NOT EXISTS idx_books_description_enhanced ON books(description_enhanced)",
                    "CREATE INDEX IF NOT EXISTS idx_books_back_cover_style ON books(back_cover_style)"
                ]

                for index_sql in new_indexes:
                    try:
                        conn.execute(index_sql)
                    except sqlite3.OperationalError:
                        pass  # Index might already exist

                conn.commit()

            console.print("[bold green]✓[/bold green] Migrated to schema v2.1 (Back Cover Support)")
            return True

        except Exception as e:
            console.print(f"[bold red]Failed to migrate to v2.1: {str(e)}[/bold red]")
            return False

    def _create_backup(self) -> str:
        """
        Create a backup of the database before migration.

        Returns:
            Path to backup file or empty string if failed
        """
        try:
            if not os.path.exists(self.db_path):
                return ""

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_path = f"{self.db_path}.backup_{timestamp}"

            # Copy database file
            import shutil
            shutil.copy2(self.db_path, backup_path)

            return backup_path

        except Exception as e:
            console.print(f"[yellow]Warning: Could not create backup: {str(e)}[/yellow]")
            return ""

    def _set_schema_version(self, version: str) -> None:
        """
        Set the schema version in the database.

        Args:
            version: Schema version to set
        """
        with self.get_connection() as conn:
            conn.execute("""
                INSERT OR REPLACE INTO database_metadata (key, value, updated_date)
                VALUES ('schema_version', ?, ?)
            """, (version, datetime.now().isoformat()))
            conn.commit()

    def get_migration_info(self) -> Dict[str, Any]:
        """
        Get information about the current migration status.

        Returns:
            Dictionary containing migration information
        """
        current_version = self.get_current_schema_version()
        needs_migration = self.needs_migration()

        return {
            "current_version": current_version,
            "target_version": self.current_version,
            "needs_migration": needs_migration,
            "database_exists": os.path.exists(self.db_path),
            "database_size_mb": os.path.getsize(self.db_path) / (1024 * 1024) if os.path.exists(self.db_path) else 0
        }


def migrate_database_if_needed(db_path: str) -> bool:
    """
    Convenience function to migrate database if needed.

    Args:
        db_path: Path to the database file

    Returns:
        True if database is ready (migrated or up to date), False if migration failed
    """
    migrator = SchemaMigrator(db_path)

    if migrator.needs_migration():
        return migrator.migrate_database()

    return True
