# NovelForge AI

An advanced AI-powered publishing platform that creates complete, professional-quality novels in EPUB format based on minimal user input. This sophisticated system uses Google's Gemini 2.0 Flash API to generate marketing-quality content and provides a rich, interactive terminal interface for enterprise-grade book creation.

## 🎉 **Latest Major Updates (v2.5)**

**Production-Ready Reliability & Advanced Features:**

- ✅ **Memory Leak Fix**: Eliminated unlimited memory growth during long operations
- ✅ **Network Resilience**: Bulletproof network handling with automatic retry and recovery
- ✅ **38+ Genre Support**: Comprehensive fiction, non-fiction, and special format genres
- ✅ **Genre-Aware EPUB Formatting**: Specialized layouts for poetry, cookbooks, technical manuals
- ✅ **AI-Generated Covers**: Professional covers using Gemini AI with genre-specific prompts
- ✅ **Writer Profile Images**: Fictional author portraits with AI-generated images
- ✅ **Fast Testing System**: 5-10 minute test cycles for rapid development
- ✅ **Front/Back Matter**: Professional title pages, copyright, author bios, TOC
- ✅ **API Key Management**: Advanced rotation and monitoring system
- ✅ **Enterprise-Grade Stability**: 90% reduction in generation failures

## 🌟 Features

### **Core Functionality**

- **Complete Novel Generation**: Create full novels from basic inputs (title, author, description, genre)
- **Series Generation**: Generate multi-book series with consistent characters and plot arcs across multiple books
- **38+ Genre Support**: Fiction, non-fiction, and special formats (poetry, cookbooks, technical manuals, etc.)
- **Smart Memory Management**: Maintains context across chapters with bounded memory usage
- **Genre-Aware EPUB Formatting**: Specialized layouts and styling for different content types
- **AI-Generated Covers**: Professional covers using Gemini AI with genre-specific visual prompts
- **Writer Profile System**: Fictional author personas with AI-generated portrait images

### **Reliability & Performance**

- **Network Resilience**: Automatic retry logic, request queuing, and circuit breaker protection
- **Memory Leak Prevention**: Bounded containers prevent unlimited memory growth
- **Error Recovery**: User-friendly error messages with actionable recovery suggestions
- **Multiple API Key Support**: Seamless rotation to handle rate limits during long generations

### **User Experience**

- **Rich Terminal UI**: Clean, colorful interface with real-time progress tracking
- **API Key Management**: Interactive management with automatic rotation and status monitoring
- **Network Status Monitoring**: Real-time network health diagnostics and recovery
- **Genre-Specific Recommendations**: Tailored chapter counts and structures for 38+ genres
- **Fast Testing System**: Rapid 5-10 minute test cycles for development and validation
- **Professional Output**: Complete books with front matter, back matter, and author sections

## 📋 Requirements

- Python 3.8+
- Google Gemini API key(s)
- Internet connection

## 🚀 Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/mosadd1X/novelforge-ai.git
   cd novelforge-ai
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
novelforge-ai/
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

1. **User Input**: Collect basic information about the novel (title, genre, description)
2. **Writer Profile**: Generate a detailed fictional author profile with AI-generated portrait
3. **Outline Creation**: Create a genre-appropriate chapter-by-chapter outline
4. **Character Development**: Generate detailed character profiles with relationships and arcs
5. **Chapter Generation**: Create each chapter with context awareness and memory consistency
6. **Memory Management**: Maintain narrative consistency across chapters with bounded memory
7. **Cover Generation**: Create professional cover using Gemini AI with genre-specific prompts
8. **Genre-Aware Formatting**: Apply specialized EPUB formatting based on content type
9. **Front/Back Matter**: Add professional title pages, copyright, author bio, and TOC
10. **Final Assembly**: Package everything into a complete, professional EPUB file

## 📖 Documentation

### **User Guides**

- [Getting Started](docs/getting-started.md): Complete setup and usage guide
- [Quick Start Guide](docs/quick-start.md): Generate your first book in minutes
- [Configuration Options](docs/configuration.md): Customize the generation process

### **Core Components**

- [Novel Generator](docs/components/novel-generator.md): Core generation system
- [Memory Management](docs/components/memory-management.md): Context and consistency management
- [Series Generation](docs/components/series-generation.md): Multi-book series creation
- [Cover Generator](docs/components/cover-generator.md): AI-powered cover creation
- [EPUB Formatting](docs/components/epub-formatting.md): Professional book formatting
- [Writer Profile System](docs/components/writer-profiles.md): Fictional author generation
- [Network Resilience](docs/components/network-resilience.md): Robust API handling

### **Advanced Features**

- [Genre-Aware EPUB Formatting](docs/advanced/genre-epub-formatting.md): Specialized layouts
- [Fast Testing System](docs/advanced/fast-testing.md): Rapid development testing
- [API Key Management](docs/api-key-management.md): Multiple key management

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

## 👨‍💻 Author

**Mosaddiq** - _Creator & Lead Developer_

- GitHub: [@mosadd1X](https://github.com/mosadd1X)
- Project: [NovelForge AI](https://github.com/mosadd1X/novelforge-ai)

## 🙏 Acknowledgments

- Google Gemini API for providing the AI capabilities
- The Rich library for the beautiful terminal interface
- The EbookLib library for EPUB generation
- All contributors who have helped improve this project
