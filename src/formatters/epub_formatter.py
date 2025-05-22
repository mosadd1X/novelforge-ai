"""
EPUB formatter for converting novel content to EPUB format.
"""
import os
import uuid
from typing import Dict, List, Any, Optional
from datetime import datetime
import markdown2
from bs4 import BeautifulSoup
from ebooklib import epub

from src.utils.file_handler import sanitize_filename


class EpubFormatter:
    """
    Formatter for converting novel content to EPUB format.
    """

    def __init__(self, novel_data: Dict[str, Any]):
        """
        Initialize the EPUB formatter.

        Args:
            novel_data: Dictionary containing novel data
        """
        self.novel_data = novel_data
        self.book = epub.EpubBook()
        self.chapters = []

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

        # Create title page
        title_page = self._create_title_page()

        # Create copyright page
        copyright_page = self._create_copyright_page()

        # Create chapters
        for chapter in self.novel_data["chapters"]:
            self._create_chapter(chapter)

        # Create table of contents
        self.book.toc = [
            epub.Link("title_page.xhtml", "Title Page", "title_page"),
            epub.Link("copyright.xhtml", "Copyright", "copyright"),
            (
                epub.Section("Chapters"),
                self.chapters
            )
        ]

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

        # Add title and copyright pages
        spine.extend([title_page, copyright_page])

        # Add chapters
        spine.extend(self.chapters)

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

    def save_epub(self, output_dir: str, cover_path: str = None) -> str:
        """
        Save the EPUB file.

        Args:
            output_dir: Directory to save the file in
            cover_path: Path to cover image (optional)

        Returns:
            Path to the saved file
        """
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
