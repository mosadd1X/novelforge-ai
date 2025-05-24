"""
Network Status UI Components

This module provides user interface components for displaying network status,
connection health, and resilience metrics in a user-friendly way.
"""

import time
from datetime import datetime
from typing import Dict, Any, List
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich import box
import questionary
from src.utils.network_resilience import get_network_manager

console = Console()

class NetworkStatusUI:
    """User interface for network status monitoring and control."""
    
    def __init__(self):
        """Initialize the network status UI."""
        self.network_manager = get_network_manager()
    
    def show_quick_status(self):
        """Show a quick network status summary."""
        status = self.network_manager.get_status()
        
        # Status indicator
        status_indicators = {
            'connected': '🟢',
            'disconnected': '🔴',
            'unstable': '🟡',
            'checking': '🔵'
        }
        
        circuit_indicators = {
            'closed': '✅',
            'open': '🚫',
            'half_open': '🔄'
        }
        
        indicator = status_indicators.get(status['status'], '❓')
        circuit_indicator = circuit_indicators.get(status['circuit_state'], '❓')
        
        success_rate = status['metrics']['success_rate']
        
        console.print(
            f"{indicator} Network: {status['status'].upper()} | "
            f"{circuit_indicator} Circuit: {status['circuit_state'].upper()} | "
            f"Success Rate: {success_rate:.1f}%"
        )
    
    def show_detailed_status(self):
        """Show detailed network status information."""
        status = self.network_manager.get_status()
        
        # Create main layout
        layout = Layout()
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3)
        )
        
        # Header
        header_text = Text("Network Resilience Status Dashboard", style="bold cyan")
        layout["header"].update(Panel(header_text, style="cyan"))
        
        # Main content
        layout["main"].split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        
        # Left panel - Current Status
        status_table = self._create_status_table(status)
        layout["left"].update(Panel(status_table, title="Current Status", style="green"))
        
        # Right panel - Metrics
        metrics_table = self._create_metrics_table(status)
        layout["right"].update(Panel(metrics_table, title="Performance Metrics", style="blue"))
        
        # Footer
        footer_text = Text("Press Ctrl+C to return to menu", style="dim")
        layout["footer"].update(Panel(footer_text, style="dim"))
        
        console.print(layout)
    
    def _create_status_table(self, status: Dict[str, Any]) -> Table:
        """Create a table showing current network status."""
        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Property", style="cyan")
        table.add_column("Value", style="white")
        
        # Network status with color coding
        status_colors = {
            'connected': 'green',
            'disconnected': 'red',
            'unstable': 'yellow',
            'checking': 'blue'
        }
        
        status_color = status_colors.get(status['status'], 'white')
        table.add_row("Network Status", f"[{status_color}]{status['status'].upper()}[/{status_color}]")
        
        # Circuit breaker status
        circuit_colors = {
            'closed': 'green',
            'open': 'red',
            'half_open': 'yellow'
        }
        
        circuit_color = circuit_colors.get(status['circuit_state'], 'white')
        table.add_row("Circuit Breaker", f"[{circuit_color}]{status['circuit_state'].upper()}[/{circuit_color}]")
        
        # Queue information
        queue_info = status['queue']
        table.add_row("Active Requests", str(queue_info['active_requests']))
        table.add_row("Queued Requests", str(queue_info['queue_size']))
        
        # Last check
        if status['last_check']:
            last_check = datetime.fromisoformat(status['last_check'])
            time_ago = datetime.now() - last_check
            table.add_row("Last Check", f"{time_ago.total_seconds():.0f}s ago")
        else:
            table.add_row("Last Check", "Never")
        
        return table
    
    def _create_metrics_table(self, status: Dict[str, Any]) -> Table:
        """Create a table showing performance metrics."""
        table = Table(show_header=False, box=box.SIMPLE)
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="white")
        
        metrics = status['metrics']
        
        # Request statistics
        table.add_row("Total Requests", str(metrics['total_requests']))
        table.add_row("Successful", str(metrics['successful_requests']))
        table.add_row("Failed", str(metrics['failed_requests']))
        table.add_row("Retried", str(metrics['retried_requests']))
        
        # Success rate with color coding
        success_rate = metrics['success_rate']
        if success_rate >= 95:
            rate_color = 'green'
        elif success_rate >= 80:
            rate_color = 'yellow'
        else:
            rate_color = 'red'
        
        table.add_row("Success Rate", f"[{rate_color}]{success_rate:.1f}%[/{rate_color}]")
        
        # Response time
        avg_time = metrics['average_response_time']
        if avg_time <= 2.0:
            time_color = 'green'
        elif avg_time <= 5.0:
            time_color = 'yellow'
        else:
            time_color = 'red'
        
        table.add_row("Avg Response Time", f"[{time_color}]{avg_time:.2f}s[/{time_color}]")
        
        # Consecutive counters
        table.add_row("Consecutive Failures", str(metrics['consecutive_failures']))
        table.add_row("Consecutive Successes", str(metrics['consecutive_successes']))
        
        return table
    
    def show_connection_history(self, limit: int = 20):
        """Show recent connection history."""
        history = self.network_manager.get_connection_history(limit)
        
        if not history:
            console.print("[yellow]No connection history available[/yellow]")
            return
        
        table = Table(title="Recent Connection History", show_header=True, header_style="bold cyan")
        table.add_column("Time", style="cyan")
        table.add_column("Status", style="white")
        table.add_column("Duration", style="dim")
        
        for i, (timestamp, status) in enumerate(history):
            # Calculate duration since previous status
            if i > 0:
                prev_timestamp = history[i-1][0]
                duration = timestamp - prev_timestamp
                duration_str = str(duration).split('.')[0]  # Remove microseconds
            else:
                duration_str = "-"
            
            # Color code status
            status_colors = {
                'connected': 'green',
                'disconnected': 'red',
                'unstable': 'yellow',
                'checking': 'blue'
            }
            
            status_color = status_colors.get(status, 'white')
            time_str = timestamp.strftime("%H:%M:%S")
            
            table.add_row(
                time_str,
                f"[{status_color}]{status.upper()}[/{status_color}]",
                duration_str
            )
        
        console.print(table)
    
    def show_live_monitoring(self, duration: int = 60):
        """Show live network monitoring for a specified duration."""
        console.print(f"[bold cyan]Starting live network monitoring for {duration} seconds...[/bold cyan]")
        console.print("[dim]Press Ctrl+C to stop early[/dim]")
        
        start_time = time.time()
        
        def generate_live_display():
            current_time = time.time()
            elapsed = current_time - start_time
            remaining = max(0, duration - elapsed)
            
            status = self.network_manager.get_status()
            
            # Create layout
            layout = Layout()
            layout.split_column(
                Layout(name="header", size=3),
                Layout(name="status", size=10),
                Layout(name="metrics", size=8),
                Layout(name="footer", size=3)
            )
            
            # Header with timer
            header_text = Text(f"Live Network Monitoring - {remaining:.0f}s remaining", style="bold cyan")
            layout["header"].update(Panel(header_text, style="cyan"))
            
            # Status
            status_table = self._create_status_table(status)
            layout["status"].update(Panel(status_table, title="Current Status", style="green"))
            
            # Metrics
            metrics_table = self._create_metrics_table(status)
            layout["metrics"].update(Panel(metrics_table, title="Metrics", style="blue"))
            
            # Footer
            footer_text = Text("Press Ctrl+C to stop monitoring", style="dim")
            layout["footer"].update(Panel(footer_text, style="dim"))
            
            return layout
        
        try:
            with Live(generate_live_display(), refresh_per_second=2) as live:
                while time.time() - start_time < duration:
                    time.sleep(0.5)
                    live.update(generate_live_display())
        except KeyboardInterrupt:
            console.print("\n[yellow]Live monitoring stopped by user[/yellow]")
        
        console.print("[bold green]Live monitoring completed[/bold green]")
    
    def network_diagnostics(self):
        """Run network diagnostics and show results."""
        console.print("[bold cyan]Running network diagnostics...[/bold cyan]")
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            transient=True,
        ) as progress:
            
            # Test 1: Force connectivity check
            task1 = progress.add_task("Testing basic connectivity...", total=None)
            is_connected = self.network_manager.force_connectivity_check()
            progress.update(task1, completed=True)
            
            # Test 2: Check response time
            task2 = progress.add_task("Measuring response time...", total=None)
            start_time = time.time()
            self.network_manager.check_connectivity(timeout=10.0)
            response_time = time.time() - start_time
            progress.update(task2, completed=True)
            
            # Test 3: Check circuit breaker
            task3 = progress.add_task("Checking circuit breaker status...", total=None)
            status = self.network_manager.get_status()
            progress.update(task3, completed=True)
        
        # Show results
        results_table = Table(title="Network Diagnostics Results", show_header=True, header_style="bold cyan")
        results_table.add_column("Test", style="cyan")
        results_table.add_column("Result", style="white")
        results_table.add_column("Status", style="white")
        
        # Connectivity test
        conn_status = "✅ PASS" if is_connected else "❌ FAIL"
        conn_color = "green" if is_connected else "red"
        results_table.add_row(
            "Basic Connectivity",
            "Connected" if is_connected else "Disconnected",
            f"[{conn_color}]{conn_status}[/{conn_color}]"
        )
        
        # Response time test
        if response_time <= 2.0:
            time_status = "✅ EXCELLENT"
            time_color = "green"
        elif response_time <= 5.0:
            time_status = "⚠️ ACCEPTABLE"
            time_color = "yellow"
        else:
            time_status = "❌ POOR"
            time_color = "red"
        
        results_table.add_row(
            "Response Time",
            f"{response_time:.2f}s",
            f"[{time_color}]{time_status}[/{time_color}]"
        )
        
        # Circuit breaker test
        circuit_state = status['circuit_state']
        if circuit_state == 'closed':
            circuit_status = "✅ HEALTHY"
            circuit_color = "green"
        elif circuit_state == 'half_open':
            circuit_status = "⚠️ RECOVERING"
            circuit_color = "yellow"
        else:
            circuit_status = "❌ OPEN"
            circuit_color = "red"
        
        results_table.add_row(
            "Circuit Breaker",
            circuit_state.upper(),
            f"[{circuit_color}]{circuit_status}[/{circuit_color}]"
        )
        
        console.print(results_table)
        
        # Recommendations
        if not is_connected:
            console.print("\n[bold red]🚨 Recommendations:[/bold red]")
            console.print("• Check your internet connection")
            console.print("• Verify WiFi is connected and stable")
            console.print("• Try moving closer to your router")
            console.print("• Consider using ethernet cable for stability")
        elif response_time > 5.0:
            console.print("\n[bold yellow]⚠️ Recommendations:[/bold yellow]")
            console.print("• Connection is slow - consider upgrading internet plan")
            console.print("• Check for background downloads or streaming")
            console.print("• Try restarting your router")
        elif circuit_state != 'closed':
            console.print("\n[bold yellow]⚠️ Recommendations:[/bold yellow]")
            console.print("• System is protecting against network issues")
            console.print("• Wait for automatic recovery")
            console.print("• Check network stability")
    
    def interactive_menu(self):
        """Show interactive network status menu."""
        while True:
            console.print("\n[bold cyan]Network Status & Diagnostics Menu[/bold cyan]")
            
            choices = [
                "Show Quick Status",
                "Show Detailed Status",
                "View Connection History",
                "Live Monitoring (60s)",
                "Run Network Diagnostics",
                "Force Connectivity Check",
                "Clear Network Metrics",
                "Return to Main Menu"
            ]
            
            choice = questionary.select(
                "What would you like to do?",
                choices=choices
            ).ask()
            
            if choice == "Show Quick Status":
                self.show_quick_status()
            elif choice == "Show Detailed Status":
                self.show_detailed_status()
            elif choice == "View Connection History":
                self.show_connection_history()
            elif choice == "Live Monitoring (60s)":
                self.show_live_monitoring()
            elif choice == "Run Network Diagnostics":
                self.network_diagnostics()
            elif choice == "Force Connectivity Check":
                console.print("[cyan]Forcing connectivity check...[/cyan]")
                is_connected = self.network_manager.force_connectivity_check()
                status = "Connected" if is_connected else "Disconnected"
                color = "green" if is_connected else "red"
                console.print(f"[{color}]Result: {status}[/{color}]")
            elif choice == "Clear Network Metrics":
                self.network_manager.clear_metrics()
                console.print("[bold green]✅ Network metrics cleared[/bold green]")
            elif choice == "Return to Main Menu":
                break
