"""
Horror genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class HorrorPrompts(FictionBasePrompts):
    GENRE_NAME = "Horror"
    GENRE_DESCRIPTION = "Horror fiction aims to elicit feelings of dread, terror, and suspense in the reader. It often explores the darker aspects of human nature and the unknown, confronting readers with disturbing or frightening scenarios. Central to the genre is the disruption of normalcy, often through supernatural elements, psychological disturbances, or threats to physical safety. The goal is to provoke a visceral emotional response, leaving a lasting impression of unease and fear."

    GENRE_CHARACTERISTICS = [
        "Atmospheric Tension: Creates a palpable sense of dread and anticipation through vivid descriptions of setting, sound, and subtle cues.",
        "Psychological Exploration: Delves into the minds of characters, exploring their fears, anxieties, and descent into madness.",
        "Supernatural Elements: Incorporates ghosts, demons, monsters, and other entities that defy natural laws.",
        "Body Horror: Focuses on the grotesque and disturbing transformation or mutilation of the human body.",
        "Existential Dread: Explores themes of mortality, insignificance, and the inherent meaninglessness of existence.",
        "Gothic Elements: Utilizes decaying settings, family curses, and a sense of oppressive history.",
        "Jump Scares and Suspense: Employs sudden shocks and prolonged periods of anticipation to heighten fear.",
        "Moral Ambiguity: Blurs the lines between good and evil, forcing characters and readers to confront difficult choices.",
        "Isolation and Confinement: Places characters in situations where they are cut off from help and forced to confront their fears alone.",
        "Foreshadowing and Symbolism: Uses subtle hints and recurring motifs to build suspense and create a sense of impending doom."
    ]

    TYPICAL_ELEMENTS = [
        "Haunted Houses: Dwellings imbued with malevolent spirits or traumatic histories.",
        "Monsters and Creatures: Antagonistic entities that embody primal fears and anxieties.",
        "Demonic Possession: The takeover of a human body by a supernatural force.",
        "Curses and Hexes: Supernatural afflictions that bring misfortune and suffering.",
        "Psychological Torment: The manipulation and breakdown of a character's mental state.",
        "Nightmares and Visions: Disturbing and surreal experiences that blur the line between reality and illusion.",
        "Ancient Evils: Long-dormant forces that are awakened to wreak havoc.",
        "Sacrifice and Rituals: Dark practices performed to appease supernatural entities or achieve forbidden knowledge.",
        "Doppelgangers and Imposters: Characters who mimic or replace others, creating confusion and paranoia.",
        "Unexplained Phenomena: Events that defy logical explanation and challenge the characters' understanding of the world.",
        "Ominous Omens: Signs and portents that foreshadow impending doom.",
        "Final Girl Trope: The lone female survivor who confronts and defeats the antagonist."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        horror_additions = '''
## Horror-Specific Writing Considerations
- **Mastering Atmosphere**: Focus on creating a palpable sense of dread and suspense through vivid sensory details (sight, sound, smell, touch) and evocative language. Consider the pacing of your descriptions to build tension gradually.
- **Understanding Psychological Horror**: Delve into the characters' minds, exploring their deepest fears, anxieties, and traumas. Use internal monologue and dream sequences to reveal their inner turmoil and descent into madness.
- **Effective Use of Gore and Violence**: Employ gore and violence sparingly and strategically to maximize their impact. Focus on the psychological and emotional consequences of violence rather than gratuitous depictions.
- **Building Suspense and Tension**: Utilize techniques such as foreshadowing, red herrings, and cliffhangers to keep readers on the edge of their seats. Control the flow of information to create a sense of mystery and uncertainty.
- **Exploring Moral Ambiguity**: Challenge readers to confront difficult moral choices and question the nature of good and evil. Create characters who are flawed and complex, with motivations that are not always clear.
- **Subverting Expectations**: Avoid clichés and predictable tropes. Find fresh and innovative ways to scare readers and surprise them with unexpected twists and turns.
- **Researching Horror Subgenres**: Familiarize yourself with different subgenres of horror (e.g., gothic horror, cosmic horror, slasher horror) to find your niche and develop a unique voice.
- **Understanding the Power of the Unseen**: Often, what is implied or suggested is more terrifying than what is explicitly shown. Use ambiguity and suggestion to create a sense of unease and dread.
'''
        return base_prompt + horror_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        horror_additions = '''
## Horror-Specific Outline Requirements
- **Inciting Incident (The Unsettling)**: The event that disrupts the characters' normal lives and introduces the element of horror. This should be a clear and compelling hook that grabs the reader's attention.
- **Rising Action (The Descent)**: A series of escalating events that build suspense and tension. Introduce obstacles, challenges, and increasingly terrifying encounters that push the characters to their limits.
- **Midpoint (The Revelation)**: A turning point in the story where the characters uncover a crucial piece of information or face a major setback. This should raise the stakes and intensify the sense of dread.
- **Climax (The Confrontation)**: The ultimate showdown between the characters and the source of the horror. This should be a high-stakes, emotionally charged sequence that tests the characters' courage and resilience.
- **Falling Action (The Aftermath)**: The immediate consequences of the climax, as the characters grapple with the trauma and loss they have experienced. This should provide a sense of closure while leaving a lingering sense of unease.
- **Resolution (The Lingering Fear)**: The final outcome of the story, where the characters attempt to rebuild their lives and come to terms with the events that have transpired. Consider leaving a hint of ambiguity or uncertainty to suggest that the horror may not be truly over.
- **Atmospheric Setup**: Plan specific scenes dedicated to building atmosphere and dread. These scenes might not directly advance the plot but are crucial for establishing the tone and mood of the story.
- **Character Arcs of Despair**: Outline how each character's mental and emotional state deteriorates throughout the story, leading to potential breakdowns or sacrifices.
'''
        return base_prompt + horror_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)

        horror_additions = '''
## Horror-Specific Character Development
- **Vulnerability and Flaws**: Create characters who are relatable and vulnerable, with flaws and weaknesses that make them susceptible to fear and manipulation. Avoid creating characters who are too perfect or invincible.
- **Psychological Depth**: Explore the characters' inner lives, revealing their fears, anxieties, and traumas. Use their backstories to explain their motivations and reactions to the horror they encounter.
- **Emotional Range**: Allow characters to experience a wide range of emotions, from fear and grief to anger and despair. Show how the horror affects their relationships and their sense of self.
- **Moral Compass**: Give characters a strong moral compass, but challenge them to make difficult choices in the face of overwhelming fear. Explore the ethical dilemmas they face and the consequences of their actions.
- **Character Arcs of Despair**: Chart the characters' descent into darkness as they are confronted with the horror. Show how they change and evolve as they struggle to survive.
- **The "Final Girl" (If Applicable)**: If your story features a "final girl" archetype, give her unique strengths and vulnerabilities. Avoid making her a passive victim; instead, empower her to fight back and overcome the horror.
- **Antagonists as Embodiments of Fear**: Develop antagonists who represent primal fears and anxieties. Give them compelling motivations and backstories that make them more than just mindless monsters.
- **Sacrificial Lambs**: Consider which characters are most likely to be killed off early to raise the stakes and create a sense of danger.
'''
        return base_prompt + horror_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        horror_additions = '''
## Horror-Specific Chapter Writing
- **Building Suspense Gradually**: Start each chapter with a sense of unease or foreboding, gradually increasing the tension as the chapter progresses. Use foreshadowing and red herrings to keep readers guessing.
- **Sensory Details and Atmosphere**: Focus on creating a vivid and immersive atmosphere through detailed descriptions of sight, sound, smell, and touch. Use sensory details to evoke feelings of dread and discomfort.
- **Pacing and Rhythm**: Vary the pacing of your chapters to create a sense of urgency and suspense. Use short, choppy sentences to heighten tension during action sequences, and longer, more descriptive sentences to build atmosphere.
- **Character Reactions and Internal Monologue**: Show how the characters are reacting to the horror they are experiencing. Use internal monologue to reveal their thoughts, fears, and anxieties.
- **Cliffhangers and Twists**: End each chapter with a cliffhanger or a shocking twist to keep readers engaged and eager to turn the page.
- **Strategic Use of Violence and Gore**: Use violence and gore sparingly and strategically to maximize their impact. Focus on the psychological and emotional consequences of violence rather than gratuitous depictions.
- **Maintaining a Sense of Mystery**: Avoid revealing too much information too soon. Keep readers guessing about the nature of the horror and the characters' fates.
- **Thematic Resonance**: Ensure that each chapter contributes to the overall themes and message of the story. Explore the deeper meanings and implications of the horror.
'''
        return base_prompt + horror_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a horror-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        horror_series_additions = """

## Horror Series-Specific Planning Elements

### Genre-Specific Series Development
- **Horror Conventions**: Ensure each book fulfills horror reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to horror
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to horror
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore horror themes with increasing depth and complexity

### Horror Series Continuity
- **Genre Elements**: Maintain consistent horror elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy horror readers
- **Series Identity**: Establish a strong series identity that feels authentically horror
- **World Building**: Develop the story world in ways that enhance the horror experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the horror genre

Create a horror series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + horror_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a horror-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        horror_book_additions = """

## Horror Series Book Integration

### Horror Continuity for This Book
- **Genre Consistency**: Maintain established horror elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to horror
- **Plot Advancement**: Continue series plot threads while telling a complete horror story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill horror reader expectations while advancing the series narrative

### Book-Specific Horror Focus
- **Central Conflict**: What horror-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new horror elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent horror while serving the series?

Ensure this book feels like an authentic continuation of the horror series while telling a complete, satisfying story.
"""
        
        return base_prompt + horror_book_additions

        ```python
        class HorrorBackCover:
        """
        A class containing methods for generating back cover copy and visual style preferences
        specifically tailored for the Horror genre.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions for Horror novels.

        Args:
        **kwargs: Optional keyword arguments to customize the prompt (e.g., target_audience, specific_themes).

        Returns:
        str: A prompt string designed to guide AI in generating effective Horror back cover copy.
        """
        prompt = f"""
        You are an expert copywriter specializing in Horror novels. Your goal is to craft a back cover description that will terrify and entice potential readers.

        **Genre:** Horror

        **Key Elements to Emphasize:**

        *   **Fear and Dread:**  Focus on creating a sense of mounting dread, unease, and impending doom.  Use evocative language to paint vivid and unsettling images.
        *   **Psychological Horror:** Explore the characters' inner turmoil, paranoia, and descent into madness.  Show, don't tell, their fear.
        *   **Gothic Horror:** If applicable, emphasize settings like decaying mansions, ancient secrets, and a sense of claustrophobia.
        *   **Supernatural Horror:** Highlight the presence of malevolent entities, ghosts, demons, or other unexplainable phenomena. Focus on the violation of natural laws.
        *   **Body Horror:** If present, describe the grotesque and disturbing transformations of the body in a way that elicits revulsion and fear. Be careful not to overdo it - subtlety can be more effective.
        *   **Jump Scares and Suspense:**  Balance moments of intense shock with a sustained atmosphere of suspense.  Hint at dangers lurking just out of sight.
        *   **Moral Ambiguity:**  Explore the blurred lines between good and evil.  Make the reader question the characters' motives and their own morality.
        *   **Isolation and Vulnerability:**  Place characters in situations where they are alone, cut off from help, and vulnerable to the horrors that surround them.
        *   **High Stakes:**  Clearly establish what the characters stand to lose, whether it's their sanity, their lives, or the fate of the world.
        *   **Unanswered Questions:** Leave the reader with lingering questions that will haunt them long after they finish the book.

        **Instructions:**

        1.  **Start with a Hook:**  Open with a sentence or two that immediately grabs the reader's attention and establishes the central conflict or mystery.
        2.  **Introduce the Protagonist(s):**  Briefly describe the main character(s) and their initial situation.  Highlight their flaws and vulnerabilities.
        3.  **Raise the Stakes:**  Clearly explain what the character(s) are fighting against and what they stand to lose.
        4.  **Build Suspense:**  Use vivid language and imagery to create a sense of unease and anticipation.  Hint at the horrors to come without giving away too much.
        5.  **End with a Cliffhanger:**  Leave the reader with a question or a statement that will compel them to pick up the book.

        **Consider the following when writing:**

        *   **Target Audience:** {kwargs.get("target_audience", "General Horror readership")}
        *   **Specific Themes:** {kwargs.get("specific_themes", "The nature of evil, the fragility of sanity, the consequences of unchecked ambition")}
        *   **Tone:**  Dark, unsettling, suspenseful, and terrifying.
        *   **Word Count:**  Approximately 150-200 words.

        **Example Opening Lines:**

        *   "In the decaying halls of Blackwood Manor, something ancient and malevolent stirs..."
        *   "When Sarah uncovered the hidden diary, she unleashed a nightmare beyond comprehension..."
        *   "They thought the abandoned town was deserted. They were wrong..."

        **Now, write a back cover description for a Horror novel based on these guidelines.**
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, impactful 2-3 line book recommendation for a Horror novel.

        Args:
        **kwargs: Optional keyword arguments to customize the prompt (e.g., key_selling_point, target_reader).

        Returns:
        str: A prompt string designed to guide AI in generating concise and enticing Horror book recommendations.
        """
        prompt = f"""
        You are crafting a short, punchy book recommendation for a Horror novel.  Your goal is to capture the essence of the story in just a few lines, making it irresistible to potential readers.

        **Genre:** Horror

        **Key Elements to Emphasize:**

        *   **Intrigue:**  Hint at the central mystery or conflict without giving away spoilers.
        *   **Atmosphere:**  Evoke the feeling of dread and suspense that permeates the book.
        *   **Unique Selling Point:**  Highlight what makes this particular Horror novel stand out from the crowd. (e.g., unique monster, psychological twist, gothic setting)
        *   **Emotional Hook:**  Tap into the reader's deepest fears and anxieties.

        **Instructions:**

        1.  **Focus on the Core:**  Identify the single most terrifying or compelling aspect of the story.
        2.  **Use Strong Verbs:**  Choose action words that convey a sense of urgency and danger. (e.g., stalks, haunts, consumes, devours)
        3.  **Leave them Wanting More:**  End with a question or a statement that piques the reader's curiosity.

        **Consider the following when writing:**

        *   **Key Selling Point:** {kwargs.get("key_selling_point", "Its disturbing exploration of childhood trauma and demonic possession")}
        *   **Target Reader:** {kwargs.get("target_reader", "Fans of psychological horror and supernatural thrillers")}
        *   **Tone:**  Intriguing, suspenseful, and slightly menacing.
        *   **Length:**  2-3 lines.

        **Example Recommendations:**

        *   "A family secret. A haunted house. Some secrets are better left buried."
        *   "It stalks the shadows, feeding on fear. Are you brave enough to face your nightmares?"
        *   "One mistake. One sacrifice. Now, she must pay the ultimate price."

        **Now, write a short book recommendation for a Horror novel based on these guidelines.**
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a Horror novel.

        Args:
        **kwargs: Optional keyword arguments to customize the prompt (e.g., central_theme, target_emotion).

        Returns:
        str: A prompt string designed to guide AI in generating memorable and effective Horror taglines.
        """
        prompt = f"""
        You are crafting a marketing tagline for a Horror novel. Your goal is to create a short, memorable phrase that will instantly capture the reader's attention and convey the essence of the story's terror.

        **Genre:** Horror

        **Key Elements to Emphasize:**

        *   **Brevity:** Taglines should be short and easy to remember.
        *   **Impact:**  The tagline should evoke a strong emotional response (fear, dread, unease).
        *   **Intrigue:**  The tagline should hint at the story's central conflict or mystery without giving away spoilers.
        *   **Originality:**  The tagline should be unique and stand out from the competition.

        **Instructions:**

        1.  **Identify the Core Fear:**  What is the most terrifying aspect of the story? (e.g., isolation, loss of control, the unknown)
        2.  **Use Strong Language:**  Choose words that are evocative and unsettling. (e.g., nightmare, darkness, silence, blood)
        3.  **Create a Sense of Urgency:**  The tagline should imply that something terrible is about to happen.

        **Consider the following when writing:**

        *   **Central Theme:** {kwargs.get("central_theme", "The corruption of innocence")}
        *   **Target Emotion:** {kwargs.get("target_emotion", "Fear and dread")}
        *   **Length:**  5-10 words.

        **Example Taglines:**

        *   "Fear the silence. Fear the dark."
        *   "Some doors are never meant to be opened."
        *   "Your nightmares are just the beginning."
        *   "Evil has found a home. In you."
        *   "Death is only the beginning of the horror."

        **Now, write a marketing tagline for a Horror novel based on these guidelines.**
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining visual style preferences for a Horror novel's back cover design.

        Args:
        **kwargs: Optional keyword arguments to customize the prompt (e.g., specific_imagery, color_palette).

        Returns:
        str: A prompt string designed to guide AI or a designer in creating a visually striking and genre-appropriate back cover.
        """
        prompt = f"""
        You are art directing the visual design for the back cover of a Horror novel. Your goal is to create an image that is both visually striking and thematically appropriate, conveying the book's tone and content at a glance.

        **Genre:** Horror

        **Key Elements to Consider:**

        *   **Color Palette:**  Dark and muted colors are generally effective for Horror, such as blacks, grays, deep reds, and blues. Use color to create a sense of unease and dread. Consider using a single, striking color to draw the eye.
        *   **Imagery:**  Choose imagery that is evocative of the story's themes and setting.  Examples include:
        *   **Gothic Horror:** Decaying mansions, graveyards, twisted trees, shadows.
        *   **Supernatural Horror:** Eerie figures, otherworldly landscapes, symbols of occultism.
        *   **Psychological Horror:** Distorted faces, shattered mirrors, abstract shapes that convey a sense of unease.
        *   **Body Horror:** Grotesque transformations, decaying flesh, unsettling textures. (Use sparingly and tastefully)
        *   **Typography:**  Choose a font that is both legible and visually striking.  Consider using a font that is slightly distressed or uneven to create a sense of unease.
        *   **Composition:**  Use composition to create a sense of tension and suspense.  Consider using asymmetrical layouts or unsettling perspectives.
        *   **Texture:**  Incorporate textures that are rough, grainy, or unsettling to the touch.
        *   **Symbolism:**  Use symbols that are relevant to the story's themes and motifs.

        **Instructions:**

        1.  **Capture the Essence:**  The visual style should immediately convey the genre and tone of the book.
        2.  **Create a Sense of Mystery:**  The image should hint at the story's central conflict or mystery without giving away too much.
        3.  **Be Visually Striking:**  The image should be eye-catching and memorable.

        **Consider the following when writing:**

        *   **Specific Imagery:** {kwargs.get("specific_imagery", "A lone figure silhouetted against a blood-red moon")}
        *   **Color Palette:** {kwargs.get("color_palette", "Dominantly black and grey, with a splash of crimson red")}
        *   **Overall Tone:**  Dark, unsettling, and suspenseful.

        **Example Visual Styles:**

        *   A black and white photograph of a decaying mansion, with a single window illuminated by a flickering light.
        *   An abstract painting of swirling colors, with a hint of a human face emerging from the chaos.
        *   A close-up of a hand reaching out from the darkness, with long, sharp fingernails.

        **Now, describe the visual style preferences for a Horror novel's back cover based on these guidelines.**
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return HorrorPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return HorrorPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return HorrorPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return HorrorPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return HorrorPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return HorrorPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return HorrorPrompts.get_series_book_prompt(**kwargs)
