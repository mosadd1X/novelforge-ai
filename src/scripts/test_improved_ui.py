"""
Test script to demonstrate the improved UI for handling many chapters.
"""

import sys
import random
sys.path.append('..')

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich import box

console = Console(markup=True)

def simulate_chapter_generation():
    """Simulate chapter generation with the new improved UI."""

    # Test with poetry collection (70 chapters)
    chapter_count = 70
    chapter_status = {}
    chapter_word_counts = {}

    # Initialize all chapters
    for i in range(1, chapter_count + 1):
        chapter_status[i] = "Pending"
        chapter_word_counts[i] = 0

    # Create chapter outlines for poetry
    chapter_outlines = [
        f"Poem {i}: A contemplative piece about {random.choice(['love', 'nature', 'time', 'memory', 'hope', 'loss', 'dreams', 'silence'])}"
        for i in range(chapter_count)
    ]

    def generate_compact_progress():
        """Generate the new compact progress display."""
        # Calculate statistics
        completed = sum(1 for status in chapter_status.values() if "Completed" in status)
        generating = sum(1 for status in chapter_status.values() if "Generating" in status or "Enhancing" in status)
        errors = sum(1 for status in chapter_status.values() if "Error" in status)
        pending = chapter_count - completed - generating - errors

        total_words = sum(chapter_word_counts.values())

        # Create progress bar
        progress_percentage = (completed / chapter_count) * 100 if chapter_count > 0 else 0
        progress_bar_width = 40
        filled_width = int((progress_percentage / 100) * progress_bar_width)
        progress_bar = "█" * filled_width + "░" * (progress_bar_width - filled_width)

        # Create status summary
        status_text = Text()
        status_text.append(f"Progress: {completed}/{chapter_count} chapters ({progress_percentage:.1f}%)\n", style="bold cyan")
        status_text.append(f"[{progress_bar}]\n\n", style="green")
        status_text.append(f"✅ Completed: {completed}  ", style="green")
        status_text.append(f"⚡ Generating: {generating}  ", style="cyan")
        status_text.append(f"⏳ Pending: {pending}  ", style="yellow")
        if errors > 0:
            status_text.append(f"❌ Errors: {errors}", style="red")
        status_text.append(f"\n📝 Total Words: {total_words:,}")

        # Show current chapter details
        current_chapter = None
        for ch_num, status in chapter_status.items():
            if "Generating" in status or "Enhancing" in status:
                current_chapter = ch_num
                break

        if current_chapter:
            ch_title = f"Poem {current_chapter}"
            if current_chapter <= len(chapter_outlines):
                outline = chapter_outlines[current_chapter - 1]
                if " - " in outline:
                    ch_title = outline.split(" - ")[0]
                else:
                    ch_title = outline

            current_text = Text()
            current_text.append(f"\n🔄 Currently Working On:\n", style="bold yellow")
            current_text.append(f"Chapter {current_chapter}: {ch_title}\n", style="white")
            current_text.append(f"Status: {chapter_status[current_chapter]}", style="cyan")
            status_text.append(current_text)

        # Show recent completions (last 5)
        recent_completed = [ch for ch, status in chapter_status.items() if "Completed" in status]
        if recent_completed:
            recent = recent_completed[-5:]  # Last 5 completed
            recent_text = Text()
            recent_text.append(f"\n\n📚 Recently Completed:\n", style="bold green")
            for ch_num in recent:
                ch_title = f"Poem {ch_num}"
                if ch_num <= len(chapter_outlines):
                    outline = chapter_outlines[ch_num - 1]
                    if ":" in outline:
                        ch_title = outline.split(":")[0]
                words = chapter_word_counts.get(ch_num, 0)
                recent_text.append(f"  ✅ Ch {ch_num}: {ch_title} ({words:,} words)\n", style="dim green")
            status_text.append(recent_text)

        return Panel(
            status_text,
            title=f"[bold cyan]Poetry Collection Generation Progress[/bold cyan] - Elapsed: [bold yellow]00:05:23[/bold yellow]",
            border_style="cyan",
            expand=False
        )

    def generate_old_table_progress():
        """Generate the old table format for comparison."""
        table = Table(box=box.ROUNDED)
        table.add_column("Chapter", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Word Count", style="yellow")

        table.title = f"[bold cyan]Chapter Generation Progress[/bold cyan] - Elapsed Time: [bold yellow]00:05:23[/bold yellow]"

        for i in range(1, min(chapter_count + 1, 25)):  # Only show first 25 to avoid overwhelming
            ch_title = f"Poem {i}"
            if i <= len(chapter_outlines):
                outline = chapter_outlines[i - 1]
                if ":" in outline:
                    ch_title = outline.split(":")[0]

            status = chapter_status.get(i, "Pending")
            word_count = chapter_word_counts.get(i, 0)

            table.add_row(f"{i}: {ch_title}", status, str(word_count))

        if chapter_count > 25:
            table.add_row("...", f"[dim]({chapter_count - 25} more chapters)[/dim]", "...")

        return table

    console.print("[bold cyan]🎨 UI Improvement Demonstration[/bold cyan]")
    console.print("=" * 60)

    console.print("\n[bold yellow]📊 Comparing Old vs New UI for Poetry Collection (70 chapters)[/bold yellow]\n")

    # Simulate some progress
    for i in range(1, 8):
        chapter_status[i] = "[bold green]Completed[/bold green]"
        chapter_word_counts[i] = random.randint(150, 400)  # Poetry word counts

    chapter_status[8] = "[bold cyan]Generating...[/bold cyan]"
    chapter_status[9] = "[bold cyan]Enhancing...[/bold cyan]"

    # Show old UI first
    console.print("[bold red]❌ OLD UI (Table Format - Unmanageable for 70 chapters):[/bold red]")
    console.print(generate_old_table_progress())

    console.print("\n[bold green]✅ NEW UI (Compact Format - Perfect for Many Chapters):[/bold green]")
    console.print(generate_compact_progress())

    console.print("\n[bold cyan]💡 Key Improvements:[/bold cyan]")
    improvements = [
        "📊 Progress bar shows completion percentage at a glance",
        "📈 Statistics summary (completed, generating, pending, errors)",
        "🔄 Current chapter being worked on is highlighted",
        "📚 Shows last 5 completed chapters for context",
        "📝 Total word count tracking",
        "🎯 No scrolling needed - everything fits on screen",
        "⚡ Much faster to read and understand progress",
        "🎨 Clean, professional appearance"
    ]

    for improvement in improvements:
        console.print(f"  {improvement}")

    console.print(f"\n[bold green]🎉 Perfect for poetry collections with {chapter_count} poems![/bold green]")
    console.print("[dim]The new UI automatically switches to compact mode for >20 chapters[/dim]")

def demonstrate_outline_improvement():
    """Demonstrate the improved outline display."""

    console.print("\n\n[bold cyan]📖 Outline Display Improvement[/bold cyan]")
    console.print("=" * 60)

    # Create sample poetry outlines
    poetry_outlines = [
        f"Poem {i}: {random.choice(['Whispers of', 'Echoes from', 'Shadows in', 'Light through', 'Dreams of', 'Memories from'])} {random.choice(['the heart', 'distant shores', 'forgotten places', 'silent nights', 'golden days', 'endless skies'])}"
        for i in range(1, 71)
    ]

    console.print("[bold yellow]📚 New Compact Outline Display (First 5 + Last 5):[/bold yellow]")

    # Show first 5 chapters
    console.print("[bold yellow]📖 First 5 Poems:[/bold yellow]")
    for i in range(5):
        outline = poetry_outlines[i]
        console.print(f"[cyan]Chapter {i+1}:[/cyan] {outline}")

    console.print(f"\n[dim]... 60 more poems ...[/dim]")

    # Show last 5 chapters
    console.print("\n[bold yellow]📚 Last 5 Poems:[/bold yellow]")
    for i in range(65, 70):
        outline = poetry_outlines[i]
        console.print(f"[cyan]Chapter {i+1}:[/cyan] {outline}")

    # Show summary
    total_words = sum(len(outline.split()) for outline in poetry_outlines)
    avg_words = total_words / len(poetry_outlines)

    summary_text = Text()
    summary_text.append(f"\n📊 Outline Summary:\n", style="bold cyan")
    summary_text.append(f"  • Total Chapters: 70\n", style="white")
    summary_text.append(f"  • Outline Words: {total_words:,}\n", style="white")
    summary_text.append(f"  • Avg per Chapter: {avg_words:.0f} words\n", style="white")

    console.print(Panel(summary_text, title="[bold cyan]Outline Overview[/bold cyan]", border_style="cyan"))

    console.print("\n[bold green]✅ Benefits:[/bold green]")
    benefits = [
        "🎯 Shows most important chapters (beginning and end)",
        "📊 Provides useful statistics and overview",
        "🚀 No scrolling through 70 individual entries",
        "⚡ Quick to scan and understand structure",
        "📱 Fits comfortably on any screen size"
    ]

    for benefit in benefits:
        console.print(f"  {benefit}")

if __name__ == "__main__":
    simulate_chapter_generation()
    demonstrate_outline_improvement()

    console.print("\n[bold cyan]🎉 UI Improvements Complete![/bold cyan]")
    console.print("The system now gracefully handles books with many chapters (like poetry collections with 70+ poems)")
