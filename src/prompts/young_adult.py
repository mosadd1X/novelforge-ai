"""
Young Adult genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class YoungAdultPrompts(FictionBasePrompts):
    GENRE_NAME = "Young Adult"
    GENRE_DESCRIPTION = "Young Adult (YA) fiction focuses on the experiences, challenges, and emotional journeys of teenagers, typically aged 13-19. It explores themes of identity, self-discovery, relationships, and navigating the complexities of adolescence. YA novels often feature relatable characters, fast-paced plots, and authentic voices that resonate with young readers."
    
    GENRE_CHARACTERISTICS = [
        "Focus on relatable teenage protagonists facing realistic or fantastical challenges.",
        "Exploration of themes such as identity, self-discovery, first love, friendship, and family relationships.",
        "Authentic and engaging voice that reflects the language and concerns of contemporary teenagers.",
        "Fast-paced plot with clear stakes and compelling conflicts that keep readers invested.",
        "Emotional depth and exploration of complex emotions such as anxiety, grief, and anger.",
        "Emphasis on character development and personal growth as the protagonist learns and evolves throughout the story.",
        "Inclusion of diverse characters and perspectives to reflect the experiences of a wide range of young people.",
        "Exploration of social issues and contemporary concerns relevant to teenagers, such as bullying, social media, and environmentalism.",
        "Hopeful or optimistic tone, even when dealing with difficult or challenging subject matter.",
        "Clear moral compass and exploration of ethical dilemmas faced by young people."
    ]
    
    TYPICAL_ELEMENTS = [
        "A protagonist aged 13-19 who is grappling with a significant personal challenge.",
        "A strong supporting cast of friends, family, or mentors who play a crucial role in the protagonist's journey.",
        "A central conflict or problem that drives the plot forward and creates tension.",
        "A romantic subplot or exploration of first love and relationships.",
        "A coming-of-age arc where the protagonist learns valuable lessons and grows as a person.",
        "A clear and compelling narrative voice that resonates with young readers.",
        "A fast-paced plot with plenty of action, suspense, or emotional moments.",
        "A resolution that provides closure and leaves the reader feeling satisfied.",
        "Themes of identity, self-discovery, and finding one's place in the world.",
        "Exploration of social issues and contemporary concerns relevant to teenagers.",
        "Use of realistic dialogue and slang that reflects the way teenagers actually speak.",
        "A hopeful or optimistic tone, even when dealing with difficult subject matter."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        young_adult_additions = '''
## Young Adult-Specific Writing Considerations
- **Authentic Voice**: Capture the authentic voice of a teenager. Use contemporary language and slang appropriately, but avoid being overly trendy or using language that will quickly become dated. Focus on conveying genuine emotions and perspectives.
- **Relatable Characters**: Create characters that young readers can connect with. Give them flaws, insecurities, and relatable struggles. Make sure their motivations are clear and believable.
- **Pacing and Plot**: YA novels tend to be fast-paced. Keep the plot moving with clear stakes and compelling conflicts. Avoid long, descriptive passages that might bore young readers.
- **Emotional Depth**: Don't shy away from exploring complex emotions. YA readers are often drawn to stories that deal with difficult topics such as anxiety, grief, and identity.
- **Age-Appropriate Content**: Be mindful of the age range of your target audience. Avoid gratuitous violence, sex, or drug use. Focus on exploring mature themes in a responsible and sensitive way.
- **Hopeful Tone**: Even when dealing with difficult subject matter, maintain a hopeful or optimistic tone. YA readers want to believe that things can get better.
- **Diversity and Inclusion**: Represent a diverse range of characters and perspectives. Include characters of different races, ethnicities, sexual orientations, and gender identities.
- **Moral Complexity**: Explore ethical dilemmas and moral complexities. Avoid simplistic good vs. evil narratives. Allow your characters to make mistakes and learn from them.
'''
        return base_prompt + young_adult_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        young_adult_additions = '''
## Young Adult-Specific Outline Requirements
- **Inciting Incident**: The inciting incident should occur early in the story to quickly hook the reader. It should present a clear challenge or problem that the protagonist must face.
- **Rising Action**: The rising action should be filled with escalating conflicts and challenges that test the protagonist's abilities and push them to their limits.
- **Midpoint**: The midpoint should mark a significant turning point in the story, where the protagonist gains new information or makes a crucial decision that changes the course of the plot.
- **Climax**: The climax should be the most intense and exciting part of the story, where the protagonist confronts the main antagonist or overcomes the central conflict.
- **Falling Action**: The falling action should tie up loose ends and show the consequences of the protagonist's actions.
- **Resolution**: The resolution should provide closure and leave the reader feeling satisfied. It should show how the protagonist has grown and changed as a result of their experiences.
- **Character Arcs**: Outline the key moments in the protagonist's character arc, showing how they evolve and learn throughout the story.
- **Relationship Dynamics**: Map out the key relationships between the protagonist and other characters, and how those relationships change over time.
- **Thematic Elements**: Identify the key themes you want to explore in your novel, and outline how those themes will be developed throughout the story.
'''
        return base_prompt + young_adult_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        young_adult_additions = '''
## Young Adult-Specific Character Development
- **Relatability**: Focus on making your characters relatable to young readers. Give them flaws, insecurities, and realistic struggles.
- **Authenticity**: Ensure your characters' voices and actions are authentic to their age and background. Avoid stereotypes and create nuanced personalities.
- **Internal Conflicts**: Explore your characters' internal conflicts and motivations. What are their deepest fears and desires?
- **External Conflicts**: Define the external conflicts that your characters face. How do they react to challenges and adversity?
- **Growth and Change**: Show how your characters grow and change throughout the story. What lessons do they learn? How do they overcome their weaknesses?
- **Relationships**: Develop meaningful relationships between your characters. How do they support and challenge each other?
- **Backstory**: Create a detailed backstory for each of your main characters. What experiences have shaped them into who they are today?
- **Motivations**: Clearly define your characters' motivations. What drives them to act the way they do?
'''
        return base_prompt + young_adult_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        young_adult_additions = '''
## Young Adult-Specific Chapter Writing
- **Fast Pacing**: Maintain a fast pace throughout each chapter. Keep the plot moving forward and avoid unnecessary descriptions or exposition.
- **Clear Stakes**: Make sure the stakes are clear in each chapter. What does the protagonist stand to gain or lose?
- **Compelling Conflict**: Include compelling conflicts in each chapter, whether internal or external.
- **Emotional Resonance**: Evoke strong emotions in your readers. Make them feel what the characters are feeling.
- **Strong Voice**: Use a strong and authentic voice that resonates with young readers.
- **Cliffhangers**: End each chapter with a cliffhanger to keep readers engaged and eager to read on.
- **Dialogue**: Use realistic and engaging dialogue to reveal character and advance the plot.
- **Show, Don't Tell**: Focus on showing, not telling. Use vivid descriptions and action to bring the story to life.
'''
        return base_prompt + young_adult_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a youngadult-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        youngadult_series_additions = """

## YoungAdult Series-Specific Planning Elements

### Genre-Specific Series Development
- **YoungAdult Conventions**: Ensure each book fulfills youngadult reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to youngadult
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to youngadult
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore youngadult themes with increasing depth and complexity

### YoungAdult Series Continuity
- **Genre Elements**: Maintain consistent youngadult elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy youngadult readers
- **Series Identity**: Establish a strong series identity that feels authentically youngadult
- **World Building**: Develop the story world in ways that enhance the youngadult experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the youngadult genre

Create a youngadult series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + youngadult_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a youngadult-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        youngadult_book_additions = """

## YoungAdult Series Book Integration

### YoungAdult Continuity for This Book
- **Genre Consistency**: Maintain established youngadult elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to youngadult
- **Plot Advancement**: Continue series plot threads while telling a complete youngadult story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill youngadult reader expectations while advancing the series narrative

### Book-Specific YoungAdult Focus
- **Central Conflict**: What youngadult-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new youngadult elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent youngadult while serving the series?

Ensure this book feels like an authentic continuation of the youngadult series while telling a complete, satisfying story.
"""

        return base_prompt + youngadult_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return YoungAdultPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return YoungAdultPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return YoungAdultPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return YoungAdultPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return YoungAdultPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return YoungAdultPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return YoungAdultPrompts.get_series_book_prompt(**kwargs)
