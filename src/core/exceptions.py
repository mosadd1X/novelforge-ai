"""
Unified exception hierarchy for the Ebook Generator.

This module provides a standardized exception system with user-friendly messages,
recovery suggestions, and proper error categorization for better debugging and
user experience.
"""

from typing import List, Dict, Any


class EbookGeneratorError(Exception):
    """
    Base exception for all Ebook Generator errors.
    
    Provides user-friendly messages, recovery suggestions, and error details
    for better debugging and user experience.
    """
    
    def __init__(
        self, 
        message: str, 
        user_message: str = None, 
        details: Dict[str, Any] = None,
        recovery_suggestions: List[str] = None,
        error_code: str = None
    ):
        """
        Initialize the exception with comprehensive error information.
        
        Args:
            message: Technical error message for logging
            user_message: User-friendly message to display
            details: Additional error details for debugging
            recovery_suggestions: List of suggested recovery actions
            error_code: Unique error code for categorization
        """
        super().__init__(message)
        self.user_message = user_message or message
        self.details = details or {}
        self.recovery_suggestions = recovery_suggestions or []
        self.error_code = error_code or self.__class__.__name__
        
        # Add context information
        self.details.update({
            'error_type': self.__class__.__name__,
            'error_code': self.error_code,
            'technical_message': message
        })
    
    def get_user_display(self) -> Dict[str, Any]:
        """
        Get formatted error information for user display.
        
        Returns:
            Dictionary with formatted error information
        """
        return {
            'message': self.user_message,
            'suggestions': self.recovery_suggestions,
            'error_code': self.error_code,
            'details': self.details
        }


class NetworkError(EbookGeneratorError):
    """Network-related errors (API calls, connectivity issues)."""
    
    def __init__(self, message: str, **kwargs):
        default_suggestions = [
            "Check your internet connection",
            "Verify your API keys are valid",
            "Try again in a few moments",
            "Check if the service is experiencing issues"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', "Network connection issue detected"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )


class APIError(NetworkError):
    """API-specific errors (rate limits, authentication, service errors)."""
    
    def __init__(self, message: str, api_service: str = None, **kwargs):
        self.api_service = api_service
        
        default_suggestions = [
            f"Check your {api_service} API key" if api_service else "Check your API key",
            "Verify API service status",
            "Check for rate limiting",
            "Try again with exponential backoff"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', f"{api_service} API error" if api_service else "API error"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )
        
        if api_service:
            self.details['api_service'] = api_service


class GenerationError(EbookGeneratorError):
    """Content generation errors (AI generation failures, parsing issues)."""
    
    def __init__(self, message: str, generation_type: str = None, **kwargs):
        self.generation_type = generation_type
        
        default_suggestions = [
            "Try regenerating the content",
            "Check your prompt parameters",
            "Verify your input data is valid",
            "Try with different generation settings"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', f"Failed to generate {generation_type}" if generation_type else "Content generation failed"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )
        
        if generation_type:
            self.details['generation_type'] = generation_type


class ValidationError(EbookGeneratorError):
    """Input validation errors (invalid parameters, missing data)."""
    
    def __init__(self, message: str, field_name: str = None, **kwargs):
        self.field_name = field_name
        
        default_suggestions = [
            "Check your input parameters",
            "Verify all required fields are provided",
            "Ensure input values are in the correct format",
            "Review the documentation for valid input ranges"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', f"Invalid {field_name}" if field_name else "Invalid input"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )
        
        if field_name:
            self.details['field_name'] = field_name


class FileOperationError(EbookGeneratorError):
    """File system operation errors (read/write failures, permissions)."""
    
    def __init__(self, message: str, file_path: str = None, operation: str = None, **kwargs):
        self.file_path = file_path
        self.operation = operation
        
        default_suggestions = [
            "Check file permissions",
            "Verify the directory exists",
            "Ensure sufficient disk space",
            "Check if the file is in use by another program"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', f"File {operation} failed" if operation else "File operation failed"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )
        
        if file_path:
            self.details['file_path'] = file_path
        if operation:
            self.details['operation'] = operation


class ConfigurationError(EbookGeneratorError):
    """Configuration and setup errors (missing API keys, invalid settings)."""
    
    def __init__(self, message: str, config_key: str = None, **kwargs):
        self.config_key = config_key
        
        default_suggestions = [
            "Check your .env file configuration",
            "Verify all required API keys are set",
            "Review the setup documentation",
            "Ensure configuration values are valid"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', f"Configuration error: {config_key}" if config_key else "Configuration error"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )
        
        if config_key:
            self.details['config_key'] = config_key


class MemoryError(EbookGeneratorError):
    """Memory management errors (out of memory, memory corruption)."""
    
    def __init__(self, message: str, **kwargs):
        default_suggestions = [
            "Try reducing the generation scope",
            "Close other applications to free memory",
            "Consider generating in smaller batches",
            "Restart the application if memory issues persist"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', "Memory management issue detected"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )


class SeriesError(EbookGeneratorError):
    """Series-specific errors (continuity issues, series data corruption)."""
    
    def __init__(self, message: str, series_title: str = None, book_number: int = None, **kwargs):
        self.series_title = series_title
        self.book_number = book_number
        
        default_suggestions = [
            "Check series data integrity",
            "Verify continuity files are not corrupted",
            "Try regenerating the problematic book",
            "Review series configuration settings"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', f"Series error in {series_title}" if series_title else "Series error"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )
        
        if series_title:
            self.details['series_title'] = series_title
        if book_number:
            self.details['book_number'] = book_number


class FormatError(EbookGeneratorError):
    """Format-specific errors (EPUB generation, PDF creation, etc.)."""
    
    def __init__(self, message: str, format_type: str = None, **kwargs):
        self.format_type = format_type
        
        default_suggestions = [
            "Try a different output format",
            "Check if all required dependencies are installed",
            "Verify the content is properly formatted",
            "Try regenerating with simpler formatting"
        ]
        
        super().__init__(
            message=message,
            user_message=kwargs.get('user_message', f"{format_type} format error" if format_type else "Format error"),
            recovery_suggestions=kwargs.get('recovery_suggestions', default_suggestions),
            **{k: v for k, v in kwargs.items() if k not in ['user_message', 'recovery_suggestions']}
        )
        
        if format_type:
            self.details['format_type'] = format_type


# Convenience functions for common error scenarios
def create_network_timeout_error(timeout_duration: float) -> NetworkError:
    """Create a standardized network timeout error."""
    return NetworkError(
        message=f"Network request timed out after {timeout_duration} seconds",
        user_message="Connection timed out. Your internet may be slow or the service may be busy.",
        recovery_suggestions=[
            "Check your internet connection speed",
            "Try again in a few moments",
            "Consider increasing timeout settings",
            "Switch to a more stable network if available"
        ],
        details={'timeout_duration': timeout_duration}
    )


def create_api_rate_limit_error(api_service: str, retry_after: int = None) -> APIError:
    """Create a standardized API rate limit error."""
    suggestions = [
        f"Wait before making more {api_service} requests",
        "Consider using multiple API keys for higher limits",
        "Reduce the frequency of requests",
        "Check your API usage dashboard"
    ]
    
    if retry_after:
        suggestions.insert(0, f"Wait {retry_after} seconds before retrying")
    
    return APIError(
        message=f"{api_service} API rate limit exceeded",
        api_service=api_service,
        user_message=f"You've reached the {api_service} API rate limit. Please wait before continuing.",
        recovery_suggestions=suggestions,
        details={'retry_after': retry_after} if retry_after else {}
    )


def create_file_not_found_error(file_path: str) -> FileOperationError:
    """Create a standardized file not found error."""
    return FileOperationError(
        message=f"File not found: {file_path}",
        file_path=file_path,
        operation="read",
        user_message=f"Could not find the required file: {file_path}",
        recovery_suggestions=[
            "Check if the file path is correct",
            "Verify the file exists in the expected location",
            "Check file permissions",
            "Try regenerating the missing file"
        ]
    )
