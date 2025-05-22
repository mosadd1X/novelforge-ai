---
layout: default
title: Cover Generator
parent: Core Components
nav_order: 4
description: "Documentation for the Cover Generator that creates professional-looking book covers"
---

# Cover Generator
{: .no_toc }

The Cover Generator is a component of the Ebook Generator that creates professional-looking book covers without requiring external images or assets.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The Cover Generator uses programmatic techniques to create visually appealing book covers with:

- Dynamic backgrounds with gradients and patterns
- Professional typography for titles, subtitles, and author names
- Series information display
- Proper title case formatting
- Visual effects like shadows and embossing

## Usage

### Basic Usage

The cover generator can be accessed through the terminal UI or programmatically:

```python
from src.utils.cover_generator import CoverGenerator

# Create a cover generator instance
cover_gen = CoverGenerator(output_dir="covers")

# Generate a basic cover
cover_path = cover_gen.generate_cover(
    title="The Mysterious Island",
    author="Jane Author",
    genre="Mystery"
)
```

### Advanced Usage

For more customization, you can provide additional parameters:

```python
# Generate a cover with subtitle and series information
cover_path = cover_gen.generate_cover(
    title="The Mysterious Island",
    author="Jane Author",
    genre="Mystery",
    subtitle="A Journey of Discovery",
    series_info={
        "series_title": "The Explorer Chronicles",
        "book_number": 2
    }
)
```

## Parameters

The `generate_cover` method accepts the following parameters:

| Parameter    | Type   | Description                                      | Required |
|--------------|--------|--------------------------------------------------|----------|
| title        | str    | The title of the book                            | Yes      |
| author       | str    | The author's name                                | Yes      |
| genre        | str    | The book's genre (affects color scheme)          | Yes      |
| output_path  | str    | Custom path to save the cover image              | No       |
| subtitle     | str    | Subtitle to display under the main title         | No       |
| series_info  | dict   | Dictionary with series_title and book_number     | No       |

## Color Schemes

The cover generator selects color schemes based on the book's genre:

- **Mystery/Thriller**: Dark blues, purples, and blacks
- **Romance**: Soft pinks, reds, and purples
- **Fantasy**: Deep blues, purples, and greens
- **Science Fiction**: Blues, teals, and blacks
- **Horror**: Reds, blacks, and dark grays
- **Literary Fiction**: Neutral tones with accent colors
- **Historical Fiction**: Sepia tones, golds, and browns
- **Young Adult**: Vibrant, bright colors
- **Children's**: Playful, primary colors

## Typography

The cover generator uses appropriate typography for different elements:

- **Title**: Large, bold font with emphasis effects
- **Subtitle**: Medium-sized font with subtle effects
- **Author Name**: Professional font placement at the bottom
- **Series Information**: Clearly displayed for series books

## Title Case Formatting

The cover generator automatically applies proper title case formatting:

- First and last words are always capitalized
- Major words are capitalized
- Minor words (a, an, the, and, but, for, at, by, etc.) are lowercase when they appear in the middle of the title

## Integration with EPUB Generation

When generating an EPUB file, you can include the generated cover:

```python
from src.formatters.epub_formatter import EpubFormatter

# Format the novel as EPUB with cover
formatter = EpubFormatter(novel_data)
epub_path = formatter.save_epub(output_dir, cover_path=cover_path)
```

## Customization

The cover generator can be customized by modifying the `CoverGenerator` class:

- Change default dimensions in the `__init__` method
- Modify color schemes in the `_get_genre_colors` method
- Adjust font sizes and styles in the `_load_font` method
- Create new background patterns in the `_create_background` method

## Technical Details

The cover generator uses the Python Imaging Library (PIL/Pillow) to create images programmatically. It:

1. Creates a base image with the specified dimensions
2. Generates a background with gradients and patterns based on genre
3. Applies the title with proper formatting and visual effects
4. Adds subtitle if provided
5. Adds series information if provided
6. Places the author name at the bottom
7. Saves the image to the specified output path

## Troubleshooting

If you encounter issues with the cover generator:

- Ensure the output directory exists and is writable
- Check that the title, author, and genre are provided
- Verify that any custom fonts are properly installed or accessible
- For custom dimensions, ensure they are appropriate for book covers (typically 6:9 ratio)

## Example Output

The generated covers will be saved as JPEG files in the specified output directory. The default naming convention is:

```
[output_dir]/[sanitized_title]_cover.jpg
```

Where `[sanitized_title]` is the book title with spaces replaced by underscores and special characters removed.

## Related Components

- [EPUB Formatter](./epub-formatting.html): Uses the generated covers in the final EPUB
- [Series Generation](./series-generation.html): Integrates with cover generation for series branding
