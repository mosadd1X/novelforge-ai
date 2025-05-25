"""
Urban Fantasy genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class UrbanFantasyPrompts(FictionBasePrompts):
    GENRE_NAME = "Urban Fantasy"
    GENRE_DESCRIPTION = "Urban Fantasy is a subgenre of fantasy characterized by its setting in an urban environment. It typically features supernatural elements such as magic, mythical creatures, and paranormal phenomena existing alongside and often hidden within the mundane reality of a city. The genre often explores themes of identity, power, and the clash between the ordinary and the extraordinary."
    
    GENRE_CHARACTERISTICS = [
        "A contemporary urban setting, often a recognizable city like New York, London, or Tokyo, but sometimes a fictional city with a similar feel.",
        "The presence of magic, supernatural creatures (vampires, werewolves, fae, etc.), or other paranormal phenomena that are not widely known or accepted by the general public.",
        "A protagonist who is often caught between the mundane world and the supernatural one, possessing unique abilities or knowledge that allows them to navigate both.",
        "A strong sense of mystery and intrigue, often involving investigations into supernatural crimes or conspiracies.",
        "Exploration of the hidden or secret societies that operate within the urban environment, often with their own rules, hierarchies, and agendas.",
        "A blend of fantasy elements with aspects of other genres, such as crime fiction, thriller, romance, or horror.",
        "Themes of identity, alienation, and the struggle to find one's place in a world where the ordinary and the extraordinary collide.",
        "A focus on the impact of magic and the supernatural on everyday life, exploring how these elements affect social structures, relationships, and personal experiences.",
        "Moral ambiguity and complex characters, where the lines between good and evil are often blurred.",
        "A fast-paced plot with action sequences and suspenseful moments, reflecting the energy and dynamism of the urban setting."
    ]
    
    TYPICAL_ELEMENTS = [
        "A protagonist with hidden magical abilities or a connection to the supernatural world.",
        "A secret society or organization that governs the supernatural community.",
        "A magical artifact or object of power that is sought after by various factions.",
        "A hidden portal or gateway to another realm or dimension.",
        "A supernatural creature (vampire, werewolf, fae, demon, etc.) as a major character or antagonist.",
        "A magical curse or enchantment that affects the protagonist or the city itself.",
        "A detective or investigator who specializes in supernatural crimes.",
        "A mentor figure who guides the protagonist in their understanding and use of magic.",
        "A romantic relationship between a human and a supernatural being.",
        "A conspiracy involving powerful individuals or organizations seeking to control the supernatural world.",
        "A magical duel or battle between opposing factions.",
        "A hidden magical location or sanctuary within the city."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Writing Considerations
- **Worldbuilding**: Focus on creating a believable urban environment where the supernatural can plausibly exist in secret. Consider the history of magic in the city, the rules governing its use, and the impact it has on the mundane world.
- **Character Development**: Develop characters with compelling motivations and flaws, who are believable both as individuals and as members of their respective communities (human or supernatural). Explore their internal conflicts and how they navigate the challenges of living in a world where the ordinary and the extraordinary collide.
- **Plot and Pacing**: Craft a plot that is both engaging and suspenseful, with a clear sense of direction and escalating stakes. Maintain a fast pace that reflects the energy of the urban setting, while also allowing for moments of character development and worldbuilding.
- **Magic System**: Define a clear and consistent magic system with its own rules, limitations, and consequences. Avoid deus ex machina solutions and ensure that magic is used in a way that is both believable and integral to the plot.
- **Tone and Atmosphere**: Establish a consistent tone that balances the fantastical elements with the gritty realism of the urban setting. Create an atmosphere that is both mysterious and intriguing, with a sense of danger lurking beneath the surface.
- **Thematic Resonance**: Explore themes that are relevant to the urban fantasy genre, such as identity, power, alienation, and the struggle to find one's place in the world. Use the supernatural elements to comment on social issues and explore the human condition.
- **Research**: Thoroughly research the urban environment you are writing about, paying attention to its history, culture, and social dynamics. This will help you create a more believable and immersive setting for your story.
- **Subverting Tropes**: Be aware of common urban fantasy tropes and consider ways to subvert or subvert them to create a fresh and original story.
'''
        return base_prompt + urban_fantasy_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Outline Requirements
- **Inciting Incident**: The inciting incident should introduce the protagonist to the supernatural world or a specific problem within it. This could be a magical attack, the discovery of a hidden artifact, or a request for help from a supernatural being.
- **Rising Action**: The rising action should involve the protagonist investigating the supernatural problem, learning about the rules and factions of the supernatural world, and developing their own abilities or knowledge. Include encounters with supernatural creatures, clues that lead to further mysteries, and escalating conflicts with antagonists.
- **Midpoint**: The midpoint should be a major turning point in the story, where the protagonist gains a significant piece of information or experiences a major setback that changes their understanding of the situation. This could be the revelation of a hidden conspiracy, the loss of a key ally, or a betrayal by someone they trusted.
- **Climax**: The climax should be a confrontation between the protagonist and the main antagonist, where they must use their abilities and knowledge to overcome the supernatural threat. This could involve a magical duel, a battle against a horde of supernatural creatures, or a race against time to prevent a catastrophic event.
- **Falling Action**: The falling action should resolve the immediate conflict and address any remaining loose ends. This could involve cleaning up the aftermath of the climax, dealing with the consequences of the protagonist's actions, and setting the stage for future stories.
- **Resolution**: The resolution should provide a sense of closure and leave the reader with a feeling of satisfaction. This could involve the protagonist finding a new purpose in the supernatural world, forging lasting relationships with other characters, or achieving a personal transformation.
- **Worldbuilding Notes**: Include specific notes about the urban setting, the magic system, the supernatural creatures, and the various factions that operate within the story. These notes should be detailed and consistent, providing a solid foundation for the story's worldbuilding.
- **Character Arcs**: Outline the major character arcs for the protagonist and other key characters, focusing on their personal growth and development throughout the story. Consider how their experiences in the supernatural world change them as individuals.
- **Thematic Elements**: Identify the key thematic elements that you want to explore in your story, such as identity, power, alienation, or the clash between the ordinary and the extraordinary. Ensure that these themes are woven throughout the plot and character development.
'''
        return base_prompt + urban_fantasy_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Character Development
- **Dual Identity**: Consider how the character navigates the dual existence between the mundane world and the supernatural one. Do they keep their supernatural life a secret? How does this affect their relationships and daily routines?
- **Magical Abilities**: Define the character's magical abilities or connection to the supernatural world. What are their strengths and weaknesses? How did they acquire these abilities? What are the limitations or consequences of using them?
- **Moral Alignment**: Explore the character's moral compass and how it is influenced by their experiences in the supernatural world. Are they a hero, a villain, or something in between? What are their motivations and goals?
- **Backstory**: Develop a detailed backstory that explains the character's origins, motivations, and relationships. How did their past experiences shape them into the person they are today? What secrets are they hiding?
- **Relationships**: Consider the character's relationships with other characters, both human and supernatural. Who are their allies and enemies? How do these relationships affect their decisions and actions?
- **Internal Conflicts**: Explore the character's internal conflicts and struggles. Are they grappling with their identity, their powers, or their place in the world? How do they overcome these challenges?
- **Appearance and Demeanor**: Describe the character's physical appearance and demeanor, paying attention to details that reflect their personality and background. Do they dress in a way that blends in with the mundane world, or do they embrace their supernatural identity?
- **Character Arc**: Outline the character's arc throughout the story, focusing on their personal growth and development. How do their experiences in the supernatural world change them as individuals? What lessons do they learn?
'''
        return base_prompt + urban_fantasy_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Chapter Writing
- **Setting the Scene**: Begin each chapter by establishing the setting and atmosphere, immersing the reader in the urban environment and hinting at the presence of the supernatural. Use vivid descriptions to bring the city to life and create a sense of mystery and intrigue.
- **Pacing and Suspense**: Maintain a fast pace that reflects the energy of the urban setting, while also building suspense and anticipation. Use cliffhangers and plot twists to keep the reader engaged and eager to find out what happens next.
- **Character Interactions**: Focus on the interactions between characters, both human and supernatural. Use dialogue and body language to reveal their personalities, motivations, and relationships.
- **Magic and Supernatural Elements**: Integrate magic and supernatural elements seamlessly into the narrative, ensuring that they are consistent with the established rules and limitations of the magic system. Avoid deus ex machina solutions and use magic in a way that is both believable and integral to the plot.
- **Worldbuilding Details**: Weave in worldbuilding details throughout the chapter, providing glimpses into the history, culture, and social dynamics of the supernatural world. Avoid info dumps and instead reveal information gradually through dialogue, action, and description.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show the reader what is happening, rather than simply telling them. This will help to create a more immersive and engaging reading experience.
- **Conflict and Tension**: Introduce conflict and tension into each chapter, whether it is a physical confrontation, a verbal argument, or an internal struggle. This will help to keep the reader invested in the story and create a sense of urgency.
- **Ending with a Hook**: End each chapter with a hook that leaves the reader wanting more. This could be a cliffhanger, a plot twist, or a lingering question that will be answered in the next chapter.
'''
        return base_prompt + urban_fantasy_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a urbanfantasy-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        urbanfantasy_series_additions = """

## UrbanFantasy Series-Specific Planning Elements

### Genre-Specific Series Development
- **UrbanFantasy Conventions**: Ensure each book fulfills urbanfantasy reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to urbanfantasy
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to urbanfantasy
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore urbanfantasy themes with increasing depth and complexity

### UrbanFantasy Series Continuity
- **Genre Elements**: Maintain consistent urbanfantasy elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy urbanfantasy readers
- **Series Identity**: Establish a strong series identity that feels authentically urbanfantasy
- **World Building**: Develop the story world in ways that enhance the urbanfantasy experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the urbanfantasy genre

Create a urbanfantasy series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + urbanfantasy_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a urbanfantasy-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class UrbanFantasyBackCover:
        """
        A class containing methods for generating prompts to create compelling back cover copy
        and visual style guidelines for Urban Fantasy novels.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for crafting a captivating back cover description for an Urban Fantasy novel.

        Args:
        **kwargs: Keyword arguments providing details about the book, including:
        - protagonist: The protagonist's name, occupation, and key personality traits.
        - setting: The specific urban setting of the story.
        - magical_element: The type of magic system or supernatural creatures involved.
        - central_conflict: The main conflict or problem the protagonist faces.
        - stakes: What the protagonist stands to lose if they fail.
        - tone: The overall tone of the book (e.g., gritty, humorous, romantic).
        - target_audience: Who the book is targeted toward (e.g., YA, adult).
        - themes: Key themes explored in the novel (e.g., identity, prejudice, power).
        - unique_selling_points: Unique aspects of the book that set it apart.

        Returns:
        A string containing a detailed prompt for generating the back cover description.
        """
        return f"""
        Craft a compelling back cover description for an Urban Fantasy novel.

        **Genre:** Urban Fantasy

        **Core Elements to Emphasize:**

        *   **Urban Setting:** Highlight the gritty realism of the city and how it juxtaposes with the magical elements.  Mention specific landmarks or neighborhoods. The city *is* a character.
        *   **Hidden World:**  Emphasize the secret magical world hidden beneath the surface of everyday life.  What kind of creatures lurk in the shadows? How does magic manifest in this urban landscape?
        *   **Protagonist's Journey:** Focus on the protagonist's transformation as they navigate both the mundane and magical worlds. Are they reluctant heroes? Are they embracing their powers?  What personal struggles do they face?
        *   **Conflict and Stakes:** Clearly define the central conflict and the high stakes involved. What will happen if the protagonist fails? What are the personal costs of victory?
        *   **Emotional Hook:**  Tap into the emotional core of the story. Is it about love, loss, betrayal, or redemption? What emotions will resonate with the reader?
        *   **Unique Twist:** Highlight any unique elements that set this book apart from other Urban Fantasy novels.

        **Specific Details (Use the following information to weave a compelling narrative):**

        *   **Protagonist:** {kwargs.get('protagonist', '[Protagonist Name]')} - A {kwargs.get('protagonist_occupation', '[Occupation]')} grappling with {kwargs.get('protagonist_personality', '[Personality Traits]')} and discovering {kwargs.get('protagonist_discovery', 'a hidden power/truth')}.
        *   **Setting:** {kwargs.get('setting', '[City Name]')} - A vibrant city teeming with secrets, where {kwargs.get('setting_details', '[Specific details about the urban environment and its magical elements]')}.
        *   **Magical Element:** {kwargs.get('magical_element', '[Type of magic/supernatural creatures]')} - Magic manifests as {kwargs.get('magic_manifestation', '[How magic appears and works in the world]')}.
        *   **Central Conflict:** {kwargs.get('central_conflict', '[Briefly describe the main conflict]')} - {kwargs.get('conflict_details', '[Expand on the conflict and its implications]')}.
        *   **Stakes:** {kwargs.get('stakes', '[What the protagonist stands to lose]')} - Failure means {kwargs.get('failure_consequences', '[Consequences of failure]')}.
        *   **Tone:** {kwargs.get('tone', '[Overall tone of the book, e.g., gritty, humorous, romantic]')} - The story blends {kwargs.get('tone_elements', '[Elements that contribute to the tone]')}.
        *   **Target Audience:** {kwargs.get('target_audience', '[Target audience, e.g., YA, adult]')} - Readers who enjoy {kwargs.get('similar_books', '[Similar books or authors]')} will love this.
        *   **Themes:** Explores themes of {kwargs.get('themes', '[List of key themes, e.g., identity, prejudice, power]')} - and how they manifest in a world where magic and reality collide.
        *   **Unique Selling Points:** {kwargs.get('unique_selling_points', '[Unique aspects of the book, e.g., a new take on a classic myth, a unique magic system]')} - Making this a must-read for Urban Fantasy fans.

        **Instructions:**

        1.  Start with a hook that grabs the reader's attention.
        2.  Introduce the protagonist and their world in a compelling way.
        3.  Clearly outline the central conflict and the stakes involved.
        4.  Hint at the emotional journey the protagonist will undertake.
        5.  End with a question or a cliffhanger that leaves the reader wanting more.
        6.  Keep the description concise and engaging (around 150-200 words).
        7.  Use strong verbs and vivid imagery to bring the story to life.
        8.  Emphasize the Urban Fantasy elements: the blend of the mundane and the magical.
        9. Focus on the character and their growth.
        """

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, attention-grabbing description for book recommendations.

        Args:
        **kwargs: Keyword arguments providing details about the book, including:
        - protagonist: The protagonist's key characteristic.
        - setting: The most striking aspect of the urban setting.
        - magical_element: The most unique element of the magic system.
        - conflict: The core problem the protagonist faces.

        Returns:
        A string containing a detailed prompt for generating the short description.
        """
        return f"""
        Craft a short (2-3 sentence) description for an Urban Fantasy novel, suitable for book recommendations.

        **Genre:** Urban Fantasy

        **Focus:**

        *   Highlight the most intriguing aspects of the protagonist, setting, and magical elements.
        *   Clearly state the central conflict in a concise and compelling way.
        *   Use strong verbs and evocative language to capture the essence of the story.
        *   Focus on what makes this book UNIQUE.

        **Specific Details:**

        *   **Protagonist:** {kwargs.get('protagonist', '[Protagonist Name]')} - A {kwargs.get('protagonist_characteristic', '[Key characteristic]')}
        *   **Setting:** {kwargs.get('setting', '[City Name]')} - Known for its {kwargs.get('setting_characteristic', '[Striking aspect of the setting]')}
        *   **Magical Element:** {kwargs.get('magical_element', '[Type of magic/supernatural creatures]')} - With the unique element of {kwargs.get('magic_unique', '[Unique element of the magic system]')}
        *   **Conflict:** Faces the conflict of {kwargs.get('conflict', '[Core problem the protagonist faces]')}

        **Example:**

        "In the neon-drenched streets of Neo-Tokyo, a cynical hacker discovers she's the last line of defense against a digital demon threatening to consume the city.  She must master her newfound powers before the virtual and real worlds collide."
        """

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy, memorable marketing tagline for an Urban Fantasy novel.

        Args:
        **kwargs: Keyword arguments providing details about the book's core elements.
        - protagonist: The most compelling aspect of the protagonist.
        - magical_element: A keyword representing the type of magic.
        - setting: A keyword representing the urban setting.
        - conflict: A keyword representing the central conflict.

        Returns:
        A string containing a detailed prompt for generating the marketing tagline.
        """
        return f"""
        Craft a punchy and memorable marketing tagline for an Urban Fantasy novel.

        **Genre:** Urban Fantasy

        **Key Considerations:**

        *   Keep it short, impactful, and easy to remember.
        *   Highlight the core elements of the story: protagonist, setting, magic, and conflict.
        *   Use evocative language and imagery to create a sense of mystery and intrigue.
        *   Focus on the unique selling point of the book.
        *   Target the emotions of the reader.

        **Specific Details:**

        *   **Protagonist:** {kwargs.get('protagonist', '[Compelling aspect of the protagonist]')}
        *   **Magical Element:** {kwargs.get('magical_element', '[Keyword representing the type of magic]')}
        *   **Setting:** {kwargs.get('setting', '[Keyword representing the urban setting]')}
        *   **Conflict:** {kwargs.get('conflict', '[Keyword representing the central conflict]')}

        **Examples:**

        *   "Magic hides in plain sight. The city will never be the same."
        *   "When darkness rises, only one can see."
        *   "Urban legends are about to become reality."
        """

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining the visual style preferences for the back cover design of an Urban Fantasy novel.

        Args:
        **kwargs: Keyword arguments providing details about the book's tone, setting, and magical elements.
        - tone: The overall tone of the book (e.g., gritty, dark, romantic).
        - setting: Key visual elements of the urban setting.
        - magical_element: Visual representations of the magic or supernatural creatures.
        - protagonist: Visual representation of the protagonist.

        Returns:
        A string containing a detailed prompt for generating the visual style preferences.
        """
        return f"""
        Define the visual style preferences for the back cover design of an Urban Fantasy novel.

        **Genre:** Urban Fantasy

        **Key Considerations:**

        *   Reflect the overall tone of the book (gritty, dark, romantic, etc.).
        *   Capture the essence of the urban setting.
        *   Visually represent the magic or supernatural elements in a compelling way.
        *   Consider the target audience and their preferences.
        *   Use typography that is both readable and visually appealing.
        *   Utilize color palettes that evoke the desired mood and atmosphere.

        **Specific Details:**

        *   **Tone:** {kwargs.get('tone', '[Overall tone of the book, e.g., gritty, dark, romantic]')} - The visual style should reflect this tone by using {kwargs.get('tone_visuals', '[Visual elements that reflect the tone, e.g., dark colors, sharp contrasts, soft lighting]')}
        *   **Setting:** {kwargs.get('setting', '[Key visual elements of the urban setting, e.g., neon lights, crumbling buildings, graffiti art]')} - Incorporate elements such as {kwargs.get('setting_elements', '[Specific visual elements to include in the design]')}
        *   **Magical Element:** {kwargs.get('magical_element', '[Visual representations of the magic or supernatural creatures, e.g., glowing runes, shadowy figures, ethereal light]')} -  Represented by {kwargs.get('magic_visuals', '[Specific visual representations of the magic]')}
        *   **Protagonist:** {kwargs.get('protagonist', '[Visual representation of the protagonist, e.g., a silhouette, a close-up of their eyes, a full-body shot with magical elements]')} - Should be shown as {kwargs.get('protagonist_visuals', '[Specific visual details of the protagonist’s representation]')}

        **Examples:**

        *   **Gritty Urban Fantasy:** Dark color palette, high contrast, gritty textures, focus on shadows and silhouettes, urban decay elements.
        *   **Romantic Urban Fantasy:** Soft lighting, pastel colors, flowing lines, focus on character expressions and relationships.
        *   **Modern/Tech Urban Fantasy:** Neon lights, futuristic elements, clean lines, digital interfaces, vibrant colors.

        **Overall Style:**  Describe the overall visual aesthetic you are aiming for. Examples: Noir, Cyberpunk, Steampunk, Gothic, Contemporary.
        """
        ```
        urbanfantasy_book_additions = """

## UrbanFantasy Series Book Integration

### UrbanFantasy Continuity for This Book
- **Genre Consistency**: Maintain established urbanfantasy elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to urbanfantasy
- **Plot Advancement**: Continue series plot threads while telling a complete urbanfantasy story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill urbanfantasy reader expectations while advancing the series narrative

### Book-Specific UrbanFantasy Focus
- **Central Conflict**: What urbanfantasy-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new urbanfantasy elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent urbanfantasy while serving the series?

Ensure this book feels like an authentic continuation of the urbanfantasy series while telling a complete, satisfying story.
"""

        return base_prompt + urbanfantasy_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_series_book_prompt(**kwargs)
