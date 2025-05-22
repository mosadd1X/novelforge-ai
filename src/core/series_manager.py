"""
Series manager for maintaining context and continuity across multiple books in a series.
"""
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime
from src.utils.file_handler import sanitize_filename


class SeriesManager:
    """
    Manages the memory and context for a series of novels to ensure continuity across books.
    """

    def __init__(self, series_title: str, output_dir: str = None):
        """
        Initialize the series manager.

        Args:
            series_title: The title of the series
            output_dir: Directory to save series files (default: None, will use output/series directory)
        """
        self.series_title = series_title

        # Set output directory
        if output_dir:
            self.output_dir = output_dir
        else:
            # Default to output/series directory
            self.output_dir = os.path.join("output", "series")
            os.makedirs(self.output_dir, exist_ok=True)

        # Set series file path
        series_filename = f"series_{sanitize_filename(series_title)}.json"
        self.series_file = os.path.join(self.output_dir, series_filename)

        # Core series information
        self.metadata = {
            "title": series_title,
            "creator": "",
            "description": "",
            "genre": "",
            "target_audience": "",
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "book_count": 0,
            "planned_books": 0,
        }

        # Books in the series
        self.books = []

        # Book templates for planned books
        self.book_templates = []

        # Series universe
        self.universe = {
            "world_building": {},
            "locations": [],
            "timeline": [],
            "history": [],
            "rules": [],
        }

        # Recurring characters across the series
        self.recurring_characters = []

        # Series-level plot arcs
        self.series_arcs = []

        # Enhanced series tracking system
        self.series_tracking = {
            # Character development tracking across books
            "character_arcs": {},           # Track character development across books
            "character_relationships": {},  # Track relationships between characters
            "character_development": {},    # Track detailed character development metrics
            "character_traits": {},         # Track character traits and how they evolve
            "character_goals": {},          # Track character goals and motivations
            "character_conflicts": {},      # Track character conflicts
            "character_growth": {},         # Track character growth and transformation

            # Plot tracking
            "plot_threads": {},             # Track ongoing plot threads
            "plot_arcs": {},                # Track major plot arcs across the series
            "plot_progression": {},         # Track progression of plot arcs
            "plot_milestones": {},          # Track major plot milestones
            "unresolved_questions": [],     # Track unresolved plot points
            "foreshadowing": [],            # Track foreshadowing elements
            "callbacks": [],                # Track callbacks to earlier events

            # Timeline tracking
            "timeline_events": [],          # Chronological events across the series
            "timeline_periods": {},         # Major time periods in the series
            "timeline_connections": {},     # Connections between timeline events

            # World building
            "world_building": {},           # Track world-building elements
            "locations": {},                # Track important locations
            "objects_of_significance": {},  # Track important objects

            # Thematic elements
            "themes_and_motifs": {},        # Track recurring themes and motifs
            "symbols": {},                  # Track symbolic elements

            # Continuity tracking
            "continuity_elements": {},      # Track elements that need continuity
        }

        # Load existing series if available
        self.load_series()

    # Using imported sanitize_filename function instead of this method

    def save_series(self) -> None:
        """Save the current series state to a file."""
        # Update the last_updated timestamp
        self.metadata["last_updated"] = datetime.now().isoformat()

        # Prepare the series data
        series_data = {
            "metadata": self.metadata,
            "books": self.books,
            "book_templates": self.book_templates,
            "universe": self.universe,
            "recurring_characters": self.recurring_characters,
            "series_arcs": self.series_arcs,
            "series_tracking": self.series_tracking,
        }

        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.series_file), exist_ok=True)

        # Save to file
        with open(self.series_file, 'w', encoding='utf-8') as f:
            json.dump(series_data, f, indent=2, ensure_ascii=False)

    def load_series(self) -> bool:
        """
        Load series from file if it exists.

        Returns:
            True if series was loaded, False otherwise
        """
        if not os.path.exists(self.series_file):
            return False

        try:
            with open(self.series_file, 'r', encoding='utf-8') as f:
                series_data = json.load(f)

            # Update attributes
            self.metadata = series_data.get("metadata", self.metadata)
            self.books = series_data.get("books", self.books)
            self.book_templates = series_data.get("book_templates", self.book_templates)
            self.universe = series_data.get("universe", self.universe)
            self.recurring_characters = series_data.get("recurring_characters", self.recurring_characters)
            self.series_arcs = series_data.get("series_arcs", self.series_arcs)
            self.series_tracking = series_data.get("series_tracking", self.series_tracking)

            # Scan for existing books that might not be in the metadata
            self.scan_for_existing_books()

            return True
        except Exception as e:
            print(f"Error loading series: {e}")
            return False

    def scan_for_existing_books(self) -> None:
        """
        Scan the series directory for existing books and update the metadata.
        This helps detect books that were generated but not properly registered.
        """
        # Get the series directory
        series_dir = os.path.join("output", "series", sanitize_filename(self.series_title))

        if not os.path.exists(series_dir):
            return

        # Look for book directories
        book_dirs = []
        for item in os.listdir(series_dir):
            item_path = os.path.join(series_dir, item)
            if os.path.isdir(item_path) and item.startswith("book_"):
                book_dirs.append(item_path)

        if not book_dirs:
            # If no book directories, look for EPUB files directly
            epub_files = [f for f in os.listdir(series_dir) if f.endswith(".epub")]
            if epub_files:
                for i, epub_file in enumerate(sorted(epub_files), 1):
                    # Check if this book is already in our list
                    book_exists = False
                    for book in self.books:
                        if book.get("book_number") == i:
                            book_exists = True
                            break

                    if book_exists:
                        continue

                    # Extract title from filename
                    title = epub_file.replace(".epub", "")

                    # Add book to our list
                    self.books.append({
                        "book_number": i,
                        "title": title,
                        "description": f"Book {i} in the {self.series_title} series"
                    })
            return

        # Process each book directory
        for book_dir in book_dirs:
            # Extract book number from directory name
            dir_name = os.path.basename(book_dir)
            try:
                # Format is typically "book_XX_title"
                book_num = int(dir_name.split("_")[1])
            except (IndexError, ValueError):
                continue

            # Check if this book is already in our list
            book_exists = False
            for book in self.books:
                if book.get("book_number") == book_num:
                    book_exists = True
                    break

            if book_exists:
                continue

            # Look for novel_data.json in the book directory
            json_path = os.path.join(book_dir, "novel_data.json")
            if os.path.exists(json_path):
                try:
                    with open(json_path, 'r', encoding='utf-8') as f:
                        novel_data = json.load(f)

                    # Extract book metadata
                    metadata = novel_data.get("metadata", {})
                    title = metadata.get("title", f"Book {book_num}")
                    description = metadata.get("description", "")

                    # Add book to our list
                    self.books.append({
                        "book_number": book_num,
                        "title": title,
                        "description": description
                    })
                except Exception:
                    # If we can't load the JSON, try to extract info from directory name
                    title = " ".join(dir_name.split("_")[2:]) if len(dir_name.split("_")) > 2 else f"Book {book_num}"
                    self.books.append({
                        "book_number": book_num,
                        "title": title,
                        "description": f"Book {book_num} in the {self.series_title} series"
                    })
            else:
                # If no JSON, check for EPUB file
                epub_files = [f for f in os.listdir(book_dir) if f.endswith(".epub")]
                if epub_files:
                    title = epub_files[0].replace(".epub", "")
                    self.books.append({
                        "book_number": book_num,
                        "title": title,
                        "description": f"Book {book_num} in the {self.series_title} series"
                    })
                else:
                    # Last resort: use directory name
                    title = " ".join(dir_name.split("_")[2:]) if len(dir_name.split("_")) > 2 else f"Book {book_num}"
                    self.books.append({
                        "book_number": book_num,
                        "title": title,
                        "description": f"Book {book_num} in the {self.series_title} series"
                    })

        # Update book count in metadata
        if self.books:
            self.metadata["book_count"] = len(self.books)

            # Save the updated metadata
            self.save_series()

    def update_metadata(self, **kwargs) -> None:
        """
        Update series metadata.

        Args:
            **kwargs: Key-value pairs to update in metadata
        """
        for key, value in kwargs.items():
            if key in self.metadata:
                self.metadata[key] = value
        self.save_series()

    def add_book(self, book_data: Dict[str, Any]) -> int:
        """
        Add a book to the series.

        Args:
            book_data: Dictionary containing book details

        Returns:
            Book number in the series
        """
        # Increment book count
        self.metadata["book_count"] += 1

        # Add book number to the book data
        book_data["book_number"] = self.metadata["book_count"]

        # Add book to the series
        self.books.append(book_data)

        # Save series
        self.save_series()

        return book_data["book_number"]

    def get_book(self, book_number: int) -> Optional[Dict[str, Any]]:
        """
        Get a book from the series by its number.

        Args:
            book_number: The book number in the series

        Returns:
            Book data or None if not found
        """
        for book in self.books:
            if book.get("book_number") == book_number:
                return book
        return None

    def add_recurring_character(self, character: Dict[str, Any]) -> None:
        """
        Add a recurring character to the series.

        Args:
            character: Dictionary containing character details
        """
        # Check if character already exists
        for existing_char in self.recurring_characters:
            if existing_char.get("name") == character.get("name"):
                # Update existing character
                existing_char.update(character)
                self.save_series()
                return

        # Add new character
        self.recurring_characters.append(character)
        self.save_series()

    def add_series_arc(self, arc: Dict[str, Any]) -> None:
        """
        Add a series-level plot arc.

        Args:
            arc: Dictionary containing arc details
        """
        self.series_arcs.append(arc)
        self.save_series()

    def update_series_tracking(self, book_number: int, tracking_data: Dict[str, Any]) -> None:
        """
        Update the series tracking with information from a generated book.

        Args:
            book_number: The book number in the series
            tracking_data: Dictionary containing tracking data
        """
        # Update character arcs
        if "character_arcs" in tracking_data:
            for char_name, arc in tracking_data["character_arcs"].items():
                if char_name not in self.series_tracking["character_arcs"]:
                    self.series_tracking["character_arcs"][char_name] = {}
                self.series_tracking["character_arcs"][char_name][book_number] = arc

        # Update character relationships
        if "character_relationships" in tracking_data:
            for rel_key, status in tracking_data["character_relationships"].items():
                if rel_key not in self.series_tracking["character_relationships"]:
                    self.series_tracking["character_relationships"][rel_key] = {}
                self.series_tracking["character_relationships"][rel_key][book_number] = status

        # Update character development
        if "character_development" in tracking_data:
            for char_name, development in tracking_data["character_development"].items():
                if char_name not in self.series_tracking["character_development"]:
                    self.series_tracking["character_development"][char_name] = {}
                self.series_tracking["character_development"][char_name][book_number] = development

        # Update character traits
        if "character_traits" in tracking_data:
            for char_name, traits in tracking_data["character_traits"].items():
                if char_name not in self.series_tracking["character_traits"]:
                    self.series_tracking["character_traits"][char_name] = {}
                self.series_tracking["character_traits"][char_name][book_number] = traits

        # Update character goals
        if "character_goals" in tracking_data:
            for char_name, goals in tracking_data["character_goals"].items():
                if char_name not in self.series_tracking["character_goals"]:
                    self.series_tracking["character_goals"][char_name] = {}
                self.series_tracking["character_goals"][char_name][book_number] = goals

        # Update character conflicts
        if "character_conflicts" in tracking_data:
            for char_name, conflicts in tracking_data["character_conflicts"].items():
                if char_name not in self.series_tracking["character_conflicts"]:
                    self.series_tracking["character_conflicts"][char_name] = {}
                self.series_tracking["character_conflicts"][char_name][book_number] = conflicts

        # Update character growth
        if "character_growth" in tracking_data:
            for char_name, growth in tracking_data["character_growth"].items():
                if char_name not in self.series_tracking["character_growth"]:
                    self.series_tracking["character_growth"][char_name] = {}
                self.series_tracking["character_growth"][char_name][book_number] = growth

        # Update plot threads
        if "plot_threads" in tracking_data:
            for thread_name, status in tracking_data["plot_threads"].items():
                if thread_name not in self.series_tracking["plot_threads"]:
                    self.series_tracking["plot_threads"][thread_name] = {}
                self.series_tracking["plot_threads"][thread_name][book_number] = status

        # Update plot arcs
        if "plot_arcs" in tracking_data:
            for arc_name, arc_data in tracking_data["plot_arcs"].items():
                if arc_name not in self.series_tracking["plot_arcs"]:
                    self.series_tracking["plot_arcs"][arc_name] = {}
                self.series_tracking["plot_arcs"][arc_name][book_number] = arc_data

        # Update plot progression
        if "plot_progression" in tracking_data:
            for arc_name, progression in tracking_data["plot_progression"].items():
                if arc_name not in self.series_tracking["plot_progression"]:
                    self.series_tracking["plot_progression"][arc_name] = {}
                self.series_tracking["plot_progression"][arc_name][book_number] = progression

        # Update plot milestones
        if "plot_milestones" in tracking_data:
            for milestone in tracking_data["plot_milestones"]:
                if milestone.get("book_number") is None:
                    milestone["book_number"] = book_number
                self.series_tracking["plot_milestones"][milestone.get("id", str(len(self.series_tracking["plot_milestones"])))] = milestone

        # Update unresolved questions
        if "unresolved_questions" in tracking_data:
            for question in tracking_data["unresolved_questions"]:
                if question not in self.series_tracking["unresolved_questions"]:
                    self.series_tracking["unresolved_questions"].append(question)

        # Update timeline events
        if "timeline_events" in tracking_data:
            for event in tracking_data["timeline_events"]:
                if "book_number" not in event:
                    event["book_number"] = book_number
                self.series_tracking["timeline_events"].append(event)

        # Update timeline periods
        if "timeline_periods" in tracking_data:
            for period_name, period_data in tracking_data["timeline_periods"].items():
                self.series_tracking["timeline_periods"][period_name] = period_data

        # Update timeline connections
        if "timeline_connections" in tracking_data:
            for connection in tracking_data["timeline_connections"]:
                connection_id = f"{connection.get('from_event')}_{connection.get('to_event')}"
                self.series_tracking["timeline_connections"][connection_id] = connection

        # Save the updated series tracking
        self.save_series()

    def get_context_for_book(self, book_number: int) -> Dict[str, Any]:
        """
        Get the context needed for generating a specific book in the series.

        Args:
            book_number: The book number to generate

        Returns:
            Dictionary containing context information
        """
        # Get previous books
        previous_books = [
            book for book in self.books
            if book.get("book_number", 0) < book_number
        ]

        # Get recurring characters
        relevant_characters = self.recurring_characters

        # Get series arcs
        relevant_arcs = self.series_arcs

        # Get series tracking information
        series_context = self._get_series_context_for_book(book_number)

        return {
            "metadata": self.metadata,
            "previous_books": previous_books,
            "recurring_characters": relevant_characters,
            "series_arcs": relevant_arcs,
            "book_to_generate": book_number,
            "series_context": series_context,
            "universe": self.universe,
        }

    def _get_series_context_for_book(self, book_number: int) -> Dict[str, Any]:
        """
        Get series tracking information relevant to a specific book.

        Args:
            book_number: The book number

        Returns:
            Dictionary containing series context
        """
        # Get character arcs for recurring characters
        character_arcs = {}
        for char_name, arcs in self.series_tracking["character_arcs"].items():
            # Get the most recent character arc update
            char_arc_books = sorted([b for b in arcs.keys() if int(b) < book_number], reverse=True)
            if char_arc_books:
                character_arcs[char_name] = arcs[char_arc_books[0]]

        # Get character relationships
        relationships = {}
        for rel_key, statuses in self.series_tracking["character_relationships"].items():
            # Get the most recent relationship update
            rel_books = sorted([b for b in statuses.keys() if int(b) < book_number], reverse=True)
            if rel_books:
                relationships[rel_key] = statuses[rel_books[0]]

        # Get character development
        character_development = {}
        for char_name, developments in self.series_tracking["character_development"].items():
            # Get the most recent development update
            dev_books = sorted([b for b in developments.keys() if int(b) < book_number], reverse=True)
            if dev_books:
                character_development[char_name] = developments[dev_books[0]]

        # Get character traits
        character_traits = {}
        for char_name, traits in self.series_tracking["character_traits"].items():
            # Get the most recent traits update
            trait_books = sorted([b for b in traits.keys() if int(b) < book_number], reverse=True)
            if trait_books:
                character_traits[char_name] = traits[trait_books[0]]

        # Get character goals
        character_goals = {}
        for char_name, goals in self.series_tracking["character_goals"].items():
            # Get the most recent goals update
            goal_books = sorted([b for b in goals.keys() if int(b) < book_number], reverse=True)
            if goal_books:
                character_goals[char_name] = goals[goal_books[0]]

        # Get character conflicts
        character_conflicts = {}
        for char_name, conflicts in self.series_tracking["character_conflicts"].items():
            # Get the most recent conflicts update
            conflict_books = sorted([b for b in conflicts.keys() if int(b) < book_number], reverse=True)
            if conflict_books:
                character_conflicts[char_name] = conflicts[conflict_books[0]]

        # Get character growth
        character_growth = {}
        for char_name, growth in self.series_tracking["character_growth"].items():
            # Get the most recent growth update
            growth_books = sorted([b for b in growth.keys() if int(b) < book_number], reverse=True)
            if growth_books:
                character_growth[char_name] = growth[growth_books[0]]

        # Get plot threads
        plot_threads = {}
        for thread_name, statuses in self.series_tracking["plot_threads"].items():
            # Get the most recent plot thread update
            thread_books = sorted([b for b in statuses.keys() if int(b) < book_number], reverse=True)
            if thread_books:
                plot_threads[thread_name] = statuses[thread_books[0]]

        # Get plot arcs
        plot_arcs = {}
        for arc_name, arc_data in self.series_tracking["plot_arcs"].items():
            # Get the most recent plot arc update
            arc_books = sorted([b for b in arc_data.keys() if int(b) < book_number], reverse=True)
            if arc_books:
                plot_arcs[arc_name] = arc_data[arc_books[0]]

        # Get plot progression
        plot_progression = {}
        for arc_name, progression in self.series_tracking["plot_progression"].items():
            # Get the most recent progression update
            prog_books = sorted([b for b in progression.keys() if int(b) < book_number], reverse=True)
            if prog_books:
                plot_progression[arc_name] = progression[prog_books[0]]

        # Get plot milestones
        plot_milestones = [
            milestone for milestone_id, milestone in self.series_tracking["plot_milestones"].items()
            if milestone.get("book_number", 0) < book_number
        ]

        # Get unresolved questions
        unresolved_questions = self.series_tracking["unresolved_questions"]

        # Get timeline events
        timeline_events = [
            event for event in self.series_tracking["timeline_events"]
            if event.get("book_number", 0) < book_number
        ]

        # Get timeline periods
        timeline_periods = self.series_tracking["timeline_periods"]

        # Get timeline connections
        timeline_connections = list(self.series_tracking["timeline_connections"].values())

        return {
            # Character tracking
            "character_arcs": character_arcs,
            "relationships": relationships,
            "character_development": character_development,
            "character_traits": character_traits,
            "character_goals": character_goals,
            "character_conflicts": character_conflicts,
            "character_growth": character_growth,

            # Plot tracking
            "plot_threads": plot_threads,
            "plot_arcs": plot_arcs,
            "plot_progression": plot_progression,
            "plot_milestones": plot_milestones,
            "unresolved_questions": unresolved_questions,

            # Timeline tracking
            "timeline_events": timeline_events,
            "timeline_periods": timeline_periods,
            "timeline_connections": timeline_connections,
        }
