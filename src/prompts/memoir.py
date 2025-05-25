"""
Memoir genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class MemoirPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Memoir"
    GENRE_DESCRIPTION = "A memoir is a non-fiction narrative recounting specific events and themes in the author's life. It focuses on a particular aspect, relationship, or time period, offering personal reflections and insights rather than a comprehensive autobiography. The narrative voice is deeply personal and subjective, emphasizing emotional truth and the author's evolving understanding of their experiences."
    
    GENRE_CHARACTERISTICS = [
        "Focus on a specific theme or period: Memoirs typically center around a particular event, relationship, or period in the author's life, rather than attempting to cover their entire biography.",
        "Subjective and personal voice: The narrative is told from the author's unique perspective, emphasizing their feelings, thoughts, and interpretations of events.",
        "Emotional honesty and vulnerability: Memoirs require the author to be open and honest about their experiences, including their flaws, mistakes, and vulnerabilities.",
        "Reflection and insight: The author reflects on their experiences, drawing meaningful conclusions and insights about themselves, others, and the world.",
        "Strong narrative arc: While based on real events, memoirs should have a compelling narrative structure with a clear beginning, middle, and end.",
        "Vivid sensory details: The author uses descriptive language to bring scenes and characters to life, immersing the reader in their experiences.",
        "Exploration of universal themes: While personal, memoirs often explore universal themes such as love, loss, identity, resilience, and the search for meaning.",
        "Authenticity and truthfulness: While memoirs allow for subjective interpretation, they should be grounded in factual accuracy and a commitment to telling the truth as the author understands it.",
        "Character development: The author, and other key figures, should undergo a clear process of character development throughout the narrative.",
        "Use of flashbacks and reflection: Memoirs often interweave past experiences with present-day reflections to provide context and deeper understanding."
    ]
    
    TYPICAL_ELEMENTS = [
        "A compelling opening scene: Grabs the reader's attention and introduces the central theme or conflict of the memoir.",
        "Clearly defined scope: Establishes the specific focus and boundaries of the narrative.",
        "Vivid descriptions of settings: Creates a strong sense of place and time, immersing the reader in the author's world.",
        "Well-developed characters: Presents the author and other key figures as complex and relatable individuals.",
        "Significant events and turning points: Highlights key moments that shaped the author's life and understanding.",
        "Emotional arc: Tracks the author's emotional journey and transformation throughout the narrative.",
        "Internal monologue and reflections: Reveals the author's thoughts, feelings, and insights.",
        "Dialogue: Brings scenes to life and reveals character relationships.",
        "Use of imagery and metaphor: Enhances the emotional impact and thematic resonance of the narrative.",
        "Exploration of relationships: Examines the author's relationships with family, friends, and others.",
        "A satisfying resolution: Provides closure and offers a sense of hope or understanding.",
        "Thematic coherence: Ensures that all elements of the memoir contribute to the central theme or message."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Writing Considerations
- **Authenticity and Voice**: Develop a unique and authentic voice that reflects your personality and perspective. Prioritize honesty and vulnerability in your writing.
- **Emotional Recall**: Practice techniques for accessing and vividly recreating past emotions and sensations. Use sensory details to bring your experiences to life.
- **Ethical Considerations**: Be mindful of the impact your story may have on others. Consider obtaining consent or changing names to protect privacy.
- **Self-Reflection**: Engage in deep self-reflection to understand the motivations, beliefs, and values that shaped your experiences.
- **Narrative Structure**: Craft a compelling narrative arc with a clear beginning, middle, and end. Use flashbacks and foreshadowing to create suspense and intrigue.
- **Thematic Resonance**: Identify the universal themes that resonate within your personal story. Explore how your experiences connect to broader human experiences.
- **Objectivity vs. Subjectivity**: Strive for a balance between objective reporting of events and subjective interpretation. Acknowledge your biases and limitations.
- **Accuracy and Fact-Checking**: While memoirs prioritize emotional truth, ensure that factual details are as accurate as possible. Verify dates, names, and other relevant information.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Outline Requirements
- **Theme Identification**: Clearly define the central theme or message of your memoir. Ensure that all chapters and scenes contribute to this theme.
- **Chronological vs. Thematic Structure**: Decide whether to structure your memoir chronologically or thematically. Consider the advantages and disadvantages of each approach.
- **Key Events and Turning Points**: Identify the key events and turning points that shaped your life and understanding. Structure your outline around these pivotal moments.
- **Character Arcs**: Map out the character arcs of yourself and other key figures. Show how your relationships and perspectives evolved over time.
- **Emotional Journey**: Outline the emotional journey you experienced throughout the events of your memoir. Identify the highs, lows, and turning points in your emotional arc.
- **Reflection and Insight**: Allocate space in your outline for reflection and insight. Plan where you will interweave your present-day understanding with past experiences.
- **Balancing Act**: Ensure a balance between narrative storytelling, emotional reflection, and thematic exploration.
- **Ethical Considerations**: Outline how you will address any ethical considerations or potential sensitivities in your story.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Character Development
- **Self-Portrait**: Develop a nuanced and honest self-portrait. Explore your strengths, weaknesses, motivations, and flaws.
- **Authenticity**: Strive for authenticity in your portrayal of yourself and others. Avoid idealizing or demonizing characters.
- **Relationship Dynamics**: Explore the dynamics of your relationships with other characters. Show how your interactions shaped your experiences and perspectives.
- **Character Flaws**: Embrace the flaws and imperfections of your characters. These flaws make them relatable and human.
- **Motivation and Intentions**: Understand the motivations and intentions of each character. Explore the reasons behind their actions and decisions.
- **Change and Growth**: Show how characters change and grow throughout the narrative. Highlight the lessons they learned and the transformations they underwent.
- **Perspective**: Consider the perspectives of other characters. Acknowledge that your interpretation of events may differ from theirs.
- **Ethical Considerations**: Be mindful of the impact your portrayal of others may have on their lives. Consider obtaining consent or changing names to protect privacy.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Chapter Writing
- **Scene Setting**: Begin each chapter with a vivid description of the setting. Immerse the reader in the time and place of the events.
- **Emotional Resonance**: Focus on conveying the emotional impact of the events you are describing. Use sensory details and evocative language to create a strong emotional connection with the reader.
- **Internal Monologue**: Incorporate internal monologue to reveal your thoughts, feelings, and reactions to events.
- **Dialogue**: Use dialogue to bring scenes to life and reveal character relationships. Make sure the dialogue sounds authentic and natural.
- **Reflection and Insight**: Interweave reflections and insights throughout the chapter. Connect past experiences to present-day understanding.
- **Pacing**: Vary the pacing of your chapters to create a sense of rhythm and momentum. Use shorter sentences and paragraphs to create a sense of urgency, and longer sentences and paragraphs to create a sense of reflection.
- **Thematic Connection**: Ensure that each chapter contributes to the central theme or message of your memoir.
- **Honesty and Vulnerability**: Write with honesty and vulnerability. Share your fears, doubts, and insecurities with the reader.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a memoir-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        memoir_series_additions = """

## Memoir Series-Specific Planning Elements

### Educational Progression for Memoir
- **Knowledge Building**: Structure learning progression appropriate for memoir topics
- **Expertise Development**: Guide readers from basic to advanced understanding of memoir subjects
- **Practical Applications**: Include actionable insights specific to memoir throughout the series
- **Research Depth**: Plan comprehensive research appropriate for memoir authority
- **Reader Value**: Ensure each book provides significant memoir value while building series knowledge

### Memoir Series Continuity
- **Subject Consistency**: Maintain consistent approach to memoir topics across books
- **Authority Building**: Establish and maintain credibility in memoir throughout the series
- **Information Architecture**: Structure information flow appropriate for memoir learning
- **Cross-References**: Create meaningful connections between memoir concepts across books
- **Updated Knowledge**: Plan for incorporating new memoir research and developments

Create a memoir series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + memoir_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a memoir-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class MemoirMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover copy for a Memoir.

        Args:
        **kwargs:  Optional keyword arguments. Can include:
        - title (str): The title of the memoir.
        - author (str): The author's name.
        - main_theme (str): A brief description of the memoir's central theme.
        - target_audience (str):  Who the memoir is intended for (e.g., readers interested in family dynamics, overcoming adversity).
        - key_events (list): A list of 2-3 significant events or turning points in the memoir.
        - emotional_tone (str): The overall emotional tone of the memoir (e.g., hopeful, poignant, humorous, reflective).
        - comparable_titles (list): A list of 2-3 comparable memoirs.

        Returns:
        str: A detailed prompt for generating back cover copy.
        """
        prompt = f"""
        Write a compelling back cover description for a memoir titled "{kwargs.get('title', '[Title of Memoir]')}" by {kwargs.get('author', '[Author Name]')}.

        Genre: Memoir

        Core elements to emphasize:

        *   **Authenticity and Vulnerability:**  Memoirs thrive on raw honesty and the author's willingness to share deeply personal experiences and emotions.  The reader should feel a connection to the author's humanity.
        *   **Emotional Resonance:**  Highlight the emotional journey of the author.  What challenges did they face? What did they learn?  How did they grow?  Evoke empathy and understanding in the reader.
        *   **Transformation and Growth:**  Memoirs often chronicle a period of significant change or personal transformation.  Focus on the author's arc and the lessons they learned along the way.
        *   **Universal Themes:**  While the story is personal, connect it to broader human experiences and themes such as love, loss, family, identity, resilience, and the search for meaning.
        *   **Specific Details:**  Use vivid and sensory language to bring the author's experiences to life.  Don't be afraid to share specific details that make the story unique and memorable.

        Back Cover Copy Guidelines:

        1.  **Hook:** Start with a captivating hook that immediately grabs the reader's attention. This could be a provocative question, a striking image, or a powerful statement that encapsulates the memoir's central theme.
        2.  **Central Theme:** Clearly state the memoir's main theme and what the author hopes to convey to the reader. {kwargs.get('main_theme', 'Briefly describe the memoir\'s central theme.')}
        3.  **Key Events:** Briefly describe 2-3 significant events or turning points in the author's life that are explored in the memoir. Focus on the emotional impact of these events. {kwargs.get('key_events', 'List 2-3 significant events.')}
        4.  **Emotional Tone:**  Convey the overall emotional tone of the memoir. Is it hopeful, poignant, humorous, or reflective?  Let the reader know what to expect emotionally. {kwargs.get('emotional_tone', 'Describe the emotional tone.')}
        5.  **Target Audience:**  Consider the target audience for the memoir. Who is most likely to be interested in this story? Tailor the language and tone to appeal to that audience. {kwargs.get('target_audience', 'Describe the target audience.')}
        6.  **Author Bio Teaser:** Include a brief, intriguing sentence or two about the author that connects to the memoir's themes.
        7.  **Call to Action:** End with a compelling reason for the reader to pick up the book and start reading.

        Example Sentence Starters (adapt as needed):

        *   "In this unflinchingly honest memoir..."
        *   "A story of resilience, hope, and the power of..."
        *   "With raw vulnerability, [Author Name] shares..."
        *   "A deeply personal exploration of..."
        *   "This is a memoir for anyone who has ever..."

        Comparable Titles:  If possible, subtly reference comparable memoirs to give the reader a sense of what to expect. {kwargs.get('comparable_titles', 'List 2-3 comparable memoirs.')}

        Craft a back cover description that is emotionally resonant, authentic, and ultimately invites the reader to connect with the author's story on a personal level.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short (2-3 line) book recommendation description for a Memoir.

        Args:
        **kwargs: Optional keyword arguments. Can include:
        - title (str): The title of the memoir.
        - author (str): The author's name.
        - main_theme (str): A brief description of the memoir's central theme.
        - emotional_tone (str): The overall emotional tone of the memoir.

        Returns:
        str: A prompt for generating a short book recommendation description.
        """
        prompt = f"""
        Write a short (2-3 lines) book recommendation description for the memoir "{kwargs.get('title', '[Title of Memoir]')}" by {kwargs.get('author', '[Author Name]')}.

        Genre: Memoir

        Focus:

        *   **Emotional Impact:** Emphasize the emotional core of the story. What will readers feel?
        *   **Central Theme:** Briefly highlight the memoir's main theme.
        *   **Authenticity:** Convey the author's vulnerability and honesty.

        Guidelines:

        1.  **Brevity:** Keep it concise and impactful.
        2.  **Emotional Hook:** Use language that evokes emotion and curiosity.
        3.  **Intrigue:** Leave the reader wanting to know more.

        Example:

        "A poignant and unforgettable memoir about [main theme].  [Author Name]'s raw honesty will stay with you long after you finish reading."

        Another example:

        "Prepare to be moved by this powerful story of [main theme].  A testament to the resilience of the human spirit."

        Craft a short description that captures the essence of the memoir and entices readers to pick it up. The emotional tone is {kwargs.get('emotional_tone', 'Describe the emotional tone.')}, and the main theme is {kwargs.get('main_theme', 'Briefly describe the memoir\'s central theme.')}.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a Memoir.

        Args:
        **kwargs: Optional keyword arguments. Can include:
        - title (str): The title of the memoir.
        - main_theme (str): A brief description of the memoir's central theme.
        - emotional_tone (str): The overall emotional tone of the memoir.
        - key_message (str): A single sentence describing the core message of the memoir.

        Returns:
        str: A prompt for generating a marketing tagline.
        """
        prompt = f"""
        Write a punchy marketing tagline for the memoir "{kwargs.get('title', '[Title of Memoir]')}".

        Genre: Memoir

        Tagline Goals:

        *   **Capture the Essence:**  Concisely convey the memoir's main theme or emotional core.
        *   **Evoke Emotion:**  Use language that is evocative and memorable.
        *   **Intrigue and Curiosity:**  Make the reader want to know more.
        *   **Authenticity:**  Reflect the genuine and personal nature of the story.

        Tagline Guidelines:

        1.  **Keep it Short:** Aim for a tagline that is no more than 5-7 words.
        2.  **Focus on Emotion:** Use words that resonate emotionally (e.g., hope, resilience, loss, love, courage).
        3.  **Highlight the Theme:**  Hint at the memoir's central theme without giving too much away.
        4.  **Consider the Tone:** Match the tagline to the overall emotional tone of the memoir (e.g., hopeful, poignant, humorous).

        Example Taglines:

        *   "A story of resilience and hope."
        *   "Finding light in the darkest of times."
        *   "A life lived, lessons learned."
        *   "The courage to tell the truth."
        *   "Where healing begins."

        The memoir's main theme is {kwargs.get('main_theme', 'Briefly describe the memoir\'s central theme.')}, its emotional tone is {kwargs.get('emotional_tone', 'Describe the emotional tone.')}, and its core message is {kwargs.get('key_message', 'Describe the core message of the memoir in one sentence.')}.

        Craft a tagline that is both memorable and reflective of the author's personal journey.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for providing visual style preferences for a Memoir back cover design.

        Args:
        **kwargs: Optional keyword arguments. Can include:
        - main_theme (str): A brief description of the memoir's central theme.
        - emotional_tone (str): The overall emotional tone of the memoir.
        - imagery_suggestions (list):  List of 2-3 visual images or metaphors that relate to the memoir's theme.
        - color_palette (str): Preferred color palette for the cover.
        - font_style (str): Preferred font style (e.g., classic, modern, handwritten).

        Returns:
        str: A prompt for generating visual style preferences.
        """
        prompt = f"""
        Provide visual style preferences for the back cover design of a memoir.

        Genre: Memoir

        Visual Considerations:

        *   **Evoke Emotion:** The cover design should visually represent the emotional tone of the memoir.
        *   **Authenticity:** The design should feel genuine and personal, reflecting the author's voice.
        *   **Intrigue:** The design should pique the reader's curiosity and make them want to learn more.
        *   **Simplicity:** Often, less is more. Avoid overly cluttered or distracting designs.
        *   **Relatability:**  The imagery should resonate with the target audience.

        Specific Preferences:

        1.  **Imagery:** Suggest visual images or metaphors that relate to the memoir's theme.  For example, if the memoir is about overcoming adversity, the imagery might include a sunrise, a blooming flower, or a mountain peak. {kwargs.get('imagery_suggestions', 'List 2-3 visual imagery suggestions.')}
        2.  **Color Palette:**  Specify a preferred color palette that reflects the emotional tone of the memoir.  For example, warm colors (red, orange, yellow) might be appropriate for a hopeful or uplifting memoir, while cool colors (blue, green, purple) might be better suited for a more reflective or melancholic story. {kwargs.get('color_palette', 'Describe preferred color palette.')}
        3.  **Font Style:**  Choose a font style that is both readable and visually appealing.  Consider whether a classic, modern, or handwritten font would best represent the author's voice and the overall tone of the memoir. {kwargs.get('font_style', 'Describe preferred font style.')}
        4.  **Overall Mood:**  Describe the overall mood or feeling that the back cover design should evoke.  Should it be hopeful, poignant, reflective, or something else? {kwargs.get('emotional_tone', 'Describe the emotional tone.')}

        The memoir's main theme is {kwargs.get('main_theme', 'Briefly describe the memoir\'s central theme.')}.

        Provide these visual style preferences to guide the design process and create a back cover that is both visually appealing and emotionally resonant.
        """
        return prompt
        ```
        memoir_book_additions = """

## Memoir Series Book Integration

### Memoir Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon memoir concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous memoir books when relevant
- **Knowledge Progression**: Advance reader understanding of memoir topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the memoir series

### Book-Specific Memoir Focus
- **Educational Objectives**: What specific memoir knowledge will readers gain from this book?
- **Practical Applications**: What actionable memoir insights will be provided?
- **Research Integration**: How will new memoir research be incorporated?
- **Series Advancement**: How does this book advance the overall memoir education series?
- **Reader Value**: What unique memoir value does this book add to the series?

Ensure this book provides comprehensive memoir education while serving as an integral part of the learning series.
"""

        return base_prompt + memoir_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return MemoirPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return MemoirPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return MemoirPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return MemoirPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return MemoirPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return MemoirPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return MemoirPrompts.get_series_book_prompt(**kwargs)
