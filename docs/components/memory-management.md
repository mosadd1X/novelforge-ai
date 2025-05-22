---
layout: default
title: Memory Management
parent: Core Components
nav_order: 2
description: "Documentation for the Memory Management System that maintains context and consistency across chapters and books"
---

# Memory Management System
{: .no_toc }

The Memory Management System is a core component of the Ebook Generator that maintains context and consistency across chapters and books.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The Memory Manager tracks and provides access to:

- Character information and development
- Plot points and narrative arcs
- World-building elements and settings
- Previous chapter summaries and events
- Thematic elements and motifs
- Unresolved questions and plot threads

This information ensures that the generated content remains consistent and coherent throughout the novel or series.

## Key Components

### MemoryManager Class

The `MemoryManager` class is the central component that:

1. Stores and organizes novel metadata
2. Tracks characters and their development
3. Maintains plot continuity
4. Provides context for chapter generation
5. Extracts and updates narrative elements

### Memory Storage

The memory system stores information in:

- In-memory data structures during generation
- JSON files for persistence between sessions
- Structured context for the AI model

## How It Works

### Initialization

When a novel is initialized:

```python
memory_manager = generator.initialize_novel(
    title="The Mysterious Island",
    author="Jane Author",
    description="A thrilling adventure...",
    genre="Mystery",
    target_audience="Adult (18+)",
    output_dir="output/my_novel",
    series_manager=None,
    book_number=None
)
```

The Memory Manager:
1. Creates a memory structure for the novel
2. Stores basic metadata (title, author, genre, etc.)
3. Initializes empty collections for characters, plot points, etc.
4. Sets up the directory structure for persistent storage

### Character Tracking

When characters are generated:

```python
characters = generator.generate_characters()
```

The Memory Manager:
1. Stores each character's attributes (name, role, appearance, etc.)
2. Tracks their development throughout the novel
3. Maintains relationships between characters
4. Ensures consistent portrayal across chapters

### Plot Continuity

As the novel progresses:

1. Each chapter's key events are summarized and stored
2. Plot threads are tracked from introduction to resolution
3. Unresolved questions are maintained for future chapters
4. World-building elements are recorded for consistency

### Context Provision

When generating a chapter:

```python
chapter_text = generator.generate_chapter(chapter_num)
```

The Memory Manager:
1. Retrieves relevant context for the chapter
2. Provides information about previous chapters
3. Includes character details and their current state
4. Supplies unresolved plot threads and questions
5. Adds thematic elements and motifs

### Narrative Extraction

After a chapter is generated:

```python
narrative_elements = memory_manager.extract_narrative_elements(
    chapter_text, chapter_num, gemini_client
)
memory_manager.update_narrative_tracking(chapter_num, narrative_elements)
```

The Memory Manager:
1. Extracts key events, character developments, and plot advancements
2. Updates character states and relationships
3. Tracks resolved and new plot threads
4. Identifies new world-building elements
5. Updates the overall narrative state

## Memory Structure

The memory system organizes information in a structured format:

```
memory/
├── metadata.json           # Novel metadata
├── characters.json         # Character information
├── plot_points.json        # Plot points and arcs
├── chapter_summaries.json  # Summaries of each chapter
├── narrative_tracking.json # Tracking of narrative elements
└── world_building.json     # World-building elements
```

## Context Format

The context provided to the AI model includes:

1. **Basic Information**: Title, genre, target audience, etc.
2. **Previous Chapters**: Summaries of previous chapters
3. **Characters**: Details about relevant characters
4. **Plot Threads**: Active plot threads and their status
5. **Unresolved Questions**: Questions that need addressing
6. **Thematic Elements**: Themes and motifs to incorporate
7. **World-Building**: Established facts about the world

## Series Integration

For series, the Memory Manager:

1. Coordinates with the Series Manager to maintain consistency across books
2. Tracks character development throughout the series
3. Ensures plot continuity between books
4. Maintains world-building consistency

## API Reference

### Key Methods

- `add_character(character)`: Adds a character to memory
- `add_plot_point(plot_point)`: Adds a plot point to memory
- `add_chapter_summary(chapter_num, summary, word_count)`: Adds a chapter summary
- `get_context_for_chapter(chapter_num)`: Gets context for a specific chapter
- `extract_narrative_elements(chapter_text, chapter_num, gemini)`: Extracts narrative elements
- `update_narrative_tracking(chapter_num, elements)`: Updates narrative tracking
- `save_memory_files()`: Saves memory to disk
- `load_memory_files()`: Loads memory from disk

## Best Practices

For optimal use of the memory system:

1. **Initialize Properly**: Always initialize the novel with complete metadata
2. **Generate Characters First**: Characters form the foundation of the memory system
3. **Generate Chapters Sequentially**: The memory builds progressively
4. **Extract Narrative Elements**: Always extract and update after generating a chapter
5. **Save Memory Files**: Save memory files for persistence between sessions

## Troubleshooting

Common issues and solutions:

- **Inconsistent Characters**: Check character tracking in memory files
- **Plot Holes**: Review plot points and narrative tracking
- **Repetitive Information**: Ensure proper extraction of narrative elements
- **Missing Context**: Verify memory files are being properly loaded

## Advanced Usage

### Custom Memory Elements

You can add custom elements to the memory system:

```python
memory_manager.custom_memory["locations"] = {
    "mysterious_island": {
        "description": "A fog-shrouded island in the North Atlantic",
        "discovered_in_chapter": 2,
        "key_features": ["ancient ruins", "dense forest", "hidden caves"]
    }
}
```

### Memory Manipulation

For advanced control, you can directly manipulate memory:

```python
# Update a character's state
memory_manager.characters[0]["current_state"] = "injured in chapter 5"

# Add a new unresolved question
memory_manager.narrative_tracking["unresolved_questions"].append({
    "question": "Who left the mysterious note?",
    "introduced_in_chapter": 3
})
```

## Performance Considerations

The memory system is designed to be efficient, but consider:

1. Memory usage increases with novel length and complexity
2. Extraction of narrative elements requires API calls
3. Context size is optimized for the AI model's limitations
4. Persistent storage requires disk operations

## Related Components

- [Novel Generator](./novel-generator.html): Uses the memory system for chapter generation
- [Series Generation](./series-generation.html): Integrates with memory management for series consistency
- [API Documentation](../api.html): Details on the underlying API methods
