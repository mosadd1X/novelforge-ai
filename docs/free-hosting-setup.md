---
layout: default
title: Free Hosting Setup
nav_order: 9
description: 'Complete guide to hosting NovelForge AI Telegram bot for free'
permalink: /free-hosting-setup
---

# Free Hosting Setup for Students

{: .no_toc }

Complete guide to running your Telegram marketing bot with **zero budget** using free hosting platforms.
{: .fs-6 .fw-300 }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
   {:toc}

---

## Overview

As a student with zero budget, you can still run a professional Telegram marketing system! This guide shows you how to use **completely free** hosting solutions that are perfect for automated book publishing.

## 🆓 Free Hosting Options

### Option 1: GitHub Actions (Recommended)

**Why it's perfect for students:**
- ✅ Completely free (2,000 minutes/month)
- ✅ No credit card required
- ✅ Runs automatically on schedule
- ✅ Perfect for 2-3 posts per week
- ✅ Built-in version control

**Setup Steps:**

#### 1. Prepare Your Repository
```bash
# Make sure your NovelForge AI is in a GitHub repository
git add .
git commit -m "Add Telegram publishing system"
git push origin main
```

#### 2. Create GitHub Actions Workflow
Run this command in your NovelForge AI directory:
```bash
python scripts/telegram_auto_publisher.py --setup
```

This creates `.github/workflows/telegram-publisher.yml` that will:
- Run Monday, Wednesday, Friday at 10 AM
- Check for new books
- Publish up to 3 books per run
- Update your database automatically

#### 3. Add Secrets to GitHub
1. Go to your GitHub repository
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Add these secrets:
   - `TELEGRAM_BOT_TOKEN`: Your bot token from @BotFather
   - `TELEGRAM_CHANNEL_ID`: Your channel ID (e.g., @your_channel)

#### 4. Enable Actions
1. Go to **Actions** tab in your repository
2. Enable GitHub Actions if prompted
3. The workflow will run automatically on schedule!

### Option 2: Railway.app

**Free tier includes:**
- 500 hours/month (enough for 24/7 light usage)
- 1GB RAM, 1GB storage
- Custom domains

**Setup:**
1. Sign up at [railway.app](https://railway.app) with GitHub
2. Connect your NovelForge AI repository
3. Add environment variables:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHANNEL_ID`
4. Deploy automatically!

### Option 3: Render.com

**Free tier includes:**
- 750 hours/month
- Automatic deploys from GitHub
- Custom domains

**Setup:**
1. Sign up at [render.com](https://render.com)
2. Create new **Web Service** from GitHub
3. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python scripts/telegram_auto_publisher.py`
4. Add environment variables in dashboard

## 🤖 Telegram Bot Setup

### 1. Create Your Bot

1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot`
3. Choose a name: "YourName Book Publisher"
4. Choose a username: "yourname_books_bot"
5. Copy the token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 2. Create Your Channel

1. Create a new Telegram channel
2. Make it public with a username (e.g., @yourname_books)
3. Add your bot as an administrator
4. Give it permission to post messages

### 3. Get Channel ID

**Method 1: Use Username**
- If your channel is `@yourname_books`, use `@yourname_books` as channel ID

**Method 2: Get Numeric ID**
1. Add your bot to the channel as admin
2. Send a message to your channel
3. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Look for your channel ID (starts with `-100`)

## 📅 Publishing Schedule Options

### Conservative Schedule (Recommended for Free Hosting)
```yaml
# Monday, Wednesday, Friday at 10 AM
- cron: '0 10 * * 1,3,5'
```

### Daily Schedule
```yaml
# Every day at 2 PM
- cron: '0 14 * * *'
```

### Custom Schedule
```yaml
# Tuesday and Thursday at 6 PM
- cron: '0 18 * * 2,4'
```

## 💾 Database Considerations

### GitHub Actions Approach
- Database updates are committed back to repository
- Perfect for small-scale operations
- No additional storage costs

### Cloud Hosting Approach
- Use SQLite file in the container
- For Railway/Render, database persists between deployments
- Consider upgrading to PostgreSQL for heavy usage

## 🔧 Configuration for Free Hosting

### Environment Variables Setup

**For GitHub Actions:**
Add to repository secrets:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=@your_channel_name
```

**For Railway/Render:**
Add in platform dashboard:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHANNEL_ID=@your_channel_name
POSTING_SCHEDULE=conservative
MAX_BOOKS_PER_RUN=3
```

### Resource Optimization

**Memory Usage:**
```python
# In your publishing script
import gc

async def publish_book(self, book_data):
    # ... publishing logic ...
    gc.collect()  # Free memory after each book
```

**Database Optimization:**
```python
# Use connection pooling
with self.db_manager.get_connection() as conn:
    # Do all database operations
    pass  # Connection automatically closed
```

## 📊 Monitoring Your Free Setup

### GitHub Actions Monitoring
1. Go to **Actions** tab in your repository
2. Check workflow runs for success/failure
3. View logs for debugging

### Railway/Render Monitoring
1. Check platform dashboard for deployment status
2. View application logs
3. Monitor resource usage

## 🚨 Troubleshooting

### Common Issues

**GitHub Actions Not Running:**
- Check if Actions are enabled in repository settings
- Verify cron syntax in workflow file
- Check repository secrets are set correctly

**Bot Not Posting:**
- Verify bot token is correct
- Check bot is admin in channel
- Ensure channel ID format is correct

**Database Not Updating:**
- For GitHub Actions: Check if workflow has write permissions
- For cloud hosting: Verify database file permissions

### Error Messages

| Error | Solution |
|-------|----------|
| "Bot token invalid" | Re-create bot with @BotFather |
| "Chat not found" | Check channel ID format |
| "Not enough rights" | Make bot admin in channel |
| "File too large" | Enable file hosting for large EPUBs |

## 💡 Pro Tips for Students

### 1. Start Small
- Begin with 2-3 posts per week
- Focus on quality over quantity
- Build audience gradually

### 2. Optimize Content
- Use engaging book covers
- Write compelling descriptions
- Use relevant hashtags

### 3. Monitor Performance
- Track which genres perform best
- Adjust posting times based on engagement
- Experiment with different message formats

### 4. Scale Gradually
- Start with GitHub Actions
- Move to cloud hosting as audience grows
- Consider paid hosting only when generating revenue

## 🎯 Success Metrics for Free Hosting

**Week 1-4: Foundation**
- 10-15 books published
- Channel setup complete
- Automated posting working

**Month 2-3: Growth**
- 50+ subscribers
- Regular engagement
- Optimized posting schedule

**Month 4+: Scaling**
- 100+ subscribers
- Consider monetization
- Upgrade hosting if needed

## 🔮 Future Upgrade Path

**When to Consider Paid Hosting:**
1. 1000+ channel subscribers
2. Generating revenue from books
3. Need for real-time features
4. Multiple channels to manage

**Recommended Upgrade Path:**
1. Start: GitHub Actions (Free)
2. Growth: Railway Pro ($5/month)
3. Scale: VPS hosting ($10-20/month)

---

**Remember:** Many successful indie authors started with zero budget. Focus on creating great content, and the audience (and revenue) will follow! 🚀

*Your NovelForge AI system is designed to grow with you from student project to professional publishing platform.*
