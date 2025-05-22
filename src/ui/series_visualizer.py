"""
Visualization tools for series data.
"""
import os
from typing import Dict, List, Any, Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.tree import Tree
from rich import box
from rich.progress import BarColumn, Progress

console = Console()


def visualize_character_development(series_manager) -> None:
    """
    Visualize character development across the series.
    
    Args:
        series_manager: SeriesManager instance
    """
    if not series_manager:
        return
    
    console.print("\n[bold cyan]Character Development Across Series[/bold cyan]")
    
    # Get character development data
    character_arcs = series_manager.series_tracking.get("character_arcs", {})
    character_growth = series_manager.series_tracking.get("character_growth", {})
    character_traits = series_manager.series_tracking.get("character_traits", {})
    
    if not character_arcs and not character_growth and not character_traits:
        console.print("[yellow]No character development data available yet.[/yellow]")
        return
    
    # Create a table for each character
    for char_name in set(list(character_arcs.keys()) + list(character_growth.keys()) + list(character_traits.keys())):
        console.print(f"\n[bold cyan]Character: {char_name}[/bold cyan]")
        
        # Create a table for character development across books
        table = Table(box=box.ROUNDED)
        table.add_column("Book #", style="cyan")
        table.add_column("Character Arc", style="green")
        table.add_column("Growth", style="yellow")
        table.add_column("Traits", style="blue")
        
        # Get all book numbers for this character
        book_numbers = set()
        if char_name in character_arcs:
            book_numbers.update(character_arcs[char_name].keys())
        if char_name in character_growth:
            book_numbers.update(character_growth[char_name].keys())
        if char_name in character_traits:
            book_numbers.update(character_traits[char_name].keys())
        
        # Sort book numbers
        book_numbers = sorted([int(bn) for bn in book_numbers])
        
        # Add rows for each book
        for book_num in book_numbers:
            book_num_str = str(book_num)
            
            # Get character arc for this book
            arc = character_arcs.get(char_name, {}).get(book_num_str, "")
            
            # Get character growth for this book
            growth = character_growth.get(char_name, {}).get(book_num_str, "")
            
            # Get character traits for this book
            traits = character_traits.get(char_name, {}).get(book_num_str, "")
            if isinstance(traits, list):
                traits = ", ".join(traits)
            elif isinstance(traits, dict):
                traits = ", ".join([f"{k}: {v}" for k, v in traits.items()])
            
            table.add_row(str(book_num), arc, growth, traits)
        
        console.print(table)


def visualize_plot_arcs(series_manager) -> None:
    """
    Visualize plot arcs across the series.
    
    Args:
        series_manager: SeriesManager instance
    """
    if not series_manager:
        return
    
    console.print("\n[bold cyan]Plot Arcs Across Series[/bold cyan]")
    
    # Get plot arc data
    plot_arcs = series_manager.series_tracking.get("plot_arcs", {})
    plot_progression = series_manager.series_tracking.get("plot_progression", {})
    plot_threads = series_manager.series_tracking.get("plot_threads", {})
    
    if not plot_arcs and not plot_progression and not plot_threads:
        console.print("[yellow]No plot arc data available yet.[/yellow]")
        return
    
    # Create a table for each plot arc
    for arc_name in set(list(plot_arcs.keys()) + list(plot_progression.keys()) + list(plot_threads.keys())):
        console.print(f"\n[bold cyan]Plot Arc: {arc_name}[/bold cyan]")
        
        # Create a table for plot arc progression across books
        table = Table(box=box.ROUNDED)
        table.add_column("Book #", style="cyan")
        table.add_column("Arc Status", style="green")
        table.add_column("Progression", style="yellow")
        
        # Get all book numbers for this arc
        book_numbers = set()
        if arc_name in plot_arcs:
            book_numbers.update(plot_arcs[arc_name].keys())
        if arc_name in plot_progression:
            book_numbers.update(plot_progression[arc_name].keys())
        if arc_name in plot_threads:
            book_numbers.update(plot_threads[arc_name].keys())
        
        # Sort book numbers
        book_numbers = sorted([int(bn) for bn in book_numbers])
        
        # Add rows for each book
        for book_num in book_numbers:
            book_num_str = str(book_num)
            
            # Get arc status for this book
            arc_status = plot_arcs.get(arc_name, {}).get(book_num_str, "")
            if isinstance(arc_status, dict):
                arc_status = arc_status.get("status", "")
            
            # Get progression for this book
            progression = plot_progression.get(arc_name, {}).get(book_num_str, "")
            if isinstance(progression, dict):
                progression = f"{progression.get('percentage', '0')}% - {progression.get('stage', '')}"
            
            table.add_row(str(book_num), arc_status, progression)
        
        console.print(table)
        
        # Create a visual progression bar if we have percentage data
        progression_data = {}
        for book_num in book_numbers:
            book_num_str = str(book_num)
            prog = plot_progression.get(arc_name, {}).get(book_num_str, {})
            if isinstance(prog, dict) and "percentage" in prog:
                try:
                    percentage = float(prog["percentage"].rstrip("%"))
                    progression_data[book_num] = percentage
                except (ValueError, AttributeError):
                    pass
        
        if progression_data:
            console.print("\n[bold cyan]Arc Progression:[/bold cyan]")
            with Progress(
                "{task.description}",
                BarColumn(bar_width=40),
                "[progress.percentage]{task.percentage:>3.0f}%",
            ) as progress:
                for book_num, percentage in sorted(progression_data.items()):
                    task = progress.add_task(f"Book {book_num}", total=100, completed=percentage)


def visualize_timeline(series_manager) -> None:
    """
    Visualize the series timeline.
    
    Args:
        series_manager: SeriesManager instance
    """
    if not series_manager:
        return
    
    console.print("\n[bold cyan]Series Timeline[/bold cyan]")
    
    # Get timeline data
    timeline_events = series_manager.series_tracking.get("timeline_events", [])
    timeline_periods = series_manager.series_tracking.get("timeline_periods", {})
    
    if not timeline_events and not timeline_periods:
        console.print("[yellow]No timeline data available yet.[/yellow]")
        return
    
    # Sort events by chronological order if possible
    if timeline_events:
        # Try to sort by date/time if available
        if "date" in timeline_events[0] or "time" in timeline_events[0]:
            timeline_events.sort(key=lambda x: (x.get("date", ""), x.get("time", "")))
        # Otherwise sort by book number and event order
        else:
            timeline_events.sort(key=lambda x: (x.get("book_number", 0), x.get("order", 0)))
    
    # Create a tree for the timeline
    timeline_tree = Tree("[bold cyan]Timeline[/bold cyan]")
    
    # Add periods to the tree
    periods_tree = timeline_tree.add("[bold yellow]Time Periods[/bold yellow]")
    for period_name, period_data in timeline_periods.items():
        period_node = periods_tree.add(f"[yellow]{period_name}[/yellow]")
        if isinstance(period_data, dict):
            for key, value in period_data.items():
                period_node.add(f"[dim]{key}:[/dim] {value}")
    
    # Add events to the tree
    events_tree = timeline_tree.add("[bold green]Events[/bold green]")
    current_book = None
    book_node = None
    
    for event in timeline_events:
        # Check if we need to create a new book node
        book_number = event.get("book_number")
        if book_number != current_book:
            current_book = book_number
            book_node = events_tree.add(f"[cyan]Book {book_number}[/cyan]")
        
        # Create event node
        event_title = event.get("title", "Unnamed Event")
        event_node = book_node.add(f"[green]{event_title}[/green]")
        
        # Add event details
        for key, value in event.items():
            if key not in ["title", "book_number"]:
                event_node.add(f"[dim]{key}:[/dim] {value}")
    
    console.print(timeline_tree)


def visualize_series_data(series_manager) -> None:
    """
    Visualize all series data.
    
    Args:
        series_manager: SeriesManager instance
    """
    if not series_manager:
        return
    
    console.print("\n[bold cyan]Series Data Visualization[/bold cyan]")
    
    # Visualize character development
    visualize_character_development(series_manager)
    
    # Visualize plot arcs
    visualize_plot_arcs(series_manager)
    
    # Visualize timeline
    visualize_timeline(series_manager)
