---
layout: default
title: Core Components
nav_order: 4
has_children: true
description: "Documentation for the core components of the Ebook Generator system"
permalink: /components
---

# Core Components
{: .no_toc }

The Ebook Generator consists of several core components that work together to generate complete novels and series.
{: .fs-6 .fw-300 }

## Overview

The Ebook Generator is built with a modular architecture, where each component handles a specific aspect of the book generation process. This design allows for flexibility, maintainability, and the ability to extend or customize individual components.

### Key Components

- **[Novel Generator](./novel-generator.html)**: The main engine that coordinates the generation process
- **[Memory Management](./memory-management.html)**: Maintains context and consistency across chapters
- **[Series Generation](./series-generation.html)**: Handles the creation of multi-book series
- **[Cover Generator](./cover-generator.html)**: Creates professional-looking book covers
- **[EPUB Formatting](./epub-formatting.html)**: Formats the generated content into EPUB files

## Component Interactions

The components interact in a structured workflow:

1. The **Novel Generator** initializes the generation process and coordinates between components
2. The **Memory Manager** is created to track narrative elements and maintain consistency
3. Characters, plot points, and other narrative elements are generated and stored in memory
4. Chapters are generated sequentially, with the **Memory Manager** providing context
5. The **Cover Generator** creates a cover image based on the book's metadata
6. The **EPUB Formatter** compiles the generated content into a properly formatted ebook

For series generation, the **Series Manager** coordinates across multiple books, ensuring consistency throughout the series.

## Component Diagram

```
┌─────────────────┐     ┌─────────────────┐
│  Novel Generator │◄────┤  Series Manager │
└────────┬────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ Memory Manager  │◄────┤   Gemini API    │
└────────┬────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│ EPUB Formatter  │◄────┤ Cover Generator │
└─────────────────┘     └─────────────────┘
```

## Extending Components

Each component is designed to be extensible. You can:

- Customize the generation process by modifying the Novel Generator
- Enhance memory management with additional tracking capabilities
- Add new formatting options to the EPUB Formatter
- Create custom cover generation styles
- Implement new series planning strategies

For more information on extending the system, see [Extending the System](../advanced/extending-the-system.html).
