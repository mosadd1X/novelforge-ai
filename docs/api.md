---
layout: default
title: API Documentation
nav_order: 5
description: "Detailed documentation of the core classes and functions in the Ebook Generator"
permalink: /api
---

# API Documentation
{: .no_toc }

This document provides detailed information about the core classes and functions in the Ebook Generator project.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Core Components

### NovelGenerator

The `NovelGenerator` class is the main engine for generating novels. It coordinates the generation process and manages the flow of information between different components.

#### Key Methods

- `initialize_novel(title, author, description, genre, target_audience, output_dir, series_manager=None, book_number=None)`: Sets up the novel generation process and initializes the memory manager.
- `generate_writer_profile()`: Creates a detailed profile of the fictional author.
- `generate_novel_outline(writer_profile)`: Generates a chapter-by-chapter outline based on genre conventions.
- `generate_characters()`: Creates detailed character profiles with backgrounds and arcs.
- `generate_chapter(chapter_num)`: Generates a single chapter with awareness of previous content.
- `set_generation_options(options)`: Sets custom generation options like chapter length and writing style.

### MemoryManager

The `MemoryManager` class maintains context across chapters for consistency. It stores and retrieves information about characters, plot points, and narrative elements.

#### Key Methods

- `add_character(character)`: Adds a character to the memory.
- `add_plot_point(plot_point)`: Adds a plot point to the memory.
- `add_chapter_summary(chapter_num, summary, word_count)`: Adds a chapter summary to the memory.
- `get_context_for_chapter(chapter_num)`: Gets the context needed for generating a specific chapter.
- `extract_narrative_elements(chapter_text, chapter_num, gemini)`: Extracts narrative elements from a chapter.
- `update_narrative_tracking(chapter_num, elements)`: Updates the tracking of narrative elements.

### GeminiClient

The `GeminiClient` class handles interactions with the Gemini API, including error handling and retry logic.

#### Key Methods

- `generate_content(prompt, temperature=0.7, max_tokens=8000)`: Generates content using the Gemini API.
- `clean_response(response)`: Cleans up the response from the API.
- `check_api_connection(check_all_keys=False)`: Checks the connection to the API.
- `rotate_api_key()`: Rotates to the next available API key.
- `get_api_key_status()`: Gets the status of all API keys.

### SeriesManager

The `SeriesManager` class manages series-related information and ensures consistency across books in a series.

#### Key Methods

- `initialize_series(title, description, genre, target_audience, planned_books, author)`: Initializes a new series.
- `load_series(series_dir)`: Loads an existing series.
- `add_book(book_data)`: Adds a book to the series.
- `get_series_info()`: Gets information about the series.
- `get_book_info(book_number)`: Gets information about a specific book in the series.

### SeriesGenerator

The `SeriesGenerator` class handles the generation of a complete series of novels.

#### Key Methods

- `initialize_series(title, description, genre, target_audience, planned_books, author)`: Initializes a new series.
- `generate_series_plan()`: Generates a plan for the entire series.
- `generate_book(book_template, book_number)`: Generates a single book in the series.

## Formatters

### EpubFormatter

The `EpubFormatter` class handles the formatting and creation of EPUB files.

#### Key Methods

- `format_epub(cover_path=None)`: Formats the novel as an EPUB.
- `save_epub(output_dir, cover_path=None)`: Saves the EPUB file to the specified directory.

## Utilities

### WordCounter

The `word_counter` module provides utilities for counting words and estimating reading time.

#### Key Functions

- `count_words(text)`: Counts the number of words in a text.
- `estimate_reading_time(word_count, words_per_minute=250)`: Estimates reading time based on word count.

### ChapterPlanner

The `chapter_planner` module provides utilities for planning chapters based on genre.

#### Key Functions

- `get_genre_guidelines(genre)`: Gets chapter and word count guidelines for a specific genre.
- `recommend_chapter_count(genre, target_length="medium")`: Recommends a chapter count based on genre and desired length.
- `get_chapter_structure_by_genre(genre)`: Gets recommended chapter structure based on genre.

### FileHandler

The `file_handler` module provides utilities for file operations.

#### Key Functions

- `create_output_directory(title, author)`: Creates an output directory for a novel.
- `save_novel_json(novel, output_dir)`: Saves novel data as JSON.
- `create_series_directory(series_title, author)`: Creates a directory for a series.

### GenreDefaults

The `genre_defaults` module provides default generation options based on genre.

#### Key Functions

- `get_genre_defaults(genre)`: Gets default generation options based on genre.

### CoverGenerator

The `CoverGenerator` class generates professional-looking book covers without external images.

#### Key Methods

- `generate_cover(title, author, genre, output_path=None, subtitle=None, series_info=None)`: Generates a cover image.
- `save_cover(image, output_path=None)`: Saves the cover image to the specified path.

## Related Documentation

- [Novel Generator](./components/novel-generator.html): Detailed documentation of the Novel Generator component
- [Memory Management](./components/memory-management.html): Information about the Memory Management System
- [Series Generation](./components/series-generation.html): Documentation for the Series Generation feature
- [EPUB Formatting](./components/epub-formatting.html): Details about the EPUB formatting process
- [Cover Generator](./components/cover-generator.html): Information about the Cover Generator component
