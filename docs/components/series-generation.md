---
layout: default
title: Series Generation
parent: Core Components
nav_order: 3
description: "Documentation for the Series Generation feature that creates consistent multi-book series"
---

# Series Generation
{: .no_toc }

The Series Generation feature allows you to create a complete series of novels with consistent characters, plot arcs, and world-building.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The Series Generator creates a cohesive series of novels by:

1. Generating an overarching series plan
2. Creating consistent character development across books
3. Maintaining plot continuity and story arcs
4. Ensuring world-building consistency
5. Managing series metadata and book numbering

## Usage

### Using the Series Management Menu

The easiest way to work with series is through the Series Management Menu:

```bash
python -m src.main --series-menu
```

Or select "Generate a Series" from the main menu when running:

```bash
python run.py
```

### Programmatic Usage

You can also use the Series Generator programmatically:

```python
from src.core.series_generator import SeriesGenerator

# Create a series generator instance
series_generator = SeriesGenerator()

# Initialize a new series
series_generator.initialize_series(
    title="The Chronicles of Eldoria",
    description="An epic fantasy series set in the magical world of Eldoria.",
    genre="Fantasy",
    target_audience="Adult (18+)",
    planned_books=3,
    author="Jane Author"
)

# Generate a series plan
book_templates = series_generator.generate_series_plan()

# Generate each book in the series
for i, book_template in enumerate(book_templates, 1):
    epub_path = series_generator.generate_book(book_template, i)
    print(f"Book {i} generated: {epub_path}")
```

## Series Management Menu

The Series Management Menu provides the following options:

1. **Create New Series**: Initialize a new series with basic information
2. **Load Existing Series**: Continue working with a previously created series
3. **Generate Next Book in Series**: Generate the next book in an existing series
4. **View Series Information**: Display details about the series and its books
5. **Create Covers for Books**: Generate covers for all books in the series
6. **Export Series as EPUB**: Export all books in the series as EPUB files
7. **Return to Main Menu**: Go back to the main application menu

## Series Structure

A series consists of:

- **Series Metadata**: Title, description, genre, target audience, author
- **Series Plan**: Overarching plot, character arcs, and thematic elements
- **Book Templates**: Individual book outlines with specific plot points
- **Generated Books**: The actual novels created from the templates

## Series Directory Structure

Series are organized in the following directory structure:

```
output/series/[series_title]/
├── series_info.json       # Series metadata and plan
├── book_1/                # First book directory
│   ├── [title].epub       # Generated EPUB file
│   ├── [title].json       # Novel data in JSON format
│   └── memory/            # Memory files for consistency
├── book_2/                # Second book directory
│   └── ...
└── ...
```

## Series Consistency

The Series Generator maintains consistency across books through:

1. **Character Continuity**: Characters retain their traits, backgrounds, and development
2. **Plot Progression**: Each book builds on previous events and advances the overall arc
3. **World Consistency**: Settings, rules, and established facts remain consistent
4. **Thematic Development**: Core themes evolve and develop across the series

## Customizing Series Generation

You can customize series generation through:

### Generation Options

When creating a new series, you can specify:

- **Genre**: Affects the style, structure, and themes
- **Target Audience**: Influences content, complexity, and tone
- **Planned Books**: Number of books in the series
- **Series Arc Type**: Linear progression, episodic, or hybrid

### Advanced Options

For more control, you can modify:

- **Character Development Rate**: How quickly characters evolve
- **Plot Complexity**: Simple to complex narrative structures
- **World-Building Depth**: Level of detail in the fictional world
- **Thematic Emphasis**: Which themes receive more focus

## API Reference

### SeriesGenerator Class

The main class for generating series:

- `initialize_series(title, description, genre, target_audience, planned_books, author)`: Sets up a new series
- `generate_series_plan()`: Creates a plan for the entire series
- `generate_book(book_template, book_number)`: Generates a single book in the series

### SeriesManager Class

Manages series metadata and consistency:

- `initialize_series(title, description, genre, target_audience, planned_books, author)`: Creates a new series
- `load_series(series_dir)`: Loads an existing series
- `add_book(book_data)`: Adds a book to the series
- `get_series_info()`: Gets information about the series
- `get_book_info(book_number)`: Gets information about a specific book

## Series Management Features

### Zip Series Books

The Series Management Menu includes a "Zip Series Books" feature that allows you to create a compressed archive of all books in a series for easy sharing:

**Features:**
- **Format Selection**: Choose which file formats to include (EPUB only, all ebook formats, or everything)
- **Custom Output Location**: Save to series directory, Desktop, Downloads, or custom location
- **Organized Structure**: Books are organized in numbered folders within the zip (Book_01, Book_02, etc.)
- **Progress Tracking**: Real-time progress updates during zip creation
- **File Size Information**: Shows final zip file size

**Usage:**
1. Select "Work with Existing Series" from the main menu
2. Choose your series
3. Select "Zip Series Books"
4. Choose which file formats to include
5. Specify output location and filename
6. The zip file will be created with all selected books and formats

**Zip Structure:**
```
series_name.zip
├── series_info.json
├── Book_01/
│   ├── book_title.epub
│   ├── book_title.json
│   └── cover.jpg
├── Book_02/
│   └── ...
└── ...
```

## Best Practices

For the best results with series generation:

1. **Choose a Consistent Genre**: Series work best when the genre remains consistent
2. **Plan Appropriate Length**: 3-5 books is optimal for most series
3. **Review Between Books**: Check each book before generating the next one
4. **Maintain Character Focus**: Decide on main characters that will appear throughout
5. **Define Clear Themes**: Establish core themes that will develop across books
6. **Use Zip Feature for Sharing**: Create zip archives to easily share complete series

## Troubleshooting

Common issues and solutions:

- **Inconsistent Characters**: Use the Series Management Menu to view and edit character information
- **Plot Holes**: Review the series plan and adjust as needed
- **Generation Failures**: Check API key status and ensure you have sufficient quota
- **Missing Files**: Verify the series directory structure is intact
- **Zip Creation Fails**: Ensure you have write permissions to the output directory and sufficient disk space
- **Empty Zip File**: Check that the series has generated books with the selected file formats

## Example Series Plan

A typical series plan includes:

```json
{
  "series_title": "The Chronicles of Eldoria",
  "description": "An epic fantasy series set in the magical world of Eldoria.",
  "genre": "Fantasy",
  "target_audience": "Adult (18+)",
  "author": "Jane Author",
  "planned_books": 3,
  "current_book": 1,
  "series_arc": {
    "main_plot": "The rise of darkness in Eldoria and the quest to restore balance.",
    "character_arcs": [...],
    "thematic_elements": [...]
  },
  "books": [
    {
      "title": "The Awakening",
      "description": "Book 1 in the Chronicles of Eldoria series.",
      "main_plot": "The discovery of ancient magic and the first signs of darkness.",
      "series_connection": "Introduces the world and main characters.",
      "character_developments": "..."
    },
    ...
  ]
}
```

## Related Components

- [Novel Generator](./novel-generator.html): Used by the Series Generator to create individual books
- [Memory Management](./memory-management.html): Ensures consistency within each book
- [Cover Generator](./cover-generator.html): Creates covers for series books with consistent branding
