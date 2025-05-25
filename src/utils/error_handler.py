"""
Centralized error handling and user feedback system.

This module provides consistent error handling, user-friendly error messages,
and standardized error reporting throughout the NovelForge AI application.
"""

import traceback
from typing import Any, Dict
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from src.core.exceptions import NovelForgeError

# Initialize Rich console for beautiful error display
console = Console(markup=True)


class ErrorHandler:
    """
    Centralized error handling and user feedback system.

    Provides consistent error display, logging, and recovery guidance
    across the entire application.
    """

    def __init__(self, debug_mode: bool = False):
        """
        Initialize the error handler.

        Args:
            debug_mode: Whether to show detailed technical information
        """
        self.debug_mode = debug_mode
        self.error_count = 0
        self.last_errors = []  # Keep track of recent errors

    def handle_error(
        self,
        error: Exception,
        context: str = None,
        show_suggestions: bool = True,
        show_technical_details: bool = None
    ) -> None:
        """
        Handle any error with appropriate user feedback and logging.

        Args:
            error: The exception that occurred
            context: Additional context about where the error occurred
            show_suggestions: Whether to show recovery suggestions
            show_technical_details: Whether to show technical details (overrides debug_mode)
        """
        self.error_count += 1

        # Determine if we should show technical details
        show_tech = show_technical_details if show_technical_details is not None else self.debug_mode

        if isinstance(error, NovelForgeError):
            self._handle_known_error(error, context, show_suggestions, show_tech)
        else:
            self._handle_unknown_error(error, context, show_suggestions, show_tech)

        # Store error for tracking
        self._track_error(error, context)

    def _handle_known_error(
        self,
        error: NovelForgeError,
        context: str,
        show_suggestions: bool,
        show_technical_details: bool
    ) -> None:
        """Handle known application errors with rich formatting."""

        # Create error display
        error_info = error.get_user_display()

        # Build error message
        error_text = Text()
        error_text.append("Error: ", style="bold red")
        error_text.append(error_info['message'], style="red")

        if context:
            error_text.append(f"\nContext: {context}", style="dim")

        if error_info.get('error_code'):
            error_text.append(f"\nError Code: {error_info['error_code']}", style="dim cyan")

        # Create panel content
        panel_content = [error_text]

        # Add recovery suggestions
        if show_suggestions and error_info.get('suggestions'):
            suggestions_text = Text("\nSuggested Actions:", style="bold cyan")
            for i, suggestion in enumerate(error_info['suggestions'], 1):
                suggestions_text.append(f"\n  {i}. {suggestion}", style="cyan")
            panel_content.append(suggestions_text)

        # Add technical details if requested
        if show_technical_details and error_info.get('details'):
            details_text = Text("\nTechnical Details:", style="bold yellow")
            for key, value in error_info['details'].items():
                if key not in ['error_type', 'error_code']:  # Skip redundant info
                    details_text.append(f"\n  {key}: {value}", style="yellow")
            panel_content.append(details_text)

        # Display the error panel
        panel = Panel(
            Text.assemble(*panel_content),
            title=f"[bold red]{error.__class__.__name__}[/bold red]",
            border_style="red",
            padding=(1, 2)
        )

        console.print()
        console.print(panel)
        console.print()

    def _handle_unknown_error(
        self,
        error: Exception,
        context: str,
        show_suggestions: bool,
        show_technical_details: bool
    ) -> None:
        """Handle unexpected errors with fallback formatting."""

        # Build error message
        error_text = Text()
        error_text.append("Unexpected Error: ", style="bold red")
        error_text.append(str(error), style="red")

        if context:
            error_text.append(f"\nContext: {context}", style="dim")

        # Create panel content
        panel_content = [error_text]

        # Add generic recovery suggestions
        if show_suggestions:
            suggestions_text = Text("\nSuggested Actions:", style="bold cyan")
            suggestions = [
                "Try the operation again",
                "Check your input parameters",
                "Restart the application if the issue persists",
                "Report this error if it continues to occur"
            ]
            for i, suggestion in enumerate(suggestions, 1):
                suggestions_text.append(f"\n  {i}. {suggestion}", style="cyan")
            panel_content.append(suggestions_text)

        # Add technical details
        if show_technical_details:
            details_text = Text("\nTechnical Details:", style="bold yellow")
            details_text.append(f"\n  Error Type: {error.__class__.__name__}", style="yellow")
            details_text.append(f"\n  Error Message: {str(error)}", style="yellow")

            # Add traceback if available
            if hasattr(error, '__traceback__') and error.__traceback__:
                tb_lines = traceback.format_tb(error.__traceback__)
                details_text.append(f"\n  Traceback: {tb_lines[-1].strip()}", style="yellow")

            panel_content.append(details_text)

        # Display the error panel
        panel = Panel(
            Text.assemble(*panel_content),
            title=f"[bold red]Unexpected Error[/bold red]",
            border_style="red",
            padding=(1, 2)
        )

        console.print()
        console.print(panel)
        console.print()

    def _track_error(self, error: Exception, context: str) -> None:
        """Track error for debugging and statistics."""
        error_info = {
            'error': error,
            'context': context,
            'error_type': error.__class__.__name__,
            'message': str(error),
            'count': self.error_count
        }

        # Keep only the last 10 errors
        self.last_errors.append(error_info)
        if len(self.last_errors) > 10:
            self.last_errors.pop(0)

    def display_warning(self, message: str, title: str = "Warning") -> None:
        """Display a warning message to the user."""
        warning_text = Text(message, style="yellow")

        panel = Panel(
            warning_text,
            title=f"[bold yellow]{title}[/bold yellow]",
            border_style="yellow",
            padding=(1, 2)
        )

        console.print()
        console.print(panel)
        console.print()

    def display_info(self, message: str, title: str = "Information") -> None:
        """Display an informational message to the user."""
        info_text = Text(message, style="blue")

        panel = Panel(
            info_text,
            title=f"[bold blue]{title}[/bold blue]",
            border_style="blue",
            padding=(1, 2)
        )

        console.print()
        console.print(panel)
        console.print()

    def display_success(self, message: str, title: str = "Success") -> None:
        """Display a success message to the user."""
        success_text = Text(message, style="green")

        panel = Panel(
            success_text,
            title=f"[bold green]{title}[/bold green]",
            border_style="green",
            padding=(1, 2)
        )

        console.print()
        console.print(panel)
        console.print()

    def get_error_summary(self) -> Dict[str, Any]:
        """Get a summary of recent errors for debugging."""
        error_types = {}
        for error_info in self.last_errors:
            error_type = error_info['error_type']
            error_types[error_type] = error_types.get(error_type, 0) + 1

        return {
            'total_errors': self.error_count,
            'recent_errors': len(self.last_errors),
            'error_types': error_types,
            'last_error': self.last_errors[-1] if self.last_errors else None
        }

    def clear_error_history(self) -> None:
        """Clear the error tracking history."""
        self.last_errors.clear()
        self.error_count = 0


# Global error handler instance
_global_error_handler = ErrorHandler()


def handle_error(
    error: Exception,
    context: str = None,
    show_suggestions: bool = True,
    show_technical_details: bool = None
) -> None:
    """
    Global error handling function.

    Args:
        error: The exception that occurred
        context: Additional context about where the error occurred
        show_suggestions: Whether to show recovery suggestions
        show_technical_details: Whether to show technical details
    """
    global _global_error_handler
    _global_error_handler.handle_error(error, context, show_suggestions, show_technical_details)


def display_warning(message: str, title: str = "Warning") -> None:
    """Display a warning message."""
    _global_error_handler.display_warning(message, title)


def display_info(message: str, title: str = "Information") -> None:
    """Display an informational message."""
    _global_error_handler.display_info(message, title)


def display_success(message: str, title: str = "Success") -> None:
    """Display a success message."""
    _global_error_handler.display_success(message, title)


def get_error_summary() -> Dict[str, Any]:
    """Get a summary of recent errors."""
    return _global_error_handler.get_error_summary()


def set_debug_mode(enabled: bool) -> None:
    """Enable or disable debug mode for detailed error information."""
    _global_error_handler.debug_mode = enabled


def clear_error_history() -> None:
    """Clear the error tracking history."""
    _global_error_handler.clear_error_history()


# Context manager for error handling
class ErrorContext:
    """Context manager for handling errors in specific operations."""

    def __init__(self, operation_name: str, show_suggestions: bool = True):
        self.operation_name = operation_name
        self.show_suggestions = show_suggestions

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            handle_error(
                exc_val,
                context=self.operation_name,
                show_suggestions=self.show_suggestions
            )
            return True  # Suppress the exception
        return False
