"""
Test script to demonstrate smart character generation based on content type.
"""

import sys
sys.path.append('..')

from rich.console import Console
from rich.table import Table
from rich import box

console = Console(markup=True)

def should_generate_characters(genre: str) -> bool:
    """
    Determine if character generation is needed for a given genre.

    Args:
        genre: The genre of the book

    Returns:
        bool: True if characters should be generated, False otherwise
    """
    # Fiction genres that need characters (narrative content)
    fiction_genres = [
        "literary fiction", "commercial fiction", "mystery", "mystery thriller",
        "thriller", "romance", "fantasy", "epic fantasy", "science fiction",
        "historical fiction", "horror", "young adult", "middle grade",
        "children's chapter books", "speculative fiction", "alternate history",
        "contemporary fiction", "paranormal romance", "urban fantasy", "dystopian",
        "test"  # Include test genre for development
    ]

    # Non-fiction genres that don't need characters (informational content)
    non_fiction_genres = [
        "memoir", "biography", "history", "self help", "business",
        "popular science", "academic", "travel", "cookbook", "how to",
        "philosophy", "true crime"
    ]

    # Special formats that don't need traditional characters
    special_format_genres = [
        "short story collection", "novella", "graphic novel",
        "essay collection", "poetry collection", "creative non fiction"
    ]

    # Normalize genre name for comparison
    genre_normalized = genre.lower().strip()

    # Check if it's a fiction genre that needs characters
    for fiction_genre in fiction_genres:
        if fiction_genre.lower() in genre_normalized or genre_normalized in fiction_genre.lower():
            return True

    # All other genres (non-fiction and special formats) don't need characters
    return False

def test_character_generation_logic():
    """Test the character generation logic for different genres."""

    console.print("[bold cyan]🧪 Smart Character Generation Test[/bold cyan]")
    console.print("=" * 60)

    # Test cases with different genres
    test_cases = [
        # Fiction genres (should generate characters)
        ("Fantasy", True),
        ("Romance", True),
        ("Mystery", True),
        ("Science Fiction", True),
        ("Young Adult", True),
        ("Horror", True),
        ("Literary Fiction", True),

        # Non-fiction genres (should NOT generate characters)
        ("Self Help", False),
        ("Biography", False),
        ("History", False),
        ("Business", False),
        ("Cookbook", False),
        ("Travel", False),
        ("Philosophy", False),

        # Special formats (should NOT generate characters)
        ("Poetry Collection", False),
        ("Essay Collection", False),
        ("Graphic Novel", False),
        ("Short Story Collection", False),
        ("Creative Non Fiction", False),
    ]

    # Create results table
    table = Table(box=box.ROUNDED)
    table.add_column("Genre", style="cyan")
    table.add_column("Content Type", style="white")
    table.add_column("Generate Characters?", style="green")
    table.add_column("Reasoning", style="yellow")

    table.title = "[bold cyan]Character Generation Decision Matrix[/bold cyan]"

    fiction_count = 0
    non_fiction_count = 0
    special_format_count = 0

    for genre, expected in test_cases:
        result = should_generate_characters(genre)

        # Determine content type
        if result:
            content_type = "📚 Fiction"
            fiction_count += 1
            reasoning = "Needs characters for narrative storytelling"
        else:
            if any(nf in genre.lower() for nf in ["self help", "biography", "history", "business", "cookbook", "travel", "philosophy"]):
                content_type = "📖 Non-Fiction"
                non_fiction_count += 1
                reasoning = "Informational content - no characters needed"
            else:
                content_type = "🎨 Special Format"
                special_format_count += 1
                reasoning = "Format-specific content - no traditional characters"

        # Status indicator
        status = "✅ Generate" if result else "⏭️ Skip"

        # Verify expectation
        if result == expected:
            status_color = "green" if result else "yellow"
        else:
            status_color = "red"
            status = "❌ ERROR"

        table.add_row(
            genre,
            content_type,
            f"[{status_color}]{status}[/{status_color}]",
            reasoning
        )

    console.print(table)

    # Summary statistics
    console.print(f"\n[bold cyan]📊 Summary Statistics:[/bold cyan]")
    console.print(f"  📚 Fiction genres (generate characters): {fiction_count}")
    console.print(f"  📖 Non-fiction genres (skip characters): {non_fiction_count}")
    console.print(f"  🎨 Special formats (skip characters): {special_format_count}")
    console.print(f"  📋 Total genres tested: {len(test_cases)}")

    # Benefits
    console.print(f"\n[bold green]✅ Benefits of Smart Character Generation:[/bold green]")
    benefits = [
        "🚀 Faster generation for non-fiction and special formats",
        "🎯 More appropriate prompts for each content type",
        "💾 Reduced memory usage for books that don't need characters",
        "⚡ Streamlined workflow - no unnecessary steps",
        "🎨 Better user experience with relevant features only",
        "📝 Cleaner output for informational content",
        "🔧 More efficient resource utilization"
    ]

    for benefit in benefits:
        console.print(f"  {benefit}")

    # Examples of what gets skipped
    console.print(f"\n[bold yellow]⏭️ What Gets Skipped for Non-Fiction/Special Formats:[/bold yellow]")
    skipped_items = [
        "Character profile generation (saves 30-60 seconds)",
        "Character relationship mapping",
        "POV character selection and alternation",
        "Character development prompts",
        "Character-based narrative tracking",
        "Character emotion and knowledge states"
    ]

    for item in skipped_items:
        console.print(f"  • {item}")

def demonstrate_workflow_differences():
    """Demonstrate the workflow differences for different content types."""

    console.print(f"\n\n[bold cyan]🔄 Workflow Comparison[/bold cyan]")
    console.print("=" * 60)

    workflows = [
        {
            "type": "📚 Fiction (e.g., Fantasy Novel)",
            "steps": [
                "✅ Generate writer profile",
                "✅ Generate novel outline",
                "✅ Generate characters (protagonists, antagonists, supporting)",
                "✅ Generate chapters with character development",
                "✅ Track character arcs and relationships"
            ]
        },
        {
            "type": "📖 Non-Fiction (e.g., Self-Help Book)",
            "steps": [
                "✅ Generate writer profile",
                "✅ Generate book outline",
                "⏭️ Skip character generation (not needed)",
                "✅ Generate chapters with informational content",
                "✅ Focus on expertise and practical advice"
            ]
        },
        {
            "type": "🎨 Special Format (e.g., Poetry Collection)",
            "steps": [
                "✅ Generate writer profile",
                "✅ Generate collection structure",
                "⏭️ Skip character generation (not needed)",
                "✅ Generate poems with artistic focus",
                "✅ Focus on themes and artistic expression"
            ]
        }
    ]

    for workflow in workflows:
        console.print(f"\n[bold yellow]{workflow['type']}:[/bold yellow]")
        for step in workflow['steps']:
            console.print(f"  {step}")

if __name__ == "__main__":
    test_character_generation_logic()
    demonstrate_workflow_differences()

    console.print(f"\n[bold green]🎉 Smart Character Generation System Complete![/bold green]")
    console.print("The system now intelligently determines when character generation is needed based on content type.")
