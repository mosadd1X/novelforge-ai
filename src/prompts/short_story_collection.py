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
        base_prompt = super().get_character_prompt(**kwargs)
        
        short_story_collection_additions = '''
## Short Story Collection-Specific Character Development
- **Character Focus**: In short stories, characters must be quickly established and relatable. Focus on a few key traits and motivations that drive their actions.
- **Character Arc (Optional)**: While not always necessary, consider whether each character will undergo a significant change or transformation within the story.
- **Character Diversity**: Ensure a diverse range of characters across the collection, representing different backgrounds, perspectives, and experiences.
- **Recurring Characters (Optional)**: If using recurring characters, carefully plan their development and evolution across different stories.
- **Character Relationships**: Explore the relationships between characters and how they influence each other's actions and decisions.
- **Character Voice**: Develop a distinct voice for each character, using dialogue and internal monologue to reveal their personality and motivations.
- **Character Flaws**: Give characters flaws and vulnerabilities to make them more relatable and believable.
- **Character Motivation**: Clearly define each character's motivations and goals, and how they drive the plot forward.
'''
        return base_prompt + short_story_collection_additions

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
