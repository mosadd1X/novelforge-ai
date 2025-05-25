---
layout: default
title: Telegram Integration
nav_order: 8
description: 'Complete guide to Telegram marketing and distribution for NovelForge AI'
permalink: /telegram-integration
---

# Telegram Integration for NovelForge AI

{: .no_toc }

Comprehensive marketing and distribution system for automatically publishing generated books to Telegram channels.
{: .fs-6 .fw-300 }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
   {:toc}

---

## Overview

The Telegram Integration module provides automated marketing and distribution capabilities for NovelForge AI, allowing you to:

- **Automatically publish** new books and series to Telegram channels
- **Manage multiple channels** with different publishing strategies
- **Handle file distribution** with smart hosting for large EPUB files
- **Track engagement** and analytics for your publications
- **Schedule posts** and manage publication queues
- **Build audience** with professional book announcements

## Architecture

### Integration Approach

The Telegram system is built as an **integrated module** within NovelForge AI, following established patterns:

- **Database Integration**: Extends the existing schema v2.1 with Telegram-specific fields
- **UI Integration**: Adds to the Publishing Tools menu with consistent terminal UI design
- **Workflow Integration**: Seamlessly connects with book generation, cover management, and EPUB systems

### Core Components

```
src/ui/telegram_publishing.py          # Main UI module
src/utils/telegram_bot_manager.py      # Bot API integration
src/utils/telegram_config_manager.py   # Configuration management
config/telegram_config.json           # Configuration storage
```

## Setup and Configuration

### 1. Install Dependencies

```bash
pip install aiohttp aiofiles
```

### 2. Create Telegram Bot

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Copy the bot token provided
4. Add your bot as an admin to your channel

### 3. Configure NovelForge AI

Access the Telegram configuration through:
```
Publishing Tools → Telegram Publishing → Configuration & Settings
```

#### Bot Token Configuration
- Enter your bot token from BotFather
- Token is securely stored and not saved in plain text

#### Channel Configuration
- Add your channel ID or username (e.g., `@your_channel`)
- Support for multiple channels with different purposes
- Test configuration to verify bot permissions

### 4. Publishing Settings

Configure automatic publishing behavior:

- **Auto-publish new books**: Automatically post when books are generated
- **Include covers**: Attach book covers to posts
- **Include EPUB files**: Attach EPUB files (with size limits)
- **File size limits**: Handle Telegram's 50MB limit with external hosting
- **Posting schedule**: Immediate or scheduled publishing

## Database Schema

### New Fields Added to Books Table

```sql
-- Telegram publishing tracking
telegram_published INTEGER DEFAULT 0,           -- Publication status
telegram_message_id TEXT,                       -- Message ID for tracking
telegram_publish_date TEXT,                     -- Publication timestamp
telegram_channel_id TEXT,                       -- Target channel
telegram_post_type TEXT,                        -- book, series_announcement, etc.
telegram_engagement_stats TEXT,                 -- JSON with analytics
telegram_file_hosting TEXT,                     -- File hosting details
telegram_scheduled_date TEXT,                   -- Scheduled publication
telegram_auto_publish INTEGER DEFAULT 1,        -- Auto-publish flag
telegram_publication_status TEXT DEFAULT 'pending'  -- pending, published, failed
```

## Features

### Automated Publishing

- **New Book Detection**: Automatically detects completed books
- **Smart Formatting**: Creates engaging posts with covers and descriptions
- **Series Management**: Handles series announcements and updates
- **Error Handling**: Robust error handling with retry mechanisms

### File Management

- **Size Optimization**: Handles Telegram's 50MB file limit
- **External Hosting**: Integration with file hosting services for large files
- **Download Links**: Generates secure download links for hosted files
- **Cleanup**: Automatic cleanup of old files

### Message Templates

Customizable message templates for different content types:

#### Book Announcement Template
```html
📚 <b>New Book Release!</b>

<b>📖 {title}</b>
<i>by {author}</i>

🎭 <b>Genre:</b> {genre}

📝 <b>Description:</b>
{description}

✨ <i>Generated with AI-powered creativity</i>

#NewRelease #{genre_tag} #AIGenerated
```

#### Series Announcement Template
```html
📚 <b>New Series Alert!</b>

<b>📖 {series_title}</b>
<i>{book_count} Books Available</i>

📚 <b>Books in this series:</b>
{book_list}

✨ <i>Complete series generated with AI</i>

#NewSeries #AIGenerated #BookSeries
```

### Analytics and Tracking

- **Engagement Metrics**: Track views, reactions, and downloads
- **Publication History**: Complete history of published content
- **Performance Reports**: Weekly/monthly performance summaries
- **Channel Analytics**: Multi-channel performance comparison

## Usage

### Publishing Workflow

1. **Generate Books**: Create books using NovelForge AI
2. **Auto-Detection**: System detects completed books
3. **Queue Management**: Books added to publication queue
4. **Automated Posting**: Books published according to schedule
5. **Analytics Tracking**: Engagement metrics collected

### Manual Publishing

For manual control over publications:

1. Access `Publishing Tools → Telegram Publishing`
2. View pending books in publication queue
3. Select books to publish immediately
4. Customize post content if needed
5. Publish to selected channels

### Batch Operations

- **Bulk Publishing**: Publish multiple books at once
- **Series Publishing**: Publish entire series with coordinated messaging
- **Scheduled Campaigns**: Plan publication campaigns in advance

## Best Practices

### Audience Building

1. **Consistent Posting**: Regular publication schedule
2. **Quality Content**: High-quality book covers and descriptions
3. **Engagement**: Respond to comments and feedback
4. **Cross-Promotion**: Promote across multiple channels
5. **SEO Optimization**: Use relevant hashtags and keywords

### Content Strategy

1. **Genre Focus**: Consider genre-specific channels
2. **Series Promotion**: Leverage series for audience retention
3. **Variety**: Mix individual books and series announcements
4. **Timing**: Post when your audience is most active

### Technical Considerations

1. **File Size Management**: Monitor EPUB file sizes
2. **Rate Limiting**: Respect Telegram's API limits
3. **Error Monitoring**: Monitor for failed publications
4. **Backup Channels**: Configure backup channels for redundancy

## Troubleshooting

### Common Issues

#### Bot Not Responding
- Verify bot token is correct
- Check bot is added as admin to channel
- Test bot connection in configuration

#### Files Not Uploading
- Check file size (50MB limit)
- Verify file hosting configuration
- Check network connectivity

#### Posts Not Appearing
- Verify channel permissions
- Check publication queue status
- Review error logs

### Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| "Bot token invalid" | Incorrect token | Re-enter token from BotFather |
| "Channel not found" | Wrong channel ID | Verify channel ID/username |
| "File too large" | EPUB > 50MB | Enable external hosting |
| "Permission denied" | Bot not admin | Add bot as channel admin |

## API Reference

### TelegramPublisher Class

Main class for Telegram publishing operations.

```python
from src.ui.telegram_publishing import TelegramPublisher

publisher = TelegramPublisher()
unpublished = publisher.get_unpublished_books()
stats = publisher.get_publishing_stats()
```

### TelegramBotManager Class

Low-level Telegram Bot API integration.

```python
from src.utils.telegram_bot_manager import TelegramBotManager

async with TelegramBotManager(bot_token) as bot:
    success, result = await bot.send_message(channel_id, message)
```

### Configuration Management

```python
from src.utils.telegram_config_manager import get_telegram_config_manager

config = get_telegram_config_manager()
config.set_bot_token("your_token")
config.set_channel_id("@your_channel")
config.save_configuration()
```

## Future Enhancements

### Planned Features

1. **Multi-Platform Support**: Discord, Twitter integration
2. **Advanced Analytics**: Detailed engagement tracking
3. **A/B Testing**: Test different message formats
4. **Audience Segmentation**: Target different audience groups
5. **Automated Responses**: Bot responses to user interactions

### Integration Opportunities

1. **Marketing Automation**: Integration with email marketing
2. **Social Media**: Cross-platform posting
3. **E-commerce**: Direct sales integration
4. **Reader Feedback**: Automated feedback collection

## Support

For issues with Telegram integration:

1. Check the [Troubleshooting Guide](./troubleshooting.html)
2. Review error logs in the application
3. Test configuration using built-in tools
4. Verify Telegram Bot API status

---

*The Telegram Integration module is designed to grow your audience and automate your book marketing while maintaining the professional quality standards of NovelForge AI.*
