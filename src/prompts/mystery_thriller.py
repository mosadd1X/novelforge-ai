"""
Mystery Thriller genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class MysteryThrillerPrompts(FictionBasePrompts):
    GENRE_NAME = "Mystery Thriller"
    GENRE_DESCRIPTION = "Mystery Thrillers combine the suspenseful elements of a thriller with the intricate puzzle-solving of a mystery. They typically involve a crime or a series of crimes, often violent, that the protagonist must unravel while facing escalating danger and moral dilemmas. The focus is on both the 'who' and the 'why,' with a strong emphasis on psychological tension, red herrings, and unexpected twists."
    
    GENRE_CHARACTERISTICS = [
        "A compelling central mystery or crime that drives the plot forward.",
        "A protagonist, often flawed or with a troubled past, who is determined to solve the mystery.",
        "A high level of suspense and tension, created through pacing, foreshadowing, and cliffhangers.",
        "Red herrings and misleading clues designed to keep the reader guessing.",
        "A complex plot with multiple layers and interconnected subplots.",
        "A sense of danger and threat, with the protagonist often facing physical or psychological peril.",
        "Moral ambiguity and ethical dilemmas for the characters, blurring the lines between right and wrong.",
        "Psychological depth, exploring the motivations and inner conflicts of the characters.",
        "A fast-paced narrative that keeps the reader engaged and on the edge of their seat.",
        "A satisfying resolution that ties up loose ends and reveals the truth behind the mystery."
    ]
    
    TYPICAL_ELEMENTS = [
        "A dead body or a missing person that initiates the investigation.",
        "A detective, amateur sleuth, or law enforcement officer as the protagonist.",
        "A series of clues and leads that the protagonist must follow.",
        "Interviews with suspects and witnesses to gather information.",
        "A crime scene that provides vital evidence.",
        "Red herrings that lead the protagonist down false paths.",
        "A ticking clock or deadline that adds urgency to the investigation.",
        "A conspiracy or cover-up that complicates the case.",
        "A confrontation with the antagonist or killer.",
        "A plot twist that changes the course of the investigation.",
        "A final showdown where the truth is revealed.",
        "A sense of closure and justice at the end of the story."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        mystery_thriller_additions = '''
## Mystery Thriller-Specific Writing Considerations
- **Pacing and Suspense**: Master the art of pacing to build suspense gradually. Use short, impactful sentences and cliffhangers at the end of chapters to keep readers hooked. Vary sentence length and structure to control the rhythm of the narrative.
- **Red Herrings and Misdirection**: Strategically plant red herrings to mislead the reader and create doubt. Ensure these red herrings are plausible but ultimately lead to dead ends. Avoid making them too obvious or too obscure.
- **Character Motivation and Backstory**: Develop compelling character backstories that explain their motivations and actions. Explore their inner conflicts and moral dilemmas to add depth and complexity.
- **Plot Complexity and Twists**: Craft a multi-layered plot with unexpected twists and turns. Ensure that these twists are logical and well-integrated into the story, rather than feeling arbitrary or forced.
- **Foreshadowing and Clues**: Subtly foreshadow key events and provide clues that the reader can pick up on. These clues should be subtle enough to not give away the ending but clear enough to be satisfying when revealed.
- **Atmosphere and Setting**: Create a vivid and immersive atmosphere that enhances the suspense and tension. Use descriptive language to evoke a sense of unease, danger, or mystery.
- **Dialogue and Interrogation**: Write realistic and engaging dialogue, especially during interrogations. Use dialogue to reveal character traits, advance the plot, and create conflict.
- **Research and Accuracy**: Conduct thorough research to ensure the accuracy of your portrayal of law enforcement procedures, forensic science, and other relevant details. Inaccuracies can break the reader's immersion.
'''
        return base_prompt + mystery_thriller_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        mystery_thriller_additions = '''
## Mystery Thriller-Specific Outline Requirements
- **Inciting Incident**: Clearly define the inciting incident that sets the mystery in motion (e.g., a murder, a disappearance, a theft). This should occur early in the story.
- **Rising Action (Suspense Building)**: Outline the key events that escalate the tension and raise the stakes. Include specific scenes where the protagonist encounters obstacles, uncovers clues, and faces danger.
- **Midpoint Twist**: Plan a significant plot twist or revelation at the midpoint of the story that changes the direction of the investigation and raises new questions.
- **Red Herring Placement**: Strategically place red herrings throughout the outline to mislead the reader and create doubt. Note where each red herring will be introduced and how it will be debunked.
- **Climax (Confrontation)**: Outline the climactic confrontation between the protagonist and the antagonist. This should be a high-stakes scene where the truth is revealed and the conflict is resolved.
- **Resolution (Denouement)**: Plan the resolution of the mystery, including the explanation of the crime, the capture or defeat of the antagonist, and the aftermath for the protagonist.
- **Subplot Integration**: Integrate any subplots into the main plot in a way that enhances the suspense and complexity of the story. Ensure that subplots are relevant to the central mystery.
- **Character Arc Mapping**: Map out the character arc of the protagonist, including their initial state, their transformation throughout the story, and their final state after solving the mystery.
- **Timeline Construction**: Create a detailed timeline of events, including the crime, the investigation, and the key moments in the story. This will help ensure consistency and avoid plot holes.
- **Evidence Tracking**: Keep track of all the evidence, clues, and leads that are uncovered throughout the story. Note where each piece of evidence is introduced and how it contributes to the investigation.
'''
        return base_prompt + mystery_thriller_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        mystery_thriller_additions = '''
## Mystery Thriller-Specific Character Development
- **Protagonist's Flaws and Strengths**: Define the protagonist's flaws and weaknesses, as well as their strengths and skills. These should be relevant to the mystery and influence their actions and decisions.
- **Antagonist's Motivation**: Develop a compelling motivation for the antagonist's actions. Explore their backstory and psychological profile to understand why they committed the crime.
- **Supporting Characters' Roles**: Define the roles of supporting characters in the investigation. Consider how they contribute to the plot, provide clues, or act as red herrings.
- **Moral Ambiguity**: Explore the moral ambiguity of the characters, blurring the lines between right and wrong. Consider how their actions are influenced by their past experiences and personal values.
- **Psychological Depth**: Delve into the psychological depth of the characters, exploring their inner conflicts, fears, and desires. Use their thoughts and emotions to create suspense and tension.
- **Character Relationships**: Develop complex and believable relationships between the characters. Consider how their interactions influence the plot and reveal their true nature.
- **Detective's Methods**: If the protagonist is a detective, define their investigative methods and techniques. Consider how they approach the case, gather evidence, and interrogate suspects.
- **Victim's Backstory**: Provide a backstory for the victim, even if they are deceased. This can add emotional weight to the story and provide clues about the motive for the crime.
- **Suspect Profiles**: Create detailed profiles for each suspect, including their background, alibi, and potential motive. Use these profiles to create red herrings and mislead the reader.
- **Character Transformation**: Consider how the characters change and evolve throughout the story. The protagonist, in particular, should undergo a significant transformation as a result of the investigation.
'''
        return base_prompt + mystery_thriller_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        mystery_thriller_additions = '''
## Mystery Thriller-Specific Chapter Writing
- **Opening Hook**: Start each chapter with a compelling hook that grabs the reader's attention and creates suspense. This could be a shocking revelation, a dangerous situation, or a mysterious clue.
- **Pacing and Tension**: Control the pacing of each chapter to build tension gradually. Use short, impactful sentences and cliffhangers at the end of the chapter to keep readers hooked.
- **Clue Revelation**: Introduce new clues and leads in each chapter, but avoid revealing too much too soon. Stagger the information to keep the reader guessing and engaged.
- **Character Interaction**: Use character interactions to reveal their personalities, motivations, and relationships. Write realistic and engaging dialogue that advances the plot.
- **Setting Description**: Use vivid descriptions of the setting to create atmosphere and enhance the suspense. Focus on details that evoke a sense of unease, danger, or mystery.
- **Internal Monologue**: Use internal monologue to reveal the protagonist's thoughts, feelings, and doubts. This can help create empathy and build suspense as they grapple with the mystery.
- **Red Herring Placement**: Strategically place red herrings in each chapter to mislead the reader and create doubt. Ensure these red herrings are plausible but ultimately lead to dead ends.
- **Cliffhanger Endings**: End each chapter with a cliffhanger that leaves the reader wanting more. This could be a shocking revelation, a dangerous situation, or a mysterious clue.
- **Show, Don't Tell**: Use the "show, don't tell" technique to bring the story to life. Instead of simply stating facts, use descriptive language and action to reveal information.
- **Point of View Consistency**: Maintain a consistent point of view throughout each chapter. Avoid head-hopping or switching perspectives without a clear reason.
'''
        return base_prompt + mystery_thriller_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_enhancement_prompt(**kwargs)