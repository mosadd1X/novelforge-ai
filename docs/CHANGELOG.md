# Changelog

All notable changes to the Ebook Generator will be documented in this file.

## [Unreleased]

### Added
- Comprehensive documentation in the docs/ directory
- API documentation for core components
- Contributing guidelines
- Setup.py for package installation
- .gitignore file for better version control

### Changed
- Improved project structure with better organization
- Enhanced docstrings throughout the codebase
- Consistent import organization
- Updated README with more detailed instructions
- Renamed from "Novel Generation System" to "Ebook Generator"

### Removed
- Redundant and temporary files
- Duplicate code and backups

## [0.2.0] - 2025-05-20

### Added
- Series generation support with multiple books
- Enhanced character generation with better JSON parsing
- Fallback mechanisms for malformed API responses
- Improved error handling and user feedback
- Support for maintaining character consistency across series
- Automatic series metadata management
- Book numbering and organization in series
- Interactive series management menu

### Fixed
- Fixed character generation to handle various response formats
- Improved error handling in Gemini API interactions
- Fixed JSON parsing issues in character generation
- Enhanced memory management for series generation
- Fixed issues with character consistency across chapters
- Improved handling of long-running generation processes

## [0.1.1] - 2024-05-20

### Added
- Initial project structure with modular organization under `src/` directory
- Core novel generation functionality using Gemini 2.0 Flash API
- Memory management system for maintaining context across chapters
- EPUB formatting with proper HTML structure
- Rich terminal UI with colorful output
- Interactive questionnaire for user input
- Genre-specific recommendations based on `genere_guideline.md`
- Writer profile generation
- Novel outline generation
- Character generation
- Chapter generation with context awareness
- Support for different writing styles and POVs
- Automatic EPUB file creation with proper formatting
- Error handling for API responses and display issues

### Features
- **Modular Structure**: Organized code in a clean, modular structure under `src/` directory
- **Genre Defaults**: Added utility to provide default generation options based on genre
- **Memory Management**: Implemented a system to maintain context across chapters for consistency
- **Rich UI**: Created a colorful, interactive terminal interface
- **EPUB Formatting**: Implemented proper EPUB formatting with HTML structure
- **Error Handling**: Added robust error handling throughout the application

### Technical Details
- Created the following modules:
  - `src/core/novel_generator.py`: Core novel generation logic
  - `src/core/memory_manager.py`: Context and memory management
  - `src/core/gemini_client.py`: Interface with Gemini API
  - `src/formatters/epub_formatter.py`: EPUB file creation and formatting
  - `src/utils/word_counter.py`: Word count utilities
  - `src/utils/chapter_planner.py`: Chapter recommendation based on genre
  - `src/utils/file_handler.py`: File operations
  - `src/utils/genre_defaults.py`: Default settings based on genre
  - `src/ui/terminal_ui.py`: Rich terminal UI components
  - `src/main.py`: Entry point for the application

## [0.1.1] - 2024-05-20

### Fixed
- Fixed issue with rendering dictionaries in the terminal UI
- Enhanced error handling for Gemini API responses
- Added proper type checking and conversion for displayed values
- Added try-except blocks around display functions
- Improved error messages to be more informative
- Enhanced Gemini API response handling for different response formats
- Fixed duplicate banner display in the terminal UI

### Changed
- Modified `display_writer_profile()` to properly convert dictionary values to strings
- Updated `display_characters()` to handle complex data types
- Enhanced `generate_content()` to handle different response formats
- Added support for responses with parts in the Gemini client
- Improved error messages from the API client
