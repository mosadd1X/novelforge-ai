"""
Urban Fantasy genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class UrbanFantasyPrompts(FictionBasePrompts):
    GENRE_NAME = "Urban Fantasy"
    GENRE_DESCRIPTION = "Urban Fantasy is a subgenre of fantasy characterized by its setting in an urban environment. It typically features supernatural elements such as magic, mythical creatures, and paranormal phenomena existing alongside and often hidden within the mundane reality of a city. The genre often explores themes of identity, power, and the clash between the ordinary and the extraordinary."
    
    GENRE_CHARACTERISTICS = [
        "A contemporary urban setting, often a recognizable city like New York, London, or Tokyo, but sometimes a fictional city with a similar feel.",
        "The presence of magic, supernatural creatures (vampires, werewolves, fae, etc.), or other paranormal phenomena that are not widely known or accepted by the general public.",
        "A protagonist who is often caught between the mundane world and the supernatural one, possessing unique abilities or knowledge that allows them to navigate both.",
        "A strong sense of mystery and intrigue, often involving investigations into supernatural crimes or conspiracies.",
        "Exploration of the hidden or secret societies that operate within the urban environment, often with their own rules, hierarchies, and agendas.",
        "A blend of fantasy elements with aspects of other genres, such as crime fiction, thriller, romance, or horror.",
        "Themes of identity, alienation, and the struggle to find one's place in a world where the ordinary and the extraordinary collide.",
        "A focus on the impact of magic and the supernatural on everyday life, exploring how these elements affect social structures, relationships, and personal experiences.",
        "Moral ambiguity and complex characters, where the lines between good and evil are often blurred.",
        "A fast-paced plot with action sequences and suspenseful moments, reflecting the energy and dynamism of the urban setting."
    ]
    
    TYPICAL_ELEMENTS = [
        "A protagonist with hidden magical abilities or a connection to the supernatural world.",
        "A secret society or organization that governs the supernatural community.",
        "A magical artifact or object of power that is sought after by various factions.",
        "A hidden portal or gateway to another realm or dimension.",
        "A supernatural creature (vampire, werewolf, fae, demon, etc.) as a major character or antagonist.",
        "A magical curse or enchantment that affects the protagonist or the city itself.",
        "A detective or investigator who specializes in supernatural crimes.",
        "A mentor figure who guides the protagonist in their understanding and use of magic.",
        "A romantic relationship between a human and a supernatural being.",
        "A conspiracy involving powerful individuals or organizations seeking to control the supernatural world.",
        "A magical duel or battle between opposing factions.",
        "A hidden magical location or sanctuary within the city."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Writing Considerations
- **Worldbuilding**: Focus on creating a believable urban environment where the supernatural can plausibly exist in secret. Consider the history of magic in the city, the rules governing its use, and the impact it has on the mundane world.
- **Character Development**: Develop characters with compelling motivations and flaws, who are believable both as individuals and as members of their respective communities (human or supernatural). Explore their internal conflicts and how they navigate the challenges of living in a world where the ordinary and the extraordinary collide.
- **Plot and Pacing**: Craft a plot that is both engaging and suspenseful, with a clear sense of direction and escalating stakes. Maintain a fast pace that reflects the energy of the urban setting, while also allowing for moments of character development and worldbuilding.
- **Magic System**: Define a clear and consistent magic system with its own rules, limitations, and consequences. Avoid deus ex machina solutions and ensure that magic is used in a way that is both believable and integral to the plot.
- **Tone and Atmosphere**: Establish a consistent tone that balances the fantastical elements with the gritty realism of the urban setting. Create an atmosphere that is both mysterious and intriguing, with a sense of danger lurking beneath the surface.
- **Thematic Resonance**: Explore themes that are relevant to the urban fantasy genre, such as identity, power, alienation, and the struggle to find one's place in the world. Use the supernatural elements to comment on social issues and explore the human condition.
- **Research**: Thoroughly research the urban environment you are writing about, paying attention to its history, culture, and social dynamics. This will help you create a more believable and immersive setting for your story.
- **Subverting Tropes**: Be aware of common urban fantasy tropes and consider ways to subvert or subvert them to create a fresh and original story.
'''
        return base_prompt + urban_fantasy_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Outline Requirements
- **Inciting Incident**: The inciting incident should introduce the protagonist to the supernatural world or a specific problem within it. This could be a magical attack, the discovery of a hidden artifact, or a request for help from a supernatural being.
- **Rising Action**: The rising action should involve the protagonist investigating the supernatural problem, learning about the rules and factions of the supernatural world, and developing their own abilities or knowledge. Include encounters with supernatural creatures, clues that lead to further mysteries, and escalating conflicts with antagonists.
- **Midpoint**: The midpoint should be a major turning point in the story, where the protagonist gains a significant piece of information or experiences a major setback that changes their understanding of the situation. This could be the revelation of a hidden conspiracy, the loss of a key ally, or a betrayal by someone they trusted.
- **Climax**: The climax should be a confrontation between the protagonist and the main antagonist, where they must use their abilities and knowledge to overcome the supernatural threat. This could involve a magical duel, a battle against a horde of supernatural creatures, or a race against time to prevent a catastrophic event.
- **Falling Action**: The falling action should resolve the immediate conflict and address any remaining loose ends. This could involve cleaning up the aftermath of the climax, dealing with the consequences of the protagonist's actions, and setting the stage for future stories.
- **Resolution**: The resolution should provide a sense of closure and leave the reader with a feeling of satisfaction. This could involve the protagonist finding a new purpose in the supernatural world, forging lasting relationships with other characters, or achieving a personal transformation.
- **Worldbuilding Notes**: Include specific notes about the urban setting, the magic system, the supernatural creatures, and the various factions that operate within the story. These notes should be detailed and consistent, providing a solid foundation for the story's worldbuilding.
- **Character Arcs**: Outline the major character arcs for the protagonist and other key characters, focusing on their personal growth and development throughout the story. Consider how their experiences in the supernatural world change them as individuals.
- **Thematic Elements**: Identify the key thematic elements that you want to explore in your story, such as identity, power, alienation, or the clash between the ordinary and the extraordinary. Ensure that these themes are woven throughout the plot and character development.
'''
        return base_prompt + urban_fantasy_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Character Development
- **Dual Identity**: Consider how the character navigates the dual existence between the mundane world and the supernatural one. Do they keep their supernatural life a secret? How does this affect their relationships and daily routines?
- **Magical Abilities**: Define the character's magical abilities or connection to the supernatural world. What are their strengths and weaknesses? How did they acquire these abilities? What are the limitations or consequences of using them?
- **Moral Alignment**: Explore the character's moral compass and how it is influenced by their experiences in the supernatural world. Are they a hero, a villain, or something in between? What are their motivations and goals?
- **Backstory**: Develop a detailed backstory that explains the character's origins, motivations, and relationships. How did their past experiences shape them into the person they are today? What secrets are they hiding?
- **Relationships**: Consider the character's relationships with other characters, both human and supernatural. Who are their allies and enemies? How do these relationships affect their decisions and actions?
- **Internal Conflicts**: Explore the character's internal conflicts and struggles. Are they grappling with their identity, their powers, or their place in the world? How do they overcome these challenges?
- **Appearance and Demeanor**: Describe the character's physical appearance and demeanor, paying attention to details that reflect their personality and background. Do they dress in a way that blends in with the mundane world, or do they embrace their supernatural identity?
- **Character Arc**: Outline the character's arc throughout the story, focusing on their personal growth and development. How do their experiences in the supernatural world change them as individuals? What lessons do they learn?
'''
        return base_prompt + urban_fantasy_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        urban_fantasy_additions = '''
## Urban Fantasy-Specific Chapter Writing
- **Setting the Scene**: Begin each chapter by establishing the setting and atmosphere, immersing the reader in the urban environment and hinting at the presence of the supernatural. Use vivid descriptions to bring the city to life and create a sense of mystery and intrigue.
- **Pacing and Suspense**: Maintain a fast pace that reflects the energy of the urban setting, while also building suspense and anticipation. Use cliffhangers and plot twists to keep the reader engaged and eager to find out what happens next.
- **Character Interactions**: Focus on the interactions between characters, both human and supernatural. Use dialogue and body language to reveal their personalities, motivations, and relationships.
- **Magic and Supernatural Elements**: Integrate magic and supernatural elements seamlessly into the narrative, ensuring that they are consistent with the established rules and limitations of the magic system. Avoid deus ex machina solutions and use magic in a way that is both believable and integral to the plot.
- **Worldbuilding Details**: Weave in worldbuilding details throughout the chapter, providing glimpses into the history, culture, and social dynamics of the supernatural world. Avoid info dumps and instead reveal information gradually through dialogue, action, and description.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show the reader what is happening, rather than simply telling them. This will help to create a more immersive and engaging reading experience.
- **Conflict and Tension**: Introduce conflict and tension into each chapter, whether it is a physical confrontation, a verbal argument, or an internal struggle. This will help to keep the reader invested in the story and create a sense of urgency.
- **Ending with a Hook**: End each chapter with a hook that leaves the reader wanting more. This could be a cliffhanger, a plot twist, or a lingering question that will be answered in the next chapter.
'''
        return base_prompt + urban_fantasy_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return UrbanFantasyPrompts.get_enhancement_prompt(**kwargs)