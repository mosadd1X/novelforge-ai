"""
Paranormal Romance genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ParanormalRomancePrompts(FictionBasePrompts):
    GENRE_NAME = "Paranormal Romance"
    GENRE_DESCRIPTION = "Paranormal Romance blends the emotional intensity and relationship focus of romance with elements of the supernatural, fantasy, or science fiction. It features a central love story between two characters, at least one of whom possesses paranormal abilities or belongs to a supernatural species. The paranormal elements are integral to the plot and often create unique challenges and opportunities for the relationship to develop. The genre emphasizes emotional connection, passion, and overcoming obstacles, often exploring themes of acceptance, identity, and the power of love to transcend boundaries."
    
    GENRE_CHARACTERISTICS = [
        "Supernatural or paranormal elements are central to the plot and character identities.",
        "A core romance plot drives the narrative, with a strong emphasis on emotional connection and relationship development.",
        "At least one protagonist possesses supernatural abilities, is a supernatural being (e.g., vampire, werewolf, witch), or has a connection to the paranormal world.",
        "The setting often blends the mundane world with a hidden or parallel supernatural realm.",
        "Conflict arises from the challenges of navigating a relationship between individuals from different worlds or with conflicting natures.",
        "Themes of acceptance, prejudice, and the struggle for identity are frequently explored.",
        "Sensuality and passion are common, often heightened by the supernatural elements.",
        "World-building is crucial, establishing the rules and lore of the paranormal elements.",
        "The narrative often includes elements of danger, suspense, and adventure related to the supernatural world.",
        "Character arcs often involve self-discovery and embracing one's true nature, both human and supernatural."
    ]
    
    TYPICAL_ELEMENTS = [
        "A forbidden love between a human and a supernatural being.",
        "A chosen one destined to save their paranormal community.",
        "A secret society of supernatural creatures living among humans.",
        "A curse that threatens the protagonist's relationship or existence.",
        "A prophecy that dictates the fate of the paranormal world.",
        "A power struggle within a supernatural hierarchy.",
        "A hunt for a powerful artifact or magical object.",
        "A transformation or awakening of supernatural abilities.",
        "A battle against a dark force that threatens both the human and paranormal worlds.",
        "A journey to a hidden or magical location.",
        "A love triangle involving a human and two supernatural beings.",
        "The discovery of a hidden heritage or family connection to the paranormal world."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Writing Considerations
- **Key Aspect 1: World-Building**: Craft a believable and immersive paranormal world with consistent rules, lore, and history. Consider the social structure, customs, and challenges faced by supernatural beings within this world.
- **Key Aspect 2: Character Motivation**: Ensure that both human and supernatural characters have compelling motivations that drive their actions and decisions, especially in relation to their romantic interest. Explore the internal conflicts arising from their different natures and desires.
- **Key Aspect 3: Balancing Romance and Paranormal Elements**: Seamlessly integrate the romance plot with the paranormal elements, ensuring that both aspects are equally compelling and contribute to the overall narrative. Avoid letting one overshadow the other.
- **Key Aspect 4: Sensuality and Intimacy**: Explore the sensuality and intimacy between characters in a way that is both passionate and respectful, considering the unique physical and emotional aspects of their supernatural natures.
- **Key Aspect 5: Conflict and Stakes**: Create high stakes and compelling conflicts that arise from the clash between the human and paranormal worlds, forcing characters to make difficult choices and confront their deepest fears.
- **Key Aspect 6: Emotional Resonance**: Focus on creating emotional resonance with readers by exploring universal themes of love, loss, acceptance, and identity through the lens of the paranormal.
- **Key Aspect 7: Originality**: Strive to create a unique and fresh take on familiar paranormal tropes, avoiding clichés and stereotypes. Develop original supernatural creatures, powers, and world-building elements.
- **Key Aspect 8: Character Growth**: Show how the characters grow and evolve throughout the story as they navigate the challenges of their relationship and embrace their true identities, both human and supernatural.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Outline Requirements
- **Structure Element 1: Introduction of the Paranormal World**: The outline should clearly establish the existence and rules of the paranormal world, introducing key supernatural elements and characters early on.
- **Structure Element 2: Initial Meeting and Attraction**: Detail the initial encounter between the protagonists, highlighting the spark of attraction and the potential challenges arising from their different backgrounds or natures.
- **Structure Element 3: Rising Action - Exploration of Powers and World**: Outline the events that lead to the exploration of the supernatural powers, world, and the deepening connection between the protagonists. Include specific scenes showcasing these elements.
- **Structure Element 4: Conflict and Obstacles**: Identify the major conflicts and obstacles that threaten the relationship, such as prejudice, external threats, or internal struggles related to their identities.
- **Structure Element 5: Climax - Confrontation and Choice**: Outline the climax of the story, where the protagonists face a major confrontation that forces them to make a difficult choice about their relationship and their future.
- **Structure Element 6: Resolution - Acceptance and Future**: Detail the resolution of the conflict, showing how the protagonists overcome the obstacles and find a way to be together, either by embracing their differences or finding a compromise.
- **Structure Element 7: World-Building Integration**: Ensure that the outline integrates the world-building elements throughout the story, using them to create tension, drive the plot, and enhance the emotional impact of the romance.
- **Structure Element 8: Character Arc Emphasis**: The outline should emphasize the character arcs of both protagonists, showing how they grow and evolve as they navigate the challenges of their relationship and embrace their true identities.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Character Development
- **Character Aspect 1: Supernatural Abilities and Limitations**: Clearly define the supernatural abilities of the paranormal character, as well as their limitations and weaknesses. Explore how these abilities impact their personality and relationships.
- **Character Aspect 2: Internal Conflict and Identity**: Explore the internal conflict of the paranormal character, particularly if they struggle with their identity or feel torn between two worlds. How does their supernatural nature affect their sense of self?
- **Character Aspect 3: Vulnerability and Emotional Depth**: Despite their supernatural powers, ensure that the paranormal character is vulnerable and possesses emotional depth. Show their fears, insecurities, and desires.
- **Character Aspect 4: Human Character's Reaction to the Paranormal**: Develop the human character's reaction to the paranormal world and the supernatural being they are falling in love with. Are they accepting, fearful, or curious? How does this relationship change them?
- **Character Aspect 5: Power Dynamics**: Consider the power dynamics between the human and paranormal characters. How does the supernatural character's power affect the relationship? How does the human character assert their own agency?
- **Character Aspect 6: Shared Goals and Values**: Despite their differences, identify shared goals and values that connect the human and paranormal characters. What do they both want out of life? What are they willing to fight for?
- **Character Aspect 7: Character Growth Through Relationship**: Show how both characters grow and evolve through their relationship. How do they learn from each other? How do they overcome their individual weaknesses?
- **Character Aspect 8: Backstory and Trauma**: Develop a compelling backstory for both characters, including any past traumas that may affect their present-day behavior and relationships.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Chapter Writing
- **Writing Technique 1: Sensory Details and Atmosphere**: Use vivid sensory details to create a compelling atmosphere that immerses the reader in the paranormal world. Describe the sights, sounds, smells, tastes, and textures of the supernatural realm.
- **Writing Technique 2: Show, Don't Tell with Powers**: Instead of simply stating that a character has a certain power, show them using it in a creative and engaging way. Describe the physical sensations and visual effects of their abilities.
- **Writing Technique 3: Dialogue and Banter**: Use dialogue to reveal character personalities, build romantic tension, and explore the differences between the human and paranormal worlds. Include witty banter and meaningful conversations.
- **Writing Technique 4: Pacing and Suspense**: Vary the pacing of the chapter to create suspense and keep the reader engaged. Use cliffhangers and foreshadowing to hint at future events.
- **Writing Technique 5: Emotional Intensity**: Focus on creating emotional intensity in key scenes, particularly those involving romantic interactions or moments of conflict. Use evocative language and imagery to convey the characters' feelings.
- **Writing Technique 6: Integration of Paranormal Elements**: Seamlessly integrate the paranormal elements into the chapter, ensuring that they are not just window dressing but an integral part of the plot and character development.
- **Writing Technique 7: Balancing Action and Romance**: Strike a balance between action-packed scenes and romantic moments, ensuring that both aspects are equally compelling and contribute to the overall narrative.
- **Writing Technique 8: Character Development Through Action**: Use action scenes to reveal character traits, test their abilities, and show how they react under pressure.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_enhancement_prompt(**kwargs)

        paranormal_romance_additions = '''
## Paranormal Romance-Specific Enhancement Considerations
- **Enhancement Focus 1: World-Building Consistency**: Ensure that the enhanced text maintains consistency with the established rules and lore of the paranormal world. Check for any contradictions or inconsistencies in the world-building.
- **Enhancement Focus 2: Character Voice and Motivation**: Verify that the enhanced text accurately reflects the characters' voices and motivations, particularly in relation to their supernatural natures and romantic interests.
- **Enhancement Focus 3: Emotional Impact and Resonance**: Enhance the emotional impact of the text by adding more vivid sensory details, evocative language, and poignant moments of connection between the characters.
- **Enhancement Focus 4: Pacing and Suspense**: Improve the pacing of the text by adding more suspenseful elements, cliffhangers, and foreshadowing to keep the reader engaged.
- **Enhancement Focus 5: Dialogue and Banter**: Enhance the dialogue by adding more witty banter, meaningful conversations, and character-revealing exchanges between the protagonists.
- **Enhancement Focus 6: Supernatural Element Integration**: Ensure that the enhanced text seamlessly integrates the supernatural elements into the plot and character development, avoiding any jarring or unnatural transitions.
- **Enhancement Focus 7: Sensuality and Intimacy**: Enhance the sensuality and intimacy of the text by adding more descriptive details and emotional depth to the romantic interactions between the characters.
'''
        return base_prompt + paranormal_romance_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a paranormalromance-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        paranormalromance_series_additions = """

## ParanormalRomance Series-Specific Planning Elements

### Genre-Specific Series Development
- **ParanormalRomance Conventions**: Ensure each book fulfills paranormalromance reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to paranormalromance
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to paranormalromance
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore paranormalromance themes with increasing depth and complexity

### ParanormalRomance Series Continuity
- **Genre Elements**: Maintain consistent paranormalromance elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy paranormalromance readers
- **Series Identity**: Establish a strong series identity that feels authentically paranormalromance
- **World Building**: Develop the story world in ways that enhance the paranormalromance experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the paranormalromance genre

Create a paranormalromance series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + paranormalromance_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a paranormalromance-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        paranormalromance_book_additions = """

## ParanormalRomance Series Book Integration

### ParanormalRomance Continuity for This Book
- **Genre Consistency**: Maintain established paranormalromance elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to paranormalromance
- **Plot Advancement**: Continue series plot threads while telling a complete paranormalromance story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill paranormalromance reader expectations while advancing the series narrative

### Book-Specific ParanormalRomance Focus
- **Central Conflict**: What paranormalromance-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new paranormalromance elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent paranormalromance while serving the series?

Ensure this book feels like an authentic continuation of the paranormalromance series while telling a complete, satisfying story.
"""
        
        return base_prompt + paranormalromance_book_additions

        ```python
        class ParanormalRomanceMarketing:
        """
        A class containing methods for generating prompts for Paranormal Romance back cover copy,
        taglines, short descriptions, and visual style preferences.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling Paranormal Romance back cover descriptions.

        Args:
        **kwargs: Keyword arguments providing book-specific details.

        Returns:
        str: A prompt string tailored for AI content generation.
        """
        prompt = f"""
        Write a captivating back cover description for a Paranormal Romance novel.

        Genre: Paranormal Romance

        Key Elements to Emphasize:
        *   Forbidden Love: Highlight the intense connection between the human and paranormal characters, emphasizing the obstacles and societal pressures they face.
        *   Supernatural Powers/Abilities: Showcase the unique abilities of the paranormal character(s) and how they impact the relationship and the plot.
        *   Worldbuilding: Briefly describe the unique paranormal world and its rules, creating a sense of mystery and intrigue.
        *   Emotional Intensity: Focus on the deep emotions, passion, and vulnerability between the characters.  Readers want to *feel* the connection.
        *   High Stakes: Emphasize the dangers and challenges the characters face, both from external threats and internal conflicts.  What will they risk for love?
        *   Transformation/Growth: Show how the relationship changes the characters, leading to personal growth and self-discovery.
        *   Intrigue and Suspense: Tease the central conflict or mystery that drives the plot, leaving the reader wanting more.
        *   Strong Female Lead (if applicable): Highlight the heroine's strength, independence, and resilience.

        Specific Details (Use these to tailor the description):
        *   Title: {kwargs.get('title', '[Book Title]')}
        *   Heroine Name: {kwargs.get('heroine_name', '[Heroine Name]')}
        *   Hero Name: {kwargs.get('hero_name', '[Hero Name]')}
        *   Paranormal Creature Type (e.g., Vampire, Werewolf, Fae, Witch): {kwargs.get('paranormal_creature', '[Paranormal Creature]')}
        *   Brief Plot Summary: {kwargs.get('plot_summary', '[Brief Plot Summary]')}
        *   Central Conflict/Mystery: {kwargs.get('conflict', '[Central Conflict]')}
        *   Setting (Time Period and Location): {kwargs.get('setting', '[Setting]')}
        *   Key Themes: {kwargs.get('themes', '[Themes, e.g., destiny, sacrifice, acceptance]')}
        *   Tone (e.g., Dark, Romantic, Humorous): {kwargs.get('tone', '[Tone]')}

        Instructions:
        1.  Start with a hook that immediately grabs the reader's attention and introduces the heroine and/or hero.
        2.  Briefly introduce the paranormal element and the central conflict.
        3.  Highlight the forbidden romance and the emotional connection between the characters.
        4.  Tease the high stakes and the potential consequences of their relationship.
        5.  End with a cliffhanger or a question that leaves the reader wanting to know what happens next.
        6.  Use evocative language and imagery to create a sense of atmosphere and emotion.
        7.  Keep the description concise and engaging (approximately 150-200 words).
        8.  Avoid spoilers.
        9.  Mention any unique aspects of the paranormal world or the characters' abilities.
        10. Focus on the emotional journey of the characters and the power of love to overcome obstacles.

        Example Opening Lines (Feel free to adapt or use as inspiration):
        *   "She never believed in vampires... until she met him."
        *   "In a world where magic is forbidden, their love is the most dangerous spell of all."
        *   "He was a creature of the night, bound by duty, until she awakened his heart."

        Write the back cover description now.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short (2-3 line) book recommendation description for Paranormal Romance.

        Args:
        **kwargs: Keyword arguments providing book-specific details.

        Returns:
        str: A prompt string tailored for AI content generation.
        """
        prompt = f"""
        Write a short, enticing 2-3 line description of a Paranormal Romance novel for book recommendations.

        Genre: Paranormal Romance

        Key Elements to Emphasize:
        *   Forbidden love between a human and a paranormal being.
        *   Unique paranormal elements and worldbuilding.
        *   Intense emotions and passionate connection.
        *   High stakes and potential danger.

        Specific Details (Use these to tailor the description):
        *   Title: {kwargs.get('title', '[Book Title]')}
        *   Heroine Name: {kwargs.get('heroine_name', '[Heroine Name]')}
        *   Hero Name: {kwargs.get('hero_name', '[Hero Name]')}
        *   Paranormal Creature Type: {kwargs.get('paranormal_creature', '[Paranormal Creature]')}
        *   Brief Plot Summary: {kwargs.get('plot_summary', '[Brief Plot Summary]')}

        Instructions:
        1.  Focus on creating intrigue and capturing the essence of the story in a concise way.
        2.  Highlight the unique aspects of the paranormal romance.
        3.  Use strong, evocative language.
        4.  End with a hook that makes the reader want to learn more.

        Example:
        "When a mortal woman stumbles into a world of ancient vampires, she finds herself drawn to a dark and dangerous lord. But their love could ignite a war that destroys them both."

        Write the short description now.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a Paranormal Romance novel.

        Args:
        **kwargs: Keyword arguments providing book-specific details.

        Returns:
        str: A prompt string tailored for AI content generation.
        """
        prompt = f"""
        Write a captivating marketing tagline for a Paranormal Romance novel.

        Genre: Paranormal Romance

        Key Elements to Emphasize:
        *   Forbidden love and desire.
        *   The clash between two worlds (human and paranormal).
        *   Intense emotions and passion.
        *   Danger and high stakes.
        *   The power of love to overcome obstacles.

        Specific Details (Use these to tailor the tagline):
        *   Title: {kwargs.get('title', '[Book Title]')}
        *   Heroine Name: {kwargs.get('heroine_name', '[Heroine Name]')}
        *   Hero Name: {kwargs.get('hero_name', '[Hero Name]')}
        *   Paranormal Creature Type: {kwargs.get('paranormal_creature', '[Paranormal Creature]')}
        *   Central Conflict: {kwargs.get('conflict', '[Central Conflict]')}
        *   Key Themes: {kwargs.get('themes', '[Themes, e.g., destiny, sacrifice, acceptance]')}

        Instructions:
        1.  Keep the tagline short, memorable, and impactful (ideally under 10 words).
        2.  Focus on the core conflict or theme of the story.
        3.  Use strong verbs and evocative language.
        4.  Create a sense of mystery and intrigue.
        5.  Consider using a question or a play on words.

        Example Taglines:
        *   "Love is a dangerous game when your heart belongs to a vampire."
        *   "Their love could break the curse... or destroy the world."
        *   "He's a monster. She's his obsession."

        Write the marketing tagline now.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining visual style preferences for a Paranormal Romance book cover.

        Args:
        **kwargs: Keyword arguments providing book-specific details.

        Returns:
        str: A prompt string tailored for AI content generation.
        """
        prompt = f"""
        Describe the visual style preferences for a Paranormal Romance book cover.

        Genre: Paranormal Romance

        Key Visual Elements to Consider:
        *   Imagery: What kind of imagery would best represent the story? (e.g., a couple embracing, a lone figure in a mystical setting, a close-up of a paranormal creature, symbolic elements like a moon, stars, or ancient artifacts)
        *   Color Palette: What colors evoke the mood and atmosphere of the story? (e.g., dark and moody colors for a gothic romance, vibrant and ethereal colors for a fae romance, warm and passionate colors for a werewolf romance)
        *   Typography: What font styles would be appropriate for the title and author name? (e.g., elegant and flowing fonts for a romantic feel, bold and dramatic fonts for a darker tone, handwritten fonts for a more personal touch)
        *   Overall Mood: What is the overall mood you want to convey? (e.g., romantic, mysterious, sensual, dangerous, suspenseful)

        Specific Details (Use these to tailor the visual style):
        *   Title: {kwargs.get('title', '[Book Title]')}
        *   Heroine Appearance: {kwargs.get('heroine_appearance', '[Heroine Appearance Description]')}
        *   Hero Appearance: {kwargs.get('hero_appearance', '[Hero Appearance Description]')}
        *   Paranormal Creature Type: {kwargs.get('paranormal_creature', '[Paranormal Creature]')}
        *   Setting: {kwargs.get('setting', '[Setting Description]')}
        *   Tone: {kwargs.get('tone', '[Tone, e.g., Dark, Romantic, Humorous]')}
        *   Target Audience: {kwargs.get('target_audience', '[Target Audience Description]')}
        *   Specific Cover Art Examples (Optional): {kwargs.get('cover_examples', '[Examples of similar covers you like]')}

        Instructions:
        1.  Provide a detailed description of the desired imagery, color palette, typography, and overall mood.
        2.  Consider the target audience and what kind of cover art would appeal to them.
        3.  Think about the key themes and elements of the story and how they can be visually represented.
        4.  Be specific and provide as much detail as possible to help the AI generate a cover that accurately reflects your vision.
        5.  If you have any specific cover art examples that you like, include them for reference.
        6.  Consider the use of silhouettes, textures, and lighting to create a visually appealing and memorable cover.
        7.  Think about the composition of the cover and how the different elements will be arranged.

        Describe the desired visual style for the book cover now.
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_series_book_prompt(**kwargs)
