---
layout: default
title: Genre-Aware EPUB Formatting
parent: Advanced Features
nav_order: 1
description: "Documentation of the Genre-Aware EPUB Formatting system for specialized book layouts"
---

# Genre-Aware EPUB Formatting
{: .no_toc }

The Genre-Aware EPUB Formatting system provides specialized formatting and layout optimizations for different book genres, ensuring that each type of content is presented in the most appropriate and professional manner.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The Genre-Aware EPUB Formatting system automatically detects the genre of your book and applies appropriate formatting, styling, and layout optimizations. This ensures that poetry collections look like poetry collections, cookbooks have proper recipe formatting, and technical manuals have appropriate code highlighting.

### Supported Genres

The system provides specialized formatting for 8 special format genres:

- **Poetry Collection**: Centered titles, preserved line breaks, stanza spacing
- **Cookbook**: Recipe formatting, ingredient lists, instruction steps
- **Technical Manual**: Code highlighting, technical diagrams, structured layouts
- **Children's Book**: Large fonts, simple layouts, illustration support
- **Academic Textbook**: Citations, footnotes, academic formatting
- **Art Book**: Image galleries, caption formatting, visual layouts
- **Travel Guide**: Maps, itineraries, location-based organization
- **Reference Manual**: Index support, cross-references, structured navigation

## How It Works

### Automatic Genre Detection

The system automatically detects the genre and applies appropriate formatting:

```python
from src.utils.epub_formatter import EpubFormatter

# Automatic genre detection and formatting
novel_data = {
    "metadata": {"genre": "Poetry Collection", ...},
    "chapters": [{"content": "**Poem Title**\n\nVerse content...", ...}]
}

formatter = EpubFormatter(novel_data)  # Automatically detects poetry format
epub_path = formatter.save_epub(output_dir)  # Generates poetry-formatted EPUB
```

### Genre-Specific CSS

Each genre receives specialized CSS styling:

```css
/* Poetry Collection CSS */
.poem-title {
    text-align: center;
    font-weight: bold;
    margin: 2em 0 1em 0;
    font-size: 1.2em;
}

.poem-content {
    white-space: pre-line;
    text-align: left;
    margin: 1em 2em;
    line-height: 1.6;
}

.stanza-break {
    margin: 1.5em 0;
}
```

### Content Processing

Content is processed according to genre-specific rules:

```python
# Poetry-specific processing
def process_poetry_content(content):
    # Preserve line breaks and spacing
    content = preserve_line_breaks(content)
    # Center poem titles
    content = format_poem_titles(content)
    # Add stanza spacing
    content = add_stanza_spacing(content)
    return content
```

## Genre-Specific Features

### Poetry Collection

**Formatting Features:**
- Centered poem titles with elegant typography
- Preserved line breaks and indentation
- Proper stanza spacing and visual separation
- Support for different poetry forms (sonnets, haikus, free verse)

**CSS Optimizations:**
- Responsive typography that works on all devices
- Proper line height for readability
- Elegant spacing between poems and stanzas

### Cookbook

**Formatting Features:**
- Structured recipe layouts with clear sections
- Formatted ingredient lists with proper alignment
- Step-by-step instruction formatting
- Cooking time and serving information display

**Content Processing:**
- Automatic detection of ingredients lists
- Numbered instruction steps
- Cooking time and temperature highlighting

### Technical Manual

**Formatting Features:**
- Syntax highlighting for code blocks
- Structured layouts for technical content
- Support for diagrams and technical illustrations
- Cross-reference navigation

**CSS Optimizations:**
- Monospace fonts for code sections
- Proper indentation and spacing
- Technical diagram support

### Children's Book

**Formatting Features:**
- Large, child-friendly fonts
- Simple, clean layouts
- Support for illustrations and images
- Easy navigation for young readers

**Accessibility:**
- High contrast text
- Simple navigation
- Screen reader optimization

## Configuration

### Genre Detection Settings

Configure how genres are detected and processed:

```python
GENRE_FORMATTING_CONFIG = {
    "auto_detect": True,
    "fallback_to_default": True,
    "custom_css_override": False,
    "preserve_manual_formatting": True
}
```

### Custom Genre Formatting

Define custom formatting for specific genres:

```python
CUSTOM_GENRE_FORMATS = {
    "custom_poetry": {
        "css_template": "custom_poetry.css",
        "content_processor": "custom_poetry_processor",
        "layout_type": "poetry_centered"
    }
}
```

### CSS Customization

Override default CSS for specific genres:

```python
# Custom CSS for poetry collections
POETRY_CUSTOM_CSS = """
.poem-title {
    color: #2c3e50;
    font-family: 'Georgia', serif;
    text-align: center;
    margin: 3em 0 2em 0;
}

.poem-content {
    font-family: 'Times New Roman', serif;
    line-height: 1.8;
    text-align: left;
    margin: 1.5em 3em;
}
"""
```

## Usage Examples

### Poetry Collection

```python
# Generate a poetry collection with specialized formatting
novel_data = {
    "metadata": {
        "title": "Whispers of the Wind",
        "author": "Elena Rodriguez",
        "genre": "Poetry Collection"
    },
    "chapters": [
        {
            "title": "Nature's Voice",
            "content": """
**Morning Dew**

Glistening drops on emerald leaves,
Nature's tears of joy,
Silent witnesses to dawn's embrace,
Whispering secrets to the wind.

**Sunset Symphony**

Colors dance across the sky,
Orange, pink, and gold,
A masterpiece painted by time,
As day surrenders to night.
"""
        }
    ]
}

formatter = EpubFormatter(novel_data)
epub_path = formatter.save_epub("output/poetry")
```

### Cookbook

```python
# Generate a cookbook with recipe formatting
novel_data = {
    "metadata": {
        "title": "Mediterranean Delights",
        "author": "Chef Maria Santos",
        "genre": "Cookbook"
    },
    "chapters": [
        {
            "title": "Appetizers",
            "content": """
# Greek Hummus

**Prep Time:** 15 minutes  
**Serves:** 4-6

## Ingredients:
- 1 can (15 oz) chickpeas, drained and rinsed
- 1/4 cup fresh lemon juice
- 1/4 cup tahini
- 1 small garlic clove, minced
- 2 tablespoons extra-virgin olive oil
- 1/2 teaspoon ground cumin
- Salt to taste

## Instructions:
1. In a food processor, combine tahini and lemon juice. Process for 1 minute.
2. Add olive oil, minced garlic, cumin, and 1/2 teaspoon salt. Process for 30 seconds.
3. Add half the chickpeas and process for 1 minute.
4. Add remaining chickpeas and process until smooth, 1-2 minutes.
5. Taste and adjust seasoning as needed.
6. Serve with pita bread and vegetables.
"""
        }
    ]
}

formatter = EpubFormatter(novel_data)
epub_path = formatter.save_epub("output/cookbook")
```

### Technical Manual

```python
# Generate a technical manual with code formatting
novel_data = {
    "metadata": {
        "title": "Python Programming Guide",
        "author": "Dr. James Chen",
        "genre": "Technical Manual"
    },
    "chapters": [
        {
            "title": "Getting Started",
            "content": """
# Python Basics

## Variables and Data Types

Python supports several built-in data types:

```python
# String
name = "Hello, World!"

# Integer
age = 25

# Float
price = 19.99

# Boolean
is_active = True

# List
numbers = [1, 2, 3, 4, 5]

# Dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
```

## Functions

Define functions using the `def` keyword:

```python
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)  # Output: Hello, Alice!
```
"""
        }
    ]
}

formatter = EpubFormatter(novel_data)
epub_path = formatter.save_epub("output/technical")
```

## Advanced Features

### Custom Content Processors

Create custom content processors for specialized formatting:

```python
def custom_poetry_processor(content, metadata):
    """Custom processor for poetry content."""
    # Add custom poetry formatting logic
    content = add_poem_numbers(content)
    content = format_special_poetry_forms(content)
    content = add_poetry_navigation(content)
    return content

# Register custom processor
register_content_processor("Poetry Collection", custom_poetry_processor)
```

### Dynamic CSS Generation

Generate CSS dynamically based on content:

```python
def generate_dynamic_css(genre, content_analysis):
    """Generate CSS based on content analysis."""
    css = base_css_for_genre(genre)
    
    if content_analysis.has_long_lines:
        css += ".content { font-size: 0.9em; }"
    
    if content_analysis.has_many_images:
        css += ".image { max-width: 100%; height: auto; }"
    
    return css
```

### Multi-Genre Support

Handle books that span multiple genres:

```python
# Book with mixed content types
novel_data = {
    "metadata": {
        "genre": "Mixed",
        "sub_genres": ["Poetry Collection", "Essay Collection"]
    },
    "chapters": [
        {"type": "poetry", "content": "..."},
        {"type": "essay", "content": "..."}
    ]
}

# Formatter applies appropriate styling per chapter
formatter = EpubFormatter(novel_data, multi_genre=True)
```

## Best Practices

### Content Structure

- **Consistent Formatting**: Use consistent markdown/HTML structure
- **Clear Hierarchy**: Maintain clear heading hierarchy
- **Semantic Markup**: Use semantic HTML elements when possible

### CSS Design

- **Responsive Design**: Ensure formatting works on all devices
- **Accessibility**: Follow accessibility guidelines for text and colors
- **Performance**: Optimize CSS for fast loading

### Testing

- **Multiple Devices**: Test EPUB files on various e-readers
- **Validation**: Use EPUB validation tools
- **User Testing**: Get feedback from actual readers

## Troubleshooting

### Common Issues

**Formatting Not Applied**
- Verify genre is correctly detected
- Check if custom CSS is overriding default styles
- Ensure content structure matches expected format

**CSS Not Loading**
- Verify CSS file paths in EPUB structure
- Check for CSS syntax errors
- Ensure proper EPUB packaging

**Content Processing Errors**
- Review content processor logs
- Verify input content format
- Check for special characters or encoding issues

## Related Documentation

- [EPUB Formatting](../components/epub-formatting.html): General EPUB formatting
- [Configuration Options](../configuration.html): Configuring formatting options
- [Novel Generator](../components/novel-generator.html): How formatting integrates with generation
- [Front and Back Matter](./front-back-matter.html): Professional book structure

---

The Genre-Aware EPUB Formatting system ensures that every book is formatted professionally according to its genre conventions, providing readers with the best possible reading experience.
