"""
Short Story Collection genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class ShortStoryCollectionPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Short Story Collection"
    GENRE_DESCRIPTION = "A short story collection is a compilation of multiple short stories, typically sharing a common theme, setting, authorial voice, or exploring related ideas. The individual stories can stand alone, but the collection as a whole creates a larger, more nuanced reading experience. The strength of a collection lies in the diversity of its stories and the connections, both subtle and overt, that bind them together."

    GENRE_CHARACTERISTICS = [
        "Thematic Cohesion: Stories often revolve around a central theme, idea, or motif, creating a unified reading experience.",
        "Varied Perspectives: The collection may explore a single theme from multiple viewpoints or character perspectives.",
        "Standalone Narratives: Each story should be a complete and satisfying narrative in its own right, with a clear beginning, middle, and end.",
        "Interconnectedness (Optional): Stories may feature recurring characters, settings, or plot elements that create a sense of interconnectedness.",
        "Exploration of Nuance: The short story format allows for focused exploration of specific moments, characters, or ideas, often with a sense of ambiguity or open-endedness.",
        "Emphasis on Style and Voice: Short story collections often showcase the author's distinct writing style and narrative voice.",
        "Brevity and Impact: Stories are typically concise and impactful, aiming to create a strong emotional or intellectual response in a limited space.",
        "Experimentation: The collection format allows for experimentation with different narrative structures, styles, and perspectives.",
        "Cumulative Effect: The overall impact of the collection is greater than the sum of its individual stories, creating a richer and more complex reading experience.",
        "Focus on Character or Setting: Some collections prioritize character studies, while others focus on exploring a specific setting or environment."
    ]

    TYPICAL_ELEMENTS = [
        "A unifying theme or concept that ties the stories together.",
        "Diverse characters with unique motivations and backstories.",
        "Vivid settings that contribute to the atmosphere and meaning of the stories.",
        "Compelling plots that explore a range of human experiences.",
        "Strong narrative voice and distinct writing style.",
        "Varying lengths and structures of individual stories.",
        "Recurring motifs or symbols that reinforce the collection's theme.",
        "A well-defined opening story that sets the tone and introduces the collection's themes.",
        "A satisfying concluding story that provides closure or a sense of resolution.",
        "A clear sense of pacing and flow throughout the collection.",
        "A title that reflects the collection's overall theme or focus.",
        "An author's note or introduction that provides context or insight into the collection's creation."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        short_story_collection_additions = '''
## Short Story Collection-Specific Writing Considerations
- **Thematic Resonance**: Consider how each story contributes to the overall theme of the collection. Ensure each piece resonates with the central idea, even if subtly.
- **Voice Consistency**: Maintain a consistent authorial voice throughout the collection, even when writing from different character perspectives. This creates a cohesive reading experience.
- **Pacing and Variety**: Vary the length, tone, and style of the stories to maintain reader engagement. Avoid monotony by alternating between fast-paced and slower-paced narratives.
- **Interconnectedness (Optional)**: If stories are interconnected, carefully plan how characters, settings, or plot elements will reappear and evolve across different narratives.
- **Standalone Strength**: Each story must stand alone as a complete and satisfying narrative. Avoid relying too heavily on prior knowledge from other stories in the collection.
- **Emotional Impact**: Focus on creating a strong emotional impact in each story, even within the constraints of the short story format. Use vivid imagery, compelling characters, and evocative language to engage the reader's emotions.
- **Ordering and Arrangement**: Carefully consider the order in which the stories are presented. The arrangement can significantly impact the reader's overall experience and understanding of the collection's themes.
- **Target Audience**: Define your target audience and tailor the themes, style, and content of the collection to their interests and expectations.
'''
        return base_prompt + short_story_collection_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        short_story_collection_additions = '''
## Short Story Collection-Specific Outline Requirements
- **Overall Theme**: Define the overarching theme or concept that will unify the collection. This should be a clear and concise statement that guides the selection and development of individual stories.
- **Story Ideas**: Brainstorm a list of potential story ideas that relate to the overall theme. Consider different perspectives, settings, and characters that could be explored.
- **Story Summaries**: For each story idea, create a brief summary that outlines the plot, characters, setting, and key themes.
- **Interconnectedness Plan**: If the stories are interconnected, outline how characters, settings, or plot elements will reappear and evolve across different narratives.
- **Ordering and Arrangement**: Plan the order in which the stories will be presented. Consider the pacing, tone, and thematic progression of the collection.
- **Opening Story**: Outline the opening story, ensuring it effectively introduces the collection's themes and sets the tone for the rest of the book.
- **Concluding Story**: Outline the concluding story, ensuring it provides closure or a sense of resolution to the collection's themes.
- **Individual Story Outlines**: For each story, create a detailed outline that includes the following elements:
    - **Exposition**: Introduce the characters, setting, and initial conflict.
    - **Rising Action**: Develop the conflict and build tension.
    - **Climax**: The turning point of the story.
    - **Falling Action**: The consequences of the climax.
    - **Resolution**: The resolution of the conflict.
'''
        return base_prompt + short_story_collection_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character development prompt specifically for short story collections."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")
        target_audience = kwargs.get("target_audience", "Adult")
        subplot_info = kwargs.get("subplot_info", "")

        return f"""
# Short Story Collection Character Development

Create a set of well-developed characters for the short story collection "{title}" for {target_audience}.

## Collection Information
- Title: {title}
- Description: {description}
- Genre: Short Story Collection
- Target Audience: {target_audience}

## Collection Outline
{outline}

{subplot_info}

## Short Story Collection Character Requirements

### Character Development Guidelines
1. **Quick Establishment**: Characters must be quickly established and relatable since short stories have limited space
2. **Focused Traits**: Focus on a few key traits and motivations that drive their actions
3. **Character Diversity**: Ensure diverse characters across the collection representing different backgrounds and perspectives
4. **Recurring Potential**: Some characters may appear in multiple stories, plan their evolution carefully
5. **Distinct Voices**: Each character should have a unique voice and speech pattern
6. **Clear Motivations**: Define each character's goals and what drives them forward
7. **Relatable Flaws**: Give characters vulnerabilities that make them believable and human

### Character Types for Short Story Collections
- **Protagonists**: 2-3 main characters who could anchor different stories
- **Recurring Characters**: 1-2 characters who might appear across multiple stories
- **Supporting Characters**: 3-4 characters who enhance specific stories
- **Diverse Voices**: Characters from different backgrounds, ages, and perspectives

## Character Object Format
For each character, provide the following fields in a JSON object:
- "name": (string) Character's full name
- "role": (string) Their role (protagonist, recurring character, supporting, etc.)
- "appearance": (string) Detailed physical description including distinctive features
- "personality": (string) Key personality traits and characteristics (focus on 2-3 main traits)
- "background": (string) Essential backstory that explains motivations
- "goals": (string) Primary motivations and what they want to achieve
- "arc": (string) Potential character development across stories (if applicable)
- "relationships": (string) How they relate to other characters
- "strengths": (string) Their key abilities or positive traits
- "flaws": (string) Their weaknesses or vulnerabilities
- "voice": (string) Their speech patterns, vocabulary, and communication style
- "story_potential": (string) What types of stories this character could anchor or support

## Short Story Collection Guidelines
- Characters should work well in the compressed format of short stories
- Each character should be memorable and distinctive
- Consider how characters might connect across different stories
- Focus on characters who can carry emotional weight quickly
- Ensure characters represent diverse perspectives and experiences

Return ONLY a valid JSON array of character objects, nothing else.
Example format:
[
  {{
    "name": "Maria Santos",
    "role": "protagonist",
    "appearance": "Mid-thirties with expressive dark eyes and calloused hands from years of gardening",
    "personality": "Resilient and nurturing, but struggles with letting others help her",
    "background": "Single mother who immigrated to start a new life, works multiple jobs",
    "goals": "Wants to provide stability for her daughter while finding her own sense of belonging",
    "arc": "Learns to accept help from her community and trust in relationships",
    "relationships": "Protective of her daughter, slowly building friendships with neighbors",
    "strengths": "Determination, empathy, practical problem-solving",
    "flaws": "Stubborn independence, difficulty trusting others",
    "voice": "Speaks with quiet authority, mixes English with Spanish when emotional",
    "story_potential": "Stories about community, belonging, sacrifice, and finding home"
  }}
]
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        short_story_collection_additions = '''
## Short Story Collection-Specific Chapter Writing
- **Conciseness**: Short stories demand conciseness. Every sentence should contribute to the plot, character development, or atmosphere.
- **Impactful Openings**: Begin each story with a compelling opening that immediately grabs the reader's attention and introduces the central conflict or theme.
- **Focused Scope**: Limit the scope of each story to a single, well-defined conflict or idea. Avoid trying to cram too much into a short space.
- **Show, Don't Tell**: Use vivid imagery, sensory details, and active voice to show the reader what is happening, rather than simply telling them.
- **Subtext and Implication**: Utilize subtext and implication to convey deeper meanings and emotions. Leave room for the reader to interpret and engage with the story.
- **Strong Endings**: End each story with a satisfying and memorable conclusion that leaves a lasting impression on the reader. This could be a resolution, a revelation, or an open-ended question.
- **Pacing and Rhythm**: Pay attention to the pacing and rhythm of each story. Vary the sentence structure and paragraph length to create a dynamic and engaging reading experience.
- **Emotional Resonance**: Focus on creating an emotional connection with the reader. Use compelling characters, relatable situations, and evocative language to evoke empathy and understanding.
'''
        return base_prompt + short_story_collection_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a shortstorycollection-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        shortstorycollection_series_additions = """

## ShortStoryCollection Series-Specific Planning Elements

### Artistic Progression for ShortStoryCollection
- **Format Mastery**: Show increasing sophistication in shortstorycollection techniques across volumes
- **Creative Evolution**: Plan how the artistic vision develops throughout the shortstorycollection series
- **Thematic Development**: Create themes that deepen and evolve through the shortstorycollection format
- **Artistic Cohesion**: Maintain unified artistic vision while allowing creative growth
- **Format Innovation**: Explore different aspects of shortstorycollection across the series

### ShortStoryCollection Series Continuity
- **Style Consistency**: Maintain recognizable artistic voice across shortstorycollection volumes
- **Technical Standards**: Maintain quality standards appropriate for shortstorycollection
- **Creative Connections**: Create meaningful artistic links between shortstorycollection volumes
- **Format Exploration**: Continue exploring the possibilities of shortstorycollection format
- **Reader Experience**: Create engaging progression for shortstorycollection enthusiasts

Create a shortstorycollection series that showcases artistic development and format mastery across multiple volumes.
"""

        return base_prompt + shortstorycollection_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a shortstorycollection-specific individual volume prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class ShortStoryCollectionMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover copy for a short story collection.

        Args:
        **kwargs: Keyword arguments to customize the prompt further.  Consider including:
        * title (str): The title of the short story collection.
        * author (str): The author of the short story collection.
        * genre_themes (list): A list of genre-specific themes (e.g., "loss," "redemption," "identity," "speculative fiction," "historical fiction," "contemporary realism").
        * story_count (int): The number of stories in the collection.
        * setting_description (str): A brief description of the predominant settings in the stories.
        * target_audience (str):  Description of the target reader (e.g., "fans of literary fiction," "readers who enjoy thought-provoking narratives").
        * emotional_tone (list): A list of emotional tones present in the collection (e.g., "melancholy," "hopeful," "suspenseful," "wry humor").
        * comparison_titles (list): Titles of similar or comparable books or authors (e.g., "in the vein of Alice Munro," "for fans of Ted Chiang").
        * central_conflict_themes (list): Central conflicts/themes explored across stories (e.g., "man vs. nature," "inner turmoil," "societal pressures").
        * unique_selling_point (str): What makes this collection stand out (e.g., "unique narrative structure," "unexplored historical period," "bold experimentation").
        * story_keywords (list): Keywords that represent the stories (e.g., "family secrets," "first love," "alien encounters," "haunted houses").

        Returns:
        str: A detailed prompt string for generating back cover copy.
        """

        title = kwargs.get('title', '[Title of Short Story Collection]')
        author = kwargs.get('author', '[Author Name]')
        genre_themes = kwargs.get('genre_themes', ['[Theme 1]', '[Theme 2]', '[Theme 3]'])
        story_count = kwargs.get('story_count', '[Number of Stories]')
        setting_description = kwargs.get('setting_description', '[Brief Description of the Primary Setting(s)]')
        target_audience = kwargs.get('target_audience', '[Target Audience Description]')
        emotional_tone = kwargs.get('emotional_tone', ['[Emotional Tone 1]', '[Emotional Tone 2]'])
        comparison_titles = kwargs.get('comparison_titles', ['[Comparable Author/Book 1]', '[Comparable Author/Book 2]'])
        central_conflict_themes = kwargs.get('central_conflict_themes', ['[Conflict Theme 1]', '[Conflict Theme 2]'])
        unique_selling_point = kwargs.get('unique_selling_point', '[Unique Selling Point]')
        story_keywords = kwargs.get('story_keywords', ['[Keyword 1]', '[Keyword 2]', '[Keyword 3]'])

        prompt = f"""
        Write compelling back cover copy for a short story collection titled "{title}" by {author}.  This collection features {story_count} interconnected/standalone (choose one) stories that explore themes of {', '.join(genre_themes)}.

        The stories are primarily set in {setting_description}.  The target audience is {target_audience}.  The overall emotional tone of the collection is {', and '.join(emotional_tone)}.

        Consider these central conflicts/themes that appear across multiple stories: {', '.join(central_conflict_themes)}.

        This collection is [choose one: perfect for readers who enjoy/reminiscent of/in the vein of] {', and '.join(comparison_titles)}.

        Highlight the unique selling point: {unique_selling_point}.

        The back cover copy should:

        *   Intrigue the reader with a brief overview of the collection's core themes and emotional resonance.
        *   Hint at the interconnectedness (or stark contrast) between the stories.
        *   Feature a compelling hook that showcases the author's unique voice and storytelling style.
        *   Use evocative language to paint a vivid picture of the settings and characters.
        *   Incorporate some of these keywords: {', '.join(story_keywords)}.
        *   End with a question or statement that leaves the reader wanting more.
        *   Keep the length between 150-200 words.
        *   Focus on the emotional impact and overall experience of reading the collection, rather than summarizing individual stories.
        *   Emphasize the power of short stories to explore complex themes and capture fleeting moments of human experience.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short, punchy 2-3 line description of the short story collection, suitable for online retailers or social media.

        Args:
        **kwargs: Keyword arguments to customize the prompt. Consider:
        * title (str): The title of the short story collection.
        * author (str): The author of the short story collection.
        * core_theme (str): The central theme that ties the collection together.
        * emotional_hook (str):  The primary emotion the stories evoke.
        * unique_element (str): A unique aspect of the collection (e.g., style, setting).
        Returns:
        str: A prompt string for generating a short description.
        """
        title = kwargs.get('title', '[Title of Short Story Collection]')
        author = kwargs.get('author', '[Author Name]')
        core_theme = kwargs.get('core_theme', '[Core Theme]')
        emotional_hook = kwargs.get('emotional_hook', '[Emotional Hook]')
        unique_element = kwargs.get('unique_element', '[Unique Element]')

        prompt = f"""
        Write a concise and captivating 2-3 line description for the short story collection "{title}" by {author}.

        This description should:

        *   Highlight the core theme of {core_theme}.
        *   Emphasize the emotional hook of {emotional_hook}.
        *   Mention the unique element of {unique_element}.
        *   Be attention-grabbing and memorable.
        *   Focus on the overall feeling and experience of reading the collection.
        *   Use strong verbs and evocative language.
        *   Target readers who appreciate short, impactful narratives.
        *   Example: "In {title}, {author} weaves tales of [core_theme] with a [emotional_hook] touch.  Experience a world where [unique_element] shape destinies."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for a punchy, memorable marketing tagline for the short story collection.

        Args:
        **kwargs: Keyword arguments to customize the prompt. Consider:
        * title (str): The title of the short story collection.
        * core_concept (str):  The central idea or concept explored in the stories.
        * emotional_resonance (str): The primary emotional impact of the stories.
        * audience_desire (str): What the target audience is looking for in a short story collection.

        Returns:
        str: A prompt string for generating a marketing tagline.
        """
        title = kwargs.get('title', '[Title of Short Story Collection]')
        core_concept = kwargs.get('core_concept', '[Core Concept]')
        emotional_resonance = kwargs.get('emotional_resonance', '[Emotional Resonance]')
        audience_desire = kwargs.get('audience_desire', '[Audience Desire]')

        prompt = f"""
        Create a short, impactful, and memorable marketing tagline for the short story collection "{title}."

        The tagline should:

        *   Capture the essence of the core concept: {core_concept}.
        *   Convey the emotional resonance: {emotional_resonance}.
        *   Appeal to the audience's desire for: {audience_desire}.
        *   Be concise and easy to remember.
        *   Use strong verbs and evocative language.
        *   Intrigue potential readers and make them want to learn more.
        *   Examples:
        *   "{title}: Where every story is a world."
        *   "{title}:  Short stories, lasting impact."
        *   "{title}: Explore the extraordinary in the ordinary."
        *   "{title}: Bite-sized stories, soul-sized impact."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt to guide the visual style and design of the back cover, considering the short story collection genre.

        Args:
        **kwargs: Keyword arguments to customize the prompt. Consider:
        * genre_mood (str): The overall mood of the collection (e.g., "dark and atmospheric," "bright and whimsical," "realistic and gritty").
        * target_reader_demographic (str): Description of the target reader in terms of visual preferences.
        * cover_art_keywords (list): Keywords related to potential cover art imagery (e.g., "vintage photograph," "abstract shapes," "silhouette of a figure").
        * typography_style (str): Preferred typography style (e.g., "classic serif," "modern sans-serif," "handwritten font").
        * color_palette (list): A list of preferred colors or color schemes.
        * visual_metaphor (str): A central visual metaphor that represents the stories (e.g., "a winding road," "a broken mirror," "a constellation of stars").

        Returns:
        str: A prompt string for guiding the visual design.
        """
        genre_mood = kwargs.get('genre_mood', '[Overall Mood of the Collection]')
        target_reader_demographic = kwargs.get('target_reader_demographic', '[Description of Target Reader Visual Preferences]')
        cover_art_keywords = kwargs.get('cover_art_keywords', ['[Keyword 1]', '[Keyword 2]'])
        typography_style = kwargs.get('typography_style', '[Preferred Typography Style]')
        color_palette = kwargs.get('color_palette', ['[Color 1]', '[Color 2]'])
        visual_metaphor = kwargs.get('visual_metaphor', '[Central Visual Metaphor]')

        prompt = f"""
        Define the visual style and design preferences for the back cover of a short story collection.

        Consider the following:

        *   The overall mood of the collection is: {genre_mood}.
        *   The target reader is {target_reader_demographic}, so the visual style should appeal to their aesthetic preferences.
        *   Potential cover art imagery could include elements related to: {', '.join(cover_art_keywords)}.
        *   The preferred typography style is: {typography_style}.
        *   The color palette should consist of: {', '.join(color_palette)}.
        *   A central visual metaphor that represents the stories is: {visual_metaphor}.

        The back cover design should:

        *   Reflect the tone and themes of the collection.
        *   Be visually appealing and attention-grabbing.
        *   Communicate the genre and target audience.
        *   Create a sense of mystery and intrigue.
        *   Consider using minimalist design principles or a more detailed, illustrative approach depending on the overall mood and target audience.
        *   Think about how the design can hint at the interconnectedness (or distinct nature) of the stories within the collection.
        """
        return prompt
        ```
        shortstorycollection_book_additions = """

## ShortStoryCollection Series Volume Integration

### ShortStoryCollection Artistic Continuity
- **Style Consistency**: Maintain the artistic voice established in previous shortstorycollection volumes
- **Technical Standards**: Maintain quality standards established in the shortstorycollection series
- **Creative Evolution**: Show artistic growth from previous shortstorycollection volumes
- **Format Mastery**: Build upon shortstorycollection techniques established in the series
- **Thematic Connections**: Continue developing themes from earlier shortstorycollection works

### Volume-Specific ShortStoryCollection Focus
- **Artistic Objectives**: What specific shortstorycollection artistic goals will this volume achieve?
- **Format Innovation**: What new shortstorycollection techniques or approaches will be introduced?
- **Creative Development**: How will this volume advance the artistic vision of the series?
- **Series Integration**: How does this volume connect meaningfully to other shortstorycollection works in the series?
- **Artistic Value**: What unique shortstorycollection artistic value does this volume add to the series?

Ensure this volume demonstrates shortstorycollection mastery while serving as an integral part of the artistic series.
"""

        return base_prompt + shortstorycollection_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_series_book_prompt(**kwargs)
