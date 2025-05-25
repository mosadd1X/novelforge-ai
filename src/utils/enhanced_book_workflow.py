"""
Enhanced Book Generation Workflow with Back Cover Support.

This module manages the enhanced book generation process including
description generation, back cover creation, and database updates.
"""

import json
from typing import Dict, Any, Optional, List
from datetime import datetime

from src.utils.back_cover_generator import BackCoverGenerator
from src.utils.back_cover_image_generator import BackCoverImageGenerator
from src.database.database_manager import get_database_manager
from src.database.schema_migrator import migrate_database_if_needed


class EnhancedBookWorkflow:
    """
    Manages the enhanced book generation workflow with back cover support.
    """

    def __init__(self):
        """Initialize the enhanced book workflow."""
        self.db_manager = get_database_manager()
        self.back_cover_generator = BackCoverGenerator()
        self.back_cover_image_generator = BackCoverImageGenerator()

        # Ensure database schema is up to date
        migrate_database_if_needed(self.db_manager.db_path)

    def process_completed_book(self, book_id: str, novel_data: Dict[str, Any]) -> bool:
        """
        Process a completed book with enhanced descriptions and back cover.

        Args:
            book_id: The book ID in database
            novel_data: Complete novel data

        Returns:
            True if processing was successful
        """
        try:
            print(f"🔄 Processing completed book: {book_id}")

            # Step 1: Generate enhanced descriptions
            descriptions = self._generate_enhanced_descriptions(novel_data)
            if descriptions:
                print("✅ Enhanced descriptions generated")

                # Update database with descriptions
                success = self.db_manager.update_book_descriptions(book_id, descriptions)
                if success:
                    print("✅ Descriptions saved to database")
                else:
                    print("⚠️ Failed to save descriptions to database")
            else:
                print("⚠️ Failed to generate enhanced descriptions")

            # Step 2: Generate back cover image (automatic)
            if descriptions:
                print("🎨 Generating back cover image...")
                back_cover_data = self._generate_back_cover_image(novel_data, descriptions)
                if back_cover_data:
                    print("✅ Back cover image generated")

                    # Save back cover to database (as cover or separate field)
                    self._save_back_cover_image(book_id, back_cover_data)
                    print("✅ Back cover saved to database")
                else:
                    print("⚠️ Failed to generate back cover image (continuing anyway)")

            # Step 3: Mark processing complete
            self.db_manager.mark_back_cover_generated(book_id)

            print(f"🎉 Enhanced processing completed for book: {book_id}")
            return True

        except Exception as e:
            print(f"❌ Error processing book {book_id}: {e}")
            return False

    def batch_process_existing_books(self, max_books: int = 10) -> Dict[str, Any]:
        """
        Batch process existing books that need enhanced descriptions.

        Args:
            max_books: Maximum number of books to process

        Returns:
            Dictionary with processing results
        """
        try:
            print(f"🔄 Starting batch processing (max {max_books} books)")

            # Get books needing descriptions
            books_needing_descriptions = self.db_manager.get_books_needing_descriptions()
            books_to_process = books_needing_descriptions[:max_books]

            if not books_to_process:
                print("✅ No books need description processing")
                return {"processed": 0, "skipped": 0, "errors": 0}

            print(f"📚 Found {len(books_to_process)} books to process")

            results = {"processed": 0, "skipped": 0, "errors": 0}

            for book in books_to_process:
                book_id = book["book_id"]
                title = book.get("title", "Unknown")

                print(f"\n📖 Processing: {title}")

                try:
                    # Try to reconstruct novel data from database
                    novel_data = self._reconstruct_novel_data(book)

                    if novel_data:
                        success = self.process_completed_book(book_id, novel_data)
                        if success:
                            results["processed"] += 1
                        else:
                            results["errors"] += 1
                    else:
                        print(f"⚠️ Could not reconstruct novel data for {title}")
                        results["skipped"] += 1

                except Exception as e:
                    print(f"❌ Error processing {title}: {e}")
                    results["errors"] += 1

            print(f"\n🎉 Batch processing complete:")
            print(f"  ✅ Processed: {results['processed']}")
            print(f"  ⚠️ Skipped: {results['skipped']}")
            print(f"  ❌ Errors: {results['errors']}")

            return results

        except Exception as e:
            print(f"❌ Error in batch processing: {e}")
            return {"processed": 0, "skipped": 0, "errors": 1}

    def _generate_enhanced_descriptions(self, novel_data: Dict[str, Any]) -> Optional[Dict[str, str]]:
        """
        Generate enhanced descriptions for a book.

        Args:
            novel_data: Complete novel data

        Returns:
            Dictionary with generated descriptions or None if failed
        """
        try:
            descriptions = self.back_cover_generator.generate_descriptions(novel_data)

            # Validate descriptions
            if descriptions and descriptions.get("short_description") and descriptions.get("back_cover_description"):
                return descriptions
            else:
                print("⚠️ Generated descriptions are incomplete")
                return None

        except Exception as e:
            print(f"❌ Error generating descriptions: {e}")
            return None

    def _generate_back_cover_image(self, novel_data: Dict[str, Any],
                                 descriptions: Dict[str, str]) -> Optional[str]:
        """
        Generate back cover image.

        Args:
            novel_data: Complete novel data
            descriptions: Generated descriptions

        Returns:
            Base64 encoded image data or None if failed
        """
        try:
            # Extract book metadata for image generation
            metadata = novel_data.get("metadata", {})
            book_data = {
                "title": metadata.get("title", "Unknown Title"),
                "author": metadata.get("author", "Unknown Author"),
                "genre": metadata.get("genre", "Fiction")
            }

            return self.back_cover_image_generator.generate_back_cover(book_data, descriptions)

        except Exception as e:
            print(f"❌ Error generating back cover image: {e}")
            return None

    def _save_back_cover_image(self, book_id: str, back_cover_data: str) -> bool:
        """
        Save back cover image to database.

        Args:
            book_id: Book ID
            back_cover_data: Base64 encoded image data

        Returns:
            True if successful
        """
        try:
            # For now, we'll save it as a separate field
            # In the future, this could be a separate back cover table
            updates = {
                "back_cover_image": back_cover_data,
                "back_cover_generated": 1
            }

            return self.db_manager.update_book(book_id, updates)

        except Exception as e:
            print(f"❌ Error saving back cover image: {e}")
            return False

    def _reconstruct_novel_data(self, book: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Reconstruct novel data from database book record.

        Args:
            book: Book record from database

        Returns:
            Reconstructed novel data or None if failed
        """
        try:
            # Try to get novel data from JSON field first
            if book.get("novel_data_json"):
                try:
                    return json.loads(book["novel_data_json"])
                except json.JSONDecodeError:
                    pass

            # Reconstruct from available fields
            metadata = {
                "title": book.get("title", "Unknown Title"),
                "author": book.get("author", "Unknown Author"),
                "genre": book.get("genre", "Fiction"),
                "target_audience": book.get("target_audience", "Adult"),
                "description": book.get("description", ""),
                "word_count": book.get("word_count", 0),
                "chapter_count": book.get("chapter_count", 0),
                "created_at": book.get("created_date", datetime.now().isoformat())
            }

            # Add series information if available
            if book.get("series_info"):
                metadata["series"] = book["series_info"]

            # Create minimal novel data structure
            novel_data = {
                "metadata": metadata,
                "chapters": []  # We don't have chapter content in database
            }

            return novel_data

        except Exception as e:
            print(f"❌ Error reconstructing novel data: {e}")
            return None

    def get_processing_status(self) -> Dict[str, Any]:
        """
        Get status of description and back cover processing.

        Returns:
            Dictionary with processing status information
        """
        try:
            books_needing_descriptions = len(self.db_manager.get_books_needing_descriptions())
            books_needing_back_covers = len(self.db_manager.get_books_needing_back_covers())

            # Get total completed books
            completed_books = self.db_manager.get_books(status="completed")
            total_completed = len(completed_books)

            # Calculate completion rates
            description_completion = 0
            back_cover_completion = 0

            if total_completed > 0:
                description_completion = ((total_completed - books_needing_descriptions) / total_completed) * 100
                back_cover_completion = ((total_completed - books_needing_back_covers) / total_completed) * 100

            return {
                "total_completed_books": total_completed,
                "books_needing_descriptions": books_needing_descriptions,
                "books_needing_back_covers": books_needing_back_covers,
                "description_completion_rate": round(description_completion, 1),
                "back_cover_completion_rate": round(back_cover_completion, 1),
                "ready_for_processing": books_needing_descriptions > 0 or books_needing_back_covers > 0
            }

        except Exception as e:
            print(f"❌ Error getting processing status: {e}")
            return {
                "total_completed_books": 0,
                "books_needing_descriptions": 0,
                "books_needing_back_covers": 0,
                "description_completion_rate": 0,
                "back_cover_completion_rate": 0,
                "ready_for_processing": False
            }
