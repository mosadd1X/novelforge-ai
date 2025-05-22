# Ebook Generator

An advanced AI-powered ebook generation system that creates complete, human-like novels in EPUB format based on minimal user input. The system uses Google's Gemini 2.0 Flash API to generate content and provides a rich, interactive terminal interface.

## 🌟 Features

- **Complete Novel Generation**: Create full novels from basic inputs (title, author, description, genre)
- **Series Generation**: Generate multi-book series with consistent characters and plot arcs
- **Smart Memory Management**: Maintains context across chapters for narrative consistency
- **Professional EPUB Formatting**: Properly formatted ebooks with customizable covers
- **Multiple API Key Support**: Automatic key rotation to handle rate limits during long generations
- **Genre-Specific Recommendations**: Tailored chapter counts and structures based on genre
- **Rich Terminal UI**: Colorful, interactive interface with progress tracking
- **Cover Generation**: Create professional-looking covers without external images

## 📋 Requirements

- Python 3.8+
- Google Gemini API key(s)
- Internet connection

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ebook-generator.git
   cd ebook-generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your API keys:
   - Copy `.env.example` to `.env`
   - Add your Gemini API key(s) to the `.env` file
   ```
   # Main API key (required)
   GEMINI_API_KEY=your_main_api_key_here

   # Additional API keys (optional)
   GEMINI_API_KEY_1=your_second_api_key_here
   GEMINI_API_KEY_2=your_third_api_key_here
   ```

## 📚 Usage

### Quick Start

Run the main menu interface:

```bash
python run.py
```

This provides a user-friendly menu with options to:
- Generate a single book
- Generate a series
- Check API key status
- Exit the application

### Direct Book Generation

To directly start the book generation process:

```bash
python -m src.main
```

### Series Management

For series management features:

```bash
python -m src.main --series-menu
```

## 📁 Project Structure

```
ebook-generator/
├── docs/                       # Documentation
│   ├── genere_guideline.md     # Genre guidelines and standards
│   ├── multiple_api_keys.md    # API key rotation documentation
│   ├── api.md                  # API documentation
│   └── contributing.md         # Contribution guidelines
├── src/                        # Source code
│   ├── core/                   # Core functionality
│   │   ├── novel_generator.py  # Novel generation logic
│   │   ├── memory_manager.py   # Context management
│   │   ├── gemini_client.py    # Gemini API interface
│   │   └── series_manager.py   # Series management
│   ├── formatters/             # Output formatting
│   │   └── epub_formatter.py   # EPUB creation
│   ├── ui/                     # User interface
│   │   ├── terminal_ui.py      # Terminal UI components
│   │   └── series_menu.py      # Series management menu
│   ├── utils/                  # Utilities
│   │   ├── word_counter.py     # Word counting
│   │   ├── chapter_planner.py  # Chapter planning
│   │   ├── file_handler.py     # File operations
│   │   ├── genre_defaults.py   # Genre-specific defaults
│   │   └── cover_generator.py  # Cover image generation
│   ├── data/                   # Data files
│   │   └── book_ideas.json     # Sample book ideas
│   └── main.py                 # Main application entry point
├── output/                     # Generated books output directory
├── .env                        # Environment variables (API keys)
├── .env.example                # Example environment file
├── requirements.txt            # Project dependencies
├── run.py                      # Simplified run script
├── CHANGELOG.md                # Version history
└── README.md                   # This file
```

## 🔄 How It Works

1. **User Input**: Collect basic information about the novel
2. **Writer Profile**: Generate a detailed fictional author profile
3. **Outline Creation**: Create a chapter-by-chapter outline based on genre
4. **Character Development**: Generate detailed character profiles
5. **Chapter Generation**: Create each chapter with context awareness
6. **Memory Management**: Maintain narrative consistency across chapters
7. **Cover Generation**: Create a professional cover image
8. **EPUB Formatting**: Format the novel as a properly structured EPUB

## 📖 Documentation

- [API Documentation](docs/api.md): Details on the core functions and classes
- [Multiple API Key Support](docs/multiple_api_keys.md): How to use multiple API keys
- [Contributing Guidelines](docs/contributing.md): How to contribute to the project

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini API for providing the AI capabilities
- The Rich library for the beautiful terminal interface
- The EbookLib library for EPUB generation
- All contributors who have helped improve this project
