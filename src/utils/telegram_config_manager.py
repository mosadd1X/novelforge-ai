"""
Telegram Configuration Manager for NovelForge AI

This module handles all Telegram-related configuration management,
including bot tokens, channel settings, publishing preferences,
and file hosting configuration.
"""

import os
import json
from typing import Dict, Any, Optional, List
from pathlib import Path
from datetime import datetime

class TelegramConfigManager:
    """
    Manages Telegram configuration settings with secure storage and validation.
    
    Handles bot tokens, channel configurations, publishing preferences,
    and file hosting settings with proper security considerations.
    """
    
    def __init__(self):
        """Initialize the configuration manager."""
        self.config_dir = Path("config")
        self.config_file = self.config_dir / "telegram_config.json"
        self.env_file = Path(".env")
        self.config_data = {}
        self.load_configuration()
    
    def load_configuration(self) -> None:
        """Load configuration from file and environment variables."""
        # Create config directory if it doesn't exist
        self.config_dir.mkdir(exist_ok=True)
        
        # Load from JSON file
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    self.config_data = json.load(f)
            except Exception as e:
                print(f"Warning: Could not load Telegram config: {e}")
                self.config_data = {}
        
        # Override with environment variables if available
        env_token = os.getenv('TELEGRAM_BOT_TOKEN')
        env_channel = os.getenv('TELEGRAM_CHANNEL_ID')
        
        if env_token:
            self.config_data['bot_token'] = env_token
        if env_channel:
            self.config_data['channel_id'] = env_channel
    
    def save_configuration(self) -> bool:
        """
        Save configuration to file.
        
        Returns:
            True if successful, False otherwise
        """
        try:
            # Ensure config directory exists
            self.config_dir.mkdir(exist_ok=True)
            
            # Save to JSON file (without sensitive data)
            safe_config = self.config_data.copy()
            
            # Remove sensitive data from file storage
            if 'bot_token' in safe_config:
                safe_config['bot_token'] = '***CONFIGURED***'
            
            with open(self.config_file, 'w') as f:
                json.dump(safe_config, f, indent=2)
            
            return True
        except Exception as e:
            print(f"Error saving Telegram config: {e}")
            return False
    
    def set_bot_token(self, token: str) -> bool:
        """
        Set the Telegram bot token.
        
        Args:
            token: Bot token from BotFather
            
        Returns:
            True if valid and set, False otherwise
        """
        if not token or not token.strip():
            return False
        
        # Basic validation
        if not token.startswith('bot') and ':' not in token:
            return False
        
        self.config_data['bot_token'] = token.strip()
        return True
    
    def set_channel_id(self, channel_id: str) -> bool:
        """
        Set the Telegram channel ID.
        
        Args:
            channel_id: Channel ID or username
            
        Returns:
            True if valid and set, False otherwise
        """
        if not channel_id or not channel_id.strip():
            return False
        
        # Clean up the channel ID
        channel_id = channel_id.strip()
        if channel_id.startswith('@'):
            # Username format
            self.config_data['channel_id'] = channel_id
        elif channel_id.startswith('-'):
            # Numeric ID format
            self.config_data['channel_id'] = channel_id
        else:
            # Try to add @ prefix for username
            self.config_data['channel_id'] = f"@{channel_id}"
        
        return True
    
    def get_bot_token(self) -> Optional[str]:
        """Get the configured bot token."""
        return self.config_data.get('bot_token')
    
    def get_channel_id(self) -> Optional[str]:
        """Get the configured channel ID."""
        return self.config_data.get('channel_id')
    
    def is_configured(self) -> bool:
        """Check if basic Telegram configuration is complete."""
        return bool(self.get_bot_token() and self.get_channel_id())
    
    def get_publishing_settings(self) -> Dict[str, Any]:
        """Get publishing-related settings."""
        return self.config_data.get('publishing_settings', {
            'auto_publish_new_books': True,
            'auto_publish_series': True,
            'include_covers': True,
            'include_epub_files': True,
            'max_file_size_mb': 45,  # Leave buffer under 50MB limit
            'posting_schedule': 'immediate',
            'engagement_features': True
        })
    
    def set_publishing_settings(self, settings: Dict[str, Any]) -> None:
        """Set publishing-related settings."""
        self.config_data['publishing_settings'] = settings
    
    def get_file_hosting_config(self) -> Dict[str, Any]:
        """Get file hosting configuration."""
        return self.config_data.get('file_hosting', {
            'service': 'local',
            'max_local_storage_gb': 10,
            'cleanup_after_days': 30,
            'external_hosting': {
                'enabled': False,
                'service': None,
                'api_key': None,
                'base_url': None
            }
        })
    
    def set_file_hosting_config(self, config: Dict[str, Any]) -> None:
        """Set file hosting configuration."""
        self.config_data['file_hosting'] = config
    
    def get_message_templates(self) -> Dict[str, str]:
        """Get message templates for different post types."""
        return self.config_data.get('message_templates', {
            'book_announcement': """📚 <b>New Book Release!</b>

<b>📖 {title}</b>
<i>by {author}</i>

🎭 <b>Genre:</b> {genre}

📝 <b>Description:</b>
{description}

✨ <i>Generated with AI-powered creativity</i>

#NewRelease #{genre_tag} #AIGenerated""",
            
            'series_announcement': """📚 <b>New Series Alert!</b>

<b>📖 {series_title}</b>
<i>{book_count} Books Available</i>

📚 <b>Books in this series:</b>
{book_list}

✨ <i>Complete series generated with AI</i>

#NewSeries #AIGenerated #BookSeries""",
            
            'series_update': """📚 <b>Series Update!</b>

<b>📖 New book added to {series_title}</b>

📖 <b>{book_title}</b>
<i>Book {book_number} in the series</i>

🎭 <b>Genre:</b> {genre}

#SeriesUpdate #{genre_tag} #AIGenerated"""
        })
    
    def set_message_templates(self, templates: Dict[str, str]) -> None:
        """Set custom message templates."""
        self.config_data['message_templates'] = templates
    
    def get_analytics_settings(self) -> Dict[str, Any]:
        """Get analytics and tracking settings."""
        return self.config_data.get('analytics', {
            'track_engagement': True,
            'track_downloads': True,
            'generate_reports': True,
            'report_frequency': 'weekly'
        })
    
    def set_analytics_settings(self, settings: Dict[str, Any]) -> None:
        """Set analytics and tracking settings."""
        self.config_data['analytics'] = settings
    
    def add_channel(self, channel_id: str, channel_name: str, 
                   channel_type: str = 'primary') -> bool:
        """
        Add a channel to the configuration.
        
        Args:
            channel_id: Channel ID or username
            channel_name: Human-readable channel name
            channel_type: Type of channel (primary, backup, test)
            
        Returns:
            True if added successfully
        """
        if 'channels' not in self.config_data:
            self.config_data['channels'] = []
        
        channel_config = {
            'id': channel_id,
            'name': channel_name,
            'type': channel_type,
            'added_date': datetime.now().isoformat(),
            'active': True
        }
        
        # Check if channel already exists
        for existing in self.config_data['channels']:
            if existing['id'] == channel_id:
                existing.update(channel_config)
                return True
        
        self.config_data['channels'].append(channel_config)
        return True
    
    def get_channels(self) -> List[Dict[str, Any]]:
        """Get list of configured channels."""
        return self.config_data.get('channels', [])
    
    def get_primary_channel(self) -> Optional[str]:
        """Get the primary channel ID."""
        channels = self.get_channels()
        for channel in channels:
            if channel.get('type') == 'primary' and channel.get('active'):
                return channel['id']
        
        # Fallback to main channel_id if no primary channel found
        return self.get_channel_id()
    
    def export_config(self, include_sensitive: bool = False) -> Dict[str, Any]:
        """
        Export configuration for backup or sharing.
        
        Args:
            include_sensitive: Whether to include sensitive data like tokens
            
        Returns:
            Configuration dictionary
        """
        config_copy = self.config_data.copy()
        
        if not include_sensitive:
            # Remove sensitive information
            if 'bot_token' in config_copy:
                config_copy['bot_token'] = '***REDACTED***'
            
            # Remove API keys from file hosting config
            if 'file_hosting' in config_copy:
                hosting = config_copy['file_hosting']
                if 'external_hosting' in hosting and 'api_key' in hosting['external_hosting']:
                    hosting['external_hosting']['api_key'] = '***REDACTED***'
        
        return config_copy
    
    def import_config(self, config_data: Dict[str, Any], 
                     merge: bool = True) -> bool:
        """
        Import configuration from external source.
        
        Args:
            config_data: Configuration to import
            merge: Whether to merge with existing config or replace
            
        Returns:
            True if imported successfully
        """
        try:
            if merge:
                # Merge with existing configuration
                for key, value in config_data.items():
                    if key not in ['bot_token']:  # Don't overwrite sensitive data
                        self.config_data[key] = value
            else:
                # Replace configuration (keeping sensitive data)
                bot_token = self.config_data.get('bot_token')
                self.config_data = config_data.copy()
                if bot_token:
                    self.config_data['bot_token'] = bot_token
            
            return True
        except Exception as e:
            print(f"Error importing config: {e}")
            return False
    
    def validate_configuration(self) -> List[str]:
        """
        Validate the current configuration and return any issues.
        
        Returns:
            List of validation error messages
        """
        errors = []
        
        # Check bot token
        if not self.get_bot_token():
            errors.append("Bot token is not configured")
        elif not self.get_bot_token().strip():
            errors.append("Bot token is empty")
        
        # Check channel ID
        if not self.get_channel_id():
            errors.append("Channel ID is not configured")
        elif not self.get_channel_id().strip():
            errors.append("Channel ID is empty")
        
        # Check publishing settings
        pub_settings = self.get_publishing_settings()
        max_size = pub_settings.get('max_file_size_mb', 0)
        if max_size > 50:
            errors.append("Max file size exceeds Telegram's 50MB limit")
        
        return errors

def get_telegram_config_manager() -> TelegramConfigManager:
    """
    Factory function to get a TelegramConfigManager instance.
    
    Returns:
        TelegramConfigManager instance
    """
    return TelegramConfigManager()
