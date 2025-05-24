"""
Contemporary Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ContemporaryFictionPrompts(FictionBasePrompts):
    GENRE_NAME = "Contemporary Fiction"
    GENRE_DESCRIPTION = "Contemporary fiction explores the complexities of modern life, reflecting current social issues, cultural trends, and the human condition within a relatable and recognizable setting. It often features realistic characters grappling with everyday problems, moral dilemmas, and personal growth in a rapidly changing world."
    
    GENRE_CHARACTERISTICS = [
        "Focus on realism and relatability, depicting characters and situations that resonate with contemporary readers.",
        "Exploration of current social issues such as identity, inequality, technology's impact, and environmental concerns.",
        "Emphasis on character development and psychological depth, delving into the motivations and inner lives of protagonists.",
        "Use of contemporary language and vernacular, reflecting how people communicate in the modern world.",
        "Exploration of diverse perspectives and experiences, representing a wide range of cultural, ethnic, and socioeconomic backgrounds.",
        "Examination of relationships and their complexities, including family dynamics, romantic entanglements, and friendships.",
        "Addressing moral ambiguities and ethical dilemmas, forcing readers to confront difficult questions and consider different viewpoints.",
        "Setting stories in recognizable contemporary settings, often reflecting the urban or suburban landscapes of modern life.",
        "Incorporation of technology and its influence on human interaction, communication, and daily routines.",
        "Exploration of themes such as identity, belonging, purpose, and the search for meaning in a complex world."
    ]
    
    TYPICAL_ELEMENTS = [
        "A protagonist facing a relatable personal or professional challenge.",
        "A realistic setting that grounds the story in the present day.",
        "Complex relationships that drive the plot and character development.",
        "Internal conflicts and moral dilemmas that force characters to make difficult choices.",
        "Exploration of social issues relevant to contemporary society.",
        "Use of dialogue that reflects contemporary speech patterns.",
        "A narrative structure that allows for exploration of character's inner thoughts and feelings.",
        "A theme that resonates with contemporary readers, such as identity, belonging, or the search for meaning.",
        "Subplots that add depth and complexity to the main narrative.",
        "Symbolism and imagery that enhance the thematic resonance of the story.",
        "A resolution that offers a sense of closure, even if it is not a traditional happy ending.",
        "Exploration of the impact of technology on the characters' lives and relationships."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        contemporary_fiction_additions = '''
## Contemporary Fiction-Specific Writing Considerations
- **Authenticity and Voice**: Develop a distinct and authentic voice that resonates with contemporary readers. Pay close attention to capturing the nuances of modern language and cultural references.
- **Character-Driven Narrative**: Prioritize character development and ensure that the plot is driven by the characters' motivations, desires, and flaws.
- **Social Commentary**: Consider incorporating subtle social commentary on relevant issues without being preachy or didactic. Let the characters and their experiences speak for themselves.
- **Relatable Themes**: Focus on universal themes such as love, loss, identity, and belonging, but explore them through the lens of contemporary experiences.
- **Realistic Dialogue**: Craft dialogue that sounds natural and authentic, reflecting the way people actually speak in the modern world. Avoid clichés and forced exposition.
- **Setting as Character**: Use the setting to enhance the mood, atmosphere, and thematic resonance of the story. Pay attention to details that ground the story in a specific time and place.
- **Moral Ambiguity**: Embrace moral ambiguity and explore the gray areas of human behavior. Avoid simplistic portrayals of good versus evil.
- **Emotional Resonance**: Strive to create an emotional connection with readers by exploring the characters' vulnerabilities, fears, and hopes.
'''
        return base_prompt + contemporary_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        contemporary_fiction_additions = '''
## Contemporary Fiction-Specific Outline Requirements
- **Character Arc**: Outline the protagonist's journey of self-discovery and transformation, including their initial state, key turning points, and ultimate resolution.
- **Relationship Dynamics**: Map out the key relationships in the story and how they evolve over time, including conflicts, alliances, and emotional connections.
- **Thematic Development**: Identify the central themes of the story and how they will be explored through the plot, characters, and setting.
- **Social Context**: Consider the social and cultural context of the story and how it will influence the characters' actions and decisions.
- **Plot Structure**: Structure the plot around a central conflict or challenge that the protagonist must overcome, with clear rising action, climax, and resolution.
- **Subplot Integration**: Weave subplots into the main narrative to add depth and complexity to the story, while ensuring they contribute to the overall themes.
- **Pacing and Tension**: Vary the pacing of the story to create moments of tension, suspense, and emotional release.
- **Ending**: Plan a satisfying ending that provides closure while leaving the reader with something to think about. Consider open endings or ambiguous resolutions that reflect the complexities of real life.
'''
        return base_prompt + contemporary_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        contemporary_fiction_additions = '''
## Contemporary Fiction-Specific Character Development
- **Relatability**: Create characters that readers can relate to, even if they don't agree with their choices. Focus on their flaws, vulnerabilities, and desires.
- **Authenticity**: Develop characters with unique voices, backgrounds, and perspectives that reflect the diversity of contemporary society.
- **Motivation**: Clearly define each character's motivations and goals, and how they drive their actions throughout the story.
- **Internal Conflict**: Give characters internal conflicts and moral dilemmas that force them to make difficult choices and confront their own beliefs.
- **Growth and Change**: Show how characters evolve and change over the course of the story, as a result of their experiences and relationships.
- **Backstory**: Develop a rich backstory for each character, including their upbringing, relationships, and formative experiences.
- **Flaws and Strengths**: Balance characters' strengths with their weaknesses to make them more realistic and compelling.
- **Relationships**: Explore the complex relationships between characters, including their conflicts, alliances, and emotional connections.
'''
        return base_prompt + contemporary_fiction_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        contemporary_fiction_additions = '''
## Contemporary Fiction-Specific Chapter Writing
- **Focus on Character**: Each chapter should advance the character's arc, revealing new aspects of their personality, motivations, or relationships.
- **Realistic Dialogue**: Use dialogue to reveal character, advance the plot, and create tension. Ensure it sounds natural and authentic.
- **Sensory Details**: Incorporate vivid sensory details to bring the setting to life and immerse the reader in the scene.
- **Pacing**: Vary the pacing of each chapter to create a sense of rhythm and momentum. Use shorter sentences and paragraphs for action scenes, and longer ones for introspection and description.
- **Conflict and Tension**: Introduce conflict or tension in each chapter to keep the reader engaged and eager to turn the page.
- **Show, Don't Tell**: Use vivid descriptions and actions to show the reader what is happening, rather than simply telling them.
- **Emotional Impact**: Aim to evoke an emotional response in the reader, whether it's empathy, sadness, joy, or anger.
- **Chapter Endings**: End each chapter with a hook that leaves the reader wanting more, such as a cliffhanger, a revelation, or a question.
'''
        return base_prompt + contemporary_fiction_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a contemporaryfiction-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        contemporaryfiction_series_additions = """

## ContemporaryFiction Series-Specific Planning Elements

### Genre-Specific Series Development
- **ContemporaryFiction Conventions**: Ensure each book fulfills contemporaryfiction reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to contemporaryfiction
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to contemporaryfiction
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore contemporaryfiction themes with increasing depth and complexity

### ContemporaryFiction Series Continuity
- **Genre Elements**: Maintain consistent contemporaryfiction elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy contemporaryfiction readers
- **Series Identity**: Establish a strong series identity that feels authentically contemporaryfiction
- **World Building**: Develop the story world in ways that enhance the contemporaryfiction experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the contemporaryfiction genre

Create a contemporaryfiction series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + contemporaryfiction_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a contemporaryfiction-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        contemporaryfiction_book_additions = """

## ContemporaryFiction Series Book Integration

### ContemporaryFiction Continuity for This Book
- **Genre Consistency**: Maintain established contemporaryfiction elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to contemporaryfiction
- **Plot Advancement**: Continue series plot threads while telling a complete contemporaryfiction story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill contemporaryfiction reader expectations while advancing the series narrative

### Book-Specific ContemporaryFiction Focus
- **Central Conflict**: What contemporaryfiction-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new contemporaryfiction elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent contemporaryfiction while serving the series?

Ensure this book feels like an authentic continuation of the contemporaryfiction series while telling a complete, satisfying story.
"""
        
        return base_prompt + contemporaryfiction_book_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_series_book_prompt(**kwargs)
