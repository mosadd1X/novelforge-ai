---
layout: default
title: Getting Started
nav_order: 2
description: "Installation and setup instructions for the Ebook Generator"
---

# Getting Started
{: .no_toc }

This guide will help you install and set up the Ebook Generator system on your machine.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Prerequisites

Before installing the Ebook Generator, ensure you have the following prerequisites:

- **Python 3.8+** installed on your system
- **Google Gemini API key(s)** - [Get API keys here](https://ai.google.dev/)
- **Internet connection** for API access
- **Git** (optional, for cloning the repository)

## Installation

### Option 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/mosadd1X/ebook-generator.git

# Navigate to the project directory
cd ebook-generator

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Install via pip

```bash
# Install from PyPI
pip install ebook-generator

# Or install directly from GitHub
pip install git+https://github.com/mosadd1X/ebook-generator.git
```

## Configuration

### API Keys Setup

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file in your preferred text editor and add your Gemini API key(s):
   ```
   # Main API key (required)
   GEMINI_API_KEY=your_main_api_key_here

   # Additional API keys (optional)
   GEMINI_API_KEY_1=your_second_api_key_here
   GEMINI_API_KEY_2=your_third_api_key_here
   ```

3. Save the file

For more information on using multiple API keys, see the [Multiple API Keys](./multiple-api-keys.html) documentation.

### Output Directory

By default, generated books are saved to the `output/` directory in the project root. You can customize this location by:

1. Creating a custom output directory:
   ```bash
   mkdir -p /path/to/your/custom/output
   ```

2. Specifying the directory when generating books (through the UI or programmatically)

## Running the Application

### Using the Command Line Interface

The simplest way to start the application is using the provided run script:

```bash
python run.py
```

This will launch the main menu interface with options to:
- Generate a single book
- Generate a series
- Check API key status
- Exit the application

### Direct Module Execution

You can also run specific modules directly:

```bash
# Start the main book generation process
python -m src.main

# Launch the series management menu
python -m src.main --series-menu

# Auto-generate a series (for testing)
python -m src.main --auto-series
```

## Verifying Installation

To verify that your installation is working correctly:

1. Run the application:
   ```bash
   python run.py
   ```

2. Select "API Key Status" from the main menu

3. Confirm that your API key(s) are valid and working

If you encounter any issues, check the [Troubleshooting](./troubleshooting.html) guide.

## Next Steps

Now that you have installed and configured the Ebook Generator, you can:

- Follow the [Quick Start Guide](./quick-start.html) to generate your first book
- Learn about [Configuration Options](./configuration.html) to customize the generation process
- Explore the [Core Components](./components/novel-generator.html) to understand how the system works

---

## System Requirements

For optimal performance, we recommend:

- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **Processor**: Multi-core processor (4+ cores recommended for faster generation)
- **Memory**: 8GB RAM minimum, 16GB recommended
- **Storage**: 1GB free space for the application and dependencies, plus additional space for generated books
- **Internet**: Broadband connection for API access
