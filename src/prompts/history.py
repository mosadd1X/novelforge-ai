"""
History genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class HistoryPrompts(NonFictionBasePrompts):
    GENRE_NAME = "History"
    GENRE_DESCRIPTION = "Historical fiction immerses readers in the past, blending factual events with fictional narratives. It strives for authenticity in depicting the social, political, and cultural contexts of a specific historical period, while also exploring universal human themes through compelling characters and storylines."
    
    GENRE_CHARACTERISTICS = [
        "Authenticity: Meticulous research and accurate portrayal of historical events, customs, and settings.",
        "Immersion: Vivid descriptions that transport the reader to the past, creating a believable and engaging experience.",
        "Character-Driven Narratives: Compelling characters whose lives are shaped by historical events and who grapple with the challenges of their time.",
        "Exploration of Themes: Examination of universal human themes such as love, loss, ambition, betrayal, and the struggle for survival within a historical context.",
        "Conflict and Intrigue: Highlighting the political, social, and personal conflicts that defined the historical period.",
        "Moral Ambiguity: Presenting characters and events with nuance, avoiding simplistic good vs. evil portrayals and exploring the complexities of historical decisions.",
        "Detailed World-Building: Creating a rich and detailed world that reflects the social hierarchies, cultural norms, and technological limitations of the time.",
        "Impact of Historical Events: Demonstrating how significant historical events shape the lives of individual characters and the course of the narrative.",
        "Sense of Place: Strong evocation of the physical environment and its influence on the characters and events.",
        "Use of Primary and Secondary Sources: Drawing upon historical documents, accounts, and scholarly research to ensure accuracy and depth."
    ]
    
    TYPICAL_ELEMENTS = [
        "Historical Setting: A clearly defined historical period and geographical location that serves as the backdrop for the story.",
        "Historical Figures: Inclusion of real historical figures, either as major characters or as supporting roles.",
        "Significant Historical Events: Incorporation of major historical events that impact the plot and characters.",
        "Social and Political Context: Exploration of the social hierarchies, political systems, and cultural norms of the time.",
        "Costumes and Customs: Detailed descriptions of clothing, food, rituals, and other customs that define the historical period.",
        "Technology and Innovation: Accurate portrayal of the technological advancements and limitations of the time.",
        "Dialogue and Language: Use of language that reflects the speech patterns and vocabulary of the historical period.",
        "Primary Source Integration: Incorporation of excerpts from historical documents, letters, or diaries to enhance authenticity.",
        "Maps and Visual Aids: Inclusion of maps, illustrations, or other visual aids to help readers visualize the historical setting.",
        "Themes of Power and Authority: Examination of the dynamics of power and authority within the historical context.",
        "Cultural Clash: Exploration of the conflicts and interactions between different cultures or social groups.",
        "Personal Journeys: Focus on the personal journeys of characters as they navigate the challenges and opportunities of their time."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Writing Considerations
- **Historical Accuracy**: Prioritize meticulous research and fact-checking to ensure the historical accuracy of your narrative. Consult primary and secondary sources, and be prepared to revise your work based on new information.
- **Authenticity of Voice**: Develop a writing style that reflects the language and tone of the historical period. Consider using archaic vocabulary and sentence structures sparingly to enhance authenticity without sacrificing readability.
- **World-Building Depth**: Create a rich and detailed world that immerses the reader in the past. Pay attention to the social, political, economic, and cultural aspects of the historical period, and incorporate these details into your narrative.
- **Character Believability**: Develop characters whose motivations, beliefs, and actions are consistent with the historical context. Avoid anachronisms in their thoughts, behaviors, and dialogue.
- **Avoiding Presentism**: Be mindful of projecting modern values and perspectives onto historical characters and events. Strive to understand the past on its own terms, without imposing contemporary judgments.
- **Balancing Fact and Fiction**: Find a balance between historical accuracy and narrative license. While it is important to remain true to the historical record, you also have the freedom to create fictional characters and storylines that explore the human experience within that context.
- **Sensitivity to Historical Trauma**: Approach sensitive historical topics with respect and empathy. Avoid trivializing or sensationalizing events that caused suffering and injustice.
- **Understanding Causality**: Demonstrate a clear understanding of the causes and consequences of historical events. Show how individual actions and decisions contribute to the larger historical narrative.
'''
        return base_prompt + history_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Outline Requirements
- **Chronological Structure**: Consider organizing your outline chronologically to reflect the sequence of historical events. This can help readers follow the narrative and understand the cause-and-effect relationships between events.
- **Key Historical Events**: Identify the key historical events that will shape your story and incorporate them into your outline. Determine how these events will impact your characters and drive the plot forward.
- **Character Arcs**: Outline the character arcs of your main characters, showing how they change and develop over the course of the story in response to historical events and personal challenges.
- **Setting and Atmosphere**: Include details about the setting and atmosphere in your outline, noting how the physical environment and social context contribute to the overall mood and tone of the story.
- **Themes and Motifs**: Identify the major themes and motifs that you want to explore in your novel and incorporate them into your outline. Consider how these themes will resonate with readers and provide insight into the human condition.
- **Historical Context**: Provide a brief overview of the historical context for each section of your outline, highlighting the key political, social, and cultural factors that are relevant to the story.
- **Research Notes**: Include research notes in your outline to remind yourself of important historical details and sources that you need to consult as you write.
- **Multiple Perspectives**: If your story involves multiple perspectives, outline each character's point of view separately to ensure that their voices are distinct and authentic.
'''
        return base_prompt + history_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Character Development
- **Historical Accuracy of Background**: Ensure your character's background, including their social class, family history, and education, is consistent with the historical period. Research the typical life experiences of people in their position.
- **Believable Motivations**: Develop motivations that are rooted in the historical context. Consider the social, political, and economic factors that would influence their desires and goals.
- **Authentic Language and Dialogue**: Craft dialogue that reflects the speech patterns and vocabulary of the time. Avoid using modern slang or idioms that would sound out of place.
- **Impact of Historical Events on Character**: Show how historical events shape your character's personality, beliefs, and actions. Explore how they react to challenges and opportunities presented by their time.
- **Moral Complexity**: Avoid creating simplistic good vs. evil characters. Explore the moral ambiguities of the historical period and allow your characters to make difficult choices with complex consequences.
- **Internal Conflicts**: Develop internal conflicts that reflect the tensions and contradictions of the historical period. Consider how your character grapples with conflicting loyalties, beliefs, and desires.
- **Relationships with Historical Figures**: If your character interacts with real historical figures, ensure that these interactions are consistent with the historical record and that they reveal something about both characters.
- **Character Arc and Transformation**: Plan a character arc that shows how your character changes and develops over the course of the story in response to historical events and personal experiences.
'''
        return base_prompt + history_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Chapter Writing
- **Setting the Scene**: Begin each chapter by vividly describing the historical setting, including the physical environment, social atmosphere, and cultural details.
- **Historical Context**: Provide relevant historical context to help readers understand the events and characters in the chapter. This could include brief explanations of political events, social customs, or economic conditions.
- **Character Development**: Use each chapter to further develop your characters, revealing their motivations, beliefs, and relationships. Show how they are affected by the historical events unfolding around them.
- **Pacing and Tension**: Control the pacing of each chapter to build tension and keep readers engaged. Use cliffhangers, foreshadowing, and dramatic irony to create suspense.
- **Authentic Dialogue**: Write dialogue that reflects the speech patterns and vocabulary of the historical period. Avoid using modern slang or idioms that would sound out of place.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show readers what is happening, rather than simply telling them. This will help to immerse them in the historical setting.
- **Historical Accuracy**: Ensure that all historical details in the chapter are accurate and consistent with your research. Double-check facts, dates, and names to avoid errors.
- **Emotional Impact**: Aim to create an emotional impact on readers by exploring the human experiences of your characters. Show how they cope with challenges, celebrate victories, and grieve losses.
'''
        return base_prompt + history_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a history-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        history_series_additions = """

## History Series-Specific Planning Elements

### Educational Progression for History
- **Knowledge Building**: Structure learning progression appropriate for history topics
- **Expertise Development**: Guide readers from basic to advanced understanding of history subjects
- **Practical Applications**: Include actionable insights specific to history throughout the series
- **Research Depth**: Plan comprehensive research appropriate for history authority
- **Reader Value**: Ensure each book provides significant history value while building series knowledge

### History Series Continuity
- **Subject Consistency**: Maintain consistent approach to history topics across books
- **Authority Building**: Establish and maintain credibility in history throughout the series
- **Information Architecture**: Structure information flow appropriate for history learning
- **Cross-References**: Create meaningful connections between history concepts across books
- **Updated Knowledge**: Plan for incorporating new history research and developments

Create a history series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + history_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a history-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class HistoryMarketing:
        """
        A class containing methods for generating back cover copy and marketing materials
        specifically tailored for the History genre.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions for History books.

        Args:
        **kwargs: Optional keyword arguments to customize the prompt.  Can include:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - time_period (str): The specific time period covered in the book (e.g., "Ancient Rome," "Victorian England").
        - subject (str): The main subject of the book (e.g., "World War II," "The French Revolution").
        - protagonist (str, optional): If applicable, a brief description of the protagonist.
        - key_events (list, optional): A list of key events covered in the book.
        - themes (list, optional): A list of major themes explored in the book (e.g., "power," "revolution," "social change").
        - target_audience (str, optional):  The target audience for the book (e.g., "general readers," "academic historians").
        - unique_selling_point (str, optional): What makes this book stand out from other history books on the same topic.
        - tone (str, optional): The desired tone of the back cover copy (e.g., "dramatic," "informative," "engaging," "scholarly").

        Returns:
        str: A detailed prompt string for generating back cover copy.
        """

        title = kwargs.get("title", "[Book Title]")
        author = kwargs.get("author", "[Author Name]")
        time_period = kwargs.get("time_period", "[Time Period]")
        subject = kwargs.get("subject", "[Historical Subject]")
        protagonist = kwargs.get("protagonist", None)
        key_events = kwargs.get("key_events", [])
        themes = kwargs.get("themes", [])
        target_audience = kwargs.get("target_audience", "general readers")
        unique_selling_point = kwargs.get("unique_selling_point", None)
        tone = kwargs.get("tone", "engaging")

        prompt = f"""
        Write a compelling back cover description for the history book "{title}" by {author}.

        The book explores {subject} during the {time_period}. The target audience is {target_audience}. The tone should be {tone}.

        The description should:

        *   Hook the reader with a captivating opening that highlights the significance of the historical events and their lasting impact.
        *   Clearly state the central argument or narrative of the book.
        *   If applicable, introduce the protagonist and their role in the events.  If a protagonist is defined, use this description: '{protagonist}'.
        *   Summarize the key events covered in the book.  If key events are defined, make sure to include them: {key_events}.
        *   Highlight the major themes explored in the book. If themes are defined, make sure to include them: {themes}. These could include themes like power, revolution, social change, conflict, and technological advancement.
        *   Emphasize the human element of history - the lives, struggles, and triumphs of individuals and societies.
        *   Explain why this book is essential reading for understanding the past and its relevance to the present.
        *   If a unique selling point is defined, make sure to include it: '{unique_selling_point}'.
        *   Use vivid language and imagery to bring the past to life.
        *   End with a call to action, encouraging the reader to delve into the book and uncover the secrets of history.
        *   Avoid overly academic jargon and focus on accessibility and readability.
        *   The description should be approximately 150-200 words.

        Consider the following questions to guide the reader:

        *   What pivotal moments shaped the course of history during this period?
        *   What were the social, political, and economic forces at play?
        *   What were the long-term consequences of these events?
        *   What can we learn from the past to inform our understanding of the present?

        Example opening lines to inspire you:

        *   "Witness the dawn of a new era..."
        *   "In the heart of [Time Period], a revolution was brewing..."
        *   "The fate of nations hung in the balance..."
        *   "Beyond the textbooks, lies the untold story of..."

        Remember to focus on the unique aspects of this historical event and its enduring impact on the world.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, impactful book recommendation for History books (2-3 lines).

        Args:
        **kwargs: Optional keyword arguments to customize the prompt.  Can include:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - time_period (str): The specific time period covered in the book.
        - subject (str): The main subject of the book.
        - focus (str, optional): A particular aspect of the history that is highlighted (e.g., "the daily lives of soldiers," "the political intrigue," "the technological innovations").

        Returns:
        str: A prompt string for generating a short book recommendation.
        """
        title = kwargs.get("title", "[Book Title]")
        author = kwargs.get("author", "[Author Name]")
        time_period = kwargs.get("time_period", "[Time Period]")
        subject = kwargs.get("subject", "[Historical Subject]")
        focus = kwargs.get("focus", None)

        prompt = f"""
        Write a short (2-3 line) book recommendation for the history book "{title}" by {author}.

        The book explores {subject} during the {time_period}.

        The recommendation should:

        *   Be concise and attention-grabbing.
        *   Highlight the most compelling aspect of the book.
        *   Focus on what makes this book unique and worth reading.
        *   Use strong verbs and vivid language.
        *   If a specific focus is provided, highlight it: {focus}

        Examples:

        *   "Uncover the hidden stories of [Time Period] in this gripping account of [Subject]."
        *   "A must-read for anyone interested in the dramatic events of [Time Period]."
        *   "Experience the past like never before with this immersive exploration of [Subject]."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for History books.

        Args:
        **kwargs: Optional keyword arguments to customize the prompt.  Can include:
        - title (str): The title of the book.
        - time_period (str): The specific time period covered in the book.
        - subject (str): The main subject of the book.
        - key_concept (str, optional): A central idea or theme from the book (e.g., "the rise and fall of empires," "the power of propaganda").

        Returns:
        str: A prompt string for generating a marketing tagline.
        """
        title = kwargs.get("title", "[Book Title]")
        time_period = kwargs.get("time_period", "[Time Period]")
        subject = kwargs.get("subject", "[Historical Subject]")
        key_concept = kwargs.get("key_concept", None)

        prompt = f"""
        Write a punchy marketing tagline for the history book "{title}".

        The book explores {subject} during the {time_period}.

        The tagline should:

        *   Be short, memorable, and impactful.
        *   Capture the essence of the book in a single phrase.
        *   Evoke curiosity and intrigue.
        *   Highlight the book's unique selling point.
        *   If a key concept is provided, incorporate it: {key_concept}

        Examples:

        *   "[Time Period]: History Uncovered."
        *   "The past is never truly past."
        *   "Witness the birth of a nation."
        *   "The story they didn't want you to know."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for suggesting visual style preferences for the back cover of History books.

        Args:
        **kwargs: Optional keyword arguments to customize the prompt.  Can include:
        - time_period (str): The specific time period covered in the book.
        - subject (str): The main subject of the book.
        - tone (str, optional): The desired tone of the cover (e.g., "serious," "dramatic," "intriguing").
        - imagery_focus (str, optional): What the imagery should primarily focus on (e.g., "portraits of historical figures," "battle scenes," "artifacts," "maps").

        Returns:
        str: A prompt string for generating visual style preferences.
        """
        time_period = kwargs.get("time_period", "[Time Period]")
        subject = kwargs.get("subject", "[Historical Subject]")
        tone = kwargs.get("tone", "serious")
        imagery_focus = kwargs.get("imagery_focus", "portraits of historical figures")

        prompt = f"""
        Suggest visual style preferences for the back cover of a history book about {subject} during the {time_period}.

        The overall tone of the cover should be {tone}.

        Consider the following elements:

        *   Color palette: Should the colors be muted and historical, or vibrant and modern? Consider colors associated with the {time_period}.
        *   Typography: What font styles would be appropriate for the subject matter and time period? (e.g., serif fonts for a classic look, sans-serif fonts for a modern look).
        *   Imagery:  The imagery should focus on {imagery_focus}. Consider using historical photographs, paintings, maps, or illustrations.  Should the imagery be realistic or stylized?
        *   Layout:  How should the text and imagery be arranged on the back cover to create a visually appealing and informative design?
        *   Overall aesthetic: Should the cover evoke a sense of mystery, drama, authority, or authenticity?

        Provide specific recommendations for the use of visual elements to create a compelling and accurate representation of the book's content.
        """
        return prompt
        ```
        history_book_additions = """

## History Series Book Integration

### History Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon history concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous history books when relevant
- **Knowledge Progression**: Advance reader understanding of history topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the history series

### Book-Specific History Focus
- **Educational Objectives**: What specific history knowledge will readers gain from this book?
- **Practical Applications**: What actionable history insights will be provided?
- **Research Integration**: How will new history research be incorporated?
- **Series Advancement**: How does this book advance the overall history education series?
- **Reader Value**: What unique history value does this book add to the series?

Ensure this book provides comprehensive history education while serving as an integral part of the learning series.
"""

        return base_prompt + history_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return HistoryPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return HistoryPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return HistoryPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return HistoryPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return HistoryPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return HistoryPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return HistoryPrompts.get_series_book_prompt(**kwargs)
