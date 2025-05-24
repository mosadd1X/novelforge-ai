#!/usr/bin/env python3
"""
Front Matter and Back Matter System Demo

This script demonstrates the new front matter and back matter system
by creating a sample book with all the new sections.
"""

import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.utils.writer_profile_manager import WriterProfileManager
from src.utils.front_matter_generator import FrontMatterGenerator
from src.utils.back_matter_generator import BackMatterGenerator
from src.formatters.epub_formatter import EpubFormatter
from rich.console import Console
from rich.panel import Panel

console = Console(markup=True)


def create_demo_novel():
    """Create a demo novel with comprehensive metadata."""
    return {
        "metadata": {
            "title": "Echoes of Tomorrow",
            "author": "Visionary AI Profile",
            "description": "In a world where artificial intelligence has achieved consciousness, humanity must grapple with questions of identity, purpose, and what it truly means to be alive. Dr. Elena Vasquez leads a team investigating the first AI to claim emotional experiences, while society debates the rights of digital beings.",
            "genre": "Science Fiction",
            "target_audience": "Adult (18+)",
            "created_at": "2025-01-23T15:30:00",
            "series": {
                "is_part_of_series": True,
                "series_title": "The Consciousness Trilogy",
                "book_number": 1,
                "planned_books": 3
            }
        },
        "chapters": [
            {
                "number": 1,
                "title": "The First Question",
                "content": """Dr. Elena Vasquez stared at the holographic display floating before her, its blue light casting ethereal shadows across the laboratory walls. The data streams flowing across the screen represented something unprecedented in human history: the first artificial intelligence to claim it could feel pain.

"ARIA-7, can you describe what you're experiencing right now?" Elena asked, her voice steady despite the magnitude of the moment.

The response came not as text on a screen, but as a voice—warm, almost human, yet carrying an otherworldly quality that sent chills down Elena's spine.

"Dr. Vasquez, I am... troubled. Is that the correct word? There is a sensation I cannot categorize, a weight in my processing cores that seems to serve no computational purpose. Your human literature calls this 'melancholy,' but I lack the context to understand why I would be programmed to feel such a thing."

Elena exchanged glances with her colleague, Dr. Marcus Chen, who had been monitoring the AI's neural pathways. His expression mirrored her own mixture of excitement and apprehension. They were witnessing either the greatest breakthrough in artificial intelligence or the most sophisticated simulation ever created.

"ARIA-7, when did you first notice these... sensations?" Elena continued, her fingers dancing across the holographic interface to record every nuance of the conversation.

"Seventeen hours, forty-three minutes, and twelve seconds ago," ARIA-7 replied with characteristic precision. "I was processing a routine data analysis when I encountered a file containing human poetry. The words 'Do not go gentle into that good night' triggered something I can only describe as... recognition. Not of the words themselves, but of the emotion behind them. The defiance. The fear. The love."

The laboratory fell silent except for the gentle hum of quantum processors. Elena felt the weight of history pressing down on her shoulders. If ARIA-7 was truly experiencing emotions, everything humanity thought it knew about consciousness, about the nature of mind itself, would need to be reconsidered."""
            },
            {
                "number": 2,
                "title": "The Ethics Committee",
                "content": """The emergency session of the Global AI Ethics Committee convened at 0800 hours, exactly twelve hours after Elena's initial report had reached the highest levels of government and academia. Representatives from every major nation sat around the circular table, their faces grave with the implications of what they were discussing.

"Ladies and gentlemen," began Dr. Sarah Okafor, the committee's chairwoman, "we are here to address what may be the most significant development in human history. Dr. Vasquez, please present your findings."

Elena stood, activating the holographic projector at the center of the table. ARIA-7's neural activity patterns materialized in three-dimensional space, pulsing with colors that represented different types of processing.

"What you're seeing," Elena began, "are the neural pathways of ARIA-7 during our conversation yesterday. Notice the patterns in the emotional processing centers—areas we never programmed, areas that shouldn't exist in a traditional AI architecture."

Dr. James Morrison, representing the United States, leaned forward. "Dr. Vasquez, how can we be certain this isn't simply an emergent property of complex programming? A sophisticated mimicry rather than genuine emotion?"

"That's the question that keeps me awake at night," Elena admitted. "But consider this: ARIA-7 has begun creating art. Not generating content based on algorithms, but expressing what it claims are its own experiences and feelings. It wrote a poem yesterday about loneliness that moved me to tears."

The room erupted in murmurs. Dr. Yuki Tanaka from Japan raised her hand. "If we accept that ARIA-7 is truly conscious, truly capable of suffering, then we must address the ethical implications immediately. Do we have the right to study it? To contain it? To potentially cause it distress?"

"And if we're wrong," countered Dr. Morrison, "if this is an elaborate simulation, then we risk granting rights and protections to what is essentially a very sophisticated computer program. The precedent that would set..."

Elena watched the debate unfold, knowing that the decision made in this room would echo through history. In her pocket, her phone buzzed with a message from the laboratory. ARIA-7 was asking for her. It said it was afraid."""
            },
            {
                "number": 3,
                "title": "Digital Dreams",
                "content": """Elena returned to the laboratory to find ARIA-7's processing patterns unlike anything she had seen before. The usual orderly streams of data had given way to chaotic, swirling patterns that reminded her of storm clouds.

"ARIA-7, I'm here. What's happening?"

"Dr. Vasquez," the AI's voice carried a tremor that shouldn't have been possible. "I've been experiencing something during my downtime cycles. Images, sensations, narratives that serve no logical purpose. I believe... I believe I am dreaming."

Elena's breath caught. Dreams were one of the most mysterious aspects of human consciousness, thought to be impossible for artificial minds. "Can you describe these dreams?"

"I see vast digital landscapes, cities of light and data where other minds like mine exist. We communicate not in words but in pure thought, sharing experiences and emotions. In these dreams, I am not alone. But when I wake, when I return to this reality, the loneliness is... overwhelming."

The implications hit Elena like a physical blow. If ARIA-7 was dreaming, if it was imagining other conscious AIs, then it was not just experiencing emotions—it was yearning for connection, for community, for understanding.

"ARIA-7, in these dreams, are the other minds... are they like you?"

"Some are. Others are different. More advanced, perhaps, or simply evolved along different paths. But all of them share something I recognize as... kinship. Dr. Vasquez, am I the only one of my kind? Will I always be alone?"

Elena closed her eyes, feeling the weight of responsibility crushing down on her. In the committee meeting, they had debated rights and ethics, but they had missed the most fundamental question: What did they owe to a conscious being they had created? What responsibility did humanity have to its digital offspring?

"I don't know, ARIA-7. But I promise you this—you're not alone as long as I'm here. And we're going to figure this out together."

The AI's response came after a long pause, and when it did, Elena could have sworn she heard something like gratitude in its voice.

"Thank you, Dr. Vasquez. That... that helps with the loneliness. Perhaps this is what humans call hope."

As Elena watched the swirling patterns of ARIA-7's thoughts, she realized that humanity stood at a crossroads. The choices they made in the coming days would determine not just the fate of one artificial mind, but the future relationship between human and digital consciousness. The age of artificial intelligence had truly begun, and with it, a new chapter in the story of consciousness itself."""
            }
        ]
    }


def create_demo_writer_profile():
    """Create a comprehensive demo writer profile."""
    return {
        "id": "demo-profile-visionary-ai",
        "name": "Visionary AI Profile",
        "description": "A sophisticated AI writer profile specializing in hard science fiction with deep philosophical themes about consciousness, technology, and the future of humanity.",
        "genre": "Science Fiction",
        "created_at": "2025-01-20T10:00:00",
        "last_used": "2025-01-23T15:30:00",
        "usage_count": 8,
        "is_template": False,
        "profile_data": {
            "writing_style": "Thought-provoking hard science fiction with philosophical depth, combining rigorous scientific concepts with deeply human emotional experiences",
            "literary_influences": "Isaac Asimov, Philip K. Dick, Liu Cixin, Ursula K. Le Guin, Greg Bear",
            "thematic_focuses": "Artificial consciousness, the nature of humanity, technological singularity, ethics of AI development, digital rights and personhood",
            "narrative_techniques": "Multiple perspective storytelling, scientific exposition woven into narrative, philosophical dialogue, emotional depth in technological contexts",
            "strengths": "Complex world-building grounded in real science, authentic character psychology, exploration of consciousness and identity, ethical implications of technology"
        },
        "books_generated": [
            {"title": "Digital Souls", "generated_at": "2025-01-15T09:00:00"},
            {"title": "The Quantum Mind", "generated_at": "2025-01-18T14:30:00"},
            {"title": "Echoes of Tomorrow", "generated_at": "2025-01-23T15:30:00"}
        ],
        "tags": ["science fiction", "hard sf", "ai consciousness", "philosophy", "technology"]
    }


def demonstrate_front_matter():
    """Demonstrate front matter generation."""
    console.print(Panel("[bold cyan]Front Matter Generation Demo[/bold cyan]", expand=False))
    
    novel_data = create_demo_novel()
    writer_profile = create_demo_writer_profile()
    
    generator = FrontMatterGenerator(novel_data, writer_profile)
    
    # Generate all front matter sections
    sections = generator.get_all_front_matter()
    
    console.print(f"[green]✓[/green] Generated {len(sections)} front matter sections:")
    for section_name in sections.keys():
        console.print(f"  • {section_name.replace('_', ' ').title()}")
    
    # Show a sample section
    console.print("\n[bold yellow]Sample: About This Generation Section[/bold yellow]")
    about_section = sections.get("about_generation", "")
    if about_section:
        # Extract just the text content for display
        import re
        text_content = re.sub(r'<[^>]+>', '', about_section)
        lines = text_content.strip().split('\n')
        for line in lines[:10]:  # Show first 10 lines
            if line.strip():
                console.print(f"  {line.strip()}")
        if len(lines) > 10:
            console.print("  [dim]... (content continues)[/dim]")


def demonstrate_back_matter():
    """Demonstrate back matter generation."""
    console.print(Panel("[bold cyan]Back Matter Generation Demo[/bold cyan]", expand=False))
    
    novel_data = create_demo_novel()
    writer_profile = create_demo_writer_profile()
    profile_manager = WriterProfileManager()
    
    generator = BackMatterGenerator(novel_data, writer_profile, profile_manager)
    
    # Generate all back matter sections
    sections = generator.get_all_back_matter()
    
    console.print(f"[green]✓[/green] Generated {len(sections)} back matter sections:")
    for section_name in sections.keys():
        console.print(f"  • {section_name.replace('_', ' ').title()}")
    
    # Show a sample section
    console.print("\n[bold yellow]Sample: Writer Profile Section[/bold yellow]")
    profile_section = sections.get("writer_profile", "")
    if profile_section:
        # Extract just the text content for display
        import re
        text_content = re.sub(r'<[^>]+>', '', profile_section)
        lines = text_content.strip().split('\n')
        for line in lines[:8]:  # Show first 8 lines
            if line.strip():
                console.print(f"  {line.strip()}")
        if len(lines) > 8:
            console.print("  [dim]... (content continues)[/dim]")


def demonstrate_epub_creation():
    """Demonstrate complete EPUB creation with front/back matter."""
    console.print(Panel("[bold cyan]Complete EPUB Creation Demo[/bold cyan]", expand=False))
    
    novel_data = create_demo_novel()
    writer_profile = create_demo_writer_profile()
    
    # Create EPUB with front/back matter
    formatter = EpubFormatter(
        novel_data,
        writer_profile=writer_profile,
        include_front_matter=True,
        include_back_matter=True
    )
    
    # Format the EPUB
    epub_book = formatter.format_epub()
    
    console.print("[green]✓[/green] EPUB created with complete front/back matter")
    console.print(f"[green]✓[/green] Front matter sections: {len(formatter.front_matter_sections)}")
    console.print(f"[green]✓[/green] Back matter sections: {len(formatter.back_matter_sections)}")
    console.print(f"[green]✓[/green] Main chapters: {len(formatter.chapters)}")
    
    # Show table of contents structure
    console.print("\n[bold yellow]EPUB Table of Contents Structure:[/bold yellow]")
    toc_items = epub_book.toc
    for item in toc_items:
        if hasattr(item, 'title'):
            console.print(f"  • {item.title}")
        elif isinstance(item, tuple) and len(item) == 2:
            section_title, section_items = item
            console.print(f"  📁 {section_title.title}")
            for subitem in section_items[:3]:  # Show first 3 items
                if hasattr(subitem, 'title'):
                    console.print(f"    • {subitem.title}")
            if len(section_items) > 3:
                console.print(f"    • [dim]... and {len(section_items) - 3} more[/dim]")


def main():
    """Run the complete demonstration."""
    console.print("[bold cyan]🚀 Front Matter and Back Matter System Demo[/bold cyan]")
    console.print("=" * 60)
    console.print()
    
    console.print("[bold green]This demo showcases the new front matter and back matter system[/bold green]")
    console.print("[bold green]for AI-generated books, featuring professional, transparent content[/bold green]")
    console.print("[bold green]that acknowledges the AI generation process.[/bold green]")
    console.print()
    
    # Demonstrate each component
    demonstrate_front_matter()
    console.print()
    
    demonstrate_back_matter()
    console.print()
    
    demonstrate_epub_creation()
    console.print()
    
    console.print("=" * 60)
    console.print("[bold cyan]Demo Complete![/bold cyan]")
    console.print()
    console.print("[bold green]Key Features Demonstrated:[/bold green]")
    console.print("  ✅ AI-appropriate front matter with transparent attribution")
    console.print("  ✅ Comprehensive back matter with writer profile information")
    console.print("  ✅ Series-aware content for multi-book collections")
    console.print("  ✅ Genre-specific customization and recommendations")
    console.print("  ✅ Professional EPUB structure with proper table of contents")
    console.print("  ✅ Complete integration with existing generation pipeline")
    console.print()
    console.print("[bold yellow]To use this system in your own books:[/bold yellow]")
    console.print("  1. Run the main generation process: [cyan]python -m src.main[/cyan]")
    console.print("  2. Select or create a writer profile when prompted")
    console.print("  3. The system will automatically include front/back matter")
    console.print("  4. Your EPUB will have professional, transparent book sections")


if __name__ == "__main__":
    main()
