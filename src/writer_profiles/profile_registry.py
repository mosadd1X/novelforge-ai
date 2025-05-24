"""
Writer Profile Registry - Central Management System

This module serves as the central registry for all master writer profiles,
providing genre mapping, profile discovery, and compatibility checking.

The new system features 20 master writer profiles based on real authors,
each specializing in 2-4 genres to ensure complete coverage of all 38 genres.
"""

from typing import Dict, List, Any, Optional
from pathlib import Path
from dataclasses import dataclass

@dataclass
class AuthorProfile:
    """Data class representing an author profile."""
    name: str
    module_name: str
    primary_genres: List[str]
    secondary_genres: List[str]
    cultural_background: str
    era: str
    tags: List[str]

class WriterProfileRegistry:
    """Central registry for all master writer profiles."""

    def __init__(self):
        """Initialize the profile registry."""
        self.profiles_dir = Path("src/writer_profiles/master_profiles")
        self._author_profiles = self._initialize_author_profiles()
        self._genre_mappings = self._build_genre_mappings()

    def _initialize_author_profiles(self) -> Dict[str, AuthorProfile]:
        """Initialize the 20 fictional master author profiles."""
        return {
            "elena_thornfield": AuthorProfile(
                name="Elena Thornfield",
                module_name="elena_thornfield",
                primary_genres=["Literary Fiction", "Memoir"],
                secondary_genres=["Essay Collection", "Creative Non-Fiction"],
                cultural_background="British",
                era="Modernist",
                tags=["stream_of_consciousness", "psychological_realism", "experimental", "feminist"]
            ),
            "marcus_steele": AuthorProfile(
                name="Marcus Steele",
                module_name="marcus_steele",
                primary_genres=["Literary Fiction", "Historical Fiction"],
                secondary_genres=["Short Story Collection", "War Literature"],
                cultural_background="American",
                era="Modern",
                tags=["minimalist", "iceberg_theory", "understated", "masculine"]
            ),
            "rajesh_malhotra": AuthorProfile(
                name="Rajesh Malhotra",
                module_name="rajesh_malhotra",
                primary_genres=["Literary Fiction", "Short Story Collection"],
                secondary_genres=["Contemporary Fiction", "Humor"],
                cultural_background="Indian",
                era="Modern",
                tags=["gentle_humor", "everyday_life", "regional_fiction", "universal_themes"]
            ),
            "victoria_blackwood": AuthorProfile(
                name="Victoria Blackwood",
                module_name="victoria_blackwood",
                primary_genres=["Mystery", "Mystery/Thriller"],
                secondary_genres=["Novella", "Crime Fiction"],
                cultural_background="British",
                era="Golden Age",
                tags=["puzzle_plots", "fair_play", "ingenious_mysteries", "logical_deduction"]
            ),
            "dr_samuel_voss": AuthorProfile(
                name="Dr. Samuel Voss",
                module_name="dr_samuel_voss",
                primary_genres=["Science Fiction", "Popular Science"],
                secondary_genres=["Academic", "Short Story Collection"],
                cultural_background="Russian-American",
                era="Golden Age",
                tags=["hard_sf", "scientific", "educational", "galactic_scope"]
            ),
            "priya_sharma": AuthorProfile(
                name="Priya Sharma",
                module_name="priya_sharma",
                primary_genres=["Romance", "Contemporary Romance"],
                secondary_genres=["Literary Fiction", "Contemporary Fiction"],
                cultural_background="Indian",
                era="Contemporary",
                tags=["romance", "cultural_authenticity", "indian_romance", "contemporary"]
            ),
            "arjun_krishnamurthy": AuthorProfile(
                name="Arjun Krishnamurthy",
                module_name="arjun_krishnamurthy",
                primary_genres=["Literary Fiction", "Historical Fiction"],
                secondary_genres=["Social Commentary", "Political Fiction"],
                cultural_background="Indian",
                era="Modern",
                tags=["social_realism", "progressive", "humanist", "class_consciousness"]
            ),
            "kavya_nair": AuthorProfile(
                name="Kavya Nair",
                module_name="kavya_nair",
                primary_genres=["Memoir", "Poetry Collection"],
                secondary_genres=["Creative Non-Fiction", "Autobiography"],
                cultural_background="Indian",
                era="Contemporary",
                tags=["confessional", "feminist", "intimate", "bold"]
            ),
            "ananya_desai": AuthorProfile(
                name="Ananya Desai",
                module_name="ananya_desai",
                primary_genres=["Literary Fiction", "Contemporary Fiction"],
                secondary_genres=["Creative Non-Fiction", "Environmental Literature"],
                cultural_background="Indian",
                era="Contemporary",
                tags=["lyrical", "environmental", "political", "sensuous"]
            ),
            "vikram_chandra": AuthorProfile(
                name="Vikram Chandra",
                module_name="vikram_chandra",
                primary_genres=["Literary Fiction", "Poetry Collection"],
                secondary_genres=["Historical Fiction", "Epic Fiction"],
                cultural_background="Indian",
                era="Contemporary",
                tags=["versatile", "epic_scope", "detailed", "classical"]
            ),
            "rohan_mehta": AuthorProfile(
                name="Rohan Mehta",
                module_name="rohan_mehta",
                primary_genres=["Contemporary Fiction", "Commercial Fiction"],
                secondary_genres=["Young Adult", "Romance"],
                cultural_background="Indian",
                era="Contemporary",
                tags=["accessible", "youth_culture", "contemporary_issues", "popular"]
            ),
            "devika_ghosh": AuthorProfile(
                name="Devika Ghosh",
                module_name="devika_ghosh",
                primary_genres=["Historical Fiction", "Literary Fiction"],
                secondary_genres=["Travel", "Cultural Studies"],
                cultural_background="Indian",
                era="Contemporary",
                tags=["historical", "colonial", "migration", "scholarly"]
            ),
            "sebastian_darkmore": AuthorProfile(
                name="Sebastian Darkmore",
                module_name="sebastian_darkmore",
                primary_genres=["Horror", "Thriller"],
                secondary_genres=["Supernatural Fiction", "Contemporary Fiction"],
                cultural_background="American",
                era="Contemporary",
                tags=["supernatural", "psychological_horror", "prolific", "accessible"]
            ),
            "professor_aldrich_quantum": AuthorProfile(
                name="Professor Aldrich Quantum",
                module_name="professor_aldrich_quantum",
                primary_genres=["Fantasy", "Epic Fantasy"],
                secondary_genres=["Middle Grade", "Mythology"],
                cultural_background="British",
                era="Modern",
                tags=["high_fantasy", "world_building", "linguistic", "mythological"]
            ),
            "catherine_fairfax": AuthorProfile(
                name="Catherine Fairfax",
                module_name="catherine_fairfax",
                primary_genres=["Romance", "Historical Fiction"],
                secondary_genres=["Commercial Fiction", "Social Commentary"],
                cultural_background="British",
                era="Regency",
                tags=["wit", "social_commentary", "irony", "marriage_plots"]
            ),
            "gabriel_montoya": AuthorProfile(
                name="Gabriel Montoya",
                module_name="gabriel_montoya",
                primary_genres=["Literary Fiction", "Speculative Fiction"],
                secondary_genres=["Short Story Collection", "Magical Realism"],
                cultural_background="Colombian",
                era="Contemporary",
                tags=["magical_realism", "latin_american", "political", "lyrical"]
            ),
            "hiroshi_nakamura": AuthorProfile(
                name="Hiroshi Nakamura",
                module_name="hiroshi_nakamura",
                primary_genres=["Contemporary Fiction", "Speculative Fiction"],
                secondary_genres=["Urban Fantasy", "Surreal Fiction"],
                cultural_background="Japanese",
                era="Contemporary",
                tags=["surreal", "pop_culture", "alienation", "dreamlike"]
            ),
            "grace_washington": AuthorProfile(
                name="Grace Washington",
                module_name="grace_washington",
                primary_genres=["Memoir", "Biography"],
                secondary_genres=["Poetry Collection", "Inspirational"],
                cultural_background="African American",
                era="Contemporary",
                tags=["autobiographical", "resilience", "lyrical", "empowering"]
            ),
            "dr_malcolm_sterling": AuthorProfile(
                name="Dr. Malcolm Sterling",
                module_name="dr_malcolm_sterling",
                primary_genres=["Popular Science", "Business"],
                secondary_genres=["Self-Help", "Psychology"],
                cultural_background="Canadian",
                era="Contemporary",
                tags=["analytical", "accessible", "research_based", "storytelling"]
            ),
            "anthony_rivers": AuthorProfile(
                name="Anthony Rivers",
                module_name="anthony_rivers",
                primary_genres=["Travel", "Memoir"],
                secondary_genres=["Cookbook", "Cultural Commentary"],
                cultural_background="American",
                era="Contemporary",
                tags=["culinary", "travel", "irreverent", "authentic"]
            ),
            "dr_patricia_blackwell": AuthorProfile(
                name="Dr. Patricia Blackwell",
                module_name="dr_patricia_blackwell",
                primary_genres=["Business", "Self-Help"],
                secondary_genres=["How-To", "Philosophy"],
                cultural_background="American",
                era="Contemporary",
                tags=["analytical", "practical", "accessible", "research_based"]
            ),
            "luna_brightwater": AuthorProfile(
                name="Luna Brightwater",
                module_name="luna_brightwater",
                primary_genres=["Children's Chapter Books", "Middle Grade"],
                secondary_genres=["Graphic Novel", "Young Adult"],
                cultural_background="British",
                era="Contemporary",
                tags=["whimsical", "imaginative", "age_appropriate", "engaging"]
            ),
            "professor_elena_vasquez": AuthorProfile(
                name="Professor Elena Vasquez",
                module_name="professor_elena_vasquez",
                primary_genres=["Academic", "Essay Collection"],
                secondary_genres=["Philosophy", "History"],
                cultural_background="Spanish",
                era="Contemporary",
                tags=["scholarly", "analytical", "thoughtful", "rigorous"]
            ),
            "detective_marcus_kane": AuthorProfile(
                name="Detective Marcus Kane",
                module_name="detective_marcus_kane",
                primary_genres=["True Crime", "Mystery/Thriller"],
                secondary_genres=["Thriller", "Crime Fiction"],
                cultural_background="American",
                era="Contemporary",
                tags=["investigative", "detailed", "procedural", "authentic"]
            ),
            "dr_sophia_chronos": AuthorProfile(
                name="Dr. Sophia Chronos",
                module_name="dr_sophia_chronos",
                primary_genres=["History", "Alternate History"],
                secondary_genres=["Academic", "Historical Fiction"],
                cultural_background="Greek-American",
                era="Contemporary",
                tags=["scholarly", "narrative", "detailed", "engaging"]
            ),
            "raven_nightshade": AuthorProfile(
                name="Raven Nightshade",
                module_name="raven_nightshade",
                primary_genres=["Paranormal Romance", "Urban Fantasy"],
                secondary_genres=["Fantasy", "Romance"],
                cultural_background="American",
                era="Contemporary",
                tags=["supernatural", "romantic", "atmospheric", "sensual"]
            ),
            "zara_blackthorn": AuthorProfile(
                name="Zara Blackthorn",
                module_name="zara_blackthorn",
                primary_genres=["Dystopian", "Speculative Fiction"],
                secondary_genres=["Science Fiction", "Young Adult"],
                cultural_background="Canadian",
                era="Contemporary",
                tags=["dystopian", "social_commentary", "thought_provoking", "atmospheric"]
            )
        }

    def _build_genre_mappings(self) -> Dict[str, List[str]]:
        """Build mappings from genres to available author profiles."""
        mappings = {}

        for profile_id, profile in self._author_profiles.items():
            # Add primary genres
            for genre in profile.primary_genres:
                if genre not in mappings:
                    mappings[genre] = []
                mappings[genre].append(profile_id)

            # Add secondary genres
            for genre in profile.secondary_genres:
                if genre not in mappings:
                    mappings[genre] = []
                if profile_id not in mappings[genre]:
                    mappings[genre].append(profile_id)

        return mappings

    def get_profiles_for_genre(self, genre: str) -> List[AuthorProfile]:
        """Get all author profiles that can handle a specific genre."""
        profile_ids = self._genre_mappings.get(genre, [])
        return [self._author_profiles[pid] for pid in profile_ids]

    def get_profile_by_name(self, author_name: str) -> Optional[AuthorProfile]:
        """Get a profile by author name."""
        for profile in self._author_profiles.values():
            if profile.name.lower() == author_name.lower():
                return profile
        return None

    def get_all_profiles(self) -> List[AuthorProfile]:
        """Get all available author profiles."""
        return list(self._author_profiles.values())

    def get_coverage_report(self) -> Dict[str, Any]:
        """Generate a coverage report showing genre coverage."""
        from src.utils.genre_defaults import get_all_genres

        all_genres = [g.lower() for g in get_all_genres()]
        covered_genres = set()
        uncovered_genres = []

        for genre in all_genres:
            profiles = self.get_profiles_for_genre(genre)
            if profiles:
                covered_genres.add(genre)
            else:
                uncovered_genres.append(genre)

        return {
            "total_genres": len(all_genres),
            "covered_genres": len(covered_genres),
            "uncovered_genres": uncovered_genres,
            "coverage_percentage": (len(covered_genres) / len(all_genres)) * 100,
            "genre_mappings": self._genre_mappings
        }

# Global registry instance
registry = WriterProfileRegistry()
