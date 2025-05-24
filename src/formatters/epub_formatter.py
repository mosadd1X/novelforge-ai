"""
EPUB formatter for converting novel content to EPUB format.
"""
import os
import uuid
from typing import Dict, List, Any
from datetime import datetime
import markdown2
from bs4 import BeautifulSoup
from ebooklib import epub

from src.utils.file_handler import sanitize_filename
from src.utils.front_matter_generator import FrontMatterGenerator
from src.utils.back_matter_generator import BackMatterGenerator
from src.utils.writer_profile_manager import WriterProfileManager


class EpubFormatter:
    """
    Formatter for converting novel content to EPUB format.
    """

    def __init__(
        self,
        novel_data: Dict[str, Any],
        writer_profile: Dict[str, Any] = None,
        include_front_matter: bool = True,
        include_back_matter: bool = True
    ):
        """
        Initialize the EPUB formatter.

        Args:
            novel_data: Dictionary containing novel data
            writer_profile: Writer profile information (optional)
            include_front_matter: Whether to include front matter sections
            include_back_matter: Whether to include back matter sections
        """
        self.novel_data = novel_data
        self.writer_profile = writer_profile
        self.include_front_matter = include_front_matter
        self.include_back_matter = include_back_matter
        self.book = epub.EpubBook()
        self.chapters = []
        self.front_matter_sections = []
        self.back_matter_sections = []

        # Initialize generators
        if self.include_front_matter:
            self.front_matter_generator = FrontMatterGenerator(novel_data, writer_profile)
        if self.include_back_matter:
            profile_manager = WriterProfileManager()
            self.back_matter_generator = BackMatterGenerator(novel_data, writer_profile, profile_manager)

    def _setup_metadata(self) -> None:
        """Set up the EPUB metadata."""
        metadata = self.novel_data["metadata"]

        # Set metadata
        self.book.set_identifier(str(uuid.uuid4()))
        self.book.set_title(metadata["title"])
        self.book.set_language('en')
        self.book.add_author(metadata["author"])

        # Add more metadata
        self.book.add_metadata('DC', 'description', metadata["description"])
        self.book.add_metadata('DC', 'publisher', "Novel Generation System")
        self.book.add_metadata('DC', 'date', datetime.now().strftime("%Y-%m-%d"))
        self.book.add_metadata('DC', 'rights', f"© {datetime.now().year} {metadata['author']}")

        # Add genre as subject
        self.book.add_metadata('DC', 'subject', metadata["genre"])

        # Add series information if available
        if "series" in metadata and metadata["series"]["is_part_of_series"]:
            series_title = metadata["series"]["series_title"]
            book_number = metadata["series"]["book_number"]

            # Add series metadata
            self.book.add_metadata('DC', 'relation', f"{series_title} Series, Book {book_number}")
            self.book.add_metadata('DC', 'coverage', f"Book {book_number} of the {series_title} Series")

    def _create_css(self) -> epub.EpubItem:
        """
        Create CSS for the EPUB.

        Returns:
            EpubItem containing CSS
        """
        css_content = """
        @namespace epub "http://www.idpf.org/2007/ops";

        body {
            font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
            margin: 0 5%;
            text-align: justify;
            line-height: 1.5;
        }

        h1, h2, h3, h4, h5, h6 {
            text-align: center;
            line-height: 1.3;
            font-weight: bold;
            margin: 1em 0;
        }

        h1 {
            font-size: 2em;
            margin: 2em 0 1em;
        }

        h2 {
            font-size: 1.5em;
            margin: 1.5em 0 0.8em;
        }

        p {
            margin: 0.5em 0;
            text-indent: 1.5em;
        }

        .chapter-title {
            margin: 3em 0 2em;
            text-align: center;
            font-size: 2em;
            font-weight: bold;
        }

        .no-indent {
            text-indent: 0;
        }

        .centered {
            text-align: center;
            text-indent: 0;
        }

        .scene-break {
            text-align: center;
            text-indent: 0;
            margin: 1.5em auto;
        }

        .scene-break::before {
            content: "* * *";
        }

        .cover {
            text-align: center;
            padding: 0;
            margin: 0;
        }

        .cover img {
            max-width: 100%;
            max-height: 100%;
            padding: 0;
            margin: 0;
        }

        .series-info {
            font-style: italic;
            color: #666;
            margin-top: 2em;
            font-size: 1.1em;
        }

        /* Front Matter and Back Matter Styles */
        .title-page {
            text-align: center;
            padding-top: 20%;
        }

        .title-content {
            margin: 0 auto;
            max-width: 80%;
        }

        .book-title {
            font-size: 3em;
            margin-bottom: 0.5em;
            font-weight: bold;
        }

        .author-name {
            font-size: 2em;
            margin-top: 1em;
            font-weight: normal;
        }

        .ai-attribution {
            font-style: italic;
            margin-top: 2em;
            font-size: 0.9em;
            color: #666;
        }

        .copyright-page h1,
        .introduction h1,
        .about-generation h1,
        .writer-profile h1,
        .series-information h1,
        .genre-recommendations h1,
        .technical-details h1 {
            margin-bottom: 2em;
        }

        .writer-profile h2,
        .series-information h2,
        .genre-recommendations h2,
        .technical-details h2,
        .about-generation h2 {
            text-align: left;
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            font-size: 1.3em;
        }

        .writer-profile ul,
        .series-information ul,
        .genre-recommendations ul,
        .technical-details ul,
        .about-generation ul,
        .writer-profile ol,
        .series-information ol,
        .genre-recommendations ol,
        .technical-details ol,
        .about-generation ol {
            margin-left: 2em;
            margin-bottom: 1em;
        }

        .writer-profile li,
        .series-information li,
        .genre-recommendations li,
        .technical-details li,
        .about-generation li {
            margin-bottom: 0.5em;
        }
        """

        # Create CSS file
        css = epub.EpubItem(
            uid="style",
            file_name="style/style.css",
            media_type="text/css",
            content=css_content
        )

        # Add CSS file
        self.book.add_item(css)

        return css

    def _create_title_page(self) -> epub.EpubHtml:
        """
        Create the title page.

        Returns:
            EpubHtml containing the title page
        """
        metadata = self.novel_data["metadata"]

        # If we already have a cover page, create a minimal title page that won't be visible
        # This prevents duplicate title/cover pages in the EPUB
        if hasattr(self, 'cover_page'):
            # Create a minimal title page that won't be visible in most readers
            title_page = epub.EpubHtml(
                title="Title Page",
                file_name="title_page.xhtml",
                lang="en"
            )
            title_page.content = f"""
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>{metadata["title"]}</title>
                <link rel="stylesheet" type="text/css" href="style/style.css" />
            </head>
            <body>
                <div style="display: none;">
                    <h1>{metadata["title"]}</h1>
                    <p>by {metadata["author"]}</p>
                </div>
            </body>
            </html>
            """

            # Add title page to book
            self.book.add_item(title_page)

            return title_page

        # Check if this is part of a series
        series_info = ""
        if "series" in metadata and metadata["series"]["is_part_of_series"]:
            series_title = metadata["series"]["series_title"]
            book_number = metadata["series"]["book_number"]
            series_info = f"""
            <p class="centered series-info">Book {book_number} of the {series_title} Series</p>
            """

        # Create title page content
        title_content = f"""
        <div class="cover">
            <h1>{metadata["title"]}</h1>
            <p class="centered">by</p>
            <h2>{metadata["author"]}</h2>
            {series_info}
        </div>
        """

        # Create title page
        title_page = epub.EpubHtml(
            title="Title Page",
            file_name="title_page.xhtml",
            lang="en"
        )
        title_page.content = title_content

        # Add title page
        self.book.add_item(title_page)

        return title_page

    def _create_copyright_page(self) -> epub.EpubHtml:
        """
        Create the copyright page.

        Returns:
            EpubHtml containing the copyright page
        """
        metadata = self.novel_data["metadata"]

        # Create copyright page content
        copyright_content = f"""
        <div>
            <h1>Copyright</h1>
            <p class="no-indent">{metadata["title"]}</p>
            <p class="no-indent">by {metadata["author"]}</p>
            <p class="no-indent">© {datetime.now().year} {metadata["author"]}</p>
            <p class="no-indent">All rights reserved.</p>
            <p class="no-indent">This is a work of fiction. Names, characters, places, and incidents are either products of the author's imagination or are used fictitiously. Any resemblance to actual persons, living or dead, events, or locales is entirely coincidental.</p>
        </div>
        """

        # Create copyright page
        copyright_page = epub.EpubHtml(
            title="Copyright",
            file_name="copyright.xhtml",
            lang="en"
        )
        copyright_page.content = copyright_content

        # Add copyright page
        self.book.add_item(copyright_page)

        return copyright_page

    def _create_front_matter_sections(self) -> List[epub.EpubHtml]:
        """
        Create all front matter sections.

        Returns:
            List of EpubHtml objects for front matter
        """
        if not self.include_front_matter:
            return []

        sections = []
        front_matter_content = self.front_matter_generator.get_all_front_matter()

        # Create each front matter section
        for section_name, content in front_matter_content.items():
            if content:  # Only create if content exists
                section = epub.EpubHtml(
                    title=section_name.replace('_', ' ').title(),
                    file_name=f"{section_name}.xhtml",
                    lang="en"
                )

                # Wrap content in proper HTML structure
                section.content = f"""
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                    <title>{section_name.replace('_', ' ').title()}</title>
                    <link rel="stylesheet" type="text/css" href="style/style.css" />
                </head>
                <body>
                    {content}
                </body>
                </html>
                """

                self.book.add_item(section)
                sections.append(section)
                self.front_matter_sections.append(section)

        return sections

    def _create_back_matter_sections(self) -> List[epub.EpubHtml]:
        """
        Create all back matter sections.

        Returns:
            List of EpubHtml objects for back matter
        """
        if not self.include_back_matter:
            return []

        sections = []
        back_matter_content = self.back_matter_generator.get_all_back_matter()

        # Create each back matter section
        for section_name, content in back_matter_content.items():
            if content:  # Only create if content exists
                section = epub.EpubHtml(
                    title=section_name.replace('_', ' ').title(),
                    file_name=f"{section_name}.xhtml",
                    lang="en"
                )

                # Wrap content in proper HTML structure
                section.content = f"""
                <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                    <title>{section_name.replace('_', ' ').title()}</title>
                    <link rel="stylesheet" type="text/css" href="style/style.css" />
                </head>
                <body>
                    {content}
                </body>
                </html>
                """

                self.book.add_item(section)
                sections.append(section)
                self.back_matter_sections.append(section)

        return sections

    def _create_chapter(self, chapter: Dict[str, Any]) -> epub.EpubHtml:
        """
        Create an EPUB chapter.

        Args:
            chapter: Dictionary containing chapter data

        Returns:
            EpubHtml containing the chapter
        """
        chapter_num = chapter["number"]
        chapter_title = chapter.get("title", f"Chapter {chapter_num}")
        chapter_content = chapter["content"]

        # Convert markdown to HTML if needed
        if "```" in chapter_content or "#" in chapter_content or "*" in chapter_content:
            html_content = markdown2.markdown(chapter_content)
        else:
            # If not markdown, wrap paragraphs in <p> tags
            paragraphs = chapter_content.split("\n\n")
            html_content = "".join([f"<p>{p}</p>" for p in paragraphs if p.strip()])

        # Clean up HTML
        soup = BeautifulSoup(html_content, "html.parser")

        # Create chapter HTML
        chapter_html = f"""
        <div class="chapter">
            {str(soup)}
        </div>
        """

        # Create chapter
        epub_chapter = epub.EpubHtml(
            title=f"Chapter {chapter_num}",
            file_name=f"chapter_{chapter_num:02d}.xhtml",
            lang="en"
        )
        epub_chapter.content = chapter_html

        # Add chapter
        self.book.add_item(epub_chapter)
        self.chapters.append(epub_chapter)

        return epub_chapter

    def format_epub(self, cover_path: str = None) -> epub.EpubBook:
        """
        Format the novel as an EPUB.

        Args:
            cover_path: Path to cover image (optional)

        Returns:
            EpubBook object
        """
        # Set up metadata
        self._setup_metadata()

        # Create CSS
        css = self._create_css()

        # Add cover if provided
        if cover_path and os.path.exists(cover_path):
            # Create cover image
            with open(cover_path, 'rb') as f:
                cover_content = f.read()

            # Add cover image
            cover_image = epub.EpubItem(
                uid="cover-image",
                file_name="images/cover.jpg",
                media_type="image/jpeg",
                content=cover_content
            )
            self.book.add_item(cover_image)

            # Create cover page
            self.cover_page = epub.EpubHtml(
                title="Cover",
                file_name="cover.xhtml",
                lang="en"
            )
            self.cover_page.content = f"""
            <html xmlns="http://www.w3.org/1999/xhtml">
            <head>
                <title>Cover</title>
                <link rel="stylesheet" type="text/css" href="style/style.css" />
            </head>
            <body>
                <div class="cover">
                    <img src="images/cover.jpg" alt="Cover" />
                </div>
            </body>
            </html>
            """
            self.book.add_item(self.cover_page)

            # Set cover image
            self.book.set_cover("images/cover.jpg", cover_content)

        # Create front matter sections (replaces old title/copyright pages)
        front_matter_sections = self._create_front_matter_sections()

        # Create legacy title and copyright pages if front matter is disabled
        if not self.include_front_matter:
            title_page = self._create_title_page()
            copyright_page = self._create_copyright_page()
        else:
            title_page = None
            copyright_page = None

        # Create chapters
        for chapter in self.novel_data["chapters"]:
            self._create_chapter(chapter)

        # Create back matter sections
        back_matter_sections = self._create_back_matter_sections()

        # Create table of contents
        toc_items = []

        # Add front matter to TOC
        if self.include_front_matter and front_matter_sections:
            front_matter_toc = []
            for section in front_matter_sections:
                section_title = section.title
                if section_title.lower() == "title page":
                    continue  # Skip title page in TOC
                front_matter_toc.append(section)

            if front_matter_toc:
                toc_items.append((epub.Section("Front Matter"), front_matter_toc))
        else:
            # Legacy front matter
            if title_page:
                toc_items.append(epub.Link("title_page.xhtml", "Title Page", "title_page"))
            if copyright_page:
                toc_items.append(epub.Link("copyright.xhtml", "Copyright", "copyright"))

        # Add chapters
        toc_items.append((epub.Section("Chapters"), self.chapters))

        # Add back matter to TOC
        if self.include_back_matter and back_matter_sections:
            toc_items.append((epub.Section("Additional Information"), back_matter_sections))

        self.book.toc = toc_items

        # Add navigation files
        self.book.add_item(epub.EpubNcx())
        nav = epub.EpubNav()
        self.book.add_item(nav)

        # Define the book spine - without including the nav in the spine
        # This prevents the TOC from appearing as a separate page
        spine = []

        # Add cover page to spine if it exists
        if hasattr(self, 'cover_page'):
            spine.append(self.cover_page)

        # Add front matter sections
        if self.include_front_matter and front_matter_sections:
            spine.extend(front_matter_sections)
        else:
            # Add legacy title and copyright pages
            if title_page:
                spine.append(title_page)
            if copyright_page:
                spine.append(copyright_page)

        # Add chapters
        spine.extend(self.chapters)

        # Add back matter sections
        if self.include_back_matter and back_matter_sections:
            spine.extend(back_matter_sections)

        # Set the spine
        self.book.spine = spine

        # Configure the navigation to be hidden from the spine
        # This prevents the TOC from appearing at the end of the book
        self.book.guide = []  # Clear the guide to prevent duplicate TOC

        # Note: set_option method is not available in some versions of ebooklib
        # Using alternative approach for compatibility
        try:
            self.book.set_option('epub3_pages', False)  # Disable epub3 page list
            self.book.set_option('toc_ncx', False)  # Use only the nav document for TOC
        except AttributeError:
            # If set_option is not available, we'll use the default behavior
            # This may result in both NCX and NAV TOCs being included
            pass

        return self.book

    def save_epub(self, output_dir: str, cover_path: str = None, writer_profile: Dict[str, Any] = None) -> str:
        """
        Save the EPUB file.

        Args:
            output_dir: Directory to save the file in
            cover_path: Path to cover image (optional)
            writer_profile: Writer profile for back matter (optional)

        Returns:
            Path to the saved file
        """
        # Update writer profile if provided
        if writer_profile and not self.writer_profile:
            self.writer_profile = writer_profile
            # Reinitialize generators with the profile
            if self.include_front_matter:
                self.front_matter_generator = FrontMatterGenerator(self.novel_data, writer_profile)
            if self.include_back_matter:
                profile_manager = WriterProfileManager()
                self.back_matter_generator = BackMatterGenerator(self.novel_data, writer_profile, profile_manager)
        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Format the EPUB with cover if provided
        self.format_epub(cover_path)

        # Create a filename
        title = sanitize_filename(self.novel_data["metadata"]["title"])
        filename = f"{title}.epub"
        file_path = os.path.join(output_dir, filename)

        # Save the EPUB
        epub.write_epub(file_path, self.book, {})

        return file_path
