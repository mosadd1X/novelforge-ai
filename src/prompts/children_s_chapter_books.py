"""
Children's Chapter Books genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ChildrenSChapterBooksPrompts(FictionBasePrompts):
    GENRE_NAME = "Children's Chapter Books"
    GENRE_DESCRIPTION = "Children's chapter books are designed for young readers transitioning from picture books to longer narratives. They typically feature simple plots, relatable characters, and age-appropriate themes, divided into easily digestible chapters. The language is accessible, and the stories often focus on themes of friendship, family, problem-solving, and self-discovery, with a clear and satisfying resolution."

    GENRE_CHARACTERISTICS = [
        "Simple and straightforward plotlines that are easy for young readers to follow.",
        "Relatable and age-appropriate characters, often children or animals, with clear motivations and flaws.",
        "Focus on themes of friendship, family, school, and personal growth.",
        "Clear and concise language with limited complex vocabulary or sentence structures.",
        "Positive and optimistic tone, often with a focus on problem-solving and overcoming challenges.",
        "Shorter chapters that provide natural stopping points and encourage reading progress.",
        "Illustrations interspersed throughout the text to break up the narrative and enhance engagement.",
        "A clear moral or lesson, often subtly woven into the story.",
        "Limited subplots to avoid overwhelming young readers.",
        "A satisfying and age-appropriate resolution to the central conflict."
    ]

    TYPICAL_ELEMENTS = [
        "A protagonist who is a child or animal facing a relatable challenge.",
        "A supportive cast of friends, family members, or mentors.",
        "A clear antagonist or obstacle that the protagonist must overcome.",
        "A series of events or adventures that lead to the resolution of the conflict.",
        "A turning point or moment of realization for the protagonist.",
        "A satisfying resolution that reinforces positive values.",
        "Humorous elements or situations to engage young readers.",
        "Descriptive language that paints a vivid picture of the setting and characters.",
        "Dialogue that is realistic and age-appropriate.",
        "Illustrations that complement the text and enhance the story.",
        "Chapters that end on a cliffhanger or with a question to encourage further reading.",
        "Themes of kindness, empathy, and perseverance."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        children_s_chapter_books_additions = '''
## Children's Chapter Books-Specific Writing Considerations
- **Key Aspect 1: Age Appropriateness**: Ensure all content, including vocabulary, themes, and plot complexity, is suitable for the target age range (typically 6-10 years old). Avoid mature themes or overly complex sentence structures.
- **Key Aspect 2: Relatability**: Create characters and situations that young readers can easily relate to, drawing on common childhood experiences and emotions.
- **Key Aspect 3: Positive Messaging**: Focus on positive values such as friendship, kindness, perseverance, and problem-solving. Avoid negativity or cynicism.
- **Key Aspect 4: Clear and Concise Language**: Use simple, straightforward language with limited jargon or figurative language. Keep sentences short and easy to understand.
- **Key Aspect 5: Engaging Tone**: Maintain an engaging and upbeat tone that will capture and hold the reader's attention. Use humor and vivid descriptions to bring the story to life.
- **Key Aspect 6: Visual Appeal**: Consider how illustrations can enhance the story and break up the text. Work with an illustrator to create images that complement the narrative.
- **Key Aspect 7: Chapter Length**: Keep chapters relatively short (5-10 pages) to provide natural stopping points and encourage reading progress.
- **Key Aspect 8: Moral of the Story**: Subtly weave a moral or lesson into the story without being preachy or didactic. Let the characters' actions and experiences speak for themselves.
'''
        return base_prompt + children_s_chapter_books_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        children_s_chapter_books_additions = '''
## Children's Chapter Books-Specific Outline Requirements
- **Structure Element 1: Clear Beginning, Middle, and End**: Ensure the story has a well-defined beginning that introduces the characters and setting, a middle that develops the conflict, and an end that resolves the conflict in a satisfying way.
- **Structure Element 2: Chapter Breakdown**: Plan out each chapter with a specific goal in mind, such as introducing a new character, advancing the plot, or building suspense.
- **Structure Element 3: Rising Action**: Build tension gradually throughout the story, leading to a climax or turning point.
- **Structure Element 4: Conflict and Resolution**: Clearly define the central conflict and how the protagonist will overcome it.
- **Structure Element 5: Subplot Limitation**: Avoid complex subplots that could confuse young readers. Focus on the main storyline.
- **Structure Element 6: Pacing**: Maintain a brisk pace to keep readers engaged. Avoid lengthy descriptions or unnecessary details.
- **Structure Element 7: Cliffhangers**: Consider ending chapters on a cliffhanger or with a question to encourage further reading.
- **Structure Element 8: Emotional Arc**: Map out the emotional journey of the protagonist, showing how they grow and change throughout the story.

**Detailed Outline Guidance:**

1.  **Introduction:**
    *   Introduce the main character(s) and their world.
    *   Establish the setting and time period.
    *   Hint at the central conflict or problem.

2.  **Rising Action:**
    *   The protagonist encounters a challenge or obstacle.
    *   The protagonist attempts to solve the problem, but faces setbacks.
    *   New characters are introduced who may help or hinder the protagonist.
    *   The stakes are raised as the story progresses.

3.  **Climax:**
    *   The protagonist faces their greatest challenge or fear.
    *   A turning point occurs that changes the course of the story.

4.  **Falling Action:**
    *   The protagonist works to resolve the conflict.
    *   Loose ends are tied up.

5.  **Resolution:**
    *   The conflict is resolved in a satisfying way.
    *   The protagonist learns a valuable lesson.
    *   The story ends on a positive and hopeful note.
'''
        return base_prompt + children_s_chapter_books_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)

        children_s_chapter_books_additions = '''
## Children's Chapter Books-Specific Character Development
- **Character Aspect 1: Relatable Flaws**: Give your characters relatable flaws and weaknesses that make them more human and sympathetic.
- **Character Aspect 2: Clear Motivations**: Ensure your characters have clear motivations and goals that drive their actions.
- **Character Aspect 3: Age-Appropriate Behavior**: Make sure your characters behave in a way that is consistent with their age and maturity level.
- **Character Aspect 4: Growth and Change**: Show how your characters grow and change throughout the story as a result of their experiences.
- **Character Aspect 5: Distinct Personalities**: Give each character a distinct personality and voice that makes them memorable.
- **Character Aspect 6: Positive Role Models**: Create characters who embody positive values such as kindness, courage, and perseverance.
- **Character Aspect 7: Character Backstories**: Develop brief backstories for your main characters to understand their motivations and behaviors better.
- **Character Aspect 8: Character Relationships**: Explore the relationships between your characters and how they influence each other.

**Detailed Character Guidance:**

*   **Protagonist:**
    *   A child or animal who is relatable and sympathetic.
    *   Faces a challenge or problem that they must overcome.
    *   Undergoes a transformation or learns a valuable lesson.

*   **Supporting Characters:**
    *   Friends, family members, or mentors who help the protagonist.
    *   Provide support, guidance, and encouragement.
    *   May have their own subplots or challenges.

*   **Antagonist:**
    *   A character or force that opposes the protagonist.
    *   Creates conflict and obstacles for the protagonist to overcome.
    *   May be a person, an animal, or a natural force.
'''
        return base_prompt + children_s_chapter_books_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        children_s_chapter_books_additions = '''
## Children's Chapter Books-Specific Chapter Writing
- **Writing Technique 1: Focus on Action**: Keep the plot moving forward with plenty of action and dialogue. Avoid lengthy descriptions or exposition.
- **Writing Technique 2: Use Vivid Language**: Use vivid and descriptive language to paint a picture in the reader's mind.
- **Writing Technique 3: Create Suspense**: Build suspense by hinting at future events or creating cliffhangers at the end of chapters.
- **Writing Technique 4: Show, Don't Tell**: Show the reader what is happening through the characters' actions and dialogue, rather than simply telling them.
- **Writing Technique 5: Maintain a Consistent Tone**: Maintain a consistent tone throughout the chapter that is appropriate for the target age range.
- **Writing Technique 6: Vary Sentence Structure**: Vary your sentence structure to keep the writing engaging and avoid monotony.
- **Writing Technique 7: Use Dialogue Effectively**: Use dialogue to reveal character, advance the plot, and create conflict.
- **Writing Technique 8: End with a Hook**: End each chapter with a hook that will make the reader want to keep reading.

**Detailed Chapter Writing Guidance:**

*   **Beginning:**
    *   Start with an engaging hook that grabs the reader's attention.
    *   Briefly recap previous events if necessary.
    *   Introduce the main action or conflict of the chapter.

*   **Middle:**
    *   Develop the plot and characters through action and dialogue.
    *   Build suspense and tension.
    *   Introduce new challenges or obstacles.

*   **End:**
    *   Resolve the main conflict of the chapter.
    *   Leave the reader with a sense of closure or anticipation.
    *   End with a cliffhanger or a question that will make them want to read the next chapter.
'''
        return base_prompt + children_s_chapter_books_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a childrenschapterbooks-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        childrenschapterbooks_series_additions = """

## ChildrenSChapterBooks Series-Specific Planning Elements

### Genre-Specific Series Development
- **ChildrenSChapterBooks Conventions**: Ensure each book fulfills childrenschapterbooks reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to childrenschapterbooks
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to childrenschapterbooks
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore childrenschapterbooks themes with increasing depth and complexity

### ChildrenSChapterBooks Series Continuity
- **Genre Elements**: Maintain consistent childrenschapterbooks elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy childrenschapterbooks readers
- **Series Identity**: Establish a strong series identity that feels authentically childrenschapterbooks
- **World Building**: Develop the story world in ways that enhance the childrenschapterbooks experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the childrenschapterbooks genre

Create a childrenschapterbooks series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + childrenschapterbooks_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a childrenschapterbooks-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        childrenschapterbooks_book_additions = """

## ChildrenSChapterBooks Series Book Integration

### ChildrenSChapterBooks Continuity for This Book
- **Genre Consistency**: Maintain established childrenschapterbooks elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to childrenschapterbooks
- **Plot Advancement**: Continue series plot threads while telling a complete childrenschapterbooks story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill childrenschapterbooks reader expectations while advancing the series narrative

### Book-Specific ChildrenSChapterBooks Focus
- **Central Conflict**: What childrenschapterbooks-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new childrenschapterbooks elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent childrenschapterbooks while serving the series?

Ensure this book feels like an authentic continuation of the childrenschapterbooks series while telling a complete, satisfying story.
"""

        return base_prompt + childrenschapterbooks_book_additions

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover copy for a Children's Chapter Book.

        Args:
        **kwargs: Keyword arguments that can be passed to customize the prompt (e.g., title, author, target_age).

        Returns:
        A string containing the prompt for back cover copy generation.
        """

        title = kwargs.get("title", "[Book Title]")
        author = kwargs.get("author", "[Author Name]")
        target_age = kwargs.get("target_age", "6-9")
        main_character = kwargs.get("main_character", "[Main Character Name]")
        genre_themes = kwargs.get("genre_themes", "Friendship, Adventure, Problem-Solving")

        prompt = f"""
        Craft a captivating back cover description for the Children's Chapter Book, '{title}' by {author}. Target audience: ages {target_age}.

        The description should be approximately 100-150 words and follow these guidelines:

        *   **Hook:** Start with an engaging question or statement that immediately grabs the reader's attention.  Think about what makes this story irresistible to a child.  For example: "What happens when a talking squirrel moves into your treehouse?" or "Lily thought summer vacation would be boring... until she discovered a secret map!"

        *   **Introduce the Main Character:** Briefly introduce {main_character} and their personality. Highlight their most relatable qualities (e.g., curious, brave, kind, a little bit clumsy). Focus on a challenge or a desire they have.

        *   **Describe the Central Conflict/Adventure:** What problem does {main_character} face? What exciting adventure do they embark on? Hint at the stakes involved. Make sure the conflict is age-appropriate and engaging for the target audience.  Use vivid language that sparks imagination.

        *   **Emphasize Key Themes:** Highlight the core themes of the story, such as {genre_themes}. Show, don't tell, how these themes are woven into the narrative.

        *   **Leave the Reader Wanting More:** End with a cliffhanger or a question that compels the reader to open the book and find out what happens next. Avoid spoilers!

        *   **Tone:** Maintain a playful, optimistic, and age-appropriate tone. Use simple language and avoid complex sentence structures.

        *   **Example Sentence Starters:**
        *   "Join {main_character} as they..."
        *   "When {main_character} discovers..."
        *   "But things take a turn when..."
        *   "{main_character} must find a way to..."
        *   "Can {main_character} and their friends..."

        *   **Avoid:** Overly complex plot summaries, mature themes, or language that is too sophisticated for the target age group.

        Remember, the goal is to make kids *want* to read this book!
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short, punchy book recommendation (2-3 lines) for a Children's Chapter Book.

        Args:
        **kwargs: Keyword arguments that can be passed to customize the prompt (e.g., title, author, main_character).

        Returns:
        A string containing the prompt for a short book recommendation.
        """

        title = kwargs.get("title", "[Book Title]")
        author = kwargs.get("author", "[Author Name]")
        main_character = kwargs.get("main_character", "[Main Character Name]")

        prompt = f"""
        Craft a short, attention-grabbing book recommendation (2-3 lines) for the Children's Chapter Book, '{title}' by {author}.

        Focus on these elements:

        *   **Intrigue:** Immediately pique the reader's interest with a hint of adventure or mystery.
        *   **Main Character Highlight:** Briefly mention the main character, {main_character}, and their most appealing trait.
        *   **Promise of Fun:** Convey the excitement and entertainment the book offers.

        Examples:

        *   "Get ready for a wild ride! {main_character} is about to discover that their backyard is full of secrets."
        *   "{title}: A heartwarming story about friendship and bravery that will leave you smiling!"
        *   "If you love adventure, you'll love {title}! Join {main_character} on a quest to save the day."

        Keep it concise, engaging, and kid-friendly!  Think of what would make a child immediately grab the book off the shelf.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a Children's Chapter Book.

        Args:
        **kwargs: Keyword arguments that can be passed to customize the prompt (e.g., title, main_theme).

        Returns:
        A string containing the prompt for a marketing tagline.
        """

        title = kwargs.get("title", "[Book Title]")
        main_theme = kwargs.get("main_theme", "[Main Theme]")

        prompt = f"""
        Create a catchy and memorable marketing tagline for the Children's Chapter Book, '{title}'.

        The tagline should be:

        *   **Short and Sweet:** Ideally, no more than 5-7 words.
        *   **Intriguing:** Spark curiosity and make kids want to know more.
        *   **Relevant:** Reflect the core theme or adventure of the book.  Focus on the fun and exciting aspects.
        *   **Memorable:** Easy to remember and repeat.

        Consider these approaches:

        *   **Highlight the adventure:** "Adventure awaits!" or "Get ready to explore!"
        *   **Focus on the main character:** "[Main Character Name]: The adventure begins!"
        *   **Emphasize the theme:** "Friendship is the greatest adventure!" or "[Main Theme]: It's an adventure!"
        *   **Ask a question:** "Ready for a magical journey?"

        Examples:

        *   "Friendship. Adventure. Magic."
        *   "Where imagination takes flight!"
        *   "The adventure starts here!"

        Think like a kid! What would make *you* want to read this book?
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for describing the desired visual style for the back cover of a Children's Chapter Book.

        Args:
        **kwargs: Keyword arguments that can be passed to customize the prompt (e.g., main_character, setting).

        Returns:
        A string containing the prompt for visual style preferences.
        """

        main_character = kwargs.get("main_character", "[Main Character Name]")
        setting = kwargs.get("setting", "[Setting Description]")
        genre = kwargs.get("genre", "[Genre Type]")

        prompt = f"""
        Describe the desired visual style for the back cover of a Children's Chapter Book featuring {main_character} and set in {setting}. This is a {genre} story.

        Consider these elements:

        *   **Overall Tone:** Should the visual style be playful, whimsical, adventurous, mysterious, or heartwarming?  Think about the overall feeling the book evokes.

        *   **Color Palette:** What colors would best represent the story's mood and themes? (e.g., bright and cheerful, warm and inviting, cool and mysterious)

        *   **Illustration Style:** Should the illustrations be cartoonish, realistic, whimsical, or stylized?  Consider artists like Quentin Blake, Chris Van Allsburg, or Beatrix Potter for inspiration.

        *   **Font:** What font style would be appropriate for the title and author name? Should it be bold and playful, elegant and classic, or something else?

        *   **Imagery:** What specific elements from the story should be featured on the back cover? (e.g., the main character, a key object, a glimpse of the setting)

        *   **Composition:** How should the elements be arranged on the back cover to create a visually appealing and engaging design?

        *   **Target Audience:** Keep the visual style appropriate for the target age group.

        Examples:

        *   "Cartoonish illustrations with bright, vibrant colors, featuring {main_character} in a playful pose."
        *   "Whimsical watercolor illustrations with a soft, muted color palette, showing the magical forest setting."
        *   "Bold, hand-lettered font for the title, with an image of a key object from the story in the background."

        The goal is to create a back cover that is visually appealing to children and accurately reflects the tone and content of the book.
        """
        return prompt


# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return ChildrenSChapterBooksPrompts.get_series_book_prompt(**kwargs)
