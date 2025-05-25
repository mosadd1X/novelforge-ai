"""
Telegram File Distribution Manager for NovelForge AI

Handles optimal file distribution strategy including:
- Multi-format package creation (EPUB, PDF, TXT)
- File size optimization for Telegram's 50MB limit
- External hosting integration for large files
- Smart compression and format selection
"""

import os
import zipfile
import json
from typing import Dict, List, Any, Optional, Tuple
from pathlib import Path
import base64
from datetime import datetime

class TelegramFileManager:
    """
    Manages file distribution strategy for Telegram publishing.
    
    Handles multiple formats, size optimization, and external hosting
    to provide the best user experience within Telegram's constraints.
    """
    
    def __init__(self):
        """Initialize the file manager."""
        self.max_telegram_size = 45 * 1024 * 1024  # 45MB (buffer under 50MB limit)
        self.supported_formats = ['epub', 'pdf', 'txt']
        self.hosting_config = self.load_hosting_config()
    
    def load_hosting_config(self) -> Dict[str, Any]:
        """Load file hosting configuration."""
        return {
            'use_external_hosting': True,
            'hosting_service': 'github_releases',  # Free option for students
            'local_backup': True,
            'compression_level': 6,  # Balance between size and speed
            'formats_priority': ['epub', 'pdf', 'txt']  # Order of preference
        }
    
    def create_book_package(self, book_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create optimized file package for a book.
        
        Args:
            book_data: Book information from database
            
        Returns:
            Package information with file paths and distribution strategy
        """
        book_id = book_data.get('book_id', '')
        title = book_data.get('title', 'Untitled')
        
        package_info = {
            'book_id': book_id,
            'title': title,
            'files': {},
            'telegram_files': [],
            'external_files': [],
            'total_size': 0,
            'distribution_strategy': 'direct'  # direct, external, hybrid
        }
        
        # Generate all available formats
        formats = self.generate_book_formats(book_data)
        
        # Calculate total size
        total_size = sum(format_info['size'] for format_info in formats.values())
        package_info['total_size'] = total_size
        package_info['files'] = formats
        
        # Determine distribution strategy
        if total_size <= self.max_telegram_size:
            package_info['distribution_strategy'] = 'direct'
            package_info['telegram_files'] = list(formats.keys())
        else:
            package_info['distribution_strategy'] = 'hybrid'
            # Send EPUB directly, host complete package externally
            if 'epub' in formats and formats['epub']['size'] <= self.max_telegram_size:
                package_info['telegram_files'] = ['epub']
                package_info['external_files'] = ['complete_package']
            else:
                package_info['distribution_strategy'] = 'external'
                package_info['external_files'] = ['complete_package']
        
        return package_info
    
    def generate_book_formats(self, book_data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
        """
        Generate all available formats for a book.
        
        Args:
            book_data: Book information
            
        Returns:
            Dictionary of format information
        """
        formats = {}
        book_id = book_data.get('book_id', '')
        title = book_data.get('title', 'Untitled')
        
        # EPUB format (primary)
        epub_info = self.get_epub_info(book_data)
        if epub_info:
            formats['epub'] = epub_info
        
        # PDF format (generated from EPUB if needed)
        pdf_info = self.generate_pdf_format(book_data)
        if pdf_info:
            formats['pdf'] = pdf_info
        
        # TXT format (plain text version)
        txt_info = self.generate_txt_format(book_data)
        if txt_info:
            formats['txt'] = txt_info
        
        return formats
    
    def get_epub_info(self, book_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Get EPUB file information."""
        try:
            # Try database first
            epub_base64 = book_data.get('epub_base64')
            if epub_base64:
                epub_data = base64.b64decode(epub_base64)
                return {
                    'format': 'epub',
                    'size': len(epub_data),
                    'data': epub_data,
                    'filename': f"{book_data.get('title', 'book')}.epub",
                    'source': 'database'
                }
            
            # Try file system
            possible_paths = [
                f"output/{book_data.get('book_id', '')}/{book_data.get('title', 'book')}.epub",
                f"output/{book_data.get('title', 'book')}.epub"
            ]
            
            for path in possible_paths:
                if os.path.exists(path):
                    size = os.path.getsize(path)
                    with open(path, 'rb') as f:
                        data = f.read()
                    return {
                        'format': 'epub',
                        'size': size,
                        'data': data,
                        'filename': os.path.basename(path),
                        'source': 'filesystem'
                    }
            
            return None
            
        except Exception as e:
            print(f"Error getting EPUB info: {e}")
            return None
    
    def generate_pdf_format(self, book_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate PDF format from EPUB (placeholder for future implementation)."""
        # For now, return None - PDF generation would require additional libraries
        # Future implementation could use weasyprint or similar
        return None
    
    def generate_txt_format(self, book_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Generate plain text format from book content."""
        try:
            # Extract text from novel_data_json
            novel_data_json = book_data.get('novel_data_json')
            if not novel_data_json:
                return None
            
            novel_data = json.loads(novel_data_json)
            chapters = novel_data.get('chapters', [])
            
            # Create plain text version
            text_content = []
            text_content.append(f"Title: {book_data.get('title', 'Untitled')}")
            text_content.append(f"Author: {book_data.get('author', 'Unknown')}")
            text_content.append(f"Genre: {book_data.get('genre', 'Fiction')}")
            text_content.append("\n" + "="*50 + "\n")
            
            for i, chapter in enumerate(chapters, 1):
                chapter_title = chapter.get('title', f'Chapter {i}')
                chapter_content = chapter.get('content', '')
                
                text_content.append(f"Chapter {i}: {chapter_title}")
                text_content.append("-" * 30)
                text_content.append(chapter_content)
                text_content.append("\n")
            
            full_text = "\n".join(text_content)
            text_bytes = full_text.encode('utf-8')
            
            return {
                'format': 'txt',
                'size': len(text_bytes),
                'data': text_bytes,
                'filename': f"{book_data.get('title', 'book')}.txt",
                'source': 'generated'
            }
            
        except Exception as e:
            print(f"Error generating TXT format: {e}")
            return None
    
    def create_complete_package(self, package_info: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Create a complete ZIP package with all formats.
        
        Args:
            package_info: Package information from create_book_package
            
        Returns:
            ZIP package information
        """
        try:
            title = package_info['title']
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            
            # Create temporary ZIP file
            zip_filename = f"{safe_title}_Complete.zip"
            zip_path = Path("temp") / zip_filename
            zip_path.parent.mkdir(exist_ok=True)
            
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # Add all available formats
                for format_name, format_info in package_info['files'].items():
                    if format_info and format_info.get('data'):
                        zipf.writestr(format_info['filename'], format_info['data'])
                
                # Add README
                readme_content = self.create_package_readme(package_info)
                zipf.writestr("README.txt", readme_content)
            
            # Get ZIP file info
            zip_size = zip_path.stat().st_size
            with open(zip_path, 'rb') as f:
                zip_data = f.read()
            
            # Clean up temp file
            zip_path.unlink()
            
            return {
                'format': 'zip',
                'size': zip_size,
                'data': zip_data,
                'filename': zip_filename,
                'source': 'generated'
            }
            
        except Exception as e:
            print(f"Error creating complete package: {e}")
            return None
    
    def create_package_readme(self, package_info: Dict[str, Any]) -> str:
        """Create README content for complete packages."""
        title = package_info['title']
        
        readme = f"""📚 {title} - Complete Package
{'='*50}

This package contains your book in multiple formats for maximum compatibility:

📱 EPUB Format (.epub)
   - Best for e-readers (Kindle, Kobo, etc.)
   - Supports reflowable text and custom fonts
   - Recommended for mobile reading

📄 PDF Format (.pdf)
   - Fixed layout, preserves formatting
   - Best for printing or desktop reading
   - Universal compatibility

📝 TXT Format (.txt)
   - Plain text version
   - Smallest file size
   - Compatible with any text editor

🤖 Generated with NovelForge AI
   - Professional quality AI-generated content
   - Complete with covers and formatting
   - Part of our growing digital library

📞 Support & Feedback:
   - Telegram: @your_channel
   - Report issues or request formats

Thank you for reading! 📖
"""
        return readme
    
    def get_distribution_message(self, package_info: Dict[str, Any]) -> str:
        """
        Generate distribution message based on strategy.
        
        Args:
            package_info: Package information
            
        Returns:
            Formatted message for Telegram post
        """
        strategy = package_info['distribution_strategy']
        title = package_info['title']
        
        if strategy == 'direct':
            return f"""⬇️ **Download Options:**

📱 **EPUB** (Recommended): Direct download
📄 **PDF**: Direct download  
📝 **TXT**: Direct download

💡 **Tip**: EPUB works best on phones and e-readers!"""
        
        elif strategy == 'hybrid':
            return f"""⬇️ **Download Options:**

📱 **EPUB** (Quick Download): ⬇️ Available below
📦 **Complete Package** (All Formats): [External Link]

💡 **Tip**: Download EPUB for instant reading, or get the complete package for all formats!"""
        
        else:  # external
            return f"""⬇️ **Download Options:**

📦 **Complete Package** (All Formats): [External Link]
   • EPUB (e-readers)
   • PDF (printing/desktop)
   • TXT (plain text)

💡 **Note**: Large file hosted externally for your convenience!"""

def get_optimal_file_strategy(book_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Get optimal file distribution strategy for a book.
    
    Args:
        book_data: Book information from database
        
    Returns:
        Complete distribution strategy
    """
    file_manager = TelegramFileManager()
    return file_manager.create_book_package(book_data)
