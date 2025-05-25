"""
Back Cover Description Generator for Ebook Generation System.

This module generates compelling back cover descriptions and short descriptions
for book recommendations using Gemini AI with genre-specific prompts.
"""

import json
import re
from typing import Dict, Any, Optional, Tuple
from datetime import datetime

from src.core.resilient_gemini_client import ResilientGeminiClient


class BackCoverGenerator:
    """
    Generates back cover descriptions and short descriptions for books.
    """

    def __init__(self):
        """Initialize the back cover generator."""
        self.gemini_client = ResilientGeminiClient()

    def generate_descriptions(self, novel_data: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate both short description and back cover description for a book.

        Args:
            novel_data: Complete novel data including metadata and chapters

        Returns:
            Dictionary containing generated descriptions
        """
        try:
            # Extract book information
            metadata = novel_data.get("metadata", {})
            chapters = novel_data.get("chapters", [])

            title = metadata.get("title", "Unknown Title")
            genre = metadata.get("genre", "Fiction")
            author = metadata.get("author", "Unknown Author")

            # Generate descriptions using Gemini
            raw_descriptions = self._generate_raw_descriptions(
                title=title,
                genre=genre,
                author=author,
                metadata=metadata,
                chapters=chapters
            )

            if not raw_descriptions:
                return self._generate_fallback_descriptions(metadata)

            # Return the descriptions (already enhanced by Gemini)
            return raw_descriptions

        except Exception as e:
            print(f"Error generating descriptions: {e}")
            return self._generate_fallback_descriptions(novel_data.get("metadata", {}))

    def _generate_raw_descriptions(self, title: str, genre: str, author: str,
                                 metadata: Dict[str, Any], chapters: list) -> Optional[Dict[str, str]]:
        """
        Generate raw descriptions using Gemini AI.

        Args:
            title: Book title
            genre: Book genre
            author: Author name
            metadata: Book metadata
            chapters: List of chapters

        Returns:
            Dictionary with raw descriptions or None if failed
        """
        try:
            # Create chapter summary for context
            chapter_summary = self._create_chapter_summary(chapters[:3])  # First 3 chapters

            # Get genre-specific prompt
            prompt = self._get_genre_specific_prompt(
                title=title,
                genre=genre,
                author=author,
                metadata=metadata,
                chapter_summary=chapter_summary
            )

            # Generate descriptions using Gemini
            response = self.gemini_client.generate_content(prompt)

            if not response:
                return None

            # Parse the response
            return self._parse_gemini_response(response)

        except Exception as e:
            print(f"Error generating raw descriptions: {e}")
            return None

    def _get_genre_specific_prompt(self, title: str, genre: str, author: str,
                                 metadata: Dict[str, Any], chapter_summary: str) -> str:
        """
        Create a genre-specific prompt for description generation using genre-specific prompts.

        Args:
            title: Book title
            genre: Book genre
            author: Author name
            metadata: Book metadata
            chapter_summary: Summary of first few chapters

        Returns:
            Formatted prompt for Gemini
        """
        try:
            # Try to import genre-specific prompts
            genre_module = self._import_genre_module(genre)

            if genre_module:
                # Use genre-specific back cover prompt
                back_cover_prompt = genre_module.get_back_cover_prompt(
                    title=title,
                    author=author,
                    chapter_summary=chapter_summary,
                    metadata=metadata
                )

                # Get short description prompt
                short_desc_prompt = genre_module.get_short_description_prompt(
                    title=title,
                    metadata=metadata
                )

                # Get tagline prompt
                tagline_prompt = genre_module.get_marketing_tagline_prompt(
                    title=title,
                    metadata=metadata
                )

                # Combine all prompts
                combined_prompt = f"""
{back_cover_prompt}

ALSO GENERATE:

SHORT DESCRIPTION (for recommendations):
{short_desc_prompt}

MARKETING TAGLINE:
{tagline_prompt}

FORMAT YOUR RESPONSE EXACTLY AS:
SHORT_DESCRIPTION:
[Your 2-3 line description here]

BACK_COVER_DESCRIPTION:
[Your compelling back cover copy here]

TAGLINE:
[A punchy 5-10 word tagline]
"""
                return combined_prompt

        except Exception as e:
            print(f"Warning: Could not load genre-specific prompts for {genre}: {e}")

        # Fallback to generic prompt
        return self._get_fallback_prompt(title, genre, author, metadata, chapter_summary)

    def _import_genre_module(self, genre: str):
        """
        Import the genre-specific prompt module.

        Args:
            genre: Genre name

        Returns:
            Genre module or None if not found
        """
        try:
            import importlib

            # Convert genre name to module name
            module_name = genre.lower().replace(' ', '_').replace('-', '_').replace('/', '_')
            module_name = ''.join(c for c in module_name if c.isalnum() or c == '_')

            # Try to import the genre module
            module = importlib.import_module(f'src.prompts.{module_name}')
            return module

        except ImportError:
            # Try common variations
            variations = [
                genre.lower().replace(' ', '_').replace('/', '_').replace('-', '_'),
                genre.lower().replace(' ', '_').replace('/', '_'),
                genre.lower().replace(' ', '').replace('/', '_'),
                genre.lower().replace('_', '').replace('/', '_'),
                genre.lower().replace('/', '_'),
                genre.lower()
            ]

            for variation in variations:
                try:
                    module = importlib.import_module(f'src.prompts.{variation}')
                    return module
                except ImportError:
                    continue

            return None
        except Exception:
            return None

    def _get_fallback_prompt(self, title: str, genre: str, author: str,
                           metadata: Dict[str, Any], chapter_summary: str) -> str:
        """
        Create a fallback prompt when genre-specific prompts are not available.

        Args:
            title: Book title
            genre: Book genre
            author: Author name
            metadata: Book metadata
            chapter_summary: Summary of first few chapters

        Returns:
            Formatted fallback prompt
        """
        # Get series information if available
        series_info = ""
        if metadata.get("series", {}).get("is_part_of_series"):
            series_data = metadata["series"]
            series_title = series_data.get("series_title", "")
            book_number = series_data.get("book_number", 1)
            series_info = f"\n- This is Book {book_number} in the {series_title} series"

        # Get target audience
        target_audience = metadata.get("target_audience", "Adult")

        # Genre-specific style guidelines
        genre_guidelines = self._get_genre_guidelines(genre)

        prompt = f"""
You are a professional book marketing copywriter specializing in {genre} literature.
Generate compelling book descriptions for "{title}" by {author}.

BOOK INFORMATION:
- Title: {title}
- Genre: {genre}
- Author: {author}
- Target Audience: {target_audience}{series_info}

STORY CONTEXT:
{chapter_summary}

GENRE-SPECIFIC GUIDELINES:
{genre_guidelines}

GENERATE THREE DESCRIPTIONS:

1. SHORT_DESCRIPTION (2-3 lines, 150-200 characters):
   - Perfect for book recommendations and author pages
   - Hook the reader immediately
   - Include key genre elements
   - End with intrigue or question

2. BACK_COVER_DESCRIPTION (3-5 paragraphs, 400-600 words):
   - Professional back cover copy that sells the book
   - Start with compelling hook
   - Build tension and stakes
   - Include character motivation
   - End with compelling question or cliffhanger
   - Use genre-appropriate language and tone
   - Create urgency to read

3. TAGLINE (5-10 words):
   - Punchy, memorable marketing tagline
   - Captures the essence of the book
   - Perfect for promotion and marketing

FORMAT YOUR RESPONSE EXACTLY AS:
SHORT_DESCRIPTION:
[Your 2-3 line description here]

BACK_COVER_DESCRIPTION:
[Your compelling back cover copy here]

TAGLINE:
[A punchy 5-10 word tagline]

Focus on emotional hooks, stakes, and what makes this book irresistible to {genre} readers.
Make the reader feel they MUST read this book immediately.
"""

        return prompt

    def _get_genre_guidelines(self, genre: str) -> str:
        """
        Get genre-specific writing guidelines for descriptions.

        Args:
            genre: Book genre

        Returns:
            Genre-specific guidelines string
        """
        genre_lower = genre.lower()

        if "romance" in genre_lower:
            return """
- Emphasize emotional connection and chemistry
- Highlight relationship obstacles and tension
- Use passionate, emotional language
- Focus on character growth through love
- Include stakes for the relationship
"""
        elif "mystery" in genre_lower or "thriller" in genre_lower:
            return """
- Create immediate sense of danger or intrigue
- Emphasize the puzzle or threat
- Use suspenseful, urgent language
- Highlight what's at stake if mystery isn't solved
- Build tension with each sentence
"""
        elif "fantasy" in genre_lower:
            return """
- Establish the magical world and its rules
- Highlight unique fantasy elements
- Emphasize the epic scope or personal journey
- Use vivid, imaginative language
- Focus on the hero's destiny or quest
"""
        elif "science fiction" in genre_lower or "sci-fi" in genre_lower:
            return """
- Establish the scientific or technological premise
- Highlight future implications or discoveries
- Use precise, intelligent language
- Emphasize exploration or innovation
- Focus on how technology affects humanity
"""
        elif "horror" in genre_lower:
            return """
- Create atmosphere of dread and fear
- Hint at supernatural or psychological terror
- Use dark, atmospheric language
- Build sense of inescapable doom
- Focus on survival and sanity
"""
        else:
            return """
- Focus on compelling characters and conflicts
- Highlight emotional stakes and growth
- Use engaging, accessible language
- Emphasize universal themes
- Create connection with target audience
"""

    def _create_chapter_summary(self, chapters: list) -> str:
        """
        Create a brief summary of the first few chapters for context.

        Args:
            chapters: List of chapter dictionaries

        Returns:
            Summary string
        """
        if not chapters:
            return "No chapter content available."

        summary_parts = []
        for i, chapter in enumerate(chapters[:3], 1):
            title = chapter.get("title", f"Chapter {i}")
            content = chapter.get("content", "")

            # Get first 200 characters of content
            preview = content[:200].strip()
            if len(content) > 200:
                preview += "..."

            summary_parts.append(f"Chapter {i} ({title}): {preview}")

        return "\n".join(summary_parts)

    def _parse_gemini_response(self, response: str) -> Dict[str, str]:
        """
        Parse Gemini's response to extract descriptions.

        Args:
            response: Raw response from Gemini

        Returns:
            Dictionary with parsed descriptions
        """
        result = {}

        # Extract short description
        short_match = re.search(r'SHORT_DESCRIPTION:\s*\n(.*?)(?=\n\n|\nBACK_COVER_DESCRIPTION:)',
                               response, re.DOTALL | re.IGNORECASE)
        if short_match:
            result["short_description"] = short_match.group(1).strip()

        # Extract back cover description
        back_match = re.search(r'BACK_COVER_DESCRIPTION:\s*\n(.*?)(?=\n\nTAGLINE:|\Z)',
                              response, re.DOTALL | re.IGNORECASE)
        if back_match:
            result["back_cover_description"] = back_match.group(1).strip()

        # Extract tagline
        tagline_match = re.search(r'TAGLINE:\s*\n(.*?)(?=\n\n|\Z)',
                                 response, re.DOTALL | re.IGNORECASE)
        if tagline_match:
            result["tagline"] = tagline_match.group(1).strip()

        return result



    def _generate_fallback_descriptions(self, metadata: Dict[str, Any]) -> Dict[str, str]:
        """
        Generate fallback descriptions when AI generation fails.

        Args:
            metadata: Book metadata

        Returns:
            Dictionary with fallback descriptions
        """
        title = metadata.get("title", "Unknown Title")
        genre = metadata.get("genre", "Fiction")
        author = metadata.get("author", "Unknown Author")

        short_description = f"A compelling {genre.lower()} novel that explores themes of adventure, discovery, and human nature."

        back_cover_description = f"""
{title} takes readers on an unforgettable journey through the world of {genre.lower()}.

In this engaging novel, {author} weaves a tale that combines compelling characters with an intricate plot that will keep readers turning pages late into the night.

With masterful storytelling and rich character development, this book explores the depths of human experience while delivering the excitement and satisfaction that {genre.lower()} readers crave.

Will the characters overcome the challenges they face? Discover the answer in this captivating novel that promises to leave a lasting impression.
"""

        tagline = f"An unforgettable {genre.lower()} adventure"

        return {
            "short_description": short_description,
            "back_cover_description": back_cover_description.strip(),
            "tagline": tagline
        }
