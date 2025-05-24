"""
Literary Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class LiteraryFictionPrompts(FictionBasePrompts):
    GENRE_NAME = "Literary Fiction"
    GENRE_DESCRIPTION = "Literary fiction is a genre characterized by its focus on artistic merit and depth of meaning, rather than solely on plot or commercial appeal. It often explores complex themes, nuanced characters, and intricate relationships, employing sophisticated language and stylistic techniques to create a profound and thought-provoking reading experience. The genre frequently delves into the human condition, societal issues, and philosophical questions, leaving a lasting impact on the reader."
    
    GENRE_CHARACTERISTICS = [
        "Emphasis on Character Development: Characters are intricately drawn, with complex motivations, internal conflicts, and realistic flaws. Their psychological depth is prioritized over plot-driven actions.",
        "Exploration of Universal Themes: Stories often grapple with profound and timeless themes such as love, loss, identity, morality, and the search for meaning in life.",
        "Introspective Narrative: The narrative often delves into the inner thoughts and feelings of characters, providing insight into their perspectives and motivations.",
        "Sophisticated Language and Style: The writing is characterized by its elegance, precision, and attention to detail, often employing literary devices such as symbolism, metaphor, and imagery.",
        "Subtle Plot Development: Plot is often secondary to character development and thematic exploration, with a focus on internal conflicts and emotional journeys rather than external action.",
        "Ambiguity and Open-Endedness: Stories may leave certain questions unanswered or offer multiple interpretations, encouraging readers to engage with the text on a deeper level.",
        "Realistic and Believable Settings: Settings are often depicted with vivid detail and authenticity, serving as a backdrop for the characters' experiences and reflecting the themes of the story.",
        "Focus on the Human Condition: Literary fiction explores the complexities of human relationships, the challenges of existence, and the search for meaning and purpose in a chaotic world.",
        "Social Commentary: Stories may offer subtle or overt critiques of societal norms, political systems, and cultural values, prompting readers to reflect on the world around them."
    ]
    
    TYPICAL_ELEMENTS = [
        "Complex and nuanced characters with internal conflicts.",
        "Exploration of universal themes such as love, loss, identity, and morality.",
        "Introspective narrative style with a focus on character's inner thoughts and feelings.",
        "Use of symbolism, metaphor, and imagery to convey deeper meaning.",
        "Subtle plot development that prioritizes character development and thematic exploration.",
        "Realistic and believable settings that reflect the themes of the story.",
        "Exploration of human relationships and the complexities of human connection.",
        "Social commentary on societal norms, political systems, and cultural values.",
        "Ambiguous or open-ended endings that leave readers with questions to ponder.",
        "Use of stream-of-consciousness or other experimental narrative techniques.",
        "Focus on the psychological and emotional impact of events on characters.",
        "Exploration of philosophical questions about the nature of existence and the meaning of life."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        literary_fiction_additions = '''
## Literary Fiction-Specific Writing Considerations
- **Character-Driven Narrative**: Prioritize the development of complex, believable characters with internal conflicts and motivations. Focus on their psychological depth and emotional journeys.
- **Thematic Resonance**: Identify and explore universal themes that resonate with readers on a deeper level. Use symbolism, metaphor, and imagery to convey these themes effectively.
- **Sophisticated Prose**: Employ elegant and precise language, paying attention to rhythm, tone, and imagery. Avoid clichés and strive for originality in your writing style.
- **Subtle Plot Development**: Focus on internal conflicts and emotional journeys rather than external action. Allow the plot to unfold organically from the characters' choices and experiences.
- **Realistic Worldbuilding**: Create believable settings that reflect the themes of the story and provide a backdrop for the characters' experiences. Pay attention to detail and authenticity.
- **Exploration of Human Condition**: Delve into the complexities of human relationships, the challenges of existence, and the search for meaning and purpose in a chaotic world.
- **Ambiguity and Open-Endedness**: Embrace ambiguity and leave certain questions unanswered, encouraging readers to engage with the text on a deeper level and draw their own conclusions.
- **Social Commentary (Optional)**: Consider incorporating subtle or overt critiques of societal norms, political systems, and cultural values to prompt readers to reflect on the world around them.
'''
        return base_prompt + literary_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        literary_fiction_additions = '''
## Literary Fiction-Specific Outline Requirements
- **Character Arcs**: Outline the emotional and psychological journeys of your main characters, focusing on their internal conflicts and transformations.
- **Thematic Development**: Identify the key themes you want to explore and outline how they will be developed throughout the story. Consider using recurring motifs or symbols.
- **Subtle Plot Points**: Focus on key moments of decision and realization for your characters, rather than plot-driven events. These moments should drive the narrative forward and reveal deeper truths about the characters and their world.
- **Setting as Character**: Consider how the setting can be used to reflect the themes of the story and the emotional states of the characters. Outline key settings and their symbolic significance.
- **Internal Conflict**: Emphasize the internal struggles of your characters. Outline the nature of these conflicts and how they will be resolved (or not) by the end of the story.
- **Relationship Dynamics**: Outline the key relationships between characters and how they will evolve throughout the story. Focus on the complexities and nuances of these relationships.
- **Symbolic Structure**: Consider using a symbolic structure to organize your story, such as a journey, a quest, or a descent into darkness.
- **Open-Ended Resolution**: Plan for an ending that is ambiguous or open-ended, leaving readers with questions to ponder and encouraging them to engage with the text on a deeper level.
'''
        return base_prompt + literary_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        literary_fiction_additions = '''
## Literary Fiction-Specific Character Development
- **Internal Conflicts**: Focus on creating characters with deep-seated internal conflicts that drive their actions and shape their personalities. What are their deepest fears, desires, and insecurities?
- **Moral Ambiguity**: Avoid creating purely good or purely evil characters. Instead, create characters who are morally ambiguous and capable of both good and bad actions.
- **Psychological Depth**: Delve into the psychological complexities of your characters. Explore their past traumas, their coping mechanisms, and their motivations for their actions.
- **Realistic Flaws**: Give your characters realistic flaws that make them relatable and believable. These flaws should be integral to their personalities and should influence their decisions.
- **Character Arcs**: Plan for your characters to undergo significant transformations throughout the story. How will their experiences change them, and what lessons will they learn?
- **Subtlety in Motivation**: Avoid explicitly stating your characters' motivations. Instead, reveal their motivations through their actions, their dialogue, and their interactions with other characters.
- **Backstory Integration**: Develop a detailed backstory for each of your main characters, and integrate this backstory into the narrative in a subtle and organic way.
- **Unreliable Narrators**: Consider using an unreliable narrator to add layers of complexity and ambiguity to your story.
'''
        return base_prompt + literary_fiction_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        literary_fiction_additions = '''
## Literary Fiction-Specific Chapter Writing
- **Focus on Atmosphere**: Prioritize creating a strong sense of atmosphere through vivid descriptions of the setting, the weather, and the characters' emotional states.
- **Show, Don't Tell**: Use sensory details and evocative language to show the reader what is happening, rather than simply telling them.
- **Internal Monologue**: Incorporate internal monologue to reveal the characters' thoughts, feelings, and motivations.
- **Subtext and Implication**: Use subtext and implication to convey deeper meaning and create a sense of unease or tension.
- **Symbolic Imagery**: Employ symbolic imagery to reinforce the themes of the story and add layers of meaning to the narrative.
- **Pacing and Rhythm**: Vary the pacing and rhythm of your writing to create a sense of flow and momentum. Use short, choppy sentences to create tension, and long, flowing sentences to create a sense of peace or tranquility.
- **Character-Driven Scenes**: Ensure that each scene is driven by the characters' actions and decisions. Avoid scenes that are purely expositional or plot-driven.
- **Emotional Resonance**: Strive to create scenes that resonate emotionally with the reader, evoking feelings of empathy, sadness, joy, or anger.
'''
        return base_prompt + literary_fiction_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a literaryfiction-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        literaryfiction_series_additions = """

## LiteraryFiction Series-Specific Planning Elements

### Genre-Specific Series Development
- **LiteraryFiction Conventions**: Ensure each book fulfills literaryfiction reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to literaryfiction
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to literaryfiction
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore literaryfiction themes with increasing depth and complexity

### LiteraryFiction Series Continuity
- **Genre Elements**: Maintain consistent literaryfiction elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy literaryfiction readers
- **Series Identity**: Establish a strong series identity that feels authentically literaryfiction
- **World Building**: Develop the story world in ways that enhance the literaryfiction experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the literaryfiction genre

Create a literaryfiction series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + literaryfiction_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a literaryfiction-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        literaryfiction_book_additions = """

## LiteraryFiction Series Book Integration

### LiteraryFiction Continuity for This Book
- **Genre Consistency**: Maintain established literaryfiction elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to literaryfiction
- **Plot Advancement**: Continue series plot threads while telling a complete literaryfiction story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill literaryfiction reader expectations while advancing the series narrative

### Book-Specific LiteraryFiction Focus
- **Central Conflict**: What literaryfiction-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new literaryfiction elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent literaryfiction while serving the series?

Ensure this book feels like an authentic continuation of the literaryfiction series while telling a complete, satisfying story.
"""

        return base_prompt + literaryfiction_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return LiteraryFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return LiteraryFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return LiteraryFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return LiteraryFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return LiteraryFictionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return LiteraryFictionPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return LiteraryFictionPrompts.get_series_book_prompt(**kwargs)
