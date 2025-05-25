"""
Thriller genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ThrillerPrompts(FictionBasePrompts):
    GENRE_NAME = "Thriller"
    GENRE_DESCRIPTION = "The Thriller genre is characterized by its focus on suspense, tension, and excitement. It often involves high stakes, dangerous situations, and a race against time. The protagonist typically faces a formidable antagonist or a complex web of conspiracies, forcing them to use their wits and courage to survive and uncover the truth. Psychological elements, moral ambiguity, and unexpected twists are common features, creating a gripping and immersive reading experience."
    
    GENRE_CHARACTERISTICS = [
        "Pace and Suspense: A relentless pace that builds suspense through carefully crafted plot twists and cliffhangers, keeping the reader constantly on edge.",
        "High Stakes: The protagonist faces significant personal risk, often involving life-or-death situations or the potential for catastrophic consequences.",
        "Formidable Antagonist: A cunning and resourceful antagonist who poses a credible threat to the protagonist, driving the conflict and raising the stakes.",
        "Moral Ambiguity: Characters often operate in shades of gray, blurring the lines between good and evil and forcing the reader to question their allegiances.",
        "Psychological Depth: Explores the psychological impact of fear, trauma, and paranoia on the characters, adding layers of complexity to their motivations and actions.",
        "Twists and Turns: Unexpected plot twists and revelations that challenge the reader's assumptions and keep them guessing until the very end.",
        "Red Herrings: Deliberate misdirection and false leads that create confusion and uncertainty, adding to the suspense and intrigue.",
        "Atmospheric Setting: A vivid and immersive setting that enhances the sense of danger and isolation, often featuring dark, claustrophobic, or unfamiliar environments.",
        "Race Against Time: The protagonist is often under pressure to solve a mystery or prevent a disaster before it's too late, adding urgency to the narrative.",
        "Unreliable Narrator: A narrator whose perspective is biased, deceptive, or incomplete, forcing the reader to question the truth and piece together the real story."
    ]
    
    TYPICAL_ELEMENTS = [
        "A protagonist with a hidden past or a secret vulnerability.",
        "A conspiracy that reaches the highest levels of power.",
        "A ticking clock scenario that adds urgency to the plot.",
        "A series of escalating threats and challenges.",
        "A cat-and-mouse game between the protagonist and the antagonist.",
        "A double-crossing character who betrays the protagonist's trust.",
        "A shocking revelation that changes everything.",
        "A chase scene that puts the protagonist in mortal danger.",
        "A suspenseful interrogation scene.",
        "A climactic confrontation that tests the protagonist's limits.",
        "A lingering sense of unease or paranoia.",
        "A resolution that leaves some questions unanswered or open to interpretation."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Writing Considerations
- **Pacing and Tension**: Master the art of building suspense through carefully controlled pacing. Use short, impactful sentences and paragraphs to create a sense of urgency, and strategically deploy cliffhangers to keep the reader hooked.
- **Creating Believable Threats**: Develop antagonists who are not only formidable but also believable. Give them clear motivations and a plausible plan, making their actions feel grounded in reality.
- **Red Herrings and Misdirection**: Skillfully weave in red herrings and misdirection to keep the reader guessing. Plant false clues and create misleading scenarios that lead them down the wrong path.
- **Psychological Realism**: Explore the psychological impact of fear, trauma, and paranoia on your characters. Show how these emotions affect their decision-making and behavior, adding depth and complexity to their portrayal.
- **Atmospheric Detail**: Pay close attention to the setting and atmosphere. Use vivid descriptions to create a sense of unease and foreboding, immersing the reader in the world of the story.
- **Twist Endings and Resolutions**: Craft a satisfying twist ending that subverts expectations but remains logically consistent with the established plot. Ensure that the resolution provides closure while leaving a lasting impact on the reader.
- **Moral Ambiguity**: Embrace moral ambiguity in your characters and plot. Explore the gray areas of right and wrong, forcing the reader to question their own values and beliefs.
- **Research and Authenticity**: Conduct thorough research to ensure the authenticity of your story. Pay attention to details about law enforcement, technology, and other relevant fields to create a believable and immersive experience.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Outline Requirements
- **Inciting Incident**: The inciting incident should immediately thrust the protagonist into a dangerous or unsettling situation, setting the stage for the escalating conflict.
- **Rising Action and Suspense**: The rising action should be structured to gradually increase the tension and suspense, with each scene presenting new challenges and obstacles for the protagonist.
- **Midpoint Twist**: Introduce a significant twist or revelation at the midpoint of the story that changes the protagonist's understanding of the situation and raises the stakes even higher.
- **False Climax**: Include a false climax that appears to resolve the conflict but ultimately leads to an even greater threat or challenge.
- **Climax and Confrontation**: The climax should be a high-stakes confrontation between the protagonist and the antagonist, where the protagonist must use all their skills and resources to survive.
- **Resolution and Aftermath**: The resolution should provide closure to the main plot threads while leaving a lasting impact on the protagonist and the reader. Consider including a final twist or revelation that adds a layer of complexity to the ending.
- **Subplot Integration**: Subplots should be carefully integrated into the main plot, adding depth and complexity to the story while also contributing to the overall suspense and tension.
- **Pacing and Momentum**: Maintain a relentless pace throughout the story, with short, impactful scenes and frequent cliffhangers to keep the reader engaged.
- **Red Herring Placement**: Strategically place red herrings throughout the outline to mislead the reader and create a sense of uncertainty.
- **Character Arc Integration**: Ensure that the protagonist's character arc is closely tied to the plot, with their growth and development influencing their ability to overcome the challenges they face.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Character Development
- **Protagonist Vulnerability**: Give the protagonist a vulnerability or a hidden flaw that makes them relatable and sympathetic, but also creates opportunities for the antagonist to exploit them.
- **Antagonist Motivation**: Develop a clear and compelling motivation for the antagonist's actions, making them more than just a one-dimensional villain. Explore their backstory and psychological makeup to create a complex and believable character.
- **Moral Ambiguity**: Explore the moral ambiguity of your characters, blurring the lines between good and evil and forcing the reader to question their allegiances.
- **Psychological Depth**: Delve into the psychological impact of fear, trauma, and paranoia on your characters, showing how these emotions affect their decision-making and behavior.
- **Hidden Agendas**: Give your characters hidden agendas and secret motivations that add layers of complexity to their interactions and relationships.
- **Character Arcs**: Develop clear character arcs for your protagonist and antagonist, showing how they change and evolve throughout the story in response to the challenges they face.
- **Supporting Characters**: Use supporting characters to provide contrast and support for the protagonist, while also adding depth and complexity to the world of the story.
- **Unreliable Narrators**: Consider using an unreliable narrator to create a sense of uncertainty and suspense, forcing the reader to question the truth and piece together the real story.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Chapter Writing
- **Opening Hook**: Start each chapter with a compelling hook that grabs the reader's attention and immediately draws them into the scene.
- **Pacing and Tension**: Maintain a relentless pace throughout the chapter, using short, impactful sentences and paragraphs to create a sense of urgency.
- **Cliffhangers**: End each chapter with a cliffhanger that leaves the reader wanting more and eager to turn the page.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show the reader what is happening, rather than simply telling them.
- **Dialogue**: Write realistic and engaging dialogue that reveals character, advances the plot, and builds tension.
- **Suspenseful Atmosphere**: Create a suspenseful atmosphere through the use of setting, imagery, and sound.
- **Red Herrings**: Weave in red herrings and misdirection to keep the reader guessing and create a sense of uncertainty.
- **Character Development**: Use each chapter to further develop your characters, revealing their motivations, flaws, and strengths.
- **Plot Advancement**: Ensure that each chapter advances the plot in a meaningful way, either by introducing new information, raising the stakes, or creating new challenges for the protagonist.
- **Point of View**: Maintain a consistent point of view throughout the chapter, using it to create suspense and build empathy for the protagonist.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a thriller-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        thriller_series_additions = """

## Thriller Series-Specific Planning Elements

### Genre-Specific Series Development
- **Thriller Conventions**: Ensure each book fulfills thriller reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to thriller
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to thriller
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore thriller themes with increasing depth and complexity

### Thriller Series Continuity
- **Genre Elements**: Maintain consistent thriller elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy thriller readers
- **Series Identity**: Establish a strong series identity that feels authentically thriller
- **World Building**: Develop the story world in ways that enhance the thriller experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the thriller genre

Create a thriller series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + thriller_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a thriller-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class ThrillerMarketing:
        """
        A class containing methods for generating marketing materials for Thriller books,
        specifically focused on creating compelling back cover copy,
        short descriptions, marketing taglines, and visual style preferences.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions for Thriller books.

        Args:
        **kwargs:  Arbitrary keyword arguments. These can include specific plot details,
        character names, settings, and desired tone.  Use these to tailor the prompt.

        Returns:
        str: A prompt string designed to guide AI in generating effective back cover copy.
        """
        prompt = f"""
        Write a gripping back cover description for a Thriller novel.

        **Genre:** Thriller

        **Core Elements to Emphasize:**

        *   **High Stakes:** Clearly establish the life-or-death consequences facing the protagonist.  What will they lose if they fail?
        *   **Suspense and Tension:** Use language that creates a sense of unease, anticipation, and impending danger.  Hint at twists and turns, but avoid spoilers.
        *   **Mystery and Intrigue:**  Introduce a central mystery that the reader will be compelled to solve.  Plant seeds of doubt and suspicion. Who can the protagonist trust?
        *   **Fast-Paced Action:** Convey a sense of urgency and relentless pursuit.  Use active verbs and short, punchy sentences.
        *   **Moral Ambiguity:**  Explore the gray areas of morality.  Are the characters truly good or evil?  Are their actions justified?
        *   **Psychological Depth:** Delve into the protagonist's inner turmoil, fears, and motivations.  What drives them to take such risks?  What are their deepest secrets?

        **Specific Guidelines for Thrillers:**

        *   **Hook the Reader Immediately:** Start with a captivating opening line or question that grabs the reader's attention.
        *   **Introduce the Protagonist:** Briefly introduce the main character and their current situation.  Make them relatable, even if flawed.
        *   **Hint at the Antagonist:** Subtly introduce the antagonist or the force opposing the protagonist.  Create a sense of menace and danger.
        *   **Tease the Plot:** Provide just enough information to pique the reader's interest without revealing key plot points or the ending.
        *   **Use Strong Verbs and Imagery:** Employ vivid language to create a visceral reading experience.
        *   **End with a Cliffhanger:** Leave the reader with a burning question or a sense of unresolved tension that compels them to read the book.
        *   **Focus on the 'What If' Scenario:**  Present a compelling 'what if' scenario that explores the darkest possibilities.
        *   **Incorporate Genre Tropes:** Subtly use established thriller tropes (e.g., ticking clock, unreliable narrator, conspiracy, cat-and-mouse game) to appeal to genre fans.

        **Optional Elements (Use if applicable to the specific book):**

        *   **Specific Setting:** If the setting is crucial to the plot, highlight its unique atmosphere and how it contributes to the suspense.
        *   **Twist Ending:** If the book has a major twist, subtly hint at its existence without giving it away.
        *   **Themes:**  If the book explores deeper themes (e.g., betrayal, revenge, redemption), briefly allude to them.

        **Tone:**  Suspenseful, intense, mysterious, gripping, unsettling, morally ambiguous.

        **Consider these questions when crafting the description:**

        *   What is the central conflict of the story?
        *   What are the stakes for the protagonist?
        *   What secrets are being kept?
        *   What are the consequences of failure?
        *   What makes this thriller unique and unforgettable?

        **Specific details about the book (use these to personalize the description):**
        {kwargs}

        **Example Start:**
        "One wrong move could cost her everything..."
        "He thought he knew the truth. He was dead wrong."
        "In a city of secrets, some are best left buried."

        **Example End:**
        "But the clock is ticking. And time is running out."
        "The truth is closer than she thinks. And far more dangerous."
        "Will he survive the night? Or will he become the next victim?"

        Write a back cover description of approximately 150-200 words.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short (2-3 line) book recommendation for a Thriller novel.

        Args:
        **kwargs: Arbitrary keyword arguments.  Use these to provide specific details about the book.

        Returns:
        str: A prompt string designed to guide AI in generating a concise and compelling recommendation.
        """
        prompt = f"""
        Write a short, punchy book recommendation (2-3 lines) for a Thriller novel.  This should be suitable for use on a website, social media, or in an email newsletter.

        **Genre:** Thriller

        **Key Considerations:**

        *   **Intrigue:** Immediately grab the reader's attention with a hint of mystery or danger.
        *   **Conciseness:** Get straight to the point and use impactful language.
        *   **Emotional Hook:** Evoke a sense of suspense, fear, or excitement.
        *   **Target Audience:** Appeal to fans of fast-paced thrillers with high stakes.

        **Specific Guidelines for Thrillers:**

        *   **Highlight the Central Conflict:** Briefly mention the main problem or challenge the protagonist faces.
        *   **Emphasize the Stakes:**  Convey the potential consequences of failure.
        *   **Use Strong Action Verbs:**  Create a sense of urgency and excitement.
        *   **Focus on the Unique Selling Point:**  What makes this thriller stand out from the crowd?

        **Example Recommendations:**

        *   "A twisty, suspenseful thriller that will keep you guessing until the very end. Perfect for fans of [Author] and [Author]."
        *   "Secrets, lies, and betrayal collide in this pulse-pounding thriller.  Prepare to be on the edge of your seat!"
        *   "When a seemingly perfect life unravels, one woman must fight to uncover the truth before it's too late.  A must-read for thriller addicts."

        **Specific details about the book (use these to personalize the recommendation):**
        {kwargs}

        Write a recommendation that is approximately 2-3 lines long.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a Thriller novel.

        Args:
        **kwargs: Arbitrary keyword arguments. Use these to provide specific details about the book.

        Returns:
        str: A prompt string designed to guide AI in generating a memorable and effective tagline.
        """
        prompt = f"""
        Write a punchy marketing tagline for a Thriller novel.  The tagline should be short, memorable, and attention-grabbing.

        **Genre:** Thriller

        **Key Considerations:**

        *   **Intrigue:**  Create a sense of mystery and suspense.
        *   **Conciseness:**  Use as few words as possible.
        *   **Impact:**  Leave a lasting impression on the reader.
        *   **Target Audience:**  Appeal to fans of thrilling and suspenseful stories.

        **Specific Guidelines for Thrillers:**

        *   **Focus on the Core Conflict:**  Hint at the central problem or challenge.
        *   **Emphasize the Stakes:**  Convey the potential consequences of failure.
        *   **Use Strong Verbs and Imagery:**  Create a sense of urgency and excitement.
        *   **Highlight the Unique Selling Point:** What makes this thriller stand out?
        *   **Consider using questions:** Taglines framed as questions can pique curiosity.

        **Example Taglines:**

        *   "The truth will cost her everything."
        *   "Trust no one."
        *   "Every secret has a price."
        *   "What if everything you knew was a lie?"
        *   "Some secrets are better left buried."
        *   "The clock is ticking."
        *   "Survival is the only option."

        **Specific details about the book (use these to personalize the tagline):**
        {kwargs}

        Write a tagline that is approximately 5-10 words long.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt describing visual style preferences for the back cover of a Thriller novel.

        Args:
        **kwargs: Arbitrary keyword arguments. Use these to provide specific details about the book.

        Returns:
        str: A prompt string designed to guide a graphic designer in creating a visually appealing and genre-appropriate back cover.
        """
        prompt = f"""
        Describe the desired visual style for the back cover of a Thriller novel.

        **Genre:** Thriller

        **Key Considerations:**

        *   **Atmosphere:**  Create a sense of unease, suspense, and mystery.
        *   **Color Palette:**  Use colors that evoke a sense of danger, darkness, or urgency.  Common choices include:
        *   Dark blues and blacks
        *   Reds (to suggest blood or danger)
        *   Grays and silvers
        *   Monochromatic schemes
        *   **Imagery:**  Use images that are suggestive and symbolic rather than literal.  Consider:
        *   Shadows and silhouettes
        *   Blurred or distorted images
        *   Abstract patterns
        *   Objects associated with danger (e.g., weapons, keys, clocks)
        *   Close-ups of faces or eyes (to convey emotion)
        *   **Typography:**  Use fonts that are clean, modern, and easy to read.  Consider using different font weights and styles to create visual interest.  Avoid overly decorative or playful fonts.
        *   **Layout:**  Keep the layout clean and uncluttered.  Use negative space to create a sense of tension and isolation.

        **Specific Guidelines for Thrillers:**

        *   **Convey a Sense of Danger:** The visual elements should immediately communicate that the book is a thriller and that the reader is in for a suspenseful ride.
        *   **Create a Visual Hook:**  Use an image or design element that will grab the reader's attention and make them want to learn more about the book.
        *   **Avoid Clichés:**  While it's important to adhere to genre conventions, avoid using overly generic or predictable imagery.
        *   **Consider the Target Audience:**  Think about what visual styles will appeal to fans of thrillers.

        **Specific details about the book (use these to personalize the visual style):**
        {kwargs}

        **Examples:**

        *   "A stark, minimalist design with a single, blood-red object on a black background."
        *   "A blurred image of a woman running through a dark forest, with a sense of impending danger."
        *   "A close-up of a pair of eyes, filled with fear and desperation."
        *   "Use a glitch effect on the text to create a sense of unease."
        """
        return prompt
        ```
        thriller_book_additions = """

## Thriller Series Book Integration

### Thriller Continuity for This Book
- **Genre Consistency**: Maintain established thriller elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to thriller
- **Plot Advancement**: Continue series plot threads while telling a complete thriller story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill thriller reader expectations while advancing the series narrative

### Book-Specific Thriller Focus
- **Central Conflict**: What thriller-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new thriller elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent thriller while serving the series?

Ensure this book feels like an authentic continuation of the thriller series while telling a complete, satisfying story.
"""

        return base_prompt + thriller_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_series_book_prompt(**kwargs)
