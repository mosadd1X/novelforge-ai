"""
Back Matter Generator for AI-Generated Books

This module generates appropriate back matter sections for AI-generated books,
including writer profile information, series details, and AI generation insights.
"""

from typing import Dict, Any, List, Optional
from datetime import datetime

from src.utils.genre_defaults import get_genre_defaults, get_all_genres
from src.utils.writer_profile_manager import WriterProfileManager
from src.utils.profile_image_manager import ProfileImageManager


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
        self.image_manager = ProfileImageManager()
        self.metadata = novel_data.get("metadata", {})
        self.genre = self.metadata.get("genre", "Fiction")
        self.genre_defaults = get_genre_defaults(self.genre)

    def generate_writer_profile_section(self) -> str:
        """
        Generate "About the Author" section with enhanced biographical content.

        Returns:
            HTML content for the writer profile section
        """
        if not self.writer_profile:
            return self._generate_generic_profile_section()

        profile_name = self.writer_profile.get("name", "Custom AI Writer Profile")

        # Get profile image information
        image_info = self.image_manager.get_writer_image_info(profile_name)
        profile_image_html = ""

        if image_info['has_image'] and image_info['base64_data']:
            profile_image_html = f"""
            <div class="profile-image">
                <img src="{image_info['base64_data']}" alt="Portrait of {profile_name}"
                     class="author-portrait" />
                <p class="image-caption">Portrait of {profile_name}</p>
            </div>
            """

        # Try to get the enhanced author biography
        author_biography = self._get_enhanced_author_biography()

        if author_biography:
            # Use the enhanced biographical narrative
            return f"""
            <div class="writer-profile">
                <h1>About the Author</h1>

                {profile_image_html}

                <h2>{profile_name}</h2>

                <div class="author-biography">
                    {self._format_biography_paragraphs(author_biography)}
                </div>

                <div class="fictional-author-notice">
                    <p><em><strong>Important Note:</strong> {profile_name} is a fictional author persona.
                    This profile draws inspiration from real literary techniques and styles but represents
                    a completely original fictional identity. All books attributed to this name are
                    AI-generated works.</em></p>
                </div>
            </div>
            """
        else:
            # Fallback to technical profile information
            return self._generate_technical_profile_section(profile_image_html, profile_name)

    def _get_enhanced_author_biography(self) -> Optional[str]:
        """
        Get the enhanced author biography from the writer profile module.

        Returns:
            Enhanced biography string or None if not available
        """
        try:
            # Try to get the biography from the profile module
            if hasattr(self.writer_profile, '_module_name'):
                module_name = f"src.writer_profiles.master_profiles.{self.writer_profile['_module_name']}"
            else:
                # Try to derive module name from writer name
                profile_name = self.writer_profile.get("name", "")
                if profile_name:
                    # Convert name to module format (e.g., "Catherine Fairfax" -> "catherine_fairfax")
                    module_name = profile_name.lower().replace(" ", "_").replace(".", "_")
                    module_name = f"src.writer_profiles.master_profiles.{module_name}"
                else:
                    return None

            # Import the module and get the biography
            import importlib
            module = importlib.import_module(module_name)

            if hasattr(module, 'get_author_biography'):
                biography = module.get_author_biography()
                if biography and len(biography.strip()) > 50:
                    return biography.strip()

            return None

        except Exception as e:
            # If we can't get the enhanced biography, return None to use fallback
            return None

    def _format_biography_paragraphs(self, biography: str) -> str:
        """
        Format the biography text into proper HTML paragraphs.

        Args:
            biography: Raw biography text

        Returns:
            HTML formatted biography
        """
        # Split into paragraphs and wrap in <p> tags
        paragraphs = [p.strip() for p in biography.split('\n\n') if p.strip()]
        formatted_paragraphs = [f"<p>{paragraph}</p>" for paragraph in paragraphs]
        return '\n'.join(formatted_paragraphs)

    def _generate_technical_profile_section(self, profile_image_html: str, profile_name: str) -> str:
        """
        Generate fallback technical profile section when enhanced biography is not available.

        Args:
            profile_image_html: HTML for profile image
            profile_name: Name of the profile

        Returns:
            HTML content for technical profile section
        """
        profile_data = self.writer_profile.get("profile_data", {})

        # Extract profile information
        writing_style = profile_data.get("writing_style", "Engaging and descriptive")
        influences = profile_data.get("literary_influences", "Various classic and contemporary authors")
        themes = profile_data.get("thematic_focuses", "Human experience and storytelling")
        techniques = profile_data.get("narrative_techniques", "Character-driven narratives")
        strengths = profile_data.get("strengths", "Creating compelling stories")

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
            <h1>About the Author</h1>

            {profile_image_html}

            <h2>{profile_name}</h2>

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
            <p><strong>Writing Style:</strong> {writing_style[:200]}...</p>
            <p><strong>Literary Influences:</strong> {', '.join(influences[:3]) if isinstance(influences, list) else str(influences)[:200]}...</p>
            <p><strong>Thematic Focus:</strong> {', '.join(themes[:3]) if isinstance(themes, list) else str(themes)[:200]}...</p>
            {cultural_context}
            {style_tags}
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
        sections = {}

        # Add writer profile section with image
        writer_profile = self.generate_writer_profile_section()
        if writer_profile:
            sections["writer_profile"] = writer_profile

        # Add series information if applicable
        series_info = self.generate_series_information()
        if series_info:
            sections["series_information"] = series_info

        # Add genre recommendations
        sections["genre_recommendations"] = self.generate_genre_recommendations()

        # Add technical details
        sections["technical_details"] = self.generate_technical_details()

        return sections
