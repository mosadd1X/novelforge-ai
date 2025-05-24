#!/usr/bin/env python3
"""
User Feedback System for Generated Content

This system provides an intuitive interface for users to rate and provide
feedback on generated content, helping to validate the effectiveness of
the fictional author system.
"""

import sys
from pathlib import Path
from typing import Dict, List, Any

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from src.quality.content_quality_system import quality_system

console = Console(markup=True)

class FeedbackUI:
    """User interface for collecting feedback on generated content."""

    def __init__(self):
        """Initialize the feedback UI."""
        self.custom_style = questionary.Style([
            ('question', 'fg:#ff0066 bold'),
            ('answer', 'fg:#44ff00 bold'),
            ('pointer', 'fg:#ff0066 bold'),
            ('highlighted', 'fg:#ff0066 bold'),
            ('selected', 'fg:#cc5454'),
            ('separator', 'fg:#cc5454'),
            ('instruction', ''),
            ('text', ''),
            ('disabled', 'fg:#858585 italic')
        ])

    def collect_content_feedback(self, content_id: str, title: str,
                               fictional_author: str, genre: str) -> bool:
        """Collect comprehensive feedback for generated content."""
        try:
            console.print(Panel.fit(
                f"[bold cyan]Content Feedback[/bold cyan]\n"
                f"Title: {title}\n"
                f"Fictional Author: {fictional_author}\n"
                f"Genre: {genre}",
                border_style="cyan"
            ))

            # Overall rating
            console.print("\n[bold cyan]Overall Rating[/bold cyan]")
            rating = questionary.select(
                "How would you rate this content overall?",
                choices=[
                    "5 - Excellent (Exceeded expectations)",
                    "4 - Very Good (Met expectations well)",
                    "3 - Good (Met basic expectations)",
                    "2 - Fair (Below expectations)",
                    "1 - Poor (Well below expectations)"
                ],
                style=self.custom_style
            ).ask()

            if not rating:
                return False

            rating_value = int(rating[0])

            # Specific feedback categories
            console.print("\n[bold cyan]Specific Feedback Categories[/bold cyan]")
            feedback_categories = []

            # Author voice consistency
            voice_rating = questionary.select(
                "How well did the content match the fictional author's expected voice?",
                choices=[
                    "Excellent - Perfect match",
                    "Good - Mostly consistent",
                    "Fair - Somewhat consistent",
                    "Poor - Inconsistent"
                ],
                style=self.custom_style
            ).ask()

            if voice_rating:
                feedback_categories.append(f"Author Voice: {voice_rating}")

            # Genre appropriateness
            genre_rating = questionary.select(
                "How well did the content fit the selected genre?",
                choices=[
                    "Excellent - Perfect genre fit",
                    "Good - Mostly appropriate",
                    "Fair - Somewhat appropriate",
                    "Poor - Doesn't fit genre"
                ],
                style=self.custom_style
            ).ask()

            if genre_rating:
                feedback_categories.append(f"Genre Fit: {genre_rating}")

            # Story quality
            story_rating = questionary.select(
                "How would you rate the story/content quality?",
                choices=[
                    "Excellent - Engaging and well-crafted",
                    "Good - Interesting and readable",
                    "Fair - Adequate but unremarkable",
                    "Poor - Boring or poorly written"
                ],
                style=self.custom_style
            ).ask()

            if story_rating:
                feedback_categories.append(f"Story Quality: {story_rating}")

            # Character development (for fiction)
            if any(keyword in genre.lower() for keyword in ['fiction', 'novel', 'story']):
                character_rating = questionary.select(
                    "How would you rate the character development?",
                    choices=[
                        "Excellent - Rich, believable characters",
                        "Good - Well-developed characters",
                        "Fair - Basic character development",
                        "Poor - Weak or unrealistic characters"
                    ],
                    style=self.custom_style
                ).ask()

                if character_rating:
                    feedback_categories.append(f"Characters: {character_rating}")

            # Writing style
            style_rating = questionary.select(
                "How would you rate the writing style?",
                choices=[
                    "Excellent - Beautiful, engaging prose",
                    "Good - Clear and well-written",
                    "Fair - Adequate writing style",
                    "Poor - Awkward or unclear writing"
                ],
                style=self.custom_style
            ).ask()

            if style_rating:
                feedback_categories.append(f"Writing Style: {style_rating}")

            # Open-ended feedback
            console.print("\n[bold cyan]Additional Comments[/bold cyan]")
            feedback_text = questionary.text(
                "Any additional comments or suggestions? (Optional)",
                style=self.custom_style
            ).ask()

            if not feedback_text:
                feedback_text = ""

            # What did you like most?
            liked_most = questionary.text(
                "What did you like most about this content? (Optional)",
                style=self.custom_style
            ).ask()

            if liked_most:
                feedback_text += f"\n\nLiked most: {liked_most}"

            # What could be improved?
            improvements = questionary.text(
                "What could be improved? (Optional)",
                style=self.custom_style
            ).ask()

            if improvements:
                feedback_text += f"\n\nSuggested improvements: {improvements}"

            # Would you use this fictional author again?
            use_again = questionary.confirm(
                f"Would you choose {fictional_author} for future {genre} content?",
                default=True,
                style=self.custom_style
            ).ask()

            if use_again is not None:
                feedback_categories.append(f"Would use author again: {'Yes' if use_again else 'No'}")

            # Store feedback
            success = quality_system.add_user_feedback(
                content_id=content_id,
                rating=rating_value,
                feedback_text=feedback_text,
                feedback_categories=feedback_categories
            )

            if success:
                console.print(f"\n[bold green]✓[/bold green] Thank you for your feedback!")
                console.print(f"[dim]Your input helps improve the fictional author system.[/dim]")

                # Show quick summary
                console.print(f"\n[bold cyan]Feedback Summary:[/bold cyan]")
                console.print(f"  Overall Rating: {rating_value}/5")
                console.print(f"  Categories: {len(feedback_categories)}")
                if feedback_text.strip():
                    console.print(f"  Comments: Provided")

                return True
            else:
                console.print(f"[red]Failed to save feedback. Please try again.[/red]")
                return False

        except KeyboardInterrupt:
            console.print(f"\n[yellow]Feedback collection cancelled.[/yellow]")
            return False
        except Exception as e:
            console.print(f"[red]Error collecting feedback: {e}[/red]")
            return False

    def quick_rating(self, content_id: str, title: str) -> bool:
        """Collect a quick 1-5 star rating."""
        try:
            console.print(f"\n[bold cyan]Quick Rating for: {title}[/bold cyan]")

            rating = questionary.select(
                "Rate this content:",
                choices=[
                    "⭐⭐⭐⭐⭐ (5) - Excellent",
                    "⭐⭐⭐⭐ (4) - Very Good",
                    "⭐⭐⭐ (3) - Good",
                    "⭐⭐ (2) - Fair",
                    "⭐ (1) - Poor"
                ],
                style=self.custom_style
            ).ask()

            if not rating:
                return False

            rating_value = int(rating.split('(')[1].split(')')[0])

            success = quality_system.add_user_feedback(
                content_id=content_id,
                rating=rating_value,
                feedback_text="Quick rating",
                feedback_categories=["quick_rating"]
            )

            if success:
                console.print(f"[green]✓[/green] Rating saved: {rating_value}/5")
                return True
            else:
                console.print(f"[red]Failed to save rating.[/red]")
                return False

        except Exception as e:
            console.print(f"[red]Error saving quick rating: {e}[/red]")
            return False

    def view_feedback_summary(self, days: int = 30):
        """Display a summary of recent feedback."""
        try:
            console.print(Panel.fit(
                f"[bold cyan]Feedback Summary - Last {days} Days[/bold cyan]",
                border_style="cyan"
            ))

            # Get overall feedback report
            report = quality_system.get_quality_report(days=days)

            if not report or not report.get("user_feedback"):
                console.print("[yellow]No feedback data available for the specified period.[/yellow]")
                return

            feedback = report["user_feedback"]
            stats = report.get("generation_stats", {})

            # Display summary statistics
            console.print(f"\n[bold cyan]Overall Statistics:[/bold cyan]")
            console.print(f"  Average Rating: {feedback['avg_rating']:.1f}/5.0")
            console.print(f"  Total Feedback Entries: {feedback['feedback_count']}")
            console.print(f"  Content Generated: {stats.get('total_content', 0)}")
            console.print(f"  Feedback Rate: {(feedback['feedback_count'] / max(stats.get('total_content', 1), 1) * 100):.1f}%")

            # Get author comparison
            author_comparison = quality_system.get_author_performance_comparison()

            if author_comparison.get("author_ratings"):
                console.print(f"\n[bold cyan]Top Rated Fictional Authors:[/bold cyan]")

                # Sort authors by rating
                sorted_authors = sorted(
                    author_comparison["author_ratings"].items(),
                    key=lambda x: x[1]["avg_rating"],
                    reverse=True
                )

                table = Table()
                table.add_column("Fictional Author", style="cyan")
                table.add_column("Avg Rating", style="green")
                table.add_column("Feedback Count", style="yellow")

                for author, data in sorted_authors[:10]:  # Top 10
                    table.add_row(
                        author,
                        f"{data['avg_rating']:.1f}/5.0",
                        str(data['count'])
                    )

                console.print(table)

            # Show recommendations
            recommendations = quality_system.get_improvement_recommendations()
            if recommendations:
                console.print(f"\n[bold cyan]Improvement Recommendations:[/bold cyan]")
                for i, rec in enumerate(recommendations[:5], 1):  # Top 5
                    console.print(f"  {i}. {rec}")

        except Exception as e:
            console.print(f"[red]Error displaying feedback summary: {e}[/red]")

    def feedback_menu(self):
        """Display the main feedback menu."""
        while True:
            try:
                console.print(Panel.fit(
                    "[bold cyan]Feedback System[/bold cyan]\n"
                    "Manage and view content feedback",
                    border_style="cyan"
                ))

                choice = questionary.select(
                    "What would you like to do?",
                    choices=[
                        "View Feedback Summary (Last 30 Days)",
                        "View Feedback Summary (Last 7 Days)",
                        "View Author Performance Comparison",
                        "View Quality Dashboard",
                        "Back to Main Menu"
                    ],
                    style=self.custom_style
                ).ask()

                if not choice:
                    break

                if "Last 30 Days" in choice:
                    self.view_feedback_summary(30)
                elif "Last 7 Days" in choice:
                    self.view_feedback_summary(7)
                elif "Author Performance" in choice:
                    self._show_author_performance()
                elif "Quality Dashboard" in choice:
                    self._show_quality_dashboard()
                elif "Back to Main Menu" in choice:
                    break

                # Pause for user to read
                console.print(f"\n[dim]Press Enter to continue...[/dim]")
                input()

            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"[red]Error in feedback menu: {e}[/red]")
                break

    def _show_author_performance(self):
        """Show detailed author performance comparison."""
        try:
            comparison = quality_system.get_author_performance_comparison()

            if not comparison.get("author_ratings"):
                console.print("[yellow]No author performance data available.[/yellow]")
                return

            console.print(f"\n[bold cyan]Fictional Author Performance Comparison[/bold cyan]")

            # Create detailed table
            table = Table(title="Author Performance (Last 30 Days)")
            table.add_column("Fictional Author", style="cyan")
            table.add_column("Avg Rating", style="green")
            table.add_column("Feedback Count", style="yellow")
            table.add_column("Performance", style="white")

            sorted_authors = sorted(
                comparison["author_ratings"].items(),
                key=lambda x: x[1]["avg_rating"],
                reverse=True
            )

            for author, data in sorted_authors:
                rating = data["avg_rating"]
                count = data["count"]

                # Performance indicator
                if rating >= 4.5:
                    performance = "Excellent"
                elif rating >= 4.0:
                    performance = "Very Good"
                elif rating >= 3.5:
                    performance = "Good"
                elif rating >= 3.0:
                    performance = "Fair"
                else:
                    performance = "Needs Improvement"

                table.add_row(
                    author,
                    f"{rating:.1f}/5.0",
                    str(count),
                    performance
                )

            console.print(table)

        except Exception as e:
            console.print(f"[red]Error showing author performance: {e}[/red]")

    def _show_quality_dashboard(self):
        """Show the quality dashboard."""
        try:
            # Ask for filters
            author_filter = questionary.text(
                "Filter by fictional author (optional, press Enter to skip):",
                style=self.custom_style
            ).ask()

            genre_filter = questionary.text(
                "Filter by genre (optional, press Enter to skip):",
                style=self.custom_style
            ).ask()

            # Display dashboard
            quality_system.display_quality_dashboard(
                fictional_author=author_filter if author_filter else None,
                genre=genre_filter if genre_filter else None
            )

        except Exception as e:
            console.print(f"[red]Error showing quality dashboard: {e}[/red]")

# Global feedback UI instance
feedback_ui = FeedbackUI()
