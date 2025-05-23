"""
Novella genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class NovellaPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Novella"
    GENRE_DESCRIPTION = "A novella is a work of narrative prose fiction longer than a short story but shorter than a novel. Its length allows for more developed characters and plot than a short story, but it maintains a focused scope and intensity often absent in longer novels. Novellas often explore a single, significant event or theme in a character's life, leading to a concentrated and impactful reading experience."
    
    GENRE_CHARACTERISTICS = [
        "Focused Scope: Novellas typically center on a single, significant event, conflict, or transformation in a character's life, avoiding sprawling subplots or multiple perspectives.",
        "Limited Cast: The number of characters is usually smaller compared to a novel, allowing for deeper exploration of their motivations and relationships.",
        "Concise Plot: The plot is streamlined and efficient, with minimal digressions or unnecessary details, driving directly towards a resolution.",
        "Intense Atmosphere: Novellas often create a strong sense of atmosphere or mood, contributing to the overall impact of the story.",
        "Significant Character Arc: While the plot may be simple, the protagonist often undergoes a significant change or realization by the story's end.",
        "Unified Theme: A central theme or idea is explored in depth, providing a cohesive and meaningful reading experience.",
        "Fast Pacing: Compared to novels, novellas tend to have a quicker pace, maintaining reader engagement through focused storytelling.",
        "Single Setting: Many novellas take place primarily in a single location or a limited number of settings, enhancing the sense of intimacy and focus.",
        "Exploration of a Moral Dilemma: Novellas often present characters facing difficult moral choices, exploring the complexities of human nature.",
        "Subtle Symbolism: Novellas frequently employ symbolism to enrich the narrative and add layers of meaning."
    ]
    
    TYPICAL_ELEMENTS = [
        "A clear inciting incident that sets the plot in motion.",
        "A protagonist with a distinct flaw or vulnerability.",
        "A central conflict that drives the narrative forward.",
        "A limited number of supporting characters who play crucial roles.",
        "A well-defined setting that contributes to the story's atmosphere.",
        "A rising action that builds tension and suspense.",
        "A climax that represents the peak of the conflict.",
        "A resolution that provides closure to the main storyline.",
        "A thematic exploration of a universal human experience.",
        "Use of vivid imagery and sensory details to create a strong sense of place and atmosphere.",
        "Internal monologue or flashbacks to reveal character motivations and backstories.",
        "Symbolic elements that add depth and meaning to the narrative."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        novella_additions = '''
## Novella-Specific Writing Considerations
- **Pacing and Economy**: Maintain a brisk pace, ensuring every scene and sentence contributes to the overall narrative. Avoid unnecessary exposition or digressions.
- **Character Focus**: Prioritize depth over breadth in character development. Focus on a small number of characters and explore their motivations and inner lives thoroughly.
- **Thematic Resonance**: Ensure the story's theme is subtly woven throughout the narrative, emerging organically from the plot and character interactions.
- **Atmospheric Detail**: Use vivid language and sensory details to create a strong sense of atmosphere and immerse the reader in the story's world.
- **Structural Integrity**: Pay close attention to the novella's structure, ensuring a clear beginning, rising action, climax, and resolution. The shorter length demands a tight, well-constructed plot.
- **Impactful Ending**: Craft an ending that is both satisfying and thought-provoking, leaving a lasting impression on the reader. Consider the emotional resonance and thematic implications of the final scene.
- **Subtext and Symbolism**: Employ subtext and symbolism to add layers of meaning to the narrative, enriching the reader's experience and encouraging deeper interpretation.
- **Revision and Refinement**: Given the novella's concise nature, meticulous revision is crucial. Pay attention to every word and sentence, ensuring clarity, precision, and impact.
'''
        return base_prompt + novella_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        novella_additions = '''
## Novella-Specific Outline Requirements
- **Inciting Incident**: Clearly define the event that sets the story in motion and disrupts the protagonist's status quo. This should occur early in the novella.
- **Rising Action (3-5 Key Scenes)**: Outline 3-5 key scenes that build tension and develop the central conflict. Each scene should escalate the stakes and reveal more about the characters and their motivations.
- **Midpoint Shift**: Identify a turning point or significant event that alters the direction of the plot and raises the stakes even higher. This should occur roughly halfway through the novella.
- **Climax**: Plan a single, decisive climax that represents the peak of the conflict. This should be a high-stakes scene with significant consequences for the protagonist.
- **Falling Action (2-3 Key Scenes)**: Outline 2-3 key scenes that show the immediate aftermath of the climax and begin to resolve the central conflict.
- **Resolution**: Define a clear resolution that provides closure to the main storyline and reveals the protagonist's transformation.
- **Thematic Elements**: Identify specific scenes or moments where the novella's central theme will be explored and reinforced.
- **Character Arc Milestones**: Outline key moments in the protagonist's journey that demonstrate their growth or change throughout the story.
- **Setting Integration**: Plan how the setting will be used to enhance the story's atmosphere and contribute to the overall narrative.
- **Word Count Targets**: Break down the outline into approximate word count targets for each section (e.g., Inciting Incident: 500 words, Rising Action: 2000 words, etc.) to ensure the novella stays within its target length.
'''
        return base_prompt + novella_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        novella_additions = '''
## Novella-Specific Character Development
- **Protagonist's Flaw**: Identify a specific flaw or vulnerability that makes the protagonist relatable and drives their character arc. This flaw should be central to the story's conflict.
- **Limited Supporting Cast**: Focus on developing a small number of supporting characters who play crucial roles in the protagonist's journey. Avoid introducing unnecessary characters.
- **Character Relationships**: Define the key relationships between the protagonist and the supporting characters, and how these relationships evolve throughout the story.
- **Internal Motivations**: Explore the internal motivations and desires that drive each character's actions. What are they striving for, and what obstacles stand in their way?
- **Backstory Relevance**: Only include backstory details that are directly relevant to the present-day plot and character motivations. Avoid lengthy or unnecessary exposition.
- **Show, Don't Tell**: Use actions, dialogue, and internal monologue to reveal character traits and motivations, rather than simply stating them outright.
- **Character Transformation**: Plan how the protagonist will change or grow throughout the story, and what events will trigger this transformation.
- **Unique Voice**: Develop a distinct voice for each character, using dialogue and narration to differentiate them and make them memorable.
'''
        return base_prompt + novella_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        novella_additions = '''
## Novella-Specific Chapter Writing
- **Focused Scene Objectives**: Each chapter should have a clear objective that contributes to the overall plot and character development. Avoid aimless or meandering scenes.
- **Pacing and Tension**: Maintain a brisk pace throughout each chapter, building tension and suspense with each scene. Use cliffhangers or unresolved conflicts to keep the reader engaged.
- **Concise Descriptions**: Use vivid language and sensory details to create a strong sense of place and atmosphere, but avoid lengthy or unnecessary descriptions.
- **Dialogue Purpose**: Ensure that all dialogue serves a purpose, whether it's to reveal character traits, advance the plot, or create conflict.
- **Show, Don't Tell**: Use actions, dialogue, and internal monologue to reveal information and develop characters, rather than simply stating it outright.
- **Chapter Endings**: End each chapter with a hook or a question that compels the reader to continue reading.
- **Word Count Awareness**: Be mindful of the overall word count and ensure that each chapter contributes to the novella's target length.
- **Transitions**: Use smooth transitions between scenes and chapters to maintain the flow of the narrative.
'''
        return base_prompt + novella_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return NovellaPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return NovellaPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return NovellaPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return NovellaPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return NovellaPrompts.get_enhancement_prompt(**kwargs)