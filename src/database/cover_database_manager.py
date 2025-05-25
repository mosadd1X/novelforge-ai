"""
Cover database manager for storing and retrieving book covers as base64 data.
"""

import os
import base64
from typing import Dict, Any, Optional, List
from PIL import Image
import io
from rich.console import Console

from src.database.database_manager import get_database_manager

console = Console()


class CoverDatabaseManager:
    """
    Manages cover images stored in the database as base64 data.
    """
    
    def __init__(self):
        """Initialize the cover database manager."""
        self.db_manager = get_database_manager()
        self.supported_formats = ['.jpg', '.jpeg', '.png', '.webp', '.bmp']
    
    def store_cover_from_file(self, book_id: str, cover_path: str) -> bool:
        """
        Store a cover image from a file path into the database.
        
        Args:
            book_id: The book ID to associate the cover with
            cover_path: Path to the cover image file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if not os.path.exists(cover_path):
                console.print(f"[bold red]Cover file not found: {cover_path}[/bold red]")
                return False
            
            # Validate image format
            if not self._is_valid_image_format(cover_path):
                console.print(f"[bold red]Unsupported image format: {cover_path}[/bold red]")
                return False
            
            # Read and encode the image
            with open(cover_path, 'rb') as f:
                image_data = f.read()
            
            # Validate image data
            if not self._validate_image_data(image_data):
                console.print(f"[bold red]Invalid image data: {cover_path}[/bold red]")
                return False
            
            # Convert to base64
            cover_base64 = base64.b64encode(image_data).decode('utf-8')
            
            # Get filename for reference
            cover_filename = os.path.basename(cover_path)
            
            # Update book record with cover data
            success = self.db_manager.update_book(book_id, {
                "cover_base64": cover_base64,
                "cover_filename": cover_filename
            })
            
            if success:
                console.print(f"[bold green]✓[/bold green] Cover stored in database for book: {book_id}")
                return True
            else:
                console.print(f"[bold red]Failed to update book record: {book_id}[/bold red]")
                return False
                
        except Exception as e:
            console.print(f"[bold red]Error storing cover: {str(e)}[/bold red]")
            return False
    
    def store_cover_from_base64(self, book_id: str, cover_base64: str, filename: str = "cover.jpg") -> bool:
        """
        Store a cover image from base64 data into the database.
        
        Args:
            book_id: The book ID to associate the cover with
            cover_base64: Base64 encoded image data
            filename: Original filename for reference
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Validate base64 data
            try:
                image_data = base64.b64decode(cover_base64)
                if not self._validate_image_data(image_data):
                    console.print(f"[bold red]Invalid base64 image data[/bold red]")
                    return False
            except Exception as e:
                console.print(f"[bold red]Invalid base64 data: {str(e)}[/bold red]")
                return False
            
            # Update book record with cover data
            success = self.db_manager.update_book(book_id, {
                "cover_base64": cover_base64,
                "cover_filename": filename
            })
            
            if success:
                console.print(f"[bold green]✓[/bold green] Cover stored in database for book: {book_id}")
                return True
            else:
                console.print(f"[bold red]Failed to update book record: {book_id}[/bold red]")
                return False
                
        except Exception as e:
            console.print(f"[bold red]Error storing cover: {str(e)}[/bold red]")
            return False
    
    def get_cover_base64(self, book_id: str) -> Optional[str]:
        """
        Get the base64 cover data for a book.
        
        Args:
            book_id: The book ID to get the cover for
            
        Returns:
            Base64 encoded cover data or None if not found
        """
        book_data = self.db_manager.get_book(book_id)
        if book_data and book_data.get("cover_base64"):
            return book_data["cover_base64"]
        return None
    
    def get_cover_as_file(self, book_id: str, output_path: str) -> bool:
        """
        Extract a cover from the database and save it as a file.
        
        Args:
            book_id: The book ID to get the cover for
            output_path: Path where to save the cover file
            
        Returns:
            True if successful, False otherwise
        """
        try:
            cover_base64 = self.get_cover_base64(book_id)
            if not cover_base64:
                return False
            
            # Decode base64 data
            image_data = base64.b64decode(cover_base64)
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Write to file
            with open(output_path, 'wb') as f:
                f.write(image_data)
            
            return True
            
        except Exception as e:
            console.print(f"[bold red]Error extracting cover: {str(e)}[/bold red]")
            return False
    
    def get_cover_data_url(self, book_id: str) -> Optional[str]:
        """
        Get a data URL for the cover image (for HTML embedding).
        
        Args:
            book_id: The book ID to get the cover for
            
        Returns:
            Data URL string or None if not found
        """
        cover_base64 = self.get_cover_base64(book_id)
        if cover_base64:
            # Assume JPEG format for data URL (most common)
            return f"data:image/jpeg;base64,{cover_base64}"
        return None
    
    def has_cover(self, book_id: str) -> bool:
        """
        Check if a book has a cover stored in the database.
        
        Args:
            book_id: The book ID to check
            
        Returns:
            True if cover exists, False otherwise
        """
        return self.get_cover_base64(book_id) is not None
    
    def remove_cover(self, book_id: str) -> bool:
        """
        Remove the cover for a book from the database.
        
        Args:
            book_id: The book ID to remove the cover for
            
        Returns:
            True if successful, False otherwise
        """
        return self.db_manager.update_book(book_id, {
            "cover_base64": None,
            "cover_filename": None
        })
    
    def get_books_with_covers(self) -> List[Dict[str, Any]]:
        """
        Get all books that have covers stored in the database.
        
        Returns:
            List of book dictionaries with covers
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute("""
                SELECT * FROM books 
                WHERE cover_base64 IS NOT NULL 
                ORDER BY updated_date DESC
            """)
            rows = cursor.fetchall()
            
            return [self.db_manager._row_to_dict(row) for row in rows]
    
    def get_cover_stats(self) -> Dict[str, Any]:
        """
        Get statistics about covers stored in the database.
        
        Returns:
            Dictionary containing cover statistics
        """
        with self.db_manager.get_connection() as conn:
            cursor = conn.execute("""
                SELECT 
                    COUNT(*) as total_covers,
                    SUM(LENGTH(cover_base64)) as total_size_bytes,
                    AVG(LENGTH(cover_base64)) as avg_size_bytes,
                    MIN(LENGTH(cover_base64)) as min_size_bytes,
                    MAX(LENGTH(cover_base64)) as max_size_bytes
                FROM books 
                WHERE cover_base64 IS NOT NULL
            """)
            stats = cursor.fetchone()
            
            return {
                "total_covers": stats["total_covers"] or 0,
                "total_size_bytes": stats["total_size_bytes"] or 0,
                "total_size_mb": (stats["total_size_bytes"] or 0) / (1024 * 1024),
                "avg_size_bytes": stats["avg_size_bytes"] or 0,
                "min_size_bytes": stats["min_size_bytes"] or 0,
                "max_size_bytes": stats["max_size_bytes"] or 0
            }
    
    def _is_valid_image_format(self, file_path: str) -> bool:
        """Check if the file has a supported image format."""
        _, ext = os.path.splitext(file_path.lower())
        return ext in self.supported_formats
    
    def _validate_image_data(self, image_data: bytes) -> bool:
        """
        Validate that the image data is a valid image.
        
        Args:
            image_data: Raw image data bytes
            
        Returns:
            True if valid image, False otherwise
        """
        try:
            # Try to open the image with PIL
            image = Image.open(io.BytesIO(image_data))
            
            # Verify it's a valid image by getting its size
            width, height = image.size
            
            # Basic validation - image should have reasonable dimensions
            if width < 10 or height < 10 or width > 10000 or height > 10000:
                return False
            
            return True
            
        except Exception:
            return False
    
    def optimize_cover_for_storage(self, image_data: bytes, max_width: int = 800, 
                                 quality: int = 85) -> bytes:
        """
        Optimize a cover image for database storage.
        
        Args:
            image_data: Original image data
            max_width: Maximum width for the optimized image
            quality: JPEG quality (1-100)
            
        Returns:
            Optimized image data
        """
        try:
            # Open the image
            image = Image.open(io.BytesIO(image_data))
            
            # Convert to RGB if necessary (for JPEG compatibility)
            if image.mode in ('RGBA', 'LA', 'P'):
                # Create a white background
                background = Image.new('RGB', image.size, (255, 255, 255))
                if image.mode == 'P':
                    image = image.convert('RGBA')
                background.paste(image, mask=image.split()[-1] if image.mode == 'RGBA' else None)
                image = background
            
            # Resize if too large
            if image.width > max_width:
                ratio = max_width / image.width
                new_height = int(image.height * ratio)
                image = image.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Save as optimized JPEG
            output = io.BytesIO()
            image.save(output, format='JPEG', quality=quality, optimize=True)
            
            return output.getvalue()
            
        except Exception as e:
            console.print(f"[yellow]Warning: Could not optimize image: {str(e)}[/yellow]")
            return image_data


# Global cover database manager instance
_cover_db_manager = None

def get_cover_database_manager() -> CoverDatabaseManager:
    """Get the global cover database manager instance."""
    global _cover_db_manager
    if _cover_db_manager is None:
        _cover_db_manager = CoverDatabaseManager()
    return _cover_db_manager
