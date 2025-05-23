"""
Fantasy genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class FantasyPrompts(FictionBasePrompts):
    """Fantasy-specific prompts for novel generation."""
    
    GENRE_NAME = "Fantasy"
    GENRE_DESCRIPTION = "A genre featuring magical elements, mythical creatures, and imaginary worlds"
    
    GENRE_CHARACTERISTICS = [
        "Rich world-building with detailed magical systems",
        "Mythical creatures and fantastical beings",
        "Magic as a central element of the story",
        "Epic quests and heroic journeys",
        "Complex political systems and ancient histories",
        "Moral conflicts between good and evil",
        "Coming-of-age themes and personal growth",
        "Detailed descriptions of magical phenomena"
    ]
    
    TYPICAL_ELEMENTS = [
        "Magic systems with clear rules and limitations",
        "Fantastical creatures (dragons, elves, dwarves, etc.)",
        "Imaginary worlds with unique geography and cultures",
        "Ancient prophecies and mystical artifacts",
        "Epic battles between forces of good and evil",
        "Magical abilities and supernatural powers",
        "Medieval or pre-industrial settings",
        "Quests for powerful objects or knowledge",
        "Political intrigue in magical kingdoms",
        "Themes of destiny, sacrifice, and heroism"
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific writer profile prompt."""
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        fantasy_additions = """

## Fantasy-Specific Writing Considerations
- **World-Building Depth**: Create immersive magical worlds with consistent internal logic
- **Magic System Design**: Develop clear rules for how magic works, its costs, and limitations
- **Cultural Development**: Build diverse societies with unique customs, languages, and beliefs
- **Mythological Integration**: Weave folklore and mythology naturally into the narrative
- **Character Archetypes**: Utilize and subvert classic fantasy archetypes (heroes, wizards, rogues)
- **Epic Scope**: Balance intimate character moments with grand, world-changing events

## Fantasy Reader Expectations
- Rich, detailed world-building that feels lived-in and authentic
- Magic that follows consistent rules and has meaningful consequences
- Characters who grow through trials and discover their true potential
- Epic conflicts with high stakes and meaningful resolutions
- Immersive descriptions that transport readers to another world
"""
        
        return base_prompt + fantasy_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific outline prompt."""
        base_prompt = super().get_outline_prompt(**kwargs)
        
        fantasy_additions = """

## Fantasy-Specific Outline Requirements
- **World-Building Foundation**: Establish the magical world's rules, geography, and cultures
- **Magic System Integration**: Show how magic affects plot, character development, and conflict
- **Character Journey**: Include a clear hero's journey or character transformation arc
- **Escalating Conflicts**: Build from personal stakes to world-threatening consequences
- **Magical Elements**: Incorporate fantastical creatures, artifacts, and supernatural events
- **Cultural Depth**: Show different societies, their conflicts, and interactions

## Fantasy Plot Structure Elements
- Inciting incident that reveals the magical world or threat
- Discovery of magical abilities or ancient knowledge
- Gathering of allies and formation of fellowship/party
- Series of trials that test characters' growth and abilities
- Major setback that forces characters to dig deeper
- Final confrontation with ultimate evil or challenge
- Resolution that shows how the world has changed

Ensure the outline creates a compelling fantasy adventure with rich world-building and character development.
"""
        
        return base_prompt + fantasy_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific character development prompt."""
        base_prompt = super().get_character_prompt(**kwargs)
        
        fantasy_additions = """

## Fantasy Character Archetypes and Roles
- **The Hero/Chosen One**: Reluctant protagonist with hidden potential
- **The Mentor**: Wise guide with magical knowledge or experience
- **The Warrior**: Skilled fighter with personal code of honor
- **The Mage/Wizard**: Magic user with deep understanding of mystical forces
- **The Rogue/Thief**: Cunning character with street smarts and agility
- **The Noble**: Character from royal or aristocratic background
- **The Outsider**: Character from different culture or species

## Fantasy Character Development Guidelines
- Give each character a unique relationship with magic (user, resistant, affected by)
- Develop personal stakes that connect to larger world-threatening conflicts
- Create character flaws that must be overcome through magical trials
- Design character abilities that complement the group dynamic
- Include characters from different fantasy races/species if appropriate
- Show how characters' backgrounds shape their worldview and decisions

## Magical Abilities and Powers
Consider giving characters:
- Elemental magic (fire, water, earth, air)
- Divine or clerical powers
- Nature-based abilities
- Mental/psychic powers
- Weapon enchantment or combat magic
- Healing or protective abilities
- Unique magical talents tied to their background

Create characters that feel authentic to the fantasy genre while avoiding tired clichés.
"""
        
        return base_prompt + fantasy_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific chapter writing prompt."""
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        fantasy_additions = """

## Fantasy Writing Techniques
- **Immersive Descriptions**: Paint vivid pictures of magical landscapes, creatures, and phenomena
- **Magic Integration**: Show magic as natural part of the world, not just special effects
- **Cultural Details**: Include customs, languages, and social structures of fantasy societies
- **Sensory Magic**: Describe how magic looks, feels, sounds, and affects the environment
- **World Consistency**: Maintain established rules for magic, geography, and cultures
- **Epic Scope**: Balance intimate character moments with grand, fantastical elements

## Fantasy Dialogue Considerations
- Use language that fits the world's time period and culture
- Include fantasy terminology naturally without over-explaining
- Show character relationships through speech patterns and formality levels
- Incorporate magical concepts into everyday conversation
- Avoid modern slang unless it fits the established world

## Atmospheric Elements for Fantasy
- Describe magical phenomena with wonder and detail
- Create tension through supernatural threats and mysteries
- Use weather, lighting, and environment to enhance mood
- Include sounds, smells, and textures unique to the fantasy world
- Show the impact of magic on daily life and society

Write with rich, immersive prose that transports readers into a believable magical world.
"""
        
        return base_prompt + fantasy_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return FantasyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return FantasyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return FantasyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return FantasyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return FantasyPrompts.get_enhancement_prompt(**kwargs)
