"""
Creative Non-Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class CreativeNonFictionPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Creative Non-Fiction"
    GENRE_DESCRIPTION = "Creative Non-Fiction blends factual accuracy with literary flair. It employs narrative techniques typically associated with fiction, such as character development, plot structure, and vivid imagery, to tell true stories. The genre encompasses a wide range of forms, including memoir, personal essay, literary journalism, and travel writing, all grounded in verifiable reality but elevated by artistic expression."

    GENRE_CHARACTERISTICS = [
        "Personal Voice: The author's unique perspective and experiences are central to the narrative.",
        "Factual Accuracy: While employing creative techniques, the work remains committed to truth and verifiable facts.",
        "Narrative Structure: Employs storytelling techniques like plot, pacing, and suspense to engage the reader.",
        "Character Development: Real people are portrayed as complex characters with motivations, flaws, and growth.",
        "Setting and Atmosphere: Vivid descriptions of places and environments contribute to the overall impact.",
        "Thematic Exploration: Explores universal themes and ideas through personal experiences and observations.",
        "Reflective Tone: Often includes introspection and analysis of the events and their significance.",
        "Emotional Resonance: Aims to evoke emotional responses in the reader through relatable experiences.",
        "Immersive Detail: Uses sensory details and specific anecdotes to create a sense of immediacy and authenticity.",
        "Ethical Considerations: Navigates the ethical complexities of representing real people and events responsibly."
    ]

    TYPICAL_ELEMENTS = [
        "Memoir: Focuses on a specific period or theme in the author's life.",
        "Personal Essay: Explores a topic through the lens of the author's personal experiences and reflections.",
        "Literary Journalism: Combines journalistic reporting with literary techniques to tell true stories.",
        "Travel Writing: Documents journeys and cultural encounters with a focus on personal observations and insights.",
        "Biography/Autobiography: Tells the life story of a real person, either by themselves or another author.",
        "Creative Biography: A biography that employs creative writing techniques to bring the subject to life.",
        "Flash Nonfiction: Short, impactful pieces that capture a moment or idea with brevity and precision.",
        "Lyric Essay: Blends elements of poetry and prose to explore a subject in a fragmented and evocative way.",
        "Immersion Journalism: The author embeds themselves in a situation to report on it firsthand.",
        "Anecdotes: Short, engaging stories that illustrate a point or reveal character.",
        "Dialogue: Realistic conversations that reveal character and advance the narrative.",
        "Reflection: Introspective passages that explore the meaning and significance of events."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        creative_non_fiction_additions = '''
## Creative Non-Fiction-Specific Writing Considerations
- **Ethical Responsibility**: Understand the ethical implications of writing about real people and events. Prioritize accuracy, fairness, and respect for privacy. Consider obtaining consent when necessary and avoiding sensationalism.
- **Voice and Authenticity**: Cultivate a unique and authentic voice that resonates with readers. Be honest and vulnerable in your writing, sharing your personal experiences and perspectives with sincerity.
- **Memory and Recall**: Develop techniques for accurately recalling and representing past events. Utilize journals, photographs, interviews, and research to enhance memory and ensure factual accuracy.
- **Emotional Honesty**: Explore your emotions and motivations with honesty and introspection. Be willing to confront difficult truths and share your vulnerabilities with readers.
- **Balancing Fact and Art**: Master the art of blending factual accuracy with literary techniques. Use vivid language, imagery, and narrative structure to engage readers while remaining true to the facts.
- **Research and Verification**: Conduct thorough research to support your writing and ensure accuracy. Verify facts, dates, and details to maintain credibility and avoid misinformation.
- **Audience Awareness**: Consider your target audience and tailor your writing to their interests and expectations. Choose a tone, style, and level of detail that will resonate with your readers.
- **Self-Reflection**: Regularly reflect on your writing process and identify areas for improvement. Seek feedback from trusted sources and be open to constructive criticism.
'''
        return base_prompt + creative_non_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        creative_non_fiction_additions = '''
## Creative Non-Fiction-Specific Outline Requirements
- **Theme Identification**: Clearly define the central theme or message you want to convey. Ensure that each section of the outline contributes to the exploration of this theme.
- **Chronological vs. Thematic Structure**: Decide whether to structure your narrative chronologically or thematically. A chronological structure follows a linear timeline, while a thematic structure groups events and experiences around specific themes.
- **Character Arcs**: Map out the character arcs of the real people in your story. Consider how they change and evolve throughout the narrative.
- **Setting the Scene**: Outline the key settings and environments that will be featured in your narrative. Include details about the atmosphere, sensory details, and significance of each setting.
- **Anecdotal Integration**: Identify key anecdotes and stories that will illustrate your points and engage readers. Plan where to incorporate these anecdotes into your outline.
- **Reflective Passages**: Allocate space for reflective passages where you can explore your thoughts, feelings, and insights about the events and experiences you are describing.
- **Ethical Considerations**: Consider any ethical implications of your story and plan how to address them in your narrative.
- **Dramatic Tension**: Identify moments of conflict, tension, or suspense that will keep readers engaged. Plan how to build and release tension throughout the narrative.
- **Resolution and Reflection**: Plan how to bring your narrative to a satisfying resolution. Include a final reflective passage that summarizes your key insights and takeaways.
'''
        return base_prompt + creative_non_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character development prompt specifically for creative non-fiction."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")
        target_audience = kwargs.get("target_audience", "Adult")
        subplot_info = kwargs.get("subplot_info", "")

        return f"""
# Creative Non-Fiction Character Development

Create authentic, complex characters for the creative non-fiction work "{title}" for {target_audience}.

## Work Information
- Title: {title}
- Description: {description}
- Genre: Creative Non-Fiction
- Target Audience: {target_audience}

## Work Outline
{outline}

{subplot_info}

## Creative Non-Fiction Character Requirements

### Character Development Guidelines
1. **Authenticity and Complexity**: Portray real people with depth, avoiding stereotypes and caricatures
2. **Multiple Perspectives**: Consider different viewpoints to provide nuanced character portraits
3. **Inner Life Exploration**: Reveal characters' thoughts, feelings, and motivations through introspection
4. **Ethical Considerations**: Respect privacy and dignity of real people being portrayed
5. **Character Evolution**: Show how people change and develop throughout the narrative
6. **Dialogue and Interaction**: Use realistic conversation to reveal character and advance story
7. **Contextual Understanding**: Provide backstory and context to explain motivations and actions

### Character Types for Creative Non-Fiction
- **Central Figures**: 1-2 main people whose stories drive the narrative
- **Supporting Characters**: 3-4 people who provide context and depth to the story
- **The Author/Narrator**: Often a character themselves, observing and participating
- **Historical/Cultural Figures**: People who provide broader context or comparison

## Character Object Format
For each character, provide the following fields in a JSON object:
- "name": (string) Character's name (real name or pseudonym for privacy)
- "role": (string) Their role (central figure, supporting character, narrator, etc.)
- "appearance": (string) Physical description with meaningful, memorable details
- "personality": (string) Key personality traits and characteristics
- "background": (string) Essential life context and experiences
- "goals": (string) What they seek or represent in the narrative
- "arc": (string) How they develop or are revealed throughout the work
- "relationships": (string) How they relate to other characters and the narrator
- "strengths": (string) Their positive qualities and contributions
- "flaws": (string) Their human weaknesses and complexities
- "voice": (string) How they speak and express themselves
- "significance": (string) What they represent or contribute to the larger narrative
- "ethical_considerations": (string) Privacy and portrayal considerations for this person
- "inner_life": (string) Their thoughts, feelings, and internal motivations

## Creative Non-Fiction Guidelines
- Characters should feel like real, complex human beings
- Balance honesty with compassion in character portrayal
- Respect the privacy and dignity of real people
- Focus on authentic experiences and genuine insights
- Use literary techniques to bring characters to life while maintaining factual integrity

Return ONLY a valid JSON array of character objects, nothing else.
Example format:
[
  {{
    "name": "Sarah Martinez",
    "role": "central figure",
    "appearance": "A woman in her forties with calloused hands and laugh lines, always wearing her grandmother's silver bracelet",
    "personality": "Resilient and optimistic, but carries deep grief from family losses",
    "background": "Third-generation immigrant who runs a family restaurant while caring for aging parents",
    "goals": "To preserve her family's cultural traditions while adapting to modern challenges",
    "arc": "Learns to balance honoring the past with embracing necessary change",
    "relationships": "Devoted daughter and mother, mentor to younger family members",
    "strengths": "Cultural wisdom, business acumen, emotional strength",
    "flaws": "Sometimes too stubborn about tradition, difficulty asking for help",
    "voice": "Speaks with quiet authority, mixes English with Spanish when emotional",
    "significance": "Represents the immigrant experience and the challenge of preserving culture",
    "ethical_considerations": "Real person whose story is told with permission and respect",
    "inner_life": "Constantly weighing family obligations against personal dreams"
  }}
]
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        creative_non_fiction_additions = '''
## Creative Non-Fiction-Specific Chapter Writing
- **Scene Setting**: Begin each chapter with a vivid description of the setting, including sensory details, atmosphere, and significance.
- **Anecdotal Storytelling**: Weave anecdotes and personal stories into your chapters to illustrate your points and engage readers.
- **Character Development**: Use each chapter to further develop your characters, revealing their personalities, motivations, and flaws.
- **Dialogue Integration**: Incorporate realistic dialogue to reveal character and advance the narrative.
- **Reflective Passages**: Include reflective passages where you explore your thoughts, feelings, and insights about the events and experiences you are describing.
- **Pacing and Structure**: Vary the pacing and structure of your chapters to keep readers engaged. Use short, punchy sentences to create a sense of urgency, and longer, more descriptive sentences to create a sense of atmosphere.
- **Thematic Focus**: Ensure that each chapter contributes to the overall theme or message of your narrative.
- **Ethical Considerations**: Be mindful of the ethical implications of your writing and avoid sensationalizing or exploiting your subjects.
- **Show, Don't Tell**: Use vivid language and imagery to show readers what is happening, rather than simply telling them.
'''
        return base_prompt + creative_non_fiction_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a creativenonfiction-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        creativenonfiction_series_additions = """

## CreativeNonFiction Series-Specific Planning Elements

### Educational Progression for CreativeNonFiction
- **Knowledge Building**: Structure learning progression appropriate for creativenonfiction topics
- **Expertise Development**: Guide readers from basic to advanced understanding of creativenonfiction subjects
- **Practical Applications**: Include actionable insights specific to creativenonfiction throughout the series
- **Research Depth**: Plan comprehensive research appropriate for creativenonfiction authority
- **Reader Value**: Ensure each book provides significant creativenonfiction value while building series knowledge

### CreativeNonFiction Series Continuity
- **Subject Consistency**: Maintain consistent approach to creativenonfiction topics across books
- **Authority Building**: Establish and maintain credibility in creativenonfiction throughout the series
- **Information Architecture**: Structure information flow appropriate for creativenonfiction learning
- **Cross-References**: Create meaningful connections between creativenonfiction concepts across books
- **Updated Knowledge**: Plan for incorporating new creativenonfiction research and developments

Create a creativenonfiction series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + creativenonfiction_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a creativenonfiction-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        creativenonfiction_book_additions = """

## CreativeNonFiction Series Book Integration

### CreativeNonFiction Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon creativenonfiction concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous creativenonfiction books when relevant
- **Knowledge Progression**: Advance reader understanding of creativenonfiction topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the creativenonfiction series

### Book-Specific CreativeNonFiction Focus
- **Educational Objectives**: What specific creativenonfiction knowledge will readers gain from this book?
- **Practical Applications**: What actionable creativenonfiction insights will be provided?
- **Research Integration**: How will new creativenonfiction research be incorporated?
- **Series Advancement**: How does this book advance the overall creativenonfiction education series?
- **Reader Value**: What unique creativenonfiction value does this book add to the series?

Ensure this book provides comprehensive creativenonfiction education while serving as an integral part of the learning series.
"""

        return base_prompt + creativenonfiction_book_additions

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a prompt for creating compelling back cover copy for a
        Creative Non-Fiction book.

        Args:
        **kwargs:  Keyword arguments containing book details such as:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - central_theme (str): The central theme or subject matter.
        - emotional_core (str): The main emotion the book evokes.
        - key_events (list): A list of key events or turning points.
        - target_audience (str):  Description of the ideal reader.
        - unique_selling_point (str):  What makes this book stand out.
        - tone (str): The overall tone of the writing (e.g., reflective, humorous, poignant).
        - writing_style (str):  Description of the author's writing style (e.g., lyrical, journalistic, conversational).

        Returns:
        str: A detailed prompt string for generating back cover copy.
        """
        title = kwargs.get('title', '[Title]')
        author = kwargs.get('author', '[Author]')
        central_theme = kwargs.get('central_theme', '[Central Theme]')
        emotional_core = kwargs.get('emotional_core', '[Emotional Core]')
        key_events = kwargs.get('key_events', '[Key Events, comma-separated]')
        target_audience = kwargs.get('target_audience', '[Target Audience]')
        unique_selling_point = kwargs.get('unique_selling_point', '[Unique Selling Point]')
        tone = kwargs.get('tone', '[Tone]')
        writing_style = kwargs.get('writing_style', '[Writing Style]')

        prompt = f"""
        Craft compelling back cover copy for the Creative Non-Fiction book, "{title}" by {author}.
        The central theme explores {central_theme}, evoking an emotional core of {emotional_core}.
        Key events include: {key_events}.

        **Guidelines for Creative Non-Fiction:**

        *   **Emphasize the 'Creative'**:  Highlight the artistry and literary techniques used in telling the story. Focus on vivid language, sensory details, and narrative structure.
        *   **Authenticity and Truth**:  Acknowledge the factual basis of the story while emphasizing the author's unique perspective and personal journey.
        *   **Emotional Resonance**:  Connect with readers on a deep emotional level.  Highlight the universal human experiences explored in the book.
        *   **Personal Transformation**:  If applicable, showcase the author's or subjects' personal growth, insights, or transformations.
        *   **Literary Merit**:  Position the book as a work of literary significance, appealing to readers who appreciate well-crafted prose and insightful storytelling.

        **Include the following elements:**

        1.  **A Hook**:  Start with a captivating opening that immediately grabs the reader's attention.  Pose a question, present a striking image, or introduce a compelling character.
        2.  **A Brief Summary**:  Provide a concise overview of the book's subject matter, focusing on the most intriguing aspects.
        3.  **Emotional Impact**:  Convey the emotional weight of the story and how it will resonate with readers. Use strong verbs and evocative language.
        4.  **Author's Voice**:  Hint at the author's unique perspective and writing style ({writing_style} tone).
        5.  **Target Audience Appeal**:  Clearly indicate who the book is for ({target_audience}).
        6.  **Unique Selling Proposition**:  Emphasize what sets this book apart from other Creative Non-Fiction works ({unique_selling_point}).
        7.  **A Call to Action**:  Encourage readers to pick up the book and embark on the journey within its pages.

        **Example Framework:**

        "In '{title}', {author} masterfully blends [writing style] with the raw truth of [central theme]. Experience [emotional core] as [brief summary of key events/plot].  For readers who [target audience], this book offers [unique selling point]. Prepare to be moved, challenged, and ultimately transformed."

        Write approximately 150-200 words.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short (2-3 line) description
        for a Creative Non-Fiction book, suitable for recommendations.

        Args:
        **kwargs:  Keyword arguments containing book details such as:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - central_theme (str): The central theme.
        - emotional_impact (str): The primary emotional impact.
        - target_audience (str):  Ideal reader description.

        Returns:
        str: A detailed prompt string for generating a short description.
        """
        title = kwargs.get('title', '[Title]')
        author = kwargs.get('author', '[Author]')
        central_theme = kwargs.get('central_theme', '[Central Theme]')
        emotional_impact = kwargs.get('emotional_impact', '[Emotional Impact]')
        target_audience = kwargs.get('target_audience', '[Target Audience]')

        prompt = f"""
        Create a short, impactful 2-3 line description for the Creative Non-Fiction book, "{title}" by {author}.

        **Guidelines for Creative Non-Fiction:**

        *   **Focus on Emotional Resonance**:  Highlight the core emotion the book evokes (e.g., hope, grief, resilience, wonder).
        *   **Intrigue and Mystery**:  Hint at the book's central question or conflict without giving away too much.
        *   **Target Audience Appeal**:  Immediately convey who the book is for and why they should read it.

        **Include the following elements:**

        1.  **A Hook**:  Start with a captivating phrase or question that grabs attention.
        2.  **Core Theme**:  Briefly mention the central theme or subject matter.
        3.  **Emotional Impact**:  Convey the emotional experience readers will have.

        **Example Framework:**

        "'{title}' by {author} delves into {central_theme}, leaving readers with {emotional_impact}.  A must-read for anyone interested in {target_audience}."

        "Experience the raw power of {central_theme} in '{title}'.  {author}'s deeply personal account will resonate with those seeking {emotional_impact}."

        "For readers who [target_audience], '{title}' offers a poignant and unforgettable exploration of {central_theme}."

        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline
        for a Creative Non-Fiction book.

        Args:
        **kwargs:  Keyword arguments containing book details such as:
        - title (str): The title of the book.
        - central_theme (str): The central theme.
        - emotional_core (str):  The primary emotion.
        - unique_selling_point (str):  What makes the book unique.

        Returns:
        str: A detailed prompt string for generating a tagline.
        """
        title = kwargs.get('title', '[Title]')
        central_theme = kwargs.get('central_theme', '[Central Theme]')
        emotional_core = kwargs.get('emotional_core', '[Emotional Core]')
        unique_selling_point = kwargs.get('unique_selling_point', '[Unique Selling Point]')

        prompt = f"""
        Create a compelling and memorable marketing tagline for the Creative Non-Fiction book, "{title}".

        **Guidelines for Creative Non-Fiction:**

        *   **Focus on Authenticity**:  The tagline should feel genuine and reflect the true essence of the story.
        *   **Emotional Connection**:  Evoke the primary emotion the book explores.
        *   **Intrigue and Curiosity**:  Make readers want to know more.
        *   **Conciseness and Impact**:  Keep it short, memorable, and impactful.

        **Consider these angles:**

        *   **Thematic Focus**:  Highlight the central theme in a provocative way.
        *   **Emotional Core**:  Capture the emotional heart of the book.
        *   **Unique Selling Point**:  Emphasize what makes the book stand out.

        **Examples:**

        *   "{central_theme}: A Story of [Emotional Core]."
        *   "The Truth You Didn't Know You Needed."
        *   "{title}: Where [Central Theme] Meets [Emotional Core]."
        *   "More Than Just a Story. It's a [Unique Selling Point]."
        *   "Unearthing the Truth Within."

        Generate several options, each no more than 7-10 words.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt to guide the visual design of the back cover
        for a Creative Non-Fiction book.

        Args:
        **kwargs:  Keyword arguments containing book details such as:
        - title (str): The title of the book.
        - central_theme (str): The central theme.
        - emotional_tone (str): The overall feeling.
        - target_audience (str): The intended reader.
        - key_imagery (list): List of keywords for imagery.
        - writing_style (str): The author's writing style.

        Returns:
        str: A detailed prompt string for visual design guidance.
        """
        title = kwargs.get('title', '[Title]')
        central_theme = kwargs.get('central_theme', '[Central Theme]')
        emotional_tone = kwargs.get('emotional_tone', '[Emotional Tone]')
        target_audience = kwargs.get('target_audience', '[Target Audience]')
        key_imagery = kwargs.get('key_imagery', '[Key Imagery Keywords, comma-separated]')
        writing_style = kwargs.get('writing_style', '[Writing Style]')

        prompt = f"""
        Provide visual style preferences for the back cover design of the Creative Non-Fiction book, "{title}".

        **Guidelines for Creative Non-Fiction:**

        *   **Reflect Authenticity**: The design should feel genuine and avoid overly stylized or artificial elements.
        *   **Evoke Emotion**:  The visual style should complement the book's emotional tone.
        *   **Hint at the Story**:  The imagery should subtly suggest the book's central theme or subject matter.
        *   **Appeal to the Target Audience**: The design should resonate with the intended reader.

        **Consider these elements:**

        1.  **Color Palette**:  Suggest a color palette that reflects the book's emotional tone ({emotional_tone}). Consider using muted tones, natural colors, or colors that evoke specific emotions.
        2.  **Imagery**:  Describe the type of imagery that would be appropriate, drawing inspiration from the book's key imagery keywords ({key_imagery}). Consider using photographs, illustrations, or abstract designs.
        3.  **Typography**:  Suggest font styles that complement the book's writing style ({writing_style}) and target audience ({target_audience}). Consider using classic fonts, handwritten fonts, or fonts that evoke a sense of history or authenticity.
        4.  **Layout**:  Describe the overall layout of the back cover, including the placement of text, images, and other elements. Consider using a minimalist layout, a layered layout, or a layout that emphasizes the book's title.
        5.  **Overall Aesthetic**:  Describe the overall aesthetic of the back cover. Consider using words like "intimate," "reflective," "powerful," "haunting," or "uplifting."

        **Example:**

        "For '{title}', a book exploring {central_theme} with an emotional tone of {emotional_tone}, the back cover design should evoke a sense of [aesthetic]. The color palette should be [color palette description], with imagery featuring [key imagery]. The font should be [font style suggestion] to appeal to [target audience]."

        Provide specific and actionable suggestions to guide the visual designer.
        """
        return prompt


# Convenience functions for direct access

def get_writer_profile_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_series_book_prompt(**kwargs)
