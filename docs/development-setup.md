---
layout: default
title: Development Setup
nav_order: 10
description: "Detailed instructions for setting up a development environment for the Ebook Generator"
permalink: /development-setup
---

# Development Setup
{: .no_toc }

This guide provides detailed instructions for setting up a development environment for the Ebook Generator.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Prerequisites

Before setting up the development environment, ensure you have the following prerequisites:

- **Python 3.8+** installed on your system
- **Git** for version control
- **pip** (Python package manager)
- **Google Gemini API key(s)** for testing
- A code editor or IDE (VS Code, PyCharm, etc.)

## Setting Up the Development Environment

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/mosadd1X/ebook-generator.git

# Navigate to the project directory
cd ebook-generator
```

### 2. Create a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
# Install development dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Copy the example environment file
cp .env.example .env
```

Edit the `.env` file to add your Gemini API key(s):

```
# Main API key (required)
GEMINI_API_KEY=your_main_api_key_here

# Additional API keys (optional)
GEMINI_API_KEY_1=your_second_api_key_here
GEMINI_API_KEY_2=your_third_api_key_here
```

## Development Tools

### Code Formatting

The project uses the following tools for code formatting:

- **Black**: For consistent code formatting
- **isort**: For sorting imports
- **flake8**: For linting

Install these tools:

```bash
pip install black isort flake8
```

Format your code before committing:

```bash
# Format with Black
black src tests

# Sort imports
isort src tests

# Lint with flake8
flake8 src tests
```

### Type Checking

The project uses **mypy** for type checking:

```bash
# Install mypy
pip install mypy

# Run type checking
mypy src
```

### Pre-commit Hooks

You can set up pre-commit hooks to automatically format and lint your code before committing:

```bash
# Install pre-commit
pip install pre-commit

# Install the pre-commit hooks
pre-commit install
```

## Project Structure

Understanding the project structure will help you navigate and contribute effectively:

```
ebook-generator/
├── docs/                       # Documentation
├── src/                        # Source code
│   ├── core/                   # Core functionality
│   │   ├── gemini_client.py    # Gemini API interface
│   │   ├── memory_manager.py   # Memory management
│   │   ├── novel_generator.py  # Novel generation
│   │   ├── series_generator.py # Series generation
│   │   └── series_manager.py   # Series management
│   ├── formatters/             # Output formatting
│   │   └── epub_formatter.py   # EPUB formatting
│   ├── ui/                     # User interface
│   │   ├── series_menu.py      # Series management menu
│   │   └── terminal_ui.py      # Terminal UI components
│   ├── utils/                  # Utilities
│   │   ├── chapter_planner.py  # Chapter planning
│   │   ├── cover_generator.py  # Cover generation
│   │   ├── file_handler.py     # File operations
│   │   ├── genre_defaults.py   # Genre defaults
│   │   └── word_counter.py     # Word counting
│   ├── __init__.py             # Package initialization
│   └── main.py                 # Main application entry point
├── tests/                      # Test suite
├── .env.example                # Example environment file
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## Running Tests

The project uses **pytest** for testing:

```bash
# Install pytest
pip install pytest pytest-cov

# Run tests
pytest

# Run tests with coverage
pytest --cov=src tests/
```

## Development Workflow

1. **Create a Branch**: Create a new branch for your feature or bugfix
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**: Implement your changes following the project's coding standards

3. **Run Tests**: Ensure your changes pass all tests
   ```bash
   pytest
   ```

4. **Format Code**: Format your code before committing
   ```bash
   black src tests
   isort src tests
   flake8 src tests
   ```

5. **Commit Changes**: Commit your changes with a clear message
   ```bash
   git commit -m "Add feature: description of the feature"
   ```

6. **Push Changes**: Push your branch to your fork
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create Pull Request**: Submit a pull request to the main repository

## Debugging

### Using the Python Debugger

You can use the Python debugger (pdb) to debug the application:

```python
import pdb

# Add a breakpoint
pdb.set_trace()
```

### Logging

The project uses the Python logging module. You can add logging statements to debug your code:

```python
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Add log statements
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
```

## Documentation

The project uses GitHub Pages with the Just the Docs theme for documentation. To preview the documentation locally:

1. Install Ruby and Bundler
2. Navigate to the `docs` directory
3. Install dependencies:
   ```bash
   bundle install
   ```
4. Start the local server:
   ```bash
   bundle exec jekyll serve
   ```
5. Open your browser to `http://localhost:4000`

## Related Documentation

- [Contributing Guidelines](./contributing.html): Guidelines for contributing to the project
- [Code Style Guide](./code-style.html): Specific code style requirements
- [API Documentation](./api.html): Reference for the project's API
