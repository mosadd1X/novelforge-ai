"""
Speculative Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class SpeculativeFictionPrompts(FictionBasePrompts):
    GENRE_NAME = "Speculative Fiction"
    GENRE_DESCRIPTION = "Speculative fiction explores possibilities beyond the realm of reality as we know it, often extrapolating from current trends or imagining entirely new technologies, societies, or realities. It encompasses subgenres like science fiction, fantasy, alternate history, dystopian fiction, utopian fiction, and supernatural horror, using these frameworks to examine philosophical, social, and political themes. The core of speculative fiction lies in its 'what if' questions, prompting readers to consider the potential consequences of choices and the nature of humanity itself."
    
    GENRE_CHARACTERISTICS = [
        "Worldbuilding is paramount: Creating believable and internally consistent worlds with unique rules, histories, and cultures is crucial for immersing the reader.",
        "Exploration of 'what if' scenarios: The narrative hinges on exploring the ramifications of a specific change to reality, be it technological, social, or magical.",
        "Thematic depth: Speculative fiction often tackles complex philosophical, ethical, and social issues, using the fictional setting as a lens for examining real-world concerns.",
        "Use of allegory and metaphor: The genre frequently employs allegorical storytelling to comment on contemporary society or explore universal human experiences.",
        "Focus on the impact of change: The narrative emphasizes how the speculative element affects individuals, communities, and the world at large.",
        "Sense of wonder and possibility: Speculative fiction aims to evoke a sense of awe and curiosity about the unknown, encouraging readers to imagine different futures or realities.",
        "Subversion of expectations: The genre often challenges conventional wisdom and societal norms, presenting alternative perspectives and possibilities.",
        "Emphasis on plausibility (within the established rules): Even fantastical elements should adhere to a consistent internal logic, making the world believable despite its divergence from reality.",
        "Examination of the human condition: At its core, speculative fiction explores what it means to be human in the face of extraordinary circumstances or transformative technologies."
    ]
    
    TYPICAL_ELEMENTS = [
        "Advanced technology or scientific concepts: Ranging from faster-than-light travel to artificial intelligence to genetic engineering.",
        "Magical systems with defined rules and limitations: If magic is present, it should operate according to consistent principles within the world.",
        "Alternate timelines or historical divergences: Exploring 'what if' scenarios based on pivotal moments in history.",
        "Dystopian societies with oppressive regimes: Often characterized by surveillance, control, and the suppression of individual freedoms.",
        "Utopian societies striving for perfection: Exploring the challenges and potential pitfalls of idealized social structures.",
        "Alien encounters and extraterrestrial civilizations: Interactions with beings from other planets, ranging from peaceful contact to hostile invasion.",
        "Supernatural creatures and phenomena: Vampires, werewolves, ghosts, and other entities that defy the laws of nature.",
        "Post-apocalyptic settings and survival scenarios: Exploring the aftermath of global catastrophes and the struggle to rebuild civilization.",
        "Cyberpunk themes of technology, corporate power, and social decay: Often featuring augmented humans, virtual reality, and hacking.",
        "Steampunk aesthetics blending Victorian-era technology with futuristic elements: Airships, clockwork automatons, and steam-powered devices.",
        "Exploration of consciousness, identity, and transhumanism: Examining the boundaries of human existence and the potential for technological enhancement.",
        "Moral dilemmas arising from technological or social advancements: Exploring the ethical implications of new discoveries and their impact on society."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        speculative_fiction_additions = '''
## Speculative Fiction-Specific Writing Considerations
- **Worldbuilding Depth**: Demonstrate a strong ability to create immersive and believable worlds with consistent internal logic. Consider the history, culture, technology, and ecology of your setting.
- **Conceptual Innovation**: Showcase your capacity to generate original and thought-provoking ideas that challenge conventional thinking and explore new possibilities.
- **Thematic Resonance**: Ensure that your story explores meaningful themes and addresses relevant social, philosophical, or ethical issues through the lens of speculative fiction.
- **Plausibility and Internal Consistency**: Maintain a sense of plausibility within the established rules of your world, even when dealing with fantastical or futuristic elements.
- **Character Development in Extreme Circumstances**: Focus on how characters react and evolve in response to the unique challenges and opportunities presented by the speculative setting.
- **Use of Foresight and Extrapolation**: Demonstrate an understanding of current trends and technologies, and use them as a basis for extrapolating potential future developments.
- **Balance of Speculation and Human Experience**: Ground the speculative elements in relatable human emotions and experiences, making the story engaging and emotionally resonant.
- **Understanding of Subgenres**: Possess a strong understanding of the various subgenres within speculative fiction (e.g., science fiction, fantasy, dystopian, cyberpunk) and their conventions.
'''
        return base_prompt + speculative_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        speculative_fiction_additions = '''
## Speculative Fiction-Specific Outline Requirements
- **Worldbuilding Foundation**: The outline should clearly establish the core elements of the world, including its history, technology, social structures, and any unique rules or laws that govern it.
- **Central Speculative Element**: Identify the key 'what if' question or speculative concept that drives the narrative and how it impacts the characters and the world.
- **Character Arcs and Transformations**: Outline how the characters will be affected by the speculative elements and how they will grow or change throughout the story.
- **Thematic Exploration**: The outline should indicate how the story will explore its central themes through the plot, characters, and setting.
- **Rising Action and Conflict**: Detail the escalating conflicts and challenges that arise as a result of the speculative element, leading to a climax.
- **Climax and Resolution**: Outline the pivotal moment where the central conflict comes to a head and how the story resolves the 'what if' question it poses.
- **Worldbuilding Integration**: Ensure that the plot and character development are seamlessly integrated with the worldbuilding, creating a cohesive and immersive narrative.
- **Plausibility Checks**: Consider the logical consequences of the speculative elements and ensure that the outline maintains internal consistency.
'''
        return base_prompt + speculative_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        speculative_fiction_additions = '''
## Speculative Fiction-Specific Character Development
- **Adaptation to the Speculative World**: Consider how the character has adapted to the unique challenges and opportunities presented by the speculative setting. What skills, knowledge, or traits have they developed to survive or thrive?
- **Moral Compass in Extreme Situations**: Explore how the character's moral compass is tested by the ethical dilemmas and difficult choices that arise in the speculative world.
- **Relationship to Technology or Magic**: Define the character's relationship to the dominant technology or magical system in the world. Are they a user, an innovator, a skeptic, or a victim?
- **Impact of the Speculative Element on Identity**: Consider how the speculative element has shaped the character's identity, beliefs, and values. Have they been transformed by technology, magic, or social change?
- **Internal Conflicts and Motivations**: Develop compelling internal conflicts that drive the character's actions and decisions, especially in the face of adversity.
- **Backstory and Worldbuilding Integration**: Integrate the character's backstory with the worldbuilding, ensuring that their experiences and motivations are rooted in the specific context of the speculative setting.
- **Character Arc and Transformation**: Outline how the character will grow and change throughout the story, learning from their experiences and evolving in response to the challenges they face.
- **Relatability and Human Connection**: Despite the fantastical or futuristic setting, ensure that the character remains relatable and emotionally resonant, allowing readers to connect with their struggles and triumphs.
'''
        return base_prompt + speculative_fiction_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        speculative_fiction_additions = '''
## Speculative Fiction-Specific Chapter Writing
- **Worldbuilding Immersion**: Use vivid descriptions and sensory details to immerse the reader in the speculative world, showcasing its unique features and atmosphere.
- **Show, Don't Tell (Speculative Elements)**: Instead of simply explaining the speculative elements, demonstrate their impact on the characters and the world through action, dialogue, and internal monologue.
- **Pacing and Revelation**: Carefully pace the revelation of new information about the speculative world, building suspense and intrigue as the story unfolds.
- **Character-Driven Exploration**: Use the characters' experiences and perspectives to explore the themes and ideas of the story, making the speculative elements more relatable and engaging.
- **Conflict and Tension**: Create conflict and tension by introducing challenges, obstacles, and moral dilemmas that arise from the speculative elements.
- **Emotional Resonance**: Focus on the emotional impact of the speculative elements on the characters, allowing readers to connect with their struggles and triumphs.
- **Internal Consistency**: Maintain internal consistency within the chapter, ensuring that the speculative elements adhere to the established rules and logic of the world.
- **Subtext and Symbolism**: Use subtext and symbolism to add depth and meaning to the story, exploring the underlying themes and ideas in a subtle and nuanced way.
'''
        return base_prompt + speculative_fiction_additions

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_enhancement_prompt(**kwargs)

        speculative_fiction_additions = '''
## Speculative Fiction-Specific Enhancement Considerations

- **Worldbuilding Enrichment:** Focus on adding more depth and detail to the world, exploring its history, culture, and the intricacies of its speculative elements.
- **Thematic Resonance Amplification:** Strengthen the thematic elements of the story by adding scenes or dialogue that further explore the underlying ideas and messages.
- **Character Arc Deepening:** Enhance the character arcs by adding moments of vulnerability, growth, or transformation that make them more relatable and compelling.
- **Plausibility Reinforcement:** Ensure that the speculative elements are grounded in a sense of plausibility, even if they are fantastical, by adding logical explanations or scientific justifications.
- **Emotional Impact Intensification:** Increase the emotional impact of key scenes by adding sensory details, internal monologues, or dialogue that evoke strong feelings in the reader.
- **Conflict Escalation:** Heighten the conflict by adding new challenges, obstacles, or moral dilemmas that force the characters to make difficult choices.
- **Subtext and Symbolism Layering:** Add layers of subtext and symbolism to the story, allowing readers to discover new meanings and interpretations upon multiple readings.
- **Originality Infusion:** Inject more originality into the story by adding unique twists, unexpected turns, or unconventional perspectives that set it apart from other speculative fiction works.
'''

        return base_prompt + speculative_fiction_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a speculativefiction-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        speculativefiction_series_additions = """

## SpeculativeFiction Series-Specific Planning Elements

### Genre-Specific Series Development
- **SpeculativeFiction Conventions**: Ensure each book fulfills speculativefiction reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to speculativefiction
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to speculativefiction
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore speculativefiction themes with increasing depth and complexity

### SpeculativeFiction Series Continuity
- **Genre Elements**: Maintain consistent speculativefiction elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy speculativefiction readers
- **Series Identity**: Establish a strong series identity that feels authentically speculativefiction
- **World Building**: Develop the story world in ways that enhance the speculativefiction experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the speculativefiction genre

Create a speculativefiction series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + speculativefiction_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a speculativefiction-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        speculativefiction_book_additions = """

## SpeculativeFiction Series Book Integration

### SpeculativeFiction Continuity for This Book
- **Genre Consistency**: Maintain established speculativefiction elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to speculativefiction
- **Plot Advancement**: Continue series plot threads while telling a complete speculativefiction story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill speculativefiction reader expectations while advancing the series narrative

### Book-Specific SpeculativeFiction Focus
- **Central Conflict**: What speculativefiction-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new speculativefiction elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent speculativefiction while serving the series?

Ensure this book feels like an authentic continuation of the speculativefiction series while telling a complete, satisfying story.
"""
        
        return base_prompt + speculativefiction_book_additions

        ```python
        class SpeculativeFictionMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions for Speculative Fiction novels.

        Args:
        **kwargs: Keyword arguments containing book details such as title, author, main character, setting, plot summary, themes, target audience, and comparable titles.

        Returns:
        A string containing the prompt for the AI model.
        """

        prompt = f"""
        Craft a captivating back cover description for a Speculative Fiction novel. Consider the following details:

        **Book Title:** {kwargs.get('title', '[Book Title]')}
        **Author:** {kwargs.get('author', '[Author Name]')}
        **Main Character(s):** {kwargs.get('main_character', '[Main Character Name(s)]')} - Briefly describe their personality and motivations.
        **Setting:** {kwargs.get('setting', '[Setting Description]')} - Emphasize the unique or altered aspects of the setting that make it Speculative Fiction. Is it a dystopian society, a futuristic world, an alternate history, a world with magic, or a reality altered by technology? Be specific.
        **Plot Summary:** {kwargs.get('plot_summary', '[Plot Summary]')} - Concisely outline the central conflict and the stakes involved. Focus on the core speculative element driving the narrative.
        **Themes:** {kwargs.get('themes', '[Themes Explored]')} - Highlight the thought-provoking themes explored in the novel, such as the nature of humanity, the impact of technology, social justice, morality, or the consequences of choices.
        **Target Audience:** {kwargs.get('target_audience', '[Target Audience]')} - (e.g., fans of dystopian fiction, readers interested in AI ethics, etc.)
        **Comparable Titles:** {kwargs.get('comparable_titles', '[Comparable Titles]')} - (e.g., "If you enjoyed 'The Handmaid's Tale' or 'Ready Player One', you'll love this.")

        **Instructions:**

        1.  **Begin with a Hook:** Start with a compelling question, a striking image, or a provocative statement that immediately grabs the reader's attention.  Examples:
        *   "What if reality wasn't what you thought it was?"
        *   "In a world where [SPECULATIVE ELEMENT], one person dares to..."
        *   "The year is [YEAR], and humanity is on the brink..."

        2.  **Emphasize the Speculative Element:** Clearly showcase the core speculative element that defines the novel. This could be advanced technology, magic systems, alternate timelines, alien encounters, or societal shifts. Make it intriguing and relevant to the plot.

        3.  **Highlight the Stakes:** What are the consequences if the protagonist fails?  Focus on the potential for societal collapse, personal loss, or the alteration of reality itself.

        4.  **Focus on Emotional Resonance:** Connect with the reader's emotions. Explore themes of hope, fear, love, loss, rebellion, or redemption. Make them care about the characters and their struggles.

        5.  **Create Intrigue and Mystery:** Hint at secrets, conspiracies, or hidden truths that the protagonist must uncover. Leave the reader wanting to know more.

        6.  **End with a Cliffhanger:** Conclude with a tantalizing question or a statement that leaves the reader eager to dive into the story.

        7.  **Genre Conventions:** Adhere to the conventions of Speculative Fiction. Focus on world-building, plausible extrapolation, and thought-provoking explorations of "what if" scenarios.

        8.  **Word Count:** Aim for approximately 150-200 words.

        **Example Openings (Modify to fit the book):**

        *   "In the neon-drenched metropolis of Neo-Tokyo, where artificial intelligence reigns supreme, a rogue programmer discovers a hidden code that could shatter the foundations of reality."
        *   "Generations after the Great Collapse, humanity clings to survival in underground bunkers, haunted by the ghosts of a world lost to ecological disaster. But a whisper of hope emerges from the ruins..."
        *   "Elara was born with a gift, a curse, that set her apart from the rigid Order of Mages. Now, she must choose between obedience and rebellion, as a dark prophecy threatens to consume the land."

        **Write a back cover description that will entice readers to pick up this book and lose themselves in a world of imagination and possibility.**
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, impactful description for Speculative Fiction novels (2-3 lines). Ideal for book recommendations.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, genre, key themes).

        Returns:
        A string containing the prompt for the AI model.
        """

        prompt = f"""
        Create a concise and compelling 2-3 line description for a Speculative Fiction novel, suitable for a book recommendation or a quick summary.

        **Book Title:** {kwargs.get('title', '[Book Title]')}
        **Author:** {kwargs.get('author', '[Author Name]')}
        **Genre:** Speculative Fiction (Focus on the specific subgenre if applicable, e.g., Dystopian, Cyberpunk, Space Opera)
        **Key Themes:** {kwargs.get('themes', '[Key Themes]')} - List 2-3 main themes explored in the book.

        **Instructions:**

        1.  **Focus on Intrigue:** Start with a hook that immediately grabs the reader's attention.
        2.  **Highlight the Speculative Element:** Clearly state the core speculative element that defines the story (e.g., "AI gone rogue," "a parallel universe," "magic returning to Earth").
        3.  **Emphasize the stakes:** Hint at the consequences or conflict that drives the narrative.
        4.  **Use strong, evocative language:** Choose words that paint a vivid picture and create a sense of wonder or unease.
        5.  **Keep it brief and impactful:** Every word counts!

        **Examples:**

        *   "In a city powered by dreams, one woman discovers a nightmare that could unravel reality."
        *   "Humanity fled Earth, only to find that the stars hold secrets far more terrifying than they imagined."
        *   "When magic returns to a world ruled by technology, chaos and hope collide in an epic struggle for survival."

        **Write a short description that will make readers instantly want to learn more about this Speculative Fiction novel.**
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy and memorable marketing tagline for Speculative Fiction novels.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, core concept).

        Returns:
        A string containing the prompt for the AI model.
        """

        prompt = f"""
        Craft a short, attention-grabbing marketing tagline for a Speculative Fiction novel.

        **Book Title:** {kwargs.get('title', '[Book Title]')}
        **Core Concept:** {kwargs.get('core_concept', '[Core Concept of the Book]')} - Briefly describe the central idea or premise of the book (e.g., "AI singularity," "time travel paradox," "magical rebellion").

        **Instructions:**

        1.  **Keep it concise:** Aim for a tagline of 5-10 words.
        2.  **Highlight the speculative element:** Emphasize what makes the book unique and thought-provoking.
        3.  **Create intrigue:** Make the reader curious to learn more.
        4.  **Use strong verbs and imagery:** Choose words that are impactful and memorable.
        5.  **Consider the tone:** Is the book dark and gritty, or optimistic and hopeful? The tagline should reflect the overall tone.

        **Examples:**

        *   "Reality is hacked. Humanity is the virus." (Cyberpunk)
        *   "The future is closer than you think. And darker." (Dystopian)
        *   "Magic reborn. The world will never be the same." (Fantasy/Sci-Fi Blend)
        *   "What if the past could be rewritten? At what cost?" (Alternate History)
        *   "Beyond the stars, a war for humanity's soul." (Space Opera)

        **Write a tagline that will stick in readers' minds and make them want to explore this Speculative Fiction world.**
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for suggesting visual style preferences for the back cover design of a Speculative Fiction novel.

        Args:
        **kwargs: Keyword arguments containing book details (setting, themes, tone).

        Returns:
        A string containing the prompt for the AI model.
        """

        prompt = f"""
        Suggest visual style preferences for the back cover design of a Speculative Fiction novel.

        **Book Setting:** {kwargs.get('setting', '[Setting Description]')} - Describe the visual aspects of the setting (e.g., futuristic cityscape, desolate wasteland, enchanted forest).
        **Themes:** {kwargs.get('themes', '[Themes Explored]')} - List the key themes that should be visually represented.
        **Tone:** {kwargs.get('tone', '[Overall Tone of the Book]')} - (e.g., Dark, gritty, hopeful, whimsical, mysterious)

        **Instructions:**

        1.  **Color Palette:** Suggest a color palette that reflects the setting and tone. Consider using cool colors for futuristic or dystopian settings, warm colors for magical or fantastical settings, and contrasting colors to create tension or drama.
        2.  **Imagery:** Suggest specific imagery that could be used on the back cover. This could include landscapes, characters, objects, or abstract designs.  Consider how the imagery can visually represent the core speculative element of the story.
        3.  **Typography:** Suggest font styles that are appropriate for the genre and tone. Consider using futuristic fonts for cyberpunk or science fiction, elegant fonts for fantasy, and bold fonts for action-packed stories.
        4.  **Overall Style:** Describe the overall visual style of the back cover. Should it be minimalist, detailed, abstract, realistic, or stylized?
        5.  **Inspirational Examples:** Mention specific artists, designers, or book covers that could serve as inspiration.

        **Examples:**

        *   **Cyberpunk:** "Dark, neon-lit cityscape with glitch effects, using a color palette of electric blue, hot pink, and deep black. A futuristic, sans-serif font would complement the technological theme."
        *   **Dystopian:** "A desolate, barren landscape with a cracked earth texture, using a color palette of muted grays, browns, and reds. A distressed, handwritten font would convey a sense of decay and desperation."
        *   **Fantasy:** "An enchanted forest with glowing flora and fauna, using a color palette of emerald green, sapphire blue, and gold. An elegant, calligraphic font would evoke a sense of magic and wonder."
        *   **Space Opera:** "A vast, swirling nebula with distant planets and spaceships, using a color palette of deep purples, blues, and oranges. A bold, futuristic font would convey a sense of adventure and exploration."

        **Provide detailed visual style preferences that will help create a back cover that is visually appealing and accurately reflects the essence of this Speculative Fiction novel.**
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return SpeculativeFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return SpeculativeFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return SpeculativeFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return SpeculativeFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return SpeculativeFictionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return SpeculativeFictionPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return SpeculativeFictionPrompts.get_series_book_prompt(**kwargs)
