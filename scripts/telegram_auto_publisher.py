#!/usr/bin/env python3
"""
Automated Telegram Publisher for NovelForge AI - Free Hosting Compatible

This script is designed to run on free hosting platforms like GitHub Actions,
Railway, or Render. It checks for new books and publishes them to Telegram
without requiring 24/7 server hosting.

Perfect for students with zero budget!
"""

import os
import sys
import json
import asyncio
from datetime import datetime, timedelta
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import NovelForge AI modules
from src.database.database_manager import get_database_manager
from src.utils.telegram_bot_manager import TelegramBotManager, TelegramMessageFormatter
from src.utils.telegram_config_manager import get_telegram_config_manager

class AutoTelegramPublisher:
    """
    Automated publisher that works with free hosting platforms.

    Designed to run periodically (via cron/GitHub Actions) rather than 24/7,
    making it perfect for zero-budget deployments.
    """

    def __init__(self):
        """Initialize the auto publisher."""
        self.db_manager = get_database_manager()
        self.config_manager = get_telegram_config_manager()
        self.bot_token = self.get_bot_token()
        self.channel_id = self.get_channel_id()
        self.published_count = 0
        self.errors = []

    def get_bot_token(self) -> str:
        """Get bot token from environment or config."""
        # Try environment first (for GitHub Actions secrets)
        token = os.getenv('TELEGRAM_BOT_TOKEN')
        if token:
            return token

        # Fallback to config file
        return self.config_manager.get_bot_token()

    def get_channel_id(self) -> str:
        """Get channel ID from environment or config."""
        # Try environment first
        channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
        if channel_id:
            return channel_id

        # Fallback to config file
        return self.config_manager.get_channel_id()

    def is_configured(self) -> bool:
        """Check if publisher is properly configured."""
        return bool(self.bot_token and self.channel_id)

    def get_books_to_publish(self, limit: int = 5) -> list:
        """
        Get books that need to be published.

        Args:
            limit: Maximum number of books to publish in one run

        Returns:
            List of book records to publish
        """
        try:
            with self.db_manager.get_connection() as conn:
                cursor = conn.execute("""
                    SELECT * FROM books
                    WHERE generation_status = 'completed'
                    AND (telegram_published = 0 OR telegram_published IS NULL)
                    AND (telegram_auto_publish = 1 OR telegram_auto_publish IS NULL)
                    ORDER BY created_date ASC
                    LIMIT ?
                """, (limit,))
                return [dict(row) for row in cursor.fetchall()]
        except Exception as e:
            self.errors.append(f"Database error: {e}")
            return []

    async def publish_book(self, book_data: dict) -> bool:
        """
        Publish a single book to Telegram.

        Args:
            book_data: Book information from database

        Returns:
            True if published successfully
        """
        try:
            async with TelegramBotManager(self.bot_token) as bot:
                # Format the message
                formatter = TelegramMessageFormatter()
                message = formatter.format_book_announcement(book_data)

                # Send cover image if available
                cover_data = self.get_book_cover(book_data)
                if cover_data:
                    success, result = await bot.send_photo(
                        self.channel_id,
                        cover_data,
                        caption=message
                    )
                else:
                    # Send text message if no cover
                    success, result = await bot.send_message(
                        self.channel_id,
                        message
                    )

                if success:
                    # Update database
                    self.mark_as_published(book_data['book_id'], result)
                    print(f"✅ Published: {book_data['title']}")
                    return True
                else:
                    error_msg = result.get('error', 'Unknown error')
                    self.errors.append(f"Failed to publish {book_data['title']}: {error_msg}")
                    return False

        except Exception as e:
            self.errors.append(f"Error publishing {book_data['title']}: {e}")
            return False

    def get_book_cover(self, book_data: dict) -> bytes:
        """
        Get book cover image data.

        Args:
            book_data: Book information

        Returns:
            Cover image bytes or None
        """
        try:
            # Try to get from database first
            cover_base64 = book_data.get('cover_base64')
            if cover_base64:
                import base64
                return base64.b64decode(cover_base64)

            # Try to get from file system
            book_id = book_data.get('book_id', '')
            cover_paths = [
                f"covers/{book_data.get('title', '')}/Cover.jpg",
                f"output/{book_id}/cover.jpg",
                f"output/{book_data.get('title', '')}/cover.jpg"
            ]

            for cover_path in cover_paths:
                if os.path.exists(cover_path):
                    with open(cover_path, 'rb') as f:
                        return f.read()

            return None

        except Exception as e:
            print(f"Warning: Could not load cover for {book_data['title']}: {e}")
            return None

    def mark_as_published(self, book_id: str, telegram_result: dict) -> None:
        """
        Mark book as published in database.

        Args:
            book_id: Book ID
            telegram_result: Result from Telegram API
        """
        try:
            message_id = telegram_result.get('message_id')
            publish_date = datetime.now().isoformat()

            with self.db_manager.get_connection() as conn:
                conn.execute("""
                    UPDATE books
                    SET telegram_published = 1,
                        telegram_message_id = ?,
                        telegram_publish_date = ?,
                        telegram_channel_id = ?,
                        telegram_post_type = 'book',
                        telegram_publication_status = 'published'
                    WHERE book_id = ?
                """, (str(message_id), publish_date, self.channel_id, book_id))
                conn.commit()

        except Exception as e:
            self.errors.append(f"Database update error for {book_id}: {e}")

    async def run_publishing_cycle(self, max_books: int = 3) -> dict:
        """
        Run a complete publishing cycle with intelligent queue management.

        Args:
            max_books: Maximum books to publish in this cycle

        Returns:
            Publishing results summary
        """
        print("🚀 Starting Telegram publishing cycle...")

        if not self.is_configured():
            error = "Telegram not configured. Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHANNEL_ID environment variables."
            print(f"❌ {error}")
            return {"success": False, "error": error}

        # Get all available books
        all_books = self.get_books_to_publish(50)  # Get more books for intelligent selection

        if not all_books:
            print("ℹ️ No books to publish")
            return {"success": True, "published": 0, "message": "No books to publish"}

        print(f"📚 Found {len(all_books)} books available for publishing")

        # Use content planner for intelligent selection
        try:
            from src.utils.telegram_content_planner import get_content_planner
            planner = get_content_planner()

            # Prioritize books based on strategy
            prioritized_books = planner.prioritize_publication_queue(all_books, max_books)
            print(f"📋 Selected {len(prioritized_books)} books based on content strategy")

            # Handle overflow
            overflow_books = all_books[len(prioritized_books):]
            if overflow_books:
                overflow_info = planner.handle_publication_overflow(overflow_books)
                print(f"📦 {overflow_info['message']}")

        except ImportError:
            # Fallback to simple selection if planner not available
            prioritized_books = all_books[:max_books]
            print(f"📋 Using simple selection: {len(prioritized_books)} books")

        # Publish selected books
        for i, book in enumerate(prioritized_books, 1):
            print(f"📖 Publishing book {i}/{len(prioritized_books)}: {book.get('title', 'Untitled')}")
            success = await self.publish_book(book)
            if success:
                self.published_count += 1

            # Add delay between posts to avoid rate limiting
            await asyncio.sleep(3)

        # Generate comprehensive summary
        result = {
            "success": True,
            "published": self.published_count,
            "total_found": len(all_books),
            "queued": len(all_books) - len(prioritized_books),
            "errors": self.errors,
            "strategy_used": "intelligent" if 'planner' in locals() else "simple"
        }

        print(f"✅ Publishing cycle complete:")
        print(f"   📤 Published: {self.published_count}/{len(prioritized_books)}")
        print(f"   📦 Queued for next cycle: {result['queued']}")

        if self.errors:
            print("⚠️ Errors encountered:")
            for error in self.errors:
                print(f"  - {error}")

        return result

def create_github_action_workflow():
    """Create GitHub Actions workflow file for automated publishing."""
    workflow_content = """name: Telegram Book Publisher

on:
  schedule:
    # Run Monday, Wednesday, Friday at 10 AM UTC
    - cron: '0 10 * * 1,3,5'
  workflow_dispatch:  # Allow manual triggering

jobs:
  publish:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run Telegram Publisher
      env:
        TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
        TELEGRAM_CHANNEL_ID: ${{ secrets.TELEGRAM_CHANNEL_ID }}
      run: python scripts/telegram_auto_publisher.py

    - name: Commit database changes
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action"
        git add data/novelforge_ai.db
        git diff --staged --quiet || git commit -m "Update Telegram publication status"
        git push
"""

    # Create .github/workflows directory
    workflow_dir = Path(".github/workflows")
    workflow_dir.mkdir(parents=True, exist_ok=True)

    # Write workflow file
    workflow_file = workflow_dir / "telegram-publisher.yml"
    with open(workflow_file, 'w') as f:
        f.write(workflow_content)

    print(f"✅ Created GitHub Actions workflow: {workflow_file}")

async def main():
    """Main function for running the auto publisher."""
    publisher = AutoTelegramPublisher()

    # Check if this is a setup run
    if len(sys.argv) > 1 and sys.argv[1] == "--setup":
        print("🔧 Setting up GitHub Actions workflow...")
        create_github_action_workflow()
        print("\n📋 Next steps:")
        print("1. Add TELEGRAM_BOT_TOKEN to GitHub repository secrets")
        print("2. Add TELEGRAM_CHANNEL_ID to GitHub repository secrets")
        print("3. Commit and push the workflow file")
        print("4. GitHub Actions will automatically publish books 3x per week!")
        return

    # Run publishing cycle
    result = await publisher.run_publishing_cycle()

    # Output results for GitHub Actions
    if result["success"]:
        print(f"::notice::Published {result['published']} books to Telegram")
    else:
        print(f"::error::{result.get('error', 'Publishing failed')}")

if __name__ == "__main__":
    asyncio.run(main())
