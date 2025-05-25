"""
Telegram Bot Manager for NovelForge AI

This module handles the core Telegram Bot API integration, including:
- Bot authentication and configuration
- Message posting and file uploads
- Channel management and analytics
- Error handling and rate limiting
- File hosting integration for EPUB distribution
"""

import os
import json
import asyncio
import aiohttp
import aiofiles
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import base64
from pathlib import Path

class TelegramBotManager:
    """
    Core Telegram Bot API manager with async support for efficient operations.
    
    Handles all direct interactions with the Telegram Bot API, including
    message posting, file uploads, and channel management.
    """
    
    def __init__(self, bot_token: str):
        """
        Initialize the Telegram bot manager.
        
        Args:
            bot_token: Telegram bot token from BotFather
        """
        self.bot_token = bot_token
        self.base_url = f"https://api.telegram.org/bot{bot_token}"
        self.session = None
        self.rate_limit_delay = 1.0  # Seconds between requests
        
    async def __aenter__(self):
        """Async context manager entry."""
        self.session = aiohttp.ClientSession()
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            await self.session.close()
    
    async def test_bot_connection(self) -> Tuple[bool, str]:
        """
        Test the bot connection and get bot information.
        
        Returns:
            Tuple of (success, message/error)
        """
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{self.base_url}/getMe") as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('ok'):
                            bot_info = data.get('result', {})
                            bot_name = bot_info.get('first_name', 'Unknown')
                            bot_username = bot_info.get('username', 'Unknown')
                            return True, f"Connected to bot: {bot_name} (@{bot_username})"
                        else:
                            return False, f"Bot API error: {data.get('description', 'Unknown error')}"
                    else:
                        return False, f"HTTP error: {response.status}"
        except Exception as e:
            return False, f"Connection error: {str(e)}"
    
    async def get_channel_info(self, channel_id: str) -> Tuple[bool, Dict[str, Any]]:
        """
        Get information about a channel.
        
        Args:
            channel_id: Channel ID or username
            
        Returns:
            Tuple of (success, channel_info)
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/getChat"
                params = {"chat_id": channel_id}
                
                async with session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        if data.get('ok'):
                            return True, data.get('result', {})
                        else:
                            return False, {"error": data.get('description', 'Unknown error')}
                    else:
                        return False, {"error": f"HTTP error: {response.status}"}
        except Exception as e:
            return False, {"error": f"Connection error: {str(e)}"}
    
    async def send_message(self, channel_id: str, text: str, 
                          parse_mode: str = "HTML") -> Tuple[bool, Dict[str, Any]]:
        """
        Send a text message to a channel.
        
        Args:
            channel_id: Channel ID or username
            text: Message text
            parse_mode: Message formatting (HTML or Markdown)
            
        Returns:
            Tuple of (success, response_data)
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/sendMessage"
                data = {
                    "chat_id": channel_id,
                    "text": text,
                    "parse_mode": parse_mode
                }
                
                async with session.post(url, json=data) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        if response_data.get('ok'):
                            return True, response_data.get('result', {})
                        else:
                            return False, {"error": response_data.get('description', 'Unknown error')}
                    else:
                        return False, {"error": f"HTTP error: {response.status}"}
        except Exception as e:
            return False, {"error": f"Connection error: {str(e)}"}
    
    async def send_photo(self, channel_id: str, photo_data: bytes, 
                        caption: str = "", parse_mode: str = "HTML") -> Tuple[bool, Dict[str, Any]]:
        """
        Send a photo to a channel.
        
        Args:
            channel_id: Channel ID or username
            photo_data: Photo binary data
            caption: Photo caption
            parse_mode: Caption formatting
            
        Returns:
            Tuple of (success, response_data)
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/sendPhoto"
                
                data = aiohttp.FormData()
                data.add_field('chat_id', channel_id)
                data.add_field('photo', photo_data, filename='cover.jpg', content_type='image/jpeg')
                if caption:
                    data.add_field('caption', caption)
                    data.add_field('parse_mode', parse_mode)
                
                async with session.post(url, data=data) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        if response_data.get('ok'):
                            return True, response_data.get('result', {})
                        else:
                            return False, {"error": response_data.get('description', 'Unknown error')}
                    else:
                        return False, {"error": f"HTTP error: {response.status}"}
        except Exception as e:
            return False, {"error": f"Connection error: {str(e)}"}
    
    async def send_document(self, channel_id: str, document_data: bytes, 
                           filename: str, caption: str = "", 
                           parse_mode: str = "HTML") -> Tuple[bool, Dict[str, Any]]:
        """
        Send a document to a channel.
        
        Args:
            channel_id: Channel ID or username
            document_data: Document binary data
            filename: Document filename
            caption: Document caption
            parse_mode: Caption formatting
            
        Returns:
            Tuple of (success, response_data)
        """
        try:
            async with aiohttp.ClientSession() as session:
                url = f"{self.base_url}/sendDocument"
                
                data = aiohttp.FormData()
                data.add_field('chat_id', channel_id)
                data.add_field('document', document_data, filename=filename, 
                              content_type='application/epub+zip')
                if caption:
                    data.add_field('caption', caption)
                    data.add_field('parse_mode', parse_mode)
                
                async with session.post(url, data=data) as response:
                    if response.status == 200:
                        response_data = await response.json()
                        if response_data.get('ok'):
                            return True, response_data.get('result', {})
                        else:
                            return False, {"error": response_data.get('description', 'Unknown error')}
                    else:
                        return False, {"error": f"HTTP error: {response.status}"}
        except Exception as e:
            return False, {"error": f"Connection error: {str(e)}"}

class TelegramMessageFormatter:
    """
    Formats book information into attractive Telegram messages.
    
    Creates engaging posts with proper formatting, emojis, and structure
    that work well in Telegram channels.
    """
    
    @staticmethod
    def format_book_announcement(book_data: Dict[str, Any]) -> str:
        """
        Format a book announcement message.
        
        Args:
            book_data: Book information from database
            
        Returns:
            Formatted message text
        """
        title = book_data.get('title', 'Untitled')
        author = book_data.get('author', 'Unknown Author')
        genre = book_data.get('genre', 'Fiction')
        description = book_data.get('description', '')
        
        # Truncate description if too long
        if len(description) > 300:
            description = description[:297] + "..."
        
        message = f"""📚 <b>New Book Release!</b>
        
<b>📖 {title}</b>
<i>by {author}</i>

🎭 <b>Genre:</b> {genre}

📝 <b>Description:</b>
{description}

✨ <i>Generated with AI-powered creativity</i>

#NewRelease #{genre.replace(' ', '')} #AIGenerated"""
        
        return message
    
    @staticmethod
    def format_series_announcement(series_data: Dict[str, Any], books: List[Dict[str, Any]]) -> str:
        """
        Format a series announcement message.
        
        Args:
            series_data: Series information
            books: List of books in the series
            
        Returns:
            Formatted message text
        """
        series_title = series_data.get('series_title', 'Untitled Series')
        book_count = len(books)
        
        message = f"""📚 <b>New Series Alert!</b>
        
<b>📖 {series_title}</b>
<i>{book_count} Books Available</i>

📚 <b>Books in this series:</b>"""
        
        for i, book in enumerate(books, 1):
            book_title = book.get('title', f'Book {i}')
            message += f"\n{i}. {book_title}"
        
        message += f"""

✨ <i>Complete series generated with AI</i>

#NewSeries #AIGenerated #BookSeries"""
        
        return message

class FileHostingManager:
    """
    Manages file hosting for EPUB files that exceed Telegram's 50MB limit.
    
    Provides integration with various file hosting services and generates
    download links for large files.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize file hosting manager.
        
        Args:
            config: File hosting configuration
        """
        self.config = config or {}
        self.hosting_service = self.config.get('service', 'local')
    
    async def upload_file(self, file_data: bytes, filename: str) -> Tuple[bool, str]:
        """
        Upload a file to the configured hosting service.
        
        Args:
            file_data: File binary data
            filename: Original filename
            
        Returns:
            Tuple of (success, download_url)
        """
        if self.hosting_service == 'local':
            return await self._upload_to_local(file_data, filename)
        else:
            # Future: Add support for cloud hosting services
            return False, "Hosting service not configured"
    
    async def _upload_to_local(self, file_data: bytes, filename: str) -> Tuple[bool, str]:
        """
        Save file locally and generate a local URL.
        
        Args:
            file_data: File binary data
            filename: Original filename
            
        Returns:
            Tuple of (success, local_path)
        """
        try:
            # Create uploads directory if it doesn't exist
            uploads_dir = Path("uploads/telegram")
            uploads_dir.mkdir(parents=True, exist_ok=True)
            
            # Generate unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"{timestamp}_{filename}"
            file_path = uploads_dir / unique_filename
            
            # Save file
            async with aiofiles.open(file_path, 'wb') as f:
                await f.write(file_data)
            
            return True, str(file_path)
        except Exception as e:
            return False, f"Upload error: {str(e)}"

def get_telegram_bot_manager(bot_token: str) -> TelegramBotManager:
    """
    Factory function to create a TelegramBotManager instance.
    
    Args:
        bot_token: Telegram bot token
        
    Returns:
        TelegramBotManager instance
    """
    return TelegramBotManager(bot_token)
