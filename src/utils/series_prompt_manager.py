"""
Series prompt management system.
Coordinates between series continuity tracking and prompt generation for enhanced series coherence.
"""

from typing import Dict, List, Any
from src.utils.series_continuity import SeriesContinuityManager
from src.prompts import get_prompt


class SeriesPromptManager:
    """
    Manages prompt generation for series with continuity awareness.
    Enhances prompts with series context and continuity information.
    """

    def __init__(self, continuity_manager: SeriesContinuityManager):
        """
        Initialize the series prompt manager.

        Args:
            continuity_manager: SeriesContinuityManager instance
        """
        self.continuity_manager = continuity_manager

    def get_enhanced_series_plan_prompt(self, genre: str, series_title: str,
                                      series_description: str, planned_books: int,
                                      target_audience: str, **kwargs) -> str:
        """
        Get an enhanced series planning prompt with continuity considerations.

        Args:
            genre: Genre of the series
            series_title: Title of the series
            series_description: Description of the series
            planned_books: Number of planned books
            target_audience: Target audience
            **kwargs: Additional prompt parameters

        Returns:
            Enhanced series planning prompt
        """
        # Get base genre-specific prompt
        base_prompt = get_prompt(
            genre=genre,
            prompt_type="series_plan",
            series_title=series_title,
            series_description=series_description,
            planned_books=planned_books,
            target_audience=target_audience,
            **kwargs
        )

        if not base_prompt:
            return ""

        # Add series continuity enhancements
        continuity_enhancements = f"""

## Series Continuity Planning Requirements

### Character Development Across {planned_books} Books
- Plan character arcs that span multiple books with clear progression stages
- Design character relationships that evolve meaningfully over time
- Create character knowledge and abilities that build logically across books
- Ensure character consistency while allowing for realistic growth and change

### Plot Thread Management
- Design overarching plot threads that span the entire series
- Create subplot threads that resolve within individual books or across multiple books
- Plan plot thread intersections and how they influence each other
- Ensure each book advances major plot threads while telling a complete story

### World-Building Continuity
- Establish world rules, geography, and cultures that remain consistent
- Plan how the world evolves and changes in response to series events
- Design world elements that can be explored in depth across multiple books
- Create a timeline that maintains chronological consistency

### Series Coherence Elements
- Plan recurring themes that develop and deepen across books
- Design series-specific terminology and concepts that build over time
- Create callbacks and references that reward series readers
- Ensure each book can stand alone while contributing to the series narrative

### Continuity Tracking Considerations
- Identify key characters whose development should be tracked across books
- Define major plot threads that need continuity management
- Establish world elements that require consistency tracking
- Plan timeline events and character aging across the series

When creating the series plan, consider how each element will be tracked and maintained across all {planned_books} books to ensure series coherence and reader satisfaction.
"""

        return base_prompt + continuity_enhancements

    def get_enhanced_series_book_prompt(self, genre: str, book_number: int,
                                      book_title: str, series_title: str,
                                      previous_books: List[Dict], **kwargs) -> str:
        """
        Get an enhanced individual book prompt with series continuity context.

        Args:
            genre: Genre of the series
            book_number: Number of the current book
            book_title: Title of the current book
            series_title: Title of the series
            previous_books: List of previous books in the series
            **kwargs: Additional prompt parameters

        Returns:
            Enhanced book generation prompt with continuity context
        """
        # Get base genre-specific prompt
        base_prompt = get_prompt(
            genre=genre,
            prompt_type="series_book",
            book_number=book_number,
            book_title=book_title,
            series_title=series_title,
            previous_books=previous_books,
            **kwargs
        )

        if not base_prompt:
            return ""

        # Get continuity summary for this book
        continuity_summary = self.continuity_manager.get_continuity_summary(book_number)

        # Build continuity context
        continuity_context = self._build_continuity_context(continuity_summary, book_number)

        # Add enhanced continuity requirements
        continuity_enhancements = f"""

## Series Continuity Context for Book {book_number}

{continuity_context}

## Continuity Requirements for This Book

### Character Continuity Obligations
- Maintain established character personalities, relationships, and knowledge
- Show realistic character development from previous books
- Respect character abilities and limitations established in earlier books
- Continue character arcs in meaningful ways that build on previous development

### Plot Thread Continuity
- Address or advance active plot threads from previous books
- Introduce new plot elements that fit logically with established narrative
- Show consequences of events from previous books
- Maintain consistency with established plot rules and limitations

### World Continuity Standards
- Use established world elements accurately and consistently
- Maintain geographic, cultural, and technological consistency
- Show realistic world changes resulting from previous book events
- Respect established world rules (magic systems, technology, social structures)

### Timeline and Chronology
- Maintain accurate timeline progression from previous books
- Show appropriate character aging and world changes
- Reference past events accurately and meaningfully
- Ensure chronological consistency with established series timeline

### Reader Experience Considerations
- Provide enough context for new readers while rewarding series readers
- Include meaningful callbacks to previous books without over-explaining
- Advance the series narrative while telling a complete individual story
- Create anticipation for future books while providing satisfaction for this book

Use this continuity information to ensure Book {book_number} feels like an authentic continuation of the {series_title} series while telling a compelling standalone story.
"""

        return base_prompt + continuity_enhancements

    def _build_continuity_context(self, continuity_summary: Dict[str, Any],
                                book_number: int) -> str:
        """
        Build a formatted continuity context string from the summary.

        Args:
            continuity_summary: Continuity summary from SeriesContinuityManager
            book_number: Current book number

        Returns:
            Formatted continuity context string
        """
        context_parts = []

        # Active characters
        if continuity_summary.get('active_characters'):
            context_parts.append("### Established Characters")
            for name, char_data in continuity_summary['active_characters'].items():
                status = char_data.get('current_status', 'unknown')
                location = char_data.get('location', 'unknown')
                arc_stage = char_data.get('character_arc_stage', 'unknown')
                context_parts.append(f"- **{name}**: Status: {status}, Location: {location}, Arc Stage: {arc_stage}")

                # Add relationships if any
                relationships = char_data.get('relationships', {})
                if relationships:
                    rel_list = [f"{other}: {rel_type}" for other, rel_type in relationships.items()]
                    context_parts.append(f"  - Relationships: {', '.join(rel_list)}")

                # Add knowledge if any
                knowledge = char_data.get('knowledge', [])
                if knowledge:
                    context_parts.append(f"  - Key Knowledge: {', '.join(knowledge[-3:])}")  # Last 3 items

        # Active plot threads
        if continuity_summary.get('active_plot_threads'):
            context_parts.append("\n### Active Plot Threads")
            for thread_id, thread_data in continuity_summary['active_plot_threads'].items():
                name = thread_data.get('name', thread_id)
                description = thread_data.get('description', 'No description')
                importance = thread_data.get('importance_level', 'unknown')
                introduced_book = thread_data.get('introduced_book', 'unknown')
                context_parts.append(f"- **{name}** (Book {introduced_book}, {importance}): {description}")

                # Add connected characters if any
                connected_chars = thread_data.get('connected_characters', [])
                if connected_chars:
                    context_parts.append(f"  - Connected Characters: {', '.join(connected_chars)}")

        # Established world elements
        if continuity_summary.get('established_world_elements'):
            context_parts.append("\n### Established World Elements")
            for element_id, element_data in continuity_summary['established_world_elements'].items():
                name = element_data.get('name', element_id)
                element_type = element_data.get('type', 'unknown')
                description = element_data.get('description', 'No description')
                introduced_book = element_data.get('first_introduced_book', 'unknown')
                context_parts.append(f"- **{name}** ({element_type}, Book {introduced_book}): {description}")

        # Timeline events
        if continuity_summary.get('timeline_events'):
            context_parts.append("\n### Previous Timeline Events")
            recent_events = continuity_summary['timeline_events'][-5:]  # Last 5 events
            for event in recent_events:
                book_num = event.get('book_number', 'unknown')
                event_desc = event.get('event', 'Unknown event')
                context_parts.append(f"- Book {book_num}: {event_desc}")

        return '\n'.join(context_parts) if context_parts else "No previous continuity elements established."

    def update_continuity_from_book(self, book_data: Dict[str, Any],
                                  book_number: int) -> None:
        """
        Update continuity tracking based on a completed book.

        Args:
            book_data: Data from the completed book
            book_number: Number of the completed book
        """
        try:
            # Extract and update character information
            if 'characters' in book_data:
                for character in book_data['characters']:
                    char_name = character.get('name', '')
                    if char_name:
                        # Add or update character
                        char_state = self.continuity_manager.add_character(
                            name=char_name,
                            status='alive',  # Default, could be extracted from character data
                            location=character.get('location', 'unknown'),
                            book_introduced=book_number
                        )

                        # Update character details with proper error handling
                        if 'personality' in character:
                            char_state.personality_changes.append(f"Book {book_number}: {character['personality']}")

                        if 'abilities' in character:
                            abilities = character.get('abilities', [])
                            # Handle both string and list formats
                            if isinstance(abilities, str):
                                # If abilities is a string, split it or treat as single ability
                                abilities = [abilities] if abilities.strip() else []
                            elif isinstance(abilities, list):
                                # Ensure all items are strings
                                abilities = [str(ability) for ability in abilities if ability]
                            else:
                                abilities = []
                            char_state.abilities.extend(abilities)

                        if 'relationships' in character:
                            relationships_data = character.get('relationships', {})
                            # Handle different relationship data formats
                            if isinstance(relationships_data, dict):
                                # Already in correct format
                                char_state.relationships.update(relationships_data)
                            elif isinstance(relationships_data, str):
                                # Convert string description to structured format
                                # For now, store as a general relationship note
                                if relationships_data.strip():
                                    char_state.relationships[f"general_book_{book_number}"] = relationships_data.strip()
                            elif isinstance(relationships_data, list):
                                # Handle list of relationship descriptions
                                for i, rel in enumerate(relationships_data):
                                    if isinstance(rel, str) and rel.strip():
                                        char_state.relationships[f"relationship_{i}_book_{book_number}"] = rel.strip()
                                    elif isinstance(rel, dict):
                                        char_state.relationships.update(rel)
                            # If relationships_data is None or other type, skip silently

            # Extract plot threads from outline or chapters with error handling
            if 'outline' in book_data:
                outline = book_data['outline']
                if isinstance(outline, dict) and 'subplots' in outline:
                    for i, subplot in enumerate(outline['subplots']):
                        try:
                            thread_id = f"book_{book_number}_subplot_{i}"
                            self.continuity_manager.add_plot_thread(
                                thread_id=thread_id,
                                name=subplot.get('name', f'Subplot {i+1}'),
                                description=subplot.get('description', ''),
                                importance='subplot',
                                book_introduced=book_number
                            )
                        except Exception as subplot_error:
                            # Log subplot processing error but continue
                            print(f"Warning: Failed to process subplot {i} for book {book_number}: {subplot_error}")
                            continue

            # Save updated continuity with error handling
            try:
                self.continuity_manager.save_continuity()
            except Exception as save_error:
                print(f"Warning: Failed to save continuity data for book {book_number}: {save_error}")

        except Exception as e:
            # Log the error but don't crash the generation process
            print(f"Error updating series continuity for book {book_number}: {e}")
            print("Continuing with book generation despite continuity tracking error...")

            # Additional debug information
            if hasattr(e, '__traceback__'):
                import traceback
                print("Debug traceback:")
                traceback.print_exc()

    def get_character_development_prompt_enhancement(self, character_name: str) -> str:
        """
        Get character development enhancement for prompts.

        Args:
            character_name: Name of the character

        Returns:
            Character development prompt enhancement
        """
        char_notes = self.continuity_manager.get_character_development_notes(character_name)

        if not char_notes:
            return ""

        enhancement = f"""

## Character Development Context for {character_name}

### Current Character State
- Arc Stage: {char_notes.get('arc_stage', 'unknown')}
- Recent Changes: {', '.join(char_notes.get('recent_changes', []))}
- Current Relationships: {', '.join([f"{name}: {rel}" for name, rel in char_notes.get('current_relationships', {}).items()])}
- Knowledge: {', '.join(char_notes.get('knowledge_gained', []))}
- Abilities: {', '.join(char_notes.get('abilities', []))}

### Development Suggestions
{chr(10).join(f"- {suggestion}" for suggestion in char_notes.get('suggested_development', []))}

Use this context to ensure {character_name}'s development feels natural and consistent with their established character arc.
"""

        return enhancement
