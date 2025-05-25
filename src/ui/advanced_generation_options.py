#!/usr/bin/env python3
"""
Advanced Generation Options System

This system provides smart generation presets that leverage the automated
fictional author system to create unique and engaging content experiences:

1. "Surprise Me" Mode - Full automation with random selections
2. "Author Focus" Mode - Explore specific fictional authors
3. "Cultural Journey" Mode - Explore different cultural perspectives
4. "Genre Fusion" Mode - Blend multiple genres intelligently
"""

import random
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.columns import Columns

from src.utils.writer_profile_manager import WriterProfileManager
from src.writer_profiles.profile_registry import registry
from src.utils.genre_defaults import get_all_genres, get_genre_defaults
from src.ui.terminal_ui import custom_style

console = Console(markup=True)

class AdvancedGenerationOptions:
    """Advanced generation options with smart presets."""

    def __init__(self):
        """Initialize the advanced generation options system."""
        self.profile_manager = WriterProfileManager()
        self.all_genres = get_all_genres()
        self.all_profiles = registry.get_all_profiles()

        # Cultural background mappings
        self.cultural_backgrounds = {
            "Western": ["British", "American", "Canadian"],
            "Indian": ["Indian", "Indian-American"],
            "East Asian": ["Japanese", "Chinese", "Korean"],
            "Latin American": ["Colombian", "Mexican", "Brazilian"],
            "African": ["African American", "Nigerian", "South African"],
            "European": ["French", "German", "Italian", "Spanish", "Russian-American", "Greek-American"],
            "Middle Eastern": ["Persian", "Arabic", "Turkish"]
        }

        # Genre fusion combinations
        self.fusion_combinations = {
            "Sci-Fi Mystery": ["Science Fiction", "Mystery"],
            "Fantasy Romance": ["Fantasy", "Romance"],
            "Historical Horror": ["Historical Fiction", "Horror"],
            "Literary Thriller": ["Literary Fiction", "Thriller"],
            "Paranormal Mystery": ["Paranormal Romance", "Mystery"],
            "Dystopian Romance": ["Dystopian", "Romance"],
            "Urban Fantasy Mystery": ["Urban Fantasy", "Mystery"],
            "Alternate History Thriller": ["Alternate History", "Thriller"],
            "Space Opera Romance": ["Science Fiction", "Romance"],
            "Gothic Literary": ["Horror", "Literary Fiction"]
        }

    def show_advanced_options_menu(self) -> Optional[Dict[str, Any]]:
        """Display the creative generation modes menu following clean design principles."""
        try:
            console.print()
            console.print("[bold cyan]🎨 Creative Generation Modes[/bold cyan]")
            console.print("    Smart presets that leverage our sophisticated fictional author system")
            console.print("    for unique and engaging content experiences")
            console.print()

            choice = questionary.select(
                "Choose your generation experience:",
                choices=[
                    "Surprise Me - Full automation with delightful randomness",
                    "Author Focus - Explore a specific fictional author's range",
                    "Cultural Journey - Discover diverse cultural perspectives",
                    "Genre Fusion - Blend multiple genres creatively",
                    "View Author Statistics",
                    "← Back to Content Creation"
                ],
                style=custom_style
            ).ask()

            if not choice:
                return None

            if "Surprise Me" in choice:
                return self.surprise_me_mode()
            elif "Author Focus" in choice:
                return self.author_focus_mode()
            elif "Cultural Journey" in choice:
                return self.cultural_journey_mode()
            elif "Genre Fusion" in choice:
                return self.genre_fusion_mode()
            elif "View Author Statistics" in choice:
                self.show_author_statistics()
                return self.show_advanced_options_menu()  # Return to menu
            else:
                return None

        except KeyboardInterrupt:
            return None
        except Exception as e:
            console.print(f"[red]Error in creative generation modes menu: {e}[/red]")
            return None

    def surprise_me_mode(self) -> Dict[str, Any]:
        """Surprise Me mode - full automation with delightful randomness."""
        console.print(Panel.fit(
            "[bold cyan]Surprise Me Mode[/bold cyan]\n"
            "Let the system choose everything for a delightful surprise!\n"
            "Perfect for discovering new genres and authors",
            border_style="cyan"
        ))

        # Randomly select genre
        genre = random.choice(self.all_genres)

        # Get genre defaults for themes and options
        genre_defaults = get_genre_defaults(genre)

        # Randomly select themes from the genre
        available_themes = genre_defaults.get("themes", [])
        num_themes = random.randint(2, min(4, len(available_themes)))
        themes = random.sample(available_themes, num_themes) if available_themes else []

        # Randomly select writing style
        writing_styles = ["descriptive", "concise", "lyrical", "conversational", "formal", "experimental"]
        writing_style = random.choice(writing_styles)

        # Randomly select target length
        target_lengths = ["short", "medium", "long"]
        target_length = random.choice(target_lengths)

        # Generate random title components
        title_adjectives = ["Hidden", "Lost", "Ancient", "Forgotten", "Secret", "Mysterious", "Golden", "Silver", "Dark", "Bright"]
        title_nouns = ["Journey", "Quest", "Mystery", "Adventure", "Story", "Tale", "Chronicle", "Legend", "Saga", "Dream"]

        title = f"The {random.choice(title_adjectives)} {random.choice(title_nouns)}"

        # Create description based on genre and themes
        description = f"A {genre.lower()} story exploring themes of {', '.join(themes[:2])}."

        # Show the surprise selection
        console.print(f"\n[bold green]Your Surprise Selection:[/bold green]")
        console.print(f"  Genre: [cyan]{genre}[/cyan]")
        console.print(f"  Title: [cyan]{title}[/cyan]")
        console.print(f"  Themes: [cyan]{', '.join(themes)}[/cyan]")
        console.print(f"  Writing Style: [cyan]{writing_style}[/cyan]")
        console.print(f"  Length: [cyan]{target_length}[/cyan]")

        # Automatically select fictional author
        selected_profile = self.profile_manager.get_auto_selected_profile_for_book(
            genre=genre,
            themes=themes,
            writing_style=writing_style,
            target_length=target_length
        )

        if selected_profile:
            author_name = selected_profile.get("name", "Unknown Author")
            console.print(f"  Fictional Author: [cyan]{author_name}[/cyan]")

            if "_enhancement" in selected_profile:
                console.print(f"  [green]AI-enhanced for this specific combination![/green]")

        # Confirm the surprise selection
        proceed = questionary.confirm(
            "Ready to generate this surprise book?",
            default=True,
            style=custom_style
        ).ask()

        if not proceed:
            return self.surprise_me_mode()  # Try again

        return {
            "mode": "surprise_me",
            "title": title,
            "genre": genre,
            "description": description,
            "themes": themes,
            "writing_style": writing_style,
            "target_length": target_length,
            "selected_profile": selected_profile,
            "author": selected_profile.get("name", "AI Author") if selected_profile else "AI Author"
        }

    def author_focus_mode(self) -> Optional[Dict[str, Any]]:
        """Author Focus mode - explore a specific fictional author's range."""
        console.print(Panel.fit(
            "[bold cyan]Author Focus Mode[/bold cyan]\n"
            "Choose a fictional author and explore their expertise\n"
            "Perfect for discovering an author's range and style",
            border_style="cyan"
        ))

        # Display available authors with their specializations
        self._display_author_showcase()

        # Let user select an author
        author_choices = []
        for profile in self.all_profiles:
            expertise = f"{', '.join(profile.primary_genres[:2])}"
            if len(profile.primary_genres) > 2:
                expertise += f" (+{len(profile.primary_genres) - 2} more)"

            author_choices.append(f"{profile.name} - {expertise} ({profile.cultural_background})")

        author_choices.append("Back to Advanced Options")

        selected_author = questionary.select(
            "Choose a fictional author to focus on:",
            choices=author_choices,
            style=custom_style
        ).ask()

        if not selected_author or "Back to Advanced Options" in selected_author:
            return None

        # Extract author name
        author_name = selected_author.split(" - ")[0]

        # Find the selected profile
        selected_profile = None
        for profile in self.all_profiles:
            if profile.name == author_name:
                selected_profile = profile
                break

        if not selected_profile:
            console.print("[red]Error: Could not find selected author[/red]")
            return None

        # Show author details
        console.print(f"\n[bold green]Exploring {author_name}[/bold green]")
        console.print(f"  Cultural Background: [cyan]{selected_profile.cultural_background}[/cyan]")
        console.print(f"  Primary Genres: [cyan]{', '.join(selected_profile.primary_genres)}[/cyan]")
        console.print(f"  Secondary Genres: [cyan]{', '.join(selected_profile.secondary_genres)}[/cyan]")
        console.print(f"  Style Tags: [cyan]{', '.join(selected_profile.tags)}[/cyan]")

        # Let user choose from author's genres
        available_genres = selected_profile.primary_genres + selected_profile.secondary_genres

        genre = questionary.select(
            f"Which genre would you like {author_name} to write in?",
            choices=available_genres + ["Surprise me with any of their genres"],
            style=custom_style
        ).ask()

        if not genre:
            return None

        if "Surprise me" in genre:
            genre = random.choice(available_genres)
            console.print(f"  Randomly selected: [cyan]{genre}[/cyan]")

        # Get genre-specific options
        genre_defaults = get_genre_defaults(genre)
        themes = genre_defaults.get("themes", [])[:3]  # Use first 3 themes

        # Generate title based on author and genre
        title = f"{author_name}'s {genre} Tale"
        description = f"A {genre.lower()} work by the fictional author {author_name}, showcasing their unique voice and style."

        # Load the full profile
        full_profile = self.profile_manager.get_master_profile_by_author(author_name)

        return {
            "mode": "author_focus",
            "title": title,
            "genre": genre,
            "description": description,
            "themes": themes,
            "writing_style": "author_signature",  # Use author's signature style
            "target_length": "medium",
            "selected_profile": full_profile,
            "author": author_name,
            "focus_author": author_name
        }

    def cultural_journey_mode(self) -> Optional[Dict[str, Any]]:
        """Cultural Journey mode - explore different cultural perspectives."""
        console.print(Panel.fit(
            "[bold cyan]Cultural Journey Mode[/bold cyan]\n"
            "Explore literature from different cultural perspectives\n"
            "Perfect for discovering diverse voices and traditions",
            border_style="cyan"
        ))

        # Display cultural regions
        console.print(f"\n[bold cyan]Available Cultural Regions:[/bold cyan]")

        cultural_choices = []
        for region, backgrounds in self.cultural_backgrounds.items():
            # Count authors from this region
            author_count = sum(1 for profile in self.all_profiles
                             if profile.cultural_background in backgrounds)

            if author_count > 0:
                cultural_choices.append(f"{region} - {author_count} authors ({', '.join(backgrounds[:2])})")

        cultural_choices.append("Surprise me with any culture")
        cultural_choices.append("Back to Advanced Options")

        selected_culture = questionary.select(
            "Choose a cultural perspective to explore:",
            choices=cultural_choices,
            style=custom_style
        ).ask()

        if not selected_culture or "Back to Advanced Options" in selected_culture:
            return None

        # Determine cultural backgrounds to use
        if "Surprise me" in selected_culture:
            # Random culture
            region = random.choice(list(self.cultural_backgrounds.keys()))
            backgrounds = self.cultural_backgrounds[region]
            console.print(f"  Randomly selected: [cyan]{region}[/cyan]")
        else:
            region = selected_culture.split(" - ")[0]
            backgrounds = self.cultural_backgrounds[region]

        # Find authors from this cultural background
        cultural_authors = [profile for profile in self.all_profiles
                          if profile.cultural_background in backgrounds]

        if not cultural_authors:
            console.print(f"[red]No authors found for {region} culture[/red]")
            return None

        # Select a random author from this culture
        selected_author_profile = random.choice(cultural_authors)

        # Select a genre from their expertise
        available_genres = selected_author_profile.primary_genres + selected_author_profile.secondary_genres
        genre = random.choice(available_genres)

        # Get cultural themes
        cultural_themes = {
            "Western": ["individualism", "freedom", "progress", "tradition"],
            "Indian": ["dharma", "family", "spirituality", "tradition", "modernity"],
            "East Asian": ["harmony", "honor", "family", "tradition", "balance"],
            "Latin American": ["community", "passion", "heritage", "struggle", "celebration"],
            "African": ["community", "heritage", "resilience", "identity", "tradition"],
            "European": ["history", "culture", "philosophy", "art", "society"],
            "Middle Eastern": ["honor", "tradition", "family", "faith", "heritage"]
        }

        themes = cultural_themes.get(region, ["culture", "identity", "tradition"])[:3]

        # Generate culturally-inspired title
        cultural_title_elements = {
            "Western": ["The American Dream", "Frontier Spirit", "New World"],
            "Indian": ["Monsoon", "Sacred River", "Ancient Wisdom"],
            "East Asian": ["Cherry Blossom", "Mountain Path", "Jade Garden"],
            "Latin American": ["Fiesta", "Desert Rose", "Golden Coast"],
            "African": ["Savanna", "Ancient Drums", "River of Life"],
            "European": ["Old World", "Cathedral", "Renaissance"],
            "Middle Eastern": ["Desert Wind", "Ancient City", "Golden Sands"]
        }

        title_elements = cultural_title_elements.get(region, ["Cultural", "Journey"])
        title = f"{random.choice(title_elements)}: A {genre} Story"

        description = f"A {genre.lower()} story from a {region} perspective, exploring themes of {', '.join(themes[:2])}."

        # Load the full profile
        full_profile = self.profile_manager.get_master_profile_by_author(selected_author_profile.name)

        console.print(f"\n[bold green]Your Cultural Journey:[/bold green]")
        console.print(f"  Cultural Region: [cyan]{region}[/cyan]")
        console.print(f"  Fictional Author: [cyan]{selected_author_profile.name}[/cyan] ({selected_author_profile.cultural_background})")
        console.print(f"  Genre: [cyan]{genre}[/cyan]")
        console.print(f"  Cultural Themes: [cyan]{', '.join(themes)}[/cyan]")

        return {
            "mode": "cultural_journey",
            "title": title,
            "genre": genre,
            "description": description,
            "themes": themes,
            "writing_style": "culturally_authentic",
            "target_length": "medium",
            "selected_profile": full_profile,
            "author": selected_author_profile.name,
            "cultural_region": region,
            "cultural_background": selected_author_profile.cultural_background
        }

    def genre_fusion_mode(self) -> Optional[Dict[str, Any]]:
        """Genre Fusion mode - blend multiple genres creatively."""
        console.print(Panel.fit(
            "[bold cyan]Genre Fusion Mode[/bold cyan]\n"
            "Blend multiple genres for unique storytelling experiences\n"
            "Perfect for experimental and innovative narratives",
            border_style="cyan"
        ))

        # Display fusion combinations
        console.print(f"\n[bold cyan]Popular Fusion Combinations:[/bold cyan]")

        fusion_choices = []
        for fusion_name, genres in self.fusion_combinations.items():
            fusion_choices.append(f"{fusion_name} - {' + '.join(genres)}")

        fusion_choices.extend([
            "Surprise me with a random fusion",
            "Create custom fusion",
            "Back to Advanced Options"
        ])

        selected_fusion = questionary.select(
            "Choose a genre fusion:",
            choices=fusion_choices,
            style=custom_style
        ).ask()

        if not selected_fusion or "Back to Advanced Options" in selected_fusion:
            return None

        # Determine genres to fuse
        if "Surprise me" in selected_fusion:
            # Random fusion
            fusion_name = random.choice(list(self.fusion_combinations.keys()))
            genres = self.fusion_combinations[fusion_name]
            console.print(f"  Randomly selected: [cyan]{fusion_name}[/cyan]")
        elif "Create custom" in selected_fusion:
            return self._create_custom_fusion()
        else:
            fusion_name = selected_fusion.split(" - ")[0]
            genres = self.fusion_combinations[fusion_name]

        # Select primary genre (first one)
        primary_genre = genres[0]
        secondary_genre = genres[1]

        # Find an author who can handle the primary genre
        suitable_authors = []
        for profile in self.all_profiles:
            if primary_genre in profile.primary_genres or primary_genre in profile.secondary_genres:
                suitable_authors.append(profile)

        if not suitable_authors:
            console.print(f"[red]No authors found for {primary_genre}[/red]")
            return None

        selected_author = random.choice(suitable_authors)

        # Combine themes from both genres
        primary_defaults = get_genre_defaults(primary_genre)
        secondary_defaults = get_genre_defaults(secondary_genre)

        primary_themes = primary_defaults.get("themes", [])[:2]
        secondary_themes = secondary_defaults.get("themes", [])[:2]
        combined_themes = primary_themes + secondary_themes

        # Remove duplicates while preserving order
        themes = list(dict.fromkeys(combined_themes))[:4]

        # Generate fusion title
        title = f"The {fusion_name.replace(' ', ' ')}"
        description = f"An innovative fusion of {primary_genre.lower()} and {secondary_genre.lower()}, blending the best of both genres."

        # Load the full profile
        full_profile = self.profile_manager.get_master_profile_by_author(selected_author.name)

        console.print(f"\n[bold green]Your Genre Fusion:[/bold green]")
        console.print(f"  Fusion Type: [cyan]{fusion_name}[/cyan]")
        console.print(f"  Primary Genre: [cyan]{primary_genre}[/cyan]")
        console.print(f"  Secondary Genre: [cyan]{secondary_genre}[/cyan]")
        console.print(f"  Fictional Author: [cyan]{selected_author.name}[/cyan]")
        console.print(f"  Blended Themes: [cyan]{', '.join(themes)}[/cyan]")

        return {
            "mode": "genre_fusion",
            "title": title,
            "genre": primary_genre,  # Use primary genre for generation
            "description": description,
            "themes": themes,
            "writing_style": "experimental",
            "target_length": "medium",
            "selected_profile": full_profile,
            "author": selected_author.name,
            "fusion_type": fusion_name,
            "primary_genre": primary_genre,
            "secondary_genre": secondary_genre
        }

    def _create_custom_fusion(self) -> Optional[Dict[str, Any]]:
        """Create a custom genre fusion."""
        console.print(f"\n[bold cyan]Create Custom Fusion[/bold cyan]")

        # Select first genre
        first_genre = questionary.select(
            "Select the first genre:",
            choices=self.all_genres,
            style=custom_style
        ).ask()

        if not first_genre:
            return None

        # Select second genre (exclude the first one)
        remaining_genres = [g for g in self.all_genres if g != first_genre]
        second_genre = questionary.select(
            "Select the second genre to fuse with:",
            choices=remaining_genres,
            style=custom_style
        ).ask()

        if not second_genre:
            return None

        # Create custom fusion name
        fusion_name = f"{first_genre}-{second_genre} Fusion"

        console.print(f"  Created: [cyan]{fusion_name}[/cyan]")

        # Continue with fusion logic
        genres = [first_genre, second_genre]

        # Find suitable author and continue as in genre_fusion_mode
        suitable_authors = []
        for profile in self.all_profiles:
            if first_genre in profile.primary_genres or first_genre in profile.secondary_genres:
                suitable_authors.append(profile)

        if not suitable_authors:
            console.print(f"[red]No authors found for {first_genre}[/red]")
            return None

        selected_author = random.choice(suitable_authors)

        # Combine themes
        first_defaults = get_genre_defaults(first_genre)
        second_defaults = get_genre_defaults(second_genre)

        first_themes = first_defaults.get("themes", [])[:2]
        second_themes = second_defaults.get("themes", [])[:2]
        combined_themes = first_themes + second_themes
        themes = list(dict.fromkeys(combined_themes))[:4]

        title = f"The {fusion_name}"
        description = f"A custom fusion of {first_genre.lower()} and {second_genre.lower()}, creating a unique narrative experience."

        full_profile = self.profile_manager.get_master_profile_by_author(selected_author.name)

        return {
            "mode": "genre_fusion",
            "title": title,
            "genre": first_genre,
            "description": description,
            "themes": themes,
            "writing_style": "experimental",
            "target_length": "medium",
            "selected_profile": full_profile,
            "author": selected_author.name,
            "fusion_type": fusion_name,
            "primary_genre": first_genre,
            "secondary_genre": second_genre,
            "custom_fusion": True
        }

    def _display_author_showcase(self):
        """Display a showcase of available fictional authors."""
        console.print(f"\n[bold cyan]Fictional Author Showcase[/bold cyan]")

        # Group authors by cultural background
        authors_by_culture = {}
        for profile in self.all_profiles:
            culture = profile.cultural_background
            if culture not in authors_by_culture:
                authors_by_culture[culture] = []
            authors_by_culture[culture].append(profile)

        # Display in columns
        culture_panels = []
        for culture, authors in sorted(authors_by_culture.items()):
            author_list = []
            for author in authors[:3]:  # Show first 3 authors per culture
                genres = f"{', '.join(author.primary_genres[:2])}"
                if len(author.primary_genres) > 2:
                    genres += f" (+{len(author.primary_genres) - 2})"
                author_list.append(f"• {author.name}\n  {genres}")

            if len(authors) > 3:
                author_list.append(f"... and {len(authors) - 3} more")

            panel_content = "\n\n".join(author_list)
            culture_panels.append(Panel(panel_content, title=f"[cyan]{culture}[/cyan]", width=25))

        # Display in columns
        if culture_panels:
            columns = Columns(culture_panels, equal=True, expand=True)
            console.print(columns)

    def show_author_statistics(self):
        """Show comprehensive author statistics."""
        console.print(Panel.fit(
            "[bold cyan]Fictional Author Statistics[/bold cyan]\n"
            "Comprehensive overview of our fictional author library",
            border_style="cyan"
        ))

        # Overall statistics
        total_authors = len(self.all_profiles)
        cultures = set(profile.cultural_background for profile in self.all_profiles)
        total_cultures = len(cultures)

        # Genre coverage
        all_covered_genres = set()
        for profile in self.all_profiles:
            all_covered_genres.update(profile.primary_genres)
            all_covered_genres.update(profile.secondary_genres)

        genre_coverage = (len(all_covered_genres) / len(self.all_genres)) * 100

        console.print(f"\n[bold cyan]Overall Statistics:[/bold cyan]")
        console.print(f"  Total Fictional Authors: [green]{total_authors}[/green]")
        console.print(f"  Cultural Backgrounds: [green]{total_cultures}[/green]")
        console.print(f"  Genre Coverage: [green]{genre_coverage:.1f}%[/green] ({len(all_covered_genres)}/{len(self.all_genres)} genres)")

        # Authors by culture
        console.print(f"\n[bold cyan]Authors by Cultural Background:[/bold cyan]")
        culture_counts = {}
        for profile in self.all_profiles:
            culture = profile.cultural_background
            culture_counts[culture] = culture_counts.get(culture, 0) + 1

        culture_table = Table()
        culture_table.add_column("Cultural Background", style="cyan")
        culture_table.add_column("Author Count", style="green")
        culture_table.add_column("Percentage", style="yellow")

        for culture, count in sorted(culture_counts.items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_authors) * 100
            culture_table.add_row(culture, str(count), f"{percentage:.1f}%")

        console.print(culture_table)

        # Genre expertise
        console.print(f"\n[bold cyan]Genre Expertise Distribution:[/bold cyan]")
        genre_counts = {}
        for profile in self.all_profiles:
            for genre in profile.primary_genres:
                genre_counts[genre] = genre_counts.get(genre, 0) + 1

        genre_table = Table()
        genre_table.add_column("Genre", style="cyan")
        genre_table.add_column("Expert Authors", style="green")
        genre_table.add_column("Coverage", style="yellow")

        for genre, count in sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:15]:  # Top 15
            coverage = "Excellent" if count >= 3 else "Good" if count >= 2 else "Limited"
            genre_table.add_row(genre, str(count), coverage)

        console.print(genre_table)

        # Most versatile authors
        console.print(f"\n[bold cyan]Most Versatile Authors:[/bold cyan]")
        versatile_authors = sorted(
            self.all_profiles,
            key=lambda p: len(p.primary_genres) + len(p.secondary_genres),
            reverse=True
        )[:10]

        versatile_table = Table()
        versatile_table.add_column("Author", style="cyan")
        versatile_table.add_column("Cultural Background", style="yellow")
        versatile_table.add_column("Total Genres", style="green")
        versatile_table.add_column("Primary Expertise", style="white")

        for author in versatile_authors:
            total_genres = len(author.primary_genres) + len(author.secondary_genres)
            primary_expertise = ", ".join(author.primary_genres[:2])
            if len(author.primary_genres) > 2:
                primary_expertise += f" (+{len(author.primary_genres) - 2})"

            versatile_table.add_row(
                author.name,
                author.cultural_background,
                str(total_genres),
                primary_expertise
            )

        console.print(versatile_table)

        # Recommendations
        console.print(f"\n[bold cyan]Recommendations:[/bold cyan]")

        # Find underrepresented genres
        underrepresented = [genre for genre, count in genre_counts.items() if count < 2]
        if underrepresented:
            console.print(f"  Consider exploring: [yellow]{', '.join(underrepresented[:5])}[/yellow]")

        # Find most popular cultures
        top_culture = max(culture_counts.items(), key=lambda x: x[1])
        console.print(f"  Most represented culture: [green]{top_culture[0]}[/green] ({top_culture[1]} authors)")

        # Find unique combinations
        unique_combos = []
        for profile in self.all_profiles:
            if len(set(profile.primary_genres)) >= 3:  # Authors with 3+ different primary genres
                unique_combos.append(profile.name)

        if unique_combos:
            console.print(f"  Most experimental authors: [cyan]{', '.join(unique_combos[:3])}[/cyan]")

# Global instance
advanced_options = AdvancedGenerationOptions()
