"""
Enhanced Gemini Client with Network Resilience

This module provides a network-resilient wrapper around the existing GeminiClient
that integrates with the NetworkResilienceManager for robust handling of unstable
WiFi connections and network issues.
"""

from typing import Dict, List, Optional, Any
from src.core.gemini_client import GeminiClient
from src.utils.network_resilience import (
    get_network_manager, 
    NetworkResilienceManager, 
    RequestPriority,
    NetworkStatus
)
from rich.console import Console

console = Console()

class ResilientGeminiClient:
    """
    Network-resilient wrapper for GeminiClient that provides:
    - Automatic retry with exponential backoff
    - Request queuing during network outages
    - Circuit breaker pattern for protection
    - Real-time network status monitoring
    - Graceful degradation capabilities
    """
    
    def __init__(self, resilience_config: Optional[Dict[str, Any]] = None):
        """
        Initialize the resilient Gemini client.
        
        Args:
            resilience_config: Configuration for network resilience manager
        """
        # Initialize the underlying Gemini client
        self.gemini_client = GeminiClient()
        
        # Initialize network resilience manager
        self.network_manager = get_network_manager(resilience_config)
        
        # Configuration
        self.default_priority = RequestPriority.NORMAL
        self.default_max_retries = 8  # Increased for unstable connections
        self.default_timeout = 120.0  # Increased timeout for slow connections
        
        # Offline mode capabilities
        self.offline_mode = False
        self.cached_responses: Dict[str, str] = {}
        
        # Add status change callback
        self.network_manager.add_status_change_callback(self._on_network_status_change)
        
        console.print("[bold green]🛡️ Resilient Gemini Client initialized with network protection[/bold green]")
    
    def _on_network_status_change(self, old_status: NetworkStatus, new_status: NetworkStatus):
        """Handle network status changes."""
        if new_status == NetworkStatus.DISCONNECTED:
            console.print("[bold yellow]📡 Network disconnected - switching to offline mode[/bold yellow]")
            self.offline_mode = True
        elif new_status == NetworkStatus.CONNECTED and old_status == NetworkStatus.DISCONNECTED:
            console.print("[bold green]🌐 Network restored - resuming online operations[/bold green]")
            self.offline_mode = False
    
    def _create_cache_key(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """Create a cache key for response caching."""
        import hashlib
        content = f"{prompt}_{temperature}_{max_tokens}"
        return hashlib.md5(content.encode()).hexdigest()
    
    def _get_cached_response(self, cache_key: str) -> Optional[str]:
        """Get cached response if available."""
        return self.cached_responses.get(cache_key)
    
    def _cache_response(self, cache_key: str, response: str):
        """Cache a response for offline use."""
        # Limit cache size to prevent memory issues
        if len(self.cached_responses) > 100:
            # Remove oldest entries (simple FIFO)
            oldest_key = next(iter(self.cached_responses))
            del self.cached_responses[oldest_key]
        
        self.cached_responses[cache_key] = response
    
    def _handle_offline_request(self, prompt: str, temperature: float, max_tokens: int) -> str:
        """Handle requests when offline."""
        cache_key = self._create_cache_key(prompt, temperature, max_tokens)
        cached_response = self._get_cached_response(cache_key)
        
        if cached_response:
            console.print("[bold blue]📋 Using cached response (offline mode)[/bold blue]")
            return cached_response
        else:
            # Return a helpful offline message
            return (
                "⚠️ OFFLINE MODE: Unable to generate new content due to network connectivity issues. "
                "The system is monitoring network status and will automatically resume when connection is restored. "
                "Please check your internet connection and try again."
            )
    
    def generate_content(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 16000,
        priority: RequestPriority = None,
        max_retries: int = None,
        timeout: float = None,
        use_cache: bool = True
    ) -> str:
        """
        Generate content with network resilience.
        
        Args:
            prompt: The prompt to send to the model
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate
            priority: Request priority level
            max_retries: Maximum number of retry attempts
            timeout: Maximum time to wait for completion
            use_cache: Whether to use response caching
        
        Returns:
            Generated content as string
        """
        # Use defaults if not specified
        if priority is None:
            priority = self.default_priority
        if max_retries is None:
            max_retries = self.default_max_retries
        if timeout is None:
            timeout = self.default_timeout
        
        # Check cache first if enabled
        cache_key = None
        if use_cache:
            cache_key = self._create_cache_key(prompt, temperature, max_tokens)
            cached_response = self._get_cached_response(cache_key)
            if cached_response:
                console.print("[bold blue]📋 Using cached response[/bold blue]")
                return cached_response
        
        # Handle offline mode
        if self.offline_mode:
            return self._handle_offline_request(prompt, temperature, max_tokens)
        
        # Check if network is healthy
        if not self.network_manager.is_healthy():
            console.print("[bold yellow]⚠️ Network unhealthy - queuing request for retry[/bold yellow]")
        
        # Create wrapper function for the actual API call
        def api_call():
            return self.gemini_client.generate_content(
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                max_retries=1,  # Let resilience manager handle retries
                initial_retry_delay=1.0
            )
        
        try:
            # Execute with network resilience
            result = self.network_manager.execute_with_resilience(
                function=api_call,
                priority=priority,
                max_retries=max_retries,
                timeout=timeout
            )
            
            # Cache successful response
            if use_cache and cache_key and result and not result.startswith("Error"):
                self._cache_response(cache_key, result)
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            console.print(f"[bold red]❌ Content generation failed: {error_msg}[/bold red]")
            
            # Try to provide cached response as fallback
            if use_cache and cache_key:
                cached_response = self._get_cached_response(cache_key)
                if cached_response:
                    console.print("[bold yellow]📋 Falling back to cached response[/bold yellow]")
                    return cached_response
            
            # Return error message with guidance
            return (
                f"Error generating content: {error_msg}\n\n"
                "The system will automatically retry when network connectivity improves. "
                "You can check network status or try again manually."
            )
    
    def generate_with_context(
        self,
        prompt: str,
        context: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 16000,
        priority: RequestPriority = None,
        max_retries: int = None,
        timeout: float = None
    ) -> str:
        """
        Generate content with conversation context and network resilience.
        
        Args:
            prompt: The prompt to send to the model
            context: List of previous messages in the conversation
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate
            priority: Request priority level
            max_retries: Maximum number of retry attempts
            timeout: Maximum time to wait for completion
        
        Returns:
            Generated content as string
        """
        # Use defaults if not specified
        if priority is None:
            priority = self.default_priority
        if max_retries is None:
            max_retries = self.default_max_retries
        if timeout is None:
            timeout = self.default_timeout
        
        # Handle offline mode
        if self.offline_mode:
            return (
                "⚠️ OFFLINE MODE: Context-based generation unavailable due to network connectivity issues. "
                "The system is monitoring network status and will automatically resume when connection is restored."
            )
        
        # Create wrapper function for the actual API call
        def api_call():
            return self.gemini_client.generate_with_context(
                prompt=prompt,
                context=context,
                temperature=temperature,
                max_tokens=max_tokens,
                max_retries=1,  # Let resilience manager handle retries
                initial_retry_delay=1.0
            )
        
        try:
            # Execute with network resilience
            result = self.network_manager.execute_with_resilience(
                function=api_call,
                priority=priority,
                max_retries=max_retries,
                timeout=timeout
            )
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            console.print(f"[bold red]❌ Context generation failed: {error_msg}[/bold red]")
            
            return (
                f"Error generating content with context: {error_msg}\n\n"
                "The system will automatically retry when network connectivity improves."
            )
    
    def check_api_connection(self, check_all_keys: bool = False) -> Dict[str, Any]:
        """
        Check API connection with network resilience awareness.
        
        Args:
            check_all_keys: Whether to check all API keys
        
        Returns:
            Dictionary with connection status and network health info
        """
        # Get basic API status
        api_status = self.gemini_client.check_api_connection(check_all_keys)
        
        # Add network resilience information
        network_status = self.network_manager.get_status()
        
        return {
            **api_status,
            'network_resilience': {
                'status': network_status['status'],
                'circuit_state': network_status['circuit_state'],
                'is_healthy': self.network_manager.is_healthy(),
                'offline_mode': self.offline_mode,
                'cached_responses': len(self.cached_responses)
            }
        }
    
    def get_network_status(self) -> Dict[str, Any]:
        """Get detailed network status information."""
        return self.network_manager.get_status()
    
    def show_network_status(self):
        """Display network status panel."""
        self.network_manager.show_status_panel()
    
    def force_network_check(self) -> bool:
        """Force an immediate network connectivity check."""
        return self.network_manager.force_connectivity_check()
    
    def clear_cache(self):
        """Clear the response cache."""
        self.cached_responses.clear()
        console.print("[bold green]📋 Response cache cleared[/bold green]")
    
    def get_cache_info(self) -> Dict[str, Any]:
        """Get information about the response cache."""
        return {
            'cached_responses': len(self.cached_responses),
            'cache_keys': list(self.cached_responses.keys())
        }
    
    def cleanup(self):
        """Clean up resources."""
        # Remove status change callback
        self.network_manager.remove_status_change_callback(self._on_network_status_change)
        
        # Clear cache
        self.cached_responses.clear()
        
        console.print("[bold blue]🧹 Resilient Gemini Client cleaned up[/bold blue]")
