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
from src.utils.cover_folder_manager import CoverFolderManager
from src.database.cover_database_manager import get_cover_database_manager
from src.database.database_manager import get_database_manager
import os
import base64


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
        self.cover_manager = CoverFolderManager()
        self.cover_db_manager = get_cover_database_manager()
        self.db_manager = get_database_manager()
        self.metadata = novel_data.get("metadata", {})
        self.genre = self.metadata.get("genre", "Fiction")
        self.genre_defaults = get_genre_defaults(self.genre)

    def generate_writer_profile_section(self) -> str:
        """
        Generate enhanced "About the Author" section with rich biographical content,
        book description, and other books by the same author.

        Returns:
            HTML content for the enhanced writer profile section
        """
        try:
            if not self.writer_profile:
                return self._generate_generic_profile_section()

            profile_name = self.writer_profile.get("name", "Custom AI Writer Profile")

            # Generate the enhanced author section with new layout
            return self._generate_enhanced_author_section(profile_name)

        except Exception as e:
            # Return a basic fallback section
            return f"""
            <div class="writer-profile">
                <h1>About the Author</h1>
                <p>This book was generated using AI technology.</p>
            </div>
            """

    def _generate_enhanced_author_section(self, profile_name: str) -> str:
        """
        Generate the enhanced author section with improved layout matching the diagram.

        Args:
            profile_name: Name of the author profile

        Returns:
            HTML content for enhanced author section
        """
        # Get profile image (smaller, right-aligned)
        profile_image_html = self._get_enhanced_profile_image(profile_name)

        # Get enhanced author biography
        author_biography = self._get_enhanced_author_biography()

        # Get current book description (2-3 lines)
        book_description = self._get_current_book_description()

        # Get other books by the same author
        other_books_html = self._get_other_books_by_author(profile_name)

        # Build the enhanced layout
        if author_biography:
            biography_content = self._format_biography_paragraphs(author_biography)
        else:
            biography_content = self._get_fallback_biography_content(profile_name)

        return f"""
        <div class="writer-profile enhanced-layout">
            <h1>About the Author</h1>

            <div class="author-content-wrapper">
                {profile_image_html}

                <div class="author-text-content">
                    <h2>{profile_name}</h2>

                    <div class="author-biography">
                        {biography_content}
                    </div>

                    {book_description}

                    <div class="fictional-author-notice">
                        <p><em><strong>Important Note:</strong> {profile_name} is a fictional author persona.
                        This profile draws inspiration from real literary techniques and styles but represents
                        a completely original fictional identity. All books attributed to this name are
                        AI-generated works.</em></p>
                    </div>
                </div>
            </div>

            {other_books_html}
        </div>
        """

    def _get_enhanced_profile_image(self, profile_name: str) -> str:
        """
        Get profile image HTML with enhanced styling (smaller, right-aligned).

        Args:
            profile_name: Name of the author profile

        Returns:
            HTML for enhanced profile image
        """
        image_info = self.image_manager.get_writer_image_info(profile_name)

        if image_info['has_image'] and image_info['base64_data']:
            return f"""
            <div class="profile-image-enhanced">
                <img src="{image_info['base64_data']}" alt="Portrait of {profile_name}"
                     class="author-portrait-small" />
            </div>
            """
        return ""

    def _get_current_book_description(self) -> str:
        """
        Get the current book's description formatted for the author section.

        Returns:
            HTML content with book description
        """
        # Get description from metadata
        description = self.metadata.get("description", "")

        if not description:
            # Try to get from database if we have book ID
            try:
                # Look for current book in database by title and author
                title = self.metadata.get("title", "")
                author = self.metadata.get("author", "")

                if title and author:
                    books = self.db_manager.get_books(status="completed")
                    for book in books:
                        if (book.get("title", "").lower() == title.lower() and
                            book.get("author", "").lower() == author.lower()):
                            description = book.get("description", "")
                            break
            except Exception:
                pass

        if description:
            # Truncate to 2-3 lines (approximately 200-300 characters)
            if len(description) > 300:
                description = description[:297] + "..."

            return f"""
            <div class="current-book-description">
                <p><strong>About this book:</strong> {description}</p>
            </div>
            """

        return ""

    def _get_other_books_by_author(self, profile_name: str) -> str:
        """
        Get other books by the same author with small cover thumbnails.

        Args:
            profile_name: Name of the author profile

        Returns:
            HTML content for other books section
        """
        try:
            # Get all completed books by this author
            books = self.db_manager.get_books(status="completed")
            author_books = []

            current_title = self.metadata.get("title", "").lower()

            for book in books:
                book_author = book.get("author", "").lower()
                book_title = book.get("title", "").lower()

                # Match by author name and exclude current book
                if (profile_name.lower() in book_author or book_author in profile_name.lower()) and book_title != current_title:
                    author_books.append(book)

            if not author_books:
                return ""

            # Select the best book to display using smart selection
            selected_book = self._select_best_author_book(author_books)
            author_books = [selected_book]

            # Use singular/plural text based on number of books
            section_title = "Another Book by the Same Author" if len(author_books) == 1 else "Other Books by the Same Author"

            books_html = f"""
            <div class="other-books-section">
                <h3>{section_title}</h3>
                <div class="other-books-gallery">
            """

            for book in author_books:
                book_id = book.get("book_id", "")
                book_title = book.get("title", "Unknown Title")
                book_description = book.get("description", "")

                # Get cover image if available
                cover_html = ""
                if book_id and self.cover_db_manager.has_cover(book_id):
                    cover_data_url = self.cover_db_manager.get_cover_data_url(book_id)
                    if cover_data_url:
                        cover_html = f"""
                        <div class="other-book-cover">
                            <img src="{cover_data_url}" alt="{book_title} Cover" class="other-book-thumbnail" />
                        </div>
                        """

                # Truncate description for display
                short_description = ""
                if book_description:
                    if len(book_description) > 100:
                        short_description = book_description[:97] + "..."
                    else:
                        short_description = book_description

                books_html += f"""
                <div class="other-book-item">
                    {cover_html}
                    <div class="other-book-info">
                        <h4>{book_title}</h4>
                        {f'<p class="other-book-desc">{short_description}</p>' if short_description else ''}
                    </div>
                </div>
                """

            books_html += """
                </div>
            </div>
            """

            return books_html

        except Exception as e:
            # If anything goes wrong, return empty string
            return ""

    def _select_best_author_book(self, author_books: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Select the best book to display from the author's other works.
        Uses intelligent criteria rather than just taking the first/newest.

        Args:
            author_books: List of books by the same author

        Returns:
            The best book to display
        """
        if len(author_books) == 1:
            return author_books[0]

        # Scoring criteria for book selection
        scored_books = []

        for book in author_books:
            score = 0

            # 1. Prefer books with descriptions (more informative for readers)
            description = book.get("description", "")
            if description and len(description.strip()) > 50:
                score += 30
            elif description and len(description.strip()) > 20:
                score += 15

            # 2. Prefer books with covers (more visually appealing)
            if book.get("cover_base64"):
                score += 25

            # 3. Prefer books from same genre (reader interest alignment)
            current_genre = self.metadata.get("genre", "").lower()
            book_genre = book.get("genre", "").lower()
            if current_genre and book_genre == current_genre:
                score += 20
            elif current_genre and current_genre in book_genre:
                score += 10

            # 4. Prefer books with reasonable word count (quality indicator)
            word_count = book.get("word_count", 0)
            if 30000 <= word_count <= 120000:  # Typical novel range
                score += 15
            elif 15000 <= word_count <= 150000:  # Acceptable range
                score += 8

            # 5. Prefer books that are part of series (reader engagement)
            series_info = book.get("series_info", {})
            if series_info and series_info.get("is_part_of_series"):
                score += 10

            # 6. Slight preference for newer books (relevance)
            try:
                from datetime import datetime
                created_date = book.get("created_date", "")
                if created_date:
                    book_date = datetime.fromisoformat(created_date.replace('Z', '+00:00'))
                    days_old = (datetime.now() - book_date).days
                    if days_old < 30:  # Very recent
                        score += 8
                    elif days_old < 90:  # Recent
                        score += 5
                    elif days_old < 365:  # This year
                        score += 2
            except:
                pass  # Skip date scoring if parsing fails

            # 7. Prefer books with longer titles (often more descriptive)
            title = book.get("title", "")
            if len(title) > 20:
                score += 5
            elif len(title) > 10:
                score += 2

            scored_books.append((score, book))

        # Sort by score (highest first) and return the best book
        scored_books.sort(key=lambda x: x[0], reverse=True)

        # If multiple books have the same top score, prefer the most recent
        top_score = scored_books[0][0]
        top_books = [book for score, book in scored_books if score == top_score]

        if len(top_books) > 1:
            # Among top-scored books, prefer the most recent
            top_books.sort(key=lambda x: x.get("created_date", ""), reverse=True)

        return top_books[0]

    def _get_fallback_biography_content(self, profile_name: str) -> str:
        """
        Generate fallback biography content when enhanced biography is not available.

        Args:
            profile_name: Name of the author profile

        Returns:
            HTML formatted biography content
        """
        profile_data = self.writer_profile.get("profile_data", {})

        # Extract profile information
        writing_style = profile_data.get("writing_style", "Engaging and descriptive")
        influences = profile_data.get("literary_influences", "Various classic and contemporary authors")
        themes = profile_data.get("thematic_focuses", "Human experience and storytelling")

        # Get additional profile metadata
        cultural_background = self.writer_profile.get("cultural_background", "")
        era = self.writer_profile.get("era", "")

        # Create biographical narrative
        bio_paragraphs = []

        # First paragraph - introduction
        intro = f"{profile_name} is a fictional author persona created specifically for AI-generated {self.genre.lower()} literature."
        if cultural_background and era:
            intro += f" Drawing inspiration from {cultural_background} literary traditions of the {era} era, this profile represents a unique blend of historical influence and contemporary storytelling."
        bio_paragraphs.append(f"<p>{intro}</p>")

        # Second paragraph - writing style and approach
        style_para = f"Known for {writing_style.lower()}, {profile_name}'s work is characterized by {themes.lower()}."
        if isinstance(influences, list):
            influences_str = ", ".join(influences[:3])
        else:
            influences_str = str(influences)[:100]
        style_para += f" The writing draws from influences including {influences_str}, creating narratives that resonate with modern readers while honoring literary traditions."
        bio_paragraphs.append(f"<p>{style_para}</p>")

        # Third paragraph - thematic focus
        theme_para = f"Through carefully crafted {self.genre.lower()} narratives, {profile_name} explores the complexities of human experience, weaving together compelling characters and thought-provoking themes. Each work demonstrates a commitment to both entertaining storytelling and meaningful literary exploration."
        bio_paragraphs.append(f"<p>{theme_para}</p>")

        return '\n'.join(bio_paragraphs)

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

    def _get_series_cover_images(self, series_title: str, total_books: int) -> str:
        """
        Get HTML for series cover images if they exist.

        Args:
            series_title: Title of the series
            total_books: Total number of books in the series

        Returns:
            HTML content for cover images or empty string
        """
        try:
            cover_images = []

            # Check for covers for each book in the series
            for book_num in range(1, min(total_books + 1, 6)):  # Limit to first 5 books for display
                cover_found = False

                # Step 1: Check database for covers first
                try:
                    # Find books in database with matching series info
                    all_books = self.db_manager.get_books(status="completed")
                    for book in all_books:
                        book_series = book.get("series_info", {})
                        if (book_series.get("series_title") == series_title and
                            book_series.get("book_number") == book_num):

                            if self.cover_db_manager.has_cover(book["book_id"]):
                                # Get cover as base64 data URL
                                cover_data_url = self.cover_db_manager.get_cover_data_url(book["book_id"])
                                if cover_data_url:
                                    cover_images.append({
                                        'book_number': book_num,
                                        'base64_data': cover_data_url,
                                        'filename': f"Book{book_num}_database.jpg"
                                    })
                                    cover_found = True
                                    break
                except Exception as e:
                    pass  # Continue to file system check

                # Step 2: If not found in database, check file system
                if not cover_found:
                    book_series_info = {
                        "series_title": series_title,
                        "book_number": book_num
                    }

                    found_images = self.cover_manager.scan_for_cover_images(series_title, book_series_info)
                    if found_images:
                        # Use the first valid image found
                        for image_path in found_images:
                            is_valid, _ = self.cover_manager.validate_cover_image(image_path)
                            if is_valid:
                                # Convert to base64 for embedding
                                try:
                                    with open(image_path, 'rb') as img_file:
                                        img_data = base64.b64encode(img_file.read()).decode('utf-8')
                                        cover_images.append({
                                            'book_number': book_num,
                                            'base64_data': f"data:image/jpeg;base64,{img_data}",
                                            'filename': os.path.basename(image_path)
                                        })
                                        break
                                except Exception as e:
                                    continue

            if not cover_images:
                return ""

            # Generate HTML for cover gallery
            covers_html = """
            <div class="series-covers">
                <h2>Books in This Series</h2>
                <div class="cover-gallery">
            """

            for cover in cover_images:
                covers_html += f"""
                    <div class="series-cover-item">
                        <img src="{cover['base64_data']}" alt="Book {cover['book_number']} Cover"
                             class="series-cover-thumbnail" />
                        <p class="cover-caption">Book {cover['book_number']}</p>
                    </div>
                """

            covers_html += """
                </div>
            </div>
            """

            return covers_html

        except Exception as e:
            # If anything goes wrong, just return empty string
            return ""

    def generate_genre_recommendations(self) -> str:
        """
        Generate reading recommendations for the genre, or series information if part of a series.

        Returns:
            HTML content for genre recommendations or series information
        """
        # Check if this is part of a series
        if "series" in self.metadata and self.metadata["series"].get("is_part_of_series"):
            # Generate series-specific content instead of generic genre recommendations
            return self._generate_series_recommendations()

        # Fall back to genre recommendations for non-series books
        return self._generate_genre_recommendations()

    def _generate_series_recommendations(self) -> str:
        """
        Generate series-specific recommendations and information with cover images.

        Returns:
            HTML content for series recommendations
        """
        series_data = self.metadata["series"]
        series_title = series_data.get("series_title", "Unknown Series")
        book_number = series_data.get("book_number", 1)
        total_books = series_data.get("planned_books", "multiple")

        # Get cover images for the series
        total_books_int = total_books if isinstance(total_books, int) else 5  # Default to 5 for "multiple"
        cover_images_html = self._get_series_cover_images(series_title, total_books_int)

        # Create series description
        series_description = f"""
        This book is part of the {series_title} series, an AI-generated collection
        of interconnected {self.genre.lower()} novels. The series maintains consistent
        characters, world-building, and thematic elements while telling unique stories
        in each volume.
        """

        # Generate reading order information
        reading_order = ""
        if book_number > 1:
            reading_order = f"""
            <h2>Reading Order</h2>
            <p>This is Book {book_number} in the {series_title} series. While each book
            tells a complete story, reading the series in order will provide the best
            experience for understanding character development and overarching plot threads.</p>
            """

        # Generate future books information
        future_info = ""
        if isinstance(total_books, int) and book_number < total_books:
            remaining = total_books - book_number
            future_info = f"""
            <h2>Upcoming Books</h2>
            <p>There are {remaining} more books planned in the {series_title} series,
            continuing the story and expanding the world introduced in this collection.</p>
            """
        elif total_books == "multiple" or (isinstance(total_books, int) and total_books > book_number):
            future_info = f"""
            <h2>Continuing the Series</h2>
            <p>The {series_title} series continues with additional books that expand
            the world and develop the characters further. Each new volume brings fresh
            perspectives while maintaining the series' core themes and continuity.</p>
            """

        return f"""
        <div class="series-recommendations">
            <h1>About the {series_title} Series</h1>

            <p>{series_description}</p>

            {cover_images_html}

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

            <h2>AI Generation Process</h2>
            <p>The AI generation process for this series involved creating detailed
            continuity tracking, character development arcs, and overarching narrative
            threads to ensure a cohesive and engaging multi-book experience. Each book
            builds upon the foundation established in previous volumes while introducing
            new elements to keep the series fresh and engaging.</p>
        </div>
        """

    def _generate_genre_recommendations(self) -> str:
        """
        Generate traditional genre-based reading recommendations.

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

        # Add genre recommendations (includes series information for series books)
        sections["genre_recommendations"] = self.generate_genre_recommendations()

        # Add technical details
        sections["technical_details"] = self.generate_technical_details()

        return sections
