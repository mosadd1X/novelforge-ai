"""
Beautiful Rich-based logging system for the Ebook Generator.

This module provides stunning terminal logging with colors, panels, progress bars,
and beautiful formatting using the Rich library.
"""

import logging
import os
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Optional, Any, Dict
import json

from rich.console import Console
from rich.logging import RichHandler
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich import box

class EbookLogger:
    """Beautiful Rich-enhanced logger for the Ebook Generator with stunning terminal output."""

    def __init__(self, log_level: str = "INFO"):
        """Initialize the beautiful logger with Rich console and file output."""
        self.log_level = getattr(logging, log_level.upper(), logging.INFO)
        self.logger = None
        self.log_file_path = None
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Rich console for beautiful output
        self.console = Console(record=True, width=120, markup=True)
        self.rich_console = Console(markup=True)

        # Session tracking
        self.session_stats = {
            "start_time": datetime.now(),
            "operations": 0,
            "errors": 0,
            "warnings": 0,
            "api_calls": 0,
            "current_operation": None
        }

        self.setup_logger()

    def setup_logger(self):
        """Set up the beautiful Rich-enhanced logger."""
        # Create logs directory if it doesn't exist
        logs_dir = Path("logs")
        logs_dir.mkdir(exist_ok=True)

        # Create log file with timestamp
        self.log_file_path = logs_dir / f"ebook_generator_{self.session_id}.log"

        # Create logger with Rich handler
        self.logger = logging.getLogger("EbookGenerator")
        self.logger.setLevel(self.log_level)

        # Clear any existing handlers
        self.logger.handlers.clear()

        # Rich console handler for beautiful terminal output
        rich_handler = RichHandler(
            console=self.rich_console,
            show_time=True,
            show_level=True,
            show_path=False,
            rich_tracebacks=True,
            tracebacks_show_locals=True,
            markup=True,
            log_time_format="[%H:%M:%S]"
        )
        rich_handler.setLevel(logging.INFO)  # Show info and above in terminal

        # File handler for detailed logging
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(name)s | %(funcName)s:%(lineno)d | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler = logging.FileHandler(self.log_file_path, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)

        # Add handlers to logger
        self.logger.addHandler(rich_handler)
        self.logger.addHandler(file_handler)

        # Display beautiful session start
        self._display_session_start()

    def _display_session_start(self):
        """Display a beautiful session start banner."""
        start_time = self.session_stats["start_time"].strftime("%Y-%m-%d %H:%M:%S")

        # Create session info table
        session_table = Table(box=box.ROUNDED, show_header=False, padding=(0, 1))
        session_table.add_column("Property", style="cyan bold")
        session_table.add_column("Value", style="white")

        session_table.add_row("🆔 Session ID", self.session_id)
        session_table.add_row("📅 Start Time", start_time)
        session_table.add_row("📁 Log File", str(self.log_file_path))
        session_table.add_row("🔧 Log Level", logging.getLevelName(self.log_level))
        session_table.add_row("🐍 Python", f"{sys.version.split()[0]}")
        session_table.add_row("📂 Directory", os.getcwd())

        # Create beautiful panel
        session_panel = Panel(
            session_table,
            title="[bold cyan]🚀 Ebook Generator Session Started[/bold cyan]",
            border_style="cyan",
            padding=(1, 2)
        )

        self.rich_console.print()
        self.rich_console.print(session_panel)
        self.rich_console.print()

    def info(self, message: str, **kwargs):
        """Log info message with beautiful formatting."""
        self.session_stats["operations"] += 1
        self._log_with_rich_context("INFO", message, "blue", "ℹ️", **kwargs)

    def debug(self, message: str, **kwargs):
        """Log debug message with beautiful formatting."""
        self._log_with_rich_context("DEBUG", message, "dim white", "🔍", **kwargs)

    def warning(self, message: str, **kwargs):
        """Log warning message with beautiful formatting."""
        self.session_stats["warnings"] += 1
        self._log_with_rich_context("WARNING", message, "yellow", "⚠️", **kwargs)

    def error(self, message: str, exception: Optional[Exception] = None, **kwargs):
        """Log error message with beautiful formatting and exception details."""
        self.session_stats["errors"] += 1

        if exception:
            # Create beautiful error panel
            error_text = Text()
            error_text.append(f"❌ {message}\n", style="bold red")
            error_text.append(f"Exception: {str(exception)}", style="red")

            error_panel = Panel(
                error_text,
                title="[bold red]🚨 Error Occurred[/bold red]",
                border_style="red",
                padding=(1, 2)
            )

            self.rich_console.print(error_panel)

            # Log to file with full traceback
            self.logger.error(f"{message} | Exception: {str(exception)}")
            self.logger.error(f"Exception traceback:\n{traceback.format_exc()}")
        else:
            self._log_with_rich_context("ERROR", message, "red", "❌", **kwargs)

    def critical(self, message: str, exception: Optional[Exception] = None, **kwargs):
        """Log critical message with beautiful formatting."""
        self.session_stats["errors"] += 1

        if exception:
            # Create beautiful critical error panel
            critical_text = Text()
            critical_text.append(f"💥 CRITICAL: {message}\n", style="bold red blink")
            critical_text.append(f"Exception: {str(exception)}", style="red")

            critical_panel = Panel(
                critical_text,
                title="[bold red blink]💥 CRITICAL ERROR[/bold red blink]",
                border_style="red",
                padding=(1, 2)
            )

            self.rich_console.print(critical_panel)

            # Log to file with full traceback
            self.logger.critical(f"{message} | Exception: {str(exception)}")
            self.logger.critical(f"Exception traceback:\n{traceback.format_exc()}")
        else:
            self._log_with_rich_context("CRITICAL", message, "bold red", "💥", **kwargs)

    def _log_with_rich_context(self, level: str, message: str, color: str, icon: str, **kwargs):
        """Log message with beautiful Rich formatting and context."""
        # Create the main message
        log_text = Text()
        log_text.append(f"{icon} ", style=color)
        log_text.append(message, style=color)

        # Add context if provided
        if kwargs:
            log_text.append(" | ", style="dim white")
            for i, (k, v) in enumerate(kwargs.items()):
                if i > 0:
                    log_text.append(" ", style="dim white")
                log_text.append(f"{k}=", style="dim white")
                log_text.append(str(v), style="cyan")

        # Log to Rich console
        self.rich_console.print(log_text)

        # Also log to file
        file_message = f"{message}"
        if kwargs:
            context_str = " | ".join([f"{k}={v}" for k, v in kwargs.items()])
            file_message = f"{message} | Context: {context_str}"

        log_level = getattr(logging, level.upper())
        self.logger.log(log_level, file_message)

    def log_function_start(self, func_name: str, **params):
        """Log the start of a function with beautiful formatting."""
        function_text = Text()
        function_text.append("🚀 FUNCTION START: ", style="green")
        function_text.append(func_name, style="bold green")

        if params:
            function_text.append("(", style="dim white")
            for i, (k, v) in enumerate(params.items()):
                if i > 0:
                    function_text.append(", ", style="dim white")
                function_text.append(k, style="cyan")
                function_text.append("=", style="dim white")
                function_text.append(str(v), style="yellow")
            function_text.append(")", style="dim white")

        self.rich_console.print(function_text)
        self.logger.debug(f"FUNCTION START: {func_name}({', '.join([f'{k}={v}' for k, v in params.items()])})")

    def log_function_end(self, func_name: str, result: Any = None, duration: Optional[float] = None):
        """Log the end of a function with beautiful formatting."""
        function_text = Text()
        function_text.append("✅ FUNCTION END: ", style="green")
        function_text.append(func_name, style="bold green")

        if duration:
            function_text.append(" | Duration: ", style="dim white")
            function_text.append(f"{duration:.2f}s", style="yellow")

        if result is not None:
            if isinstance(result, (dict, list)):
                function_text.append(" | Result: ", style="dim white")
                function_text.append(type(result).__name__, style="cyan")
                function_text.append(f" ({len(result)} items)", style="dim white")
            else:
                result_str = str(result)[:50] + "..." if len(str(result)) > 50 else str(result)
                function_text.append(" | Result: ", style="dim white")
                function_text.append(result_str, style="cyan")

        self.rich_console.print(function_text)

        # File logging
        msg = f"FUNCTION END: {func_name}"
        if duration:
            msg += f" | Duration: {duration:.2f}s"
        if result is not None:
            if isinstance(result, (dict, list)):
                msg += f" | Result type: {type(result).__name__} | Length: {len(result)}"
            else:
                msg += f" | Result: {str(result)[:100]}..."
        self.logger.debug(msg)

    def log_api_call(self, api_name: str, endpoint: str, params: Dict = None, response_status: str = None):
        """Log API calls with beautiful formatting."""
        self.session_stats["api_calls"] += 1

        # Create beautiful API call display
        api_table = Table(box=box.SIMPLE, show_header=False, padding=(0, 1))
        api_table.add_column("Property", style="cyan")
        api_table.add_column("Value", style="white")

        api_table.add_row("🌐 API", api_name)
        api_table.add_row("📡 Endpoint", endpoint)

        if params:
            params_str = json.dumps(params, default=str)[:100] + "..." if len(json.dumps(params, default=str)) > 100 else json.dumps(params, default=str)
            api_table.add_row("📝 Params", params_str)

        if response_status:
            status_color = "green" if response_status.lower() in ["success", "200", "ok"] else "red"
            api_table.add_row("📊 Status", f"[{status_color}]{response_status}[/{status_color}]")

        api_panel = Panel(
            api_table,
            title="[bold blue]🌐 API Call[/bold blue]",
            border_style="blue",
            padding=(0, 1)
        )

        self.rich_console.print(api_panel)

        # File logging
        msg = f"API CALL: {api_name} | Endpoint: {endpoint}"
        if params:
            msg += f" | Params: {json.dumps(params, default=str)[:200]}..."
        if response_status:
            msg += f" | Status: {response_status}"
        self.logger.info(msg)

    def log_generation_step(self, step: str, genre: str, status: str, details: str = ""):
        """Log book generation steps with beautiful formatting."""
        # Choose icon and color based on status
        if status.lower() in ["starting", "in progress", "generating"]:
            icon = "🔄"
            color = "yellow"
        elif status.lower() in ["completed", "success", "finished"]:
            icon = "✅"
            color = "green"
        elif status.lower() in ["error", "failed"]:
            icon = "❌"
            color = "red"
        else:
            icon = "📋"
            color = "blue"

        # Create generation step display
        step_text = Text()
        step_text.append(f"{icon} ", style=color)
        step_text.append("GENERATION: ", style="bold cyan")
        step_text.append(step, style="bold white")
        step_text.append(" | Genre: ", style="dim white")
        step_text.append(genre, style="magenta")
        step_text.append(" | Status: ", style="dim white")
        step_text.append(status, style=color)

        if details:
            step_text.append(" | ", style="dim white")
            step_text.append(details, style="dim cyan")

        self.rich_console.print(step_text)

        # File logging
        msg = f"GENERATION STEP: {step} | Genre: {genre} | Status: {status}"
        if details:
            msg += f" | Details: {details}"
        self.logger.info(msg)

    def log_chapter_progress(self, chapter_num: int, total_chapters: int, status: str, word_count: int = 0):
        """Log chapter generation progress with beautiful formatting."""
        progress = (chapter_num / total_chapters) * 100

        # Create progress bar
        progress_bar_width = 20
        filled_width = int((progress / 100) * progress_bar_width)
        progress_bar = "█" * filled_width + "░" * (progress_bar_width - filled_width)

        # Choose color based on status
        if status.lower() in ["completed", "success"]:
            status_color = "green"
            icon = "✅"
        elif status.lower() in ["generating", "in progress"]:
            status_color = "yellow"
            icon = "🔄"
        elif status.lower() in ["error", "failed"]:
            status_color = "red"
            icon = "❌"
        else:
            status_color = "blue"
            icon = "📝"

        # Create beautiful progress display
        progress_text = Text()
        progress_text.append(f"{icon} ", style=status_color)
        progress_text.append("CHAPTER: ", style="bold cyan")
        progress_text.append(f"{chapter_num}/{total_chapters}", style="bold white")
        progress_text.append(f" ({progress:.1f}%) ", style="dim white")
        progress_text.append(f"[{progress_bar}] ", style="green")
        progress_text.append("Status: ", style="dim white")
        progress_text.append(status, style=status_color)

        if word_count > 0:
            progress_text.append(" | Words: ", style="dim white")
            progress_text.append(f"{word_count:,}", style="cyan")

        self.rich_console.print(progress_text)

        # File logging
        msg = f"CHAPTER PROGRESS: {chapter_num}/{total_chapters} ({progress:.1f}%) | Status: {status}"
        if word_count > 0:
            msg += f" | Words: {word_count}"
        self.logger.info(msg)

    def log_memory_usage(self, context: str = ""):
        """Log current memory usage with beautiful formatting."""
        try:
            import psutil
            process = psutil.Process()
            memory_mb = process.memory_info().rss / 1024 / 1024

            # Choose color based on memory usage
            if memory_mb < 50:
                color = "green"
                icon = "💚"
            elif memory_mb < 100:
                color = "yellow"
                icon = "💛"
            else:
                color = "red"
                icon = "❤️"

            memory_text = Text()
            memory_text.append(f"{icon} MEMORY: ", style=color)
            memory_text.append(f"{memory_mb:.1f} MB", style=f"bold {color}")
            if context:
                memory_text.append(" | Context: ", style="dim white")
                memory_text.append(context, style="cyan")

            self.rich_console.print(memory_text)
            self.logger.debug(f"MEMORY USAGE: {memory_mb:.1f} MB | Context: {context}")

        except ImportError:
            self.debug("MEMORY USAGE: psutil not available")

    def display_session_stats(self):
        """Display beautiful session statistics."""
        duration = datetime.now() - self.session_stats["start_time"]
        duration_str = str(duration).split('.')[0]  # Remove microseconds

        # Create stats table
        stats_table = Table(box=box.ROUNDED, show_header=False, padding=(0, 1))
        stats_table.add_column("Metric", style="cyan bold")
        stats_table.add_column("Value", style="white")

        stats_table.add_row("⏱️ Duration", duration_str)
        stats_table.add_row("🔧 Operations", str(self.session_stats["operations"]))
        stats_table.add_row("🌐 API Calls", str(self.session_stats["api_calls"]))
        stats_table.add_row("⚠️ Warnings", str(self.session_stats["warnings"]))
        stats_table.add_row("❌ Errors", str(self.session_stats["errors"]))

        # Create beautiful panel
        stats_panel = Panel(
            stats_table,
            title="[bold cyan]📊 Session Statistics[/bold cyan]",
            border_style="cyan",
            padding=(1, 2)
        )

        self.rich_console.print(stats_panel)

    def get_log_file_path(self) -> str:
        """Get the current log file path."""
        return str(self.log_file_path)

    def close(self):
        """Close the logger with beautiful session end display."""
        # Display session statistics
        self.display_session_stats()

        # Create session end banner
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        end_table = Table(box=box.ROUNDED, show_header=False, padding=(0, 1))
        end_table.add_column("Property", style="cyan bold")
        end_table.add_column("Value", style="white")

        end_table.add_row("🆔 Session ID", self.session_id)
        end_table.add_row("🏁 End Time", end_time)
        end_table.add_row("📁 Log File", str(self.log_file_path))

        # Create beautiful panel
        end_panel = Panel(
            end_table,
            title="[bold cyan]🏁 Ebook Generator Session Ended[/bold cyan]",
            border_style="cyan",
            padding=(1, 2)
        )

        self.rich_console.print()
        self.rich_console.print(end_panel)
        self.rich_console.print()

        # File logging
        self.logger.info("=" * 80)
        self.logger.info(f"EBOOK GENERATOR SESSION ENDED - ID: {self.session_id}")
        self.logger.info("=" * 80)

        # Close all handlers
        for handler in self.logger.handlers[:]:
            handler.close()
            self.logger.removeHandler(handler)

# Global logger instance
_global_logger: Optional[EbookLogger] = None

def get_logger() -> EbookLogger:
    """Get the global logger instance."""
    global _global_logger
    if _global_logger is None:
        _global_logger = EbookLogger()
    return _global_logger

def init_logger(log_level: str = "DEBUG") -> EbookLogger:
    """Initialize the global logger with specified level."""
    global _global_logger
    _global_logger = EbookLogger(log_level)
    return _global_logger

def close_logger():
    """Close the global logger."""
    global _global_logger
    if _global_logger:
        _global_logger.close()
        _global_logger = None

# Convenience functions
def log_info(message: str, **kwargs):
    """Log info message."""
    get_logger().info(message, **kwargs)

def log_debug(message: str, **kwargs):
    """Log debug message."""
    get_logger().debug(message, **kwargs)

def log_warning(message: str, **kwargs):
    """Log warning message."""
    get_logger().warning(message, **kwargs)

def log_error(message: str, exception: Optional[Exception] = None, **kwargs):
    """Log error message."""
    get_logger().error(message, exception, **kwargs)

def log_critical(message: str, exception: Optional[Exception] = None, **kwargs):
    """Log critical message."""
    get_logger().critical(message, exception, **kwargs)
