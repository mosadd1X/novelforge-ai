---
layout: default
title: Configuration Options
nav_order: 4
description: "Detailed documentation of the configuration options available in the Ebook Generator"
permalink: /configuration
---

# Configuration Options
{: .no_toc }

The Ebook Generator provides various configuration options to customize the generation process according to your preferences.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Environment Configuration

### API Keys

API keys are configured in the `.env` file in the project root:

```
# Main API key (required)
GEMINI_API_KEY=your_main_api_key_here

# Additional API keys (optional)
GEMINI_API_KEY_1=your_second_api_key_here
GEMINI_API_KEY_2=your_third_api_key_here
```

For more information on using multiple API keys, see the [Multiple API Keys](./multiple-api-keys.html) documentation.

### Output Directory

By default, generated books are saved to the `output/` directory in the project root. You can customize this by setting the `OUTPUT_DIR` environment variable in your `.env` file:

```
OUTPUT_DIR=/path/to/your/custom/output
```

## Generation Options

The Ebook Generator supports various options to customize the generation process. These can be set through the interactive UI or programmatically.

### Basic Options

| Option | Description | Default |
|--------|-------------|---------|
| `chapter_count` | Number of chapters in the novel | Based on genre |
| `target_word_count` | Target total word count for the novel | Based on genre |
| `chapter_length` | Target words per chapter | Based on genre |
| `writing_style` | Preferred writing style | "Descriptive and detailed" |
| `pov` | Point of view for narration | "Third person limited" |

### Advanced Options

| Option | Description | Default |
|--------|-------------|---------|
| `min_chapter_length` | Minimum words per chapter | 3500 |
| `temperature` | Creativity level (0.0-1.0) | 0.7 |
| `themes` | List of themes to emphasize | Based on genre |
| `pov_structure` | Structure for POV (single, alternating, etc.) | "single" |
| `pov_characters` | Characters to use as POV (for alternating) | [] |

## Setting Options Through the UI

When generating a book through the terminal UI, you'll be asked if you want to customize generation options:

```
Would you like to customize generation options? (y/n): y
```

If you select "yes," you'll be presented with a series of prompts to customize each option.

## Setting Options Programmatically

You can set generation options programmatically by passing a dictionary to the `set_generation_options` method:

```python
from src.core.novel_generator import NovelGenerator

generator = NovelGenerator()
generator.initialize_novel(
    title="The Quantum Garden",
    author="Dr. Elise Moreau",
    description="A physicist discovers a way to manipulate quantum particles...",
    genre="Science Fiction",
    target_audience="Adult (18+)",
    output_dir="output/quantum_garden"
)

# Set custom generation options
generator.set_generation_options({
    "chapter_count": 25,
    "target_word_count": 80000,
    "chapter_length": 3500,
    "writing_style": "Descriptive and lyrical",
    "pov": "Third person limited",
    "themes": ["Identity", "Technology ethics", "Human connection"],
    "temperature": 0.8
})
```

## Genre-Specific Defaults

The system uses different default options based on the selected genre. These defaults are defined in `src/utils/genre_defaults.py`.

### Example Genre Defaults

#### Fantasy

```python
"fantasy": {
    "target_length": "long",
    "writing_style": "Descriptive and immersive",
    "pov": "Third person limited",
    "themes": ["Good vs. evil", "Coming of age", "Power and responsibility"],
    "chapter_count": 30,
    "target_word_count": 100000,
    "chapter_length": 3500,
    "min_chapter_length": 3500,
}
```

#### Mystery

```python
"mystery": {
    "target_length": "medium",
    "writing_style": "Tense and suspenseful",
    "pov": "First person or third person limited",
    "themes": ["Justice", "Truth", "Deception"],
    "chapter_count": 25,
    "target_word_count": 75000,
    "chapter_length": 3500,
    "min_chapter_length": 3500,
}
```

## API Configuration

### Gemini API Settings

You can configure the Gemini API settings in your `.env` file:

```
# API settings
GEMINI_API_VERSION=v1
GEMINI_MODEL=gemini-1.5-flash
GEMINI_MAX_TOKENS=8000
GEMINI_TEMPERATURE=0.7
```

### Rate Limit Handling

You can configure how the system handles rate limits:

```
# Rate limit settings
RATE_LIMIT_WAIT_TIME=60  # Seconds to wait when rate limited
MAX_RETRIES=3            # Maximum number of retries
```

## EPUB Formatting Options

### Cover Options

You can configure cover generation options:

```
# Cover options
COVER_WIDTH=1600         # Cover width in pixels
COVER_HEIGHT=2400        # Cover height in pixels
INCLUDE_COVER=true       # Whether to include a cover
```

### Metadata Options

You can configure additional metadata for the EPUB:

```
# EPUB metadata
PUBLISHER_NAME="Your Publisher Name"
COPYRIGHT_TEXT="Copyright © 2024"
LANGUAGE="en"            # Language code
```

## Related Documentation

- [Getting Started](./getting-started.html): Initial setup instructions
- [Multiple API Keys](./multiple-api-keys.html): Using multiple API keys
- [Genre Guidelines](./advanced/genre-guidelines.html): Details on genre-specific settings
