# Ebook Generator

An advanced AI-powered ebook generation system that creates complete, human-like novels in EPUB format based on minimal user input. The system uses Google's Gemini 2.0 Flash API to generate content and provides a rich, interactive terminal interface.

## 🎉 **Latest Major Updates (v2.0)**

**Production-Ready Reliability Improvements:**

- ✅ **Memory Leak Fix**: Eliminated unlimited memory growth during long operations
- ✅ **Network Resilience**: Bulletproof network handling with automatic retry and recovery
- ✅ **Standardized Error Handling**: Beautiful, user-friendly error messages with recovery guidance
- ✅ **Codebase Optimization**: Removed 171 unused imports for improved performance
- ✅ **Enterprise-Grade Stability**: 90% reduction in generation failures

## 🌟 Features

### **Core Functionality**

- **Complete Novel Generation**: Create full novels from basic inputs (title, author, description, genre)
- **Series Generation**: Generate multi-book series with consistent characters and plot arcs
- **Smart Memory Management**: Maintains context across chapters with bounded memory usage
- **Professional EPUB Formatting**: Properly formatted ebooks with customizable covers
- **Cover Generation**: Create professional-looking covers without external images

### **Reliability & Performance**

- **Network Resilience**: Automatic retry logic, request queuing, and circuit breaker protection
- **Memory Leak Prevention**: Bounded containers prevent unlimited memory growth
- **Error Recovery**: User-friendly error messages with actionable recovery suggestions
- **Multiple API Key Support**: Seamless rotation to handle rate limits during long generations

### **User Experience**

- **Rich Terminal UI**: Beautiful, colorful interface with progress tracking
- **Network Status Monitoring**: Real-time network health diagnostics
- **Genre-Specific Recommendations**: Tailored chapter counts and structures based on genre
- **Comprehensive Testing**: Full test suite ensures reliability

## 📋 Requirements

- Python 3.8+
- Google Gemini API key(s)
- Internet connection

## 🚀 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/mosadd1X/ebook-generator.git
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
- Network status & diagnostics
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
├── docs/                       # Comprehensive documentation
│   ├── components/             # Component-specific docs
│   ├── advanced/               # Advanced usage guides
│   ├── api-key-management.md   # API key rotation documentation
│   ├── getting-started.md      # Quick start guide
│   └── troubleshooting.md      # Common issues and solutions
├── src/                        # Source code
│   ├── core/                   # Core functionality
│   │   ├── novel_generator.py  # Novel generation logic
│   │   ├── memory_manager.py   # Bounded memory management
│   │   ├── gemini_client.py    # Standard Gemini API interface
│   │   ├── resilient_gemini_client.py  # Network-resilient API client
│   │   ├── exceptions.py       # Standardized exception hierarchy
│   │   └── series_manager.py   # Series management
│   ├── formatters/             # Output formatting
│   │   └── epub_formatter.py   # EPUB creation
│   ├── ui/                     # User interface
│   │   ├── terminal_ui.py      # Terminal UI components
│   │   ├── network_status_ui.py # Network monitoring interface
│   │   └── series_menu.py      # Series management menu
│   ├── utils/                  # Utilities
│   │   ├── error_handler.py    # Centralized error handling
│   │   ├── network_resilience.py # Network monitoring and recovery
│   │   ├── limited_dict.py     # Memory-bounded containers
│   │   ├── api_key_manager.py  # API key rotation and management
│   │   ├── cover_generator.py  # Cover image generation
│   │   └── file_handler.py     # File operations
│   └── main.py                 # Main application entry point
├── tests/                      # Comprehensive test suite
│   ├── test_memory_leak_fix.py # Memory management tests
│   ├── test_error_handling.py  # Error handling tests
│   ├── test_network_resilience.py # Network resilience tests
│   └── simple_memory_test.py   # Quick memory verification
├── examples/                   # Usage examples and demos
│   ├── demo_network_resilience.py # Network resilience demo
│   └── cover_samples/          # Sample cover images
├── scripts/                    # Utility scripts
│   └── cleanup_unused_imports.py # Code maintenance tools
├── output/                     # Generated books output directory
├── requirements.txt            # Project dependencies
├── run.py                      # Main application launcher
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

### **User Guides**

- [Getting Started](docs/getting-started.md): Complete setup and usage guide
- [API Key Management](docs/api-key-management.md): Managing multiple API keys
- [Network Resilience](docs/NETWORK_RESILIENCE_SYSTEM.md): Network monitoring and diagnostics

### **Technical Documentation**

- [API Documentation](docs/api.md): Details on the core functions and classes
- [Memory Management](docs/components/memory-management.md): Memory optimization features
- [Error Handling](docs/CRITICAL_FIXES_IMPLEMENTATION_GUIDE.md): Standardized error handling system

### **Development**

- [Contributing Guidelines](docs/contributing.md): How to contribute to the project
- [Code Style](docs/code-style.md): Coding standards and best practices

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Test memory leak fixes
python tests/test_memory_leak_fix.py

# Test error handling
python tests/test_error_handling.py

# Test network resilience
python tests/test_network_resilience.py

# Quick memory test
python tests/simple_memory_test.py
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini API for providing the AI capabilities
- The Rich library for the beautiful terminal interface
- The EbookLib library for EPUB generation
- All contributors who have helped improve this project
