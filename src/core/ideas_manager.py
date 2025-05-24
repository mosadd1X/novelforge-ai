#!/usr/bin/env python3
"""
Ideas Manager for the Ebook Generator.

This module handles loading, managing, and selecting from pre-defined book and series ideas
stored in JSON files. It provides functionality to import ideas and auto-populate
creation forms for both individual books and series.
"""

import json
from typing import Dict, List, Optional, Any
from pathlib import Path

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import questionary
from questionary import Style

console = Console()

# Custom questionary style
custom_style = Style([
    ('qmark', 'fg:cyan bold'),
    ('question', 'fg:white bold'),
    ('answer', 'fg:green bold'),
    ('pointer', 'fg:cyan bold'),
    ('highlighted', 'fg:cyan bold'),
    ('selected', 'fg:green bold'),
    ('separator', 'fg:cyan'),
    ('instruction', 'fg:white'),
    ('text', 'fg:white'),
    ('disabled', 'fg:gray'),
])


class IdeasManager:
    """Manages book and series ideas from JSON files."""
    
    def __init__(self):
        """Initialize the ideas manager."""
        self.data_dir = Path("src/data")
        self.book_ideas_file = self.data_dir / "book_ideas.json"
        self.series_ideas_file = self.data_dir / "series_ideas.json"
        
        self.book_ideas = {}
        self.series_ideas = {}
        
        self._load_ideas()
    
    def _load_ideas(self) -> None:
        """Load ideas from JSON files."""
        try:
            # Load book ideas
            if self.book_ideas_file.exists():
                with open(self.book_ideas_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.book_ideas = data.get('book_ideas', {})
            
            # Load series ideas
            if self.series_ideas_file.exists():
                with open(self.series_ideas_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.series_ideas = data.get('series_ideas', {})
                    
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load ideas files: {e}[/yellow]")
            self.book_ideas = {}
            self.series_ideas = {}
    
    def get_available_book_genres(self) -> List[str]:
        """Get list of available genres for book ideas."""
        return list(self.book_ideas.keys())
    
    def get_available_series_genres(self) -> List[str]:
        """Get list of available genres for series ideas."""
        return list(self.series_ideas.keys())
    
    def get_book_ideas_by_genre(self, genre: str) -> List[Dict[str, Any]]:
        """Get book ideas for a specific genre."""
        return self.book_ideas.get(genre, [])
    
    def get_series_ideas_by_genre(self, genre: str) -> List[Dict[str, Any]]:
        """Get series ideas for a specific genre."""
        return self.series_ideas.get(genre, [])
    
    def display_book_ideas_table(self, genre: str) -> None:
        """Display book ideas for a genre in a table format."""
        ideas = self.get_book_ideas_by_genre(genre)
        
        if not ideas:
            console.print(f"[yellow]No book ideas found for genre: {genre}[/yellow]")
            return
        
        table = Table(title=f"Book Ideas - {genre.replace('_', ' ').title()}")
        table.add_column("ID", style="cyan", width=4)
        table.add_column("Title", style="bold green", width=30)
        table.add_column("Description", style="white", width=60)
        
        for i, idea in enumerate(ideas, 1):
            description = idea.get('description', 'No description available')
            # Truncate long descriptions
            if len(description) > 100:
                description = description[:97] + "..."
            
            table.add_row(
                str(i),
                idea.get('title', 'Untitled'),
                description
            )
        
        console.print(table)
    
    def display_series_ideas_table(self, genre: str) -> None:
        """Display series ideas for a genre in a table format."""
        ideas = self.get_series_ideas_by_genre(genre)
        
        if not ideas:
            console.print(f"[yellow]No series ideas found for genre: {genre}[/yellow]")
            return
        
        table = Table(title=f"Series Ideas - {genre.replace('_', ' ').title()}")
        table.add_column("ID", style="cyan", width=4)
        table.add_column("Series Title", style="bold green", width=25)
        table.add_column("Description", style="white", width=45)
        table.add_column("Books", style="yellow", width=8)
        
        for i, idea in enumerate(ideas, 1):
            description = idea.get('description', 'No description available')
            # Truncate long descriptions
            if len(description) > 80:
                description = description[:77] + "..."
            
            book_count = idea.get('book_count', len(idea.get('books', [])))
            
            table.add_row(
                str(i),
                idea.get('title', 'Untitled Series'),
                description,
                str(book_count)
            )
        
        console.print(table)
    
    def select_book_idea(self) -> Optional[Dict[str, Any]]:
        """
        Interactive selection of a book idea.
        
        Returns:
            Selected book idea dictionary or None if cancelled
        """
        console.print("\n[bold cyan]📚 Import Book Idea[/bold cyan]")
        console.print("Select a book idea to import and auto-populate your book creation form.\n")
        
        # Get available genres
        genres = self.get_available_book_genres()
        if not genres:
            console.print("[red]No book ideas available. Please check your data files.[/red]")
            return None
        
        # Select genre
        genre_choices = [genre.replace('_', ' ').title() for genre in genres]
        selected_genre_display = questionary.select(
            "Select a genre:",
            choices=genre_choices,
            style=custom_style
        ).ask()
        
        if not selected_genre_display:
            return None
        
        # Convert back to original format
        selected_genre = selected_genre_display.lower().replace(' ', '_')
        
        # Display ideas for selected genre
        console.print()
        self.display_book_ideas_table(selected_genre)
        
        # Get ideas for the genre
        ideas = self.get_book_ideas_by_genre(selected_genre)
        if not ideas:
            console.print("[red]No ideas found for this genre.[/red]")
            return None
        
        # Select specific idea
        idea_choices = []
        for i, idea in enumerate(ideas, 1):
            title = idea.get('title', 'Untitled')
            description = idea.get('description', 'No description')
            # Truncate for menu display
            if len(description) > 60:
                description = description[:57] + "..."
            idea_choices.append(f"{i}. {title} - {description}")
        
        idea_choices.append("← Back to Genre Selection")
        
        selected_idea_display = questionary.select(
            "Select a book idea:",
            choices=idea_choices,
            style=custom_style
        ).ask()
        
        if not selected_idea_display or selected_idea_display == "← Back to Genre Selection":
            return self.select_book_idea()  # Recursive call to go back
        
        # Extract the idea index
        idea_index = int(selected_idea_display.split('.')[0]) - 1
        selected_idea = ideas[idea_index].copy()
        
        # Add genre information
        selected_idea['genre'] = selected_genre
        
        return selected_idea
    
    def select_series_idea(self) -> Optional[Dict[str, Any]]:
        """
        Interactive selection of a series idea.
        
        Returns:
            Selected series idea dictionary or None if cancelled
        """
        console.print("\n[bold cyan]📚 Import Series Idea[/bold cyan]")
        console.print("Select a series idea to import and auto-populate your series creation form.\n")
        
        # Get available genres
        genres = self.get_available_series_genres()
        if not genres:
            console.print("[red]No series ideas available. Please check your data files.[/red]")
            return None
        
        # Select genre
        genre_choices = [genre.replace('_', ' ').title() for genre in genres]
        selected_genre_display = questionary.select(
            "Select a genre:",
            choices=genre_choices,
            style=custom_style
        ).ask()
        
        if not selected_genre_display:
            return None
        
        # Convert back to original format
        selected_genre = selected_genre_display.lower().replace(' ', '_')
        
        # Display ideas for selected genre
        console.print()
        self.display_series_ideas_table(selected_genre)
        
        # Get ideas for the genre
        ideas = self.get_series_ideas_by_genre(selected_genre)
        if not ideas:
            console.print("[red]No ideas found for this genre.[/red]")
            return None
        
        # Select specific idea
        idea_choices = []
        for i, idea in enumerate(ideas, 1):
            title = idea.get('title', 'Untitled Series')
            book_count = idea.get('book_count', len(idea.get('books', [])))
            description = idea.get('description', 'No description')
            # Truncate for menu display
            if len(description) > 40:
                description = description[:37] + "..."
            idea_choices.append(f"{i}. {title} ({book_count} books) - {description}")
        
        idea_choices.append("← Back to Genre Selection")
        
        selected_idea_display = questionary.select(
            "Select a series idea:",
            choices=idea_choices,
            style=custom_style
        ).ask()
        
        if not selected_idea_display or selected_idea_display == "← Back to Genre Selection":
            return self.select_series_idea()  # Recursive call to go back
        
        # Extract the idea index
        idea_index = int(selected_idea_display.split('.')[0]) - 1
        selected_idea = ideas[idea_index].copy()
        
        # Add genre information
        selected_idea['genre'] = selected_genre
        
        return selected_idea
    
    def display_selected_book_idea(self, idea: Dict[str, Any]) -> None:
        """Display the selected book idea in a formatted panel."""
        title = idea.get('title', 'Untitled')
        description = idea.get('description', 'No description available')
        genre = idea.get('genre', 'Unknown').replace('_', ' ').title()
        
        content = f"[bold green]Title:[/bold green] {title}\n"
        content += f"[bold cyan]Genre:[/bold cyan] {genre}\n"
        content += f"[bold yellow]Description:[/bold yellow]\n{description}"
        
        console.print(Panel(content, title="📖 Selected Book Idea", border_style="green"))
    
    def display_selected_series_idea(self, idea: Dict[str, Any]) -> None:
        """Display the selected series idea in a formatted panel."""
        title = idea.get('title', 'Untitled Series')
        description = idea.get('description', 'No description available')
        genre = idea.get('genre', 'Unknown').replace('_', ' ').title()
        book_count = idea.get('book_count', len(idea.get('books', [])))
        books = idea.get('books', [])
        
        content = f"[bold green]Series Title:[/bold green] {title}\n"
        content += f"[bold cyan]Genre:[/bold cyan] {genre}\n"
        content += f"[bold magenta]Number of Books:[/bold magenta] {book_count}\n"
        content += f"[bold yellow]Description:[/bold yellow]\n{description}\n\n"
        
        if books:
            content += "[bold blue]Books in Series:[/bold blue]\n"
            for i, book in enumerate(books, 1):
                book_title = book.get('title', f'Book {i}')
                content += f"  {i}. {book_title}\n"
        
        console.print(Panel(content, title="📚 Selected Series Idea", border_style="green"))
