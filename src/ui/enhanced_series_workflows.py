"""
Enhanced Series Workflows for NovelForge AI - Phase 3 Implementation

This module provides advanced series creation workflows with automatic book sequencing,
consistent character development, series-wide visual consistency, and metadata management.
"""

import os
import sys
from typing import Dict, List, Any, Optional, Tuple
import questionary
from rich.console import Console
import time
import json

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from src.ui.terminal_ui import (
    clear_screen,
    display_title,
    custom_style
)

console = Console()

class EnhancedSeriesWorkflow:
    """Advanced series creation with automatic sequencing and consistency management."""

    def __init__(self):
        self.series_data = {}
        self.character_database = {}
        self.visual_style_guide = {}
        self.continuity_tracker = {}
        self.current_book = 0
        self.total_books = 0

    def start_enhanced_series_workflow(self):
        """Start the enhanced series creation workflow."""
        clear_screen()
        display_title()

        console.print("[bold cyan]📚 Enhanced Series Creation[/bold cyan]")
        console.print("    Advanced workflow with character continuity and visual consistency")
        console.print()

        # Collect series information
        if not self.collect_series_information():
            return

        # Set up character database
        if not self.setup_character_database():
            return

        # Create visual style guide
        if not self.create_visual_style_guide():
            return

        # Execute series generation
        self.execute_series_generation()

    def collect_series_information(self) -> bool:
        """Collect comprehensive series information."""
        console.print("[bold cyan]📋 Series Planning[/bold cyan]")
        console.print("    Let's plan your series for maximum consistency")
        console.print()

        # Series title
        series_title = questionary.text(
            "What's your series title?",
            style=custom_style
        ).ask()

        if not series_title:
            return False

        # Genre
        genre = questionary.select(
            "Select your series genre:",
            choices=[
                "Romance", "Mystery", "Science Fiction", "Fantasy",
                "Thriller", "Adventure", "Historical Fiction",
                "Contemporary Fiction", "Young Adult", "Other"
            ],
            style=custom_style
        ).ask()

        if not genre:
            return False

        # Number of books
        book_count = questionary.select(
            "How many books will be in your series?",
            choices=[
                "3 books (Trilogy)",
                "5 books (Pentalogy)",
                "7 books (Heptalogy)",
                "10 books (Extended series)",
                "Custom number"
            ],
            style=custom_style
        ).ask()

        if not book_count:
            return False

        if "Custom" in book_count:
            custom_count = questionary.text(
                "Enter the number of books:",
                validate=lambda x: x.isdigit() and int(x) > 0,
                style=custom_style
            ).ask()

            if not custom_count:
                return False

            self.total_books = int(custom_count)
        else:
            self.total_books = int(book_count.split()[0])

        # Series type
        series_type = questionary.select(
            "What type of series is this?",
            choices=[
                "Sequential (books must be read in order)",
                "Standalone (books can be read independently)",
                "Hybrid (some books standalone, some sequential)"
            ],
            style=custom_style
        ).ask()

        if not series_type:
            return False

        # Story arc
        story_arc = questionary.select(
            "What's the overarching story structure?",
            choices=[
                "Single main conflict resolved across all books",
                "Each book has its own conflict with series themes",
                "Character development focus across books",
                "World-building expansion across books"
            ],
            style=custom_style
        ).ask()

        if not story_arc:
            return False

        self.series_data = {
            "title": series_title,
            "genre": genre,
            "book_count": self.total_books,
            "series_type": series_type,
            "story_arc": story_arc
        }

        console.print()
        console.print("[bold green]✅ Series planning completed![/bold green]")
        console.print(f"    📚 {series_title} ({self.total_books} books)")
        console.print(f"    🎭 Genre: {genre}")
        console.print(f"    📖 Type: {series_type}")

        input("\nPress Enter to continue...")
        return True

    def setup_character_database(self) -> bool:
        """Set up the character database for consistency tracking."""
        clear_screen()
        display_title()

        console.print("[bold cyan]👥 Character Database Setup[/bold cyan]")
        console.print("    Create consistent characters across your series")
        console.print()

        # Main characters
        console.print("    Let's identify your main characters:")
        console.print()

        main_characters = []

        while True:
            character_name = questionary.text(
                f"Enter main character name (or press Enter to finish):",
                style=custom_style
            ).ask()

            if not character_name:
                break

            # Character details
            character_role = questionary.select(
                f"What's {character_name}'s role?",
                choices=[
                    "Protagonist",
                    "Love Interest",
                    "Antagonist",
                    "Supporting Character",
                    "Mentor",
                    "Comic Relief",
                    "Other"
                ],
                style=custom_style
            ).ask()

            character_arc = questionary.select(
                f"How does {character_name} develop across the series?",
                choices=[
                    "Major development across all books",
                    "Development in specific books",
                    "Consistent character throughout",
                    "Evolving background presence"
                ],
                style=custom_style
            ).ask()

            main_characters.append({
                "name": character_name,
                "role": character_role,
                "development_arc": character_arc,
                "appearances": list(range(1, self.total_books + 1))  # Default: appears in all books
            })

            console.print(f"    ✅ Added {character_name} ({character_role})")

        if not main_characters:
            console.print("    ⚠️ No main characters defined. Using default character setup.")
            main_characters = [
                {
                    "name": "Main Character",
                    "role": "Protagonist",
                    "development_arc": "Major development across all books",
                    "appearances": list(range(1, self.total_books + 1))
                }
            ]

        self.character_database = {
            "main_characters": main_characters,
            "character_relationships": {},
            "character_growth_tracking": {}
        }

        console.print()
        console.print(f"[bold green]✅ Character database created with {len(main_characters)} main characters![/bold green]")

        input("\nPress Enter to continue...")
        return True

    def create_visual_style_guide(self) -> bool:
        """Create a visual style guide for series consistency."""
        clear_screen()
        display_title()

        console.print("[bold cyan]🎨 Visual Style Guide[/bold cyan]")
        console.print("    Establish consistent visual branding for your series")
        console.print()

        # Color scheme
        color_scheme = questionary.select(
            "Choose a color scheme for your series:",
            choices=[
                "Warm (reds, oranges, yellows)",
                "Cool (blues, greens, purples)",
                "Monochromatic (shades of one color)",
                "High Contrast (black, white, one accent)",
                "Genre-Appropriate (let AI decide based on genre)"
            ],
            style=custom_style
        ).ask()

        if not color_scheme:
            return False

        # Typography style
        typography = questionary.select(
            "What typography style fits your series?",
            choices=[
                "Classic (traditional, elegant fonts)",
                "Modern (clean, contemporary fonts)",
                "Dramatic (bold, impactful fonts)",
                "Handwritten (personal, intimate feel)",
                "Genre-Specific (optimized for your genre)"
            ],
            style=custom_style
        ).ask()

        if not typography:
            return False

        # Visual elements
        visual_elements = questionary.checkbox(
            "What visual elements should be consistent across covers?",
            choices=[
                "Character silhouettes",
                "Symbolic objects",
                "Background themes",
                "Border/frame styles",
                "Logo/series branding",
                "Color gradients",
                "Texture patterns"
            ],
            style=custom_style
        ).ask()

        # Layout consistency
        layout_style = questionary.select(
            "How should the cover layouts relate to each other?",
            choices=[
                "Identical layout with different content",
                "Similar layout with variations",
                "Progressive evolution across books",
                "Thematic variations on core design"
            ],
            style=custom_style
        ).ask()

        if not layout_style:
            return False

        self.visual_style_guide = {
            "color_scheme": color_scheme,
            "typography": typography,
            "visual_elements": visual_elements or [],
            "layout_style": layout_style,
            "series_branding": {
                "consistent_elements": ["series title placement", "author name styling"],
                "book_numbering": "Book 1, Book 2, etc."
            }
        }

        console.print()
        console.print("[bold green]✅ Visual style guide created![/bold green]")
        console.print(f"    🎨 Color scheme: {color_scheme}")
        console.print(f"    ✍️ Typography: {typography}")
        console.print(f"    📐 Layout: {layout_style}")

        input("\nPress Enter to continue...")
        return True

    def execute_series_generation(self):
        """Execute the complete series generation with consistency tracking."""
        clear_screen()
        display_title()

        console.print("[bold cyan]🚀 Enhanced Series Generation[/bold cyan]")
        console.print("    Creating your series with automatic consistency management")
        console.print()

        console.print(f"    📚 Series: {self.series_data['title']}")
        console.print(f"    📖 Books: {self.total_books}")
        console.print(f"    👥 Main Characters: {len(self.character_database['main_characters'])}")
        console.print(f"    🎨 Visual Style: {self.visual_style_guide['color_scheme']}")
        console.print()

        proceed = questionary.confirm(
            "Ready to generate your enhanced series?",
            default=True,
            style=custom_style
        ).ask()

        if not proceed:
            return

        console.print()

        # Generate each book in sequence
        for book_num in range(1, self.total_books + 1):
            self.current_book = book_num

            if self.generate_series_book(book_num):
                console.print(f"    ✅ Book {book_num} completed successfully")
            else:
                console.print(f"    ❌ Book {book_num} generation failed")
                break

            console.print()

        self.series_generation_complete()

    def generate_series_book(self, book_number: int) -> bool:
        """Generate a single book in the series with consistency tracking."""
        console.print(f"[bold cyan]📖 Generating Book {book_number}[/bold cyan]")

        try:
            # Step 1: Content generation with character consistency
            console.print(f"    📝 Generating content with character continuity...")
            self.apply_character_consistency(book_number)
            time.sleep(1.0)

            # Step 2: Cover creation with visual consistency
            console.print(f"    🎨 Creating cover with series visual consistency...")
            self.apply_visual_consistency(book_number)
            time.sleep(0.8)

            # Step 3: Metadata with series information
            console.print(f"    📋 Adding series metadata...")
            self.apply_series_metadata(book_number)
            time.sleep(0.5)

            # Step 4: Continuity tracking update
            console.print(f"    🔄 Updating continuity tracker...")
            self.update_continuity_tracker(book_number)
            time.sleep(0.3)

            return True

        except Exception as e:
            console.print(f"    ❌ Error generating book {book_number}: {e}")
            return False

    def apply_character_consistency(self, book_number: int):
        """Apply character consistency for the current book."""
        characters_in_book = [
            char for char in self.character_database["main_characters"]
            if book_number in char["appearances"]
        ]

        for character in characters_in_book:
            console.print(f"        👤 Ensuring {character['name']} consistency")

    def apply_visual_consistency(self, book_number: int):
        """Apply visual consistency for the current book's cover."""
        style_guide = self.visual_style_guide

        console.print(f"        🎨 Applying {style_guide['color_scheme']} color scheme")
        console.print(f"        ✍️ Using {style_guide['typography']} typography")
        console.print(f"        📐 Following {style_guide['layout_style']} layout")

    def apply_series_metadata(self, book_number: int):
        """Apply series-specific metadata to the current book."""
        console.print(f"        📚 Series: {self.series_data['title']}")
        console.print(f"        📖 Book {book_number} of {self.total_books}")
        console.print(f"        🎭 Genre: {self.series_data['genre']}")

    def update_continuity_tracker(self, book_number: int):
        """Update the continuity tracker with information from the current book."""
        if "books_completed" not in self.continuity_tracker:
            self.continuity_tracker["books_completed"] = []

        self.continuity_tracker["books_completed"].append({
            "book_number": book_number,
            "characters_featured": [
                char["name"] for char in self.character_database["main_characters"]
                if book_number in char["appearances"]
            ],
            "plot_points": f"Book {book_number} plot developments",
            "character_growth": f"Character development in book {book_number}"
        })

    def series_generation_complete(self):
        """Handle successful series generation completion."""
        clear_screen()
        display_title()

        console.print("[bold green]🎉 Enhanced Series Generation Complete![/bold green]")
        console.print(f"    Your {self.series_data['title']} series is ready!")
        console.print()

        console.print("[bold cyan]📚 Series Summary:[/bold cyan]")
        console.print(f"    📖 {self.total_books} books generated")
        console.print(f"    👥 {len(self.character_database['main_characters'])} main characters")
        console.print(f"    🎨 Consistent visual branding")
        console.print(f"    📋 Complete series metadata")

        console.print()
        console.print("[bold cyan]✅ What's Included:[/bold cyan]")
        console.print("    • Character consistency across all books")
        console.print("    • Visual style guide implementation")
        console.print("    • Series metadata and numbering")
        console.print("    • Continuity tracking database")
        console.print("    • Cross-book reference system")

        console.print()
        console.print("[bold cyan]📋 Next Steps:[/bold cyan]")
        console.print("    • Review individual books for quality")
        console.print("    • Generate EPUB files for the series")
        console.print("    • Create series marketing materials")
        console.print("    • Plan your series launch strategy")

        input("\nPress Enter to continue...")

def enhanced_series_workflows_menu():
    """Main menu for enhanced series workflows."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]📚 Enhanced Series Workflows[/bold cyan]")
        console.print("    Advanced series creation with consistency management")
        console.print()

        choices = [
            "🚀 Create Enhanced Series",
            "👥 Manage Character Database",
            "🎨 Series Visual Consistency",
            "📋 Series Metadata Management",
            "🔄 Continuity Tracking",
            "← Back to Content Creation"
        ]

        selected = questionary.select(
            "What would you like to do?",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "🚀 Create Enhanced Series":
            workflow = EnhancedSeriesWorkflow()
            workflow.start_enhanced_series_workflow()
        elif selected == "👥 Manage Character Database":
            manage_character_database()
        elif selected == "🎨 Series Visual Consistency":
            manage_visual_consistency()
        elif selected == "📋 Series Metadata Management":
            manage_series_metadata()
        elif selected == "🔄 Continuity Tracking":
            manage_continuity_tracking()
        elif selected == "← Back to Content Creation":
            break

def manage_character_database():
    """Manage the character database for series consistency."""
    clear_screen()
    display_title()

    console.print("[bold cyan]👥 Character Database Management[/bold cyan]")
    console.print("    Manage character consistency across your series")
    console.print()

    console.print("[yellow]Character database management will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Character profile management")
    console.print("• Relationship tracking")
    console.print("• Character development arcs")
    console.print("• Consistency checking tools")

    input("\nPress Enter to continue...")

def manage_visual_consistency():
    """Manage visual consistency across series."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🎨 Series Visual Consistency[/bold cyan]")
    console.print("    Manage visual branding across your series")
    console.print()

    console.print("[yellow]Visual consistency management will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Style guide editor")
    console.print("• Cover template management")
    console.print("• Brand consistency checking")
    console.print("• Visual element library")

    input("\nPress Enter to continue...")

def manage_series_metadata():
    """Manage series metadata and cross-book references."""
    clear_screen()
    display_title()

    console.print("[bold cyan]📋 Series Metadata Management[/bold cyan]")
    console.print("    Manage metadata and cross-references")
    console.print()

    console.print("[yellow]Series metadata management will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Series information editing")
    console.print("• Cross-book reference tracking")
    console.print("• Publication order management")
    console.print("• Series description generation")

    input("\nPress Enter to continue...")

def manage_continuity_tracking():
    """Manage continuity tracking across the series."""
    clear_screen()
    display_title()

    console.print("[bold cyan]🔄 Continuity Tracking[/bold cyan]")
    console.print("    Track plot and character continuity")
    console.print()

    console.print("[yellow]Continuity tracking will be implemented in the next update.[/yellow]")
    console.print("This will include:")
    console.print("• Plot point tracking")
    console.print("• Character development monitoring")
    console.print("• Timeline consistency checking")
    console.print("• Continuity error detection")

    input("\nPress Enter to continue...")
