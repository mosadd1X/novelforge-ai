"""
Memory manager for maintaining context and coherence across novel generation.
"""
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime

# Import SeriesManager conditionally to avoid circular imports
try:
    from src.core.series_manager import SeriesManager
except ImportError:
    SeriesManager = None


class MemoryManager:
    """
    Manages the memory and context for novel generation to ensure coherence.
    """

    def __init__(self, novel_title: str, output_dir: str = None, series_manager=None, book_number: int = None):
        """
        Initialize the memory manager.

        Args:
            novel_title: The title of the novel being generated
            output_dir: Directory to save memory files (default: None, will use root directory)
            series_manager: Optional SeriesManager instance if this book is part of a series
            book_number: Book number in the series (if part of a series)
        """
        self.novel_title = novel_title
        self.output_dir = output_dir
        self.series_manager = series_manager
        self.book_number = book_number

        # Set memory file path
        memory_filename = f"memory_{self._sanitize_filename(novel_title)}.json"
        if output_dir:
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)
            # Use forward slashes for consistency across platforms
            normalized_output_dir = output_dir.replace('\\', '/')
            self.memory_file = os.path.join(normalized_output_dir, memory_filename).replace('\\', '/')
        else:
            self.memory_file = memory_filename

        # Core novel information
        self.metadata = {
            "title": novel_title,
            "author": "",
            "description": "",
            "genre": "",
            "target_audience": "",
            "created_at": datetime.now().isoformat(),
            "last_updated": datetime.now().isoformat(),
            "series": {
                "is_part_of_series": bool(series_manager),
                "series_title": series_manager.series_title if series_manager else "",
                "book_number": book_number if book_number else 0,
            }
        }

        # Novel structure
        self.structure = {
            "total_chapters": 0,
            "target_word_count": 0,
            "current_word_count": 0,
            "outline": [],
        }

        # Characters
        self.characters = []

        # Settings/locations
        self.settings = []

        # Plot points and events
        self.plot_points = []

        # Chapter summaries
        self.chapter_summaries = []

        # Enhanced narrative tracking system
        self.narrative_tracking = {
            # Character development tracking
            "character_arcs": {},           # Track character development over time
            "character_emotions": {},       # Track emotional states of characters
            "character_knowledge": {},      # Track what each character knows
            "character_locations": {},      # Track where each character is at any point

            # Relationship tracking
            "relationships": {},            # Track relationships between characters
            "relationship_development": {}, # Track how relationships change over time

            # Plot tracking
            "plot_threads": {},             # Track ongoing plot threads
            "unresolved_questions": [],     # Track unresolved plot points
            "foreshadowing": [],            # Track foreshadowing elements
            "callbacks": [],                # Track callbacks to earlier events
            "plot_progression": {},         # Track progression of major plot arcs

            # World building
            "world_building": {},           # Track world-building elements
            "locations_visited": {},        # Track locations visited in each chapter
            "objects_of_significance": {},  # Track important objects

            # Narrative structure
            "timeline": [],                 # Track chronological events
            "pov_shifts": {},               # Track POV shifts between chapters
            "chapter_connections": {},      # Track connections between chapters
            "scene_transitions": {},        # Track transitions between scenes

            # Thematic elements
            "themes_and_motifs": {},        # Track recurring themes and motifs
            "symbols": {},                  # Track symbolic elements
            "tone_shifts": {},              # Track shifts in narrative tone

            # Continuity tracking
            "continuity_elements": {},      # Track elements that need continuity
            "time_of_day": {},              # Track time of day in each chapter
            "weather_conditions": {},       # Track weather conditions
            "clothing_and_appearance": {},  # Track character clothing and appearance
        }

        # Load existing memory if available
        self.load_memory()

    def _sanitize_filename(self, filename: str) -> str:
        """
        Sanitize a string to be used as a filename.

        Args:
            filename: The string to sanitize

        Returns:
            A sanitized filename
        """
        # Replace invalid characters with underscores
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            filename = filename.replace(char, '_')
        return filename

    def save_memory(self) -> None:
        """Save the current memory state to a file."""
        # Update the last_updated timestamp
        self.metadata["last_updated"] = datetime.now().isoformat()

        # Prepare the memory data
        memory_data = {
            "metadata": self.metadata,
            "structure": self.structure,
            "characters": self.characters,
            "settings": self.settings,
            "plot_points": self.plot_points,
            "chapter_summaries": self.chapter_summaries,
            "narrative_tracking": self.narrative_tracking,
        }

        # Save to file
        with open(self.memory_file, 'w', encoding='utf-8') as f:
            json.dump(memory_data, f, indent=2, ensure_ascii=False)

    def set_output_directory(self, output_dir: str) -> None:
        """
        Update the output directory for memory files.

        Args:
            output_dir: New output directory
        """
        if not output_dir:
            return

        # Create the directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Normalize output directory path with forward slashes
        normalized_output_dir = output_dir.replace('\\', '/')

        # Check if we need to move an existing memory file
        old_memory_file = self.memory_file
        memory_filename = os.path.basename(old_memory_file)
        new_memory_file = os.path.join(normalized_output_dir, memory_filename).replace('\\', '/')

        # Update the memory file path
        self.output_dir = normalized_output_dir
        self.memory_file = new_memory_file

        # If the old file exists and is different from the new path, move it
        if os.path.exists(old_memory_file) and old_memory_file != new_memory_file:
            try:
                # Read the old file
                with open(old_memory_file, 'r', encoding='utf-8') as f:
                    memory_data = json.load(f)

                # Write to the new location
                with open(new_memory_file, 'w', encoding='utf-8') as f:
                    json.dump(memory_data, f, indent=2, ensure_ascii=False)

                # Optionally remove the old file
                try:
                    os.remove(old_memory_file)
                except:
                    pass  # Ignore errors when removing old file
            except Exception as e:
                print(f"Error moving memory file: {e}")

        # Save memory to the new location
        self.save_memory()

    def load_memory(self) -> bool:
        """
        Load memory from file if it exists.

        Returns:
            True if memory was loaded, False otherwise
        """
        # Ensure memory file path uses consistent separators
        normalized_memory_file = self.memory_file.replace('\\', '/')

        if not os.path.exists(normalized_memory_file):
            # Try to find a memory file in the root directory with the same name
            root_memory_file = os.path.basename(normalized_memory_file)
            if os.path.exists(root_memory_file) and self.output_dir:
                # Move the file to the output directory
                try:
                    with open(root_memory_file, 'r', encoding='utf-8') as f:
                        memory_data = json.load(f)

                    # Ensure directory exists
                    os.makedirs(os.path.dirname(normalized_memory_file), exist_ok=True)

                    with open(normalized_memory_file, 'w', encoding='utf-8') as f:
                        json.dump(memory_data, f, indent=2, ensure_ascii=False)

                    # Try to remove the old file
                    try:
                        os.remove(root_memory_file)
                    except:
                        pass  # Ignore errors when removing old file

                except Exception as e:
                    print(f"Error moving memory file: {e}")
                    return False
            else:
                return False

        # Update memory file path to use normalized path
        self.memory_file = normalized_memory_file

        try:
            with open(self.memory_file, 'r', encoding='utf-8') as f:
                memory_data = json.load(f)

            # Update attributes
            self.metadata = memory_data.get("metadata", self.metadata)
            self.structure = memory_data.get("structure", self.structure)
            self.characters = memory_data.get("characters", self.characters)
            self.settings = memory_data.get("settings", self.settings)
            self.plot_points = memory_data.get("plot_points", self.plot_points)
            self.chapter_summaries = memory_data.get("chapter_summaries", self.chapter_summaries)
            self.narrative_tracking = memory_data.get("narrative_tracking", self.narrative_tracking)

            return True
        except Exception as e:
            print(f"Error loading memory: {e}")
            # Create a new memory file if loading failed
            self.save_memory()
            return False

    def update_metadata(self, **kwargs) -> None:
        """
        Update novel metadata.

        Args:
            **kwargs: Key-value pairs to update in metadata
        """
        for key, value in kwargs.items():
            if key in self.metadata:
                self.metadata[key] = value
        self.save_memory()

    def set_novel_structure(self, total_chapters: int, target_word_count: int, outline: List[str]) -> None:
        """
        Set the novel structure.

        Args:
            total_chapters: Total number of chapters
            target_word_count: Target word count for the novel
            outline: List of chapter titles or brief descriptions
        """
        self.structure["total_chapters"] = total_chapters
        self.structure["target_word_count"] = target_word_count
        self.structure["outline"] = outline
        self.save_memory()

    def add_character(self, character: Dict[str, Any]) -> None:
        """
        Add a character to the novel.

        Args:
            character: Dictionary containing character details
        """
        self.characters.append(character)
        self.save_memory()

    def add_setting(self, setting: Dict[str, Any]) -> None:
        """
        Add a setting/location to the novel.

        Args:
            setting: Dictionary containing setting details
        """
        self.settings.append(setting)
        self.save_memory()

    def add_plot_point(self, plot_point: Dict[str, Any]) -> None:
        """
        Add a plot point to the novel.

        Args:
            plot_point: Dictionary containing plot point details
        """
        self.plot_points.append(plot_point)
        self.save_memory()

    def add_chapter_summary(self, chapter_num: int, summary: str, word_count: int) -> None:
        """
        Add a chapter summary.

        Args:
            chapter_num: Chapter number
            summary: Brief summary of the chapter
            word_count: Word count of the chapter
        """
        # Update current word count
        self.structure["current_word_count"] += word_count

        # Add chapter summary
        self.chapter_summaries.append({
            "chapter_num": chapter_num,
            "summary": summary,
            "word_count": word_count,
        })

        self.save_memory()

    def update_narrative_tracking(self, chapter_num: int, chapter_data: Dict[str, Any]) -> None:
        """
        Update the narrative tracking with information from a generated chapter.

        Args:
            chapter_num: The chapter number
            chapter_data: Dictionary containing extracted narrative elements
        """
        # Ensure chapter_num is an integer
        chapter_num = int(chapter_num)
        # Update character arcs and emotions
        if "character_updates" in chapter_data:
            for char_name, updates in chapter_data["character_updates"].items():
                # Initialize character entry if it doesn't exist
                if char_name not in self.narrative_tracking["character_arcs"]:
                    self.narrative_tracking["character_arcs"][char_name] = {}
                if char_name not in self.narrative_tracking["character_emotions"]:
                    self.narrative_tracking["character_emotions"][char_name] = {}
                if char_name not in self.narrative_tracking["character_knowledge"]:
                    self.narrative_tracking["character_knowledge"][char_name] = {}
                if char_name not in self.narrative_tracking["character_locations"]:
                    self.narrative_tracking["character_locations"][char_name] = {}

                # Update character arc
                if "development" in updates:
                    self.narrative_tracking["character_arcs"][char_name][str(chapter_num)] = updates["development"]

                # Update character emotions
                if "emotions" in updates:
                    self.narrative_tracking["character_emotions"][char_name][str(chapter_num)] = updates["emotions"]

                # Update character knowledge
                if "knowledge" in updates:
                    self.narrative_tracking["character_knowledge"][char_name][str(chapter_num)] = updates["knowledge"]

                # Update character location
                if "location" in updates:
                    self.narrative_tracking["character_locations"][char_name][str(chapter_num)] = updates["location"]

        # Update relationships
        if "relationship_updates" in chapter_data:
            for rel_key, updates in chapter_data["relationship_updates"].items():
                # Initialize relationship entry if it doesn't exist
                if rel_key not in self.narrative_tracking["relationships"]:
                    self.narrative_tracking["relationships"][rel_key] = {}
                if rel_key not in self.narrative_tracking["relationship_development"]:
                    self.narrative_tracking["relationship_development"][rel_key] = {}

                # Update relationship status
                self.narrative_tracking["relationships"][rel_key][str(chapter_num)] = updates["status"]

                # Update relationship development
                if "development" in updates:
                    self.narrative_tracking["relationship_development"][rel_key][str(chapter_num)] = updates["development"]

        # Update plot threads
        if "plot_updates" in chapter_data:
            for thread_name, updates in chapter_data["plot_updates"].items():
                # Initialize plot thread if it doesn't exist
                if thread_name not in self.narrative_tracking["plot_threads"]:
                    self.narrative_tracking["plot_threads"][thread_name] = {}
                if thread_name not in self.narrative_tracking["plot_progression"]:
                    self.narrative_tracking["plot_progression"][thread_name] = {}

                # Update plot thread
                self.narrative_tracking["plot_threads"][thread_name][str(chapter_num)] = updates["status"]

                # Update plot progression
                if "progression" in updates:
                    self.narrative_tracking["plot_progression"][thread_name][str(chapter_num)] = updates["progression"]

        # Update unresolved questions
        if "unresolved_questions" in chapter_data:
            for question in chapter_data["unresolved_questions"]:
                if question not in self.narrative_tracking["unresolved_questions"]:
                    self.narrative_tracking["unresolved_questions"].append(question)

        # Update foreshadowing
        if "foreshadowing" in chapter_data:
            for foreshadow in chapter_data["foreshadowing"]:
                if foreshadow not in self.narrative_tracking["foreshadowing"]:
                    self.narrative_tracking["foreshadowing"].append(foreshadow)

        # Update callbacks
        if "callbacks" in chapter_data:
            for callback in chapter_data["callbacks"]:
                if callback not in self.narrative_tracking["callbacks"]:
                    self.narrative_tracking["callbacks"].append(callback)

        # Update world building
        if "world_building" in chapter_data:
            for element, details in chapter_data["world_building"].items():
                if element not in self.narrative_tracking["world_building"]:
                    self.narrative_tracking["world_building"][element] = {}
                self.narrative_tracking["world_building"][element][str(chapter_num)] = details

        # Update locations visited
        if "locations" in chapter_data:
            self.narrative_tracking["locations_visited"][str(chapter_num)] = chapter_data["locations"]

        # Update objects of significance
        if "objects" in chapter_data:
            for obj, details in chapter_data["objects"].items():
                if obj not in self.narrative_tracking["objects_of_significance"]:
                    self.narrative_tracking["objects_of_significance"][obj] = {}
                self.narrative_tracking["objects_of_significance"][obj][str(chapter_num)] = details

        # Update timeline
        if "timeline_events" in chapter_data:
            for event in chapter_data["timeline_events"]:
                self.narrative_tracking["timeline"].append({
                    "chapter": chapter_num,
                    "event": event
                })

        # Update POV shifts
        if "pov" in chapter_data:
            self.narrative_tracking["pov_shifts"][str(chapter_num)] = chapter_data["pov"]

        # Update chapter connections
        if "connections" in chapter_data:
            self.narrative_tracking["chapter_connections"][str(chapter_num)] = chapter_data["connections"]

        # Update scene transitions
        if "scene_transitions" in chapter_data:
            self.narrative_tracking["scene_transitions"][str(chapter_num)] = chapter_data["scene_transitions"]

        # Update themes and motifs
        if "themes" in chapter_data:
            for theme, details in chapter_data["themes"].items():
                if theme not in self.narrative_tracking["themes_and_motifs"]:
                    self.narrative_tracking["themes_and_motifs"][theme] = {}
                self.narrative_tracking["themes_and_motifs"][theme][str(chapter_num)] = details

        # Update symbols
        if "symbols" in chapter_data:
            for symbol, details in chapter_data["symbols"].items():
                if symbol not in self.narrative_tracking["symbols"]:
                    self.narrative_tracking["symbols"][symbol] = {}
                self.narrative_tracking["symbols"][symbol][str(chapter_num)] = details

        # Update tone shifts
        if "tone" in chapter_data:
            self.narrative_tracking["tone_shifts"][str(chapter_num)] = chapter_data["tone"]

        # Update continuity elements
        if "continuity" in chapter_data:
            for element, details in chapter_data["continuity"].items():
                if element not in self.narrative_tracking["continuity_elements"]:
                    self.narrative_tracking["continuity_elements"][element] = {}
                self.narrative_tracking["continuity_elements"][element][str(chapter_num)] = details

        # Update time of day
        if "time_of_day" in chapter_data:
            self.narrative_tracking["time_of_day"][str(chapter_num)] = chapter_data["time_of_day"]

        # Update weather conditions
        if "weather" in chapter_data:
            self.narrative_tracking["weather_conditions"][str(chapter_num)] = chapter_data["weather"]

        # Update clothing and appearance
        if "appearance" in chapter_data:
            for char, details in chapter_data["appearance"].items():
                if char not in self.narrative_tracking["clothing_and_appearance"]:
                    self.narrative_tracking["clothing_and_appearance"][char] = {}
                self.narrative_tracking["clothing_and_appearance"][char][str(chapter_num)] = details

        # Save the updated narrative tracking
        self.save_memory()

    def extract_narrative_elements(self, chapter_text: str, chapter_num: int, gemini_client=None) -> Dict[str, Any]:
        """
        Extract narrative elements from a chapter for tracking using Gemini.

        Args:
            chapter_text: The text of the chapter
            chapter_num: The chapter number
            gemini_client: Optional GeminiClient instance

        Returns:
            Dictionary containing extracted narrative elements
        """
        if not gemini_client:
            # If no Gemini client is provided, return an empty dictionary
            return {}

        # Create a prompt for Gemini to extract narrative elements
        extraction_prompt = f"""
        Analyze the following chapter (Chapter {chapter_num}) and extract key narrative elements for tracking.

        Extract the following information in a structured JSON format:

        1. Character updates:
           - For each character mentioned, track their development, emotions, knowledge gained, and current location

        2. Relationship updates:
           - For each relationship between characters, track the current status and development

        3. Plot updates:
           - For each plot thread, track its current status and progression

        4. Unresolved questions introduced in this chapter

        5. Foreshadowing elements introduced in this chapter

        6. Callbacks to earlier events

        7. World building elements introduced or expanded

        8. Locations visited in this chapter

        9. Objects of significance introduced or used

        10. Timeline events that occurred

        11. POV character for this chapter

        12. Connections to other chapters

        13. Scene transitions within the chapter

        14. Themes and motifs present

        15. Symbols used

        16. Overall tone of the chapter

        17. Continuity elements to track (things that need to remain consistent)

        18. Time of day during the chapter

        19. Weather conditions

        20. Character clothing and appearance details

        Format your response as a JSON object with these categories as keys. Be thorough but concise.

        CHAPTER TEXT:
        ```
        {chapter_text[:10000]}... [chapter continues]
        ```

        JSON RESPONSE:
        """

        try:
            # Generate the extraction using Gemini
            response = gemini_client.generate_content(extraction_prompt, temperature=0.2, max_tokens=4000)

            # Try to parse the response as JSON
            try:
                # Find JSON content in the response
                start_idx = response.find('{')
                end_idx = response.rfind('}') + 1

                if start_idx >= 0 and end_idx > start_idx:
                    json_str = response[start_idx:end_idx]
                    extracted_data = json.loads(json_str)
                    return extracted_data
                else:
                    # If JSON parsing fails, return a basic structure
                    return self._fallback_extraction(chapter_text, chapter_num)

            except json.JSONDecodeError:
                # If JSON parsing fails, return a basic structure
                return self._fallback_extraction(chapter_text, chapter_num)

        except Exception as e:
            print(f"Error extracting narrative elements: {e}")
            return {}

    def _fallback_extraction(self, chapter_text: str, chapter_num: int) -> Dict[str, Any]:
        """
        Fallback method for basic narrative element extraction when Gemini fails.

        Args:
            chapter_text: The text of the chapter
            chapter_num: The chapter number

        Returns:
            Dictionary containing basic extracted narrative elements
        """
        # Extract character names from the chapter
        character_names = set()
        for char in self.characters:
            name = char.get("name", "")
            if name and name in chapter_text:
                character_names.add(name)

        # Create basic character updates
        character_updates = {}
        for name in character_names:
            character_updates[name] = {
                "development": "Appeared in chapter",
                "emotions": "Unknown",
                "knowledge": "Unknown",
                "location": "Unknown"
            }

        # Extract POV character based on chapter number
        pov_character = None
        pov_characters = []
        for char in self.characters:
            if char.get("pov_character") is True or char.get("pov_character") == "true":
                pov_characters.append(char)

        # Sort by POV order if available
        pov_characters.sort(key=lambda x: x.get("pov_order", 999))

        if pov_characters:
            if len(pov_characters) >= 2:
                # Odd chapters use first POV character, even chapters use second
                pov_index = 0 if chapter_num % 2 == 1 else 1
                pov_character = pov_characters[pov_index].get("name")
            else:
                # If only one POV character, use that one
                pov_character = pov_characters[0].get("name")

        # Create a basic extraction result
        return {
            "character_updates": character_updates,
            "pov": pov_character,
            "time_of_day": "Unknown",
            "weather": "Unknown"
        }

    def get_context_for_chapter(self, chapter_num: int) -> Dict[str, Any]:
        """
        Get the context needed for generating a specific chapter.

        Args:
            chapter_num: The chapter number to generate

        Returns:
            Dictionary containing context information
        """
        # Ensure chapter_num is an integer
        chapter_num = int(chapter_num)
        # Get previous chapter summaries
        previous_chapters = [
            summary for summary in self.chapter_summaries
            if summary["chapter_num"] < chapter_num
        ]

        # Get relevant plot points for this chapter
        relevant_plot_points = self.plot_points

        # Get narrative tracking information relevant to this chapter
        narrative_context = self._get_narrative_context_for_chapter(chapter_num)

        # Create base context
        context = {
            "metadata": self.metadata,
            "structure": self.structure,
            "characters": self.characters,
            "settings": self.settings,
            "previous_chapters": previous_chapters,
            "relevant_plot_points": relevant_plot_points,
            "chapter_to_generate": chapter_num,
            "chapter_title": self.structure["outline"][chapter_num - 1] if chapter_num <= len(self.structure["outline"]) else f"Chapter {chapter_num}",
            "narrative_context": narrative_context,
        }

        # Add series context if this book is part of a series
        if self.series_manager and self.book_number:
            series_context = self.series_manager.get_context_for_book(self.book_number)
            context["series_context"] = series_context

            # Add recurring characters from the series
            recurring_characters = series_context.get("recurring_characters", [])
            # Only add recurring characters that aren't already in the current book's characters
            current_character_names = [char.get("name") for char in self.characters]
            for rec_char in recurring_characters:
                if rec_char.get("name") not in current_character_names:
                    context["recurring_characters"] = recurring_characters
                    break

            # Add series arcs
            context["series_arcs"] = series_context.get("series_arcs", [])

            # Add universe information
            context["universe"] = series_context.get("universe", {})

        return context

    def _get_narrative_context_for_chapter(self, chapter_num: int) -> Dict[str, Any]:
        """
        Get narrative tracking information relevant to a specific chapter.

        Args:
            chapter_num: The chapter number

        Returns:
            Dictionary containing narrative context
        """
        # Ensure chapter_num is an integer
        chapter_num = int(chapter_num)
        # Determine which character's POV this chapter should use
        pov_character = None
        if chapter_num in self.narrative_tracking["pov_shifts"]:
            pov_character = self.narrative_tracking["pov_shifts"][chapter_num]
        else:
            # Default POV assignment based on chapter number (odd/even)
            pov_characters = []
            for char in self.characters:
                if char.get("pov_character") is True or char.get("pov_character") == "true":
                    pov_characters.append(char)

            # Sort by POV order if available
            pov_characters.sort(key=lambda x: x.get("pov_order", 999))

            if pov_characters:
                if len(pov_characters) >= 2:
                    # Odd chapters use first POV character, even chapters use second
                    pov_index = 0 if chapter_num % 2 == 1 else 1
                    pov_character = pov_characters[pov_index].get("name")
                else:
                    # If only one POV character, use that one
                    pov_character = pov_characters[0].get("name")

        # Get character arcs and emotions for relevant characters
        character_arcs = {}
        character_emotions = {}
        character_knowledge = {}
        character_locations = {}

        for char in self.characters:
            char_name = char.get("name")
            if char_name:
                # Get character arc
                if char_name in self.narrative_tracking["character_arcs"]:
                    # Get the most recent character arc update
                    char_arc_chapters = sorted([int(c) for c in self.narrative_tracking["character_arcs"][char_name].keys() if int(c) < chapter_num], reverse=True)
                    if char_arc_chapters:
                        character_arcs[char_name] = self.narrative_tracking["character_arcs"][char_name][char_arc_chapters[0]]

                # Get character emotions
                if char_name in self.narrative_tracking["character_emotions"]:
                    # Get the most recent emotions update
                    char_emotion_chapters = sorted([int(c) for c in self.narrative_tracking["character_emotions"][char_name].keys() if int(c) < chapter_num], reverse=True)
                    if char_emotion_chapters:
                        character_emotions[char_name] = self.narrative_tracking["character_emotions"][char_name][char_emotion_chapters[0]]

                # Get character knowledge
                if char_name in self.narrative_tracking["character_knowledge"]:
                    # Get the most recent knowledge update
                    char_knowledge_chapters = sorted([int(c) for c in self.narrative_tracking["character_knowledge"][char_name].keys() if int(c) < chapter_num], reverse=True)
                    if char_knowledge_chapters:
                        character_knowledge[char_name] = self.narrative_tracking["character_knowledge"][char_name][char_knowledge_chapters[0]]

                # Get character location
                if char_name in self.narrative_tracking["character_locations"]:
                    # Get the most recent location update
                    char_location_chapters = sorted([int(c) for c in self.narrative_tracking["character_locations"][char_name].keys() if int(c) < chapter_num], reverse=True)
                    if char_location_chapters:
                        character_locations[char_name] = self.narrative_tracking["character_locations"][char_name][char_location_chapters[0]]

        # Get relationship status for relevant relationships
        relationships = {}
        for rel_key in self.narrative_tracking["relationships"]:
            # Get the most recent relationship update
            rel_chapters = sorted([int(c) for c in self.narrative_tracking["relationships"][rel_key].keys() if int(c) < chapter_num], reverse=True)
            if rel_chapters:
                relationships[rel_key] = self.narrative_tracking["relationships"][rel_key][rel_chapters[0]]

        # Get plot thread status for relevant plot threads
        plot_threads = {}
        for thread_name in self.narrative_tracking["plot_threads"]:
            # Get the most recent plot thread update
            thread_chapters = sorted([int(c) for c in self.narrative_tracking["plot_threads"][thread_name].keys() if int(c) < chapter_num], reverse=True)
            if thread_chapters:
                plot_threads[thread_name] = self.narrative_tracking["plot_threads"][thread_name][thread_chapters[0]]

        # Get unresolved questions
        unresolved_questions = self.narrative_tracking["unresolved_questions"]

        # Get foreshadowing elements
        foreshadowing = self.narrative_tracking["foreshadowing"]

        # Get callbacks
        callbacks = self.narrative_tracking["callbacks"]

        # Get world building elements
        world_building = {}
        for element in self.narrative_tracking["world_building"]:
            # Get the most recent world building update
            element_chapters = sorted([int(c) for c in self.narrative_tracking["world_building"][element].keys() if int(c) < chapter_num], reverse=True)
            if element_chapters:
                world_building[element] = self.narrative_tracking["world_building"][element][element_chapters[0]]

        # Get locations visited in previous chapter
        locations_visited = {}
        if chapter_num - 1 in self.narrative_tracking["locations_visited"]:
            locations_visited = self.narrative_tracking["locations_visited"][chapter_num - 1]

        # Get objects of significance
        objects = {}
        for obj in self.narrative_tracking["objects_of_significance"]:
            # Get the most recent object update
            obj_chapters = sorted([int(c) for c in self.narrative_tracking["objects_of_significance"][obj].keys() if int(c) < chapter_num], reverse=True)
            if obj_chapters:
                objects[obj] = self.narrative_tracking["objects_of_significance"][obj][obj_chapters[0]]

        # Get themes and motifs
        themes = {}
        for theme in self.narrative_tracking["themes_and_motifs"]:
            # Get all theme occurrences
            theme_chapters = sorted([int(c) for c in self.narrative_tracking["themes_and_motifs"][theme].keys() if int(c) < chapter_num])
            if theme_chapters:
                themes[theme] = [self.narrative_tracking["themes_and_motifs"][theme][c] for c in theme_chapters]

        # Get symbols
        symbols = {}
        for symbol in self.narrative_tracking["symbols"]:
            # Get all symbol occurrences
            symbol_chapters = sorted([int(c) for c in self.narrative_tracking["symbols"][symbol].keys() if int(c) < chapter_num])
            if symbol_chapters:
                symbols[symbol] = [self.narrative_tracking["symbols"][symbol][c] for c in symbol_chapters]

        # Get tone from previous chapter
        tone = None
        if chapter_num - 1 in self.narrative_tracking["tone_shifts"]:
            tone = self.narrative_tracking["tone_shifts"][chapter_num - 1]

        # Get continuity elements
        continuity = {}
        for element in self.narrative_tracking["continuity_elements"]:
            # Get the most recent continuity update
            element_chapters = sorted([int(c) for c in self.narrative_tracking["continuity_elements"][element].keys() if int(c) < chapter_num], reverse=True)
            if element_chapters:
                continuity[element] = self.narrative_tracking["continuity_elements"][element][element_chapters[0]]

        # Get time of day from previous chapter
        time_of_day = None
        if chapter_num - 1 in self.narrative_tracking["time_of_day"]:
            time_of_day = self.narrative_tracking["time_of_day"][chapter_num - 1]

        # Get weather conditions from previous chapter
        weather = None
        if chapter_num - 1 in self.narrative_tracking["weather_conditions"]:
            weather = self.narrative_tracking["weather_conditions"][chapter_num - 1]

        # Get character appearance
        appearance = {}
        for char in self.narrative_tracking["clothing_and_appearance"]:
            # Get the most recent appearance update
            appearance_chapters = sorted([int(c) for c in self.narrative_tracking["clothing_and_appearance"][char].keys() if int(c) < chapter_num], reverse=True)
            if appearance_chapters:
                appearance[char] = self.narrative_tracking["clothing_and_appearance"][char][appearance_chapters[0]]

        return {
            "pov_character": pov_character,
            "character_arcs": character_arcs,
            "character_emotions": character_emotions,
            "character_knowledge": character_knowledge,
            "character_locations": character_locations,
            "relationships": relationships,
            "plot_threads": plot_threads,
            "unresolved_questions": unresolved_questions,
            "foreshadowing": foreshadowing,
            "callbacks": callbacks,
            "world_building": world_building,
            "locations_visited": locations_visited,
            "objects": objects,
            "themes": themes,
            "symbols": symbols,
            "tone": tone,
            "continuity": continuity,
            "time_of_day": time_of_day,
            "weather": weather,
            "appearance": appearance,
        }
