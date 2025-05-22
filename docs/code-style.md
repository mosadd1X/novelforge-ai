---
layout: default
title: Code Style Guide
nav_order: 11
description: "Code style guidelines for contributing to the Ebook Generator project"
permalink: /code-style
---

# Code Style Guide
{: .no_toc }

This document outlines the code style guidelines for contributing to the Ebook Generator project.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Python Style Guide

The Ebook Generator project follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code with some additional project-specific guidelines.

### General Guidelines

- Use 4 spaces for indentation (no tabs)
- Maximum line length of 100 characters
- Use meaningful variable and function names
- Follow the principle of "Explicit is better than implicit"
- Keep functions and methods focused on a single responsibility
- Limit the use of global variables

### Naming Conventions

- **Classes**: Use `CamelCase` for class names
  ```python
  class NovelGenerator:
      pass
  ```

- **Functions and Variables**: Use `snake_case` for function and variable names
  ```python
  def generate_chapter(chapter_num):
      chapter_content = "Chapter content"
      return chapter_content
  ```

- **Constants**: Use `UPPER_CASE` for constants
  ```python
  DEFAULT_CHAPTER_COUNT = 20
  MAX_RETRIES = 3
  ```

- **Private Methods and Variables**: Use a leading underscore for private methods and variables
  ```python
  def _internal_helper_method(self):
      self._private_variable = "Private"
  ```

### Imports

- Organize imports into three groups, separated by a blank line:
  1. Standard library imports
  2. Third-party imports
  3. Local application imports

- Within each group, sort imports alphabetically

```python
# Standard library imports
import json
import os
import sys
from typing import Dict, List, Optional

# Third-party imports
import questionary
from rich.console import Console
from rich.progress import Progress

# Local application imports
from src.core.memory_manager import MemoryManager
from src.utils.file_handler import create_output_directory
```

### Docstrings

All modules, classes, and functions should have docstrings following the [Google style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings):

```python
def generate_chapter(chapter_num: int, context: Dict[str, any]) -> str:
    """
    Generate a single chapter with the given context.
    
    Args:
        chapter_num: The chapter number to generate
        context: Dictionary containing context information for the chapter
        
    Returns:
        The generated chapter text
        
    Raises:
        ValueError: If chapter_num is less than 1
        RuntimeError: If generation fails after multiple retries
    """
    # Function implementation
```

### Type Annotations

Use type annotations for function parameters and return values:

```python
def count_words(text: str) -> int:
    """Count the number of words in a text."""
    return len(text.split())

def get_characters(names: List[str] = None) -> Dict[str, Dict[str, any]]:
    """Get character information for the given names."""
    # Function implementation
```

## Code Formatting Tools

The project uses the following tools for code formatting:

### Black

[Black](https://black.readthedocs.io/) is used for automatic code formatting:

```bash
# Format a single file
black src/main.py

# Format all files in a directory
black src tests
```

### isort

[isort](https://pycqa.github.io/isort/) is used for sorting imports:

```bash
# Sort imports in a single file
isort src/main.py

# Sort imports in all files in a directory
isort src tests
```

### flake8

[flake8](https://flake8.pycqa.org/) is used for linting:

```bash
# Lint a single file
flake8 src/main.py

# Lint all files in a directory
flake8 src tests
```

## Project-Specific Guidelines

### Error Handling

- Use specific exception types rather than catching all exceptions
- Include meaningful error messages
- Log exceptions with appropriate context
- Implement retry logic for transient errors (e.g., API rate limits)

```python
try:
    response = api_client.generate_content(prompt)
except RateLimitError as e:
    logger.warning(f"Rate limit exceeded: {e}. Retrying in {wait_time} seconds.")
    time.sleep(wait_time)
    response = api_client.generate_content(prompt)
except ApiError as e:
    logger.error(f"API error: {e}")
    raise RuntimeError(f"Failed to generate content: {e}")
```

### Logging

- Use the Python logging module for all logging
- Configure appropriate log levels based on the message importance
- Include context information in log messages
- Avoid logging sensitive information

```python
import logging

logger = logging.getLogger(__name__)

logger.debug("Detailed information for debugging")
logger.info("General information about program execution")
logger.warning("Warning about potential issues")
logger.error("Error that doesn't prevent the program from running")
logger.critical("Critical error that prevents the program from continuing")
```

### Configuration

- Use environment variables for configuration that varies by environment
- Use constants for configuration that doesn't change
- Document all configuration options
- Provide sensible defaults

```python
# Environment variables
API_KEY = os.environ.get("GEMINI_API_KEY")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "output")

# Constants
DEFAULT_CHAPTER_COUNT = 20
MAX_RETRIES = 3
```

### Testing

- Write unit tests for all functions and methods
- Use pytest for testing
- Mock external dependencies
- Aim for high test coverage
- Include both positive and negative test cases

```python
def test_count_words():
    """Test the count_words function."""
    # Positive test case
    assert count_words("Hello world") == 2
    
    # Edge cases
    assert count_words("") == 0
    assert count_words("   ") == 0
    
    # Special characters
    assert count_words("Hello, world!") == 2
```

## Related Documentation

- [Contributing Guidelines](./contributing.html): Guidelines for contributing to the project
- [Development Setup](./development-setup.html): Setting up the development environment
- [API Documentation](./api.html): Reference for the project's API
