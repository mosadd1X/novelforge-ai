"""
Book library manager for on-demand book access and format conversion.
Provides a cloud-like experience for accessing books stored in the database.
"""

import os
import tempfile
import shutil
from typing import Dict, Any, Optional, List
from datetime import datetime
from rich.console import Console
from rich.progress import Progress

from src.database.database_manager import get_database_manager
from src.database.epub_database_manager import get_epub_database_manager
from src.database.cover_database_manager import get_cover_database_manager

console = Console()


class BookLibraryManager:
    """
    Manages on-demand access to books stored in the database.
    Provides cloud-like functionality for book retrieval and format conversion.
    """
    
    def __init__(self):
        """Initialize the book library manager."""
        self.db_manager = get_database_manager()
        self.epub_db_manager = get_epub_database_manager()
        self.cover_db_manager = get_cover_database_manager()
        self.temp_dir = tempfile.gettempdir()
        self.export_dir = "exported_books"
    
    def get_book_from_library(self, book_id: str, output_dir: Optional[str] = None, 
                            include_cover: bool = True) -> Optional[str]:
        """
        Extract a complete book from the database to the file system.
        
        Args:
            book_id: The book ID to extract
            output_dir: Directory to extract to (default: exported_books)
            include_cover: Whether to extract cover image
            
        Returns:
            Path to extracted book directory or None if failed
        """
        try:
            # Get book data
            book_data = self.db_manager.get_book(book_id)
            if not book_data:
                console.print(f"[bold red]Book not found: {book_id}[/bold red]")
                return None
            
            # Determine output directory
            if not output_dir:
                output_dir = self.export_dir
            
            # Create book directory
            book_title = book_data.get("title", "Unknown")
            safe_title = "".join(c for c in book_title if c.isalnum() or c in " -_").strip()
            safe_title = safe_title.replace(" ", "_")
            
            book_dir = os.path.join(output_dir, safe_title)
            os.makedirs(book_dir, exist_ok=True)
            
            console.print(f"[bold cyan]Extracting book: {book_title}[/bold cyan]")
            
            # Extract EPUB
            epub_extracted = False
            if self.epub_db_manager.has_epub(book_id):
                epub_filename = book_data.get("epub_filename", f"{safe_title}.epub")
                epub_path = os.path.join(book_dir, epub_filename)
                
                if self.epub_db_manager.get_epub_as_file(book_id, epub_path):
                    console.print(f"[bold green]✓[/bold green] EPUB extracted: {epub_filename}")
                    epub_extracted = True
                else:
                    console.print(f"[bold red]✗[/bold red] Failed to extract EPUB")
            
            # Extract novel data
            novel_data_extracted = False
            novel_data = self.epub_db_manager.get_novel_data(book_id)
            if novel_data:
                import json
                novel_data_path = os.path.join(book_dir, "novel_data.json")
                with open(novel_data_path, 'w', encoding='utf-8') as f:
                    json.dump(novel_data, f, indent=2, ensure_ascii=False)
                console.print(f"[bold green]✓[/bold green] Novel data extracted: novel_data.json")
                novel_data_extracted = True
            
            # Extract cover
            cover_extracted = False
            if include_cover and self.cover_db_manager.has_cover(book_id):
                cover_filename = book_data.get("cover_filename", "cover.jpg")
                cover_path = os.path.join(book_dir, cover_filename)
                
                if self.cover_db_manager.get_cover_as_file(book_id, cover_path):
                    console.print(f"[bold green]✓[/bold green] Cover extracted: {cover_filename}")
                    cover_extracted = True
            
            # Create extraction summary
            summary_path = os.path.join(book_dir, "extraction_info.txt")
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(f"Book Extraction Summary\n")
                f.write(f"======================\n\n")
                f.write(f"Book ID: {book_id}\n")
                f.write(f"Title: {book_title}\n")
                f.write(f"Author: {book_data.get('author', 'Unknown')}\n")
                f.write(f"Genre: {book_data.get('genre', 'Unknown')}\n")
                f.write(f"Extraction Date: {datetime.now().isoformat()}\n\n")
                f.write(f"Extracted Components:\n")
                f.write(f"- EPUB: {'✓' if epub_extracted else '✗'}\n")
                f.write(f"- Novel Data: {'✓' if novel_data_extracted else '✗'}\n")
                f.write(f"- Cover: {'✓' if cover_extracted else '✗'}\n")
            
            if epub_extracted or novel_data_extracted:
                console.print(f"[bold green]✓[/bold green] Book extracted to: [cyan]{book_dir}[/cyan]")
                return book_dir
            else:
                console.print(f"[bold red]✗[/bold red] No content could be extracted")
                return None
                
        except Exception as e:
            console.print(f"[bold red]Error extracting book: {str(e)}[/bold red]")
            return None
    
    def convert_book_format(self, book_id: str, target_format: str, 
                          output_path: Optional[str] = None) -> Optional[str]:
        """
        Convert a book from the database to a different format.
        
        Args:
            book_id: The book ID to convert
            target_format: Target format (pdf, mobi, txt, etc.)
            output_path: Optional output path for converted file
            
        Returns:
            Path to converted file or None if failed
        """
        try:
            # Get temporary EPUB file
            temp_epub = self.epub_db_manager.get_epub_as_temp_file(book_id)
            if not temp_epub:
                console.print(f"[bold red]Could not extract EPUB for conversion[/bold red]")
                return None
            
            # Get book data for naming
            book_data = self.db_manager.get_book(book_id)
            if not book_data:
                return None
            
            book_title = book_data.get("title", "Unknown")
            safe_title = "".join(c for c in book_title if c.isalnum() or c in " -_").strip()
            safe_title = safe_title.replace(" ", "_")
            
            # Determine output path
            if not output_path:
                output_path = os.path.join(self.export_dir, f"{safe_title}.{target_format}")
            
            console.print(f"[bold cyan]Converting {book_title} to {target_format.upper()}...[/bold cyan]")
            
            # Import format converter
            try:
                from src.formatters.format_converter import FormatConverter
                converter = FormatConverter()
                
                # Convert the file
                success = converter.convert_epub_to_format(temp_epub, output_path, target_format)
                
                if success:
                    console.print(f"[bold green]✓[/bold green] Converted to: [cyan]{output_path}[/cyan]")
                    return output_path
                else:
                    console.print(f"[bold red]✗[/bold red] Conversion failed")
                    return None
                    
            except ImportError:
                console.print(f"[bold red]Format converter not available[/bold red]")
                return None
            finally:
                # Clean up temporary file
                try:
                    os.remove(temp_epub)
                except:
                    pass
                    
        except Exception as e:
            console.print(f"[bold red]Error converting book: {str(e)}[/bold red]")
            return None
    
    def batch_export_books(self, book_ids: List[str], output_dir: Optional[str] = None,
                          include_covers: bool = True) -> Dict[str, str]:
        """
        Export multiple books from the database in batch.
        
        Args:
            book_ids: List of book IDs to export
            output_dir: Directory to export to
            include_covers: Whether to include cover images
            
        Returns:
            Dictionary mapping book_id to export path (or error message)
        """
        results = {}
        
        if not output_dir:
            output_dir = self.export_dir
        
        console.print(f"[bold cyan]Batch exporting {len(book_ids)} books...[/bold cyan]")
        
        with Progress() as progress:
            task = progress.add_task("Exporting books...", total=len(book_ids))
            
            for book_id in book_ids:
                try:
                    export_path = self.get_book_from_library(book_id, output_dir, include_covers)
                    if export_path:
                        results[book_id] = export_path
                    else:
                        results[book_id] = "Export failed"
                except Exception as e:
                    results[book_id] = f"Error: {str(e)}"
                
                progress.update(task, advance=1)
        
        successful_exports = sum(1 for result in results.values() if not result.startswith("Error") and result != "Export failed")
        console.print(f"[bold green]Batch export complete: {successful_exports}/{len(book_ids)} books exported[/bold green]")
        
        return results
    
    def export_genre_collection(self, genre: str, output_dir: Optional[str] = None,
                              max_books: Optional[int] = None) -> Dict[str, str]:
        """
        Export all books of a specific genre.
        
        Args:
            genre: Genre to export
            output_dir: Directory to export to
            max_books: Maximum number of books to export
            
        Returns:
            Dictionary mapping book_id to export path
        """
        # Get books of the specified genre
        books = self.db_manager.get_books(genre=genre, status="completed", limit=max_books)
        
        if not books:
            console.print(f"[yellow]No books found for genre: {genre}[/yellow]")
            return {}
        
        # Create genre-specific output directory
        if not output_dir:
            output_dir = os.path.join(self.export_dir, f"{genre}_Collection")
        
        book_ids = [book["book_id"] for book in books]
        return self.batch_export_books(book_ids, output_dir)
    
    def get_library_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the book library.
        
        Returns:
            Dictionary containing library statistics
        """
        stats = self.db_manager.get_database_stats()
        epub_stats = self.epub_db_manager.get_epub_stats()
        
        return {
            "total_books": stats["total_books"],
            "books_with_epubs": stats["epubs_stored"],
            "books_with_covers": stats["covers_stored"],
            "total_storage_mb": stats["database_size_bytes"] / (1024 * 1024),
            "epub_storage_mb": epub_stats["total_compressed_size_bytes"] / (1024 * 1024),
            "storage_saved_mb": epub_stats["storage_saved_mb"],
            "avg_compression_ratio": epub_stats["avg_compression_ratio"],
            "total_accesses": epub_stats["total_accesses"],
            "genres": list(stats["genre_counts"].keys()),
            "most_popular_genre": max(stats["genre_counts"].items(), key=lambda x: x[1])[0] if stats["genre_counts"] else None
        }
    
    def cleanup_exported_books(self, older_than_days: int = 7) -> int:
        """
        Clean up old exported books from the file system.
        
        Args:
            older_than_days: Remove exports older than this many days
            
        Returns:
            Number of directories cleaned up
        """
        if not os.path.exists(self.export_dir):
            return 0
        
        import time
        cutoff_time = time.time() - (older_than_days * 24 * 60 * 60)
        cleaned_count = 0
        
        try:
            for item in os.listdir(self.export_dir):
                item_path = os.path.join(self.export_dir, item)
                if os.path.isdir(item_path):
                    # Check if directory is older than cutoff
                    if os.path.getctime(item_path) < cutoff_time:
                        shutil.rmtree(item_path)
                        cleaned_count += 1
        except Exception as e:
            console.print(f"[yellow]Warning: Error during cleanup: {str(e)}[/yellow]")
        
        if cleaned_count > 0:
            console.print(f"[bold green]Cleaned up {cleaned_count} old exported book directories[/bold green]")
        
        return cleaned_count


# Global book library manager instance
_book_library_manager = None

def get_book_library_manager() -> BookLibraryManager:
    """Get the global book library manager instance."""
    global _book_library_manager
    if _book_library_manager is None:
        _book_library_manager = BookLibraryManager()
    return _book_library_manager
