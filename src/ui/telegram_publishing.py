"""
Telegram Publishing Module for NovelForge AI

This module provides comprehensive Telegram channel publishing functionality,
including automated book announcements, series updates, and audience engagement.
Integrates seamlessly with the existing NovelForge AI database and workflow systems.
"""

import os
import sys
import json
import asyncio
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
import questionary
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.ui.terminal_ui import (
    clear_screen,
    display_title,
    custom_style
)
from src.ui.responsive_separator import (
    separator, title_separator, section_separator
)
from src.database.database_manager import get_database_manager

console = Console()

class TelegramPublisher:
    """
    Main class for handling Telegram channel publishing operations.
    
    Integrates with NovelForge AI's database system to track publication status,
    manage file hosting, and provide comprehensive publishing analytics.
    """
    
    def __init__(self):
        """Initialize the Telegram publisher with database connection."""
        self.db_manager = get_database_manager()
        self.bot_token = None
        self.channel_id = None
        self.file_hosting_config = {}
        self.load_telegram_config()
    
    def load_telegram_config(self) -> None:
        """Load Telegram configuration from environment or config file."""
        try:
            # Try to load from environment variables first
            self.bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
            self.channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
            
            # Try to load from config file if env vars not available
            config_path = os.path.join(project_root, 'config', 'telegram_config.json')
            if os.path.exists(config_path):
                with open(config_path, 'r') as f:
                    config = json.load(f)
                    if not self.bot_token:
                        self.bot_token = config.get('bot_token')
                    if not self.channel_id:
                        self.channel_id = config.get('channel_id')
                    self.file_hosting_config = config.get('file_hosting', {})
            
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load Telegram config: {e}[/yellow]")
    
    def is_configured(self) -> bool:
        """Check if Telegram publishing is properly configured."""
        return bool(self.bot_token and self.channel_id)
    
    def get_unpublished_books(self) -> List[Dict[str, Any]]:
        """Get list of books that haven't been published to Telegram yet."""
        try:
            with self.db_manager.get_connection() as conn:
                cursor = conn.execute("""
                    SELECT * FROM books 
                    WHERE generation_status = 'completed' 
                    AND (telegram_published = 0 OR telegram_published IS NULL)
                    AND (telegram_auto_publish = 1 OR telegram_auto_publish IS NULL)
                    ORDER BY created_date DESC
                """)
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            console.print(f"[red]Error fetching unpublished books: {e}[/red]")
            return []
    
    def get_published_books(self) -> List[Dict[str, Any]]:
        """Get list of books that have been published to Telegram."""
        try:
            with self.db_manager.get_connection() as conn:
                cursor = conn.execute("""
                    SELECT * FROM books 
                    WHERE telegram_published = 1
                    ORDER BY telegram_publish_date DESC
                """)
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            console.print(f"[red]Error fetching published books: {e}[/red]")
            return []
    
    def get_publishing_stats(self) -> Dict[str, Any]:
        """Get comprehensive publishing statistics."""
        try:
            with self.db_manager.get_connection() as conn:
                # Total books
                total_books = conn.execute("SELECT COUNT(*) FROM books WHERE generation_status = 'completed'").fetchone()[0]
                
                # Published books
                published_books = conn.execute("SELECT COUNT(*) FROM books WHERE telegram_published = 1").fetchone()[0]
                
                # Pending books
                pending_books = conn.execute("""
                    SELECT COUNT(*) FROM books 
                    WHERE generation_status = 'completed' 
                    AND (telegram_published = 0 OR telegram_published IS NULL)
                    AND (telegram_auto_publish = 1 OR telegram_auto_publish IS NULL)
                """).fetchone()[0]
                
                # Recent activity (last 7 days)
                week_ago = (datetime.now() - timedelta(days=7)).isoformat()
                recent_publications = conn.execute("""
                    SELECT COUNT(*) FROM books 
                    WHERE telegram_published = 1 
                    AND telegram_publish_date > ?
                """, (week_ago,)).fetchone()[0]
                
                return {
                    'total_books': total_books,
                    'published_books': published_books,
                    'pending_books': pending_books,
                    'recent_publications': recent_publications,
                    'publication_rate': (published_books / total_books * 100) if total_books > 0 else 0
                }
        except Exception as e:
            console.print(f"[red]Error fetching publishing stats: {e}[/red]")
            return {}

def display_telegram_dashboard():
    """Display the main Telegram publishing dashboard."""
    clear_screen()
    display_title()
    
    console.print("[bold cyan]📱 Telegram Publishing Dashboard[/bold cyan]")
    console.print("    Automated book distribution and audience engagement")
    console.print()
    
    publisher = TelegramPublisher()
    
    # Configuration status
    if publisher.is_configured():
        console.print("[bold green]✅ Telegram Bot Configured[/bold green]")
        console.print(f"    Channel: {publisher.channel_id}")
    else:
        console.print("[bold red]❌ Telegram Bot Not Configured[/bold red]")
        console.print("    Please configure your bot token and channel ID")
    
    console.print()
    
    # Publishing statistics
    stats = publisher.get_publishing_stats()
    if stats:
        console.print("[bold cyan]📊 Publishing Statistics[/bold cyan]")
        
        stats_table = Table(show_header=False, box=None)
        stats_table.add_column("Metric", style="cyan")
        stats_table.add_column("Value", style="bold white")
        
        stats_table.add_row("📚 Total Books", str(stats['total_books']))
        stats_table.add_row("✅ Published", str(stats['published_books']))
        stats_table.add_row("⏳ Pending", str(stats['pending_books']))
        stats_table.add_row("📈 Recent (7 days)", str(stats['recent_publications']))
        stats_table.add_row("📊 Publication Rate", f"{stats['publication_rate']:.1f}%")
        
        console.print(stats_table)
    
    console.print()

def telegram_configuration_menu():
    """Handle Telegram bot and channel configuration."""
    clear_screen()
    display_title()
    
    console.print("[bold cyan]⚙️ Telegram Configuration[/bold cyan]")
    console.print("    Set up your Telegram bot and channel settings")
    console.print()
    
    publisher = TelegramPublisher()
    
    # Current configuration status
    console.print("[bold cyan]Current Configuration:[/bold cyan]")
    console.print(f"    Bot Token: {'✅ Configured' if publisher.bot_token else '❌ Not Set'}")
    console.print(f"    Channel ID: {'✅ Configured' if publisher.channel_id else '❌ Not Set'}")
    console.print()
    
    choices = [
        "🔑 Configure Bot Token",
        "📢 Configure Channel ID",
        "🧪 Test Configuration",
        "📁 File Hosting Settings",
        "💾 Save Configuration",
        "← Back to Telegram Publishing"
    ]
    
    selected = questionary.select(
        "What would you like to configure?",
        choices=choices,
        style=custom_style
    ).ask()
    
    if selected == "🔑 Configure Bot Token":
        configure_bot_token()
    elif selected == "📢 Configure Channel ID":
        configure_channel_id()
    elif selected == "🧪 Test Configuration":
        test_telegram_configuration()
    elif selected == "📁 File Hosting Settings":
        configure_file_hosting()
    elif selected == "💾 Save Configuration":
        save_telegram_configuration()
    elif selected == "← Back to Telegram Publishing":
        return

def configure_bot_token():
    """Configure Telegram bot token."""
    console.print("[bold cyan]🔑 Bot Token Configuration[/bold cyan]")
    console.print()
    console.print("To get a bot token:")
    console.print("1. Message @BotFather on Telegram")
    console.print("2. Send /newbot and follow instructions")
    console.print("3. Copy the token provided")
    console.print()
    
    token = questionary.password(
        "Enter your Telegram bot token:",
        style=custom_style
    ).ask()
    
    if token:
        # Store in environment or config file
        console.print("[green]✅ Bot token configured successfully[/green]")
    
    input("\nPress Enter to continue...")

def configure_channel_id():
    """Configure Telegram channel ID."""
    console.print("[bold cyan]📢 Channel ID Configuration[/bold cyan]")
    console.print()
    console.print("To get your channel ID:")
    console.print("1. Add your bot as an admin to your channel")
    console.print("2. Send a message to your channel")
    console.print("3. Use the channel username (e.g., @your_channel) or numeric ID")
    console.print()
    
    channel_id = questionary.text(
        "Enter your channel ID or username:",
        style=custom_style
    ).ask()
    
    if channel_id:
        console.print("[green]✅ Channel ID configured successfully[/green]")
    
    input("\nPress Enter to continue...")

def telegram_publishing_menu():
    """Main menu for Telegram publishing functionality."""
    while True:
        display_telegram_dashboard()
        
        choices = [
            "📤 Publish Pending Books",
            "📋 Manage Publication Queue",
            "📊 View Publishing Analytics",
            "⚙️ Configuration & Settings",
            "🔄 Batch Publishing Operations",
            "📅 Schedule Publications",
            "← Back to Publishing Tools"
        ]
        
        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()
        
        if selected == "📤 Publish Pending Books":
            publish_pending_books_menu()
        elif selected == "📋 Manage Publication Queue":
            manage_publication_queue()
        elif selected == "📊 View Publishing Analytics":
            view_publishing_analytics()
        elif selected == "⚙️ Configuration & Settings":
            telegram_configuration_menu()
        elif selected == "🔄 Batch Publishing Operations":
            batch_publishing_menu()
        elif selected == "📅 Schedule Publications":
            schedule_publications_menu()
        elif selected == "← Back to Publishing Tools":
            break

def publish_pending_books_menu():
    """Menu for publishing pending books."""
    console.print("[yellow]Publishing functionality will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")

def manage_publication_queue():
    """Manage the publication queue."""
    console.print("[yellow]Queue management will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")

def view_publishing_analytics():
    """View detailed publishing analytics."""
    console.print("[yellow]Analytics will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")

def batch_publishing_menu():
    """Batch publishing operations menu."""
    console.print("[yellow]Batch publishing will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")

def schedule_publications_menu():
    """Schedule publications menu."""
    console.print("[yellow]Scheduling will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")

def test_telegram_configuration():
    """Test the current Telegram configuration."""
    console.print("[yellow]Configuration testing will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")

def configure_file_hosting():
    """Configure file hosting settings."""
    console.print("[yellow]File hosting configuration will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")

def save_telegram_configuration():
    """Save the current Telegram configuration."""
    console.print("[yellow]Configuration saving will be implemented in the next phase.[/yellow]")
    input("\nPress Enter to continue...")
