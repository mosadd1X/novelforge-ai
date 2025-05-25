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

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        fantasy_series_additions = """

## Fantasy Series-Specific Planning Elements

### World-Building Across the Series
- **Expanding Magic System**: Reveal deeper layers of magic and its consequences across books
- **Geographic Exploration**: Gradually explore different regions, realms, or dimensions
- **Historical Depth**: Uncover ancient events, prophecies, and their modern implications
- **Cultural Evolution**: Show how societies change in response to series events
- **Magical Consequences**: Explore long-term effects of magical events from previous books

### Character Development Across Fantasy Series
- **Power Progression**: Show characters growing in magical ability and wisdom
- **Relationship Dynamics**: Develop complex relationships between different fantasy races/cultures
- **Moral Complexity**: Explore how power and responsibility affect character choices
- **Legacy Characters**: Introduce descendants, students, or inheritors of previous characters
- **Cross-Book Character Arcs**: Plan character development that spans multiple books

### Fantasy Series Plot Threads
- **Ancient Prophecies**: Multi-book prophecies that unfold gradually
- **Magical Artifacts**: Powerful items whose significance grows across the series
- **Rising Dark Forces**: Escalating supernatural threats that build across books
- **Political Intrigue**: Complex political situations that develop over time
- **World-Changing Events**: Major magical events that reshape the world

### Fantasy Series Themes
- **Power and Responsibility**: How characters handle increasing magical power
- **Good vs. Evil**: Evolving understanding of morality and conflict
- **Sacrifice and Heroism**: What characters are willing to give up for others
- **Unity vs. Division**: How different peoples come together or fall apart
- **Tradition vs. Change**: Balancing ancient ways with necessary evolution

Create a fantasy series that builds an epic, immersive world with compelling character arcs and escalating magical conflicts.
"""

        return base_prompt + fantasy_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        fantasy_book_additions = """

## Fantasy Series Book Integration

### World Continuity for This Book
- **Magic System Consistency**: Maintain established magical rules while potentially revealing new aspects
- **Geographic Accuracy**: Use established locations correctly and introduce new areas logically
- **Cultural Continuity**: Keep established societies consistent while showing natural evolution
- **Timeline Accuracy**: Maintain proper chronology and show realistic passage of time
- **Character Knowledge**: Respect what characters have learned and experienced

### Fantasy-Specific Book Elements
- **Magical Progression**: Show how characters' magical abilities have developed since previous books
- **New Magical Elements**: Introduce new spells, creatures, or magical phenomena that fit the established world
- **Political Developments**: Continue political storylines and show consequences of previous events
- **Relationship Evolution**: Develop relationships between characters, especially across different fantasy races
- **World Impact**: Show how events from previous books have affected the broader world

### Book-Specific Fantasy Focus
- **Central Magical Conflict**: What magical threat or mystery drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Discoveries**: What new aspects of the world, magic, or history will be revealed?
- **Escalating Stakes**: How do the stakes increase from previous books while remaining believable?
- **Series Advancement**: How does this book move the overall series arc forward significantly?

Ensure this book feels like an authentic continuation of the fantasy world while telling a complete, satisfying story.
"""

        return base_prompt + fantasy_book_additions

    @classmethod
    def get_back_cover_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific back cover description prompt."""
        title = kwargs.get("title", "Unknown Title")
        author = kwargs.get("author", "Unknown Author")
        chapter_summary = kwargs.get("chapter_summary", "")

        return f"""
You are a professional fantasy book marketing copywriter specializing in epic back cover descriptions.

Generate an immersive back cover description for "{title}" by {author}.

FANTASY-SPECIFIC GUIDELINES:
- EPIC SCOPE: Emphasize the grand scale and world-changing stakes
- MAGICAL ELEMENTS: Highlight unique magic systems, creatures, and fantastical elements
- HEROIC JOURNEY: Focus on the protagonist's transformation and destiny
- WORLD-BUILDING: Showcase the rich, immersive fantasy world
- ADVENTURE PROMISE: Create excitement for epic quests and discoveries
- GOOD VS EVIL: Emphasize the moral stakes and battle between light and darkness

FANTASY LANGUAGE STYLE:
- Epic and grandiose without being overwrought
- Rich, descriptive language that paints vivid imagery
- Mythic and legendary tone
- Emphasis on wonder, magic, and adventure
- Heroic and inspiring language

KEY FANTASY ELEMENTS TO EMPHASIZE:
- Unique magical systems and supernatural powers
- Mythical creatures and fantastical beings
- Epic quests and world-threatening dangers
- Ancient prophecies and mystical artifacts
- Hero's journey and character transformation
- Rich world-building and immersive settings

STORY CONTEXT:
{chapter_summary}

FANTASY HOOKS:
- "In a world where magic comes at a price..."
- "Ancient powers stir, and only one can stop them..."
- "Destiny calls, but will they answer?"
- "When darkness threatens everything, heroes must rise..."
- "Magic is returning, and the world will never be the same..."

FORMAT: Write 400-600 words that transport fantasy readers into an epic adventure.
Focus on wonder, heroism, and the promise of an unforgettable magical journey.
"""

    @classmethod
    def get_short_description_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific short description prompt for recommendations."""
        title = kwargs.get("title", "Unknown Title")

        return f"""
Create an epic 2-3 line description for "{title}" perfect for fantasy book recommendations.

FANTASY SHORT DESCRIPTION REQUIREMENTS:
- 150-200 characters maximum
- Immediately establish the magical premise
- Create sense of wonder and adventure
- Hint at epic scope and stakes
- End with compelling hook about destiny or danger

FANTASY FOCUS:
- Magical elements and fantasy world
- Epic adventure and heroic journey
- World-threatening stakes
- Character's destiny and transformation

EXAMPLE FANTASY HOOKS:
- "When ancient magic awakens, only one can save the realm..."
- "Destiny chose her. Magic will test her. Evil will challenge her..."
- "In a world of dragons and magic, heroes are forged in fire..."
- "The prophecy is clear: save the world or watch it burn..."

Write a short description that makes fantasy readers eager to embark on this epic adventure.
"""

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs) -> str:
        """Generate a fantasy-specific marketing tagline prompt."""

        return f"""
Create an epic, memorable marketing tagline for this fantasy novel.

FANTASY TAGLINE REQUIREMENTS:
- 5-10 words maximum
- Epic and inspiring tone
- Captures the magical adventure
- Creates sense of wonder and excitement
- Perfect for fantasy marketing

FANTASY TAGLINE STYLES:
- "Magic awakens. Destiny calls."
- "Heroes rise. Legends are born."
- "When darkness falls, light must rise."
- "One quest. Infinite possibilities."
- "Magic has a price. Heroes pay it."
- "Destiny cannot be denied."
- "Adventure beyond imagination."

Focus on themes of heroism, magic, destiny, and epic adventure that resonate with fantasy readers.
"""

    @classmethod
    def get_visual_style_preferences(cls, **kwargs) -> str:
        """Get visual style preferences for fantasy back covers."""

        return """
FANTASY VISUAL STYLE PREFERENCES:

COLOR SCHEMES:
- Rich, mystical colors (deep purples, midnight blues, emerald greens)
- Metallic accents (gold, silver, bronze) for magical elements
- Dramatic contrasts (dark backgrounds with bright magical effects)
- Earth tones for grounded fantasy (browns, forest greens, stone grays)

TYPOGRAPHY:
- Bold, epic fonts for titles (medieval or mystical styles)
- Ornate decorative elements and borders
- Readable but atmospheric font choices
- Emphasis on magical or heroic words

IMAGERY SUGGESTIONS:
- Epic fantasy landscapes (castles, mountains, magical forests)
- Mythical creatures (dragons, phoenixes, magical beasts)
- Magical elements (glowing runes, spell effects, enchanted objects)
- Heroic figures in dramatic poses
- Ancient symbols and mystical artifacts

LAYOUT PREFERENCES:
- Grand, epic composition with sweeping elements
- Layered imagery suggesting depth and mystery
- Magical effects and atmospheric lighting
- Focus on adventure and wonder
- Professional but fantastical design

MOOD:
- Epic and adventurous
- Mysterious and magical
- Heroic and inspiring
- Sense of wonder and discovery
- Appeals to fantasy readers' imagination
"""

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

def get_series_plan_prompt(**kwargs) -> str:
    return FantasyPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return FantasyPrompts.get_series_book_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return FantasyPrompts.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return FantasyPrompts.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return FantasyPrompts.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return FantasyPrompts.get_visual_style_preferences(**kwargs)
