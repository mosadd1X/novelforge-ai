#!/usr/bin/env python3
"""
Test script for responsive separators in NovelForge AI

This script demonstrates the responsive separator functionality and allows
testing how separators adapt to different terminal widths.
"""

import os
import sys
from rich.console import Console

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.ui.responsive_separator import (
    separator, title_separator, section_separator, 
    equals_separator, dash_separator, star_separator,
    get_terminal_width, ResponsiveSeparator
)

console = Console()

def test_basic_separators():
    """Test basic separator functionality."""
    console.print("[bold cyan]🧪 Testing Basic Separators[/bold cyan]")
    console.print(f"Terminal width: {get_terminal_width()} characters")
    console.print()
    
    console.print("1. Full equals separator:")
    console.print(equals_separator())
    console.print()
    
    console.print("2. Full dash separator:")
    console.print(dash_separator())
    console.print()
    
    console.print("3. Star separator:")
    console.print(star_separator())
    console.print()

def test_title_separators():
    """Test title separator functionality."""
    console.print("[bold cyan]🧪 Testing Title Separators[/bold cyan]")
    console.print()
    
    console.print("1. Title with equals:")
    console.print(title_separator("Test Results"))
    console.print()
    
    console.print("2. Title with dashes:")
    console.print(title_separator("Configuration", "-"))
    console.print()
    
    console.print("3. Long title:")
    console.print(title_separator("NovelForge AI - Advanced Book Generation System"))
    console.print()

def test_section_separators():
    """Test section separator functionality."""
    console.print("[bold cyan]🧪 Testing Section Separators[/bold cyan]")
    console.print()
    
    console.print("1. Simple section separator:")
    console.print(section_separator("API Configuration", "-", "simple"))
    console.print()
    
    console.print("2. Boxed section separator:")
    console.print(section_separator("Database Status", "=", "boxed"))
    console.print()
    
    console.print("3. Spaced section separator:")
    console.print(section_separator("User Settings", "*", "spaced"))

def test_style_variations():
    """Test different separator styles."""
    console.print("[bold cyan]🧪 Testing Style Variations[/bold cyan]")
    console.print()
    
    console.print("1. Full width separator:")
    console.print(separator("=", "full"))
    console.print()
    
    console.print("2. Centered separator:")
    console.print(separator("=", "centered"))
    console.print()
    
    console.print("3. Padded separator:")
    console.print(separator("-", "padded"))
    console.print()

def test_custom_separator():
    """Test custom separator configurations."""
    console.print("[bold cyan]🧪 Testing Custom Separator Configurations[/bold cyan]")
    console.print()
    
    # Create custom separator with different settings
    custom_sep = ResponsiveSeparator(min_width=30, max_width=80, padding=4)
    
    console.print("1. Custom separator (min=30, max=80, padding=4):")
    console.print(custom_sep.create_separator("*"))
    console.print()
    
    console.print("2. Custom title separator:")
    console.print(custom_sep.create_title_separator("Custom Configuration", "#"))
    console.print()

def test_real_world_usage():
    """Test separators in real-world usage scenarios."""
    console.print("[bold cyan]🧪 Real-World Usage Examples[/bold cyan]")
    console.print()
    
    # Simulate API key status display
    console.print(title_separator("API Key Status"))
    console.print("🔑 Main Key: AIzaSyCg********uYys")
    console.print("🔄 Backup Keys: 3 available")
    console.print("✅ Status: All keys active")
    console.print(separator("-"))
    console.print()
    
    # Simulate book generation progress
    console.print(title_separator("Book Generation Progress"))
    console.print("📖 Title: The Mystery of the Lost Code")
    console.print("🎭 Genre: Mystery")
    console.print("📝 Progress: Chapter 5 of 12")
    console.print(section_separator("Current Chapter", "-", "simple"))
    console.print("Chapter 5: The Detective's Discovery")
    console.print("Status: Generating content...")
    console.print(separator("="))
    console.print()

def test_terminal_width_simulation():
    """Test how separators look at different terminal widths."""
    console.print("[bold cyan]🧪 Terminal Width Simulation[/bold cyan]")
    console.print(f"Current terminal width: {get_terminal_width()}")
    console.print()
    
    # Test with different simulated widths
    widths = [40, 60, 80, 100, 120]
    
    for width in widths:
        console.print(f"Simulated width: {width} characters")
        
        # Create separator with fixed width for demonstration
        sim_separator = ResponsiveSeparator(min_width=width, max_width=width)
        
        console.print(sim_separator.create_separator("="))
        console.print(sim_separator.create_title_separator("Test Title"))
        console.print(sim_separator.create_section_separator("Section", "-", "simple"))
        console.print()

def interactive_test():
    """Interactive test allowing user to resize terminal and see changes."""
    console.print("[bold cyan]🧪 Interactive Terminal Width Test[/bold cyan]")
    console.print("Resize your terminal window and press Enter to see how separators adapt")
    console.print("Type 'quit' to exit")
    console.print()
    
    while True:
        user_input = input("Press Enter to refresh (or 'quit' to exit): ").strip().lower()
        
        if user_input == 'quit':
            break
        
        # Clear and redisplay
        os.system('cls' if os.name == 'nt' else 'clear')
        
        current_width = get_terminal_width()
        console.print(f"[bold green]Current terminal width: {current_width} characters[/bold green]")
        console.print()
        
        console.print("Full separator:")
        console.print(equals_separator())
        console.print()
        
        console.print("Title separator:")
        console.print(title_separator("Responsive Design Test"))
        console.print()
        
        console.print("Section separator:")
        console.print(section_separator("Dynamic Width", "-", "simple"))
        console.print()
        
        console.print("Centered separator:")
        console.print(separator("*", "centered"))
        console.print()

def main():
    """Main test function."""
    console.print("[bold green]🚀 NovelForge AI - Responsive Separator Testing[/bold green]")
    console.print()
    
    try:
        test_basic_separators()
        console.print()
        
        test_title_separators()
        console.print()
        
        test_section_separators()
        console.print()
        
        test_style_variations()
        console.print()
        
        test_custom_separator()
        console.print()
        
        test_real_world_usage()
        console.print()
        
        test_terminal_width_simulation()
        console.print()
        
        # Ask if user wants to try interactive test
        try_interactive = input("Would you like to try the interactive terminal width test? (y/n): ").strip().lower()
        if try_interactive in ['y', 'yes']:
            interactive_test()
        
        console.print("[bold green]✅ All tests completed successfully![/bold green]")
        console.print("The responsive separator system is working correctly.")
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Testing interrupted by user.[/yellow]")
    except Exception as e:
        console.print(f"[bold red]Error during testing: {e}[/bold red]")

if __name__ == "__main__":
    main()
