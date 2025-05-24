"""
Series continuity tracking and management system.
Handles cross-book element tracking, character development, plot threads, and world consistency.
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class CharacterState:
    """Tracks character state across books."""
    name: str
    last_appearance_book: int
    current_status: str  # alive, dead, missing, etc.
    location: str
    relationships: Dict[str, str]  # character_name -> relationship_type
    abilities: List[str]
    knowledge: List[str]  # what they know
    character_arc_stage: str  # beginning, development, climax, resolution
    personality_changes: List[str]
    physical_changes: List[str]


@dataclass
class PlotThread:
    """Tracks plot threads across books."""
    thread_id: str
    name: str
    description: str
    status: str  # active, resolved, dormant, abandoned
    introduced_book: int
    last_mentioned_book: int
    resolution_book: Optional[int]
    key_events: List[Dict[str, Any]]  # book_number, event_description
    connected_characters: List[str]
    importance_level: str  # major, minor, subplot


@dataclass
class WorldElement:
    """Tracks world-building elements across books."""
    element_id: str
    name: str
    type: str  # location, organization, magic_system, technology, culture, etc.
    description: str
    first_introduced_book: int
    last_mentioned_book: int
    current_state: str
    rules_and_properties: Dict[str, Any]
    changes_over_time: List[Dict[str, Any]]  # book_number, change_description
    connected_characters: List[str]
    connected_plot_threads: List[str]


@dataclass
class SeriesTimeline:
    """Tracks timeline and chronology across books."""
    events: List[Dict[str, Any]]  # timestamp, book_number, event, characters_involved
    time_gaps: List[Dict[str, Any]]  # between_books, duration, description
    character_ages: Dict[str, Dict[int, int]]  # character_name -> {book_number: age}
    seasonal_progression: List[Dict[str, Any]]  # book_number, season, year


class SeriesContinuityManager:
    """
    Manages continuity tracking across a book series.
    Tracks characters, plot threads, world elements, and timeline consistency.
    """

    def __init__(self, series_title: str, series_dir: str):
        """
        Initialize the continuity manager.

        Args:
            series_title: Title of the series
            series_dir: Directory where series files are stored
        """
        self.series_title = series_title
        self.series_dir = Path(series_dir)
        self.continuity_file = self.series_dir / "series_continuity.json"

        # Initialize tracking structures
        self.characters: Dict[str, CharacterState] = {}
        self.plot_threads: Dict[str, PlotThread] = {}
        self.world_elements: Dict[str, WorldElement] = {}
        self.timeline = SeriesTimeline(events=[], time_gaps=[], character_ages={}, seasonal_progression=[])

        # Metadata
        self.current_book_number = 0
        self.total_books_planned = 0
        self.last_updated = datetime.now().isoformat()

        # Load existing continuity data if available
        self.load_continuity()

    def load_continuity(self) -> bool:
        """
        Load existing continuity data from file with robust error handling and validation.

        Returns:
            True if data was loaded successfully, False otherwise
        """
        if not self.continuity_file.exists():
            return False

        try:
            # Create backup before loading
            self._create_backup_if_needed()

            with open(self.continuity_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Validate data structure
            if not self._validate_continuity_data(data):
                print("Warning: Continuity data validation failed, attempting recovery...")
                return self._attempt_data_recovery()

            # Load characters with validation
            if 'characters' in data and isinstance(data['characters'], list):
                for char_data in data['characters']:
                    try:
                        if self._validate_character_data(char_data):
                            char = self._safe_create_character(char_data)
                            if char and char.name:
                                self.characters[char.name] = char
                    except Exception as e:
                        print(f"Warning: Failed to load character {char_data.get('name', 'unknown')}: {e}")
                        continue

            # Load plot threads with validation
            if 'plot_threads' in data and isinstance(data['plot_threads'], list):
                for thread_data in data['plot_threads']:
                    try:
                        if self._validate_plot_thread_data(thread_data):
                            thread = self._safe_create_plot_thread(thread_data)
                            if thread and thread.thread_id:
                                self.plot_threads[thread.thread_id] = thread
                    except Exception as e:
                        print(f"Warning: Failed to load plot thread {thread_data.get('thread_id', 'unknown')}: {e}")
                        continue

            # Load world elements with validation
            if 'world_elements' in data and isinstance(data['world_elements'], list):
                for element_data in data['world_elements']:
                    try:
                        if self._validate_world_element_data(element_data):
                            element = self._safe_create_world_element(element_data)
                            if element and element.element_id:
                                self.world_elements[element.element_id] = element
                    except Exception as e:
                        print(f"Warning: Failed to load world element {element_data.get('element_id', 'unknown')}: {e}")
                        continue

            # Load timeline with validation
            if 'timeline' in data and isinstance(data['timeline'], dict):
                try:
                    self.timeline = self._safe_create_timeline(data['timeline'])
                except Exception as e:
                    print(f"Warning: Failed to load timeline data: {e}")
                    self.timeline = SeriesTimeline(events=[], time_gaps=[], character_ages={}, seasonal_progression=[])

            # Load metadata with defaults
            self.current_book_number = max(0, data.get('current_book_number', 0))
            self.total_books_planned = max(0, data.get('total_books_planned', 0))
            self.last_updated = data.get('last_updated', datetime.now().isoformat())

            print(f"Successfully loaded continuity data: {len(self.characters)} characters, {len(self.plot_threads)} plot threads, {len(self.world_elements)} world elements")
            return True

        except (json.JSONDecodeError, KeyError, TypeError, FileNotFoundError) as e:
            print(f"Error loading continuity data: {e}")
            return self._attempt_data_recovery()
        except Exception as e:
            print(f"Unexpected error loading continuity data: {e}")
            return False

    def save_continuity(self) -> bool:
        """
        Save continuity data to file with atomic write and backup.

        Returns:
            True if saved successfully, False otherwise
        """
        try:
            # Ensure directory exists
            self.series_dir.mkdir(parents=True, exist_ok=True)

            # Prepare data for serialization with validation
            data = self._prepare_save_data()

            # Validate data before saving
            if not self._validate_continuity_data(data):
                print("Error: Continuity data validation failed before save")
                return False

            # Use atomic write (write to temp file, then rename)
            temp_file = self.continuity_file.with_suffix('.tmp')

            try:
                # Write to temporary file
                with open(temp_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                # Verify the written file can be read back
                with open(temp_file, 'r', encoding='utf-8') as f:
                    verification_data = json.load(f)

                if not self._validate_continuity_data(verification_data):
                    raise ValueError("Written data failed validation")

                # Atomic rename (this is the critical moment)
                if self.continuity_file.exists():
                    # Create backup before overwriting
                    backup_file = self.continuity_file.with_suffix('.backup')
                    import shutil
                    shutil.copy2(self.continuity_file, backup_file)

                # Atomic rename
                temp_file.replace(self.continuity_file)

                # Update timestamp
                self.last_updated = datetime.now().isoformat()

                print(f"Successfully saved continuity data: {len(self.characters)} characters, {len(self.plot_threads)} plot threads")
                return True

            except Exception as e:
                # Clean up temp file if it exists
                if temp_file.exists():
                    temp_file.unlink()
                raise e

        except Exception as e:
            print(f"Error saving continuity data: {e}")
            return False

    def start_new_book(self, book_number: int) -> None:
        """
        Initialize tracking for a new book in the series.

        Args:
            book_number: The number of the book being started
        """
        self.current_book_number = book_number

        # Update last appearance for all active characters
        for char in self.characters.values():
            if char.current_status in ['alive', 'active']:
                char.last_appearance_book = max(char.last_appearance_book, book_number - 1)

        # Update plot thread mentions
        for thread in self.plot_threads.values():
            if thread.status == 'active':
                thread.last_mentioned_book = max(thread.last_mentioned_book, book_number - 1)

        # Update world element mentions
        for element in self.world_elements.values():
            element.last_mentioned_book = max(element.last_mentioned_book, book_number - 1)

    def add_character(self, name: str, status: str = "alive", location: str = "unknown",
                     book_introduced: Optional[int] = None) -> Optional[CharacterState]:
        """
        Add or update a character in the continuity tracking with validation.

        Args:
            name: Character name
            status: Current status (alive, dead, missing, etc.)
            location: Current location
            book_introduced: Book number where character was introduced

        Returns:
            CharacterState object or None if validation fails
        """
        # Input validation
        if not name or not isinstance(name, str) or not name.strip():
            print(f"Error: Invalid character name: {name}")
            return None

        name = name.strip()

        if not status or not isinstance(status, str):
            print(f"Error: Invalid character status: {status}")
            return None

        if not location or not isinstance(location, str):
            print(f"Error: Invalid character location: {location}")
            return None

        book_num = book_introduced or self.current_book_number
        if not isinstance(book_num, int) or book_num < 0:
            print(f"Error: Invalid book number: {book_num}")
            return None

        try:
            if name in self.characters:
                # Update existing character
                char = self.characters[name]
                char.current_status = status
                char.location = location
                char.last_appearance_book = self.current_book_number
            else:
                # Create new character
                char = CharacterState(
                    name=name,
                    last_appearance_book=book_num,
                    current_status=status,
                    location=location,
                    relationships={},
                    abilities=[],
                    knowledge=[],
                    character_arc_stage="beginning",
                    personality_changes=[],
                    physical_changes=[]
                )
                self.characters[name] = char

            return char

        except Exception as e:
            print(f"Error creating/updating character {name}: {e}")
            return None

    def add_plot_thread(self, thread_id: str, name: str, description: str,
                       importance: str = "minor", book_introduced: Optional[int] = None) -> Optional[PlotThread]:
        """
        Add a new plot thread to track across the series with validation.

        Args:
            thread_id: Unique identifier for the plot thread
            name: Name/title of the plot thread
            description: Description of the plot thread
            importance: Importance level (major, minor, subplot)
            book_introduced: Book where thread was introduced

        Returns:
            PlotThread object or None if validation fails
        """
        # Input validation
        if not thread_id or not isinstance(thread_id, str) or not thread_id.strip():
            print(f"Error: Invalid plot thread ID: {thread_id}")
            return None

        thread_id = thread_id.strip()

        if not name or not isinstance(name, str) or not name.strip():
            print(f"Error: Invalid plot thread name: {name}")
            return None

        if not description or not isinstance(description, str):
            print(f"Error: Invalid plot thread description: {description}")
            return None

        valid_importance_levels = ['major', 'minor', 'subplot']
        if importance not in valid_importance_levels:
            print(f"Error: Invalid importance level: {importance}. Must be one of {valid_importance_levels}")
            return None

        book_num = book_introduced or self.current_book_number
        if not isinstance(book_num, int) or book_num < 0:
            print(f"Error: Invalid book number: {book_num}")
            return None

        try:
            thread = PlotThread(
                thread_id=thread_id,
                name=name.strip(),
                description=description,
                status="active",
                introduced_book=book_num,
                last_mentioned_book=book_num,
                resolution_book=None,
                key_events=[],
                connected_characters=[],
                importance_level=importance
            )

            self.plot_threads[thread_id] = thread
            return thread

        except Exception as e:
            print(f"Error creating plot thread {thread_id}: {e}")
            return None

    def add_world_element(self, element_id: str, name: str, element_type: str,
                         description: str, book_introduced: Optional[int] = None) -> Optional[WorldElement]:
        """
        Add a world-building element to track across the series with validation.

        Args:
            element_id: Unique identifier for the element
            name: Name of the element
            element_type: Type (location, organization, magic_system, etc.)
            description: Description of the element
            book_introduced: Book where element was introduced

        Returns:
            WorldElement object or None if validation fails
        """
        # Input validation
        if not element_id or not isinstance(element_id, str) or not element_id.strip():
            print(f"Error: Invalid world element ID: {element_id}")
            return None

        element_id = element_id.strip()

        if not name or not isinstance(name, str) or not name.strip():
            print(f"Error: Invalid world element name: {name}")
            return None

        if not element_type or not isinstance(element_type, str) or not element_type.strip():
            print(f"Error: Invalid world element type: {element_type}")
            return None

        if not description or not isinstance(description, str):
            print(f"Error: Invalid world element description: {description}")
            return None

        book_num = book_introduced or self.current_book_number
        if not isinstance(book_num, int) or book_num < 0:
            print(f"Error: Invalid book number: {book_num}")
            return None

        try:
            element = WorldElement(
                element_id=element_id,
                name=name.strip(),
                type=element_type.strip(),
                description=description,
                first_introduced_book=book_num,
                last_mentioned_book=book_num,
                current_state="active",
                rules_and_properties={},
                changes_over_time=[],
                connected_characters=[],
                connected_plot_threads=[]
            )

            self.world_elements[element_id] = element
            return element

        except Exception as e:
            print(f"Error creating world element {element_id}: {e}")
            return None

    def get_continuity_summary(self, for_book_number: Optional[int] = None) -> Dict[str, Any]:
        """
        Get a summary of continuity elements relevant for a specific book with optimized performance.

        Args:
            for_book_number: Book number to get continuity for (current book if None)

        Returns:
            Dictionary with continuity information
        """
        book_num = for_book_number or self.current_book_number

        # Use list comprehensions for better performance
        active_characters = {}
        active_threads = {}
        established_elements = {}

        # Optimized character filtering
        for name, char in self.characters.items():
            if char.current_status in ['alive', 'active'] and char.last_appearance_book < book_num:
                try:
                    active_characters[name] = asdict(char)
                except Exception as e:
                    print(f"Warning: Failed to serialize character {name}: {e}")
                    continue

        # Optimized plot thread filtering
        for thread_id, thread in self.plot_threads.items():
            if thread.status == 'active' and thread.introduced_book < book_num:
                try:
                    active_threads[thread_id] = asdict(thread)
                except Exception as e:
                    print(f"Warning: Failed to serialize plot thread {thread_id}: {e}")
                    continue

        # Optimized world element filtering
        for element_id, element in self.world_elements.items():
            if element.first_introduced_book < book_num:
                try:
                    established_elements[element_id] = asdict(element)
                except Exception as e:
                    print(f"Warning: Failed to serialize world element {element_id}: {e}")
                    continue

        # Optimized timeline event filtering
        relevant_events = []
        for event in self.timeline.events:
            try:
                if event.get('book_number', 0) < book_num:
                    relevant_events.append(event)
            except Exception as e:
                print(f"Warning: Failed to process timeline event: {e}")
                continue

        return {
            'book_number': book_num,
            'active_characters': active_characters,
            'active_plot_threads': active_threads,
            'established_world_elements': established_elements,
            'timeline_events': relevant_events,
            'summary_stats': {
                'character_count': len(active_characters),
                'plot_thread_count': len(active_threads),
                'world_element_count': len(established_elements),
                'timeline_event_count': len(relevant_events)
            }
        }

    def get_character_development_notes(self, character_name: str) -> Dict[str, Any]:
        """
        Get development notes for a specific character.

        Args:
            character_name: Name of the character

        Returns:
            Dictionary with character development information
        """
        if character_name not in self.characters:
            return {}

        char = self.characters[character_name]
        return {
            'name': char.name,
            'arc_stage': char.character_arc_stage,
            'recent_changes': char.personality_changes[-3:] if char.personality_changes else [],
            'current_relationships': char.relationships,
            'knowledge_gained': char.knowledge,
            'abilities': char.abilities,
            'suggested_development': self._suggest_character_development(char)
        }

    def _suggest_character_development(self, character: CharacterState) -> List[str]:
        """
        Suggest character development opportunities based on current state.

        Args:
            character: CharacterState object

        Returns:
            List of development suggestions
        """
        suggestions = []

        # Arc stage suggestions
        if character.character_arc_stage == "beginning":
            suggestions.append("Consider introducing a major challenge or conflict")
            suggestions.append("Establish character's core motivation and goals")
        elif character.character_arc_stage == "development":
            suggestions.append("Show character growth through difficult choices")
            suggestions.append("Develop relationships with other characters")
        elif character.character_arc_stage == "climax":
            suggestions.append("Test character's growth with ultimate challenge")
            suggestions.append("Show how character has changed from the beginning")

        # Relationship suggestions
        if len(character.relationships) < 2:
            suggestions.append("Develop more character relationships")

        # Knowledge and abilities
        if not character.knowledge:
            suggestions.append("Have character learn something significant")

        return suggestions

    # Validation and Safety Methods

    def _validate_continuity_data(self, data: Dict[str, Any]) -> bool:
        """
        Validate the structure of continuity data.

        Args:
            data: Data dictionary to validate

        Returns:
            True if data structure is valid, False otherwise
        """
        try:
            # Check required top-level keys
            required_keys = ['series_title', 'current_book_number', 'total_books_planned']
            for key in required_keys:
                if key not in data:
                    print(f"Missing required key: {key}")
                    return False

            # Validate data types
            if not isinstance(data.get('characters', []), list):
                print("Characters data is not a list")
                return False

            if not isinstance(data.get('plot_threads', []), list):
                print("Plot threads data is not a list")
                return False

            if not isinstance(data.get('world_elements', []), list):
                print("World elements data is not a list")
                return False

            if 'timeline' in data and not isinstance(data['timeline'], dict):
                print("Timeline data is not a dictionary")
                return False

            return True

        except Exception as e:
            print(f"Error validating continuity data: {e}")
            return False

    def _validate_character_data(self, char_data: Dict[str, Any]) -> bool:
        """
        Validate character data structure.

        Args:
            char_data: Character data to validate

        Returns:
            True if valid, False otherwise
        """
        try:
            # Check required fields
            required_fields = ['name', 'last_appearance_book', 'current_status', 'location']
            for field in required_fields:
                if field not in char_data:
                    return False

            # Validate data types
            if not isinstance(char_data['name'], str) or not char_data['name'].strip():
                return False

            if not isinstance(char_data['last_appearance_book'], int):
                return False

            if not isinstance(char_data.get('relationships', {}), dict):
                return False

            if not isinstance(char_data.get('abilities', []), list):
                return False

            return True

        except Exception:
            return False

    def _validate_plot_thread_data(self, thread_data: Dict[str, Any]) -> bool:
        """
        Validate plot thread data structure.

        Args:
            thread_data: Plot thread data to validate

        Returns:
            True if valid, False otherwise
        """
        try:
            # Check required fields
            required_fields = ['thread_id', 'name', 'description', 'status', 'introduced_book']
            for field in required_fields:
                if field not in thread_data:
                    return False

            # Validate data types and values
            if not isinstance(thread_data['thread_id'], str) or not thread_data['thread_id'].strip():
                return False

            if not isinstance(thread_data['introduced_book'], int):
                return False

            valid_statuses = ['active', 'resolved', 'dormant', 'abandoned']
            if thread_data['status'] not in valid_statuses:
                return False

            return True

        except Exception:
            return False

    def _validate_world_element_data(self, element_data: Dict[str, Any]) -> bool:
        """
        Validate world element data structure.

        Args:
            element_data: World element data to validate

        Returns:
            True if valid, False otherwise
        """
        try:
            # Check required fields
            required_fields = ['element_id', 'name', 'type', 'description', 'first_introduced_book']
            for field in required_fields:
                if field not in element_data:
                    return False

            # Validate data types
            if not isinstance(element_data['element_id'], str) or not element_data['element_id'].strip():
                return False

            if not isinstance(element_data['first_introduced_book'], int):
                return False

            return True

        except Exception:
            return False

    def _safe_create_character(self, char_data: Dict[str, Any]) -> Optional[CharacterState]:
        """
        Safely create a CharacterState object with fallback values.

        Args:
            char_data: Character data dictionary

        Returns:
            CharacterState object or None if creation fails
        """
        try:
            # Provide defaults for missing fields
            defaults = {
                'relationships': {},
                'abilities': [],
                'knowledge': [],
                'character_arc_stage': 'beginning',
                'personality_changes': [],
                'physical_changes': []
            }

            # Merge with defaults
            safe_data = {**defaults, **char_data}

            # Ensure required fields are valid
            if not safe_data['name'] or not isinstance(safe_data['name'], str):
                return None

            # Sanitize data types
            safe_data['relationships'] = dict(safe_data.get('relationships', {}))
            safe_data['abilities'] = list(safe_data.get('abilities', []))
            safe_data['knowledge'] = list(safe_data.get('knowledge', []))
            safe_data['personality_changes'] = list(safe_data.get('personality_changes', []))
            safe_data['physical_changes'] = list(safe_data.get('physical_changes', []))

            return CharacterState(**safe_data)

        except Exception as e:
            print(f"Failed to create character from data: {e}")
            return None

    def _safe_create_plot_thread(self, thread_data: Dict[str, Any]) -> Optional[PlotThread]:
        """
        Safely create a PlotThread object with fallback values.

        Args:
            thread_data: Plot thread data dictionary

        Returns:
            PlotThread object or None if creation fails
        """
        try:
            # Provide defaults for missing fields
            defaults = {
                'resolution_book': None,
                'key_events': [],
                'connected_characters': [],
                'importance_level': 'minor',
                'last_mentioned_book': thread_data.get('introduced_book', 0)
            }

            # Merge with defaults
            safe_data = {**defaults, **thread_data}

            # Ensure required fields are valid
            if not safe_data['thread_id'] or not isinstance(safe_data['thread_id'], str):
                return None

            # Sanitize data types
            safe_data['key_events'] = list(safe_data.get('key_events', []))
            safe_data['connected_characters'] = list(safe_data.get('connected_characters', []))

            return PlotThread(**safe_data)

        except Exception as e:
            print(f"Failed to create plot thread from data: {e}")
            return None

    def _safe_create_world_element(self, element_data: Dict[str, Any]) -> Optional[WorldElement]:
        """
        Safely create a WorldElement object with fallback values.

        Args:
            element_data: World element data dictionary

        Returns:
            WorldElement object or None if creation fails
        """
        try:
            # Provide defaults for missing fields
            defaults = {
                'current_state': 'active',
                'rules_and_properties': {},
                'changes_over_time': [],
                'connected_characters': [],
                'connected_plot_threads': [],
                'last_mentioned_book': element_data.get('first_introduced_book', 0)
            }

            # Merge with defaults
            safe_data = {**defaults, **element_data}

            # Ensure required fields are valid
            if not safe_data['element_id'] or not isinstance(safe_data['element_id'], str):
                return None

            # Sanitize data types
            safe_data['rules_and_properties'] = dict(safe_data.get('rules_and_properties', {}))
            safe_data['changes_over_time'] = list(safe_data.get('changes_over_time', []))
            safe_data['connected_characters'] = list(safe_data.get('connected_characters', []))
            safe_data['connected_plot_threads'] = list(safe_data.get('connected_plot_threads', []))

            return WorldElement(**safe_data)

        except Exception as e:
            print(f"Failed to create world element from data: {e}")
            return None

    def _safe_create_timeline(self, timeline_data: Dict[str, Any]) -> SeriesTimeline:
        """
        Safely create a SeriesTimeline object with fallback values.

        Args:
            timeline_data: Timeline data dictionary

        Returns:
            SeriesTimeline object
        """
        try:
            # Provide defaults for missing fields
            defaults = {
                'events': [],
                'time_gaps': [],
                'character_ages': {},
                'seasonal_progression': []
            }

            # Merge with defaults
            safe_data = {**defaults, **timeline_data}

            # Sanitize data types
            safe_data['events'] = list(safe_data.get('events', []))
            safe_data['time_gaps'] = list(safe_data.get('time_gaps', []))
            safe_data['character_ages'] = dict(safe_data.get('character_ages', {}))
            safe_data['seasonal_progression'] = list(safe_data.get('seasonal_progression', []))

            return SeriesTimeline(**safe_data)

        except Exception as e:
            print(f"Failed to create timeline from data: {e}")
            return SeriesTimeline(events=[], time_gaps=[], character_ages={}, seasonal_progression=[])

    def _create_backup_if_needed(self) -> None:
        """
        Create a backup of the continuity file if it exists and is recent.
        """
        try:
            if self.continuity_file.exists():
                # Create backup directory
                backup_dir = self.series_dir / "backups"
                backup_dir.mkdir(exist_ok=True)

                # Create timestamped backup
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = backup_dir / f"series_continuity_backup_{timestamp}.json"

                # Copy current file to backup
                import shutil
                shutil.copy2(self.continuity_file, backup_file)

                # Keep only last 5 backups
                self._cleanup_old_backups(backup_dir)

        except Exception as e:
            print(f"Warning: Failed to create backup: {e}")

    def _cleanup_old_backups(self, backup_dir: Path) -> None:
        """
        Keep only the 5 most recent backup files.

        Args:
            backup_dir: Directory containing backup files
        """
        try:
            backup_files = list(backup_dir.glob("series_continuity_backup_*.json"))
            if len(backup_files) > 5:
                # Sort by modification time and remove oldest
                backup_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
                for old_backup in backup_files[5:]:
                    old_backup.unlink()

        except Exception as e:
            print(f"Warning: Failed to cleanup old backups: {e}")

    def _attempt_data_recovery(self) -> bool:
        """
        Attempt to recover from backup files or create minimal valid state.

        Returns:
            True if recovery was successful, False otherwise
        """
        try:
            # Try to load from most recent backup
            backup_dir = self.series_dir / "backups"
            if backup_dir.exists():
                backup_files = list(backup_dir.glob("series_continuity_backup_*.json"))
                if backup_files:
                    # Sort by modification time, newest first
                    backup_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)

                    for backup_file in backup_files:
                        try:
                            with open(backup_file, 'r', encoding='utf-8') as f:
                                data = json.load(f)

                            if self._validate_continuity_data(data):
                                print(f"Successfully recovered from backup: {backup_file.name}")
                                # Copy backup to main file
                                import shutil
                                shutil.copy2(backup_file, self.continuity_file)
                                return self.load_continuity()

                        except Exception as e:
                            print(f"Failed to load backup {backup_file.name}: {e}")
                            continue

            # If no backup works, create minimal valid state
            print("Creating minimal continuity state...")
            self._create_minimal_state()
            return True

        except Exception as e:
            print(f"Data recovery failed: {e}")
            return False

    def _create_minimal_state(self) -> None:
        """
        Create a minimal valid continuity state.
        """
        self.characters = {}
        self.plot_threads = {}
        self.world_elements = {}
        self.timeline = SeriesTimeline(events=[], time_gaps=[], character_ages={}, seasonal_progression=[])
        self.current_book_number = 0
        self.total_books_planned = 0
        self.last_updated = datetime.now().isoformat()

        # Save the minimal state
        self.save_continuity()

    def _prepare_save_data(self) -> Dict[str, Any]:
        """
        Prepare continuity data for serialization with error handling.

        Returns:
            Dictionary ready for JSON serialization
        """
        try:
            data = {
                'series_title': str(self.series_title),
                'current_book_number': int(self.current_book_number),
                'total_books_planned': int(self.total_books_planned),
                'last_updated': datetime.now().isoformat(),
                'characters': [],
                'plot_threads': [],
                'world_elements': [],
                'timeline': {}
            }

            # Serialize characters with error handling
            for char_name, char in self.characters.items():
                try:
                    char_dict = asdict(char)
                    if char_dict and 'name' in char_dict:
                        data['characters'].append(char_dict)
                except Exception as e:
                    print(f"Warning: Failed to serialize character {char_name}: {e}")
                    continue

            # Serialize plot threads with error handling
            for thread_id, thread in self.plot_threads.items():
                try:
                    thread_dict = asdict(thread)
                    if thread_dict and 'thread_id' in thread_dict:
                        data['plot_threads'].append(thread_dict)
                except Exception as e:
                    print(f"Warning: Failed to serialize plot thread {thread_id}: {e}")
                    continue

            # Serialize world elements with error handling
            for element_id, element in self.world_elements.items():
                try:
                    element_dict = asdict(element)
                    if element_dict and 'element_id' in element_dict:
                        data['world_elements'].append(element_dict)
                except Exception as e:
                    print(f"Warning: Failed to serialize world element {element_id}: {e}")
                    continue

            # Serialize timeline with error handling
            try:
                data['timeline'] = asdict(self.timeline)
            except Exception as e:
                print(f"Warning: Failed to serialize timeline: {e}")
                data['timeline'] = {
                    'events': [],
                    'time_gaps': [],
                    'character_ages': {},
                    'seasonal_progression': []
                }

            return data

        except Exception as e:
            print(f"Error preparing save data: {e}")
            # Return minimal valid structure
            return {
                'series_title': str(self.series_title),
                'current_book_number': 0,
                'total_books_planned': 0,
                'last_updated': datetime.now().isoformat(),
                'characters': [],
                'plot_threads': [],
                'world_elements': [],
                'timeline': {'events': [], 'time_gaps': [], 'character_ages': {}, 'seasonal_progression': []}
            }