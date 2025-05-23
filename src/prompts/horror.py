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