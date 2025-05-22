---
layout: default
title: EPUB Formatting
parent: Core Components
nav_order: 5
description: "Documentation for the EPUB Formatter that converts generated content into properly formatted ebooks"
---

# EPUB Formatting
{: .no_toc }

The EPUB Formatter is a component of the Ebook Generator that converts generated novel content into properly formatted EPUB files.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The EPUB Formatter:

1. Converts novel content to EPUB format
2. Creates a properly structured ebook with metadata
3. Formats chapters with consistent styling
4. Includes cover images when available
5. Generates a table of contents
6. Ensures compatibility with e-readers

## Basic Usage

The EPUB Formatter is typically used at the end of the novel generation process:

```python
from src.formatters.epub_formatter import EpubFormatter

# Create an EPUB formatter with novel data
formatter = EpubFormatter(novel_data)

# Format and save as EPUB
epub_path = formatter.save_epub(output_dir, cover_path="path/to/cover.jpg")
```

## Novel Data Structure

The EPUB Formatter expects novel data in the following structure:

```python
novel_data = {
    "metadata": {
        "title": "The Mysterious Island",
        "author": "Jane Author",
        "description": "A thrilling adventure...",
        "genre": "Mystery",
        "series": {
            "is_part_of_series": True,
            "series_title": "Adventure Chronicles",
            "book_number": 2
        }
    },
    "chapters": [
        {
            "number": 1,
            "title": "The Beginning",
            "content": "Chapter content in markdown or plain text..."
        },
        # More chapters...
    ]
}
```

## EPUB Structure

The generated EPUB file includes:

1. **Cover**: If a cover image is provided
2. **Title Page**: With title, author, and series information
3. **Copyright Page**: With copyright information
4. **Chapters**: Each chapter with proper formatting
5. **Table of Contents**: Navigation for the ebook

## Formatting Features

### Cover Image

If a cover image is provided, it's included as the first page of the EPUB:

```python
epub_path = formatter.save_epub(output_dir, cover_path="path/to/cover.jpg")
```

### Title Page

The title page includes:
- Book title
- Author name
- Series information (if applicable)

### Chapter Formatting

Chapters are formatted with:
- Chapter titles
- Proper paragraph spacing
- Consistent typography
- Scene breaks (if present in the content)

### Content Conversion

The formatter handles different content formats:
- **Markdown**: Automatically converted to HTML
- **Plain Text**: Paragraphs are properly formatted
- **HTML**: Used as-is with cleaning and normalization

### CSS Styling

The EPUB includes CSS styling for consistent appearance:
- Typography (font family, size, line height)
- Paragraph spacing and indentation
- Chapter title formatting
- Scene break styling
- Special elements (quotes, emphasis, etc.)

## Customization

### Custom CSS

You can customize the CSS by modifying the `_create_css` method in the `EpubFormatter` class:

```python
def _create_css(self) -> epub.EpubItem:
    """
    Create CSS for the EPUB.
    
    Returns:
        EpubItem containing CSS
    """
    css_content = """
    /* Your custom CSS here */
    body {
        font-family: 'Your Preferred Font', serif;
        line-height: 1.6;
    }
    /* More styles... */
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
```

### Custom Pages

You can add custom pages by creating additional methods in the `EpubFormatter` class:

```python
def _create_acknowledgments_page(self) -> epub.EpubHtml:
    """
    Create an acknowledgments page.
    
    Returns:
        EpubHtml containing the acknowledgments page
    """
    content = """
    <div class="acknowledgments">
        <h1>Acknowledgments</h1>
        <p>The author would like to thank...</p>
    </div>
    """
    
    page = epub.EpubHtml(
        title="Acknowledgments",
        file_name="acknowledgments.xhtml",
        lang="en"
    )
    page.content = content
    
    self.book.add_item(page)
    return page
```

Then add it to the spine in the `format_epub` method.

## Technical Details

### EPUB Version

The formatter creates EPUB 3.0 files, which are compatible with most modern e-readers.

### Metadata

The EPUB includes standard metadata:
- Title
- Author
- Language (default: English)
- Description
- Publisher
- Publication date
- Rights/copyright
- Genre (as subject)
- Series information (if applicable)

### Navigation

The EPUB includes two navigation systems:
- NCX file for older e-readers
- Navigation document (nav.xhtml) for EPUB 3.0 compatibility

### Content Processing

The formatter processes content in several steps:
1. Determines if content is markdown, HTML, or plain text
2. Converts markdown to HTML if needed
3. Wraps plain text paragraphs in HTML tags
4. Cleans and normalizes HTML using BeautifulSoup
5. Wraps content in proper HTML structure

## Best Practices

For optimal EPUB formatting:

1. **Provide Complete Metadata**: Include all relevant metadata for proper cataloging
2. **Use Markdown for Content**: Markdown provides the best balance of formatting and simplicity
3. **Include a Cover Image**: Covers enhance the professional appearance of the ebook
4. **Use Consistent Chapter Formatting**: Maintain consistent structure across chapters
5. **Test on Multiple E-readers**: Verify compatibility with different devices and apps

## Troubleshooting

Common issues and solutions:

- **Missing Cover**: Ensure the cover path is correct and the file exists
- **Formatting Issues**: Check content for malformed HTML or markdown
- **Table of Contents Problems**: Verify chapter titles and numbering
- **E-reader Compatibility**: Test with different e-readers and adjust as needed

## EPUB Validation

To ensure your EPUB meets standards:

1. Use the [EPUB Validator](https://validator.idpf.org/) to check for errors
2. Test with popular e-readers (Kindle, Kobo, etc.)
3. Verify all content is visible and properly formatted

## Related Components

- [Novel Generator](./novel-generator.html): Generates the content formatted by the EPUB Formatter
- [Cover Generator](./cover-generator.html): Creates covers that can be included in the EPUB
