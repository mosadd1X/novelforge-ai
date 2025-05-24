#!/usr/bin/env python3
"""
Network Resilience System Demo

This script demonstrates the network resilience capabilities of the ebook generator.
It shows how the system handles network issues, retries, and provides user feedback.
"""

import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

def demo_network_monitoring():
    """Demonstrate network monitoring capabilities."""
    console.print(Panel.fit(
        "[bold cyan]Network Monitoring Demo[/bold cyan]\n"
        "Showing real-time network status monitoring",
        style="cyan"
    ))
    
    try:
        from src.utils.network_resilience import get_network_manager
        
        # Get network manager
        network_manager = get_network_manager()
        
        console.print("\n[bold green]✅ Network Resilience Manager initialized[/bold green]")
        
        # Show current status
        console.print("\n[bold cyan]Current Network Status:[/bold cyan]")
        network_manager.show_status_panel()
        
        # Force connectivity check
        console.print("\n[cyan]Performing connectivity check...[/cyan]")
        is_connected = network_manager.force_connectivity_check()
        
        if is_connected:
            console.print("[bold green]🌐 Network connection: STABLE[/bold green]")
        else:
            console.print("[bold red]📡 Network connection: ISSUES DETECTED[/bold red]")
        
        return True
        
    except ImportError as e:
        console.print(f"[bold red]❌ Import error: {e}[/bold red]")
        console.print("[yellow]Make sure to install: pip install requests psutil[/yellow]")
        return False
    except Exception as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")
        return False

def demo_enhanced_error_handling():
    """Demonstrate enhanced error handling."""
    console.print(Panel.fit(
        "[bold cyan]Enhanced Error Handling Demo[/bold cyan]\n"
        "Showing improved error messages and troubleshooting guidance",
        style="cyan"
    ))
    
    try:
        from src.core.gemini_client import GeminiClient
        
        console.print("\n[cyan]Testing enhanced Gemini client error handling...[/cyan]")
        
        # This will show the enhanced error handling if there are network issues
        client = GeminiClient()
        
        # Test API connection with enhanced feedback
        console.print("\n[cyan]Checking API connection with enhanced feedback...[/cyan]")
        api_status = client.check_api_connection(check_all_keys=True)
        
        if api_status["success"]:
            console.print("[bold green]✅ API connection successful[/bold green]")
            console.print(f"[green]Working keys: {api_status['working_keys']}/{api_status['active_keys']}[/green]")
        else:
            console.print("[bold yellow]⚠️ API connection issues detected[/bold yellow]")
            console.print("[yellow]The enhanced error handling will provide guidance[/yellow]")
        
        return True
        
    except Exception as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")
        return False

def demo_user_feedback():
    """Demonstrate user feedback features."""
    console.print(Panel.fit(
        "[bold cyan]User Feedback Demo[/bold cyan]\n"
        "Showing network status UI and diagnostics",
        style="cyan"
    ))
    
    try:
        from src.ui.network_status_ui import NetworkStatusUI
        
        console.print("\n[bold green]✅ Network Status UI available[/bold green]")
        
        # Create UI instance
        network_ui = NetworkStatusUI()
        
        # Show quick status
        console.print("\n[bold cyan]Quick Network Status:[/bold cyan]")
        network_ui.show_quick_status()
        
        # Show that detailed status is available
        console.print("\n[cyan]Detailed status and diagnostics are available through:[/cyan]")
        console.print("• python run.py → Network Status & Diagnostics")
        console.print("• Interactive menus with real-time monitoring")
        console.print("• Network diagnostics and troubleshooting")
        
        return True
        
    except ImportError as e:
        console.print(f"[bold red]❌ Import error: {e}[/bold red]")
        console.print("[yellow]Make sure to install: pip install requests psutil[/yellow]")
        return False
    except Exception as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")
        return False

def demo_integration():
    """Demonstrate integration with main application."""
    console.print(Panel.fit(
        "[bold cyan]Integration Demo[/bold cyan]\n"
        "Showing how network resilience integrates with the main application",
        style="cyan"
    ))
    
    console.print("\n[bold green]✅ Network resilience is integrated into:[/bold green]")
    console.print("• Main application (src/main.py)")
    console.print("• Enhanced Gemini client (src/core/gemini_client.py)")
    console.print("• New resilient client (src/core/resilient_gemini_client.py)")
    console.print("• Main menu (run.py) - option 7")
    
    console.print("\n[bold cyan]Key Features Available:[/bold cyan]")
    console.print("🌐 Real-time network monitoring")
    console.print("🔄 Intelligent retry with exponential backoff")
    console.print("📋 Request queuing during outages")
    console.print("🛡️ Circuit breaker protection")
    console.print("📊 Detailed status and diagnostics")
    console.print("💾 Response caching and offline mode")
    console.print("🎯 Enhanced error messages with guidance")
    
    console.print("\n[bold yellow]To access network features:[/bold yellow]")
    console.print("1. Run: python run.py")
    console.print("2. Select: '7. Network Status & Diagnostics'")
    console.print("3. Explore the monitoring and diagnostic tools")
    
    return True

def main():
    """Run the network resilience demonstration."""
    console.print(Panel.fit(
        "[bold green]🛡️ Network Resilience System Demo[/bold green]\n"
        "Demonstrating robust network handling for unstable WiFi connections",
        style="green"
    ))
    
    demos = [
        ("Network Monitoring", demo_network_monitoring),
        ("Enhanced Error Handling", demo_enhanced_error_handling),
        ("User Feedback Features", demo_user_feedback),
        ("System Integration", demo_integration)
    ]
    
    for demo_name, demo_func in demos:
        console.print(f"\n{'='*60}")
        console.print(f"[bold yellow]{demo_name}[/bold yellow]")
        console.print('='*60)
        
        try:
            demo_func()
        except Exception as e:
            console.print(f"[bold red]❌ Demo failed: {e}[/bold red]")
        
        # Small pause between demos
        time.sleep(1)
    
    # Final summary
    console.print(f"\n{'='*60}")
    console.print("[bold cyan]Demo Complete![/bold cyan]")
    console.print('='*60)
    
    console.print("\n[bold green]🎉 Network Resilience System is ready![/bold green]")
    console.print("\n[bold cyan]Next Steps:[/bold cyan]")
    console.print("1. Run 'python run.py' to access the main application")
    console.print("2. Try generating content to see resilience in action")
    console.print("3. Use 'Network Status & Diagnostics' to monitor network health")
    console.print("4. Test with unstable WiFi to see automatic retry and queuing")
    
    console.print("\n[bold yellow]For testing:[/bold yellow]")
    console.print("• Run 'python test_network_resilience.py' for comprehensive tests")
    console.print("• Check 'NETWORK_RESILIENCE_SYSTEM.md' for detailed documentation")
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Demo interrupted by user[/bold yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[bold red]Demo failed with error: {e}[/bold red]")
        sys.exit(1)
