"""
Middle Grade genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class MiddleGradePrompts(FictionBasePrompts):
    GENRE_NAME = "Middle Grade"
    GENRE_DESCRIPTION = "Middle Grade fiction is aimed at readers aged 8-12. It typically features protagonists in this age range who are navigating challenges related to friendship, family, self-discovery, and the transition to adolescence. The tone is generally optimistic and hopeful, with age-appropriate themes and language. While conflict exists, resolutions are usually positive and emphasize growth and learning."
    
    GENRE_CHARACTERISTICS = [
        "Protagonist is typically between 8 and 12 years old, facing relatable challenges.",
        "Focus on themes of friendship, family, identity, and navigating social dynamics.",
        "Clear and straightforward prose, avoiding complex sentence structures or overly descriptive language.",
        "Optimistic and hopeful tone, even when dealing with difficult subjects.",
        "Age-appropriate themes and content, avoiding mature or graphic material.",
        "Strong emphasis on character development and growth.",
        "Plot-driven stories with a clear beginning, middle, and end.",
        "Presence of a moral or lesson, subtly woven into the narrative.",
        "Relatable and engaging voice that resonates with young readers.",
        "Limited use of complex world-building or intricate plotlines, unless specifically geared toward fantasy or adventure subgenres within Middle Grade."
    ]
    
    TYPICAL_ELEMENTS = [
        "A relatable protagonist with flaws and strengths.",
        "A clear and compelling central conflict.",
        "Supportive and/or challenging friendships.",
        "Family dynamics that influence the protagonist's journey.",
        "A school setting or school-related events.",
        "A mentor figure (teacher, grandparent, etc.) who provides guidance.",
        "Moments of humor and lightheartedness.",
        "Opportunities for the protagonist to learn and grow.",
        "A satisfying resolution that ties up loose ends.",
        "A clear sense of right and wrong.",
        "Elements of mystery, adventure, or fantasy (depending on the subgenre).",
        "A theme or message about the importance of kindness, empathy, or perseverance."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Writing Considerations
- **Voice and Tone**: Maintain a voice that is engaging and relatable to 8-12 year olds. Avoid condescending language or overly complex vocabulary. The tone should be generally optimistic and hopeful, even when addressing difficult topics.
- **Character Development**: Focus on creating believable and relatable characters with clear motivations and flaws. Show their growth and development throughout the story.
- **Plot Structure**: Ensure a clear and compelling plot with a well-defined beginning, middle, and end. The pacing should be appropriate for the target age group, avoiding overly slow or rushed sections.
- **Theme and Message**: Subtly weave a positive message or theme into the story, such as the importance of friendship, family, or perseverance. Avoid being preachy or didactic.
- **Age-Appropriateness**: Carefully consider the age-appropriateness of the themes, language, and content. Avoid mature or graphic material that is not suitable for young readers.
- **Worldbuilding (if applicable)**: If the story involves fantasy or science fiction elements, keep the worldbuilding relatively simple and easy to understand. Focus on the aspects that are most relevant to the plot and characters.
- **Humor**: Incorporate age-appropriate humor to keep the story engaging and entertaining. This could include witty dialogue, funny situations, or relatable observations.
- **Emotional Resonance**: Aim to create an emotional connection with the reader by exploring relatable feelings and experiences, such as joy, sadness, fear, and excitement.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Outline Requirements
- **Inciting Incident**: The inciting incident should be clear and engaging, immediately drawing the reader into the story. It should present a problem or challenge that the protagonist must overcome.
- **Rising Action**: The rising action should consist of a series of escalating events that build tension and suspense. Each event should present new obstacles or challenges for the protagonist.
- **Midpoint**: The midpoint should mark a significant turning point in the story, where the protagonist gains new knowledge or insight that changes their perspective or approach.
- **Climax**: The climax should be the most exciting and suspenseful part of the story, where the protagonist confronts the main antagonist or challenge.
- **Falling Action**: The falling action should consist of the events that lead to the resolution of the conflict. It should show the consequences of the protagonist's actions and the impact on their relationships.
- **Resolution**: The resolution should provide a satisfying conclusion to the story, tying up loose ends and showing the protagonist's growth and development. It should leave the reader with a sense of hope and optimism.
- **Subplots (if applicable)**: Subplots should be carefully integrated into the main plot, adding depth and complexity to the story without overwhelming the reader. They should contribute to the overall themes and message of the book.
- **Chapter Breaks**: Consider where to break chapters to maintain pacing and reader engagement. End chapters on cliffhangers or moments of suspense to encourage readers to keep turning the pages.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Character Development
- **Relatability**: Ensure the protagonist is relatable to middle grade readers. Give them flaws, insecurities, and relatable struggles that resonate with the target audience.
- **Motivation**: Clearly define the protagonist's motivations and goals. What do they want to achieve, and why is it important to them?
- **Growth**: Show the protagonist's growth and development throughout the story. How do they change and learn from their experiences?
- **Supporting Characters**: Develop well-rounded supporting characters who play a significant role in the protagonist's journey. Give them their own motivations and backstories.
- **Antagonist**: Create a compelling antagonist who presents a clear obstacle for the protagonist to overcome. The antagonist should have believable motivations, even if they are misguided.
- **Friendships**: Explore the dynamics of friendships, both positive and negative. Show the importance of loyalty, trust, and communication in building strong relationships.
- **Family**: Depict family relationships in a realistic and nuanced way. Show the impact of family dynamics on the protagonist's life and choices.
- **Voice**: Give each character a distinct voice and personality. Use dialogue and actions to reveal their individual traits and quirks.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Chapter Writing
- **Clear Focus**: Each chapter should have a clear focus and purpose, advancing the plot or developing the characters.
- **Engaging Opening**: Start each chapter with an engaging hook that grabs the reader's attention and makes them want to keep reading.
- **Pacing**: Maintain a good pace throughout the chapter, avoiding overly long descriptions or slow-moving scenes.
- **Dialogue**: Use dialogue to reveal character, advance the plot, and add humor or tension. Keep dialogue natural and age-appropriate.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show the reader what is happening, rather than simply telling them.
- **Conflict and Tension**: Incorporate conflict and tension into each chapter to keep the reader engaged. This could be internal conflict, external conflict, or a combination of both.
- **Cliffhangers**: End chapters on cliffhangers or moments of suspense to encourage readers to keep turning the pages.
- **Age-Appropriate Language**: Use language that is appropriate for the target age group, avoiding overly complex vocabulary or mature themes.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a middlegrade-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        middlegrade_series_additions = """

## MiddleGrade Series-Specific Planning Elements

### Genre-Specific Series Development
- **MiddleGrade Conventions**: Ensure each book fulfills middlegrade reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to middlegrade
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to middlegrade
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore middlegrade themes with increasing depth and complexity

### MiddleGrade Series Continuity
- **Genre Elements**: Maintain consistent middlegrade elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy middlegrade readers
- **Series Identity**: Establish a strong series identity that feels authentically middlegrade
- **World Building**: Develop the story world in ways that enhance the middlegrade experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the middlegrade genre

Create a middlegrade series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + middlegrade_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a middlegrade-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        middlegrade_book_additions = """

## MiddleGrade Series Book Integration

### MiddleGrade Continuity for This Book
- **Genre Consistency**: Maintain established middlegrade elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to middlegrade
- **Plot Advancement**: Continue series plot threads while telling a complete middlegrade story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill middlegrade reader expectations while advancing the series narrative

### Book-Specific MiddleGrade Focus
- **Central Conflict**: What middlegrade-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new middlegrade elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent middlegrade while serving the series?

Ensure this book feels like an authentic continuation of the middlegrade series while telling a complete, satisfying story.
"""

        return base_prompt + middlegrade_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_series_book_prompt(**kwargs)
