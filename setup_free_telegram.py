#!/usr/bin/env python3
"""
Free Telegram Setup Script for NovelForge AI

This script helps students set up Telegram publishing with zero budget
using GitHub Actions or other free hosting platforms.

Run: python setup_free_telegram.py
"""

import os
import json
from pathlib import Path
import questionary
from rich.console import Console
from rich.panel import Panel

console = Console()

def display_welcome():
    """Display welcome message for students."""
    console.print(Panel.fit(
        "[bold cyan]🎓 NovelForge AI - Free Telegram Setup for Students[/bold cyan]\n\n"
        "[green]Perfect for zero-budget book marketing![/green]\n"
        "• No hosting costs\n"
        "• No credit card required\n"
        "• Professional automation\n"
        "• Scales with your success",
        title="Welcome",
        border_style="cyan"
    ))

def check_prerequisites():
    """Check if all prerequisites are met."""
    console.print("\n[bold cyan]📋 Checking Prerequisites...[/bold cyan]")
    
    issues = []
    
    # Check if we're in a git repository
    if not Path(".git").exists():
        issues.append("Not in a Git repository. Run 'git init' first.")
    
    # Check if requirements.txt exists
    if not Path("requirements.txt").exists():
        issues.append("requirements.txt not found")
    
    # Check if NovelForge AI structure exists
    if not Path("src").exists():
        issues.append("NovelForge AI source directory not found")
    
    if issues:
        console.print("[red]❌ Issues found:[/red]")
        for issue in issues:
            console.print(f"  • {issue}")
        return False
    else:
        console.print("[green]✅ All prerequisites met![/green]")
        return True

def get_hosting_choice():
    """Get user's preferred hosting platform."""
    console.print("\n[bold cyan]🏠 Choose Your Free Hosting Platform[/bold cyan]")
    
    choices = [
        "🤖 GitHub Actions (Recommended for beginners)",
        "🚂 Railway.app (Good for 24/7 operation)",
        "🎨 Render.com (Easy deployment)",
        "ℹ️  Show me the differences"
    ]
    
    while True:
        selected = questionary.select(
            "Which free hosting platform would you like to use?",
            choices=choices
        ).ask()
        
        if selected == "ℹ️  Show me the differences":
            show_hosting_comparison()
            continue
        elif "GitHub Actions" in selected:
            return "github"
        elif "Railway" in selected:
            return "railway"
        elif "Render" in selected:
            return "render"

def show_hosting_comparison():
    """Show comparison of hosting platforms."""
    console.print("\n[bold cyan]🔍 Hosting Platform Comparison[/bold cyan]")
    
    comparison = """
[bold]GitHub Actions[/bold] (Best for students)
✅ Completely free (2,000 minutes/month)
✅ No credit card required
✅ Perfect for scheduled posting (3x/week)
✅ Automatic database updates
❌ Not suitable for real-time features

[bold]Railway.app[/bold] (Good for growth)
✅ 500 hours/month free
✅ 24/7 operation possible
✅ Easy scaling
❌ Requires credit card for verification
❌ Limited free tier

[bold]Render.com[/bold] (Balanced option)
✅ 750 hours/month free
✅ Good performance
✅ Easy deployment
❌ Requires credit card
❌ Sleeps after 15 minutes of inactivity
"""
    
    console.print(comparison)
    input("\nPress Enter to continue...")

def setup_github_actions():
    """Set up GitHub Actions workflow."""
    console.print("\n[bold cyan]🤖 Setting Up GitHub Actions[/bold cyan]")
    
    # Create workflow directory
    workflow_dir = Path(".github/workflows")
    workflow_dir.mkdir(parents=True, exist_ok=True)
    
    # Create workflow file
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
      with:
        token: ${{ secrets.GITHUB_TOKEN }}
    
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
        git diff --staged --quiet || git commit -m "📱 Update Telegram publication status [automated]"
        git push
"""
    
    workflow_file = workflow_dir / "telegram-publisher.yml"
    with open(workflow_file, 'w') as f:
        f.write(workflow_content)
    
    console.print(f"✅ Created workflow file: {workflow_file}")
    
    # Show next steps
    console.print("\n[bold green]📋 Next Steps for GitHub Actions:[/bold green]")
    console.print("1. Push this workflow to your GitHub repository")
    console.print("2. Go to your repository on GitHub.com")
    console.print("3. Click Settings → Secrets and variables → Actions")
    console.print("4. Add these secrets:")
    console.print("   • TELEGRAM_BOT_TOKEN (from @BotFather)")
    console.print("   • TELEGRAM_CHANNEL_ID (your channel @username)")
    console.print("5. Go to Actions tab and enable workflows")
    console.print("\n[cyan]Your bot will automatically publish books 3x per week![/cyan]")

def setup_railway():
    """Set up Railway.app deployment."""
    console.print("\n[bold cyan]🚂 Setting Up Railway.app[/bold cyan]")
    
    # Create railway.json
    railway_config = {
        "build": {
            "builder": "NIXPACKS"
        },
        "deploy": {
            "startCommand": "python scripts/telegram_auto_publisher.py",
            "healthcheckPath": "/health",
            "healthcheckTimeout": 100,
            "restartPolicyType": "ON_FAILURE"
        }
    }
    
    with open("railway.json", 'w') as f:
        json.dump(railway_config, f, indent=2)
    
    console.print("✅ Created railway.json configuration")
    
    # Show next steps
    console.print("\n[bold green]📋 Next Steps for Railway:[/bold green]")
    console.print("1. Sign up at railway.app with your GitHub account")
    console.print("2. Click 'New Project' → 'Deploy from GitHub repo'")
    console.print("3. Select your NovelForge AI repository")
    console.print("4. Add environment variables:")
    console.print("   • TELEGRAM_BOT_TOKEN")
    console.print("   • TELEGRAM_CHANNEL_ID")
    console.print("5. Deploy!")

def setup_render():
    """Set up Render.com deployment."""
    console.print("\n[bold cyan]🎨 Setting Up Render.com[/bold cyan]")
    
    # Create render.yaml
    render_config = {
        "services": [
            {
                "type": "web",
                "name": "novelforge-telegram",
                "env": "python",
                "buildCommand": "pip install -r requirements.txt",
                "startCommand": "python scripts/telegram_auto_publisher.py",
                "plan": "free"
            }
        ]
    }
    
    with open("render.yaml", 'w') as f:
        import yaml
        yaml.dump(render_config, f, default_flow_style=False)
    
    console.print("✅ Created render.yaml configuration")
    
    # Show next steps
    console.print("\n[bold green]📋 Next Steps for Render:[/bold green]")
    console.print("1. Sign up at render.com")
    console.print("2. Connect your GitHub account")
    console.print("3. Create new 'Web Service' from your repository")
    console.print("4. Add environment variables in dashboard:")
    console.print("   • TELEGRAM_BOT_TOKEN")
    console.print("   • TELEGRAM_CHANNEL_ID")
    console.print("5. Deploy!")

def create_telegram_guide():
    """Create a simple Telegram setup guide."""
    guide_content = """# 🤖 Telegram Bot Setup Guide

## Step 1: Create Your Bot
1. Open Telegram and message @BotFather
2. Send `/newbot`
3. Choose a name: "YourName Book Publisher"
4. Choose a username: "yourname_books_bot"
5. Copy the token (save it safely!)

## Step 2: Create Your Channel
1. Create a new Telegram channel
2. Make it public with username: @yourname_books
3. Add your bot as administrator
4. Give it permission to post messages

## Step 3: Test Your Setup
1. Send a test message to your channel
2. Verify your bot can post
3. Note your channel username (@yourname_books)

## Your Configuration:
- Bot Token: [SAVE FROM BOTFATHER]
- Channel ID: @yourname_books

## Need Help?
- Check docs/free-hosting-setup.md
- Test your bot with: python scripts/telegram_auto_publisher.py
"""
    
    with open("TELEGRAM_SETUP_GUIDE.md", 'w') as f:
        f.write(guide_content)
    
    console.print("✅ Created TELEGRAM_SETUP_GUIDE.md")

def main():
    """Main setup function."""
    display_welcome()
    
    if not check_prerequisites():
        console.print("\n[red]Please fix the issues above and run the setup again.[/red]")
        return
    
    # Get hosting choice
    hosting_platform = get_hosting_choice()
    
    # Set up based on choice
    if hosting_platform == "github":
        setup_github_actions()
    elif hosting_platform == "railway":
        setup_railway()
    elif hosting_platform == "render":
        setup_render()
    
    # Create Telegram guide
    create_telegram_guide()
    
    # Final message
    console.print(Panel.fit(
        "[bold green]🎉 Setup Complete![/bold green]\n\n"
        "[cyan]Your free Telegram publishing system is ready![/cyan]\n\n"
        "Next steps:\n"
        "1. Set up your Telegram bot (see TELEGRAM_SETUP_GUIDE.md)\n"
        "2. Configure your hosting platform\n"
        "3. Generate some books with NovelForge AI\n"
        "4. Watch them automatically publish to Telegram!\n\n"
        "[yellow]💡 Tip: Start with 2-3 books per week to build your audience[/yellow]",
        title="Success!",
        border_style="green"
    ))

if __name__ == "__main__":
    main()
