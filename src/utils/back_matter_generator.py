"""
Back Matter Generator for AI-Generated Books

This module generates appropriate back matter sections for AI-generated books,
including writer profile information, series details, and AI generation insights.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from src.utils.genre_defaults import get_genre_defaults, get_all_genres
from src.utils.writer_profile_manager import WriterProfileManager


class BackMatterGenerator:
    """
    Generates back matter content for AI-generated books.
    """

    def __init__(
        self,
        novel_data: Dict[str, Any],
        writer_profile: Dict[str, Any] = None,
        profile_manager: WriterProfileManager = None
    ):
        """
        Initialize the back matter generator.

        Args:
            novel_data: Complete novel data including metadata
            writer_profile: Writer profile information (optional)
            profile_manager: Writer profile manager for accessing profile library
        """
        self.novel_data = novel_data
        self.writer_profile = writer_profile or {}
        self.profile_manager = profile_manager
        self.metadata = novel_data.get("metadata", {})
        self.genre = self.metadata.get("genre", "Fiction")
        self.genre_defaults = get_genre_defaults(self.genre)

    def generate_writer_profile_section(self) -> str:
        """
        Generate "About This Writer Profile" section.

        Returns:
            HTML content for the writer profile section
        """
        if not self.writer_profile:
            return self._generate_generic_profile_section()

        profile_data = self.writer_profile.get("profile_data", {})
        profile_name = self.writer_profile.get("name", "Custom AI Writer Profile")

        # Extract profile information
        writing_style = profile_data.get("writing_style", "Engaging and descriptive")
        influences = profile_data.get("literary_influences", "Various classic and contemporary authors")
        themes = profile_data.get("thematic_focuses", "Human experience and storytelling")
        techniques = profile_data.get("narrative_techniques", "Character-driven narratives")
        strengths = profile_data.get("strengths", "Creating compelling stories")

        # Get books generated with this profile
        books_info = ""
        if self.profile_manager and "id" in self.writer_profile:
            profile_books = self.profile_manager.get_profile_books(self.writer_profile["id"])
            if len(profile_books) > 1:  # More than just this book
                other_books = [book for book in profile_books
                             if book.get("title") != self.metadata.get("title")]
                if other_books:
                    book_list = ", ".join([f'"{book["title"]}"' for book in other_books[:5]])
                    if len(other_books) > 5:
                        book_list += f" and {len(other_books) - 5} others"

                    books_info = f"""
                    <h2>Other Works by This Profile</h2>
                    <p>This AI writer profile has also generated: {book_list}.</p>
                    """

        # Get additional profile metadata
        cultural_background = self.writer_profile.get("cultural_background", "")
        era = self.writer_profile.get("era", "")
        tags = self.writer_profile.get("tags", [])

        # Create cultural context
        cultural_context = ""
        if cultural_background and era:
            cultural_context = f"""
            <p><strong>Cultural Background:</strong> {cultural_background}</p>
            <p><strong>Literary Era:</strong> {era}</p>
            """

        # Create style tags
        style_tags = ""
        if tags:
            tag_list = ", ".join(tags[:6])  # Show first 6 tags
            style_tags = f"""
            <p><strong>Style Tags:</strong> {tag_list}</p>
            """

        return f"""
        <div class="writer-profile">
            <h1>About This Fictional Writer Profile</h1>

            <p>This book was generated using the <strong>"{profile_name}"</strong> fictional author profile,
            a specialized AI persona inspired by literary masters but representing an entirely original
            fictional identity created specifically for AI-generated {self.genre.lower()} literature.</p>

            <div class="fictional-author-notice">
                <p><em><strong>Important Note:</strong> {profile_name} is a fictional author persona.
                This profile draws inspiration from real literary techniques and styles but represents
                a completely original fictional identity. All books attributed to this name are
                AI-generated works.</em></p>
            </div>

            <h2>Profile Characteristics</h2>
            <p><strong>Writing Style:</strong> {writing_style}</p>
            <p><strong>Literary Influences:</strong> {influences}</p>
            <p><strong>Thematic Focus:</strong> {themes}</p>
            <p><strong>Narrative Techniques:</strong> {techniques}</p>
            <p><strong>Key Strengths:</strong> {strengths}</p>
            {cultural_context}
            {style_tags}

            {books_info}

            <h2>About Fictional AI Writer Profiles</h2>
            <p>Fictional AI writer profiles are persistent creative personas that maintain consistent
            voice, style, and thematic approaches across multiple AI-generated works. Each profile
            represents a unique fictional author identity inspired by real literary masters, allowing
            for the development of recognizable authorial characteristics while ensuring that
            AI-generated content is properly attributed to fictional rather than real authors.</p>

            <p>These profiles enable the creation of sophisticated literature while maintaining
            transparency about the AI-generated nature of the content and respecting the legacy
            of real literary figures.</p>
        </div>
        """

    def _generate_generic_profile_section(self) -> str:
        """Generate generic profile section when no specific profile is available."""
        return f"""
        <div class="writer-profile">
            <h1>About This AI Generation</h1>

            <p>This {self.genre.lower()} novel was created using artificial intelligence
            technology specifically trained for creative writing. The AI system analyzed
            extensive literary datasets to understand genre conventions, narrative structures,
            and character development techniques.</p>

            <h2>Generation Approach</h2>
            <p>The AI focused on creating authentic {self.genre.lower()} elements including:</p>
            <ul>
                <li>Genre-appropriate themes and motifs</li>
                <li>Compelling character arcs and development</li>
                <li>Engaging plot structure and pacing</li>
                <li>Authentic dialogue and narrative voice</li>
                <li>Rich descriptive language and atmosphere</li>
            </ul>

            <p>This represents the cutting edge of AI-assisted creative writing, where
            technology serves to enhance and expand the possibilities of storytelling.</p>
        </div>
        """

    def generate_series_information(self) -> Optional[str]:
        """
        Generate series information section if applicable.

        Returns:
            HTML content for series information or None
        """
        if "series" not in self.metadata or not self.metadata["series"].get("is_part_of_series"):
            return None

        series_data = self.metadata["series"]
        series_title = series_data.get("series_title", "Unknown Series")
        book_number = series_data.get("book_number", 1)
        total_books = series_data.get("planned_books", "multiple")

        # Generate reading order information
        reading_order = ""
        if book_number > 1:
            reading_order = f"""
            <h2>Reading Order</h2>
            <p>This is Book {book_number} in the {series_title} series. While each book
            tells a complete story, reading the series in order will provide the best
            experience for understanding character development and overarching plot threads.</p>
            """

        # Future books information
        future_info = ""
        if isinstance(total_books, int) and book_number < total_books:
            remaining = total_books - book_number
            future_info = f"""
            <h2>Upcoming in This Series</h2>
            <p>The {series_title} series will continue with {remaining} more book{'s' if remaining != 1 else ''},
            further developing the characters and world you've encountered in this volume.</p>
            """

        return f"""
        <div class="series-information">
            <h1>About the {series_title} Series</h1>

            <p>This book is part of the {series_title} series, an AI-generated collection
            of interconnected {self.genre.lower()} novels. The series maintains consistent
            characters, world-building, and thematic elements while telling unique stories
            in each volume.</p>

            {reading_order}

            <h2>Series Features</h2>
            <ul>
                <li>Consistent character development across books</li>
                <li>Interconnected plot threads and story arcs</li>
                <li>Evolving world-building and mythology</li>
                <li>Thematic continuity with fresh perspectives</li>
                <li>Each book tells a complete, satisfying story</li>
            </ul>

            {future_info}

            <p>The AI generation process for this series involved creating detailed
            continuity tracking, character development arcs, and overarching narrative
            threads to ensure a cohesive and engaging multi-book experience.</p>
        </div>
        """

    def generate_genre_recommendations(self) -> str:
        """
        Generate reading recommendations for the genre.

        Returns:
            HTML content for genre recommendations
        """
        # Get related genres
        all_genres = get_all_genres()
        related_genres = self._get_related_genres(self.genre, all_genres)

        # Genre-specific recommendations
        genre_lower = self.genre.lower()

        if "fantasy" in genre_lower:
            classic_recs = "J.R.R. Tolkien's Middle-earth works, Ursula K. Le Guin's Earthsea series"
            modern_recs = "Brandon Sanderson's Cosmere universe, N.K. Jemisin's Broken Earth trilogy"
        elif "science fiction" in genre_lower or "sci-fi" in genre_lower:
            classic_recs = "Isaac Asimov's Foundation series, Philip K. Dick's works"
            modern_recs = "Liu Cixin's Three-Body trilogy, Becky Chambers' Wayfarers series"
        elif "mystery" in genre_lower or "thriller" in genre_lower:
            classic_recs = "Agatha Christie's Hercule Poirot series, Raymond Chandler's works"
            modern_recs = "Tana French's Dublin Murder Squad, Gillian Flynn's psychological thrillers"
        elif "romance" in genre_lower:
            classic_recs = "Jane Austen's novels, Charlotte Brontë's works"
            modern_recs = "Julia Quinn's Bridgerton series, Sarah J. Maas's fantasy romance"
        else:
            classic_recs = "Classic works that defined the genre"
            modern_recs = "Contemporary authors pushing genre boundaries"

        related_list = ", ".join(related_genres[:4]) if related_genres else "various genres"

        return f"""
        <div class="genre-recommendations">
            <h1>If You Enjoyed This {self.genre}</h1>

            <p>If you enjoyed this AI-generated {self.genre.lower()} novel, you might also
            appreciate these recommendations from the genre and related areas:</p>

            <h2>Classic {self.genre} Works</h2>
            <p>{classic_recs}</p>

            <h2>Modern {self.genre} Authors</h2>
            <p>{modern_recs}</p>

            <h2>Related Genres to Explore</h2>
            <p>Readers of {self.genre.lower()} often enjoy: {related_list}</p>

            <h2>More AI-Generated Content</h2>
            <p>This AI generation system can create compelling stories across all these
            genres, offering fresh perspectives and unique takes on beloved literary traditions.
            Each AI-generated work brings together the best elements of the genre while
            exploring new creative possibilities.</p>
        </div>
        """

    def _get_related_genres(self, current_genre: str, all_genres: List[str]) -> List[str]:
        """
        Get genres related to the current genre.

        Args:
            current_genre: The current book's genre
            all_genres: List of all available genres

        Returns:
            List of related genre names
        """
        genre_lower = current_genre.lower()
        related = []

        # Define genre relationships
        relationships = {
            "fantasy": ["science fiction", "adventure", "epic", "mythology"],
            "science fiction": ["fantasy", "dystopian", "thriller", "adventure"],
            "mystery": ["thriller", "crime", "detective", "suspense"],
            "thriller": ["mystery", "suspense", "crime", "psychological"],
            "romance": ["contemporary", "historical", "fantasy", "paranormal"],
            "historical": ["biography", "literary fiction", "romance", "adventure"],
            "literary fiction": ["contemporary", "historical", "drama", "philosophical"],
            "horror": ["thriller", "supernatural", "gothic", "psychological"],
            "adventure": ["fantasy", "science fiction", "action", "thriller"],
            "young adult": ["fantasy", "romance", "contemporary", "dystopian"]
        }

        # Find related genres
        for genre_key, related_keywords in relationships.items():
            if genre_key in genre_lower:
                for keyword in related_keywords:
                    for genre in all_genres:
                        if keyword in genre.lower() and genre.lower() != current_genre.lower():
                            if genre not in related:
                                related.append(genre)

        return related[:6]  # Return top 6 related genres

    def generate_technical_details(self) -> str:
        """
        Generate technical details about the generation process.

        Returns:
            HTML content for technical details
        """
        generation_date = datetime.now().strftime("%B %d, %Y")

        # Extract technical parameters
        word_count = self.genre_defaults.get("target_word_count", "Unknown")
        chapter_count = self.genre_defaults.get("chapter_count", "Multiple")
        writing_style = self.genre_defaults.get("writing_style", "Descriptive")
        themes = self.genre_defaults.get("themes", [])

        theme_list = ", ".join(themes[:5]) if themes else "Various themes"

        return f"""
        <div class="technical-details">
            <h1>Generation Details</h1>

            <p>For readers interested in the technical aspects of this AI-generated work:</p>

            <h2>Generation Parameters</h2>
            <ul>
                <li><strong>Target Word Count:</strong> {word_count:,} words</li>
                <li><strong>Chapter Structure:</strong> {chapter_count} chapters</li>
                <li><strong>Writing Style:</strong> {writing_style}</li>
                <li><strong>Primary Themes:</strong> {theme_list}</li>
                <li><strong>Generation Date:</strong> {generation_date}</li>
            </ul>

            <h2>AI Technology</h2>
            <p>This book was created using advanced language models trained on extensive
            literary datasets. The AI system employs sophisticated techniques for:</p>
            <ul>
                <li>Narrative structure and pacing</li>
                <li>Character development and consistency</li>
                <li>Dialogue generation and voice</li>
                <li>Thematic development</li>
                <li>Genre-specific conventions</li>
            </ul>

            <h2>Quality Assurance</h2>
            <p>The generation process includes multiple phases of enhancement and refinement
            to ensure narrative coherence, character consistency, and engaging prose quality.</p>

            <p>This represents the current state of AI creative writing technology,
            demonstrating the potential for artificial intelligence to create meaningful,
            entertaining, and emotionally resonant literature.</p>
        </div>
        """

    def get_all_back_matter(self) -> Dict[str, str]:
        """
        Generate all back matter sections.

        Returns:
            Dictionary with section names as keys and HTML content as values
        """
        sections = {
            # Only include technical details - remove writer profile and genre recommendations
            "technical_details": self.generate_technical_details()
        }

        # Add series information if applicable
        series_info = self.generate_series_information()
        if series_info:
            sections["series_information"] = series_info

        return sections
