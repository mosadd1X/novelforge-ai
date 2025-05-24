"""
Writer Profile Management System for AI-Generated Books

This module provides functionality for managing persistent writer profiles
that can be reused across multiple book generations to maintain consistent
authorial voice and style.
"""

import json
import uuid
import importlib
from typing import Dict, List, Any, Optional
from datetime import datetime
from pathlib import Path

from src.utils.logger import log_info, log_error, log_warning
from src.utils.file_handler import sanitize_filename
from rich.console import Console

# Create console instance for output
console = Console(markup=True)


class WriterProfileManager:
    """
    Manages writer profiles for consistent authorial voice across books.
    """

    def __init__(self, profiles_dir: str = "src/writer_profiles"):
        """
        Initialize the Writer Profile Manager.

        Args:
            profiles_dir: Directory to store writer profiles
        """
        self.profiles_dir = Path(profiles_dir)
        self.profiles_dir.mkdir(parents=True, exist_ok=True)

        # Create subdirectories for organization
        (self.profiles_dir / "active").mkdir(exist_ok=True)
        (self.profiles_dir / "templates").mkdir(exist_ok=True)
        (self.profiles_dir / "archived").mkdir(exist_ok=True)
        (self.profiles_dir / "recommended").mkdir(exist_ok=True)
        (self.profiles_dir / "genre_recommendations").mkdir(exist_ok=True)

        # Analytics tracking
        self.analytics_file = self.profiles_dir / "analytics.json"
        self.analytics_data = self._load_analytics()

    def create_profile(
        self,
        name: str,
        genre: str,
        profile_data: Dict[str, Any],
        description: str = "",
        is_template: bool = False
    ) -> str:
        """
        Create a new writer profile.

        Args:
            name: Profile name
            genre: Primary genre for this profile
            profile_data: Writer profile data from generation
            description: Optional description of the profile
            is_template: Whether this is a template profile

        Returns:
            Profile ID (UUID)
        """
        profile_id = str(uuid.uuid4())

        # Prepare profile metadata
        profile = {
            "id": profile_id,
            "name": name,
            "description": description,
            "genre": genre,
            "created_at": datetime.now().isoformat(),
            "last_used": datetime.now().isoformat(),
            "usage_count": 0,
            "is_template": is_template,
            "profile_data": profile_data,
            "books_generated": [],
            "tags": [genre.lower()],
            "version": "1.0"
        }

        # Determine storage location
        subdir = "templates" if is_template else "active"
        filename = f"{sanitize_filename(name)}_{profile_id[:8]}.json"
        file_path = self.profiles_dir / subdir / filename

        # Save profile
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(profile, f, indent=2, ensure_ascii=False)

            log_info(f"Writer profile created: {name}", profile_id=profile_id)
            return profile_id

        except Exception as e:
            log_error(f"Failed to create writer profile: {name}", exception=e)
            raise

    def load_profile(self, profile_id: str) -> Optional[Dict[str, Any]]:
        """
        Load a writer profile by ID.

        Args:
            profile_id: Profile ID to load

        Returns:
            Profile data or None if not found
        """
        # Search in all subdirectories
        for subdir in ["active", "templates", "archived"]:
            for file_path in (self.profiles_dir / subdir).glob("*.json"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        profile = json.load(f)

                    if profile.get("id") == profile_id:
                        return profile

                except Exception as e:
                    log_warning(f"Failed to load profile file: {file_path}", exception=e)
                    continue

        return None

    def list_profiles(
        self,
        genre: str = None,
        include_templates: bool = True,
        include_archived: bool = False
    ) -> List[Dict[str, Any]]:
        """
        List available writer profiles.

        Args:
            genre: Filter by genre (optional)
            include_templates: Include template profiles
            include_archived: Include archived profiles

        Returns:
            List of profile summaries
        """
        profiles = []

        # Determine which directories to search
        search_dirs = ["active"]
        if include_templates:
            search_dirs.append("templates")
        if include_archived:
            search_dirs.append("archived")

        for subdir in search_dirs:
            for file_path in (self.profiles_dir / subdir).glob("*.json"):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        profile = json.load(f)

                    # Filter by genre if specified
                    if genre and profile.get("genre", "").lower() != genre.lower():
                        continue

                    # Create summary
                    summary = {
                        "id": profile.get("id"),
                        "name": profile.get("name"),
                        "description": profile.get("description", ""),
                        "genre": profile.get("genre"),
                        "created_at": profile.get("created_at"),
                        "last_used": profile.get("last_used"),
                        "usage_count": profile.get("usage_count", 0),
                        "is_template": profile.get("is_template", False),
                        "books_count": len(profile.get("books_generated", [])),
                        "tags": profile.get("tags", [])
                    }

                    profiles.append(summary)

                except Exception as e:
                    log_warning(f"Failed to load profile file: {file_path}", exception=e)
                    continue

        # Sort by last used (most recent first)
        profiles.sort(key=lambda x: x.get("last_used", ""), reverse=True)

        return profiles

    def track_profile_selection(self, profile_id: str, genre: str, selection_method: str = "manual") -> None:
        """
        Track when a profile is selected for analytics.

        Args:
            profile_id: ID of the selected profile
            genre: Genre of the book being generated
            selection_method: How the profile was selected (manual, recommended, default)
        """
        try:
            # Update genre preferences
            if genre not in self.analytics_data["genre_preferences"]:
                self.analytics_data["genre_preferences"][genre] = {
                    "recommendation_requests": 0,
                    "profiles_selected": {}
                }

            if profile_id not in self.analytics_data["genre_preferences"][genre]["profiles_selected"]:
                self.analytics_data["genre_preferences"][genre]["profiles_selected"][profile_id] = 0

            self.analytics_data["genre_preferences"][genre]["profiles_selected"][profile_id] += 1

            # Update profile usage tracking
            if profile_id not in self.analytics_data["profile_usage"]:
                self.analytics_data["profile_usage"][profile_id] = {
                    "total_uses": 0,
                    "genres_used": {},
                    "selection_methods": {},
                    "first_used": datetime.now().isoformat(),
                    "last_used": datetime.now().isoformat()
                }

            usage_data = self.analytics_data["profile_usage"][profile_id]
            usage_data["total_uses"] += 1
            usage_data["last_used"] = datetime.now().isoformat()

            # Track genre usage for this profile
            if genre not in usage_data["genres_used"]:
                usage_data["genres_used"][genre] = 0
            usage_data["genres_used"][genre] += 1

            # Track selection method
            if selection_method not in usage_data["selection_methods"]:
                usage_data["selection_methods"][selection_method] = 0
            usage_data["selection_methods"][selection_method] += 1

            self._save_analytics()

        except Exception as e:
            log_error("Failed to track profile selection", exception=e)

    def update_profile_usage(self, profile_id: str, book_title: str) -> bool:
        """
        Update profile usage statistics.

        Args:
            profile_id: Profile ID
            book_title: Title of the book generated

        Returns:
            True if updated successfully
        """
        profile = self.load_profile(profile_id)
        if not profile:
            return False

        # Update usage statistics
        profile["last_used"] = datetime.now().isoformat()
        profile["usage_count"] = profile.get("usage_count", 0) + 1

        # Add book to generated books list
        if "books_generated" not in profile:
            profile["books_generated"] = []

        profile["books_generated"].append({
            "title": book_title,
            "generated_at": datetime.now().isoformat()
        })

        # Save updated profile
        return self._save_profile(profile)

    def _save_profile(self, profile: Dict[str, Any]) -> bool:
        """
        Save a profile to disk.

        Args:
            profile: Profile data to save

        Returns:
            True if saved successfully
        """
        try:
            profile_id = profile["id"]
            name = profile["name"]
            is_template = profile.get("is_template", False)

            # Determine storage location
            subdir = "templates" if is_template else "active"
            filename = f"{sanitize_filename(name)}_{profile_id[:8]}.json"
            file_path = self.profiles_dir / subdir / filename

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(profile, f, indent=2, ensure_ascii=False)

            return True

        except Exception as e:
            log_error(f"Failed to save profile: {profile.get('name', 'Unknown')}", exception=e)
            return False

    def archive_profile(self, profile_id: str) -> bool:
        """
        Archive a profile (move to archived directory).

        Args:
            profile_id: Profile ID to archive

        Returns:
            True if archived successfully
        """
        profile = self.load_profile(profile_id)
        if not profile:
            return False

        try:
            # Find and remove original file
            for subdir in ["active", "templates"]:
                for file_path in (self.profiles_dir / subdir).glob("*.json"):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        existing_profile = json.load(f)

                    if existing_profile.get("id") == profile_id:
                        # Move to archived
                        name = profile["name"]
                        filename = f"{sanitize_filename(name)}_{profile_id[:8]}.json"
                        archived_path = self.profiles_dir / "archived" / filename

                        with open(archived_path, 'w', encoding='utf-8') as f:
                            json.dump(profile, f, indent=2, ensure_ascii=False)

                        # Remove original
                        file_path.unlink()

                        log_info(f"Profile archived: {name}", profile_id=profile_id)
                        return True

            return False

        except Exception as e:
            log_error(f"Failed to archive profile: {profile_id}", exception=e)
            return False

    def get_profile_books(self, profile_id: str) -> List[Dict[str, Any]]:
        """
        Get list of books generated with this profile.

        Args:
            profile_id: Profile ID

        Returns:
            List of book information
        """
        profile = self.load_profile(profile_id)
        if not profile:
            return []

        return profile.get("books_generated", [])

    def create_default_templates(self) -> None:
        """
        Create default template profiles for common genres.
        """
        default_templates = [
            {
                "name": "Classic Literary Fiction",
                "genre": "Literary Fiction",
                "description": "Sophisticated, character-driven narratives with rich prose",
                "profile_data": {
                    "writing_style": "Elegant and sophisticated with rich character development",
                    "literary_influences": "Virginia Woolf, Gabriel García Márquez, Toni Morrison",
                    "thematic_focuses": "Human condition, identity, social commentary",
                    "narrative_techniques": "Stream of consciousness, multiple perspectives, symbolism",
                    "strengths": "Deep character psychology, beautiful prose, thematic depth"
                }
            },
            {
                "name": "Epic Fantasy Worldbuilder",
                "genre": "Fantasy",
                "description": "Immersive fantasy worlds with complex magic systems",
                "profile_data": {
                    "writing_style": "Descriptive and immersive with detailed world-building",
                    "literary_influences": "J.R.R. Tolkien, Brandon Sanderson, Robin Hobb",
                    "thematic_focuses": "Good vs. evil, power and responsibility, coming of age",
                    "narrative_techniques": "Multiple POV, detailed magic systems, epic scope",
                    "strengths": "World-building, magic systems, character development"
                }
            },
            {
                "name": "Psychological Thriller",
                "genre": "Thriller",
                "description": "Mind-bending psychological suspense and tension",
                "profile_data": {
                    "writing_style": "Tense and atmospheric with psychological depth",
                    "literary_influences": "Gillian Flynn, Tana French, Thomas Harris",
                    "thematic_focuses": "Human psychology, moral ambiguity, hidden truths",
                    "narrative_techniques": "Unreliable narrators, psychological tension, plot twists",
                    "strengths": "Psychological insight, suspense building, character complexity"
                }
            }
        ]

        for template in default_templates:
            try:
                self.create_profile(
                    name=template["name"],
                    genre=template["genre"],
                    profile_data=template["profile_data"],
                    description=template["description"],
                    is_template=True
                )
            except Exception as e:
                log_warning(f"Failed to create default template: {template['name']}", exception=e)

    def _load_analytics(self) -> Dict[str, Any]:
        """Load analytics data from file."""
        try:
            if self.analytics_file.exists():
                with open(self.analytics_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            log_warning("Failed to load analytics data", exception=e)

        # Return default analytics structure
        return {
            "profile_usage": {},
            "genre_preferences": {},
            "creation_stats": {
                "total_profiles_created": 0,
                "profiles_by_genre": {},
                "profiles_by_month": {}
            },
            "performance_metrics": {
                "most_used_profiles": [],
                "genre_popularity": {},
                "user_satisfaction": {}
            },
            "last_updated": datetime.now().isoformat()
        }

    def _save_analytics(self) -> None:
        """Save analytics data to file."""
        try:
            self.analytics_data["last_updated"] = datetime.now().isoformat()
            with open(self.analytics_file, 'w', encoding='utf-8') as f:
                json.dump(self.analytics_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            log_error("Failed to save analytics data", exception=e)

    def get_recommended_profiles(self, genre: str) -> List[Dict[str, Any]]:
        """
        Get recommended master author profiles for a specific genre.

        Args:
            genre: Genre to get recommendations for

        Returns:
            List of recommended master author profile data
        """
        try:
            # Import the profile registry
            from src.writer_profiles.profile_registry import registry

            # Get profiles for this genre
            author_profiles = registry.get_profiles_for_genre(genre)

            # Load the actual profile data
            profiles = []
            for author_profile in author_profiles:
                try:
                    module_name = f"src.writer_profiles.master_profiles.{author_profile.module_name}"
                    module = importlib.import_module(module_name)
                    profile_data = module.get_profile()

                    # Add metadata
                    profile_data["_metadata"] = {
                        "cultural_background": author_profile.cultural_background,
                        "era": author_profile.era,
                        "tags": author_profile.tags,
                        "primary_genres": author_profile.primary_genres,
                        "secondary_genres": author_profile.secondary_genres
                    }

                    profiles.append(profile_data)

                except ImportError:
                    log_warning(f"Could not load master profile: {author_profile.module_name}")
                    continue

            # Track analytics
            if genre not in self.analytics_data["genre_preferences"]:
                self.analytics_data["genre_preferences"][genre] = {
                    "recommendation_requests": 0,
                    "profiles_selected": {}
                }

            self.analytics_data["genre_preferences"][genre]["recommendation_requests"] += 1
            self._save_analytics()

            return profiles

        except Exception as e:
            log_error(f"Failed to get recommendations for genre: {genre}", exception=e)
            return []

    def get_master_profile_by_author(self, author_name: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific master author profile by name.

        Args:
            author_name: Name of the author (e.g., "Virginia Woolf")

        Returns:
            Master author profile data or None if not found
        """
        try:
            # Import the profile registry
            from src.writer_profiles.profile_registry import registry

            # Get the author profile
            author_profile = registry.get_profile_by_name(author_name)
            if not author_profile:
                return None

            # Load the actual profile data
            module_name = f"src.writer_profiles.master_profiles.{author_profile.module_name}"
            module = importlib.import_module(module_name)
            profile_data = module.get_profile()

            # Add metadata
            profile_data["_metadata"] = {
                "cultural_background": author_profile.cultural_background,
                "era": author_profile.era,
                "tags": author_profile.tags,
                "primary_genres": author_profile.primary_genres,
                "secondary_genres": author_profile.secondary_genres
            }

            return profile_data

        except ImportError:
            log_warning(f"Could not load master profile for author: {author_name}")
            return None
        except Exception as e:
            log_error(f"Failed to get master profile for author: {author_name}", exception=e)
            return None

    def get_all_master_profiles(self) -> List[Dict[str, Any]]:
        """
        Get all available master author profiles.

        Returns:
            List of all master author profile data
        """
        try:
            # Import the profile registry
            from src.writer_profiles.profile_registry import registry

            # Get all author profiles
            author_profiles = registry.get_all_profiles()

            # Load the actual profile data
            profiles = []
            for author_profile in author_profiles:
                try:
                    module_name = f"src.writer_profiles.master_profiles.{author_profile.module_name}"
                    module = importlib.import_module(module_name)
                    profile_data = module.get_profile()

                    # Add metadata
                    profile_data["_metadata"] = {
                        "cultural_background": author_profile.cultural_background,
                        "era": author_profile.era,
                        "tags": author_profile.tags,
                        "primary_genres": author_profile.primary_genres,
                        "secondary_genres": author_profile.secondary_genres
                    }

                    profiles.append(profile_data)

                except ImportError:
                    log_warning(f"Could not load master profile: {author_profile.module_name}")
                    continue

            return profiles

        except Exception as e:
            log_error("Failed to get all master profiles", exception=e)
            return []

    def get_default_profile_for_genre(self, genre: str) -> Optional[Dict[str, Any]]:
        """
        Get the default recommended master author profile for a genre.

        Args:
            genre: Genre to get default profile for

        Returns:
            Default master author profile data or None
        """
        try:
            # Get all recommended profiles for this genre
            profiles = self.get_recommended_profiles(genre)

            if not profiles:
                return None

            # Define default fictional authors for all genres (automatic selection)
            genre_defaults = {
                "Literary Fiction": "Elena Thornfield",
                "Historical Fiction": "Marcus Steele",
                "Mystery": "Victoria Blackwood",
                "Horror": "Sebastian Darkmore",
                "Science Fiction": "Dr. Samuel Voss",
                "Fantasy": "Professor Aldrich Quantum",
                "Romance": "Catherine Fairfax",
                "Memoir": "Grace Washington",
                "Travel": "Anthony Rivers",
                "Popular Science": "Dr. Malcolm Sterling",
                "Business": "Dr. Patricia Blackwell",
                "Self-Help": "Dr. Patricia Blackwell",
                "How-To": "Dr. Patricia Blackwell",
                "Philosophy": "Professor Elena Vasquez",
                "Children's Chapter Books": "Luna Brightwater",
                "Middle Grade": "Luna Brightwater",
                "Graphic Novel": "Luna Brightwater",
                "Young Adult": "Luna Brightwater",
                "Academic": "Professor Elena Vasquez",
                "Essay Collection": "Professor Elena Vasquez",
                "True Crime": "Detective Marcus Kane",
                "Mystery/Thriller": "Detective Marcus Kane",
                "Thriller": "Detective Marcus Kane",
                "History": "Dr. Sophia Chronos",
                "Alternate History": "Dr. Sophia Chronos",
                "Romance": "Priya Sharma",
                "Contemporary Romance": "Priya Sharma",
                "Paranormal Romance": "Raven Nightshade",
                "Urban Fantasy": "Raven Nightshade",
                "Dystopian": "Zara Blackthorn",
                "Speculative Fiction": "Zara Blackthorn",
                "Contemporary Fiction": "Priya Sharma",
                "Short Story Collection": "Rajesh Malhotra",
                "Poetry Collection": "Kavya Nair",
                "Biography": "Grace Washington",
                "Autobiography": "Grace Washington",
                "Creative Non-Fiction": "Elena Thornfield",
                "Cookbook": "Anthony Rivers",
                "Inspirational": "Grace Washington",
                "Humor": "Rajesh Malhotra",
                "War Literature": "Marcus Steele",
                "Crime Fiction": "Victoria Blackwood",
                "Epic Fantasy": "Professor Aldrich Quantum",
                "Mythology": "Professor Aldrich Quantum",
                "Novella": "Victoria Blackwood",
                "Supernatural Fiction": "Sebastian Darkmore",
                "Surreal Fiction": "Hiroshi Nakamura",
                "Magical Realism": "Gabriel Montoya",
                "Social Commentary": "Arjun Krishnamurthy",
                "Political Fiction": "Arjun Krishnamurthy",
                "Cultural Literature": "Priya Sharma",
                "Environmental Literature": "Ananya Desai",
                "Cultural Commentary": "Anthony Rivers",
                "Cultural Studies": "Devika Ghosh",
                "Psychology": "Dr. Malcolm Sterling",
                "Commercial Fiction": "Rohan Mehta",
                "Epic Fiction": "Vikram Chandra"
            }

            # Try to find the preferred default author for this genre
            preferred_author = genre_defaults.get(genre)
            if preferred_author:
                for profile in profiles:
                    if profile["name"] == preferred_author:
                        return profile

            # If no specific default, return the first available profile
            return profiles[0]

        except Exception as e:
            log_error(f"Failed to get default profile for genre: {genre}", exception=e)
            return None

    def get_profile_by_style(self, genre: str, style: str) -> Optional[Dict[str, Any]]:
        """
        Get a profile by genre and style variant.

        Args:
            genre: Genre of the profile
            style: Style variant (Master, Innovator, Storyteller, etc.)

        Returns:
            Profile data or None
        """
        try:
            # Normalize genre name for file lookup
            genre_key = genre.lower().replace(" ", "_").replace("-", "_").replace("/", "_")

            # Try to import the genre recommendation module
            module_name = f"src.writer_profiles.genre_recommendations.{genre_key}"
            module = importlib.import_module(module_name)

            # Get profile by style
            profile = module.get_profile_by_style(style)

            # Track analytics if profile found
            if profile:
                self._track_style_selection(genre, style, profile.get("base_profile", "unknown"))

            return profile if profile else None

        except ImportError:
            log_warning(f"No style variants found for genre: {genre}")
            return None
        except Exception as e:
            log_error(f"Failed to get profile by style for genre: {genre}, style: {style}", exception=e)
            return None

    def get_available_styles_for_genre(self, genre: str) -> List[str]:
        """
        Get available style variants for a specific genre.

        Args:
            genre: Genre name

        Returns:
            List of available style names
        """
        try:
            # Normalize genre name for file lookup
            genre_key = genre.lower().replace(" ", "_").replace("-", "_").replace("/", "_")

            # Try to import the genre recommendation module
            module_name = f"src.writer_profiles.genre_recommendations.{genre_key}"
            module = importlib.import_module(module_name)

            # Get available styles
            if hasattr(module, 'get_available_styles'):
                return module.get_available_styles()

            # Default styles if not specified
            return ["Master", "Innovator", "Storyteller", "Craftsperson", "Commercial"]

        except ImportError:
            return []
        except Exception:
            return []

    def get_style_descriptions_for_genre(self, genre: str) -> Dict[str, str]:
        """
        Get style descriptions for a specific genre.

        Args:
            genre: Genre name

        Returns:
            Dictionary mapping style names to descriptions
        """
        try:
            # Normalize genre name for file lookup
            genre_key = genre.lower().replace(" ", "_").replace("-", "_").replace("/", "_")

            # Try to import the genre recommendation module
            module_name = f"src.writer_profiles.genre_recommendations.{genre_key}"
            module = importlib.import_module(module_name)

            # Get style descriptions
            if hasattr(module, 'get_style_descriptions'):
                return module.get_style_descriptions()

            return {}

        except ImportError:
            return {}
        except Exception:
            return {}

    def get_recommended_collections(self) -> List[Dict[str, Any]]:
        """
        Get all available recommended profile collections.

        Returns:
            List of collection metadata
        """
        try:
            from src.writer_profiles.recommended import get_available_collections, get_collection_metadata

            collections = []
            for collection_name in get_available_collections():
                metadata = get_collection_metadata(collection_name)
                if metadata:
                    collections.append({
                        "collection_name": collection_name,
                        **metadata
                    })

            return sorted(collections, key=lambda x: x.get("priority", 999))

        except Exception as e:
            log_error("Failed to get recommended collections", exception=e)
            return []

    def get_profiles_from_collection(self, collection_name: str) -> List[Dict[str, Any]]:
        """
        Get profiles from a specific recommended collection.

        Args:
            collection_name: Name of the collection

        Returns:
            List of profile data from the collection
        """
        try:
            from src.writer_profiles.recommended import get_profiles_from_collection

            profiles = get_profiles_from_collection(collection_name)

            # Track analytics
            if profiles:
                self._track_collection_access(collection_name, len(profiles))

            return profiles

        except Exception as e:
            log_error(f"Failed to get profiles from collection: {collection_name}", exception=e)
            return []

    def get_recommended_profile_for_goal(self, goal: str, genre: str = None) -> Optional[Dict[str, Any]]:
        """
        Get a recommended profile based on user goal and optional genre.

        Args:
            goal: User's goal (e.g., "commercial_success", "literary_excellence")
            genre: Optional genre filter

        Returns:
            Recommended profile or None if not found
        """
        try:
            from src.writer_profiles.recommended import get_recommended_profile_for_goal

            profile = get_recommended_profile_for_goal(goal, genre)

            # Track analytics
            if profile:
                self._track_goal_based_selection(goal, genre, profile.get("profile_id", "unknown"))

            return profile

        except Exception as e:
            log_error(f"Failed to get recommended profile for goal: {goal}", exception=e)
            return None

    def search_collections_by_genre(self, genre: str) -> List[Dict[str, Any]]:
        """
        Find collections that contain profiles suitable for a specific genre.

        Args:
            genre: Genre to search for

        Returns:
            List of matching collections with their metadata
        """
        try:
            from src.writer_profiles.recommended import search_collections_by_genre

            collections = search_collections_by_genre(genre)

            # Track analytics
            if collections:
                self._track_genre_collection_search(genre, len(collections))

            return collections

        except Exception as e:
            log_error(f"Failed to search collections for genre: {genre}", exception=e)
            return []

    def _track_style_selection(self, genre: str, style: str, profile_id: str) -> None:
        """Track style-based profile selection for analytics."""
        try:
            if "style_selections" not in self.analytics_data:
                self.analytics_data["style_selections"] = {}

            key = f"{genre}_{style}"
            if key not in self.analytics_data["style_selections"]:
                self.analytics_data["style_selections"][key] = {
                    "count": 0,
                    "profiles_used": {},
                    "last_used": None
                }

            self.analytics_data["style_selections"][key]["count"] += 1
            self.analytics_data["style_selections"][key]["last_used"] = datetime.now().isoformat()

            if profile_id not in self.analytics_data["style_selections"][key]["profiles_used"]:
                self.analytics_data["style_selections"][key]["profiles_used"][profile_id] = 0
            self.analytics_data["style_selections"][key]["profiles_used"][profile_id] += 1

            self._save_analytics()

        except Exception as e:
            log_error("Failed to track style selection", exception=e)

    def _track_collection_access(self, collection_name: str, profile_count: int) -> None:
        """Track collection access for analytics."""
        try:
            if "collection_access" not in self.analytics_data:
                self.analytics_data["collection_access"] = {}

            if collection_name not in self.analytics_data["collection_access"]:
                self.analytics_data["collection_access"][collection_name] = {
                    "access_count": 0,
                    "profiles_accessed": 0,
                    "last_accessed": None
                }

            self.analytics_data["collection_access"][collection_name]["access_count"] += 1
            self.analytics_data["collection_access"][collection_name]["profiles_accessed"] += profile_count
            self.analytics_data["collection_access"][collection_name]["last_accessed"] = datetime.now().isoformat()

            self._save_analytics()

        except Exception as e:
            log_error("Failed to track collection access", exception=e)

    def _track_goal_based_selection(self, goal: str, genre: str, profile_id: str) -> None:
        """Track goal-based profile selection for analytics."""
        try:
            if "goal_selections" not in self.analytics_data:
                self.analytics_data["goal_selections"] = {}

            key = f"{goal}_{genre}" if genre else goal
            if key not in self.analytics_data["goal_selections"]:
                self.analytics_data["goal_selections"][key] = {
                    "count": 0,
                    "profiles_used": {},
                    "last_used": None
                }

            self.analytics_data["goal_selections"][key]["count"] += 1
            self.analytics_data["goal_selections"][key]["last_used"] = datetime.now().isoformat()

            if profile_id not in self.analytics_data["goal_selections"][key]["profiles_used"]:
                self.analytics_data["goal_selections"][key]["profiles_used"][profile_id] = 0
            self.analytics_data["goal_selections"][key]["profiles_used"][profile_id] += 1

            self._save_analytics()

        except Exception as e:
            log_error("Failed to track goal-based selection", exception=e)

    def _track_genre_collection_search(self, genre: str, result_count: int) -> None:
        """Track genre-based collection searches for analytics."""
        try:
            if "genre_collection_searches" not in self.analytics_data:
                self.analytics_data["genre_collection_searches"] = {}

            if genre not in self.analytics_data["genre_collection_searches"]:
                self.analytics_data["genre_collection_searches"][genre] = {
                    "search_count": 0,
                    "total_results": 0,
                    "last_searched": None
                }

            self.analytics_data["genre_collection_searches"][genre]["search_count"] += 1
            self.analytics_data["genre_collection_searches"][genre]["total_results"] += result_count
            self.analytics_data["genre_collection_searches"][genre]["last_searched"] = datetime.now().isoformat()

            self._save_analytics()

        except Exception as e:
            log_error("Failed to track genre collection search", exception=e)

    def get_analytics_summary(self) -> Dict[str, Any]:
        """
        Get a comprehensive analytics summary.

        Returns:
            Dictionary containing analytics data
        """
        try:
            # Calculate most used profiles
            profile_usage_sorted = sorted(
                self.analytics_data["profile_usage"].items(),
                key=lambda x: x[1]["total_uses"],
                reverse=True
            )

            # Calculate genre popularity
            genre_popularity = {}
            for genre, data in self.analytics_data["genre_preferences"].items():
                total_selections = sum(data["profiles_selected"].values())
                genre_popularity[genre] = {
                    "total_selections": total_selections,
                    "recommendation_requests": data["recommendation_requests"],
                    "unique_profiles_used": len(data["profiles_selected"])
                }

            # Calculate profile effectiveness
            profile_effectiveness = {}
            for profile_id, usage_data in self.analytics_data["profile_usage"].items():
                profile = self.load_profile(profile_id)
                if profile:
                    profile_effectiveness[profile_id] = {
                        "name": profile.get("name", "Unknown"),
                        "total_uses": usage_data["total_uses"],
                        "genres_count": len(usage_data["genres_used"]),
                        "primary_genre": max(usage_data["genres_used"].items(), key=lambda x: x[1])[0] if usage_data["genres_used"] else "Unknown",
                        "selection_methods": usage_data["selection_methods"]
                    }

            return {
                "summary": {
                    "total_profiles": len(self.analytics_data["profile_usage"]),
                    "total_uses": sum(data["total_uses"] for data in self.analytics_data["profile_usage"].values()),
                    "active_genres": len(self.analytics_data["genre_preferences"]),
                    "last_updated": self.analytics_data["last_updated"]
                },
                "most_used_profiles": profile_usage_sorted[:10],
                "genre_popularity": dict(sorted(genre_popularity.items(), key=lambda x: x[1]["total_selections"], reverse=True)),
                "profile_effectiveness": profile_effectiveness,
                "creation_stats": self.analytics_data["creation_stats"]
            }

        except Exception as e:
            log_error("Failed to generate analytics summary", exception=e)
            return {}

    def record_user_satisfaction(self, profile_id: str, rating: int, feedback: str = "") -> None:
        """
        Record user satisfaction with a profile.

        Args:
            profile_id: ID of the profile
            rating: Rating from 1-5
            feedback: Optional feedback text
        """
        try:
            if "user_satisfaction" not in self.analytics_data["performance_metrics"]:
                self.analytics_data["performance_metrics"]["user_satisfaction"] = {}

            if profile_id not in self.analytics_data["performance_metrics"]["user_satisfaction"]:
                self.analytics_data["performance_metrics"]["user_satisfaction"][profile_id] = {
                    "ratings": [],
                    "feedback": [],
                    "average_rating": 0
                }

            satisfaction_data = self.analytics_data["performance_metrics"]["user_satisfaction"][profile_id]
            satisfaction_data["ratings"].append({
                "rating": rating,
                "timestamp": datetime.now().isoformat()
            })

            if feedback:
                satisfaction_data["feedback"].append({
                    "feedback": feedback,
                    "timestamp": datetime.now().isoformat()
                })

            # Calculate average rating
            ratings = [r["rating"] for r in satisfaction_data["ratings"]]
            satisfaction_data["average_rating"] = sum(ratings) / len(ratings)

            self._save_analytics()

        except Exception as e:
            log_error("Failed to record user satisfaction", exception=e)

    def get_auto_selected_profile_for_book(self, genre: str, themes: List[str] = None,
                                         writing_style: str = None, target_length: str = None) -> Optional[Dict[str, Any]]:
        """
        Automatically select and enhance the best fictional author profile for a book.

        This method:
        1. Automatically selects the most appropriate fictional author based on genre
        2. Optionally enhances the profile using Gemini AI based on book requirements
        3. Returns the enhanced profile ready for book generation

        Args:
            genre: The book genre
            themes: Optional list of themes for profile enhancement
            writing_style: Optional writing style for profile enhancement
            target_length: Optional target length for profile enhancement

        Returns:
            Enhanced fictional author profile or None if no suitable profile found
        """
        try:
            # Step 1: Automatically select the best fictional author for the genre
            base_profile = self.get_default_profile_for_genre(genre)

            if not base_profile:
                console.print(f"[yellow]No default fictional author found for {genre}, using fallback selection[/yellow]")
                # Fallback: get any compatible profile
                recommendations = self.get_recommended_profiles(genre)
                if recommendations:
                    base_profile = recommendations[0]
                else:
                    console.print(f"[red]No fictional authors available for {genre}[/red]")
                    return None

            # Step 2: Enhance the profile if specific requirements are provided
            if themes or writing_style or target_length:
                enhanced_profile = self._enhance_profile_with_ai(
                    base_profile, genre, themes, writing_style, target_length
                )
                if enhanced_profile:
                    return enhanced_profile

            # Step 3: Return the base profile if no enhancement needed or enhancement failed
            return base_profile

        except Exception as e:
            console.print(f"[red]Error in auto-selecting profile for book: {e}[/red]")
            return None

    def _enhance_profile_with_ai(self, base_profile: Dict[str, Any], genre: str,
                               themes: List[str] = None, writing_style: str = None,
                               target_length: str = None) -> Optional[Dict[str, Any]]:
        """
        Enhance a fictional author profile using Gemini AI based on specific book requirements.

        Args:
            base_profile: The base fictional author profile
            genre: The book genre
            themes: Optional themes to incorporate
            writing_style: Optional writing style preferences
            target_length: Optional target length

        Returns:
            Enhanced profile or None if enhancement fails
        """
        try:
            from src.core.gemini_client import GeminiClient

            # Create enhancement prompt
            author_name = base_profile.get("name", "Unknown Author")
            base_style = base_profile.get("profile_data", {}).get("writing_style", "")
            base_themes = base_profile.get("profile_data", {}).get("thematic_focuses", [])

            enhancement_prompt = f"""
            Enhance the fictional author profile for "{author_name}" to better suit a specific {genre} book with these requirements:

            Base Profile:
            - Author: {author_name} (fictional)
            - Current Style: {base_style[:200]}...
            - Current Themes: {', '.join(base_themes[:3]) if isinstance(base_themes, list) else str(base_themes)[:200]}

            Book Requirements:
            - Genre: {genre}
            - Themes: {', '.join(themes) if themes else 'Not specified'}
            - Writing Style: {writing_style or 'Not specified'}
            - Target Length: {target_length or 'Not specified'}

            Please provide enhanced characteristics for this fictional author that would be optimal for this specific book:

            1. Enhanced Writing Style (2-3 sentences adapting the base style for these requirements)
            2. Thematic Focus Adjustments (3-4 themes that blend the author's strengths with the book requirements)
            3. Narrative Technique Recommendations (1-2 sentences on optimal techniques for this book)
            4. Tone and Voice Adjustments (1-2 sentences on how to adapt the author's voice)

            Keep the response concise and focused on practical enhancements that maintain the fictional author's core identity while optimizing for the specific book requirements.
            """

            # Generate enhancement using Gemini
            gemini = GeminiClient()
            enhancement_response = gemini.generate_content(enhancement_prompt, temperature=0.7, max_tokens=800)

            if not enhancement_response:
                console.print(f"[yellow]AI enhancement failed for {author_name}, using base profile[/yellow]")
                return base_profile

            # Create enhanced profile by updating specific fields
            enhanced_profile = base_profile.copy()

            # Add enhancement metadata
            enhanced_profile["_enhancement"] = {
                "enhanced_for_genre": genre,
                "enhanced_for_themes": themes,
                "enhanced_for_style": writing_style,
                "enhanced_for_length": target_length,
                "enhancement_text": enhancement_response,
                "enhanced_at": "runtime"
            }

            # Parse and apply enhancements to profile_data
            if "profile_data" in enhanced_profile:
                profile_data = enhanced_profile["profile_data"].copy()

                # Add enhancement note to writing style
                if "writing_style" in profile_data:
                    profile_data["writing_style"] += f"\n\nEnhanced for this {genre} book: {enhancement_response[:200]}..."

                enhanced_profile["profile_data"] = profile_data

            console.print(f"[green]Enhanced {author_name} profile for {genre} book[/green]")
            return enhanced_profile

        except Exception as e:
            console.print(f"[yellow]Profile enhancement failed: {e}. Using base profile.[/yellow]")
            return base_profile

    def get_auto_selected_profile_for_series(self, genre: str, series_themes: List[str] = None,
                                           book_count: int = 1) -> Optional[Dict[str, Any]]:
        """
        Automatically select and enhance the best fictional author profile for a series.

        Args:
            genre: The series genre
            series_themes: Optional list of overarching series themes
            book_count: Number of books in the series

        Returns:
            Enhanced fictional author profile optimized for series writing
        """
        try:
            # Get base profile for the genre
            base_profile = self.get_default_profile_for_genre(genre)

            if not base_profile:
                # Fallback selection
                recommendations = self.get_recommended_profiles(genre)
                if recommendations:
                    base_profile = recommendations[0]
                else:
                    return None

            # Enhance for series writing if themes provided
            if series_themes or book_count > 1:
                enhanced_profile = self._enhance_profile_for_series(
                    base_profile, genre, series_themes, book_count
                )
                if enhanced_profile:
                    return enhanced_profile

            return base_profile

        except Exception as e:
            console.print(f"[red]Error in auto-selecting profile for series: {e}[/red]")
            return None

    def _enhance_profile_for_series(self, base_profile: Dict[str, Any], genre: str,
                                  series_themes: List[str] = None, book_count: int = 1) -> Optional[Dict[str, Any]]:
        """
        Enhance a fictional author profile for series writing.

        Args:
            base_profile: The base fictional author profile
            genre: The series genre
            series_themes: Optional overarching series themes
            book_count: Number of books in the series

        Returns:
            Enhanced profile optimized for series writing
        """
        try:
            from src.core.gemini_client import GeminiClient

            author_name = base_profile.get("name", "Unknown Author")

            series_prompt = f"""
            Enhance the fictional author profile for "{author_name}" for writing a {book_count}-book {genre} series:

            Series Requirements:
            - Genre: {genre}
            - Number of Books: {book_count}
            - Series Themes: {', '.join(series_themes) if series_themes else 'Not specified'}

            Provide series-specific enhancements:
            1. Series Continuity Approach (how to maintain consistency across books)
            2. Character Development Arc (how to develop characters across multiple books)
            3. World-Building Strategy (how to expand the world across the series)
            4. Thematic Thread Management (how to weave themes throughout the series)

            Keep response concise and focused on series-specific writing techniques.
            """

            gemini = GeminiClient()
            enhancement_response = gemini.generate_content(series_prompt, temperature=0.7, max_tokens=600)

            if not enhancement_response:
                return base_profile

            # Create enhanced profile for series
            enhanced_profile = base_profile.copy()
            enhanced_profile["_series_enhancement"] = {
                "enhanced_for_series": True,
                "series_genre": genre,
                "series_themes": series_themes,
                "book_count": book_count,
                "series_enhancement_text": enhancement_response,
                "enhanced_at": "runtime"
            }

            console.print(f"[green]Enhanced {author_name} profile for {book_count}-book {genre} series[/green]")
            return enhanced_profile

        except Exception as e:
            console.print(f"[yellow]Series enhancement failed: {e}. Using base profile.[/yellow]")
            return base_profile
