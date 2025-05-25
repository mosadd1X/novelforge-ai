"""
Dystopian genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class DystopianPrompts(FictionBasePrompts):
    GENRE_NAME = "Dystopian"
    GENRE_DESCRIPTION = "Dystopian fiction explores societies characterized by oppressive social control, often presented as futuristic or exaggerated versions of contemporary trends. These narratives typically critique existing power structures, warn against unchecked technological advancement, and examine the loss of individual autonomy in the face of totalitarian regimes or societal collapse."

    GENRE_CHARACTERISTICS = [
        "Oppressive Control: A governing body or societal force exerts extreme control over citizens' lives, limiting freedom of thought, expression, and action.",
        "Loss of Individuality: Characters often struggle to maintain their unique identities within a conformist society that values uniformity and obedience.",
        "Propaganda and Surveillance: The ruling power utilizes propaganda, misinformation, and constant surveillance to manipulate and control the population.",
        "Technological Control: Advanced technology is often used as a tool for oppression, monitoring citizens, and enforcing conformity.",
        "Environmental Decay: Dystopian societies frequently depict environments ravaged by pollution, resource depletion, or ecological disaster, reflecting the consequences of societal choices.",
        "Social Stratification: Stark inequalities exist between different social classes, with the ruling elite enjoying privileges denied to the masses.",
        "Suppression of History and Knowledge: Historical records are often manipulated or destroyed to control the narrative and prevent dissent.",
        "Rebellion and Resistance: Characters may actively resist the oppressive regime, seeking to reclaim their freedom and challenge the established order.",
        "Dehumanization: Citizens are often treated as cogs in a machine, stripped of their humanity and reduced to their functional roles.",
        "Loss of Hope: A pervasive sense of despair and hopelessness permeates the society, making resistance seem futile."
    ]

    TYPICAL_ELEMENTS = [
        "Totalitarian Government: A single, all-powerful entity controls all aspects of life.",
        "Surveillance State: Constant monitoring of citizens' activities and communications.",
        "Propaganda Machine: Dissemination of biased information to manipulate public opinion.",
        "Censorship: Suppression of dissenting voices and control over information access.",
        "Social Engineering: Manipulation of social structures to maintain control.",
        "Environmental Catastrophe: Pollution, climate change, or resource depletion leading to societal breakdown.",
        "Genetic Engineering: Manipulation of human genetics for control or societal improvement (often with unintended consequences).",
        "Artificial Intelligence: AI used for surveillance, control, or even replacing human roles.",
        "Thought Police: Enforcement of ideological conformity through punishment of dissenting thoughts.",
        "Black Market: Underground economy operating outside the control of the ruling power.",
        "Rebel Groups: Organized resistance movements fighting against the oppressive regime.",
        "Escape Attempts: Characters trying to flee the dystopian society to find freedom."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        dystopian_additions = '''
## Dystopian-Specific Writing Considerations
- **Worldbuilding Depth**: Craft a believable and internally consistent dystopian world with detailed rules, social structures, and historical context. Consider the political, economic, and technological factors that led to the dystopian state.
- **Thematic Resonance**: Explore relevant social and political themes, such as the dangers of unchecked power, the importance of individual freedom, and the consequences of environmental destruction.
- **Character Motivation**: Ensure that characters' actions and motivations are believable within the context of the dystopian world. Explore their internal struggles and moral dilemmas.
- **Atmosphere and Tone**: Create a sense of unease, oppression, and despair through vivid descriptions, evocative language, and a consistent tone.
- **Plausible Technology**: If incorporating technology, ensure it is believable and serves a purpose within the narrative, either as a tool of oppression or a source of hope.
- **Social Commentary**: Use the dystopian setting to critique contemporary societal trends and warn against potential future dangers.
- **Moral Ambiguity**: Explore the gray areas of morality and the difficult choices characters must make in a dystopian world.
- **Hope and Resistance**: While depicting a bleak reality, consider incorporating elements of hope, resilience, and the possibility of resistance against the oppressive forces.
'''
        return base_prompt + dystopian_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        dystopian_additions = '''
## Dystopian-Specific Outline Requirements
- **Exposition of the Dystopian Society**: Clearly establish the rules, social structures, and oppressive elements of the dystopian world in the early chapters.
- **Introduction of the Protagonist**: Introduce a protagonist who is either complacent within the system or begins to question it.
- **Inciting Incident**: A catalyst that disrupts the protagonist's life and forces them to confront the true nature of the dystopian society.
- **Rising Action**: The protagonist's journey of discovery, resistance, and struggle against the oppressive forces. This may involve joining a rebel group, uncovering secrets, or experiencing personal loss.
- **Climax**: A major confrontation between the protagonist and the ruling power or a critical turning point in the rebellion.
- **Falling Action**: The consequences of the climax, including the aftermath of the confrontation and the impact on the protagonist and the society.
- **Resolution**: The final outcome of the story, which may involve the overthrow of the oppressive regime, the establishment of a new order, or the protagonist's escape or sacrifice.
- **Thematic Development**: Ensure that the outline incorporates key dystopian themes, such as the loss of freedom, the dangers of technology, and the importance of resistance.
- **Character Arcs**: Plan the development of key characters, including their motivations, relationships, and transformations throughout the story.
- **Worldbuilding Consistency**: Maintain consistency in the worldbuilding throughout the outline, ensuring that the rules and social structures of the dystopian society are consistently applied.
'''
        return base_prompt + dystopian_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)

        dystopian_additions = '''
## Dystopian-Specific Character Development
- **Oppressed Protagonist**: The protagonist is often a victim of the dystopian system, struggling to survive and maintain their humanity in the face of oppression.
- **Rebellious Spirit**: Characters may possess a strong sense of justice and a desire to fight against the oppressive regime, even at great personal risk.
- **Moral Ambiguity**: Characters may be forced to make difficult choices that challenge their moral compass, blurring the lines between right and wrong.
- **Internal Conflict**: Characters often grapple with internal conflicts, such as the desire for freedom versus the fear of reprisal, or the need for survival versus the desire for justice.
- **Symbolic Representation**: Characters can represent different aspects of the dystopian society, such as the oppressed masses, the ruling elite, or the forces of resistance.
- **Flawed Heroes**: Protagonists should have flaws and vulnerabilities that make them relatable and believable, even in extraordinary circumstances.
- **Complex Antagonists**: Antagonists should be more than just evil villains; they should have motivations and beliefs that are understandable, even if they are morally reprehensible.
- **Character Relationships**: Explore the impact of the dystopian society on relationships between characters, such as family members, friends, and lovers.
'''
        return base_prompt + dystopian_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        dystopian_additions = '''
## Dystopian-Specific Chapter Writing
- **Establish Atmosphere**: Use vivid descriptions and sensory details to create a sense of unease, oppression, and despair in the dystopian setting.
- **Show, Don't Tell**: Instead of simply stating that the society is oppressive, show examples of the control and manipulation that citizens experience.
- **Build Suspense**: Create suspense by hinting at dangers and threats, and by gradually revealing the true nature of the dystopian society.
- **Develop Characters**: Use each chapter to further develop the characters, revealing their motivations, relationships, and internal conflicts.
- **Advance the Plot**: Ensure that each chapter contributes to the overall plot, moving the story forward and building towards the climax.
- **Explore Themes**: Use each chapter to explore key dystopian themes, such as the loss of freedom, the dangers of technology, and the importance of resistance.
- **Use Foreshadowing**: Hint at future events and consequences to create a sense of anticipation and dread.
- **End with a Hook**: End each chapter with a cliffhanger or a compelling question that will keep readers engaged and eager to continue reading.
'''
        return base_prompt + dystopian_additions

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_enhancement_prompt(**kwargs)

        dystopian_additions = '''
## Dystopian-Specific Enhancement Considerations
- **Amplify the Oppression**: Focus on intensifying the sense of control, surveillance, and lack of freedom within the society. Consider adding more specific examples of how the regime exerts its power.
- **Deepen the Character's Internal Conflict**: Explore the protagonist's moral dilemmas and internal struggles more thoroughly. Add layers of complexity to their motivations and decisions.
- **Heighten the Stakes**: Increase the risks and consequences for the characters, making their choices even more difficult and impactful.
- **Sharpen the Social Commentary**: Make the critique of contemporary societal trends more pointed and relevant. Consider adding specific examples of how the dystopian society reflects current issues.
- **Enhance the Worldbuilding**: Add more details to the dystopian setting, making it more believable and immersive. Consider expanding on the history, culture, and technology of the society.
- **Intensify the Emotional Impact**: Focus on evoking stronger emotions in the reader, such as fear, despair, hope, and anger. Use vivid language and sensory details to create a more visceral experience.
- **Strengthen the Thematic Resonance**: Reinforce the key dystopian themes throughout the story, ensuring that they are consistently explored and developed.
- **Increase the Tension**: Add more suspense and uncertainty to the plot, keeping readers on the edge of their seats.
'''
        return base_prompt + dystopian_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a dystopian-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        dystopian_series_additions = """

## Dystopian Series-Specific Planning Elements

### Genre-Specific Series Development
- **Dystopian Conventions**: Ensure each book fulfills dystopian reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to dystopian
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to dystopian
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore dystopian themes with increasing depth and complexity

### Dystopian Series Continuity
- **Genre Elements**: Maintain consistent dystopian elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy dystopian readers
- **Series Identity**: Establish a strong series identity that feels authentically dystopian
- **World Building**: Develop the story world in ways that enhance the dystopian experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the dystopian genre

Create a dystopian series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + dystopian_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a dystopian-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        dystopian_book_additions = """

## Dystopian Series Book Integration

### Dystopian Continuity for This Book
- **Genre Consistency**: Maintain established dystopian elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to dystopian
- **Plot Advancement**: Continue series plot threads while telling a complete dystopian story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill dystopian reader expectations while advancing the series narrative

### Book-Specific Dystopian Focus
- **Central Conflict**: What dystopian-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new dystopian elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent dystopian while serving the series?

Ensure this book feels like an authentic continuation of the dystopian series while telling a complete, satisfying story.
"""
        
        return base_prompt + dystopian_book_additions

        ```python
        class DystopianMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating a compelling dystopian back cover description.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, protagonist, setting).

        Returns:
        A string containing the prompt for generating a dystopian back cover description.
        """
        prompt = f"""
        Write a compelling back cover description for a dystopian novel.

        Genre: Dystopian

        Core Elements to Emphasize:

        *   Oppressive Regime: Highlight the controlling force (government, corporation, AI) and its methods of control (surveillance, propaganda, resource manipulation, thought control).
        *   Loss of Individuality: Show how the system crushes individuality, creativity, and free thought. Emphasize conformity and the suppression of dissent.
        *   Social Stratification: Depict the stark inequalities within the society – the powerful elite versus the oppressed masses.
        *   Protagonist's Rebellion: Introduce a compelling protagonist who questions the system and embarks on a dangerous path of rebellion.  Make their motivations clear and relatable (e.g., a lost loved one, a sense of injustice, a yearning for freedom).
        *   Bleak Setting: Paint a vivid picture of the dystopian world – its physical decay, environmental degradation, and psychological atmosphere of fear and despair.
        *   High Stakes: Emphasize the dangers the protagonist faces – imprisonment, torture, death, or the loss of everything they hold dear.
        *   Hope (Optional): While the tone should be dark, consider including a glimmer of hope – a possibility of change, a spark of humanity, or the strength of the human spirit to endure.  This should not undermine the core dystopian themes.

        Specifics for this Novel:

        *   Title: {kwargs.get('title', '[Insert Title Here]')}
        *   Protagonist: {kwargs.get('protagonist', '[Insert Protagonist Name]')} - Briefly describe their personality, skills, and motivations.
        *   Setting: {kwargs.get('setting', '[Insert Setting Description Here]')} - Describe the physical and societal environment.  Include details about technology, architecture, and social norms.
        *   Central Conflict: {kwargs.get('conflict', '[Insert Central Conflict Here]')} - Summarize the main conflict the protagonist faces.
        *   Target Audience:  Young Adult or Adult Dystopian readers?  Tailor the tone and complexity accordingly.
        *   Key Themes: What are the major themes explored in the novel (e.g., control, freedom, identity, survival, hope, technology)?

        Instructions for Writing the Description:

        *   Start with a hook: Capture the reader's attention immediately with a compelling question, a shocking statement, or a glimpse into the protagonist's desperate situation.
        *   Describe the world: Briefly paint a picture of the dystopian society and the forces that control it.
        *   Introduce the protagonist: Highlight their unique qualities and their reason for questioning the system.
        *   Outline the conflict: Briefly summarize the main conflict and the stakes involved.
        *   End with a cliffhanger: Leave the reader wanting to know more and eager to discover the protagonist's fate.
        *   Length: Approximately 150-200 words.
        *   Tone: Dark, suspenseful, thought-provoking, and emotionally resonant.
        *   Use strong verbs and vivid imagery to create a sense of urgency and dread.
        *   Avoid spoilers! Focus on the setup and the initial conflict.

        Example Dystopian Back Cover Description (for Inspiration):

        In a world where thoughts are monitored and individuality is a crime, sixteen-year-old Anya lives in constant fear. The Authority controls every aspect of life in the Collective, from the food they eat to the jobs they perform. But when Anya discovers a hidden message from the past, she begins to question everything she's ever known. Drawn into a secret underground resistance, Anya must choose between conformity and rebellion, knowing that one wrong move could cost her everything.  Can she expose the truth before the Authority silences her forever?
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short (2-3 line) dystopian book recommendation description.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, protagonist, setting).

        Returns:
        A string containing the prompt for generating a short dystopian description.
        """
        prompt = f"""
        Write a very short (2-3 lines) book recommendation description for a dystopian novel.

        Genre: Dystopian

        Focus:

        *   Conciseness: Keep it brief and impactful.
        *   Intrigue: Focus on the most intriguing aspect of the story.
        *   Dystopian Elements: Clearly establish the dystopian setting and conflict.

        Specifics for this Novel:

        *   Title: {kwargs.get('title', '[Insert Title Here]')}
        *   Protagonist: {kwargs.get('protagonist', '[Insert Protagonist Name]')} - Briefly mention their role.
        *   Dystopian Element: {kwargs.get('dystopian_element', '[Insert Dystopian Element Here]')} - What makes this world dystopian? (e.g., surveillance state, environmental collapse, social control).
        *   Conflict: {kwargs.get('conflict', '[Insert Central Conflict Here]')} - What's the core struggle?

        Instructions:

        *   Highlight the core dystopian element of the story.
        *   Briefly introduce the protagonist and their role in the conflict.
        *   End with a hook to encourage readers to learn more.
        *   Use strong, evocative language.

        Example:

        In a city choked by toxic smog, Elara discovers a forbidden garden, sparking a rebellion against the corporation that controls the air they breathe.  Will she save her city, or be crushed under its oppressive weight?
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for a punchy dystopian marketing tagline.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, protagonist, setting).

        Returns:
        A string containing the prompt for generating a dystopian marketing tagline.
        """
        prompt = f"""
        Write a punchy and memorable marketing tagline for a dystopian novel.

        Genre: Dystopian

        Key Considerations:

        *   Brevity: Keep it short and impactful (ideally under 10 words).
        *   Intrigue: Evoke curiosity and a sense of danger.
        *   Dystopian Themes: Reflect the core themes of dystopian fiction (control, oppression, rebellion, loss of freedom).
        *   Emotional Resonance: Tap into the emotions associated with dystopian settings (fear, hope, despair, anger).

        Specifics for this Novel:

        *   Title: {kwargs.get('title', '[Insert Title Here]')}
        *   Core Conflict: {kwargs.get('conflict', '[Insert Central Conflict Here]')} - What's the central struggle?
        *   Unique Dystopian Element: {kwargs.get('dystopian_element', '[Insert Dystopian Element Here]')} - What's unique about this dystopian world?

        Instructions:

        *   Focus on the central conflict or the most striking element of the dystopian world.
        *   Use strong verbs and powerful imagery.
        *   Consider using a question or a provocative statement.
        *   Target the emotions associated with dystopian fiction.

        Examples:

        *   "Freedom is a virus. Rebellion is the cure."
        *   "In a world of silence, one voice can ignite a revolution."
        *   "They control your mind. She will break it."
        *   "What if hope is the most dangerous weapon of all?"
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for back cover visual design preferences for a dystopian novel.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., title, protagonist, setting).

        Returns:
        A string containing the prompt for visual style direction.
        """
        prompt = f"""
        Describe the desired visual style for the back cover of a dystopian novel.

        Genre: Dystopian

        Considerations:

        *   Color Palette:  What colors evoke the mood and themes of the story? (e.g., muted tones, grays, blacks, industrial colors, pops of vibrant color to represent rebellion or hope).
        *   Imagery: What kind of images would be most effective? (e.g., cityscape, technology, protagonist's face, symbolic representation of the conflict).
        *   Typography: What font styles would be appropriate? (e.g., futuristic, industrial, distressed, bold).
        *   Overall Tone: The cover should convey the dark, oppressive, and suspenseful atmosphere of the dystopian world.
        *   Target Audience: Consider the target audience (Young Adult or Adult) and their visual preferences.

        Specifics for this Novel:

        *   Title: {kwargs.get('title', '[Insert Title Here]')}
        *   Setting: {kwargs.get('setting', '[Insert Setting Description Here]')} - The visual style should reflect the setting.
        *   Protagonist: {kwargs.get('protagonist', '[Insert Protagonist Name]')} - Should the protagonist's image be included? If so, what should their expression convey?
        *   Dystopian Element: {kwargs.get('dystopian_element', '[Insert Dystopian Element Here]')} - Can this element be visually represented? (e.g., surveillance cameras, pollution, oppressive architecture).
        *   Mood: What is the overall mood the cover should evoke? (e.g., fear, despair, hope, rebellion).

        Instructions:

        *   Provide a detailed description of the desired visual style.
        *   Include specific examples of colors, imagery, and typography.
        *   Explain how the visual style should reflect the themes and setting of the novel.
        *   Consider referencing existing dystopian book covers or artwork for inspiration.

        Example:

        The back cover should feature a desaturated color palette of grays, blacks, and rusty browns. The central image should be a stylized silhouette of the protagonist against a backdrop of a crumbling cityscape, dominated by towering surveillance towers. The font should be a bold, sans-serif typeface with a slightly distressed appearance. The overall tone should be bleak and oppressive, conveying the sense of a world on the brink of collapse. A single, small splash of vibrant red (perhaps on the protagonist's clothing) could represent a spark of rebellion.
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return DystopianPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return DystopianPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return DystopianPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return DystopianPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return DystopianPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return DystopianPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return DystopianPrompts.get_series_book_prompt(**kwargs)
