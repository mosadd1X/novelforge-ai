"""
Test script to demonstrate the comprehensive logging system.
"""

import sys
import os
sys.path.append('..')

from rich.console import Console
from rich.panel import Panel

# Import the logging system
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from src.utils.logger import init_logger, close_logger, log_info, log_error, log_debug, log_warning

console = Console(markup=True)

def test_beautiful_logging_system():
    """Test the beautiful Rich-enhanced logging system."""

    console.print("[bold cyan]✨ Beautiful Rich Logging System Test[/bold cyan]")
    console.print("=" * 70)

    # Initialize beautiful logger
    logger = init_logger("DEBUG")

    # Test different log levels with beautiful formatting
    log_info("Testing beautiful logging system initialization")
    log_debug("This is a debug message with detailed information")
    log_warning("This is a warning message with beautiful colors")

    # Test logging with context
    log_info("Testing context logging with beautiful formatting",
             genre="Poetry Collection",
             title="Test Poetry Book",
             chapter_count=70,
             author="Test Author")

    # Test function logging with beautiful formatting
    logger.log_function_start("generate_poetry_collection",
                             genre="Poetry Collection",
                             poems=70,
                             theme="Nature and Love")

    import time
    time.sleep(0.5)  # Simulate some work

    logger.log_function_end("generate_poetry_collection",
                           result={"poems": 70, "total_words": 17500},
                           duration=2.34)

    # Test generation step logging with beautiful status indicators
    logger.log_generation_step("Writer Profile", "Poetry Collection", "Starting",
                              "Generating artistic profile for poetry collection")

    time.sleep(0.3)
    logger.log_generation_step("Writer Profile", "Poetry Collection", "Completed",
                              "Successfully created poetic writer profile")

    logger.log_generation_step("Novel Outline", "Poetry Collection", "In Progress",
                              "Creating structure for 70 poems")

    time.sleep(0.5)
    logger.log_generation_step("Novel Outline", "Poetry Collection", "Completed",
                              "Successfully generated 70 poem outlines")

    # Test beautiful API call logging
    logger.log_api_call("Gemini", "generateContent",
                       {
                           "prompt": "Generate a poetry collection outline with 70 poems about nature and love...",
                           "temperature": 0.7,
                           "max_tokens": 4000
                       },
                       "Success")

    # Test beautiful chapter progress logging
    console.print("\n[bold yellow]📚 Demonstrating Chapter Progress Logging:[/bold yellow]")
    for i in range(1, 8):
        logger.log_chapter_progress(i, 70, "Completed", word_count=200 + (i * 30))
        time.sleep(0.1)  # Small delay for visual effect

    logger.log_chapter_progress(8, 70, "Generating", word_count=0)
    logger.log_chapter_progress(9, 70, "Error", word_count=0)

    # Test beautiful error logging
    console.print("\n[bold yellow]🚨 Demonstrating Error Logging:[/bold yellow]")
    try:
        raise ValueError("This is a test error to demonstrate beautiful error formatting")
    except Exception as e:
        log_error("Test error occurred during poetry generation",
                 exception=e,
                 genre="Poetry Collection",
                 chapter=8,
                 operation="poem_generation")

    # Test critical error logging
    try:
        raise RuntimeError("This is a critical error demonstration")
    except Exception as e:
        logger.critical("Critical system failure during generation", exception=e)

    # Test memory usage logging
    logger.log_memory_usage("After poetry collection generation")

    # Get log file path
    log_file_path = logger.get_log_file_path()

    console.print(f"\n[bold green]✅ Beautiful logging test completed successfully![/bold green]")
    console.print(f"[bold yellow]📁 Log file created at: {log_file_path}[/bold yellow]")

    # Show log file contents preview
    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            log_content = f.read()

        console.print(f"\n[bold cyan]📄 Log File Preview (last 800 characters):[/bold cyan]")
        preview = log_content[-800:] if len(log_content) > 800 else log_content
        console.print(Panel(preview, title="Log File Content", border_style="cyan"))

        # Show file size
        file_size = os.path.getsize(log_file_path)
        console.print(f"\n[bold green]📊 Log file size: {file_size:,} bytes[/bold green]")

    except Exception as e:
        console.print(f"[bold red]❌ Could not read log file: {e}[/bold red]")

    # Close logger with beautiful session end
    close_logger()

    return log_file_path

def demonstrate_poetry_debugging():
    """Demonstrate how logging helps debug poetry generation issues."""

    console.print(f"\n\n[bold cyan]🐛 Poetry Generation Debugging Guide[/bold cyan]")
    console.print("=" * 70)

    debugging_steps = [
        {
            "step": "1. Check Log File Location",
            "description": "Look for the log file in the 'logs' directory",
            "what_to_look_for": "File path will be shown when generation starts"
        },
        {
            "step": "2. Monitor Generation Steps",
            "description": "Track each phase of poetry collection generation",
            "what_to_look_for": "GENERATION STEP entries for Writer Profile, Novel Outline, Characters, Chapters"
        },
        {
            "step": "3. Check API Calls",
            "description": "Verify Gemini API requests and responses",
            "what_to_look_for": "API CALL entries with request/response details and status"
        },
        {
            "step": "4. Examine JSON Parsing",
            "description": "Look for JSON parsing issues in outline generation",
            "what_to_look_for": "JSON parsing indices, response previews, parsing errors"
        },
        {
            "step": "5. Track Memory Usage",
            "description": "Monitor memory consumption during generation",
            "what_to_look_for": "MEMORY USAGE entries showing MB consumption"
        },
        {
            "step": "6. Review Error Messages",
            "description": "Check for exceptions and error details",
            "what_to_look_for": "ERROR and CRITICAL entries with full stack traces"
        }
    ]

    for step_info in debugging_steps:
        console.print(f"\n[bold yellow]{step_info['step']}:[/bold yellow]")
        console.print(f"  Description: {step_info['description']}")
        console.print(f"  What to look for: {step_info['what_to_look_for']}")

    console.print(f"\n[bold green]🔍 Common Poetry Generation Issues to Check:[/bold green]")
    common_issues = [
        "API timeout or rate limiting (check API CALL entries)",
        "JSON parsing failures (check JSON parsing error messages)",
        "Memory exhaustion (check MEMORY USAGE entries)",
        "Invalid outline structure (check outline validation logs)",
        "Character generation skipping (check smart character logic)",
        "Chapter count validation failures (check chapter count logs)"
    ]

    for issue in common_issues:
        console.print(f"  • {issue}")

def show_log_analysis_tips():
    """Show tips for analyzing log files."""

    console.print(f"\n\n[bold cyan]📊 Log Analysis Tips[/bold cyan]")
    console.print("=" * 70)

    tips = [
        {
            "category": "🔍 Finding Issues",
            "tips": [
                "Search for 'ERROR' or 'CRITICAL' entries first",
                "Look for 'Exception:' to find error details",
                "Check timestamps to see where generation stops",
                "Look for 'FUNCTION START' without matching 'FUNCTION END'"
            ]
        },
        {
            "category": "⚡ Performance Analysis",
            "tips": [
                "Check 'Duration:' entries to find slow operations",
                "Monitor 'MEMORY USAGE' to detect memory leaks",
                "Look at 'API CALL' frequency for rate limiting",
                "Check 'PERFORMANCE' metrics for bottlenecks"
            ]
        },
        {
            "category": "🎯 Poetry-Specific Issues",
            "tips": [
                "Verify 'Skip characters' message appears for poetry",
                "Check outline generation for 70+ chapter handling",
                "Look for compact UI activation messages",
                "Monitor JSON parsing for large responses"
            ]
        }
    ]

    for tip_category in tips:
        console.print(f"\n[bold yellow]{tip_category['category']}:[/bold yellow]")
        for tip in tip_category['tips']:
            console.print(f"  • {tip}")

if __name__ == "__main__":
    log_file_path = test_beautiful_logging_system()
    demonstrate_poetry_debugging()
    show_log_analysis_tips()

    console.print(f"\n[bold cyan]✨ Beautiful Rich Logging System Ready![/bold cyan]")
    console.print("=" * 70)
    console.print(f"[bold green]✅ Beautiful Rich-enhanced logging system implemented[/bold green]")
    console.print(f"[bold green]✅ Stunning terminal output with colors, panels, and progress bars[/bold green]")
    console.print(f"[bold green]✅ Debug information captured in: {log_file_path}[/bold green]")
    console.print(f"[bold green]✅ Ready to debug poetry collection generation with style![/bold green]")

    console.print(f"\n[bold yellow]📝 Next Steps:[/bold yellow]")
    console.print("1. Run your poetry collection generation")
    console.print("2. Enjoy the beautiful terminal output with Rich formatting")
    console.print("3. Check the log file for detailed information")
    console.print("4. Look for beautiful error panels and progress indicators")
    console.print("5. Share the relevant log entries for further analysis")
