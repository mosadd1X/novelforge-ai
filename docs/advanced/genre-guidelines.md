---
layout: default
title: Genre Guidelines
parent: Advanced Topics
nav_order: 1
description: "Detailed information about genre-specific settings and recommendations"
---

# Genre Guidelines
{: .no_toc }

The Ebook Generator uses genre-specific guidelines to tailor the generation process for different types of books.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Different literary genres have distinct conventions, structures, and reader expectations. The Ebook Generator's genre guidelines system ensures that generated books adhere to these conventions, resulting in more authentic and satisfying content.

The system includes guidelines for:
- Chapter count and length
- Word count ranges
- Narrative structure
- Character archetypes
- Plot patterns
- Stylistic elements
- Pacing recommendations

## Supported Genres

The Ebook Generator supports the following primary genres:

- Fantasy
- Science Fiction
- Mystery/Thriller
- Romance
- Literary Fiction
- Historical Fiction
- Young Adult
- Middle Grade
- Horror
- Adventure
- Commercial Fiction
- Test (for quick testing)

Each genre has customized generation parameters and content guidelines.

## Genre-Specific Parameters

### Fantasy

```
Chapter Range: 25-35 chapters
Word Count Range: 90,000-120,000 words
Chapter Length: 3,500-4,500 words
POV Style: Third person limited or omniscient
Pacing: Balanced with emphasis on world-building
```

Fantasy novels typically include:
- Detailed world-building
- Magic systems with consistent rules
- Character journeys and growth
- Conflict between good and evil forces
- Quests or missions

### Science Fiction

```
Chapter Range: 20-30 chapters
Word Count Range: 80,000-100,000 words
Chapter Length: 3,500-4,500 words
POV Style: Varies (first or third person)
Pacing: Concept-driven with action elements
```

Science Fiction novels typically include:
- Technological concepts and their implications
- Exploration of scientific ideas
- Social commentary through speculative elements
- Future or alternate worlds
- Human adaptation to new environments

### Mystery/Thriller

```
Chapter Range: 25-35 chapters
Word Count Range: 70,000-90,000 words
Chapter Length: 3,000-4,000 words
POV Style: First person or close third person
Pacing: Tense with strategic reveals
```

Mystery/Thriller novels typically include:
- Central mystery or threat
- Clues and red herrings
- Rising tension and stakes
- Character with investigative role
- Climactic revelation or confrontation

### Romance

```
Chapter Range: 20-25 chapters
Word Count Range: 65,000-85,000 words
Chapter Length: 3,500-4,000 words
POV Style: Alternating between protagonists
Pacing: Emotional development with obstacles
```

Romance novels typically include:
- Focus on relationship development
- Emotional conflicts and growth
- Character chemistry and attraction
- Obstacles to the relationship
- Satisfying emotional resolution

### Literary Fiction

```
Chapter Range: 15-25 chapters
Word Count Range: 70,000-90,000 words
Chapter Length: 3,500-5,000 words
POV Style: Varies (often deep third person)
Pacing: Character-driven with thematic focus
```

Literary Fiction typically includes:
- Complex character development
- Thematic depth and exploration
- Emphasis on prose quality
- Internal conflicts and growth
- Social or philosophical commentary

## Customizing Genre Guidelines

You can customize the genre guidelines by modifying the `genre_defaults.py` file in the `src/utils` directory:

```python
# Example of customizing the Fantasy genre defaults
GENRE_DEFAULTS = {
    "fantasy": {
        "target_length": "long",
        "writing_style": "Descriptive and immersive",
        "pov": "Third person limited",
        "themes": ["Good vs. evil", "Coming of age", "Power and responsibility"],
        "chapter_count": 30,
        "target_word_count": 100000,
        "chapter_length": 3500,
        "min_chapter_length": 3500,
    },
    # Other genres...
}
```

## Genre Mixing

The Ebook Generator supports genre mixing by combining elements from multiple genres. When specifying a mixed genre (e.g., "Science Fiction Mystery"), the system will:

1. Identify the primary genre (first mentioned)
2. Incorporate elements from the secondary genre
3. Adjust parameters to accommodate both genres

Example mixed genres:
- Science Fiction Romance
- Historical Fantasy
- Mystery Thriller
- Paranormal Romance
- Urban Fantasy

## Genre-Specific Prompts

The system uses different prompt templates based on the selected genre. These templates emphasize different elements:

### Fantasy Prompt Elements
- World-building details
- Magic system rules
- Character backgrounds and abilities
- Cultural and historical context

### Mystery Prompt Elements
- Clue placement and tracking
- Suspect development
- Tension building
- Logical progression of investigation

### Romance Prompt Elements
- Character chemistry and attraction
- Emotional development
- Relationship obstacles
- Character growth through relationship

## Test Genre

The system includes a special "Test" genre designed for quick testing of the generation pipeline:

```
Chapter Range: 3-5 chapters
Word Count Range: 9,000-12,000 words
Chapter Length: 3,000-4,000 words
POV Style: Simple third person
Pacing: Straightforward
```

This genre uses simplified prompts and reduced content requirements to allow for rapid testing of the system's functionality.

## Related Documentation

- [Configuration Options](../configuration.html): General configuration settings
- [Novel Generator](../components/novel-generator.html): Core generation component
- [Customizing Prompts](./customizing-prompts.html): How to modify generation prompts
