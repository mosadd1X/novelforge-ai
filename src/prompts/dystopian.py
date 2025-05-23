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