"""
Epic Fantasy genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class EpicFantasyPrompts(FictionBasePrompts):
    GENRE_NAME = "Epic Fantasy"
    GENRE_DESCRIPTION = "Epic Fantasy is a subgenre of fantasy characterized by its grand scope, intricate world-building, and focus on a heroic quest or struggle against overwhelming evil. Stories often involve multiple characters, complex political landscapes, and magical systems that are deeply integrated into the world's history and culture. Themes of good versus evil, destiny, sacrifice, and the corrupting influence of power are prevalent."
    
    GENRE_CHARACTERISTICS = [
        "Extensive World-Building: A meticulously crafted world with its own history, geography, cultures, languages, and mythologies.",
        "Grand Scope and Scale: Stories that span vast distances, involve large casts of characters, and address conflicts that affect entire nations or the world itself.",
        "Heroic Quest or Struggle: A central narrative driven by a hero's journey or a group's fight against a powerful, often supernatural, antagonist.",
        "Complex Magic Systems: Well-defined and internally consistent magic systems that play a significant role in the plot and world-building.",
        "Moral Ambiguity: While often featuring a clear conflict between good and evil, characters and situations often present moral complexities and shades of gray.",
        "Prophecies and Destinies: The presence of prophecies, ancient lore, and predetermined destinies that influence the characters' actions and the course of events.",
        "Mythic and Legendary Elements: Incorporation of elements from mythology, folklore, and legends, often drawing inspiration from various cultures.",
        "High Stakes and World-Altering Consequences: The outcome of the central conflict has significant and lasting repercussions for the world and its inhabitants.",
        "Exploration of Power and Corruption: Examination of the nature of power, its potential for corruption, and the responsibilities that come with it.",
        "Detailed Political Intrigue: Complex political systems, power struggles, and alliances that shape the narrative and influence character motivations."
    ]
    
    TYPICAL_ELEMENTS = [
        "Ancient Artifacts: Powerful objects with historical significance and magical properties.",
        "Magical Creatures: Dragons, elves, dwarves, or other fantastical beings that inhabit the world.",
        "Lost Civilizations: Ruins and remnants of advanced societies with forgotten knowledge and technologies.",
        "Prophecies and Oracles: Characters who can foresee the future or interpret signs and omens.",
        "Chosen One: A character destined to fulfill a specific role or save the world.",
        "Mentors and Guides: Wise figures who provide guidance and training to the protagonist.",
        "Dark Lords and Evil Empires: Antagonistic forces seeking to dominate or destroy the world.",
        "Epic Battles: Large-scale conflicts between armies or factions with significant consequences.",
        "Political Intrigue: Complex schemes and power plays among rulers and nobles.",
        "Magical Schools and Orders: Institutions dedicated to the study and practice of magic.",
        "Journeys and Quests: Long and perilous voyages to achieve a specific goal.",
        "Sacrifice and Redemption: Characters who make significant sacrifices for the greater good or seek redemption for past actions."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Writing Considerations
- **World-Building Depth**: Focus on creating a believable and immersive world with consistent rules, history, and cultures. Consider the impact of magic on society, economy, and politics.
- **Character Complexity**: Develop characters with nuanced motivations, flaws, and strengths. Explore their moral dilemmas and how they evolve throughout the story.
- **Magic System Consistency**: Design a magic system with clear rules and limitations. Avoid deus ex machina solutions and ensure that magic has consequences.
- **Scope and Pacing**: Balance the grand scope of the story with a compelling narrative pace. Avoid excessive exposition and maintain reader engagement.
- **Political Intrigue**: Craft believable political systems and power struggles. Consider the motivations of different factions and the consequences of their actions.
- **Mythic Resonance**: Incorporate elements of mythology and folklore to add depth and resonance to the story. Draw inspiration from various cultures and traditions.
- **Theme Exploration**: Explore universal themes such as good versus evil, destiny, sacrifice, and the corrupting influence of power.
- **Language and Tone**: Use evocative language and a formal tone to create a sense of grandeur and importance. Consider the dialects and accents of different cultures within the world.
'''
        return base_prompt + epic_fantasy_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Outline Requirements
- **World Introduction**: Dedicate the initial chapters to introducing the world, its key locations, cultures, and history. Establish the setting as a character in itself.
- **Character Arcs**: Plan out the major character arcs for each significant character, including their motivations, challenges, and transformations.
- **Plot Threads**: Outline the various plot threads and subplots, ensuring they intertwine and contribute to the overall narrative.
- **Magic System Integration**: Show how the magic system influences the plot and character actions. Plan key moments where magic is used and its consequences.
- **Political Developments**: Map out the political landscape and how it evolves throughout the story. Include key political events and their impact on the characters.
- **Rising Action and Climax**: Structure the rising action to build tension and anticipation, leading to a climactic confrontation that resolves the central conflict.
- **Resolution and Aftermath**: Plan for a resolution that addresses the major plot threads and explores the long-term consequences of the events.
- **Thematic Resonance**: Ensure that the outline reflects the core themes of the story and reinforces the overall message.
'''
        return base_prompt + epic_fantasy_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Character Development
- **Heroic Archetypes**: Consider classic heroic archetypes (e.g., the reluctant hero, the chosen one) and how they can be adapted to create unique and compelling characters.
- **Moral Complexity**: Give characters flaws, doubts, and internal conflicts. Explore their moral compass and how it is tested throughout the story.
- **Backstory and Motivation**: Develop detailed backstories that explain the characters' motivations, fears, and desires.
- **Relationships and Alliances**: Create complex relationships between characters, including alliances, rivalries, and romances.
- **Magical Abilities**: If a character possesses magical abilities, define the extent and limitations of their powers.
- **Growth and Transformation**: Plan how the characters will grow and change throughout the story, learning from their experiences and overcoming their weaknesses.
- **Cultural Influences**: Consider how the characters' cultures and backgrounds shape their beliefs, values, and behaviors.
- **Impact on the World**: Think about how the characters' actions and decisions will impact the world around them.
'''
        return base_prompt + epic_fantasy_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        epic_fantasy_additions = '''
## Epic Fantasy-Specific Chapter Writing
- **World-Building Integration**: Weave world-building details seamlessly into the narrative, avoiding info dumps. Show, don't tell, the reader about the world.
- **Character Development**: Use each chapter to further develop the characters, revealing their thoughts, feelings, and motivations.
- **Plot Progression**: Advance the plot in each chapter, either by introducing new conflicts, resolving old ones, or revealing important information.
- **Descriptive Language**: Use vivid and evocative language to create a sense of atmosphere and immersion.
- **Pacing and Tension**: Vary the pacing of the chapters to create a sense of tension and anticipation.
- **Dialogue and Interaction**: Write realistic and engaging dialogue that reveals character and advances the plot.
- **Thematic Resonance**: Ensure that each chapter contributes to the overall themes of the story.
- **Cliffhangers and Hooks**: End chapters with cliffhangers or hooks to keep the reader engaged and eager to continue reading.
'''
        return base_prompt + epic_fantasy_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return EpicFantasyPrompts.get_enhancement_prompt(**kwargs)