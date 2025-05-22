"""
Client for interacting with the Gemini 2.0 Flash API.
"""
import os
import time
import random
import socket
import google.generativeai as genai
from dotenv import load_dotenv
from typing import Dict, List, Optional, Any, Union
from requests.exceptions import RequestException, Timeout, ConnectionError

# Load environment variables
load_dotenv()

# Use the Gemini 2.0 Flash model
MODEL = "gemini-2.0-flash"

# Rate limit error messages to detect
RATE_LIMIT_ERROR_MESSAGES = [
    "quota exceeded",
    "rate limit",
    "resource exhausted",
    "too many requests",
    "request limit exceeded",
    "quota limit reached"
]


class GeminiClient:
    """Client for interacting with the Gemini API with support for multiple API keys."""

    def __init__(self):
        """Initialize the Gemini client with multiple API key support."""
        # Load API keys from environment variables
        self.api_keys = self._load_api_keys()
        if not self.api_keys:
            raise ValueError("No valid Gemini API keys found in environment variables")

        # Initialize key rotation variables
        self.current_key_index = 0
        self.key_usage_count = {key: 0 for key in self.api_keys}
        self.rate_limited_keys = set()

        # Configure the initial API key
        self._configure_current_api_key()

        # Initialize model and history
        self.model = genai.GenerativeModel(MODEL)
        self.history = []

    def _load_api_keys(self) -> List[str]:
        """
        Load API keys from environment variables.

        Looks for GEMINI_API_KEY and GEMINI_API_KEY_1, GEMINI_API_KEY_2, etc.

        Returns:
            List of valid API keys
        """
        api_keys = []

        # Try to get the main API key
        main_key = os.getenv("GEMINI_API_KEY")
        if main_key and main_key.strip():
            api_keys.append(main_key.strip())

        # Try to get numbered API keys (GEMINI_API_KEY_1, GEMINI_API_KEY_2, etc.)
        for i in range(1, 11):  # Support up to 10 additional keys
            key = os.getenv(f"GEMINI_API_KEY_{i}")
            if key and key.strip():
                api_keys.append(key.strip())

        return api_keys

    def _configure_current_api_key(self) -> None:
        """Configure the Gemini API with the current API key."""
        current_key = self.api_keys[self.current_key_index]
        genai.configure(api_key=current_key)
        print(f"Using API key {self.current_key_index + 1}/{len(self.api_keys)}")

    def rotate_api_key(self, force: bool = False) -> bool:
        """
        Rotate to the next available API key.

        Args:
            force: If True, force rotation even if the current key isn't rate limited

        Returns:
            True if successfully rotated to a new key, False if all keys are rate limited
        """
        # Mark the current key as rate limited if not forced rotation
        if not force:
            current_key = self.api_keys[self.current_key_index]
            self.rate_limited_keys.add(current_key)

        # If all keys are rate limited, reset and try again
        if len(self.rate_limited_keys) >= len(self.api_keys):
            print("All API keys have been rate limited. Resetting and trying again.")
            self.rate_limited_keys.clear()

        # Find the next available key
        original_index = self.current_key_index
        while True:
            # Move to the next key
            self.current_key_index = (self.current_key_index + 1) % len(self.api_keys)

            # Check if this key is not rate limited
            current_key = self.api_keys[self.current_key_index]
            if current_key not in self.rate_limited_keys:
                break

            # If we've checked all keys and come back to the original, all keys are rate limited
            if self.current_key_index == original_index:
                print("All API keys are currently rate limited.")
                return False

        # Configure the new API key
        self._configure_current_api_key()
        return True

    def is_rate_limit_error(self, error_message: str) -> bool:
        """
        Check if an error message indicates a rate limit issue.

        Args:
            error_message: The error message to check

        Returns:
            True if the error appears to be rate limit related
        """
        error_lower = error_message.lower()
        return any(limit_msg in error_lower for limit_msg in RATE_LIMIT_ERROR_MESSAGES)

    def check_api_connection(self, check_all_keys: bool = False) -> Dict[str, Any]:
        """
        Check if the connection to the Gemini API is working.

        Args:
            check_all_keys: If True, check all API keys, otherwise just check the current key

        Returns:
            Dictionary with connection status and details
        """
        if not check_all_keys:
            # Just check the current key
            try:
                # Simple test prompt to check connection
                response = self.generate_content(
                    "Hello, this is a connection test.",
                    temperature=0.1,
                    max_tokens=10,
                    max_retries=1,
                    initial_retry_delay=1.0
                )
                success = "Error generating content" not in response
                return {
                    "success": success,
                    "active_keys": len(self.api_keys),
                    "working_keys": 1 if success else 0
                }
            except Exception as e:
                print(f"API connection check failed: {e}")
                return {
                    "success": False,
                    "active_keys": len(self.api_keys),
                    "working_keys": 0,
                    "error": str(e)
                }
        else:
            # Check all keys
            working_keys = 0
            key_statuses = {}
            original_key_index = self.current_key_index

            for i, key in enumerate(self.api_keys):
                # Switch to this key
                self.current_key_index = i
                self._configure_current_api_key()
                self.model = genai.GenerativeModel(MODEL)

                # Test the key
                try:
                    print(f"Testing API key {i+1}/{len(self.api_keys)}...")
                    response = self.generate_content(
                        "Hello, this is a connection test.",
                        temperature=0.1,
                        max_tokens=10,
                        max_retries=1,
                        initial_retry_delay=1.0
                    )
                    success = "Error generating content" not in response
                    if success:
                        working_keys += 1

                    # Mask the key for security
                    masked_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
                    key_statuses[masked_key] = {
                        "working": success,
                        "index": i + 1  # 1-based for display
                    }
                except Exception as e:
                    # Mask the key for security
                    masked_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
                    key_statuses[masked_key] = {
                        "working": False,
                        "index": i + 1,  # 1-based for display
                        "error": str(e)
                    }

            # Restore the original key
            self.current_key_index = original_key_index
            self._configure_current_api_key()
            self.model = genai.GenerativeModel(MODEL)

            return {
                "success": working_keys > 0,
                "active_keys": len(self.api_keys),
                "working_keys": working_keys,
                "key_statuses": key_statuses
            }

    def generate_content(
        self, prompt: str, temperature: float = 0.7, max_tokens: int = 16000,
        max_retries: int = 5, initial_retry_delay: float = 2.0
    ) -> str:
        """
        Generate content using the Gemini API with retry logic for network errors and API key rotation.

        Args:
            prompt: The prompt to send to the model
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate (default increased to 16000 for longer chapters)
            max_retries: Maximum number of retry attempts for network errors
            initial_retry_delay: Initial delay between retries in seconds (will be exponentially increased)

        Returns:
            The generated content as a string
        """
        retry_count = 0
        retry_delay = initial_retry_delay
        last_error = None
        key_rotation_attempts = 0
        max_key_rotations = len(self.api_keys) * 2  # Allow cycling through keys twice

        while retry_count <= max_retries:
            try:
                # If this is a retry, log the attempt
                if retry_count > 0:
                    print(f"Retry attempt {retry_count}/{max_retries} after {retry_delay:.1f}s delay...")

                # For socket errors, we'll use a small delay to allow DNS to refresh
                # This helps with "socket is null" errors
                if retry_count > 0:
                    # Clear DNS cache by forcing a new connection
                    socket.setdefaulttimeout(60)  # Increase socket timeout

                # Track API key usage
                current_key = self.api_keys[self.current_key_index]
                self.key_usage_count[current_key] = self.key_usage_count.get(current_key, 0) + 1

                # Make the API call
                response = self.model.generate_content(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "max_output_tokens": max_tokens,
                        "top_p": 0.95,
                        "top_k": 40,
                    },
                )

                # Extract the text from the response
                if hasattr(response, "text"):
                    return response.text
                elif hasattr(response, "parts"):
                    # Handle response with parts
                    parts = []
                    for part in response.parts:
                        if hasattr(part, "text"):
                            parts.append(part.text)
                        else:
                            parts.append(str(part))
                    return "\n".join(parts)
                else:
                    # Handle different response formats
                    return str(response)

            except (ConnectionError, Timeout, RequestException, socket.error) as e:
                # Network-related errors that are worth retrying
                last_error = e
                retry_count += 1

                if retry_count <= max_retries:
                    # Add jitter to retry delay to prevent thundering herd problem
                    jitter = random.uniform(0.1, 0.3) * retry_delay
                    sleep_time = retry_delay + jitter
                    print(f"Network error: {e}. Retrying in {sleep_time:.1f} seconds...")
                    time.sleep(sleep_time)
                    # Exponential backoff
                    retry_delay *= 2
                else:
                    print(f"Maximum retries ({max_retries}) exceeded. Last error: {e}")
                    return f"Error generating content after {max_retries} retries. Network issues detected. Please check your internet connection. Details: {str(e)}"

            except Exception as e:
                error_str = str(e)
                print(f"Error generating content: {error_str}")

                # Check if this is a rate limit error
                if self.is_rate_limit_error(error_str) and key_rotation_attempts < max_key_rotations:
                    key_rotation_attempts += 1
                    print(f"Rate limit detected. Rotating API key...")

                    # Rotate to the next API key
                    if self.rotate_api_key():
                        # Reset the model with the new API key
                        self.model = genai.GenerativeModel(MODEL)
                        print(f"Switched to API key {self.current_key_index + 1}/{len(self.api_keys)}. Retrying...")

                        # Don't count this as a retry, just switch keys and try again
                        continue
                    else:
                        # If we couldn't rotate to a new key, all keys are rate limited
                        return f"Error: All API keys have reached their rate limits. Please try again later."

                # For non-rate-limit errors, return the error message
                return f"Error generating content. Please try again. Details: {error_str}"

        # This should not be reached, but just in case
        return f"Error generating content after {max_retries} retries. Last error: {str(last_error)}"

    def generate_with_context(
        self,
        prompt: str,
        context: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 16000,
        max_retries: int = 5,
        initial_retry_delay: float = 2.0
    ) -> str:
        """
        Generate content with conversation context and retry logic for network errors.

        Args:
            prompt: The prompt to send to the model
            context: List of previous messages in the conversation
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate
            max_retries: Maximum number of retry attempts for network errors
            initial_retry_delay: Initial delay between retries in seconds (will be exponentially increased)

        Returns:
            The generated content as a string
        """
        retry_count = 0
        retry_delay = initial_retry_delay
        last_error = None
        key_rotation_attempts = 0
        max_key_rotations = len(self.api_keys) * 2  # Allow cycling through keys twice

        while retry_count <= max_retries:
            try:
                # If this is a retry, log the attempt
                if retry_count > 0:
                    print(f"Retry attempt {retry_count}/{max_retries} after {retry_delay:.1f}s delay...")

                # For socket errors, we'll use a small delay to allow DNS to refresh
                if retry_count > 0:
                    # Clear DNS cache by forcing a new connection
                    socket.setdefaulttimeout(60)  # Increase socket timeout

                # Track API key usage
                current_key = self.api_keys[self.current_key_index]
                self.key_usage_count[current_key] = self.key_usage_count.get(current_key, 0) + 1

                # Make the API call
                chat = self.model.start_chat(history=context)
                response = chat.send_message(
                    prompt,
                    generation_config={
                        "temperature": temperature,
                        "max_output_tokens": max_tokens,
                        "top_p": 0.95,
                        "top_k": 40,
                    },
                )

                # Extract the text from the response
                if hasattr(response, "text"):
                    return response.text
                elif hasattr(response, "parts"):
                    # Handle response with parts
                    parts = []
                    for part in response.parts:
                        if hasattr(part, "text"):
                            parts.append(part.text)
                        else:
                            parts.append(str(part))
                    return "\n".join(parts)
                else:
                    # Handle different response formats
                    return str(response)

            except (ConnectionError, Timeout, RequestException, socket.error) as e:
                # Network-related errors that are worth retrying
                last_error = e
                retry_count += 1

                if retry_count <= max_retries:
                    # Add jitter to retry delay to prevent thundering herd problem
                    jitter = random.uniform(0.1, 0.3) * retry_delay
                    sleep_time = retry_delay + jitter
                    print(f"Network error: {e}. Retrying in {sleep_time:.1f} seconds...")
                    time.sleep(sleep_time)
                    # Exponential backoff
                    retry_delay *= 2
                else:
                    print(f"Maximum retries ({max_retries}) exceeded. Last error: {e}")
                    return f"Error generating content with context after {max_retries} retries. Network issues detected. Please check your internet connection. Details: {str(e)}"

            except Exception as e:
                error_str = str(e)
                print(f"Error generating content with context: {error_str}")

                # Check if this is a rate limit error
                if self.is_rate_limit_error(error_str) and key_rotation_attempts < max_key_rotations:
                    key_rotation_attempts += 1
                    print(f"Rate limit detected. Rotating API key...")

                    # Rotate to the next API key
                    if self.rotate_api_key():
                        # Reset the model with the new API key
                        self.model = genai.GenerativeModel(MODEL)
                        print(f"Switched to API key {self.current_key_index + 1}/{len(self.api_keys)}. Retrying...")

                        # Don't count this as a retry, just switch keys and try again
                        continue
                    else:
                        # If we couldn't rotate to a new key, all keys are rate limited
                        return f"Error: All API keys have reached their rate limits. Please try again later."

                # For non-rate-limit errors, return the error message
                return f"Error generating content with context. Please try again. Details: {error_str}"

        # This should not be reached, but just in case
        return f"Error generating content with context after {max_retries} retries. Last error: {str(last_error)}"

    def clean_response(self, response: str) -> str:
        """
        Clean the response from Gemini to remove any unnecessary formatting.

        Args:
            response: The raw response from Gemini

        Returns:
            Cleaned response text
        """
        # Remove any common prefixes/suffixes that Gemini might add
        lines = response.split('\n')

        # Remove empty lines at the beginning and end
        while lines and not lines[0].strip():
            lines.pop(0)
        while lines and not lines[-1].strip():
            lines.pop()

        return '\n'.join(lines)

    def get_api_key_usage_stats(self) -> Dict[str, Any]:
        """
        Get statistics about API key usage.

        Returns:
            Dictionary containing API key usage statistics
        """
        # Calculate total usage
        total_usage = sum(self.key_usage_count.values())

        # Calculate percentage usage per key
        usage_percentages = {}
        for key, count in self.key_usage_count.items():
            # Mask the API key for security (show only first 4 and last 4 characters)
            masked_key = f"{key[:4]}...{key[-4:]}" if len(key) > 8 else "****"
            percentage = (count / total_usage * 100) if total_usage > 0 else 0
            usage_percentages[masked_key] = {
                "count": count,
                "percentage": round(percentage, 2)
            }

        # Get current key info
        current_key = self.api_keys[self.current_key_index]
        masked_current_key = f"{current_key[:4]}...{current_key[-4:]}" if len(current_key) > 8 else "****"

        return {
            "total_requests": total_usage,
            "active_keys": len(self.api_keys),
            "current_key_index": self.current_key_index + 1,  # 1-based for display
            "current_key": masked_current_key,
            "rate_limited_keys": len(self.rate_limited_keys),
            "usage_by_key": usage_percentages
        }
