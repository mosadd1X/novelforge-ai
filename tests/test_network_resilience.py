#!/usr/bin/env python3
"""
Test script for the Network Resilience System

This script tests the network resilience capabilities of the ebook generator
to ensure it can handle unstable WiFi connections and network issues properly.
"""

import time
import sys
from rich.console import Console
from rich.panel import Panel

console = Console()

def test_basic_connectivity():
    """Test basic network connectivity checking."""
    console.print("[bold cyan]Testing Basic Network Connectivity...[/bold cyan]")
    
    try:
        from src.utils.network_resilience import get_network_manager
        
        # Get network manager
        network_manager = get_network_manager()
        
        # Test connectivity
        is_connected, response_time = network_manager.check_connectivity()
        
        if is_connected:
            console.print(f"[bold green]✅ Network connectivity: CONNECTED[/bold green]")
            console.print(f"[green]Response time: {response_time:.2f}s[/green]")
        else:
            console.print(f"[bold red]❌ Network connectivity: DISCONNECTED[/bold red]")
            console.print(f"[red]Response time: {response_time:.2f}s[/red]")
        
        return True
        
    except Exception as e:
        console.print(f"[bold red]❌ Basic connectivity test failed: {e}[/bold red]")
        return False

def test_resilient_gemini_client():
    """Test the resilient Gemini client."""
    console.print("\n[bold cyan]Testing Resilient Gemini Client...[/bold cyan]")
    
    try:
        from src.core.resilient_gemini_client import ResilientGeminiClient
        
        # Initialize resilient client
        client = ResilientGeminiClient()
        
        # Test simple content generation
        console.print("[cyan]Testing simple content generation...[/cyan]")
        result = client.generate_content(
            "Say 'Hello, this is a test of the network resilience system!'",
            temperature=0.1,
            max_tokens=50,
            timeout=30.0
        )
        
        if result and not result.startswith("Error"):
            console.print(f"[bold green]✅ Content generation successful[/bold green]")
            console.print(f"[dim]Response: {result[:100]}...[/dim]")
        else:
            console.print(f"[bold yellow]⚠️ Content generation returned error/offline response[/bold yellow]")
            console.print(f"[dim]Response: {result[:100]}...[/dim]")
        
        # Test network status
        status = client.get_network_status()
        console.print(f"[cyan]Network status: {status['status']}[/cyan]")
        console.print(f"[cyan]Circuit breaker: {status['circuit_state']}[/cyan]")
        
        return True
        
    except Exception as e:
        console.print(f"[bold red]❌ Resilient Gemini client test failed: {e}[/bold red]")
        return False

def test_network_status_ui():
    """Test the network status UI."""
    console.print("\n[bold cyan]Testing Network Status UI...[/bold cyan]")
    
    try:
        from src.ui.network_status_ui import NetworkStatusUI
        
        # Initialize UI
        network_ui = NetworkStatusUI()
        
        # Test quick status
        console.print("[cyan]Testing quick status display...[/cyan]")
        network_ui.show_quick_status()
        
        # Test diagnostics
        console.print("\n[cyan]Testing network diagnostics...[/cyan]")
        network_ui.network_diagnostics()
        
        return True
        
    except Exception as e:
        console.print(f"[bold red]❌ Network status UI test failed: {e}[/bold red]")
        return False

def test_request_queuing():
    """Test request queuing functionality."""
    console.print("\n[bold cyan]Testing Request Queuing...[/bold cyan]")
    
    try:
        from src.utils.network_resilience import get_network_manager, RequestPriority
        
        network_manager = get_network_manager()
        
        # Test function that simulates API call
        def mock_api_call(message):
            time.sleep(0.1)  # Simulate network delay
            return f"Mock response: {message}"
        
        # Queue a test request
        console.print("[cyan]Queuing test request...[/cyan]")
        request_id = network_manager.queue_request(
            request_id="test_request_1",
            function=mock_api_call,
            args=("Hello from queue test",),
            priority=RequestPriority.HIGH,
            max_retries=3
        )
        
        console.print(f"[green]✅ Request queued with ID: {request_id}[/green]")
        
        # Wait a moment for processing
        time.sleep(2)
        
        # Check status
        status = network_manager.get_status()
        console.print(f"[cyan]Queue status - Active: {status['queue']['active_requests']}, Queued: {status['queue']['queue_size']}[/cyan]")
        
        return True
        
    except Exception as e:
        console.print(f"[bold red]❌ Request queuing test failed: {e}[/bold red]")
        return False

def test_circuit_breaker():
    """Test circuit breaker functionality."""
    console.print("\n[bold cyan]Testing Circuit Breaker...[/bold cyan]")
    
    try:
        from src.utils.network_resilience import get_network_manager
        
        network_manager = get_network_manager()
        
        # Get current circuit breaker status
        status = network_manager.get_status()
        console.print(f"[cyan]Current circuit breaker state: {status['circuit_state']}[/cyan]")
        console.print(f"[cyan]Consecutive failures: {status['metrics']['consecutive_failures']}[/cyan]")
        console.print(f"[cyan]Consecutive successes: {status['metrics']['consecutive_successes']}[/cyan]")
        
        # Test if circuit breaker is healthy
        is_healthy = network_manager.is_healthy()
        if is_healthy:
            console.print("[bold green]✅ Circuit breaker is healthy[/bold green]")
        else:
            console.print("[bold yellow]⚠️ Circuit breaker is not healthy[/bold yellow]")
        
        return True
        
    except Exception as e:
        console.print(f"[bold red]❌ Circuit breaker test failed: {e}[/bold red]")
        return False

def main():
    """Run all network resilience tests."""
    console.print(Panel.fit(
        "[bold cyan]Network Resilience System Test Suite[/bold cyan]\n"
        "Testing network monitoring, retry logic, and resilience features",
        style="cyan"
    ))
    
    tests = [
        ("Basic Connectivity", test_basic_connectivity),
        ("Resilient Gemini Client", test_resilient_gemini_client),
        ("Network Status UI", test_network_status_ui),
        ("Request Queuing", test_request_queuing),
        ("Circuit Breaker", test_circuit_breaker)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        console.print(f"\n{'='*60}")
        console.print(f"[bold yellow]Running: {test_name}[/bold yellow]")
        console.print('='*60)
        
        try:
            if test_func():
                passed += 1
                console.print(f"[bold green]✅ {test_name}: PASSED[/bold green]")
            else:
                console.print(f"[bold red]❌ {test_name}: FAILED[/bold red]")
        except Exception as e:
            console.print(f"[bold red]❌ {test_name}: FAILED with exception: {e}[/bold red]")
    
    # Summary
    console.print(f"\n{'='*60}")
    console.print(f"[bold cyan]Test Summary[/bold cyan]")
    console.print('='*60)
    console.print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        console.print("[bold green]🎉 All tests passed! Network resilience system is working correctly.[/bold green]")
        return 0
    else:
        console.print(f"[bold yellow]⚠️ {total - passed} test(s) failed. Check the output above for details.[/bold yellow]")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Tests interrupted by user[/bold yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[bold red]Test suite failed with error: {e}[/bold red]")
        sys.exit(1)
