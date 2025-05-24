"""
Network Resilience System for Ebook Generator

This module provides comprehensive network resilience capabilities including:
- Real-time network connectivity monitoring
- Intelligent retry mechanisms with circuit breaker pattern
- Request queuing and automatic retry on connection recovery
- Graceful degradation and offline mode support
- User feedback and status reporting
"""

import time
import threading
import queue
import socket
import requests
import psutil
from typing import Dict, List, Optional, Callable, Any, Tuple
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

console = Console()

class NetworkStatus(Enum):
    """Network connection status enumeration."""
    CONNECTED = "connected"
    DISCONNECTED = "disconnected"
    UNSTABLE = "unstable"
    CHECKING = "checking"

class RequestPriority(Enum):
    """Request priority levels for queue management."""
    CRITICAL = 1
    HIGH = 2
    NORMAL = 3
    LOW = 4

@dataclass
class QueuedRequest:
    """Represents a queued network request."""
    id: str
    function: Callable
    args: tuple
    kwargs: dict
    priority: RequestPriority
    max_retries: int
    retry_count: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    last_attempt: Optional[datetime] = None
    error_history: List[str] = field(default_factory=list)

@dataclass
class NetworkMetrics:
    """Network performance and reliability metrics."""
    total_requests: int = 0
    successful_requests: int = 0
    failed_requests: int = 0
    retried_requests: int = 0
    average_response_time: float = 0.0
    connection_uptime: float = 0.0
    last_connection_check: Optional[datetime] = None
    consecutive_failures: int = 0
    consecutive_successes: int = 0

class CircuitBreakerState(Enum):
    """Circuit breaker states."""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Failing fast, not attempting requests
    HALF_OPEN = "half_open"  # Testing if service has recovered

@dataclass
class CircuitBreakerConfig:
    """Configuration for circuit breaker."""
    failure_threshold: int = 5
    recovery_timeout: int = 60  # seconds
    success_threshold: int = 3  # successes needed to close circuit

class NetworkResilienceManager:
    """
    Comprehensive network resilience manager that handles:
    - Connection monitoring
    - Request queuing and retry
    - Circuit breaker pattern
    - User feedback and status reporting
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the network resilience manager."""
        self.config = config or {}

        # Network status tracking
        self.status = NetworkStatus.CHECKING
        self.last_status_check = None
        self.status_check_interval = self.config.get('status_check_interval', 30)  # seconds

        # Request queue
        self.request_queue = queue.PriorityQueue()
        self.active_requests: Dict[str, QueuedRequest] = {}

        # Circuit breaker
        self.circuit_config = CircuitBreakerConfig(**self.config.get('circuit_breaker', {}))
        self.circuit_state = CircuitBreakerState.CLOSED
        self.circuit_opened_at: Optional[datetime] = None
        self.circuit_successes = 0

        # Metrics and monitoring
        self.metrics = NetworkMetrics()
        self.connection_history: List[Tuple[datetime, NetworkStatus]] = []

        # Threading
        self.monitoring_thread: Optional[threading.Thread] = None
        self.queue_processor_thread: Optional[threading.Thread] = None
        self.shutdown_event = threading.Event()

        # Callbacks
        self.status_change_callbacks: List[Callable[[NetworkStatus, NetworkStatus], None]] = []
        self.request_callbacks: Dict[str, Callable] = {}

        # User feedback
        self.show_status_messages = self.config.get('show_status_messages', True)
        self.show_retry_messages = self.config.get('show_retry_messages', True)

        # Start monitoring
        self.start_monitoring()

    def start_monitoring(self):
        """Start background monitoring threads."""
        if self.monitoring_thread is None or not self.monitoring_thread.is_alive():
            self.monitoring_thread = threading.Thread(
                target=self._monitor_connection,
                daemon=True,
                name="NetworkMonitor"
            )
            self.monitoring_thread.start()

        if self.queue_processor_thread is None or not self.queue_processor_thread.is_alive():
            self.queue_processor_thread = threading.Thread(
                target=self._process_queue,
                daemon=True,
                name="QueueProcessor"
            )
            self.queue_processor_thread.start()

    def stop_monitoring(self):
        """Stop background monitoring threads."""
        self.shutdown_event.set()
        if self.monitoring_thread and self.monitoring_thread.is_alive():
            self.monitoring_thread.join(timeout=5)
        if self.queue_processor_thread and self.queue_processor_thread.is_alive():
            self.queue_processor_thread.join(timeout=5)

    def check_connectivity(self, timeout: float = 5.0) -> Tuple[bool, float]:
        """
        Check network connectivity with multiple methods.

        Returns:
            Tuple of (is_connected, response_time)
        """
        start_time = time.time()

        # Method 1: Check network interfaces
        try:
            network_stats = psutil.net_if_stats()
            active_interfaces = [
                name for name, stats in network_stats.items()
                if stats.isup and name != 'lo'  # Exclude loopback
            ]
            if not active_interfaces:
                return False, time.time() - start_time
        except Exception:
            pass

        # Method 2: DNS resolution test
        try:
            socket.setdefaulttimeout(timeout)
            socket.gethostbyname('google.com')
        except (socket.gaierror, socket.timeout):
            return False, time.time() - start_time

        # Method 3: HTTP connectivity test
        try:
            response = requests.get(
                'https://httpbin.org/status/200',
                timeout=timeout,
                headers={'User-Agent': 'EbookGenerator-NetworkCheck/1.0'}
            )
            if response.status_code == 200:
                return True, time.time() - start_time
        except (requests.RequestException, requests.Timeout):
            pass

        # Method 4: Alternative HTTP test
        try:
            response = requests.get(
                'https://www.google.com',
                timeout=timeout,
                headers={'User-Agent': 'EbookGenerator-NetworkCheck/1.0'}
            )
            if response.status_code == 200:
                return True, time.time() - start_time
        except (requests.RequestException, requests.Timeout):
            pass

        return False, time.time() - start_time

    def _monitor_connection(self):
        """Background thread to monitor network connection."""
        while not self.shutdown_event.is_set():
            try:
                is_connected, response_time = self.check_connectivity()
                current_time = datetime.now()

                # Determine new status
                if is_connected:
                    if self.metrics.consecutive_failures > 0:
                        new_status = NetworkStatus.UNSTABLE
                        # Reset consecutive failures after successful connection
                        self.metrics.consecutive_failures = 0
                    else:
                        new_status = NetworkStatus.CONNECTED
                    self.metrics.consecutive_successes += 1
                else:
                    new_status = NetworkStatus.DISCONNECTED
                    self.metrics.consecutive_failures += 1
                    self.metrics.consecutive_successes = 0

                # Update metrics
                self.metrics.last_connection_check = current_time
                if is_connected:
                    self.metrics.average_response_time = (
                        (self.metrics.average_response_time * 0.8) + (response_time * 0.2)
                    )

                # Check for status change
                old_status = self.status
                if new_status != old_status:
                    self.status = new_status
                    self.connection_history.append((current_time, new_status))

                    # Notify callbacks
                    for callback in self.status_change_callbacks:
                        try:
                            callback(old_status, new_status)
                        except Exception as e:
                            console.print(f"[yellow]Warning: Status change callback failed: {e}[/yellow]")

                    # Show user feedback
                    if self.show_status_messages:
                        self._show_status_change(old_status, new_status)

                # Update circuit breaker
                self._update_circuit_breaker(is_connected)

                # Keep only last 100 history entries
                if len(self.connection_history) > 100:
                    self.connection_history = self.connection_history[-100:]

            except Exception as e:
                console.print(f"[red]Error in network monitoring: {e}[/red]")

            # Wait before next check
            self.shutdown_event.wait(self.status_check_interval)

    def _update_circuit_breaker(self, is_connected: bool):
        """Update circuit breaker state based on connection status."""
        current_time = datetime.now()

        if self.circuit_state == CircuitBreakerState.CLOSED:
            if not is_connected:
                self.metrics.consecutive_failures += 1
                if self.metrics.consecutive_failures >= self.circuit_config.failure_threshold:
                    self.circuit_state = CircuitBreakerState.OPEN
                    self.circuit_opened_at = current_time
                    if self.show_status_messages:
                        console.print("[bold red]🚫 Circuit breaker OPENED - Failing fast to protect system[/bold red]")

        elif self.circuit_state == CircuitBreakerState.OPEN:
            if self.circuit_opened_at and (
                current_time - self.circuit_opened_at
            ).total_seconds() >= self.circuit_config.recovery_timeout:
                self.circuit_state = CircuitBreakerState.HALF_OPEN
                self.circuit_successes = 0
                if self.show_status_messages:
                    console.print("[bold yellow]🔄 Circuit breaker HALF-OPEN - Testing recovery[/bold yellow]")

        elif self.circuit_state == CircuitBreakerState.HALF_OPEN:
            if is_connected:
                self.circuit_successes += 1
                if self.circuit_successes >= self.circuit_config.success_threshold:
                    self.circuit_state = CircuitBreakerState.CLOSED
                    self.metrics.consecutive_failures = 0
                    if self.show_status_messages:
                        console.print("[bold green]✅ Circuit breaker CLOSED - Normal operation resumed[/bold green]")
            else:
                self.circuit_state = CircuitBreakerState.OPEN
                self.circuit_opened_at = current_time
                self.circuit_successes = 0
                if self.show_status_messages:
                    console.print("[bold red]🚫 Circuit breaker OPEN again - Recovery failed[/bold red]")

    def _show_status_change(self, old_status: NetworkStatus, new_status: NetworkStatus):
        """Show user-friendly status change messages."""
        status_messages = {
            NetworkStatus.CONNECTED: "[bold green]🌐 Network connection stable[/bold green]",
            NetworkStatus.DISCONNECTED: "[bold red]📡 Network connection lost[/bold red]",
            NetworkStatus.UNSTABLE: "[bold yellow]⚠️ Network connection unstable[/bold yellow]",
            NetworkStatus.CHECKING: "[bold blue]🔍 Checking network connection...[/bold blue]"
        }

        if new_status == NetworkStatus.CONNECTED and old_status == NetworkStatus.DISCONNECTED:
            console.print("[bold green]🎉 Network connection restored! Resuming operations...[/bold green]")
        elif new_status == NetworkStatus.DISCONNECTED:
            console.print("[bold red]⚠️ Network connection lost. Requests will be queued for retry.[/bold red]")
        elif new_status == NetworkStatus.UNSTABLE:
            console.print("[bold yellow]⚠️ Network connection unstable. Using enhanced retry logic.[/bold yellow]")

        console.print(status_messages.get(new_status, f"Network status: {new_status.value}"))

    def _process_queue(self):
        """Background thread to process queued requests."""
        while not self.shutdown_event.is_set():
            try:
                # Only process queue if circuit is not open
                if self.circuit_state == CircuitBreakerState.OPEN:
                    self.shutdown_event.wait(5)  # Wait 5 seconds before checking again
                    continue

                # Only process if we have some connectivity
                if self.status == NetworkStatus.DISCONNECTED:
                    self.shutdown_event.wait(10)  # Wait 10 seconds before checking again
                    continue

                try:
                    # Get next request (blocks for up to 5 seconds)
                    priority, request_id, queued_request = self.request_queue.get(timeout=5)

                    # Process the request
                    self._execute_queued_request(queued_request)

                except queue.Empty:
                    continue  # No requests in queue, continue monitoring

            except Exception as e:
                console.print(f"[red]Error in queue processor: {e}[/red]")
                self.shutdown_event.wait(5)

    def _execute_queued_request(self, queued_request: QueuedRequest):
        """Execute a queued request with retry logic."""
        queued_request.last_attempt = datetime.now()
        queued_request.retry_count += 1

        try:
            if self.show_retry_messages and queued_request.retry_count > 1:
                console.print(f"[cyan]🔄 Retrying request {queued_request.id} (attempt {queued_request.retry_count})[/cyan]")

            # Execute the request
            result = queued_request.function(*queued_request.args, **queued_request.kwargs)

            # Success - update metrics and notify callback
            self.metrics.successful_requests += 1
            if queued_request.retry_count > 1:
                self.metrics.retried_requests += 1

            # Remove from active requests
            if queued_request.id in self.active_requests:
                del self.active_requests[queued_request.id]

            # Call success callback if provided
            if queued_request.id in self.request_callbacks:
                callback = self.request_callbacks.pop(queued_request.id)
                try:
                    callback(result, None)
                except Exception as e:
                    console.print(f"[yellow]Warning: Request callback failed: {e}[/yellow]")

            if self.show_retry_messages and queued_request.retry_count > 1:
                console.print(f"[bold green]✅ Request {queued_request.id} succeeded after {queued_request.retry_count} attempts[/bold green]")

        except Exception as e:
            # Failure - decide whether to retry
            error_msg = str(e)
            queued_request.error_history.append(error_msg)
            self.metrics.failed_requests += 1

            if queued_request.retry_count < queued_request.max_retries:
                # Re-queue for retry with exponential backoff
                delay = min(300, 2 ** queued_request.retry_count)  # Max 5 minutes

                if self.show_retry_messages:
                    console.print(f"[yellow]⚠️ Request {queued_request.id} failed (attempt {queued_request.retry_count}). Retrying in {delay}s...[/yellow]")

                # Schedule retry
                threading.Timer(delay, self._requeue_request, args=[queued_request]).start()
            else:
                # Max retries exceeded
                if self.show_retry_messages:
                    console.print(f"[bold red]❌ Request {queued_request.id} failed permanently after {queued_request.retry_count} attempts[/bold red]")

                # Remove from active requests
                if queued_request.id in self.active_requests:
                    del self.active_requests[queued_request.id]

                # Call failure callback if provided
                if queued_request.id in self.request_callbacks:
                    callback = self.request_callbacks.pop(queued_request.id)
                    try:
                        callback(None, e)
                    except Exception as callback_error:
                        console.print(f"[yellow]Warning: Request callback failed: {callback_error}[/yellow]")

    def _requeue_request(self, queued_request: QueuedRequest):
        """Re-queue a failed request for retry."""
        priority_value = queued_request.priority.value
        self.request_queue.put((priority_value, queued_request.id, queued_request))

    def queue_request(
        self,
        request_id: str,
        function: Callable,
        args: tuple = (),
        kwargs: dict = None,
        priority: RequestPriority = RequestPriority.NORMAL,
        max_retries: int = 5,
        callback: Optional[Callable] = None
    ) -> str:
        """
        Queue a network request for execution with retry logic.

        Args:
            request_id: Unique identifier for the request
            function: Function to execute
            args: Arguments for the function
            kwargs: Keyword arguments for the function
            priority: Request priority level
            max_retries: Maximum number of retry attempts
            callback: Optional callback function(result, error)

        Returns:
            Request ID for tracking
        """
        if kwargs is None:
            kwargs = {}

        # Create queued request
        queued_request = QueuedRequest(
            id=request_id,
            function=function,
            args=args,
            kwargs=kwargs,
            priority=priority,
            max_retries=max_retries
        )

        # Store in active requests
        self.active_requests[request_id] = queued_request

        # Store callback if provided
        if callback:
            self.request_callbacks[request_id] = callback

        # Add to queue
        priority_value = priority.value
        self.request_queue.put((priority_value, request_id, queued_request))

        # Update metrics
        self.metrics.total_requests += 1

        if self.show_retry_messages:
            console.print(f"[blue]📤 Queued request {request_id} with priority {priority.name}[/blue]")

        return request_id

    def execute_with_resilience(
        self,
        function: Callable,
        args: tuple = (),
        kwargs: dict = None,
        priority: RequestPriority = RequestPriority.NORMAL,
        max_retries: int = 5,
        timeout: float = 30.0
    ) -> Any:
        """
        Execute a function with network resilience (blocking call).

        Args:
            function: Function to execute
            args: Arguments for the function
            kwargs: Keyword arguments for the function
            priority: Request priority level
            max_retries: Maximum number of retry attempts
            timeout: Maximum time to wait for completion

        Returns:
            Function result

        Raises:
            TimeoutError: If request times out
            Exception: If request fails permanently
        """
        if kwargs is None:
            kwargs = {}

        # Check circuit breaker
        if self.circuit_state == CircuitBreakerState.OPEN:
            raise Exception("Circuit breaker is OPEN - failing fast to protect system")

        # Generate unique request ID
        request_id = f"sync_{int(time.time() * 1000)}_{id(function)}"

        # Use threading event for synchronization
        result_event = threading.Event()
        result_container = {'result': None, 'error': None}

        def callback(result, error):
            result_container['result'] = result
            result_container['error'] = error
            result_event.set()

        # Queue the request
        self.queue_request(
            request_id=request_id,
            function=function,
            args=args,
            kwargs=kwargs,
            priority=priority,
            max_retries=max_retries,
            callback=callback
        )

        # Wait for completion
        if result_event.wait(timeout):
            if result_container['error']:
                raise result_container['error']
            return result_container['result']
        else:
            # Timeout - remove from queue and active requests
            if request_id in self.active_requests:
                del self.active_requests[request_id]
            if request_id in self.request_callbacks:
                del self.request_callbacks[request_id]
            raise TimeoutError(f"Request {request_id} timed out after {timeout} seconds")

    def get_status(self) -> Dict[str, Any]:
        """Get current network status and metrics."""
        return {
            'status': self.status.value,
            'circuit_state': self.circuit_state.value,
            'metrics': {
                'total_requests': self.metrics.total_requests,
                'successful_requests': self.metrics.successful_requests,
                'failed_requests': self.metrics.failed_requests,
                'retried_requests': self.metrics.retried_requests,
                'success_rate': (
                    self.metrics.successful_requests / max(1, self.metrics.total_requests) * 100
                ),
                'average_response_time': self.metrics.average_response_time,
                'consecutive_failures': self.metrics.consecutive_failures,
                'consecutive_successes': self.metrics.consecutive_successes
            },
            'queue': {
                'active_requests': len(self.active_requests),
                'queue_size': self.request_queue.qsize()
            },
            'last_check': self.metrics.last_connection_check.isoformat() if self.metrics.last_connection_check else None
        }

    def show_status_panel(self):
        """Display a detailed status panel."""
        status = self.get_status()

        # Create status table
        table = Table(title="Network Resilience Status", show_header=True, header_style="bold cyan")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="white")

        # Network status
        status_color = {
            'connected': 'green',
            'disconnected': 'red',
            'unstable': 'yellow',
            'checking': 'blue'
        }.get(status['status'], 'white')

        table.add_row("Network Status", f"[{status_color}]{status['status'].upper()}[/{status_color}]")

        # Circuit breaker status
        circuit_color = {
            'closed': 'green',
            'open': 'red',
            'half_open': 'yellow'
        }.get(status['circuit_state'], 'white')

        table.add_row("Circuit Breaker", f"[{circuit_color}]{status['circuit_state'].upper()}[/{circuit_color}]")

        # Metrics
        metrics = status['metrics']
        table.add_row("Total Requests", str(metrics['total_requests']))
        table.add_row("Success Rate", f"{metrics['success_rate']:.1f}%")
        table.add_row("Failed Requests", str(metrics['failed_requests']))
        table.add_row("Retried Requests", str(metrics['retried_requests']))
        table.add_row("Avg Response Time", f"{metrics['average_response_time']:.2f}s")
        table.add_row("Consecutive Failures", str(metrics['consecutive_failures']))
        table.add_row("Consecutive Successes", str(metrics['consecutive_successes']))

        # Queue info
        queue_info = status['queue']
        table.add_row("Active Requests", str(queue_info['active_requests']))
        table.add_row("Queued Requests", str(queue_info['queue_size']))

        # Last check
        if status['last_check']:
            last_check = datetime.fromisoformat(status['last_check'])
            time_ago = datetime.now() - last_check
            table.add_row("Last Check", f"{time_ago.total_seconds():.0f}s ago")

        console.print(table)

    def add_status_change_callback(self, callback: Callable[[NetworkStatus, NetworkStatus], None]):
        """Add a callback for network status changes."""
        self.status_change_callbacks.append(callback)

    def remove_status_change_callback(self, callback: Callable[[NetworkStatus, NetworkStatus], None]):
        """Remove a status change callback."""
        if callback in self.status_change_callbacks:
            self.status_change_callbacks.remove(callback)

    def clear_metrics(self):
        """Clear all metrics and reset counters."""
        self.metrics = NetworkMetrics()
        self.connection_history.clear()

    def get_connection_history(self, limit: int = 50) -> List[Tuple[datetime, str]]:
        """Get recent connection history."""
        return [(timestamp, status.value) for timestamp, status in self.connection_history[-limit:]]

    def is_healthy(self) -> bool:
        """Check if the network connection is healthy."""
        return (
            self.status in [NetworkStatus.CONNECTED, NetworkStatus.UNSTABLE] and
            self.circuit_state != CircuitBreakerState.OPEN
        )

    def force_connectivity_check(self) -> bool:
        """Force an immediate connectivity check."""
        is_connected, response_time = self.check_connectivity()

        # Update status immediately
        current_time = datetime.now()
        old_status = self.status

        if is_connected:
            self.status = NetworkStatus.CONNECTED
            self.metrics.consecutive_failures = 0
            self.metrics.consecutive_successes += 1
        else:
            self.status = NetworkStatus.DISCONNECTED
            self.metrics.consecutive_failures += 1
            self.metrics.consecutive_successes = 0

        self.metrics.last_connection_check = current_time
        self.metrics.average_response_time = response_time

        # Update circuit breaker
        self._update_circuit_breaker(is_connected)

        # Notify callbacks if status changed
        if self.status != old_status:
            self.connection_history.append((current_time, self.status))
            for callback in self.status_change_callbacks:
                try:
                    callback(old_status, self.status)
                except Exception as e:
                    console.print(f"[yellow]Warning: Status change callback failed: {e}[/yellow]")

        return is_connected

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.stop_monitoring()


# Global instance for easy access
_global_resilience_manager: Optional[NetworkResilienceManager] = None

def get_network_manager(config: Optional[Dict[str, Any]] = None) -> NetworkResilienceManager:
    """Get or create the global network resilience manager."""
    global _global_resilience_manager

    if _global_resilience_manager is None:
        _global_resilience_manager = NetworkResilienceManager(config)

    return _global_resilience_manager

def shutdown_network_manager():
    """Shutdown the global network resilience manager."""
    global _global_resilience_manager

    if _global_resilience_manager is not None:
        _global_resilience_manager.stop_monitoring()
        _global_resilience_manager = None
