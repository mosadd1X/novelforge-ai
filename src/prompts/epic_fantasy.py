"""
Epic Fantasy genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class EpicFantasyPrompts(FictionBasePrompts):
    GENRE_NAME = "Epic Fantasy"
    GENRE_DESCRIPTION = "Epic Fantasy is a subgenre of fantasy characterized by its grand scope, intricate world-building, and focus on a heroic quest or struggle against overwhelming evil. Stories often involve multiple characters, complex political landscapes, and magical systems that are deeply integrated into the world's history and culture. Themes of good versus evil, destiny, sacrifice, and the corrupting influence of power are prevalent."
    
    GENRE_CHARACTERISTICS = [
        "Extensive World-Building: A meticulously crafted world with its own history, geography, cultures, languages, and mythologies.",
        "Grand Scope and Scale: Stories that span vast distances, involve large casts of characters, and address conflicts that affect entire nations or the world itself.",
        "Heroic Quest or Struggle: A central narrative driven by a hero's journey or a group's fight against a powerful, often supernatural, antagonist.",
        "Complex Magic Systems: Well-defined and internally consistent magic systems that play a significant role in the plot and world-building.",
        "Moral Ambiguity: While often featuring a clear conflict between good and evil, characters and situations often present moral complexities and shades of gray.",
        "Prophecies and Destinies: The presence of prophecies, ancient lore, and predetermined destinies that influence the characters' actions and the course of events.",
        "Mythic and Legendary Elements: Incorporation of elements from mythology, folklore, and legends, often drawing inspiration from various cultures.",
        "High Stakes and World-Altering Consequences: The outcome of the central conflict has significant and lasting repercussions for the world and its inhabitants.",
        "Exploration of Power and Corruption: Examination of the nature of power, its potential for corruption, and the responsibilities that come with it.",
        "Detailed Political Intrigue: Complex political systems, power struggles, and alliances that shape the narrative and influence character motivations."
    ]
    
    TYPICAL_ELEMENTS = [
        "Ancient Artifacts: Powerful objects with historical significance and magical properties.",
        "Magical Creatures: Dragons, elves, dwarves, or other fantastical beings that inhabit the world.",
        "Lost Civilizations: Ruins and remnants of advanced societies with forgotten knowledge and technologies.",
        "Prophecies and Oracles: Characters who can foresee the future or interpret signs and omens.",
        "Chosen One: A character destined to fulfill a specific role or save the world.",
        "Mentors and Guides: Wise figures who provide guidance and training to the protagonist.",
        "Dark Lords and Evil Empires: Antagonistic forces seeking to dominate or destroy the world.",
        "Epic Battles: Large-scale conflicts between armies or factions with significant consequences.",
        "Political Intrigue: Complex schemes and power plays among rulers and nobles.",
        "Magical Schools and Orders: Institutions dedicated to the study and practice of magic.",
        "Journeys and Quests: Long and perilous voyages to achieve a specific goal.",
        "Sacrifice and Redemption: Characters who make significant sacrifices for the greater good or seek redemption for past actions."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Writing Considerations
- **World-Building Depth**: Focus on creating a believable and immersive world with consistent rules, history, and cultures. Consider the impact of magic on society, economy, and politics.
- **Character Complexity**: Develop characters with nuanced motivations, flaws, and strengths. Explore their moral dilemmas and how they evolve throughout the story.
- **Magic System Consistency**: Design a magic system with clear rules and limitations. Avoid deus ex machina solutions and ensure that magic has consequences.
- **Scope and Pacing**: Balance the grand scope of the story with a compelling narrative pace. Avoid excessive exposition and maintain reader engagement.
- **Political Intrigue**: Craft believable political systems and power struggles. Consider the motivations of different factions and the consequences of their actions.
- **Mythic Resonance**: Incorporate elements of mythology and folklore to add depth and resonance to the story. Draw inspiration from various cultures and traditions.
- **Theme Exploration**: Explore universal themes such as good versus evil, destiny, sacrifice, and the corrupting influence of power.
- **Language and Tone**: Use evocative language and a formal tone to create a sense of grandeur and importance. Consider the dialects and accents of different cultures within the world.
'''
        return base_prompt + epic_fantasy_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Outline Requirements
- **World Introduction**: Dedicate the initial chapters to introducing the world, its key locations, cultures, and history. Establish the setting as a character in itself.
- **Character Arcs**: Plan out the major character arcs for each significant character, including their motivations, challenges, and transformations.
- **Plot Threads**: Outline the various plot threads and subplots, ensuring they intertwine and contribute to the overall narrative.
- **Magic System Integration**: Show how the magic system influences the plot and character actions. Plan key moments where magic is used and its consequences.
- **Political Developments**: Map out the political landscape and how it evolves throughout the story. Include key political events and their impact on the characters.
- **Rising Action and Climax**: Structure the rising action to build tension and anticipation, leading to a climactic confrontation that resolves the central conflict.
- **Resolution and Aftermath**: Plan for a resolution that addresses the major plot threads and explores the long-term consequences of the events.
- **Thematic Resonance**: Ensure that the outline reflects the core themes of the story and reinforces the overall message.
'''
        return base_prompt + epic_fantasy_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Character Development
- **Heroic Archetypes**: Consider classic heroic archetypes (e.g., the reluctant hero, the chosen one) and how they can be adapted to create unique and compelling characters.
- **Moral Complexity**: Give characters flaws, doubts, and internal conflicts. Explore their moral compass and how it is tested throughout the story.
- **Backstory and Motivation**: Develop detailed backstories that explain the characters' motivations, fears, and desires.
- **Relationships and Alliances**: Create complex relationships between characters, including alliances, rivalries, and romances.
- **Magical Abilities**: If a character possesses magical abilities, define the extent and limitations of their powers.
- **Growth and Transformation**: Plan how the characters will grow and change throughout the story, learning from their experiences and overcoming their weaknesses.
- **Cultural Influences**: Consider how the characters' cultures and backgrounds shape their beliefs, values, and behaviors.
- **Impact on the World**: Think about how the characters' actions and decisions will impact the world around them.
'''
        return base_prompt + epic_fantasy_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Chapter Writing
- **World-Building Integration**: Weave world-building details seamlessly into the narrative, avoiding info dumps. Show, don't tell, the reader about the world.
- **Character Development**: Use each chapter to further develop the characters, revealing their thoughts, feelings, and motivations.
- **Plot Progression**: Advance the plot in each chapter, either by introducing new conflicts, resolving old ones, or revealing important information.
- **Descriptive Language**: Use vivid and evocative language to create a sense of atmosphere and immersion.
- **Pacing and Tension**: Vary the pacing of the chapters to create a sense of tension and anticipation.
- **Dialogue and Interaction**: Write realistic and engaging dialogue that reveals character and advances the plot.
- **Thematic Resonance**: Ensure that each chapter contributes to the overall themes of the story.
- **Cliffhangers and Hooks**: End chapters with cliffhangers or hooks to keep the reader engaged and eager to continue reading.
'''
        return base_prompt + epic_fantasy_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a epicfantasy-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        epicfantasy_series_additions = """

## EpicFantasy Series-Specific Planning Elements

### Genre-Specific Series Development
- **EpicFantasy Conventions**: Ensure each book fulfills epicfantasy reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to epicfantasy
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to epicfantasy
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore epicfantasy themes with increasing depth and complexity

### EpicFantasy Series Continuity
- **Genre Elements**: Maintain consistent epicfantasy elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy epicfantasy readers
- **Series Identity**: Establish a strong series identity that feels authentically epicfantasy
- **World Building**: Develop the story world in ways that enhance the epicfantasy experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the epicfantasy genre

Create a epicfantasy series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + epicfantasy_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a epicfantasy-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class EpicFantasyMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling Epic Fantasy back cover descriptions.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, author, target audience).

        Returns:
        A string containing the prompt for generating Epic Fantasy back cover copy.
        """
        prompt = f"""
        Write a captivating back cover description for an Epic Fantasy novel.

        **Genre:** Epic Fantasy

        **Key Elements to Include:**

        *   **Scope and Stakes:** Emphasize the vast scope of the story, including world-altering events, wars between nations, and the fate of entire civilizations hanging in the balance. Use language that conveys immense scale and consequence.
        *   **Magic System:** Briefly hint at the magic system, highlighting its depth, complexity, and potential for both good and evil. Use evocative language to describe the nature of the magic (e.g., "ancient runes," "elemental forces," "blood magic").
        *   **Characters:** Introduce the main characters, focusing on their flaws, motivations, and the burdens they carry. Emphasize their epic journey of self-discovery and their roles in the grand scheme of things. Highlight any chosen one archetypes or reluctant heroes.
        *   **Worldbuilding:** Allude to the rich and immersive world, including its history, cultures, and unique landscapes. Use vivid imagery and sensory details to bring the world to life (e.g., "towering mountain ranges," "ancient forests," "forgotten cities").
        *   **Themes:** Touch upon universal themes common in Epic Fantasy, such as good vs. evil, sacrifice, destiny, power, and the corrupting influence of ambition.
        *   **Emotional Hook:** Create a sense of wonder, excitement, and emotional investment in the story. Hint at the challenges and sacrifices the characters will face.
        *   **Intrigue:** End with a cliffhanger or a question that leaves the reader wanting to know more.

        **Specific Guidelines:**

        *   **Target Audience:** Aim for readers who enjoy sprawling narratives, complex characters, and intricate worldbuilding.
        *   **Tone:** Maintain a tone that is both epic and engaging, balancing grandeur with emotional depth.
        *   **Length:** Keep the description concise and impactful (approximately 150-250 words).
        *   **Keywords:** Incorporate relevant keywords that will attract Epic Fantasy readers (e.g., "magic," "quest," "prophecy," "kingdom," "war," "hero," "destiny").
        *   **Avoid Spoilers:** Tease the plot without revealing major twists or ending details.

        **Example Structure:**

        1.  Start with a hook that grabs the reader's attention and introduces the central conflict.
        2.  Briefly introduce the main characters and their roles in the story.
        3.  Highlight the stakes and the consequences of failure.
        4.  Allude to the magic system and the worldbuilding.
        5.  End with a cliffhanger or a question that leaves the reader wanting to know more.

        **Additional Information (if available):**

        *   Title: {kwargs.get("title", "[Title]")}
        *   Author: {kwargs.get("author", "[Author]")}
        *   Main Character(s): {kwargs.get("main_characters", "[Main Characters]")}
        *   Setting: {kwargs.get("setting", "[Setting]")}
        *   Central Conflict: {kwargs.get("central_conflict", "[Central Conflict]")}
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, punchy Epic Fantasy book recommendation (2-3 lines).

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, author, target audience).

        Returns:
        A string containing the prompt for generating a short Epic Fantasy description.
        """
        prompt = f"""
        Write a short, engaging book recommendation (2-3 lines) for an Epic Fantasy novel.

        **Genre:** Epic Fantasy

        **Key Elements to Include:**

        *   **Core Concept:** Immediately convey the central concept or hook of the story.
        *   **Target Audience:** Focus on what will appeal to fans of epic fantasy.
        *   **Intrigue:** Leave the reader wanting to know more.
        *   **Emotional Hook:** Briefly touch on the emotional core of the story.

        **Specific Guidelines:**

        *   **Length:** Extremely concise (2-3 lines maximum).
        *   **Keywords:** Use strong keywords that resonate with Epic Fantasy readers (e.g., "epic," "magic," "quest," "world-shattering").
        *   **Tone:** Enthusiastic and compelling.

        **Example:**

        "In a world teetering on the brink of destruction, a reluctant hero must rise to face an ancient evil. Prepare for a sprawling epic filled with magic, betrayal, and breathtaking battles."

        **Additional Information (if available):**

        *   Title: {kwargs.get("title", "[Title]")}
        *   Author: {kwargs.get("author", "[Author]")}
        *   Main Conflict: {kwargs.get("main_conflict", "[Main Conflict]")}
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy Epic Fantasy marketing tagline.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, author, target audience).

        Returns:
        A string containing the prompt for generating an Epic Fantasy tagline.
        """
        prompt = f"""
        Write a short, attention-grabbing marketing tagline for an Epic Fantasy novel.

        **Genre:** Epic Fantasy

        **Key Elements to Include:**

        *   **Intrigue:** Spark curiosity and make the reader want to know more.
        *   **Epic Scope:** Hint at the grand scale of the story.
        *   **Emotional Resonance:** Evoke a sense of wonder, excitement, or danger.
        *   **Uniqueness:** Highlight what makes the book stand out from other Epic Fantasy novels.

        **Specific Guidelines:**

        *   **Length:** Extremely short (ideally 5-10 words).
        *   **Keywords:** Use powerful keywords that resonate with Epic Fantasy readers (e.g., "magic," "destiny," "war," "kingdom," "prophecy").
        *   **Tone:** Bold, dramatic, and memorable.

        **Examples:**

        *   "Destiny awaits. The world hangs in the balance."
        *   "Magic will rise. Empires will fall."
        *   "One hero. A thousand worlds. An epic quest."

        **Additional Information (if available):**

        *   Title: {kwargs.get("title", "[Title]")}
        *   Core Theme: {kwargs.get("core_theme", "[Core Theme]")}
        *   Main Conflict: {kwargs.get("main_conflict", "[Main Conflict]")}
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates preferences for back cover visual design for an Epic Fantasy novel.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, author, target audience).

        Returns:
        A string containing the visual style preferences for an Epic Fantasy back cover.
        """
        prompt = f"""
        Describe the desired visual style for the back cover of an Epic Fantasy novel.

        **Genre:** Epic Fantasy

        **Visual Elements:**

        *   **Imagery:** Suggest imagery that evokes the grand scope and atmosphere of the story. Consider landscapes (e.g., mountains, forests, castles), characters (e.g., warriors, mages, mythical creatures), and symbolic elements (e.g., swords, crowns, runes).
        *   **Color Palette:** Suggest a color palette that reflects the tone and themes of the book. Consider using rich, saturated colors for a sense of grandeur or muted, earthy tones for a more gritty and realistic feel.
        *   **Typography:** Suggest a font style that is both legible and visually appealing. Consider using a classic serif font for a traditional feel or a more modern sans-serif font for a contemporary look.
        *   **Overall Design:** Aim for a design that is both eye-catching and informative. The design should clearly communicate the genre and tone of the book while also highlighting its key elements. Consider incorporating elements of fantasy art, such as intricate patterns, stylized illustrations, or dramatic lighting.

        **Specific Guidelines:**

        *   **Epic Scale:** Emphasize the vast scope and grandeur of the story through visual elements.
        *   **Atmosphere:** Create a sense of wonder, mystery, or danger.
        *   **Character Focus:** Highlight the main characters and their roles in the story.
        *   **Genre Conventions:** Adhere to common visual conventions of Epic Fantasy (e.g., swords, castles, dragons).
        *   **Target Audience:** Appeal to readers who enjoy visually stunning and immersive artwork.

        **Examples of Visual Styles:**

        *   **High Fantasy:** Lush landscapes, heroic figures, vibrant colors.
        *   **Grimdark:** Dark and gritty imagery, muted colors, realistic details.
        *   **Sword and Sorcery:** Action-packed scenes, powerful warriors, magical artifacts.

        **Additional Information (if available):**

        *   Title: {kwargs.get("title", "[Title]")}
        *   Setting: {kwargs.get("setting", "[Setting]")}
        *   Main Characters: {kwargs.get("main_characters", "[Main Characters]")}
        *   Overall Tone: {kwargs.get("overall_tone", "[Overall Tone]")}
        """
        return prompt
        ```
        epicfantasy_book_additions = """

## EpicFantasy Series Book Integration

### EpicFantasy Continuity for This Book
- **Genre Consistency**: Maintain established epicfantasy elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to epicfantasy
- **Plot Advancement**: Continue series plot threads while telling a complete epicfantasy story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill epicfantasy reader expectations while advancing the series narrative

### Book-Specific EpicFantasy Focus
- **Central Conflict**: What epicfantasy-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new epicfantasy elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent epicfantasy while serving the series?

Ensure this book feels like an authentic continuation of the epicfantasy series while telling a complete, satisfying story.
"""

        return base_prompt + epicfantasy_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_series_book_prompt(**kwargs)
