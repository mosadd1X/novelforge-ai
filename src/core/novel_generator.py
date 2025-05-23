"""
Core novel generation functionality.
"""
import os
import json
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from rich.console import Console
from rich.progress import Progress

from src.core.gemini_client import GeminiClient
from src.core.memory_manager import MemoryManager
from src.utils.word_counter import count_words
from src.utils.genre_defaults import get_genre_defaults, create_flexible_pov_structure, determine_character_gender, assign_chapter_pov

# Import SeriesManager conditionally to avoid circular imports
try:
    from src.core.series_manager import SeriesManager
except ImportError:
    SeriesManager = None

console = Console()


class NovelGenerator:
    """
    Core novel generation functionality.
    """

    def __init__(self):
        """Initialize the novel generator."""
        self.gemini = GeminiClient()
        self.memory_manager = None
        self.generation_options = None

    def initialize_novel(
        self, title: str, author: str, description: str, genre: str, target_audience: str,
        output_dir: str = None, series_manager=None, book_number: int = None
    ) -> MemoryManager:
        """
        Initialize a new novel with basic information.

        Args:
            title: Novel title
            author: Author name
            description: Brief description of the novel
            genre: Genre of the novel
            target_audience: Target audience for the novel
            output_dir: Directory to save memory files (default: None)
            series_manager: Optional SeriesManager instance if this book is part of a series
            book_number: Book number in the series (if part of a series)

        Returns:
            MemoryManager instance for the novel
        """
        self.memory_manager = MemoryManager(title, output_dir, series_manager, book_number)
        self.memory_manager.update_metadata(
            author=author,
            description=description,
            genre=genre,
            target_audience=target_audience,
        )

        # If this is part of a series, update the series with book information
        if series_manager and book_number is None:
            # This is a new book in the series
            book_data = {
                "title": title,
                "author": author,
                "description": description,
                "genre": genre,
                "target_audience": target_audience,
                "created_at": datetime.now().isoformat(),
            }
            new_book_number = series_manager.add_book(book_data)
            self.memory_manager.book_number = new_book_number
            self.memory_manager.metadata["series"]["book_number"] = new_book_number

        return self.memory_manager

    def set_output_directory(self, output_dir: str) -> None:
        """
        Set the output directory for memory files.

        Args:
            output_dir: Directory to save memory files
        """
        if self.memory_manager:
            self.memory_manager.set_output_directory(output_dir)

    def set_generation_options(self, options: Dict[str, Any]) -> None:
        """
        Set generation options for the novel.

        Args:
            options: Dictionary containing generation options
        """
        self.generation_options = options

    def generate_writer_profile(self) -> Dict[str, Any]:
        """
        Generate a writer profile based on the novel metadata.

        Returns:
            Dictionary containing writer profile information
        """
        if not self.memory_manager:
            raise ValueError("Novel not initialized. Call initialize_novel first.")

        prompt = f"""
        Create a detailed writer profile for an author who would write a {self.memory_manager.metadata['genre']} novel
        titled "{self.memory_manager.metadata['title']}" for {self.memory_manager.metadata['target_audience']} audience.

        The novel is described as: {self.memory_manager.metadata['description']}

        Include the following in your response:
        1. Writing style and voice
        2. Literary influences
        3. Thematic focuses
        4. Narrative techniques
        5. Strengths as a writer

        Format your response as a JSON object with these fields.
        """

        response = self.gemini.generate_content(prompt, temperature=0.7)

        # Try to parse the response as JSON
        try:
            # Find JSON content in the response
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1

            if start_idx >= 0 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                writer_profile = json.loads(json_str)
            else:
                # If JSON parsing fails, create a structured dictionary from the text
                writer_profile = {
                    "writing_style": "Detailed and engaging",
                    "literary_influences": "Various classic and contemporary authors",
                    "thematic_focuses": f"Themes relevant to {self.memory_manager.metadata['genre']}",
                    "narrative_techniques": "Varied techniques appropriate for the genre",
                    "strengths": "Creating compelling characters and plots",
                    "raw_response": response
                }
        except json.JSONDecodeError:
            # If JSON parsing fails, create a structured dictionary from the text
            writer_profile = {
                "writing_style": "Detailed and engaging",
                "literary_influences": "Various classic and contemporary authors",
                "thematic_focuses": f"Themes relevant to {self.memory_manager.metadata['genre']}",
                "narrative_techniques": "Varied techniques appropriate for the genre",
                "strengths": "Creating compelling characters and plots",
                "raw_response": response
            }

        return writer_profile

    def generate_novel_outline(self, writer_profile: Dict[str, Any]) -> Tuple[List[str], int]:
        """
        Generate a novel outline based on metadata and writer profile.

        Args:
            writer_profile: Writer profile information

        Returns:
            Tuple of (chapter_outlines, recommended_chapter_count)
        """
        # Track subplots and narrative threads for coherence
        self.narrative_threads = {
            "main_plot": [],
            "subplots": [],
            "character_arcs": {},
            "themes": []
        }
        if not self.memory_manager:
            raise ValueError("Novel not initialized. Call initialize_novel first.")

        # Get genre-specific chapter count and word count recommendations
        genre = self.memory_manager.metadata['genre']
        target_audience = self.memory_manager.metadata['target_audience']

        # Check if this is the Test genre - if so, use simplified outline generation
        if genre.lower() == "test":
            console.print("[yellow]Test genre detected - generating simplified outline[/yellow]")
            return self._generate_test_genre_outline()

        # Use generation options if available
        target_length = "medium"
        writing_style = writer_profile.get('writing_style', 'Detailed and engaging')
        pov = "Third person limited"
        themes = []
        chapter_count = 0
        target_word_count = 0

        if self.generation_options:
            target_length = self.generation_options.get('target_length', target_length)
            writing_style = self.generation_options.get('writing_style', writing_style)
            pov = self.generation_options.get('pov', pov)
            themes = self.generation_options.get('themes', [])
            chapter_count = self.generation_options.get('chapter_count', 0)
            target_word_count = self.generation_options.get('target_word_count', 0)

        # Create themes string
        themes_str = ", ".join(themes) if themes else writer_profile.get('thematic_focuses', 'Various themes')

        # Add specific instructions based on options
        length_instruction = f"This should be a {target_length} length novel."
        count_instruction = ""
        if chapter_count and target_word_count:
            count_instruction = f"Aim for approximately {chapter_count} chapters and {target_word_count:,} total words."

        prompt = f"""
        Create a detailed chapter-by-chapter outline for a {genre} novel titled
        "{self.memory_manager.metadata['title']}" for {target_audience} audience.

        The novel is described as: {self.memory_manager.metadata['description']}

        The author's writing style is: {writing_style}
        The author's thematic focuses are: {themes_str}
        Point of view: {pov}

        {length_instruction}
        {count_instruction}

        IMPORTANT NARRATIVE GUIDELINES:
        1. Develop a cohesive main plot with 2-3 well-integrated subplots that are introduced early and developed throughout
        2. Ensure all subplots connect meaningfully to the main narrative and themes
        3. Foreshadow major plot developments and twists at least 3-4 chapters before they occur
        4. Balance character development with plot progression in each chapter
        5. Maintain consistent thematic elements throughout the narrative
        6. Ensure each subplot has a clear arc with setup, development, and resolution

        For each chapter, provide:
        1. Chapter title
        2. Brief summary (2-3 sentences)
        3. Key plot points or character developments
        4. Which subplot elements appear and how they connect to the main plot
        5. Character development moments
        6. Thematic elements explored

        Format your response as a JSON object with these fields:
        - recommended_chapter_count: number
        - target_word_count: number
        - main_plot: object with setup, development, climax, and resolution fields
        - subplots: array of subplot objects, each with name, description, and arc fields
        - themes: array of theme objects with name and development fields
        - chapters: array of objects with title, summary, key_points, plot_threads, character_development, and thematic_elements fields
        """

        response = self.gemini.generate_content(prompt, temperature=0.7)

        # Try to parse the response as JSON
        try:
            # Clean the response to extract just the JSON part
            response_text = response.strip()

            # Remove markdown code block markers if present
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]

            # Find JSON content in the response
            start_idx = response_text.find('{')
            end_idx = response_text.rfind('}') + 1

            if start_idx >= 0 and end_idx > start_idx:
                json_str = response_text[start_idx:end_idx]
                outline_data = json.loads(json_str)

                # Extract chapter outlines
                chapters = outline_data.get('chapters', [])

                if not chapters and isinstance(outline_data, list):
                    # Handle case where the response is a list of chapters directly
                    chapters = outline_data

                # Store narrative structure data for coherence
                self.narrative_threads["main_plot"] = outline_data.get('main_plot', {})
                self.narrative_threads["subplots"] = outline_data.get('subplots', [])
                self.narrative_threads["themes"] = outline_data.get('themes', [])

                # Process chapters with enhanced metadata
                chapter_outlines = []
                for i, ch in enumerate(chapters):
                    if isinstance(ch, dict):
                        title = ch.get('title', f'Chapter {i+1}')
                        summary = ch.get('summary', '')

                        # Store additional narrative data
                        plot_threads = ch.get('plot_threads', {})
                        character_development = ch.get('character_development', {})
                        thematic_elements = ch.get('thematic_elements', [])

                        # Store in memory manager for later use in chapter generation
                        if self.memory_manager:
                            self.memory_manager.add_plot_point({
                                "chapter": i+1,
                                "title": title,
                                "summary": summary,
                                "plot_threads": plot_threads,
                                "character_development": character_development,
                                "thematic_elements": thematic_elements
                            })

                        # Add to chapter outlines
                        chapter_outlines.append(f"{title} - {summary}")
                    elif isinstance(ch, str):
                        chapter_outlines.append(ch)

                # Get recommended chapter count
                recommended_chapter_count = outline_data.get('recommended_chapter_count', len(chapters))
                if recommended_chapter_count == 0:
                    recommended_chapter_count = len(chapters)

                target_word_count = outline_data.get('target_word_count', 80000)

                # Ensure we have at least some chapters
                if len(chapter_outlines) == 0 or recommended_chapter_count == 0:
                    console.print("[yellow]Warning: No chapters found in the outline. Using fallback method.[/yellow]")
                    return self._fallback_outline_parsing(response)

                # Update memory manager with structure information
                self.memory_manager.set_novel_structure(
                    total_chapters=recommended_chapter_count,
                    target_word_count=target_word_count,
                    outline=chapter_outlines
                )

                console.print(f"[green]Successfully parsed outline with {recommended_chapter_count} chapters[/green]")
                return chapter_outlines, recommended_chapter_count
            else:
                # Try to find a JSON array instead
                start_idx = response_text.find('[')
                end_idx = response_text.rfind(']') + 1

                if start_idx >= 0 and end_idx > start_idx:
                    json_str = response_text[start_idx:end_idx]
                    chapters_array = json.loads(json_str)

                    chapter_outlines = []
                    for i, ch in enumerate(chapters_array):
                        if isinstance(ch, dict):
                            title = ch.get('title', f'Chapter {i+1}')
                            summary = ch.get('summary', '')
                            chapter_outlines.append(f"{title} - {summary}")
                        elif isinstance(ch, str):
                            chapter_outlines.append(ch)

                    recommended_chapter_count = len(chapter_outlines)

                    # Update memory manager with structure information
                    self.memory_manager.set_novel_structure(
                        total_chapters=recommended_chapter_count,
                        target_word_count=80000,
                        outline=chapter_outlines
                    )

                    console.print(f"[green]Successfully parsed outline array with {recommended_chapter_count} chapters[/green]")
                    return chapter_outlines, recommended_chapter_count
                else:
                    # Fallback if JSON parsing fails
                    console.print("[yellow]No JSON structure found in response. Using fallback method.[/yellow]")
                    return self._fallback_outline_parsing(response)

        except json.JSONDecodeError as e:
            # Fallback if JSON parsing fails
            console.print(f"[yellow]JSON parsing error: {e}. Using fallback method.[/yellow]")
            return self._fallback_outline_parsing(response)
        except Exception as e:
            console.print(f"[yellow]Error parsing outline: {e}. Using fallback method.[/yellow]")
            return self._fallback_outline_parsing(response)

    def _generate_test_genre_outline(self) -> Tuple[List[str], int]:
        """
        Generate a simplified outline for Test genre to save processing time.

        Returns:
            Tuple of (chapter_outlines, recommended_chapter_count)
        """
        title = self.memory_manager.metadata.get("title", "Test Novel")
        description = self.memory_manager.metadata.get("description", "A test novel for quick processing")

        # Create a simplified prompt for outline generation
        prompt = f"""
        # Test Genre Outline Generation

        Create a simple 3-5 chapter outline for a test novel titled "{title}".

        Novel description: {description}

        ## Requirements
        - Create a straightforward plot with clear beginning, middle, and end
        - Each chapter should have a clear purpose and advance the story
        - Keep the outline concise but sufficient for a coherent story
        - Format as a JSON object with these fields:
          - recommended_chapter_count: Number of chapters (3-5)
          - target_word_count: Total word count (9,000-12,000)
          - chapters: Array of chapter objects with title and summary fields

        Return only the JSON object.
        """

        # Generate with reduced token count
        response = self.gemini.generate_content(prompt, temperature=0.7, max_tokens=4000)

        # Try to parse the response as JSON
        try:
            # Find JSON content in the response
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1

            if start_idx >= 0 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                outline_data = json.loads(json_str)

                # Extract chapter outlines
                chapters = outline_data.get("chapters", [])
                chapter_outlines = []

                for ch in chapters:
                    title = ch.get("title", f"Chapter {len(chapter_outlines) + 1}")
                    summary = ch.get("summary", "No summary provided")
                    chapter_outlines.append(f"{title} - {summary}")

                # Get recommended chapter count and target word count
                recommended_chapter_count = outline_data.get("recommended_chapter_count", len(chapter_outlines))
                target_word_count = outline_data.get("target_word_count", 10000)  # Default for Test genre

                # Update memory manager with structure information
                self.memory_manager.set_novel_structure(
                    total_chapters=recommended_chapter_count,
                    target_word_count=target_word_count,
                    outline=chapter_outlines
                )

                return chapter_outlines, recommended_chapter_count
            else:
                # Fallback to basic outline if JSON parsing fails
                return self._fallback_test_outline()

        except (json.JSONDecodeError, Exception):
            # Fallback to basic outline if JSON parsing fails
            return self._fallback_test_outline()

    def _fallback_test_outline(self) -> Tuple[List[str], int]:
        """
        Create fallback outline for Test genre if generation fails.

        Returns:
            Tuple of (chapter_outlines, recommended_chapter_count)
        """
        # Create basic outline
        chapter_outlines = [
            "Introduction - The protagonist is introduced and the central conflict is established.",
            "Rising Action - The protagonist faces initial challenges and begins to address the conflict.",
            "Climax - The protagonist confronts the antagonist in a decisive moment.",
            "Resolution - The aftermath of the climax is explored and loose ends are tied up."
        ]

        recommended_chapter_count = 4
        target_word_count = 12000

        # Update memory manager with structure information
        self.memory_manager.set_novel_structure(
            total_chapters=recommended_chapter_count,
            target_word_count=target_word_count,
            outline=chapter_outlines
        )

        return chapter_outlines, recommended_chapter_count

    def _fallback_outline_parsing(self, response: str) -> Tuple[List[str], int]:
        """
        Fallback method to parse outline when JSON parsing fails.

        Args:
            response: Raw response from Gemini

        Returns:
            Tuple of (chapter_outlines, recommended_chapter_count)
        """
        lines = response.split('\n')
        chapter_outlines = []
        recommended_chapter_count = 0
        target_word_count = 80000  # Default

        # Try to extract chapter count and word count
        for line in lines:
            if "chapter count" in line.lower() and ":" in line:
                try:
                    recommended_chapter_count = int(line.split(':')[1].strip().split()[0])
                except (ValueError, IndexError):
                    pass

            if "word count" in line.lower() and ":" in line:
                try:
                    target_word_count = int(line.split(':')[1].strip().split()[0].replace(',', ''))
                except (ValueError, IndexError):
                    pass

        # Try to extract chapter outlines
        current_chapter = ""
        for line in lines:
            if line.strip().lower().startswith(("chapter ", "prologue", "epilogue")):
                if current_chapter:
                    chapter_outlines.append(current_chapter)
                current_chapter = line.strip()
            elif current_chapter and line.strip():
                current_chapter += " - " + line.strip()

        # Add the last chapter
        if current_chapter:
            chapter_outlines.append(current_chapter)

        # If we couldn't extract a chapter count or chapters, return an error
        if recommended_chapter_count == 0 or len(chapter_outlines) == 0:
            console.print("[bold red]Error: Could not generate a proper chapter outline.[/bold red]")
            console.print("[bold red]Please try again or provide more specific details about your novel.[/bold red]")

            # Return empty list and 0 count to signal the error
            return [], 0

        # Update memory manager with structure information
        self.memory_manager.set_novel_structure(
            total_chapters=recommended_chapter_count,
            target_word_count=target_word_count,
            outline=chapter_outlines
        )

        return chapter_outlines, recommended_chapter_count

    def generate_characters(self) -> List[Dict[str, Any]]:
        """
        Generate characters for the novel using the Gemini API.

        Returns:
            List of character dictionaries with name, role, appearance,
            personality, background, goals, and arc.
        """
        if not self.memory_manager:
            raise ValueError("Novel not initialized. Call initialize_novel first.")

        # Get novel metadata
        title = self.memory_manager.metadata.get("title", "the novel")
        description = self.memory_manager.metadata.get("description", "")
        genre = self.memory_manager.metadata.get("genre", "fiction")
        target_audience = self.memory_manager.metadata.get("target_audience", "adults")

        # Check if this is the Test genre - if so, use simplified character generation
        if genre.lower() == "test":
            console.print("[yellow]Test genre detected - generating simplified characters[/yellow]")
            return self._generate_test_genre_characters(title, description)

        # Get outline information
        outline = self.memory_manager.structure.get("outline", [])
        outline_str = "\n".join(outline) if outline else ""

        # Get subplot information if available
        subplot_info = ""
        if hasattr(self, 'narrative_threads') and self.narrative_threads:
            subplots = self.narrative_threads.get("subplots", [])
            if subplots:
                subplot_info = "Subplots in the story:\n"
                for subplot in subplots:
                    subplot_name = subplot.get("name", "")
                    subplot_desc = subplot.get("description", "")
                    subplot_info += f"- {subplot_name}: {subplot_desc}\n"

        # Create a structured prompt for character generation with improved depth requirements
        prompt = f"""
        Create a set of well-developed characters for a {genre} novel titled "{title}" for {target_audience}.

        The novel is described as: {description}

        Novel outline:
        {outline_str}

        {subplot_info}

        IMPORTANT CHARACTER DEVELOPMENT GUIDELINES:
        1. Create psychologically complex characters with clear motivations and internal conflicts
        2. Develop ALL characters with depth, including antagonists and supporting characters
        3. Give each character a distinct voice, speech patterns, and mannerisms
        4. Create meaningful relationships and dynamics between characters
        5. Ensure antagonists have understandable motivations, not just generic evil
        6. Include flaws and vulnerabilities for all characters, especially protagonists
        7. Develop backstories that directly influence present actions and decisions
        8. Create secondary characters with their own goals independent of the protagonist
        9. Ensure character arcs show meaningful growth or change throughout the story
        10. Include diverse personalities, backgrounds, and perspectives

        For each character, provide the following fields in a JSON object:
        - "name": (string) Character's full name
        - "role": (string) Their role (protagonist, antagonist, supporting, etc.)
        - "appearance": (string) Detailed physical description including distinctive features
        - "personality": (string) Comprehensive personality profile including traits, values, and contradictions
        - "background": (string) Detailed backstory that explains motivations and shapes current actions
        - "goals": (string) Primary and secondary goals, both external and internal
        - "arc": (string) Specific growth or change throughout the story
        - "relationships": (string) How they relate to other characters
        - "strengths": (string) Their key abilities or positive traits
        - "flaws": (string) Their weaknesses, blind spots, or negative traits
        - "voice": (string) Their speech patterns, vocabulary, and communication style

        Create characters with these guidelines:
        1. Include 1-2 main protagonists with complex internal conflicts
        2. Include 1-2 antagonists with understandable motivations and depth
        3. Include 3-4 supporting characters with their own arcs and purposes
        4. Ensure all characters have meaningful relationships and dynamics
        5. Make sure their goals and flaws create natural conflict

        Return ONLY a valid JSON array of character objects, nothing else.
        Example format:
        [
          {{
            "name": "John Doe",
            "role": "protagonist",
            "appearance": "Tall with brown hair and green eyes",
            "personality": "Brave but impulsive, with a strong sense of justice",
            "background": "Grew up in a small town, joined the police force to make a difference",
            "goals": "Wants to solve the case and bring the criminal to justice",
            "arc": "Learns to work with others and trust his team"
          }}
        ]
        """

        try:
            # Get response from Gemini
            response = self.gemini.generate_content(prompt, temperature=0.7)

            # Clean the response to extract just the JSON part
            response_text = response.strip()

            # Remove markdown code block markers if present
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.endswith('```'):
                response_text = response_text[:-3]

            # Parse the JSON response
            characters = json.loads(response_text)

            # Validate the characters
            if not isinstance(characters, list):
                raise ValueError("Expected a list of characters")

            # Ensure all required fields are present
            required_fields = ["name", "role", "appearance", "personality", "background", "goals", "arc"]
            optional_fields = ["relationships", "strengths", "flaws", "voice"]

            for char in characters:
                # Check required fields
                for field in required_fields:
                    if field not in char or not char[field]:
                        char[field] = f"Not specified"

                # Add optional fields if missing
                for field in optional_fields:
                    if field not in char or not char[field]:
                        if field == "relationships":
                            char[field] = "Relationships will develop throughout the story"
                        elif field == "strengths":
                            char[field] = "To be revealed through the narrative"
                        elif field == "flaws":
                            char[field] = "To be revealed through the narrative"
                        elif field == "voice":
                            char[field] = "Speaks in a manner consistent with their personality and background"

                # Determine character gender for POV purposes
                char["gender"] = determine_character_gender(char)

                # Assign POV character status for alternating POV genres
                if self.generation_options and (
                    self.generation_options.get('pov', "").lower() == "alternating povs" or
                    self.generation_options.get('pov_structure') == "flexible_alternating"
                ):
                    # Mark main characters as POV characters
                    if char.get("role", "").lower() in ["protagonist", "main character", "love interest"]:
                        char["pov_character"] = True
                        # Set POV order based on gender for balanced alternating
                        if char["gender"] == "male":
                            char["pov_order"] = 1
                        elif char["gender"] == "female":
                            char["pov_order"] = 2
                        else:
                            char["pov_order"] = 3

                # Add character to memory manager
                self.memory_manager.add_character(char)

            # Create POV structure if using flexible alternating POV
            if self.generation_options and (
                self.generation_options.get('pov', "").lower() == "alternating povs" or
                self.generation_options.get('pov_structure') == "flexible_alternating"
            ):
                pov_structure = create_flexible_pov_structure(characters, self.generation_options)
                # Store POV structure in memory manager for later use
                if hasattr(self.memory_manager, 'narrative_tracking'):
                    self.memory_manager.narrative_tracking["pov_structure"] = pov_structure

            return characters

        except json.JSONDecodeError as e:
            console.print(f"[bold red]Error parsing character JSON: {e}[/bold red]")
            console.print("[yellow]Attempting to fix malformed JSON...[/yellow]")

            # Try to extract JSON from malformed response
            try:
                # Look for JSON-like content between square brackets
                import re
                json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
                if json_match:
                    fixed_json = json_match.group(0)
                    characters = json.loads(fixed_json)

                    # Validate and add characters
                    required_fields = ["name", "role", "appearance", "personality", "background", "goals", "arc"]
                    for char in characters:
                        for field in required_fields:
                            if field not in char:
                                char[field] = "Not specified"
                        self.memory_manager.add_character(char)

                    return characters
                else:
                    raise ValueError("Could not extract JSON from response")

            except Exception as e2:
                console.print(f"[bold red]Failed to fix JSON: {e2}[/bold red]")
                return self._fallback_character_parsing(response_text)

        except Exception as e:
            console.print(f"[bold red]Error generating characters: {e}[/bold red]")
            return self._fallback_character_parsing(str(e))

    def _fallback_character_parsing(self, response_text: str) -> List[Dict[str, Any]]:
        """
        Fallback method to parse characters when JSON parsing fails.

        Args:
            response_text: Raw text response from the API

        Returns:
            List of character dictionaries
        """
        console.print("[yellow]Falling back to basic character parsing...[/yellow]")

        # Try to extract character information from the text
        characters = []
        current_char = {}

        # Simple parsing logic for text format
        lines = response_text.split('\n')
        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Look for character headers (e.g., "Character 1:" or "John Doe:")
            if ':' in line and len(line.split(':')) == 2 and len(line) < 50:
                # Save previous character if exists
                if current_char and 'name' in current_char:
                    characters.append(current_char)

                # Start new character
                name = line.split(':', 1)[0].strip()
                current_char = {'name': name}

            # Look for character attributes
            elif ':' in line and current_char and len(line.split(':', 1)) == 2:
                key, value = line.split(':', 1)
                key = key.strip().lower().replace(' ', '_')
                current_char[key] = value.strip()

        # Add the last character
        if current_char and 'name' in current_char:
            characters.append(current_char)

        # Ensure all required fields are present
        required_fields = ["name", "role", "appearance", "personality", "background", "goals", "arc"]
        for char in characters:
            for field in required_fields:
                if field not in char:
                    char[field] = f"Not specified ({field.replace('_', ' ')})"

            # Add character to memory manager
            if self.memory_manager:
                self.memory_manager.add_character(char)

        return characters

    def _generate_test_genre_characters(self, title: str, description: str) -> List[Dict[str, Any]]:
        """
        Generate simplified characters for Test genre to save processing time.

        Args:
            title: Novel title
            description: Novel description

        Returns:
            List of simplified character dictionaries
        """
        # Create a simplified prompt for character generation
        prompt = f"""
        # Test Genre Character Generation

        Create 3-4 basic characters for a test novel titled "{title}".

        Novel description: {description}

        ## Requirements
        - Create only the essential characters needed for a simple plot
        - Include a protagonist, antagonist, and 1-2 supporting characters
        - Keep character details minimal but sufficient for a coherent story
        - Format as a JSON array of character objects

        ## Character Object Format
        Each character should have these fields:
        - name: Character's name
        - role: "Protagonist", "Antagonist", or "Supporting"
        - appearance: Brief physical description (1-2 sentences)
        - personality: 2-3 key personality traits
        - background: Brief character background
        - goals: Simple character goal or motivation
        - arc: Basic character development arc

        Return only the JSON array of characters.
        """

        # Generate with reduced token count
        response = self.gemini.generate_content(prompt, temperature=0.7, max_tokens=4000)

        # Try to parse the response as JSON
        try:
            # Find JSON content in the response
            start_idx = response.find('[')
            end_idx = response.rfind(']') + 1

            if start_idx >= 0 and end_idx > start_idx:
                json_str = response[start_idx:end_idx]
                characters = json.loads(json_str)

                # Ensure each character has the required fields
                required_fields = ["name", "role", "appearance", "personality", "background", "goals", "arc"]
                for char in characters:
                    # Add default values for any missing fields
                    for field in required_fields:
                        if field not in char:
                            char[field] = f"Not specified ({field.replace('_', ' ')})"

                    # Add POV designation for protagonist
                    if char.get("role") == "Protagonist":
                        char["pov_character"] = True

                return characters
            else:
                # Fallback to basic characters if JSON parsing fails
                return self._fallback_test_characters()

        except (json.JSONDecodeError, Exception):
            # Fallback to basic characters if JSON parsing fails
            return self._fallback_test_characters()

    def _fallback_test_characters(self) -> List[Dict[str, Any]]:
        """
        Create fallback characters for Test genre if generation fails.

        Returns:
            List of basic character dictionaries
        """
        # Create basic characters
        return [
            {
                "name": "Alex Morgan",
                "role": "Protagonist",
                "appearance": "A determined individual in their early 30s with an analytical mind.",
                "personality": "Logical, persistent, and adaptable",
                "background": "Grew up in a small town with a passion for solving problems.",
                "goals": "To overcome the central challenge of the story",
                "arc": "Learning to balance logic with emotion",
                "pov_character": True
            },
            {
                "name": "Jordan Blake",
                "role": "Antagonist",
                "appearance": "A calculating person with sharp features and intense eyes.",
                "personality": "Ambitious, strategic, and ruthless",
                "background": "Rose to power through questionable means and connections.",
                "goals": "To achieve their aims at any cost",
                "arc": "Refusing to change despite opportunities for redemption"
            },
            {
                "name": "Taylor Reed",
                "role": "Supporting",
                "appearance": "A loyal friend to the protagonist with a warm smile.",
                "personality": "Supportive, insightful, and practical",
                "background": "Long-time friend who shares history with the protagonist.",
                "goals": "To help the protagonist succeed",
                "arc": "Finding their own strength through supporting others"
            }
        ]

    def generate_chapter(self, chapter_num: int) -> str:
        """
        Generate a single chapter of the novel.

        Args:
            chapter_num: Chapter number to generate

        Returns:
            Generated chapter text
        """
        if not self.memory_manager:
            raise ValueError("Novel not initialized. Call initialize_novel first.")

        # Get context for this chapter
        context = self.memory_manager.get_context_for_chapter(chapter_num)

        # Determine chapter title
        chapter_title = f"Chapter {chapter_num}"
        if chapter_num <= len(self.memory_manager.structure["outline"]):
            outline_entry = self.memory_manager.structure["outline"][chapter_num - 1]
            if " - " in outline_entry:
                chapter_title = outline_entry.split(" - ")[0]
            else:
                chapter_title = outline_entry

        # Get genre-specific minimum word count
        genre = self.memory_manager.metadata['genre']
        min_chapter_length = 3500  # Default minimum

        # Use generation options if available
        if self.generation_options and 'min_chapter_length' in self.generation_options:
            min_chapter_length = self.generation_options['min_chapter_length']
        else:
            # Try to get from genre guidelines
            try:
                from src.utils.chapter_planner import get_genre_guidelines
                guidelines = get_genre_guidelines(genre)
                min_chapter_length = guidelines["chapter_length"][0]  # Use the lower bound
            except (ImportError, KeyError, Exception):
                # Fallback to default if there's any issue
                pass

        # Create a prompt for chapter generation
        prompt = self._create_chapter_prompt(chapter_num, chapter_title, context)

        # No need to add additional word count requirements here
        # They are now included directly in the _create_chapter_prompt method

        # Generate the chapter with increased max_tokens for longer chapters
        # Use appropriate max_tokens based on genre and minimum chapter length
        if genre.lower() == "test":
            chapter_text = self.gemini.generate_content(prompt, temperature=0.7, max_tokens=24000)
        else:
            # Calculate max_tokens based on minimum chapter length
            # Use a multiplier to ensure we have enough tokens (approx 4 tokens per word + buffer)
            max_tokens = max(20000, min_chapter_length * 5)
            chapter_text = self.gemini.generate_content(prompt, temperature=0.8, max_tokens=max_tokens)

        # Clean up the response
        chapter_text = self.gemini.clean_response(chapter_text)

        # Count words
        word_count = count_words(chapter_text)

        # Check if we need to extend the chapter to meet minimum word count
        if word_count < min_chapter_length:
            console.print(f"[yellow]Chapter {chapter_num} is only {word_count} words (minimum: {min_chapter_length}). Extending...[/yellow]")

            # Create a prompt to extend the chapter
            # Request more words than actually needed to ensure we meet the minimum
            words_to_request = min_chapter_length - word_count + 500

            extension_prompt = f"""
            The chapter you've written for "{self.memory_manager.metadata['title']}" is currently {word_count} words,
            but we need it to be at least {min_chapter_length} words to meet the requirements for this {genre} novel.

            Please continue the chapter from where it left off, adding approximately {words_to_request} more words.
            It's better to write more than needed rather than too little.

            Maintain the same style, tone, and narrative flow. Develop the scenes further, add more descriptive details,
            expand on character interactions, or introduce a new scene that advances the plot.

            Here's the current end of the chapter:

            {chapter_text[-2000:]}

            Continue from here:
            """

            # Generate the extension
            extension = self.gemini.generate_content(extension_prompt, temperature=0.7, max_tokens=8000)
            extension = self.gemini.clean_response(extension)

            # Combine the original text with the extension
            chapter_text = chapter_text + "\n\n" + extension

            # Recount words
            word_count = count_words(chapter_text)
            console.print(f"[green]Chapter extended to {word_count} words[/green]")

        # Create a summary for memory
        summary_prompt = f"""
        Summarize the following chapter in 2-3 sentences, capturing the key events and developments:

        {chapter_text[:2000]}... [chapter continues]
        """

        summary = self.gemini.generate_content(summary_prompt, temperature=0.5, max_tokens=200)
        summary = self.gemini.clean_response(summary)

        # Add to memory
        self.memory_manager.add_chapter_summary(chapter_num, summary, word_count)

        # Extract narrative elements and update tracking
        narrative_elements = self.memory_manager.extract_narrative_elements(chapter_text, chapter_num, self.gemini)
        self.memory_manager.update_narrative_tracking(chapter_num, narrative_elements)

        return chapter_text

    def _create_chapter_prompt(self, chapter_num: int, chapter_title: str, context: Dict[str, Any]) -> str:
        """
        Create a detailed prompt for chapter generation.

        Args:
            chapter_num: Chapter number
            chapter_title: Chapter title
            context: Context information from memory manager

        Returns:
            Prompt string for Gemini
        """
        # Extract relevant information from context
        metadata = context["metadata"]
        characters = context["characters"]
        previous_chapters = context["previous_chapters"]
        genre = metadata["genre"]

        # Check if this is the Test genre for optimized processing
        if genre.lower() == "test":
            return self._create_test_genre_prompt(chapter_num, chapter_title, context)

        # Create character information
        character_info = ""
        for char in characters:
            name = char.get("name", "")
            role = char.get("role", "")
            traits = char.get("personality_traits", char.get("personality", ""))
            character_info += f"- {name} ({role}): {traits}\n"

        # Create previous chapter summaries
        previous_chapter_info = ""
        for prev_chapter in previous_chapters:
            prev_num = prev_chapter.get("chapter_num", "")
            prev_summary = prev_chapter.get("summary", "")
            previous_chapter_info += f"- Chapter {prev_num}: {prev_summary}\n"

        # Get writing style and POV from generation options
        writing_style = "appropriate for the genre"
        pov = "third person limited"
        pov_character = None

        # Determine if we need to use alternating POV structure
        if self.generation_options:
            writing_style = self.generation_options.get('writing_style', writing_style)
            pov = self.generation_options.get('pov', pov)

            # Check if we're using flexible alternating POVs
            if (pov.lower() == "alternating povs" or
                self.generation_options.get('pov_structure') == "flexible_alternating"):

                # Get POV structure from memory manager
                pov_structure = None
                if hasattr(self.memory_manager, 'narrative_tracking'):
                    pov_structure = self.memory_manager.narrative_tracking.get("pov_structure")

                if pov_structure:
                    # Use the new flexible POV assignment
                    chapter_outline_text = chapter_outline if isinstance(chapter_outline, str) else ""
                    pov_character = assign_chapter_pov(
                        chapter_num=chapter_num,
                        pov_structure=pov_structure,
                        chapter_outline=chapter_outline_text,
                        story_context=context
                    )
                else:
                    # Fallback to old system if POV structure not available
                    pov_characters = []
                    for char in characters:
                        if char.get("pov_character") is True or char.get("pov_character") == "true":
                            pov_characters.append(char)

                    # Sort by POV order if available
                    pov_characters.sort(key=lambda x: x.get("pov_order", 999))

                    # Determine which character's POV to use for this chapter
                    if pov_characters:
                        if len(pov_characters) >= 2:
                            # Flexible alternating based on gender balance
                            male_chars = [c for c in pov_characters if c.get("gender") == "male"]
                            female_chars = [c for c in pov_characters if c.get("gender") == "female"]

                            if male_chars and female_chars:
                                # Alternate with flexibility for story needs
                                if chapter_num % 2 == 1:
                                    pov_character = male_chars[0]
                                else:
                                    pov_character = female_chars[0]
                            else:
                                # Simple alternating if no gender balance
                                pov_index = (chapter_num - 1) % len(pov_characters)
                                pov_character = pov_characters[pov_index]
                        else:
                            # If only one POV character, use that one
                            pov_character = pov_characters[0]

        # Calculate target chapter length
        target_chapter_length = "3,500-4,500"  # Default target range
        min_chapter_length = 3500  # Default minimum words per chapter

        if self.generation_options:
            if 'chapter_length' in self.generation_options:
                chapter_length = self.generation_options['chapter_length']
                target_chapter_length = f"{chapter_length-500:,}-{chapter_length+500:,}"

            if 'min_chapter_length' in self.generation_options:
                min_chapter_length = self.generation_options['min_chapter_length']

        # Get narrative context if available
        narrative_context = context.get("narrative_context", {})

        # Determine POV character from narrative context
        narrative_pov = narrative_context.get("pov_character")
        if narrative_pov:
            pov_character = None
            # Find the character object for the POV character
            for char in characters:
                if char.get("name") == narrative_pov:
                    pov_character = char
                    break

        # Create POV-specific instructions
        pov_instructions = ""
        if pov_character:
            pov_name = pov_character.get("name", "the main character")
            pov_instructions = f"""
            IMPORTANT: This chapter should be written from {pov_name}'s point of view ONLY.
            - Show the story through {pov_name}'s eyes, thoughts, and feelings
            - Use "{pov}" perspective but limited to {pov_name}'s experiences and observations
            - Do not show the internal thoughts of other characters
            - Maintain deep immersion in {pov_name}'s perspective throughout the chapter
            """

            # Update the POV setting to be character-specific
            pov = f"{pov} (from {pov_name}'s perspective)"

        # Get character emotions and knowledge from narrative context
        character_emotions = narrative_context.get("character_emotions", {})
        character_knowledge = narrative_context.get("character_knowledge", {})
        character_locations = narrative_context.get("character_locations", {})

        # Create character state information
        character_state_info = ""
        for char_name, emotions in character_emotions.items():
            character_state_info += f"- {char_name}'s emotional state: {emotions}\n"

        for char_name, knowledge in character_knowledge.items():
            character_state_info += f"- {char_name} knows: {knowledge}\n"

        for char_name, location in character_locations.items():
            character_state_info += f"- {char_name}'s current location: {location}\n"

        # Get relationship information
        relationships = narrative_context.get("relationships", {})
        relationship_info = ""
        for rel_key, status in relationships.items():
            relationship_info += f"- Relationship between {rel_key}: {status}\n"

        # Get plot thread information
        plot_threads = narrative_context.get("plot_threads", {})
        plot_thread_info = ""
        for thread_name, status in plot_threads.items():
            plot_thread_info += f"- Plot thread '{thread_name}': {status}\n"

        # Get unresolved questions
        unresolved_questions = narrative_context.get("unresolved_questions", [])
        unresolved_info = ""
        for question in unresolved_questions:
            unresolved_info += f"- Unresolved question: {question}\n"

        # Get continuity elements
        continuity = narrative_context.get("continuity", {})
        continuity_info = ""
        for element, details in continuity.items():
            continuity_info += f"- Continuity element '{element}': {details}\n"

        # Get time and weather
        time_of_day = narrative_context.get("time_of_day")
        weather = narrative_context.get("weather")
        setting_info = ""
        if time_of_day:
            setting_info += f"- Current time of day: {time_of_day}\n"
        if weather:
            setting_info += f"- Current weather conditions: {weather}\n"

        # Get themes and symbols
        themes = narrative_context.get("themes", {})
        symbols = narrative_context.get("symbols", {})
        thematic_info = ""
        for theme, occurrences in themes.items():
            thematic_info += f"- Theme '{theme}': Continue developing this theme\n"
        for symbol, occurrences in symbols.items():
            thematic_info += f"- Symbol '{symbol}': Consider using this symbol again\n"

        # Check if this is part of a series
        series_info = ""
        if "series_context" in context and context["series_context"]:
            series_context = context["series_context"]
            series_metadata = series_context.get("metadata", {})
            series_title = series_metadata.get("title", "")
            book_number = metadata["series"]["book_number"]

            # Add series information
            series_info = f"""
            # Series Information
            This book is part of the "{series_title}" series (Book {book_number}).
            """

            # Add recurring characters if available
            if "recurring_characters" in context:
                recurring_chars = context["recurring_characters"]
                if recurring_chars:
                    series_info += "\n## Recurring Characters from Previous Books\n"
                    for char in recurring_chars:
                        char_name = char.get("name", "")
                        char_desc = char.get("description", "")
                        series_info += f"- {char_name}: {char_desc}\n"

            # Add series arcs if available
            if "series_arcs" in context and context["series_arcs"]:
                series_arcs = context["series_arcs"]
                series_info += "\n## Series Plot Arcs\n"
                for arc in series_arcs:
                    arc_name = arc.get("name", "")
                    arc_status = arc.get("status", "")
                    series_info += f"- {arc_name}: {arc_status}\n"

            # Add universe information if available
            if "universe" in context and context["universe"]:
                universe = context["universe"]
                if "world_building" in universe and universe["world_building"]:
                    series_info += "\n## World Building Elements\n"
                    for element, details in universe["world_building"].items():
                        series_info += f"- {element}: {details}\n"

        # Create the prompt
        prompt = f"""
        You are writing Chapter {chapter_num}: "{chapter_title}" of a {metadata['genre']} novel titled "{metadata['title']}"
        for {metadata['target_audience']} audience.

        Novel description: {metadata['description']}

        Key characters:
        {character_info}

        Previous chapters:
        {previous_chapter_info}

        Writing style: {writing_style}
        Point of view: {pov}
        {pov_instructions}

        {series_info}

        # Current Narrative State
        """

        # Add narrative context sections if they have content
        if character_state_info:
            prompt += f"""
        ## Character States
        {character_state_info}
        """

        if relationship_info:
            prompt += f"""
        ## Relationships
        {relationship_info}
        """

        if plot_thread_info:
            prompt += f"""
        ## Active Plot Threads
        {plot_thread_info}
        """

        if unresolved_info:
            prompt += f"""
        ## Unresolved Questions
        {unresolved_info}
        """

        if setting_info:
            prompt += f"""
        ## Current Setting
        {setting_info}
        """

        if thematic_info:
            prompt += f"""
        ## Themes and Symbols
        {thematic_info}
        """

        if continuity_info:
            prompt += f"""
        ## Continuity Elements
        {continuity_info}
        """

        # Add guidelines
        prompt += f"""
        # Guidelines for this chapter:
        1. Write in the specified style and point of view
        2. Maintain consistent character voices and personalities
        3. Advance the plot while developing characters
        4. Show, don't tell - demonstrate emotions through actions and dialogue
        5. Include balanced dialogue, description, and action
        6. End with a hook that leads to the next chapter
        7. Aim for approximately {target_chapter_length} words
        8. IMPORTANT: The chapter MUST be at least {min_chapter_length} words long - shorter chapters will not be accepted
        9. Maintain narrative consistency with the Current Narrative State information provided
        10. Address or develop at least one unresolved question if any are listed

        # IMPORTANT WRITING QUALITY GUIDELINES:
        1. AVOID REPETITIVE INTERNAL MONOLOGUES - vary the character's thoughts and emotional responses
        2. Use specific, vivid details for settings and cultural elements - avoid generic placeholders
        3. Vary sentence structure and paragraph length for better pacing
        4. Integrate subplot elements naturally into the main narrative
        5. Ensure thematic elements are woven subtly into the narrative
        6. Limit melodramatic prose - use restraint with emotional descriptions
        7. Develop secondary characters with clear motivations and distinct personalities
        8. Use concrete cultural and setting details that feel authentic to the world
        9. Maintain consistent character voices based on their established personalities
        10. Foreshadow future developments without being heavy-handed

        Write the complete chapter, including the chapter title. Format the chapter with proper paragraphs,
        dialogue formatting, and scene breaks where appropriate.

        IMPORTANT WORD COUNT REQUIREMENTS:
        - Your chapter MUST be at least {min_chapter_length} words long
        - Do not stop writing until you have reached at least {min_chapter_length} words
        - Include detailed descriptions and fully developed scenes
        - A typical scene is 800-1,200 words
        - Include enough scenes to reach the minimum word count
        - Do not summarize or rush the narrative

        Your entire response should be at least {min_chapter_length} words.
        """

        return prompt



    def _create_test_genre_prompt(self, chapter_num: int, chapter_title: str, context: Dict[str, Any]) -> str:
        """
        Create a simplified prompt for Test genre chapter generation.

        Args:
            chapter_num: Chapter number
            chapter_title: Chapter title
            context: Context information from memory manager

        Returns:
            Simplified prompt string for Gemini
        """
        metadata = context["metadata"]
        characters = context["characters"]
        previous_chapters = context["previous_chapters"]

        # Create simplified character information (just names and roles)
        character_info = ""
        for i, char in enumerate(characters[:3]):  # Limit to top 3 characters for test genre
            name = char.get("name", f"Character {i+1}")
            role = char.get("role", "Supporting character")
            character_info += f"- {name} ({role})\n"

        # Get only the most recent previous chapter summary
        previous_chapter_info = ""
        if previous_chapters and len(previous_chapters) > 0:
            prev_chapter = previous_chapters[-1]
            prev_num = prev_chapter.get("chapter_num", "")
            prev_summary = prev_chapter.get("summary", "")
            previous_chapter_info = f"Chapter {prev_num}: {prev_summary}"

        # Create a simplified prompt for test genre with emphasis on word count
        prompt = f"""
        # Test Genre Chapter Generation

        Write Chapter {chapter_num}: "{chapter_title}" for a test novel titled "{metadata['title']}".

        ## Key Information
        - Genre: Test (simplified structure for testing)
        - REQUIRED WORD COUNT: MINIMUM 3,500 WORDS (this is critical)
        - Style: Clear, straightforward prose with minimal complexity
        - POV: Third person limited

        ## Characters
        {character_info}

        ## Previous Chapter Summary
        {previous_chapter_info}

        ## Chapter Requirements
        - This chapter should advance the plot in a straightforward manner
        - Include at least one scene with dialogue
        - Maintain consistent POV throughout
        - IMPORTANT: Your response MUST be at least 3,500 words in length
        - Do not stop writing until you have reached at least 3,500 words
        - Include detailed descriptions and fully developed scenes

        ## Word Count Guidance
        - A typical scene is 800-1,200 words
        - Include 3-4 scenes in this chapter
        - Add descriptive details to reach the minimum word count
        - Do not summarize or rush the narrative

        Write the complete chapter now. Your entire response should be at least 3,500 words.
        """

        return prompt

    def enhance_chapter(self, chapter_text: str, chapter_num: int, chapter_title: str) -> str:
        """
        Enhance a generated chapter with improved style and humanization.

        Args:
            chapter_text: The original generated chapter text
            chapter_num: The chapter number
            chapter_title: The chapter title

        Returns:
            Enhanced chapter text
        """
        if not self.memory_manager:
            raise ValueError("Novel not initialized. Call initialize_novel first.")

        # Get context for enhancement
        context = self.memory_manager.get_context_for_chapter(chapter_num)

        # Check if this is the Test genre - if so, do minimal enhancement to save time
        genre = self.memory_manager.metadata['genre']
        if genre.lower() == "test":
            console.print("[yellow]Test genre detected - performing minimal enhancement to save time[/yellow]")
            # For test genre, just do basic formatting and return
            return self._minimal_test_enhancement(chapter_text, chapter_num, chapter_title)

        # Get previous chapter summary
        previous_chapter_info = ""
        for prev_chapter in context["previous_chapters"]:
            prev_num = prev_chapter.get("chapter_num", "")
            prev_summary = prev_chapter.get("summary", "")
            if prev_num == chapter_num - 1:
                previous_chapter_info = prev_summary
                break

        # Determine POV character
        pov_character = None
        if self.generation_options and (
            self.generation_options.get('pov', "").lower() == "alternating povs" or
            self.generation_options.get('pov_structure') == "alternating"
        ):
            pov_characters = []
            for char in context["characters"]:
                if char.get("pov_character") is True or char.get("pov_character") == "true":
                    pov_characters.append(char)

            # Sort by POV order if available
            pov_characters.sort(key=lambda x: x.get("pov_order", 999))

            # Determine which character's POV to use for this chapter
            if pov_characters:
                if len(pov_characters) >= 2:
                    # Odd chapters use first POV character, even chapters use second
                    pov_index = 0 if chapter_num % 2 == 1 else 1
                    pov_character = pov_characters[pov_index]
                else:
                    # If only one POV character, use that one
                    pov_character = pov_characters[0]

        # Get character voice information
        character_voices = ""
        for char in context["characters"]:
            if "voice" in char and char["voice"]:
                character_voices += f"{char['name']}: {char['voice']}\n"

        # Create enhancement prompt with focus on addressing common flaws
        enhancement_prompt = f"""
        # Content Enhancement Request for Novel Chapter

        ## Current Chapter Context
        Chapter {chapter_num}: "{chapter_title}"
        Previous chapter summary: {previous_chapter_info}
        POV Character: {pov_character.get('name') if pov_character else 'Third person limited'}

        ## CRITICAL IMPROVEMENT AREAS

        ### Prose Quality Improvements
        - REDUCE VERBOSE AND MELODRAMATIC PROSE - use concise, impactful language instead of flowery excess
        - Avoid long, convoluted sentences that slow pacing - aim for clarity and impact
        - Eliminate redundant descriptions and unnecessary adverbs
        - Replace generic metaphors with fresh, specific imagery relevant to the story world
        - Vary paragraph length for better pacing - use short paragraphs for emphasis

        ### Internal Monologue Improvements
        - REDUCE REPETITIVE INTERNAL MONOLOGUES - vary the character's thoughts and emotional responses
        - Limit internal monologues to key moments of character development
        - Show emotions through physical reactions and dialogue instead of explicit thought
        - Ensure each internal thought adds new information or perspective
        - Avoid repeating the same emotional beats multiple times

        ### Setting and Cultural Detail Improvements
        - REPLACE GENERIC CULTURAL AND SETTING DETAILS with vivid, specific elements
        - Add authentic sensory details that ground scenes in the specific location
        - Include cultural nuances that feel researched and authentic
        - Create a sense of place through specific environmental details
        - Ensure setting descriptions serve the story and mood

        ### Character Voice Improvements
        - Ensure each character has a DISTINCT VOICE based on their background and personality
        - Use the following character voice guidelines:
        {character_voices}
        - Develop secondary characters with clear motivations and personalities
        - Show character relationships through meaningful interactions

        ### Subplot Integration Improvements
        - Weave subplot elements naturally into the main narrative
        - Ensure thematic consistency throughout the chapter
        - Connect character moments to larger themes
        - Balance multiple narrative threads without losing focus

        ## Additional Enhancement Instructions

        ### Author Style Emulation
        - Vary sentence length with a mix of short, punchy sentences and longer, flowing ones
        - Use distinctive transitional phrases that feel natural and authentic
        - Balance dialogue-to-narration ratio appropriate for {context['metadata']['genre']}
        - Employ varied dialogue tags beyond "said" and "asked"
        - Integrate sensory details across all five senses

        ### Narrative Enhancement
        - Improve pacing by creating clear tension-and-release patterns
        - Enhance scene transitions to flow naturally between settings and time periods
        - Add meaningful subtext to dialogue exchanges
        - Incorporate subtle foreshadowing that connects to future plot points
        - Balance exposition with action and dialogue

        ### Humanization Elements
        - Add small imperfections in dialogue (occasional interruptions, realistic hesitations)
        - Include subtle character quirks and habits that feel authentic
        - Incorporate moments of unexpected emotion or humor
        - Add small sensory details that ground the scene in reality
        - Include brief moments of introspection that reveal character depth
        - Ensure characters react authentically to events based on their established personalities

        ### Technical Requirements
        - Maintain approximately 3000-4000 words
        - Ensure POV consistency from {pov_character.get('name') if pov_character else 'the main character'}'s perspective only
        - Balance paragraph lengths for readability
        - Use appropriate scene breaks where needed
        - Maintain consistent tense throughout

        ## Original Chapter Text
        {chapter_text}

        ## Output Format
        Please provide the enhanced chapter as a complete text, maintaining the original chapter title and number. Include any scene breaks with appropriate formatting.
        """



        # Send to Gemini for enhancement
        console.print("[bold cyan]Enhancing chapter with improved style and humanization...[/bold cyan]")
        enhanced_text = self.gemini.generate_content(enhancement_prompt, temperature=0.7, max_tokens=16000)
        enhanced_text = self.gemini.clean_response(enhanced_text)

        return enhanced_text

    def _minimal_test_enhancement(self, chapter_text: str, chapter_num: int, chapter_title: str) -> str:
        """
        Perform minimal enhancement for Test genre chapters to save time.

        Args:
            chapter_text: The original generated chapter text
            chapter_num: The chapter number
            chapter_title: The chapter title

        Returns:
            Minimally enhanced chapter text
        """
        # Create a simplified enhancement prompt
        minimal_prompt = f"""
        # Minimal Enhancement for Test Genre

        Perform basic enhancement on Chapter {chapter_num}: "{chapter_title}" for testing purposes.

        ## Enhancement Instructions
        - Fix any obvious grammar or spelling errors
        - Ensure paragraph breaks are appropriate
        - Make sure dialogue formatting is correct
        - Do NOT add significant new content
        - Do NOT change the plot or characters
        - Keep the enhancement minimal to save processing time

        ## Original Text
        {chapter_text}

        ## Output Format
        Return the enhanced text only, with no additional comments or explanations.
        """

        # Use reduced token count for faster processing
        console.print("[yellow]Performing minimal enhancement for Test genre...[/yellow]")
        enhanced_text = self.gemini.generate_content(minimal_prompt, temperature=0.5, max_tokens=8000)
        enhanced_text = self.gemini.clean_response(enhanced_text)

        return enhanced_text

    def generate_complete_novel(self) -> Dict[str, Any]:
        """
        Generate a complete novel from start to finish.

        Returns:
            Dictionary containing the complete novel information
        """
        if not self.memory_manager:
            raise ValueError("Novel not initialized. Call initialize_novel first.")

        # Check API connection before starting the generation process
        console.print("[bold cyan]Checking API connection...[/bold cyan]")
        api_status = self.gemini.check_api_connection(check_all_keys=True)

        if not api_status["success"]:
            raise ConnectionError("Unable to connect to the Gemini API. Please check your internet connection and API keys.")

        # Display API key information
        console.print(f"[bold green]✓[/bold green] API connection successful!")
        console.print(f"[bold cyan]Active API keys:[/bold cyan] {api_status['active_keys']}")
        console.print(f"[bold cyan]Working API keys:[/bold cyan] {api_status['working_keys']}")

        # If we have multiple keys, show that we're using key rotation
        if api_status['active_keys'] > 1:
            console.print("[bold green]Multiple API keys detected - will automatically rotate keys if rate limits are encountered.[/bold green]")

        console.print("[bold green]Generating writer profile...[/bold green]")
        writer_profile = self.generate_writer_profile()

        console.print("[bold green]Generating novel outline...[/bold green]")
        chapter_outlines, chapter_count = self.generate_novel_outline(writer_profile)

        console.print("[bold green]Generating characters...[/bold green]")
        characters = self.generate_characters()

        # Generate chapters
        chapters = []

        # Process one chapter at a time (generate, enhance, then move to next)
        console.print("[bold green]Generating and enhancing chapters sequentially...[/bold green]")
        with Progress() as progress:
            task = progress.add_task("[cyan]Processing chapters...", total=chapter_count)



            for chapter_num in range(1, chapter_count + 1):
                # Get chapter title
                chapter_title = f"Chapter {chapter_num}"
                if chapter_num <= len(chapter_outlines):
                    outline = chapter_outlines[chapter_num - 1]
                    if " - " in outline:
                        chapter_title = outline.split(" - ")[0]
                    else:
                        chapter_title = outline

                # Generate current chapter
                console.print(f"[bold blue]Generating Chapter {chapter_num}: {chapter_title}...[/bold blue]")
                current_chapter_text = self.generate_chapter(chapter_num)

                # Enhance the current chapter
                console.print(f"[bold blue]Enhancing Chapter {chapter_num}: {chapter_title}...[/bold blue]")
                enhanced_text = self.enhance_chapter(
                    current_chapter_text,
                    chapter_num,
                    chapter_title
                )

                # Add enhanced chapter to list
                chapters.append({
                    "number": chapter_num,
                    "title": chapter_title,
                    "content": enhanced_text
                })

                # Update progress
                progress.update(task, advance=1)

                console.print(f"[bold green]✓[/bold green] Chapter {chapter_num} completed")

        # Display final word count information
        current_word_count = self.memory_manager.structure["current_word_count"]
        target_word_count = self.memory_manager.structure["target_word_count"]

        console.print(f"[bold green]✓[/bold green] Final word count: {current_word_count} words (Target: {target_word_count} words)")

        # Compile novel information
        novel = {
            "metadata": self.memory_manager.metadata,
            "writer_profile": writer_profile,
            "outline": chapter_outlines,
            "characters": characters,
            "chapters": chapters,
            "word_count": self.memory_manager.structure["current_word_count"]
        }

        return novel
