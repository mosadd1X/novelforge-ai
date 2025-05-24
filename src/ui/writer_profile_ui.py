"""
Writer Profile UI Components

This module provides user interface components for managing writer profiles,
including selection, creation, and customization of AI writer profiles.
"""

import questionary
from typing import Dict, List, Any, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box

from src.utils.writer_profile_manager import WriterProfileManager
from src.utils.genre_defaults import get_all_genres
from src.ui.terminal_ui import custom_style, clear_screen, display_title

console = Console(markup=True)


class WriterProfileUI:
    """
    User interface for writer profile management.
    """

    def __init__(self):
        """Initialize the writer profile UI."""
        self.profile_manager = WriterProfileManager()

        # Ensure default templates exist
        try:
            self.profile_manager.create_default_templates()
        except Exception:
            pass  # Templates might already exist

    def select_writer_profile(self, genre: str = None) -> Optional[Dict[str, Any]]:
        """
        Interactive writer profile selection with recommendations.

        Args:
            genre: Optional genre filter

        Returns:
            Selected writer profile or None if cancelled
        """
        while True:
            clear_screen()
            display_title()

            console.print("[bold cyan]Writer Profile Selection[/bold cyan]")
            console.print("Choose a writer profile to maintain consistent authorial voice across your books.\n")

            # Check for recommended profiles first
            recommended_profiles = []
            if genre:
                recommended_profiles = self.profile_manager.get_recommended_profiles(genre)

                if recommended_profiles:
                    console.print(f"[bold green]📋 Recommended profiles for {genre}:[/bold green]")
                    self._display_recommended_profiles(recommended_profiles, genre)

                    # Ask if user wants to use a recommended profile
                    use_recommended = questionary.confirm(
                        f"Would you like to use a recommended profile for {genre}?",
                        default=True,
                        style=custom_style
                    ).ask()

                    if use_recommended:
                        selected_profile = self._select_recommended_profile(recommended_profiles, genre)
                        if selected_profile:
                            # Track the selection
                            profile_id = selected_profile.get("id", f"recommended_{selected_profile.get('name', 'unknown').lower().replace(' ', '_')}")
                            self.profile_manager.track_profile_selection(profile_id, genre, "recommended")
                            return selected_profile

            # Get available profiles
            profiles = self.profile_manager.list_profiles(
                genre=genre,
                include_templates=True,
                include_archived=False
            )

            if not profiles and not recommended_profiles:
                console.print("[yellow]No writer profiles found. Creating a new profile...[/yellow]")
                return self.create_new_profile(genre)

            # Display existing profiles in a table
            if profiles:
                console.print(f"\n[bold yellow]📚 Available profiles{' for ' + genre if genre else ''}:[/bold yellow]")
                self._display_profiles_table(profiles, genre)

            # Create menu options
            choices = []
            profile_map = {}

            # Add recommended profiles if available
            if recommended_profiles:
                choices.append("🌟 Use Recommended Profile")

            # Add existing profiles
            for i, profile in enumerate(profiles[:8]):  # Limit to 8 for UI clarity
                display_name = f"{profile['name']}"
                if profile.get('is_template'):
                    display_name += " (Template)"
                if profile.get('usage_count', 0) > 0:
                    display_name += f" - Used {profile['usage_count']} times"

                choices.append(display_name)
                profile_map[display_name] = profile

            # Add management options
            choices.extend([
                "Create New Profile",
                "Browse All Profiles",
                "View Analytics",
                "← Back"
            ])

            selected = questionary.select(
                "Select a writer profile:",
                choices=choices,
                style=custom_style
            ).ask()

            if selected == "← Back":
                return None
            elif selected == "🌟 Use Recommended Profile":
                selected_profile = self._select_recommended_profile(recommended_profiles, genre)
                if selected_profile:
                    profile_id = selected_profile.get("id", f"recommended_{selected_profile.get('name', 'unknown').lower().replace(' ', '_')}")
                    self.profile_manager.track_profile_selection(profile_id, genre, "recommended")
                    return selected_profile
            elif selected == "Create New Profile":
                return self.create_new_profile(genre)
            elif selected == "Browse All Profiles":
                return self.browse_all_profiles()
            elif selected == "View Analytics":
                self._display_analytics(genre)
                continue
            elif selected in profile_map:
                profile = profile_map[selected]
                loaded_profile = self.profile_manager.load_profile(profile['id'])
                if loaded_profile:
                    self.profile_manager.track_profile_selection(profile['id'], genre or "unknown", "manual")
                return loaded_profile
    def _display_profiles_table(self, profiles: List[Dict[str, Any]], genre: str = None) -> None:
        """
        Display profiles in a formatted table.

        Args:
            profiles: List of profile summaries
            genre: Optional genre filter for highlighting
        """
        if not profiles:
            console.print("[yellow]No profiles available.[/yellow]")
            return

        table = Table(box=box.ROUNDED, show_header=True, header_style="bold cyan")
        table.add_column("Name", style="white", width=25)
        table.add_column("Genre", style="cyan", width=15)
        table.add_column("Usage", style="green", width=8)
        table.add_column("Type", style="yellow", width=10)
        table.add_column("Description", style="dim white", width=30)

        for profile in profiles[:10]:  # Show top 10
            name = profile.get('name', 'Unknown')
            profile_genre = profile.get('genre', 'Unknown')
            usage = str(profile.get('usage_count', 0))
            profile_type = "Template" if profile.get('is_template') else "Custom"
            description = profile.get('description', '')[:50]
            if len(profile.get('description', '')) > 50:
                description += "..."

            # Highlight matching genre
            if genre and profile_genre.lower() == genre.lower():
                name = f"[bold]{name}[/bold]"
                profile_genre = f"[bold]{profile_genre}[/bold]"

            table.add_row(name, profile_genre, usage, profile_type, description)

        console.print(table)
        console.print()

    def create_new_profile(self, genre: str = None) -> Optional[Dict[str, Any]]:
        """
        Create a new writer profile interactively.

        Args:
            genre: Optional default genre

        Returns:
            Created profile or None if cancelled
        """
        clear_screen()
        display_title()

        console.print("[bold cyan]Create New Writer Profile[/bold cyan]")
        console.print("Define a new AI writer profile with specific characteristics.\n")

        # Get profile name
        name = questionary.text(
            "Profile name:",
            validate=lambda text: len(text.strip()) > 0,
            style=custom_style
        ).ask()

        if not name:
            return None

        # Get genre
        if not genre:
            all_genres = get_all_genres()
            genre = questionary.select(
                "Primary genre for this profile:",
                choices=all_genres,
                style=custom_style
            ).ask()

        # Get description
        description = questionary.text(
            "Profile description (optional):",
            style=custom_style
        ).ask() or ""

        # Get writing characteristics
        console.print("\n[bold cyan]Define Writing Characteristics[/bold cyan]")

        writing_style = questionary.text(
            "Writing style (e.g., 'Elegant and sophisticated', 'Fast-paced and action-packed'):",
            default="Engaging and descriptive",
            style=custom_style
        ).ask()

        influences = questionary.text(
            "Literary influences (e.g., 'Virginia Woolf, Gabriel García Márquez'):",
            default="Various classic and contemporary authors",
            style=custom_style
        ).ask()

        themes = questionary.text(
            "Thematic focuses (e.g., 'Human condition, identity, relationships'):",
            default="Character development and emotional depth",
            style=custom_style
        ).ask()

        techniques = questionary.text(
            "Narrative techniques (e.g., 'Multiple perspectives, rich dialogue'):",
            default="Character-driven narratives with vivid descriptions",
            style=custom_style
        ).ask()

        strengths = questionary.text(
            "Key strengths (e.g., 'Complex characters, atmospheric settings'):",
            default="Creating compelling stories and authentic characters",
            style=custom_style
        ).ask()

        # Create profile data
        profile_data = {
            "writing_style": writing_style,
            "literary_influences": influences,
            "thematic_focuses": themes,
            "narrative_techniques": techniques,
            "strengths": strengths
        }

        # Ask if this should be a template
        is_template = questionary.confirm(
            "Save as template for future use?",
            default=False,
            style=custom_style
        ).ask()

        try:
            # Create the profile
            profile_id = self.profile_manager.create_profile(
                name=name,
                genre=genre,
                profile_data=profile_data,
                description=description,
                is_template=is_template
            )

            # Load and return the created profile
            profile = self.profile_manager.load_profile(profile_id)

            console.print(f"\n[bold green]✓[/bold green] Profile '{name}' created successfully!")
            input("Press Enter to continue...")

            return profile

        except Exception as e:
            console.print(f"\n[bold red]✗[/bold red] Failed to create profile: {e}")
            input("Press Enter to continue...")
            return None

    def browse_all_profiles(self) -> Optional[Dict[str, Any]]:
        """
        Browse all available profiles with filtering options.

        Returns:
            Selected profile or None
        """
        while True:
            clear_screen()
            display_title()

            console.print("[bold cyan]Browse All Writer Profiles[/bold cyan]")

            # Get filter options
            filter_choices = ["All Genres", "Filter by Genre", "Templates Only", "Custom Only", "← Back"]
            filter_choice = questionary.select(
                "How would you like to browse?",
                choices=filter_choices,
                style=custom_style
            ).ask()

            if filter_choice == "← Back":
                return None

            # Apply filters
            genre_filter = None
            include_templates = True
            include_custom = True

            if filter_choice == "Filter by Genre":
                all_genres = get_all_genres()
                genre_filter = questionary.select(
                    "Select genre:",
                    choices=all_genres,
                    style=custom_style
                ).ask()
            elif filter_choice == "Templates Only":
                include_custom = False
            elif filter_choice == "Custom Only":
                include_templates = False

            # Get filtered profiles
            all_profiles = self.profile_manager.list_profiles(
                genre=genre_filter,
                include_templates=include_templates,
                include_archived=False
            )

            # Filter custom profiles if needed
            if not include_custom:
                all_profiles = [p for p in all_profiles if p.get('is_template', False)]
            elif not include_templates:
                all_profiles = [p for p in all_profiles if not p.get('is_template', False)]

            if not all_profiles:
                console.print("[yellow]No profiles found with the selected filters.[/yellow]")
                input("Press Enter to continue...")
                continue

            # Display and select
            self._display_profiles_table(all_profiles, genre_filter)

            # Create selection choices
            choices = []
            profile_map = {}

            for profile in all_profiles:
                display_name = f"{profile['name']} ({profile['genre']})"
                if profile.get('is_template'):
                    display_name += " [Template]"

                choices.append(display_name)
                profile_map[display_name] = profile

            choices.append("← Back to Filters")

            selected = questionary.select(
                "Select a profile:",
                choices=choices,
                style=custom_style
            ).ask()

            if selected == "← Back to Filters":
                continue
            elif selected in profile_map:
                profile = profile_map[selected]
                return self.profile_manager.load_profile(profile['id'])

    def generate_random_profile(self, genre: str = None) -> Optional[Dict[str, Any]]:
        """
        Generate a random writer profile for the specified genre.

        Args:
            genre: Genre for the profile

        Returns:
            Generated profile or None
        """
        if not genre:
            all_genres = get_all_genres()
            genre = questionary.select(
                "Select genre for random profile:",
                choices=all_genres,
                style=custom_style
            ).ask()

        # This would integrate with the existing writer profile generation
        # For now, return None to indicate not implemented
        console.print("[yellow]Random profile generation will be integrated with the existing AI generation system.[/yellow]")
        input("Press Enter to continue...")
        return None

    def display_profile_info(self, profile: Dict[str, Any]) -> None:
        """
        Display detailed information about a profile.

        Args:
            profile: Profile data to display
        """
        clear_screen()
        display_title()

        name = profile.get('name', 'Unknown Profile')
        console.print(f"[bold cyan]Profile: {name}[/bold cyan]")

        # Basic info
        info_panel = Panel(
            f"[bold]Genre:[/bold] {profile.get('genre', 'Unknown')}\n"
            f"[bold]Description:[/bold] {profile.get('description', 'No description')}\n"
            f"[bold]Created:[/bold] {profile.get('created_at', 'Unknown')}\n"
            f"[bold]Usage Count:[/bold] {profile.get('usage_count', 0)}\n"
            f"[bold]Type:[/bold] {'Template' if profile.get('is_template') else 'Custom'}",
            title="Profile Information",
            border_style="cyan"
        )
        console.print(info_panel)

        # Profile characteristics
        profile_data = profile.get('profile_data', {})
        if profile_data:
            characteristics = ""
            for key, value in profile_data.items():
                formatted_key = key.replace('_', ' ').title()
                characteristics += f"[bold]{formatted_key}:[/bold] {value}\n"

            char_panel = Panel(
                characteristics.strip(),
                title="Writing Characteristics",
                border_style="green"
            )
            console.print(char_panel)

    def _display_recommended_profiles(self, profiles: List[Dict[str, Any]], genre: str) -> None:
        """
        Display recommended profiles in a formatted table.

        Args:
            profiles: List of recommended profiles
            genre: Genre these profiles are recommended for
        """
        if not profiles:
            console.print("[yellow]No recommended profiles available.[/yellow]")
            return

        table = Table(box=box.ROUNDED, show_header=True, header_style="bold green")
        table.add_column("Name", style="white", width=25)
        table.add_column("Style", style="cyan", width=15)
        table.add_column("Influences", style="yellow", width=30)
        table.add_column("Strengths", style="green", width=25)

        for profile in profiles[:5]:  # Show top 5 recommendations
            name = profile.get('name', 'Unknown')
            profile_data = profile.get('profile_data', {})

            # Extract style from name (Master, Innovator, etc.)
            style = "Custom"
            for style_variant in ["Master", "Innovator", "Storyteller", "Craftsperson", "Visionary"]:
                if style_variant in name:
                    style = style_variant
                    break

            influences = profile_data.get('literary_influences', 'Various authors')[:30]
            if len(profile_data.get('literary_influences', '')) > 30:
                influences += "..."

            strengths = profile_data.get('strengths', 'General writing')[:25]
            if len(profile_data.get('strengths', '')) > 25:
                strengths += "..."

            table.add_row(name, style, influences, strengths)

        console.print(table)
        console.print()

    def _select_recommended_profile(self, profiles: List[Dict[str, Any]], genre: str) -> Optional[Dict[str, Any]]:
        """
        Allow user to select from recommended profiles.

        Args:
            profiles: List of recommended profiles
            genre: Genre for context

        Returns:
            Selected profile or None
        """
        if not profiles:
            return None

        clear_screen()
        display_title()

        console.print(f"[bold cyan]Recommended Writer Profiles for {genre}[/bold cyan]")
        console.print("These profiles have been specifically curated for optimal results in this genre.\n")

        self._display_recommended_profiles(profiles, genre)

        # Create selection choices
        choices = []
        profile_map = {}

        for profile in profiles:
            name = profile.get('name', 'Unknown Profile')
            description = profile.get('description', '')[:60]
            if len(profile.get('description', '')) > 60:
                description += "..."

            display_name = f"{name} - {description}"
            choices.append(display_name)
            profile_map[display_name] = profile

        choices.append("← Back to Profile Selection")

        selected = questionary.select(
            "Select a recommended profile:",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "← Back to Profile Selection":
            return None
        elif selected in profile_map:
            return profile_map[selected]

        return None

    def _display_analytics(self, genre: str = None) -> None:
        """
        Display analytics information.

        Args:
            genre: Optional genre to focus analytics on
        """
        clear_screen()
        display_title()

        console.print("[bold cyan]Writer Profile Analytics[/bold cyan]")
        console.print("=" * 50)

        try:
            # Get analytics summary
            analytics = self.profile_manager.get_analytics_summary()

            if not analytics:
                console.print("[yellow]No analytics data available yet.[/yellow]")
                input("Press Enter to continue...")
                return

            # Display summary
            summary = analytics.get("summary", {})
            summary_panel = Panel(
                f"[bold]Total Profiles:[/bold] {summary.get('total_profiles', 0)}\n"
                f"[bold]Total Uses:[/bold] {summary.get('total_uses', 0)}\n"
                f"[bold]Active Genres:[/bold] {summary.get('active_genres', 0)}\n"
                f"[bold]Last Updated:[/bold] {summary.get('last_updated', 'Unknown')[:19]}",
                title="Analytics Summary",
                border_style="cyan"
            )
            console.print(summary_panel)

            # Display most used profiles
            most_used = analytics.get("most_used_profiles", [])
            if most_used:
                console.print("\n[bold yellow]📊 Most Used Profiles:[/bold yellow]")
                for i, (profile_id, usage_data) in enumerate(most_used[:5]):
                    profile = self.profile_manager.load_profile(profile_id)
                    name = profile.get("name", "Unknown") if profile else "Unknown"
                    console.print(f"  {i+1}. {name}: {usage_data['total_uses']} uses")

            # Display genre popularity
            genre_popularity = analytics.get("genre_popularity", {})
            if genre_popularity:
                console.print("\n[bold yellow]📚 Genre Popularity:[/bold yellow]")
                for i, (genre_name, data) in enumerate(list(genre_popularity.items())[:5]):
                    console.print(f"  {i+1}. {genre_name}: {data['total_selections']} selections")

            # Genre-specific analytics if requested
            if genre:
                console.print(f"\n[bold green]🎯 Analytics for {genre}:[/bold green]")
                # This would show detailed genre analytics
                # Implementation depends on the specific analytics structure

        except Exception as e:
            console.print(f"[red]Error loading analytics: {e}[/red]")

        input("\nPress Enter to continue...")

    def rate_profile_experience(self, profile_id: str, profile_name: str) -> None:
        """
        Allow user to rate their experience with a profile.

        Args:
            profile_id: ID of the profile to rate
            profile_name: Name of the profile for display
        """
        clear_screen()
        display_title()

        console.print(f"[bold cyan]Rate Your Experience with {profile_name}[/bold cyan]")
        console.print("Your feedback helps improve profile recommendations for everyone.\n")

        # Get rating
        rating = questionary.select(
            "How would you rate this writer profile?",
            choices=[
                "5 - Excellent (Perfect for my needs)",
                "4 - Very Good (Minor improvements possible)",
                "3 - Good (Adequate for the task)",
                "2 - Fair (Some issues but usable)",
                "1 - Poor (Not suitable for my needs)"
            ],
            style=custom_style
        ).ask()

        if not rating:
            return

        # Extract numeric rating
        numeric_rating = int(rating[0])

        # Get optional feedback
        feedback = questionary.text(
            "Any additional feedback? (optional):",
            style=custom_style
        ).ask() or ""

        # Record the satisfaction
        self.profile_manager.record_user_satisfaction(profile_id, numeric_rating, feedback)

        console.print(f"\n[bold green]✓[/bold green] Thank you for your feedback!")
        console.print("Your rating has been recorded and will help improve recommendations.")

        input("Press Enter to continue...")
