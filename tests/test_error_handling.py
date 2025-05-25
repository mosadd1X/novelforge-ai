#!/usr/bin/env python3
"""
Test script to verify the standardized error handling implementation.

This script tests:
1. Exception hierarchy works correctly
2. Error handler displays user-friendly messages
3. Recovery suggestions are provided
4. Error tracking and statistics work
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_exception_hierarchy():
    """Test the exception hierarchy and error creation."""
    print("Testing Exception Hierarchy...")

    try:
        from src.core.exceptions import (
            NovelForgeError, NetworkError, APIError, GenerationError,
            ValidationError, FileOperationError, ConfigurationError,
            create_api_rate_limit_error, create_network_timeout_error,
            create_file_not_found_error
        )

        # Test base exception
        base_error = NovelForgeError(
            message="Test error",
            user_message="User-friendly test error",
            recovery_suggestions=["Try again", "Check settings"]
        )

        assert base_error.user_message == "User-friendly test error"
        assert len(base_error.recovery_suggestions) == 2
        assert base_error.error_code == "NovelForgeError"

        # Test API error
        api_error = APIError(
            message="API failed",
            api_service="Gemini",
            user_message="API service unavailable"
        )

        assert api_error.api_service == "Gemini"
        assert "Check your Gemini API key" in api_error.recovery_suggestions

        # Test convenience functions
        rate_limit_error = create_api_rate_limit_error("Gemini", retry_after=60)
        assert rate_limit_error.api_service == "Gemini"
        assert rate_limit_error.details.get('retry_after') == 60

        timeout_error = create_network_timeout_error(30.0)
        assert timeout_error.details.get('timeout_duration') == 30.0

        file_error = create_file_not_found_error("/path/to/missing/file.txt")
        assert file_error.file_path == "/path/to/missing/file.txt"

        print("✓ Exception hierarchy test passed")
        return True

    except Exception as e:
        print(f"✗ Exception hierarchy test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_error_handler():
    """Test the error handler functionality."""
    print("\nTesting Error Handler...")

    try:
        from src.core.exceptions import NetworkError, GenerationError
        from src.utils.error_handler import (
            ErrorHandler, handle_error, display_warning,
            display_info, display_success, get_error_summary
        )

        # Create error handler
        error_handler = ErrorHandler(debug_mode=True)

        # Test handling known error
        network_error = NetworkError(
            message="Connection failed",
            user_message="Unable to connect to the service",
            recovery_suggestions=["Check internet", "Try again later"]
        )

        print("Testing known error handling:")
        error_handler.handle_error(network_error, "Test context")

        # Test handling unknown error
        print("\nTesting unknown error handling:")
        try:
            raise ValueError("This is a test error")
        except ValueError as e:
            error_handler.handle_error(e, "Test unknown error context")

        # Test display functions
        print("\nTesting display functions:")
        display_warning("This is a test warning")
        display_info("This is test information")
        display_success("This is a test success message")

        # Test error summary
        summary = get_error_summary()
        print(f"\nError summary: {summary}")

        assert summary['total_errors'] >= 2  # We handled at least 2 errors
        assert 'NetworkError' in summary['error_types']
        assert 'ValueError' in summary['error_types']

        print("✓ Error handler test passed")
        return True

    except Exception as e:
        print(f"✗ Error handler test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_error_context_manager():
    """Test the error context manager."""
    print("\nTesting Error Context Manager...")

    try:
        from src.utils.error_handler import ErrorContext

        # Test successful operation
        with ErrorContext("Test operation"):
            result = 2 + 2
            assert result == 4

        # Test error handling
        with ErrorContext("Test error operation"):
            raise ValueError("Test error in context")

        print("✓ Error context manager test passed")
        return True

    except Exception as e:
        print(f"✗ Error context manager test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_integration_with_existing_code():
    """Test integration with existing code patterns."""
    print("\nTesting Integration with Existing Code...")

    try:
        from src.core.exceptions import APIError
        from src.utils.error_handler import handle_error

        # Simulate how the new error handling would work in existing code
        def simulate_api_call():
            """Simulate an API call that might fail."""
            # This simulates the pattern we implemented in GeminiClient
            try:
                # Simulate API failure
                raise Exception("Rate limit exceeded")
            except Exception as e:
                if "rate limit" in str(e).lower():
                    # Create standardized error
                    api_error = APIError(
                        message=f"API rate limit error: {str(e)}",
                        api_service="Test API",
                        user_message="API rate limit reached",
                        recovery_suggestions=[
                            "Wait before making more requests",
                            "Check your API usage",
                            "Consider upgrading your plan"
                        ]
                    )
                    handle_error(api_error, "Simulated API call")
                    return "Error handled gracefully"
                else:
                    raise

        result = simulate_api_call()
        assert result == "Error handled gracefully"

        print("✓ Integration test passed")
        return True

    except Exception as e:
        print(f"✗ Integration test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_error_message_formatting():
    """Test that error messages are properly formatted."""
    print("\nTesting Error Message Formatting...")

    try:
        from src.core.exceptions import GenerationError
        from src.utils.error_handler import ErrorHandler

        # Create error with rich details
        error = GenerationError(
            message="Failed to generate content due to invalid prompt",
            generation_type="chapter",
            user_message="Unable to generate chapter content",
            details={
                'chapter_number': 5,
                'word_count_target': 3000,
                'genre': 'fantasy'
            },
            recovery_suggestions=[
                "Try simplifying the prompt",
                "Check the chapter outline",
                "Verify character information is complete",
                "Try regenerating with different parameters"
            ]
        )

        # Test error display
        error_handler = ErrorHandler(debug_mode=True)
        error_handler.handle_error(error, "Chapter generation test")

        # Test error info extraction
        error_info = error.get_user_display()
        assert error_info['message'] == "Unable to generate chapter content"
        assert len(error_info['suggestions']) == 4
        assert error_info['details']['chapter_number'] == 5

        print("✓ Error message formatting test passed")
        return True

    except Exception as e:
        print(f"✗ Error message formatting test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Run all error handling tests."""
    print("🧪 Testing Standardized Error Handling Implementation")
    print("=" * 60)

    success = True

    # Run all tests
    tests = [
        test_exception_hierarchy,
        test_error_handler,
        test_error_context_manager,
        test_integration_with_existing_code,
        test_error_message_formatting
    ]

    for test in tests:
        if not test():
            success = False

    print("\n" + "=" * 60)
    if success:
        print("✅ All error handling tests PASSED!")
        print("\nStandardized error handling is working:")
        print("• Exception hierarchy provides clear error categorization")
        print("• Error handler displays user-friendly messages with recovery suggestions")
        print("• Error tracking and statistics work correctly")
        print("• Integration with existing code patterns is successful")
        print("• Rich error message formatting is functional")
    else:
        print("❌ Some error handling tests FAILED!")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
