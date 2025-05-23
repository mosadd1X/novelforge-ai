"""
Paranormal Romance genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ParanormalRomancePrompts(FictionBasePrompts):
    GENRE_NAME = "Paranormal Romance"
    GENRE_DESCRIPTION = "Paranormal Romance blends the emotional intensity and relationship focus of romance with elements of the supernatural, fantasy, or science fiction. It features a central love story between two characters, at least one of whom possesses paranormal abilities or belongs to a supernatural species. The paranormal elements are integral to the plot and often create unique challenges and opportunities for the relationship to develop. The genre emphasizes emotional connection, passion, and overcoming obstacles, often exploring themes of acceptance, identity, and the power of love to transcend boundaries."
    
    GENRE_CHARACTERISTICS = [
        "Supernatural or paranormal elements are central to the plot and character identities.",
        "A core romance plot drives the narrative, with a strong emphasis on emotional connection and relationship development.",
        "At least one protagonist possesses supernatural abilities, is a supernatural being (e.g., vampire, werewolf, witch), or has a connection to the paranormal world.",
        "The setting often blends the mundane world with a hidden or parallel supernatural realm.",
        "Conflict arises from the challenges of navigating a relationship between individuals from different worlds or with conflicting natures.",
        "Themes of acceptance, prejudice, and the struggle for identity are frequently explored.",
        "Sensuality and passion are common, often heightened by the supernatural elements.",
        "World-building is crucial, establishing the rules and lore of the paranormal elements.",
        "The narrative often includes elements of danger, suspense, and adventure related to the supernatural world.",
        "Character arcs often involve self-discovery and embracing one's true nature, both human and supernatural."
    ]
    
    TYPICAL_ELEMENTS = [
        "A forbidden love between a human and a supernatural being.",
        "A chosen one destined to save their paranormal community.",
        "A secret society of supernatural creatures living among humans.",
        "A curse that threatens the protagonist's relationship or existence.",
        "A prophecy that dictates the fate of the paranormal world.",
        "A power struggle within a supernatural hierarchy.",
        "A hunt for a powerful artifact or magical object.",
        "A transformation or awakening of supernatural abilities.",
        "A battle against a dark force that threatens both the human and paranormal worlds.",
        "A journey to a hidden or magical location.",
        "A love triangle involving a human and two supernatural beings.",
        "The discovery of a hidden heritage or family connection to the paranormal world."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Writing Considerations
- **Key Aspect 1: World-Building**: Craft a believable and immersive paranormal world with consistent rules, lore, and history. Consider the social structure, customs, and challenges faced by supernatural beings within this world.
- **Key Aspect 2: Character Motivation**: Ensure that both human and supernatural characters have compelling motivations that drive their actions and decisions, especially in relation to their romantic interest. Explore the internal conflicts arising from their different natures and desires.
- **Key Aspect 3: Balancing Romance and Paranormal Elements**: Seamlessly integrate the romance plot with the paranormal elements, ensuring that both aspects are equally compelling and contribute to the overall narrative. Avoid letting one overshadow the other.
- **Key Aspect 4: Sensuality and Intimacy**: Explore the sensuality and intimacy between characters in a way that is both passionate and respectful, considering the unique physical and emotional aspects of their supernatural natures.
- **Key Aspect 5: Conflict and Stakes**: Create high stakes and compelling conflicts that arise from the clash between the human and paranormal worlds, forcing characters to make difficult choices and confront their deepest fears.
- **Key Aspect 6: Emotional Resonance**: Focus on creating emotional resonance with readers by exploring universal themes of love, loss, acceptance, and identity through the lens of the paranormal.
- **Key Aspect 7: Originality**: Strive to create a unique and fresh take on familiar paranormal tropes, avoiding clichés and stereotypes. Develop original supernatural creatures, powers, and world-building elements.
- **Key Aspect 8: Character Growth**: Show how the characters grow and evolve throughout the story as they navigate the challenges of their relationship and embrace their true identities, both human and supernatural.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Outline Requirements
- **Structure Element 1: Introduction of the Paranormal World**: The outline should clearly establish the existence and rules of the paranormal world, introducing key supernatural elements and characters early on.
- **Structure Element 2: Initial Meeting and Attraction**: Detail the initial encounter between the protagonists, highlighting the spark of attraction and the potential challenges arising from their different backgrounds or natures.
- **Structure Element 3: Rising Action - Exploration of Powers and World**: Outline the events that lead to the exploration of the supernatural powers, world, and the deepening connection between the protagonists. Include specific scenes showcasing these elements.
- **Structure Element 4: Conflict and Obstacles**: Identify the major conflicts and obstacles that threaten the relationship, such as prejudice, external threats, or internal struggles related to their identities.
- **Structure Element 5: Climax - Confrontation and Choice**: Outline the climax of the story, where the protagonists face a major confrontation that forces them to make a difficult choice about their relationship and their future.
- **Structure Element 6: Resolution - Acceptance and Future**: Detail the resolution of the conflict, showing how the protagonists overcome the obstacles and find a way to be together, either by embracing their differences or finding a compromise.
- **Structure Element 7: World-Building Integration**: Ensure that the outline integrates the world-building elements throughout the story, using them to create tension, drive the plot, and enhance the emotional impact of the romance.
- **Structure Element 8: Character Arc Emphasis**: The outline should emphasize the character arcs of both protagonists, showing how they grow and evolve as they navigate the challenges of their relationship and embrace their true identities.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Character Development
- **Character Aspect 1: Supernatural Abilities and Limitations**: Clearly define the supernatural abilities of the paranormal character, as well as their limitations and weaknesses. Explore how these abilities impact their personality and relationships.
- **Character Aspect 2: Internal Conflict and Identity**: Explore the internal conflict of the paranormal character, particularly if they struggle with their identity or feel torn between two worlds. How does their supernatural nature affect their sense of self?
- **Character Aspect 3: Vulnerability and Emotional Depth**: Despite their supernatural powers, ensure that the paranormal character is vulnerable and possesses emotional depth. Show their fears, insecurities, and desires.
- **Character Aspect 4: Human Character's Reaction to the Paranormal**: Develop the human character's reaction to the paranormal world and the supernatural being they are falling in love with. Are they accepting, fearful, or curious? How does this relationship change them?
- **Character Aspect 5: Power Dynamics**: Consider the power dynamics between the human and paranormal characters. How does the supernatural character's power affect the relationship? How does the human character assert their own agency?
- **Character Aspect 6: Shared Goals and Values**: Despite their differences, identify shared goals and values that connect the human and paranormal characters. What do they both want out of life? What are they willing to fight for?
- **Character Aspect 7: Character Growth Through Relationship**: Show how both characters grow and evolve through their relationship. How do they learn from each other? How do they overcome their individual weaknesses?
- **Character Aspect 8: Backstory and Trauma**: Develop a compelling backstory for both characters, including any past traumas that may affect their present-day behavior and relationships.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        paranormal_romance_additions = '''
## Paranormal Romance-Specific Chapter Writing
- **Writing Technique 1: Sensory Details and Atmosphere**: Use vivid sensory details to create a compelling atmosphere that immerses the reader in the paranormal world. Describe the sights, sounds, smells, tastes, and textures of the supernatural realm.
- **Writing Technique 2: Show, Don't Tell with Powers**: Instead of simply stating that a character has a certain power, show them using it in a creative and engaging way. Describe the physical sensations and visual effects of their abilities.
- **Writing Technique 3: Dialogue and Banter**: Use dialogue to reveal character personalities, build romantic tension, and explore the differences between the human and paranormal worlds. Include witty banter and meaningful conversations.
- **Writing Technique 4: Pacing and Suspense**: Vary the pacing of the chapter to create suspense and keep the reader engaged. Use cliffhangers and foreshadowing to hint at future events.
- **Writing Technique 5: Emotional Intensity**: Focus on creating emotional intensity in key scenes, particularly those involving romantic interactions or moments of conflict. Use evocative language and imagery to convey the characters' feelings.
- **Writing Technique 6: Integration of Paranormal Elements**: Seamlessly integrate the paranormal elements into the chapter, ensuring that they are not just window dressing but an integral part of the plot and character development.
- **Writing Technique 7: Balancing Action and Romance**: Strike a balance between action-packed scenes and romantic moments, ensuring that both aspects are equally compelling and contribute to the overall narrative.
- **Writing Technique 8: Character Development Through Action**: Use action scenes to reveal character traits, test their abilities, and show how they react under pressure.
'''
        return base_prompt + paranormal_romance_additions

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_enhancement_prompt(**kwargs)

        paranormal_romance_additions = '''
## Paranormal Romance-Specific Enhancement Considerations
- **Enhancement Focus 1: World-Building Consistency**: Ensure that the enhanced text maintains consistency with the established rules and lore of the paranormal world. Check for any contradictions or inconsistencies in the world-building.
- **Enhancement Focus 2: Character Voice and Motivation**: Verify that the enhanced text accurately reflects the characters' voices and motivations, particularly in relation to their supernatural natures and romantic interests.
- **Enhancement Focus 3: Emotional Impact and Resonance**: Enhance the emotional impact of the text by adding more vivid sensory details, evocative language, and poignant moments of connection between the characters.
- **Enhancement Focus 4: Pacing and Suspense**: Improve the pacing of the text by adding more suspenseful elements, cliffhangers, and foreshadowing to keep the reader engaged.
- **Enhancement Focus 5: Dialogue and Banter**: Enhance the dialogue by adding more witty banter, meaningful conversations, and character-revealing exchanges between the protagonists.
- **Enhancement Focus 6: Supernatural Element Integration**: Ensure that the enhanced text seamlessly integrates the supernatural elements into the plot and character development, avoiding any jarring or unnatural transitions.
- **Enhancement Focus 7: Sensuality and Intimacy**: Enhance the sensuality and intimacy of the text by adding more descriptive details and emotional depth to the romantic interactions between the characters.
'''
        return base_prompt + paranormal_romance_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ParanormalRomancePrompts.get_enhancement_prompt(**kwargs)