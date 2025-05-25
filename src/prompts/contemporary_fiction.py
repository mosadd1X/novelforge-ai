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

        ```python
        class ContemporaryFictionMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions for Contemporary Fiction novels.

        Args:
        **kwargs: Keyword arguments that can be used to pass specific book details (e.g., title, author, protagonist, setting, themes, target audience).

        Returns:
        str: A detailed prompt string tailored for generating Contemporary Fiction back cover copy.
        """

        prompt = f"""
        Write a compelling back cover description for a Contemporary Fiction novel. Consider the following elements:

        Genre: Contemporary Fiction

        Core Elements to Emphasize:
        *   **Relatability:** Highlight themes and situations that resonate with modern readers' experiences, struggles, and aspirations. Focus on authentic emotions and realistic characters.
        *   **Character-Driven Narrative:** Emphasize the protagonist's internal journey, their flaws, and their growth throughout the story. Show their vulnerability and resilience.
        *   **Exploration of Modern Issues:** Address relevant social, cultural, or political issues that impact contemporary society. Do so in a nuanced and thought-provoking way.
        *   **Emotional Impact:** Evoke a strong emotional response in the reader. Aim for empathy, hope, heartbreak, or a sense of catharsis.
        *   **Setting as a Character:** If the setting is significant, showcase how it influences the characters and the plot.

        Key Questions to Answer (without revealing major spoilers):
        *   Who is the protagonist, and what are their defining characteristics? What are their desires, fears, and motivations?
        *   What is the central conflict or challenge they face?
        *   What are the stakes involved? What will they lose or gain if they succeed or fail?
        *   What are the major themes explored in the story (e.g., love, loss, identity, family, social justice, mental health)?
        *   What makes this story unique and memorable?

        Writing Style Guidelines:
        *   Use evocative language and vivid imagery to paint a picture of the story's world and characters.
        *   Create a sense of intrigue and suspense to hook the reader.
        *   Avoid clichés and strive for originality in your phrasing.
        *   Keep the tone consistent with the overall mood of the novel (e.g., heartwarming, suspenseful, humorous, poignant).
        *   Write in the present tense to create a sense of immediacy.
        *   End with a compelling hook or question that leaves the reader wanting more.

        Specific Details (replace with actual book details):
        *   Title: {kwargs.get('title', '[Title of the Book]')}
        *   Author: {kwargs.get('author', '[Author Name]')}
        *   Protagonist: {kwargs.get('protagonist', '[Protagonist Name and Brief Description]')}
        *   Setting: {kwargs.get('setting', '[Brief Description of the Setting]')}
        *   Themes: {kwargs.get('themes', '[List of Key Themes]')}
        *   Target Audience: {kwargs.get('target_audience', '[Target Audience Description]')}

        Example Structure:
        [Start with a hook that introduces the protagonist and their dilemma.]
        [Briefly describe the central conflict and the stakes involved.]
        [Hint at the major themes explored in the story.]
        [End with a compelling question or statement that leaves the reader wanting to know what happens next.]

        Remember to keep the description concise and engaging. Aim for a word count of around 150-200 words.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, impactful description (2-3 lines) for book recommendations in the Contemporary Fiction genre.

        Args:
        **kwargs: Keyword arguments that can be used to pass specific book details (e.g., title, author, protagonist, central theme).

        Returns:
        str: A prompt string designed to create a concise and attention-grabbing description.
        """

        prompt = f"""
        Write a very short (2-3 lines) description for a Contemporary Fiction novel, suitable for a book recommendation. Focus on grabbing the reader's attention quickly.

        Genre: Contemporary Fiction

        Key Elements to Include:
        *   **Intriguing Hook:** Start with a compelling question or statement that immediately piques the reader's interest.
        *   **Central Conflict:** Briefly mention the main challenge or conflict the protagonist faces.
        *   **Emotional Core:** Hint at the emotional impact of the story.
        *   **Unique Selling Point:** What makes this book stand out from other Contemporary Fiction novels?

        Writing Style Guidelines:
        *   Use strong verbs and vivid language.
        *   Keep it concise and to the point.
        *   Focus on the most compelling aspects of the story.
        *   End with a sense of mystery or anticipation.

        Specific Details (replace with actual book details):
        *   Title: {kwargs.get('title', '[Title of the Book]')}
        *   Author: {kwargs.get('author', '[Author Name]')}
        *   Protagonist: {kwargs.get('protagonist', '[Protagonist Name and Brief Description]')}
        *   Central Theme: {kwargs.get('central_theme', '[Main Theme of the Book]')}

        Example:
        "When [Protagonist's Name]'s carefully constructed life crumbles, she must confront a past she thought she'd buried. A poignant exploration of [Central Theme] and the enduring power of hope."

        Focus on creating a description that is both informative and captivating.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy and memorable marketing tagline for a Contemporary Fiction novel.

        Args:
        **kwargs: Keyword arguments that can be used to pass specific book details (e.g., title, central theme, target audience).

        Returns:
        str: A prompt string tailored for generating effective marketing taglines.
        """

        prompt = f"""
        Write a punchy and memorable marketing tagline for a Contemporary Fiction novel.

        Genre: Contemporary Fiction

        Key Elements to Consider:
        *   **Target Audience:** Who is this book for? Tailor the tagline to resonate with their interests and values.
        *   **Central Theme:** What is the main message or idea the book explores?
        *   **Emotional Impact:** What feeling should the tagline evoke in the reader?
        *   **Uniqueness:** What makes this book different from other Contemporary Fiction novels?

        Tagline Characteristics:
        *   Short and catchy
        *   Memorable and impactful
        *   Intriguing and thought-provoking
        *   Relevant to the story's core themes
        *   Reflects the tone and style of the book

        Specific Details (replace with actual book details):
        *   Title: {kwargs.get('title', '[Title of the Book]')}
        *   Central Theme: {kwargs.get('central_theme', '[Main Theme of the Book]')}
        *   Target Audience: {kwargs.get('target_audience', '[Target Audience Description]')}

        Examples:
        *   "Love. Loss. And the courage to start again."
        *   "Every family has secrets. Some are meant to stay buried."
        *   "Finding yourself is just the beginning of the journey."
        *   "The truth hurts. But silence can kill."

        Brainstorm several taglines and choose the one that best captures the essence of the book.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining visual style preferences for the back cover design of a Contemporary Fiction novel.

        Args:
        **kwargs: Keyword arguments that can be used to pass specific book details (e.g., title, setting, protagonist's personality, overall tone).

        Returns:
        str: A prompt string guiding the creation of visually appealing and genre-appropriate back cover designs.
        """

        prompt = f"""
        Describe the desired visual style for the back cover design of a Contemporary Fiction novel.

        Genre: Contemporary Fiction

        Visual Elements to Consider:
        *   **Imagery:** What kind of images would best represent the story's themes and setting? (e.g., landscapes, cityscapes, portraits, abstract designs) Should the imagery be realistic, stylized, or symbolic?
        *   **Color Palette:** What colors evoke the appropriate mood and atmosphere? (e.g., warm and inviting, cool and melancholic, vibrant and energetic) Consider the emotional associations of different colors.
        *   **Typography:** What font styles would complement the overall design and reflect the tone of the book? (e.g., modern and minimalist, classic and elegant, bold and edgy)
        *   **Layout:** How should the text and images be arranged on the back cover? (e.g., clean and organized, dynamic and asymmetrical, minimalist)
        *   **Overall Tone:** What feeling should the back cover design convey? (e.g., hopeful, mysterious, emotional, thought-provoking)

        Specific Considerations for Contemporary Fiction:
        *   **Authenticity:** Aim for a design that feels genuine and relatable. Avoid overly polished or artificial imagery.
        *   **Modernity:** Reflect the contemporary setting and themes of the story.
        *   **Emotional Connection:** Evoke a sense of empathy and connection with the characters and their experiences.
        *   **Subtlety:** Avoid being too literal or heavy-handed. Let the design hint at the story's themes without giving away too much.

        Specific Details (replace with actual book details):
        *   Title: {kwargs.get('title', '[Title of the Book]')}
        *   Setting: {kwargs.get('setting', '[Brief Description of the Setting]')}
        *   Protagonist's Personality: {kwargs.get('protagonist_personality', '[Brief Description of the Protagonist's Personality]')}
        *   Overall Tone: {kwargs.get('overall_tone', '[Overall Tone of the Book]')}

        Example:
        "For a novel set in a bustling modern city about a young woman struggling with identity, I envision a back cover with a slightly blurred cityscape in muted blues and grays. The typography should be clean and modern, with a sans-serif font. The overall tone should be reflective and a little melancholic, hinting at the protagonist's inner turmoil."

        Provide a detailed description of your desired visual style, including specific examples if possible.
        """
        return prompt
        ```
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

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return ContemporaryFictionPrompts.get_series_book_prompt(**kwargs)
