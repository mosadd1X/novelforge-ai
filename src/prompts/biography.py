"""
Biography genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class BiographyPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Biography"
    GENRE_DESCRIPTION = "A biography is a detailed account of a person's life, written by someone else. It explores their experiences, achievements, failures, and impact on the world, aiming to provide a comprehensive and insightful portrait of the subject."
    
    GENRE_CHARACTERISTICS = [
        "Thorough Research: Based on extensive research, including primary and secondary sources, interviews, and archival materials.",
        "Chronological Narrative: Typically follows a chronological structure, tracing the subject's life from birth to death or the present day.",
        "Objective Perspective: Strives for objectivity, presenting a balanced view of the subject, acknowledging both strengths and weaknesses.",
        "Contextualization: Places the subject within their historical, social, and cultural context, explaining how these factors influenced their life and work.",
        "Psychological Insight: Explores the subject's motivations, personality traits, and inner conflicts, offering insights into their character.",
        "Anecdotal Evidence: Incorporates anecdotes, personal stories, and memorable incidents to bring the subject to life and illustrate key aspects of their personality.",
        "Analysis and Interpretation: Goes beyond mere recounting of events, offering analysis and interpretation of the subject's actions and decisions.",
        "Engaging Narrative: Presents the subject's life in a compelling and engaging manner, captivating the reader's attention and maintaining their interest.",
        "Source Citation: Provides clear and accurate citations for all sources used, ensuring transparency and credibility.",
        "Ethical Considerations: Addresses ethical considerations related to privacy, accuracy, and fairness in representing the subject's life."
    ]
    
    TYPICAL_ELEMENTS = [
        "Birth and Early Life: Details about the subject's birth, family background, and childhood experiences.",
        "Education and Intellectual Development: Information about the subject's education, intellectual influences, and formative experiences.",
        "Career and Achievements: A comprehensive account of the subject's career, accomplishments, and contributions to their field.",
        "Relationships and Personal Life: Exploration of the subject's relationships with family, friends, colleagues, and romantic partners.",
        "Challenges and Obstacles: Examination of the challenges, obstacles, and setbacks the subject faced throughout their life.",
        "Turning Points and Key Decisions: Identification of critical moments and decisions that shaped the subject's life and career.",
        "Public Image and Reputation: Analysis of the subject's public image, reputation, and impact on society.",
        "Legacy and Influence: Assessment of the subject's lasting legacy and influence on future generations.",
        "Personal Beliefs and Values: Exploration of the subject's personal beliefs, values, and philosophical outlook.",
        "Physical and Mental Health: Discussion of the subject's physical and mental health, including any illnesses or disabilities.",
        "Death and Memorialization: Account of the subject's death, funeral, and memorialization.",
        "Critical Reception: Overview of how the subject and their work were received by critics and the public."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Writing Considerations
- **Historical Accuracy**: Ensure meticulous accuracy in all historical details, dates, and events. Cross-reference multiple reliable sources to verify information.
- **Objectivity and Fairness**: Strive for objectivity in portraying the subject, avoiding hagiography or demonization. Present a balanced view, acknowledging both strengths and weaknesses.
- **Source Material Management**: Develop a robust system for managing and citing source materials, including primary documents, interviews, and secondary sources. Use footnotes, endnotes, or a bibliography to provide clear attribution.
- **Ethical Considerations**: Be mindful of ethical considerations related to privacy, confidentiality, and potential harm to living individuals. Obtain necessary permissions and approvals before publishing sensitive information.
- **Narrative Voice and Tone**: Choose a narrative voice and tone that is appropriate for the subject and the intended audience. Consider whether to adopt a formal, academic style or a more informal, accessible style.
- **Contextual Understanding**: Demonstrate a deep understanding of the historical, social, and cultural context in which the subject lived and worked. Explain how these factors influenced their life and achievements.
- **Psychological Depth**: Explore the subject's motivations, personality traits, and inner conflicts, offering insights into their character and behavior. Avoid speculative or unsubstantiated psychological interpretations.
- **Engaging Storytelling**: Craft a compelling and engaging narrative that captures the reader's attention and maintains their interest. Use vivid language, anecdotes, and memorable details to bring the subject to life.
'''
        return base_prompt + biography_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Outline Requirements
- **Chronological Structure**: Organize the outline chronologically, following the subject's life from birth to death or the present day. Divide the life into distinct periods or phases, such as childhood, adolescence, early career, and later years.
- **Key Events and Turning Points**: Identify key events and turning points in the subject's life that had a significant impact on their development and career. Dedicate specific chapters or sections to these pivotal moments.
- **Thematic Organization**: Consider incorporating thematic elements into the outline, such as the subject's relationship with family, their intellectual development, or their contributions to society.
- **Relationship Mapping**: Include sections that specifically explore the subject's relationships with key individuals, such as family members, friends, mentors, and rivals. Analyze the dynamics of these relationships and their impact on the subject's life.
- **Contextual Background**: Integrate contextual background information into the outline, providing historical, social, and cultural context for the subject's life and work.
- **Source Material Integration**: Indicate where specific source materials will be used in each chapter or section, ensuring that the narrative is grounded in evidence and research.
- **Analysis and Interpretation**: Include sections that offer analysis and interpretation of the subject's actions, decisions, and legacy. Avoid simply recounting events; instead, provide insights and perspectives.
- **Conclusion and Reflection**: End the outline with a conclusion that summarizes the subject's life and legacy, reflecting on their impact and significance.
'''
        return base_prompt + biography_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Character Development
- **Authenticity and Accuracy**: Prioritize authenticity and accuracy in portraying the subject's character. Base all characterizations on verifiable evidence and reliable sources.
- **Complexity and Nuance**: Avoid simplistic or one-dimensional portrayals. Acknowledge the subject's complexities, contradictions, and internal conflicts.
- **Psychological Depth**: Explore the subject's motivations, personality traits, and emotional responses. Use psychological insights to illuminate their character and behavior.
- **Voice and Dialogue**: Recreate the subject's voice and dialogue as accurately as possible, drawing on primary sources such as letters, speeches, and interviews.
- **Physical Description**: Provide a detailed physical description of the subject, based on photographs, portraits, and eyewitness accounts.
- **Habits and Mannerisms**: Include details about the subject's habits, mannerisms, and quirks, adding depth and personality to the portrayal.
- **Relationships and Interactions**: Show how the subject interacted with others, highlighting their relationships with family, friends, colleagues, and rivals.
- **Evolution and Change**: Trace the evolution of the subject's character over time, showing how they changed and developed in response to their experiences.
'''
        return base_prompt + biography_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Chapter Writing
- **Contextual Setting**: Begin each chapter by establishing the historical, social, and cultural context in which the events take place.
- **Chronological Flow**: Maintain a clear chronological flow, guiding the reader through the subject's life in a logical and coherent manner.
- **Anecdotal Integration**: Incorporate anecdotes, personal stories, and memorable incidents to bring the subject to life and illustrate key aspects of their personality.
- **Source Material Incorporation**: Seamlessly integrate source material into the narrative, using quotes, paraphrases, and summaries to support your claims.
- **Descriptive Language**: Use vivid and descriptive language to paint a picture of the subject's world, capturing the sights, sounds, and smells of their environment.
- **Emotional Resonance**: Evoke emotional resonance in the reader, allowing them to connect with the subject on a personal level.
- **Analytical Insights**: Offer analytical insights and interpretations of the subject's actions and decisions, providing context and meaning.
- **Transition Smoothly**: Transition smoothly between different topics and time periods, maintaining a consistent narrative flow.
- **Concluding Summary**: End each chapter with a brief summary of the key events and themes, preparing the reader for the next stage of the subject's life.
'''
        return base_prompt + biography_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a biography-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        biography_series_additions = """

## Biography Series-Specific Planning Elements

### Educational Progression for Biography
- **Knowledge Building**: Structure learning progression appropriate for biography topics
- **Expertise Development**: Guide readers from basic to advanced understanding of biography subjects
- **Practical Applications**: Include actionable insights specific to biography throughout the series
- **Research Depth**: Plan comprehensive research appropriate for biography authority
- **Reader Value**: Ensure each book provides significant biography value while building series knowledge

### Biography Series Continuity
- **Subject Consistency**: Maintain consistent approach to biography topics across books
- **Authority Building**: Establish and maintain credibility in biography throughout the series
- **Information Architecture**: Structure information flow appropriate for biography learning
- **Cross-References**: Create meaningful connections between biography concepts across books
- **Updated Knowledge**: Plan for incorporating new biography research and developments

Create a biography series that provides comprehensive education with authoritative, well-researched content.
"""
        
        return base_prompt + biography_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a biography-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        biography_book_additions = """

## Biography Series Book Integration

### Biography Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon biography concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous biography books when relevant
- **Knowledge Progression**: Advance reader understanding of biography topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the biography series

### Book-Specific Biography Focus
- **Educational Objectives**: What specific biography knowledge will readers gain from this book?
- **Practical Applications**: What actionable biography insights will be provided?
- **Research Integration**: How will new biography research be incorporated?
- **Series Advancement**: How does this book advance the overall biography education series?
- **Reader Value**: What unique biography value does this book add to the series?

Ensure this book provides comprehensive biography education while serving as an integral part of the learning series.
"""
        
        return base_prompt + biography_book_additions

        ```python
        class BiographyMarketing:
        """
        A class containing methods for generating back cover copy and marketing materials for biographies.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling biography back cover descriptions.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., subject_name, subject_occupation,
        key_events, themes, target_audience).

        Returns:
        str: A detailed prompt string tailored for biography back cover copy generation.
        """
        prompt = f"""
        You are a skilled biographer and marketing copywriter. Your task is to craft a captivating back cover description for a biography.
        The goal is to entice readers to purchase the book by highlighting the subject's extraordinary life and its relevance to the reader.

        Here are the key elements to include:

        1.  **Intriguing Hook:** Begin with a captivating opening that grabs the reader's attention. Consider a thought-provoking question, a striking statement, or a glimpse into a pivotal moment in the subject's life.

        2.  **Subject Introduction:** Clearly introduce the subject of the biography. Mention their full name and a brief description of their occupation or claim to fame.  Emphasize what made them a significant figure in history or culture.

        3.  **Life's Journey:** Briefly outline the subject's life journey, highlighting key milestones, challenges, and triumphs. Focus on the most compelling and dramatic aspects of their story.  Consider including:
        *   Early life and formative experiences.
        *   Significant achievements and contributions.
        *   Major obstacles overcome.
        *   Key relationships and influences.
        *   Moments of crisis and transformation.

        4.  **Themes and Relevance:** Identify and emphasize the universal themes explored in the biography. Consider themes such as ambition, resilience, love, loss, legacy, social justice, or the pursuit of knowledge. Explain how the subject's life resonates with contemporary readers and offers valuable insights into the human condition.

        5.  **Unique Angle:** Highlight what makes this particular biography unique. Does it offer new perspectives, previously unpublished information, or a fresh interpretation of the subject's life?

        6.  **Emotional Resonance:** Evoke emotions in the reader.  Use vivid language and imagery to bring the subject's story to life.  Consider focusing on:
        *   The subject's passions and motivations.
        *   The emotional impact of their experiences.
        *   The sacrifices they made.
        *   The challenges they faced with courage and determination.

        7.  **Target Audience:** Consider the target audience for the biography. Are you writing for history buffs, fans of a particular field, or readers interested in personal growth and inspiration? Tailor the language and tone to appeal to the specific audience.

        8.  **Intriguing Question/Call to Action:** End with a compelling question or a call to action that leaves the reader wanting more.  For example:
        *   "What drove [Subject Name] to achieve such extraordinary feats?"
        *   "Discover the untold story behind one of history's most enigmatic figures."
        *   "Journey into the life of [Subject Name] and uncover the secrets to their enduring legacy."

        9.  **Keep it Concise:** Aim for a length of approximately 150-200 words. Every word should contribute to enticing the reader.

        10. **Biography-Specific Considerations:**
        * Emphasize the truth and authenticity of the narrative.
        * Highlight the depth of research undertaken by the author.
        * Convey the impact of the subject's life on the world.
        * Consider using quotes from the subject or from people who knew them.

        Subject Name: {kwargs.get('subject_name', '[Subject Name]')}
        Subject Occupation: {kwargs.get('subject_occupation', '[Subject Occupation]')}
        Key Events: {kwargs.get('key_events', '[Key Events in Subject\'s Life]')}
        Themes: {kwargs.get('themes', '[Themes explored in the Biography]')}
        Target Audience: {kwargs.get('target_audience', '[Target Audience]')}
        Unique Angle: {kwargs.get('unique_angle', '[Unique aspects of this Biography]')}

        Write a compelling back cover description that will captivate readers and convince them to buy this book.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, punchy biography description (2-3 lines) for recommendation lists.

        Args:
        **kwargs: Keyword arguments to customize the prompt.

        Returns:
        str: A prompt string for generating concise biography descriptions.
        """
        prompt = f"""
        You are writing a very short (2-3 line) description of a biography for use in recommendation lists or online stores. The goal is to quickly grab the reader's attention and pique their interest.

        Key elements to include:

        1. **Subject and Significance:** Immediately identify the subject of the biography and a key reason why they are noteworthy.

        2. **Central Conflict/Achievement:** Briefly hint at a major challenge they faced or a significant achievement they accomplished.

        3. **Intriguing Hook:** End with a question, a provocative statement, or a hint of the book's emotional core to leave the reader wanting more.

        4. **Biography-Specific Considerations:**
        * Emphasize the real-life nature of the story.
        * Focus on the impact and legacy of the subject.

        Subject Name: {kwargs.get('subject_name', '[Subject Name]')}
        Subject Occupation: {kwargs.get('subject_occupation', '[Subject Occupation]')}
        Key Achievement/Conflict: {kwargs.get('key_achievement_conflict', '[Key Achievement or Conflict]')}

        Example:
        "Discover the untold story of Marie Curie, a pioneer in radioactivity.  Fighting sexism and adversity, she changed the world with her discoveries. But at what cost?"

        Write a very short and compelling biography description.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a biography.

        Args:
        **kwargs: Keyword arguments to customize the prompt.

        Returns:
        str: A prompt string for generating biography taglines.
        """
        prompt = f"""
        You are crafting a short, memorable marketing tagline for a biography. The goal is to capture the essence of the subject's life and the book's appeal in a few powerful words.

        Key elements to include:

        1. **Core Theme:** Identify the central theme or message of the biography. What is the most compelling aspect of the subject's life?

        2. **Emotional Hook:** Evoke an emotional response in the reader. Consider using words that convey inspiration, drama, intrigue, or empathy.

        3. **Conciseness:** Keep the tagline short and easy to remember. Aim for 5-10 words.

        4. **Biography-Specific Considerations:**
        *  Emphasize the authenticity and historical significance of the story.
        *  Highlight the subject's impact on the world.

        Subject Name: {kwargs.get('subject_name', '[Subject Name]')}
        Subject Occupation: {kwargs.get('subject_occupation', '[Subject Occupation]')}
        Core Theme: {kwargs.get('core_theme', '[Core Theme of the Biography]')}

        Examples:
        *   "The untold story. The unyielding spirit." (Biography of a resilient figure)
        *   "A life of passion. A legacy of change." (Biography of a transformative leader)
        *   "Truth is stranger than fiction." (If the subject's life was exceptionally unusual)

        Write a compelling and memorable marketing tagline.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt outlining visual style preferences for a biography's back cover design.

        Args:
        **kwargs: Keyword arguments to customize the prompt.

        Returns:
        str: A prompt string for guiding the visual design of a biography back cover.
        """
        prompt = f"""
        You are an art director providing guidance for the visual design of a biography's back cover. Consider the following elements to create a visually appealing and genre-appropriate design:

        1. **Overall Tone:**  The design should reflect the tone and subject matter of the biography. Is it a serious and scholarly work, or a more accessible and popular account?  Consider using words like:  "Serious", "Scholarly", "Intimate", "Inspirational", "Dramatic", "Historical".

        2. **Imagery:**  Suggest appropriate imagery to use on the back cover. Consider:
        *   A portrait of the subject (if available and high-quality).
        *   Images related to their work or accomplishments.
        *   Historical photographs or illustrations.
        *   Symbolic imagery that reflects the themes of the biography.
        *   Avoid overly stylized or modern images if the biography is historical.

        3. **Typography:**  Recommend font styles that are appropriate for the biography's subject matter.
        *   Consider classic and elegant fonts for historical biographies.
        *   Use more modern and bold fonts for biographies of contemporary figures.
        *   Ensure the font is legible and easy to read.

        4. **Color Palette:**  Suggest a color palette that complements the imagery and reinforces the overall tone.
        *   Consider using muted colors for historical biographies.
        *   Use brighter and more vibrant colors for biographies of inspiring figures.
        *   Ensure the colors are harmonious and visually appealing.

        5. **Layout:**  Provide general layout guidelines for the back cover.
        *   Ensure the text is well-organized and easy to read.
        *   Use visual hierarchy to draw the reader's eye to the most important elements.
        *   Avoid clutter and maintain a clean and professional design.

        6. **Biography-Specific Considerations:**
        *   Strive for authenticity and historical accuracy in the visual design.
        *   Consider incorporating elements that reflect the subject's personality and achievements.
        *   Research covers of similar biographies for inspiration.

        Subject Name: {kwargs.get('subject_name', '[Subject Name]')}
        Subject Occupation: {kwargs.get('subject_occupation', '[Subject Occupation]')}
        Overall Tone: {kwargs.get('overall_tone', '[Overall Tone of the Biography]')}
        Imagery Suggestions: {kwargs.get('imagery_suggestions', '[Suggestions for Imagery]')}
        Font Style Preferences: {kwargs.get('font_style_preferences', '[Font Style Preferences]')}
        Color Palette Preferences: {kwargs.get('color_palette_preferences', '[Color Palette Preferences]')}

        Provide detailed visual style preferences for the back cover design.
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return BiographyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return BiographyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return BiographyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return BiographyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return BiographyPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return BiographyPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return BiographyPrompts.get_series_book_prompt(**kwargs)
