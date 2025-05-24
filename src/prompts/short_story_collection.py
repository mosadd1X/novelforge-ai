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

def get_series_book_prompt(**kwargs) -> str:
    return ShortStoryCollectionPrompts.get_series_book_prompt(**kwargs)
