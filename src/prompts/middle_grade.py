"""
Middle Grade genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class MiddleGradePrompts(FictionBasePrompts):
    GENRE_NAME = "Middle Grade"
    GENRE_DESCRIPTION = "Middle Grade fiction is aimed at readers aged 8-12. It typically features protagonists in this age range who are navigating challenges related to friendship, family, self-discovery, and the transition to adolescence. The tone is generally optimistic and hopeful, with age-appropriate themes and language. While conflict exists, resolutions are usually positive and emphasize growth and learning."
    
    GENRE_CHARACTERISTICS = [
        "Protagonist is typically between 8 and 12 years old, facing relatable challenges.",
        "Focus on themes of friendship, family, identity, and navigating social dynamics.",
        "Clear and straightforward prose, avoiding complex sentence structures or overly descriptive language.",
        "Optimistic and hopeful tone, even when dealing with difficult subjects.",
        "Age-appropriate themes and content, avoiding mature or graphic material.",
        "Strong emphasis on character development and growth.",
        "Plot-driven stories with a clear beginning, middle, and end.",
        "Presence of a moral or lesson, subtly woven into the narrative.",
        "Relatable and engaging voice that resonates with young readers.",
        "Limited use of complex world-building or intricate plotlines, unless specifically geared toward fantasy or adventure subgenres within Middle Grade."
    ]
    
    TYPICAL_ELEMENTS = [
        "A relatable protagonist with flaws and strengths.",
        "A clear and compelling central conflict.",
        "Supportive and/or challenging friendships.",
        "Family dynamics that influence the protagonist's journey.",
        "A school setting or school-related events.",
        "A mentor figure (teacher, grandparent, etc.) who provides guidance.",
        "Moments of humor and lightheartedness.",
        "Opportunities for the protagonist to learn and grow.",
        "A satisfying resolution that ties up loose ends.",
        "A clear sense of right and wrong.",
        "Elements of mystery, adventure, or fantasy (depending on the subgenre).",
        "A theme or message about the importance of kindness, empathy, or perseverance."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Writing Considerations
- **Voice and Tone**: Maintain a voice that is engaging and relatable to 8-12 year olds. Avoid condescending language or overly complex vocabulary. The tone should be generally optimistic and hopeful, even when addressing difficult topics.
- **Character Development**: Focus on creating believable and relatable characters with clear motivations and flaws. Show their growth and development throughout the story.
- **Plot Structure**: Ensure a clear and compelling plot with a well-defined beginning, middle, and end. The pacing should be appropriate for the target age group, avoiding overly slow or rushed sections.
- **Theme and Message**: Subtly weave a positive message or theme into the story, such as the importance of friendship, family, or perseverance. Avoid being preachy or didactic.
- **Age-Appropriateness**: Carefully consider the age-appropriateness of the themes, language, and content. Avoid mature or graphic material that is not suitable for young readers.
- **Worldbuilding (if applicable)**: If the story involves fantasy or science fiction elements, keep the worldbuilding relatively simple and easy to understand. Focus on the aspects that are most relevant to the plot and characters.
- **Humor**: Incorporate age-appropriate humor to keep the story engaging and entertaining. This could include witty dialogue, funny situations, or relatable observations.
- **Emotional Resonance**: Aim to create an emotional connection with the reader by exploring relatable feelings and experiences, such as joy, sadness, fear, and excitement.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Outline Requirements
- **Inciting Incident**: The inciting incident should be clear and engaging, immediately drawing the reader into the story. It should present a problem or challenge that the protagonist must overcome.
- **Rising Action**: The rising action should consist of a series of escalating events that build tension and suspense. Each event should present new obstacles or challenges for the protagonist.
- **Midpoint**: The midpoint should mark a significant turning point in the story, where the protagonist gains new knowledge or insight that changes their perspective or approach.
- **Climax**: The climax should be the most exciting and suspenseful part of the story, where the protagonist confronts the main antagonist or challenge.
- **Falling Action**: The falling action should consist of the events that lead to the resolution of the conflict. It should show the consequences of the protagonist's actions and the impact on their relationships.
- **Resolution**: The resolution should provide a satisfying conclusion to the story, tying up loose ends and showing the protagonist's growth and development. It should leave the reader with a sense of hope and optimism.
- **Subplots (if applicable)**: Subplots should be carefully integrated into the main plot, adding depth and complexity to the story without overwhelming the reader. They should contribute to the overall themes and message of the book.
- **Chapter Breaks**: Consider where to break chapters to maintain pacing and reader engagement. End chapters on cliffhangers or moments of suspense to encourage readers to keep turning the pages.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Character Development
- **Relatability**: Ensure the protagonist is relatable to middle grade readers. Give them flaws, insecurities, and relatable struggles that resonate with the target audience.
- **Motivation**: Clearly define the protagonist's motivations and goals. What do they want to achieve, and why is it important to them?
- **Growth**: Show the protagonist's growth and development throughout the story. How do they change and learn from their experiences?
- **Supporting Characters**: Develop well-rounded supporting characters who play a significant role in the protagonist's journey. Give them their own motivations and backstories.
- **Antagonist**: Create a compelling antagonist who presents a clear obstacle for the protagonist to overcome. The antagonist should have believable motivations, even if they are misguided.
- **Friendships**: Explore the dynamics of friendships, both positive and negative. Show the importance of loyalty, trust, and communication in building strong relationships.
- **Family**: Depict family relationships in a realistic and nuanced way. Show the impact of family dynamics on the protagonist's life and choices.
- **Voice**: Give each character a distinct voice and personality. Use dialogue and actions to reveal their individual traits and quirks.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        middle_grade_additions = '''
## Middle Grade-Specific Chapter Writing
- **Clear Focus**: Each chapter should have a clear focus and purpose, advancing the plot or developing the characters.
- **Engaging Opening**: Start each chapter with an engaging hook that grabs the reader's attention and makes them want to keep reading.
- **Pacing**: Maintain a good pace throughout the chapter, avoiding overly long descriptions or slow-moving scenes.
- **Dialogue**: Use dialogue to reveal character, advance the plot, and add humor or tension. Keep dialogue natural and age-appropriate.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show the reader what is happening, rather than simply telling them.
- **Conflict and Tension**: Incorporate conflict and tension into each chapter to keep the reader engaged. This could be internal conflict, external conflict, or a combination of both.
- **Cliffhangers**: End chapters on cliffhangers or moments of suspense to encourage readers to keep turning the pages.
- **Age-Appropriate Language**: Use language that is appropriate for the target age group, avoiding overly complex vocabulary or mature themes.
'''
        return base_prompt + middle_grade_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a middlegrade-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        middlegrade_series_additions = """

## MiddleGrade Series-Specific Planning Elements

### Genre-Specific Series Development
- **MiddleGrade Conventions**: Ensure each book fulfills middlegrade reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to middlegrade
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to middlegrade
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore middlegrade themes with increasing depth and complexity

### MiddleGrade Series Continuity
- **Genre Elements**: Maintain consistent middlegrade elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy middlegrade readers
- **Series Identity**: Establish a strong series identity that feels authentically middlegrade
- **World Building**: Develop the story world in ways that enhance the middlegrade experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the middlegrade genre

Create a middlegrade series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + middlegrade_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a middlegrade-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class MiddleGradeMarketing:
        """
        A class containing methods for generating marketing prompts
        specifically tailored for Middle Grade books.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions
        for Middle Grade novels.

        Args:
        **kwargs: Keyword arguments containing book details such as title, author,
        main character name, setting, problem/conflict, stakes,
        themes, target audience age range, and comparable titles.

        Returns:
        str: A detailed prompt string.
        """
        prompt = f"""
        Write an engaging and age-appropriate back cover description for a Middle Grade novel.
        The target audience is readers aged {kwargs.get('target_audience_age_range', '8-12')}.
        The book's title is "{kwargs.get('title', '[Title]')}," and it's written by {kwargs.get('author', '[Author]')}.

        Here's what you need to include:

        1.  **Introduce the Main Character:**  A likable and relatable character named {kwargs.get('main_character_name', '[Main Character Name]')}.
        *   Highlight their age, personality, and any unique quirks or talents.  Focus on what makes them relatable to Middle Grade readers.

        2.  **Set the Scene:**  Describe the setting, which is {kwargs.get('setting', '[Setting]')} in a vivid and imaginative way.
        *   Make it appealing and intriguing to young readers.  Consider adding elements of mystery or adventure.

        3.  **Present the Problem/Conflict:** Clearly outline the main problem or conflict that the main character faces, which is {kwargs.get('problem_conflict', '[Problem/Conflict]')}.
        *   This should be something that Middle Grade readers can connect with – friendship issues, family problems, school challenges, or a quest for self-discovery.
        *   Avoid overly complex or mature themes.

        4.  **Raise the Stakes:** Explain what's at stake if the character fails to overcome the problem. What will happen? What will they lose?
        *   The stakes should be meaningful to the character and relatable to the target audience.
        *   Examples: losing a friendship, failing a grade, letting down their family, or failing to save something important.

        5.  **Hint at the Journey:**  Tease the adventure or journey the character will embark on to solve the problem.
        *   Focus on the excitement, challenges, and discoveries they will make along the way.

        6.  **Emotional Hook:**  Tap into the emotions that Middle Grade readers experience: friendship, courage, loyalty, fear, hope, and determination.
        *   Use language that resonates with their emotional world.

        7.  **End with a Question:**  Leave the reader with a compelling question that makes them want to know more.
        *   Examples:  "Can [Main Character Name] overcome their fears and save the day?" or "Will [Main Character Name] ever find true friendship?"

        8.  **Middle Grade Tone:** Keep the tone light, engaging, and age-appropriate. Avoid sarcasm, cynicism, or overly complex language.
        *   Focus on themes of friendship, family, self-discovery, and overcoming challenges.

        9.  **Comparable Titles:** Books similar in style or theme to this one include: {kwargs.get('comparable_titles', '[Comparable Titles, e.g., Percy Jackson, Wonder, The Hobbit]')}.  Use these as inspiration for tone and style.

        10. **Themes:** The main themes of the book are: {kwargs.get('themes', '[Themes, e.g., Friendship, Courage, Self-Discovery]')}. Emphasize these themes in a way that resonates with middle grade readers.

        The back cover description should be approximately 150-200 words. Focus on creating a sense of wonder, excitement, and emotional connection for young readers.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, catchy 2-3 line book recommendation
        specifically for Middle Grade readers.

        Args:
        **kwargs: Keyword arguments containing book details like title, main character, and main conflict.

        Returns:
        str: A detailed prompt string.
        """
        prompt = f"""
        Write a short, catchy 2-3 line book recommendation for a Middle Grade novel aimed at readers aged {kwargs.get('target_audience_age_range', '8-12')}.
        The book's title is "{kwargs.get('title', '[Title]')}," and the main character is {kwargs.get('main_character_name', '[Main Character Name]')}.
        The core conflict is {kwargs.get('problem_conflict', '[Problem/Conflict]')}.

        Guidelines:

        1.  **Focus on the Hook:** Start with a strong hook that grabs the reader's attention.
        2.  **Highlight the Adventure:** Emphasize the exciting and adventurous elements of the story.
        3.  **Relatable Character:** Showcase the main character's relatability and the challenges they face.
        4.  **Keep it Concise:** Use simple, clear language that Middle Grade readers can easily understand.
        5.  **Positive Tone:** Maintain an upbeat and positive tone.

        Example:
        "[Main Character Name] thought middle school was tough enough... until they discovered a secret portal to a magical world!
        Now, they must team up with unlikely friends to save both worlds from a looming darkness.
        Get ready for an adventure filled with friendship, courage, and a whole lot of magic!"

        Another Example:
        "When [Main Character Name] discovers a hidden talent, everything changes!
        But can they overcome their fears and use their newfound ability to help their friends and their town?
        A heartwarming story about self-discovery, friendship, and believing in yourself!"
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a Middle Grade book.

        Args:
        **kwargs: Keyword arguments containing the book's core themes and target audience.

        Returns:
        str: A detailed prompt string.
        """
        prompt = f"""
        Write a punchy and memorable marketing tagline for a Middle Grade book.
        The target audience is readers aged {kwargs.get('target_audience_age_range', '8-12')}.
        The book's core themes are: {kwargs.get('themes', '[Themes, e.g., Friendship, Courage, Self-Discovery]')}.

        Guidelines:

        1.  **Keep it Short and Sweet:** Taglines should be concise and easy to remember (ideally under 10 words).
        2.  **Highlight the Appeal:** Focus on what makes the book exciting, adventurous, or heartwarming.
        3.  **Use Action Words:** Incorporate action verbs that create a sense of energy and excitement.
        4.  **Relatability:** Hint at the relatable experiences and emotions of the characters.
        5.  **Intrigue:** Leave the reader wanting to know more.

        Examples:

        *   "Adventure awaits. Friendship triumphs."
        *   "Unlock your courage. Discover your magic."
        *   "The adventure of a lifetime starts now!"
        *   "Believe in yourself. Believe in your friends."
        *   "Middle school just got a whole lot weirder."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for guiding the visual design of a Middle Grade book's back cover.

        Args:
        **kwargs: Keyword arguments containing information about the book's tone, themes, and target audience.

        Returns:
        str: A detailed prompt string.
        """
        prompt = f"""
        Provide guidance for the visual style of a Middle Grade book's back cover.
        The target audience is readers aged {kwargs.get('target_audience_age_range', '8-12')}.
        The book's tone is {kwargs.get('tone', '[Tone, e.g., adventurous, heartwarming, mysterious]')}.
        The book's core themes are: {kwargs.get('themes', '[Themes, e.g., Friendship, Courage, Self-Discovery]')}.

        Guidelines:

        1.  **Color Palette:** Suggest a color palette that aligns with the book's tone and themes.
        *   For example:
        *   Adventurous: Bright and vibrant colors like blues, greens, and yellows.
        *   Heartwarming: Warm and inviting colors like oranges, pinks, and soft yellows.
        *   Mysterious: Cool and muted colors like blues, purples, and grays.
        2.  **Imagery:** Describe the types of images or illustrations that would be appropriate.
        *   Consider using illustrations that capture the main character, the setting, or a key moment in the story.
        *   Illustrations should be age-appropriate and appealing to Middle Grade readers.
        *   Examples:
        *   Cartoony and whimsical illustrations
        *   Realistic but slightly stylized illustrations
        *   Illustrations that evoke a sense of wonder and imagination
        3.  **Typography:** Recommend font styles that are legible and visually appealing to Middle Grade readers.
        *   Avoid overly complex or difficult-to-read fonts.
        *   Consider using a playful or slightly quirky font that reflects the book's tone.
        4.  **Overall Design:** The overall design should be clean, uncluttered, and visually engaging.
        *   Use white space effectively to create a sense of balance and readability.
        *   Make sure the title and author's name are prominent and easy to read.
        5.  **Consider the Theme:** Think about how the visual elements can reinforce the book's core themes.
        *   For example, if the book is about friendship, the cover could feature images of the main characters together.
        *   If the book is about courage, the cover could feature an image of the main character facing a challenge.

        Example:

        "The back cover should have a vibrant and playful design, appealing to young readers. Use bright blues and greens to evoke a sense of adventure. Include an illustration of [Main Character Name] looking determined and ready to explore. The font should be easy to read and slightly whimsical. The overall design should feel energetic and inviting."
        """
        return prompt
        ```
        middlegrade_book_additions = """

## MiddleGrade Series Book Integration

### MiddleGrade Continuity for This Book
- **Genre Consistency**: Maintain established middlegrade elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to middlegrade
- **Plot Advancement**: Continue series plot threads while telling a complete middlegrade story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill middlegrade reader expectations while advancing the series narrative

### Book-Specific MiddleGrade Focus
- **Central Conflict**: What middlegrade-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new middlegrade elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent middlegrade while serving the series?

Ensure this book feels like an authentic continuation of the middlegrade series while telling a complete, satisfying story.
"""

        return base_prompt + middlegrade_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return MiddleGradePrompts.get_series_book_prompt(**kwargs)
