"""
Alternate History genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class AlternateHistoryPrompts(FictionBasePrompts):
    GENRE_NAME = "Alternate History"
    GENRE_DESCRIPTION = "Alternate History explores 'what if' scenarios by diverging from established historical timelines. It examines the potential consequences of altered events, decisions, or technologies, creating worlds that are both familiar and strikingly different from our own. The genre often delves into the complex interplay of politics, society, culture, and individual lives within these altered realities."
    
    GENRE_CHARACTERISTICS = [
        "A clearly defined point of divergence (POD) from real history, which serves as the foundation for the altered timeline.",
        "Plausible and logically consistent consequences stemming from the POD, demonstrating how the altered event reshapes subsequent historical developments.",
        "Detailed world-building that reflects the changes in technology, culture, politics, and social structures resulting from the altered timeline.",
        "Exploration of the impact on individual lives and societies, showcasing how characters adapt to or are affected by the alternate reality.",
        "Examination of the ethical and moral implications of the altered timeline, often raising questions about progress, freedom, and the nature of history itself.",
        "A strong sense of verisimilitude, grounding the alternate reality in historical accuracy and believable extrapolations.",
        "Consideration of the butterfly effect, acknowledging that even small changes can have significant and far-reaching consequences.",
        "The presence of familiar historical figures in altered roles or circumstances, providing a point of connection to real history.",
        "Exploration of counterfactual scenarios, such as different outcomes of wars, technological breakthroughs, or political revolutions.",
        "A narrative that balances the fantastical elements of the alternate reality with the grounded realities of human experience."
    ]
    
    TYPICAL_ELEMENTS = [
        "A specific Point of Divergence (POD) clearly identified and explained.",
        "Altered political landscapes, such as different alliances, empires, or forms of government.",
        "Technological advancements or setbacks that deviate from the real-world timeline.",
        "Modified social structures and cultural norms reflecting the altered historical context.",
        "Different outcomes of major historical events, such as wars, revolutions, or discoveries.",
        "The rise and fall of alternate empires or nations.",
        "The survival or extinction of different cultures or languages.",
        "The altered roles and fates of historical figures.",
        "The emergence of new ideologies or philosophical movements.",
        "The development of alternate technologies and inventions.",
        "The exploration of different ethical and moral dilemmas.",
        "The presence of alternate historical documents or artifacts."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Writing Considerations
- **Historical Accuracy**: Demonstrate a strong understanding of the historical period you are altering. Research the social, political, and technological context thoroughly to ensure your point of divergence and its consequences are plausible.
- **Plausibility of Divergence**: The point of divergence should be believable and grounded in the realities of the historical period. Avoid introducing elements that are entirely anachronistic or defy the laws of physics without a clear explanation.
- **Consequence Mapping**: Carefully map out the consequences of your point of divergence. Consider how it would affect different aspects of society, technology, and politics. Use a cause-and-effect approach to build a believable alternate timeline.
- **World-Building Depth**: Create a detailed world that reflects the changes in your alternate timeline. Develop new cultures, languages, political systems, and technologies that are consistent with the altered historical context.
- **Character Adaptation**: Explore how your characters adapt to the altered reality. Consider how their beliefs, values, and relationships are shaped by the new historical context.
- **Ethical Implications**: Examine the ethical and moral implications of your alternate timeline. Consider the consequences of your point of divergence on issues such as freedom, equality, and progress.
- **Internal Consistency**: Maintain internal consistency throughout your story. Ensure that the rules and principles of your alternate world are consistent and that your characters act in accordance with those rules.
- **Avoid Presentism**: Avoid imposing modern values and perspectives on your historical characters. Strive to understand their motivations and beliefs within the context of their own time.
'''
        return base_prompt + alternate_history_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Outline Requirements
- **Establish the Point of Divergence (POD)**: Clearly define the specific event or decision that deviates from real history. Explain the circumstances surrounding the POD and its immediate consequences.
- **Map the Cascade of Effects**: Outline the major changes that result from the POD, tracing their impact on politics, technology, society, and culture. Create a timeline of key events in your alternate history.
- **Develop Key Characters**: Introduce the main characters and their roles in the alternate timeline. Consider how their lives are affected by the altered historical context.
- **Structure the Narrative Arc**: Outline the major plot points and conflicts in your story. Consider how the alternate history setting shapes the narrative arc.
- **World-Building Integration**: Integrate world-building details into the outline, showcasing the unique aspects of your alternate reality. Include descriptions of new technologies, cultures, and political systems.
- **Explore Ethical Dilemmas**: Identify the ethical dilemmas that arise from the alternate timeline. Consider how your characters grapple with these dilemmas.
- **Create a Compelling Climax**: Outline a climax that resolves the major conflicts in your story and showcases the consequences of the alternate history setting.
- **Provide a Satisfying Resolution**: Outline a resolution that provides closure to the characters' stories and reflects on the broader themes of the alternate history.
- **Consider Multiple Perspectives**: Outline how different characters or groups are affected by the altered timeline, showcasing diverse viewpoints.
- **Incorporate Historical Parallels**: Identify parallels between your alternate history and real history, highlighting the similarities and differences between the two timelines.
'''
        return base_prompt + alternate_history_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Character Development
- **Historical Context**: Ground your characters in the specific historical context of your alternate timeline. Consider how their beliefs, values, and relationships are shaped by the altered historical events.
- **Adaptation to Change**: Explore how your characters adapt to the changes in the alternate reality. Consider their reactions to new technologies, political systems, and social norms.
- **Moral Dilemmas**: Present your characters with moral dilemmas that arise from the alternate timeline. Consider how they grapple with these dilemmas and the choices they make.
- **Relationships and Conflicts**: Develop relationships and conflicts between characters that are shaped by the alternate historical context. Consider how their interactions reflect the broader themes of your story.
- **Historical Awareness**: Determine the level of historical awareness your characters possess. Do they know about the real history, or are they only aware of the alternate timeline?
- **Impact of Technology**: Consider how technology impacts your characters' lives. Are they early adopters of new technologies, or are they resistant to change?
- **Political Alignment**: Define your characters' political alignment within the alternate historical context. Are they supporters of the ruling regime, or are they rebels fighting for change?
- **Cultural Identity**: Explore your characters' cultural identity within the alternate timeline. How does their culture differ from the real-world equivalent, and how does it shape their worldview?
- **Personal Goals**: Define your characters' personal goals and motivations within the alternate historical context. How do their goals align with or conflict with the broader themes of your story?
'''
        return base_prompt + alternate_history_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Chapter Writing
- **Contextual Setting**: Begin each chapter by establishing the historical context and setting. Describe the political climate, social norms, and technological advancements of the alternate timeline.
- **Character Actions**: Show how your characters' actions are influenced by the alternate historical context. Consider how their choices reflect the broader themes of your story.
- **World-Building Integration**: Weave world-building details into the narrative, showcasing the unique aspects of your alternate reality. Describe new technologies, cultures, and political systems through the characters' experiences.
- **Historical Parallels**: Draw parallels between your alternate history and real history, highlighting the similarities and differences between the two timelines. Use these parallels to create a sense of verisimilitude.
- **Ethical Dilemmas**: Present your characters with ethical dilemmas that arise from the alternate timeline. Explore the consequences of their choices and the impact on their relationships.
- **Suspense and Conflict**: Build suspense and conflict by introducing challenges and obstacles that are specific to the alternate historical context.
- **Character Development**: Use each chapter to develop your characters' personalities and motivations. Show how they grow and change as they navigate the challenges of the alternate timeline.
- **Show, Don't Tell**: Use vivid descriptions and engaging dialogue to bring your alternate history to life. Avoid simply telling the reader about the changes in the timeline; show them through the characters' experiences.
- **Maintain Consistency**: Ensure that your writing is consistent with the established rules and principles of your alternate world. Avoid introducing elements that contradict the existing historical context.
'''
        return base_prompt + alternate_history_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a alternatehistory-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        alternatehistory_series_additions = """

## AlternateHistory Series-Specific Planning Elements

### Genre-Specific Series Development
- **AlternateHistory Conventions**: Ensure each book fulfills alternatehistory reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to alternatehistory
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to alternatehistory
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore alternatehistory themes with increasing depth and complexity

### AlternateHistory Series Continuity
- **Genre Elements**: Maintain consistent alternatehistory elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy alternatehistory readers
- **Series Identity**: Establish a strong series identity that feels authentically alternatehistory
- **World Building**: Develop the story world in ways that enhance the alternatehistory experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the alternatehistory genre

Create a alternatehistory series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + alternatehistory_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a alternatehistory-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class AlternateHistoryMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions for Alternate History novels.

        Args:
        **kwargs: Optional keyword arguments for customizing the prompt.  Can include:
        * title: The title of the book.
        * author: The author of the book.
        * point_of_divergence: A brief description of the key historical event that changed.
        * main_characters: A list or description of the main characters.
        * stakes: The high-stakes consequences of the altered timeline.
        * target_audience: (Optional) Specify if the target audience is more interested in military history, social commentary, etc.
        * tone: (Optional) The tone of the book (e.g., gritty, optimistic, satirical).

        Returns:
        str: A detailed prompt string for generating back cover copy.
        """

        title = kwargs.get('title', '[Title of Book]')
        author = kwargs.get('author', '[Author Name]')
        point_of_divergence = kwargs.get('point_of_divergence', '[Briefly describe the key historical event that changes]')
        main_characters = kwargs.get('main_characters', '[Describe the main characters and their roles]')
        stakes = kwargs.get('stakes', '[Describe the high-stakes consequences of the altered timeline]')
        target_audience = kwargs.get('target_audience', 'general audience')  # Default to general audience
        tone = kwargs.get('tone', 'serious') # Default to serious

        prompt = f"""
        Write a compelling back cover description for the Alternate History novel '{title}' by {author}.

        The core concept is: What if {point_of_divergence}?  This single change has rippled through history, creating a drastically different world.

        The story follows {main_characters}.  They are caught in the crosscurrents of this altered timeline and must navigate the challenges it presents.

        The stakes are incredibly high: {stakes}. The fate of nations, the course of technology, or even the very fabric of reality hangs in the balance.

        **Key elements to emphasize in the description:**

        *   **The 'What If?'**:  Clearly articulate the central point of divergence and its immediate consequences.  Don't just state it; make it intriguing.
        *   **Historical Realism (within the Alternate Reality)**: Ground the story in plausible historical details, even if those details are twisted or re-imagined. Readers expect a degree of believability.
        *   **Character-Driven Narrative**: Highlight the personal struggles and triumphs of the characters as they grapple with the altered world.  Focus on their emotional journey.
        *   **Sense of Wonder and Danger**:  Convey the excitement of exploring a familiar yet utterly different world, while also underscoring the dangers and uncertainties that lurk within it.
        *   **Intrigue and Mystery**:  Hint at hidden agendas, conspiracies, and unanswered questions that will keep readers turning the pages.
        *   **For {target_audience}:** Tailor the language and focus to appeal to this specific readership.  For example, if targeting military history enthusiasts, emphasize battles, strategies, and geopolitical implications. If targeting a more general audience, focus on the human drama and emotional impact.

        **Tone:** The overall tone should be {tone}. Consider the following:

        *   **Gritty/Dark:** Emphasize the harsh realities and moral compromises of the altered world.
        *   **Optimistic/Hopeful:** Highlight the potential for positive change and the resilience of the human spirit.
        *   **Satirical/Humorous:** Use wit and irony to critique historical events and societal norms.
        *   **Epic/Sweeping:** Convey the grand scale and scope of the altered timeline.

        **Structure:**

        1.  Start with a hook that immediately grabs the reader's attention and introduces the central premise.
        2.  Briefly describe the setting and the key characters.
        3.  Outline the central conflict and the stakes involved.
        4.  End with a question or a cliffhanger that leaves the reader wanting more.

        **Avoid:**

        *   Generic language and clichés.
        *   Spoilers that reveal key plot points.
        *   Excessive jargon or technical details.

        Write a description that is approximately 150-200 words.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating short, punchy descriptions (2-3 lines) for book recommendations.

        Args:
        **kwargs: Optional keyword arguments for customizing the prompt.
        * title: The title of the book.
        * author: The author of the book.
        * point_of_divergence: A one-sentence description of the point of divergence.
        * key_themes: Keywords related to the book's themes.

        Returns:
        str: A prompt string for generating short book descriptions.
        """

        title = kwargs.get('title', '[Title of Book]')
        author = kwargs.get('author', '[Author Name]')
        point_of_divergence = kwargs.get('point_of_divergence', '[One-sentence description of the point of divergence]')
        key_themes = kwargs.get('key_themes', '[List of keywords related to the book\'s themes]')

        prompt = f"""
        Write a very short (2-3 lines) description for the Alternate History novel '{title}' by {author}.  This description is for book recommendation purposes.

        The core 'what if' is: {point_of_divergence}.

        The key themes of the book are: {key_themes}.

        The description should be concise, intriguing, and highlight the unique aspects of the alternate history setting. Focus on creating a sense of wonder, danger, or curiosity.

        Examples:

        *   "Imagine a world where the Roman Empire never fell. Now, imagine the dark secrets hidden beneath its eternal glory."
        *   "What if the South had won the Civil War?  A gripping tale of a divided nation struggling to rebuild in the shadow of a Confederate superpower."
        *   "In a world where magic is real, the Great War is fought with spells and enchanted weapons.  But some secrets are better left buried."

        The description should make people want to read the book immediately.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating punchy marketing taglines for Alternate History novels.

        Args:
        **kwargs: Optional keyword arguments for customizing the prompt.
        * title: The title of the book.
        * point_of_divergence: A very short description of the point of divergence.
        * target_emotion: The primary emotion the tagline should evoke (e.g., fear, wonder, excitement).

        Returns:
        str: A prompt string for generating marketing taglines.
        """

        title = kwargs.get('title', '[Title of Book]')
        point_of_divergence = kwargs.get('point_of_divergence', '[Very short description of the point of divergence]')
        target_emotion = kwargs.get('target_emotion', 'wonder')

        prompt = f"""
        Generate several punchy marketing taglines for the Alternate History novel '{title}'.

        The core 'what if' is: {point_of_divergence}.

        The taglines should be short, memorable, and evoke a sense of {target_emotion}. They should capture the essence of the book and entice readers to learn more.

        Consider these examples:

        *   "History as you know it... never happened."
        *   "The past is a battlefield. And the war is just beginning."
        *   "One choice. A million possibilities.  An infinite war."
        *   "What if the world you know... was a lie?"
        *   "The future is rewritten.  The past is a weapon."

        The taglines should be no more than 10 words each. Generate at least 5 different options.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for providing visual style preferences for the book cover design.

        Args:
        **kwargs: Optional keyword arguments for customizing the prompt.
        * point_of_divergence: A short description of the point of divergence.
        * setting: The setting of the book (e.g., Victorian England, futuristic Tokyo).
        * dominant_colors: A list of dominant colors that reflect the tone and setting.
        * key_visual_elements: A list of key visual elements that should be included (e.g., airships, Roman soldiers, cyberpunk cityscapes).
        * target_audience: (Optional) Specify the target audience to tailor the visual style.

        Returns:
        str: A prompt string for visual style preferences.
        """

        point_of_divergence = kwargs.get('point_of_divergence', '[Short description of the point of divergence]')
        setting = kwargs.get('setting', '[The setting of the book]')
        dominant_colors = kwargs.get('dominant_colors', '[List of dominant colors]')
        key_visual_elements = kwargs.get('key_visual_elements', '[List of key visual elements]')
        target_audience = kwargs.get('target_audience', 'general audience')

        prompt = f"""
        Describe the desired visual style for the cover of an Alternate History novel.

        The core concept is: What if {point_of_divergence}?

        The setting is: {setting}.

        The dominant colors should be: {dominant_colors}. These colors should evoke the mood and atmosphere of the altered historical setting.

        Key visual elements to include are: {key_visual_elements}. These elements should immediately convey the alternate history nature of the story.

        **Consider the following aspects for the cover design:**

        *   **Historical Accuracy (with a Twist)**: The cover should maintain a degree of historical authenticity, but with clear visual cues that indicate the alternate timeline.
        *   **Genre Conventions**: Consider existing cover trends in Alternate History, but also strive for originality and a unique visual identity.
        *   **Typography**: Choose fonts that are appropriate for the historical period and the overall tone of the book.
        *   **Imagery**: Use high-quality imagery that is both visually appealing and relevant to the story.
        *   **Target Audience:** Consider the preferences of the target audience when selecting the visual style. For example, if the target audience is interested in steampunk, incorporate steampunk-inspired elements into the cover design.

        **Examples:**

        *   If the book explores a world where the Roman Empire never fell, the cover might feature a futuristic cityscape with Roman architectural influences.
        *   If the book is set in a Victorian England where magic is real, the cover might depict a gaslit street scene with wizards and enchanted objects.
        *   If the book explores a world where the South won the Civil War, the cover might feature a Confederate flag with a modern twist.

        Provide specific details about the desired mood, atmosphere, and overall aesthetic of the cover.  How does the cover visually communicate the 'what if' scenario to potential readers? How does it appeal to {target_audience}?
        """
        return prompt
        ```
        alternatehistory_book_additions = """

## AlternateHistory Series Book Integration

### AlternateHistory Continuity for This Book
- **Genre Consistency**: Maintain established alternatehistory elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to alternatehistory
- **Plot Advancement**: Continue series plot threads while telling a complete alternatehistory story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill alternatehistory reader expectations while advancing the series narrative

### Book-Specific AlternateHistory Focus
- **Central Conflict**: What alternatehistory-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new alternatehistory elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent alternatehistory while serving the series?

Ensure this book feels like an authentic continuation of the alternatehistory series while telling a complete, satisfying story.
"""

        return base_prompt + alternatehistory_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_series_book_prompt(**kwargs)
