"""
Romance genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class RomancePrompts(FictionBasePrompts):
    """Romance-specific prompts for novel generation."""
    
    GENRE_NAME = "Romance"
    GENRE_DESCRIPTION = "A genre focused on romantic relationships and emotional connections between characters"
    
    GENRE_CHARACTERISTICS = [
        "Central romantic relationship drives the plot",
        "Emotional character development and growth",
        "Tension and obstacles that test the relationship",
        "Strong emotional connection between protagonists",
        "Happy ending or hopeful resolution for the couple",
        "Internal conflicts and personal growth",
        "Chemistry and attraction between main characters",
        "Exploration of love, commitment, and relationships"
    ]
    
    TYPICAL_ELEMENTS = [
        "Meet-cute or compelling first encounter",
        "Initial attraction or conflict between protagonists",
        "Obstacles that keep the couple apart (internal/external)",
        "Moments of growing intimacy and connection",
        "Misunderstandings and relationship conflicts",
        "Personal growth and overcoming individual flaws",
        "Grand gesture or declaration of love",
        "Satisfying romantic resolution and commitment",
        "Secondary characters who support or complicate romance",
        "Emotional vulnerability and authentic feelings"
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        """Generate a romance-specific writer profile prompt."""
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        romance_additions = """

## Romance-Specific Writing Considerations
- **Emotional Authenticity**: Create genuine, relatable feelings and reactions
- **Character Chemistry**: Develop believable attraction and connection
- **Relationship Pacing**: Balance romantic development with plot progression
- **Conflict Creation**: Design obstacles that test but don't destroy the relationship
- **Intimacy Building**: Show emotional and physical connection appropriately
- **Character Growth**: Ensure both protagonists evolve through their relationship

## Romance Reader Expectations
- Satisfying romantic relationship that feels earned and authentic
- Characters who grow and change through their connection
- Emotional journey that resonates with real relationship experiences
- Appropriate level of intimacy for the target audience
- Happy ending or hopeful resolution for the romantic couple
- Believable obstacles that create tension without feeling contrived
"""
        
        return base_prompt + romance_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        """Generate a romance-specific outline prompt."""
        base_prompt = super().get_outline_prompt(**kwargs)
        
        romance_additions = """

## Romance-Specific Outline Requirements
- **Meet-Cute/First Encounter**: How the protagonists first meet or reconnect
- **Initial Attraction/Conflict**: What draws them together or creates tension
- **Relationship Development**: How their connection deepens over time
- **Major Obstacles**: Internal and external conflicts that test their bond
- **Character Growth**: How each protagonist changes through the relationship
- **Romantic Resolution**: How they overcome obstacles and commit to each other

## Romance Plot Structure Elements
- Compelling first meeting that establishes character dynamics
- Growing attraction despite initial obstacles or conflicts
- Deepening emotional connection through shared experiences
- Major conflict or misunderstanding that threatens the relationship
- Dark moment where the relationship seems doomed
- Character realizations and personal growth
- Grand gesture or honest communication that resolves conflicts
- Satisfying romantic resolution and commitment

## Romance Conflict Types to Consider
- **Internal Conflicts**: Fear of commitment, past trauma, self-worth issues
- **External Obstacles**: Career demands, family disapproval, distance
- **Misunderstandings**: Poor communication, assumptions, secrets
- **Competing Priorities**: Different life goals, timing issues
- **Past Relationships**: Ex-partners, trust issues, emotional baggage

## Relationship Development Milestones
- First meaningful conversation or connection
- Moment of vulnerability or emotional opening
- First physical contact or intimate moment
- Realization of deeper feelings
- First major conflict or disagreement
- Moment of potential loss or separation
- Declaration of love or commitment

Create a romance outline that provides emotional satisfaction and authentic relationship development.
"""
        
        return base_prompt + romance_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a romance-specific character development prompt."""
        base_prompt = super().get_character_prompt(**kwargs)
        
        romance_additions = """

## Romance Character Archetypes and Roles
- **The Romantic Leads**: Two protagonists whose relationship drives the story
- **The Best Friend**: Confidant who provides advice and support
- **The Ex**: Former partner who creates complications or comparison
- **The Rival**: Competing love interest who creates romantic tension
- **The Mentor**: Older character who provides relationship wisdom
- **The Family Member**: Relative who supports or opposes the relationship
- **The Matchmaker**: Character who tries to bring the couple together

## Romance Character Development Guidelines
- Create protagonists who are complete individuals before they meet
- Give each character personal goals beyond the romantic relationship
- Develop flaws and growth areas that the relationship helps address
- Show how each character brings out the best in the other
- Create believable reasons why these specific people fall in love
- Include past experiences that shape their approach to relationships

## Romantic Lead Development
For each protagonist, establish:
- **Personal Goals**: What they want in life beyond romance
- **Emotional Wounds**: Past hurts that affect their ability to love
- **Growth Arc**: How they need to change to be ready for love
- **Strengths**: What they bring to the relationship
- **Flaws**: Weaknesses that create realistic conflict
- **Love Language**: How they express and receive affection
- **Deal Breakers**: What would end the relationship for them

## Chemistry and Attraction Elements
- Physical attraction and what draws them to each other
- Intellectual compatibility and shared interests
- Emotional connection and understanding
- Complementary personalities that balance each other
- Shared values and life goals
- Unique quirks that endear them to each other
- Ways they challenge each other to grow

## Supporting Character Functions
- Provide relationship advice and perspective
- Create obstacles or complications for the romance
- Offer examples of successful or failed relationships
- Support character growth and development
- Add humor and lightness to romantic tension
- Represent different viewpoints on love and relationships

Create characters whose romantic journey feels authentic and emotionally satisfying.
"""
        
        return base_prompt + romance_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        """Generate a romance-specific chapter writing prompt."""
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        romance_additions = """

## Romance Writing Techniques
- **Emotional Interiority**: Show characters' internal thoughts and feelings
- **Tension Building**: Create anticipation through near-misses and obstacles
- **Dialogue Subtext**: Let characters say one thing while meaning another
- **Physical Awareness**: Show attraction through body language and reactions
- **Vulnerability Moments**: Include scenes where characters open up emotionally
- **Relationship Dynamics**: Show how the couple interacts and affects each other

## Romance Scene Types to Include
- **Conversation Scenes**: Deep talks that reveal character and build connection
- **Activity Scenes**: Shared experiences that bring characters together
- **Conflict Scenes**: Disagreements that test and strengthen the relationship
- **Intimate Moments**: Emotional or physical closeness appropriate to the story
- **Separation Scenes**: Times apart that highlight the characters' feelings
- **Realization Scenes**: Moments when characters understand their true feelings

## Emotional Development Guidelines
- Show gradual deepening of feelings rather than instant love
- Include moments of doubt and uncertainty about the relationship
- Demonstrate how each character changes through their connection
- Balance romantic scenes with individual character development
- Show both the joy and challenges of falling in love
- Include realistic relationship milestones and progression

## Romance Dialogue Considerations
- Characters should have distinct voices and speaking patterns
- Include both verbal and non-verbal communication
- Show growing comfort and intimacy through conversation style
- Use dialogue to reveal character backstory and motivation
- Include moments of humor and playfulness between characters
- Balance romantic declarations with everyday conversation

## Physical and Emotional Intimacy
- Build physical awareness and attraction gradually
- Show emotional intimacy through vulnerability and trust
- Include appropriate physical contact for your target audience
- Balance romantic tension with emotional connection
- Show how intimacy deepens the characters' bond
- Respect character boundaries and relationship pacing

Write with attention to emotional authenticity and relationship development that feels genuine and satisfying.
"""
        
        return base_prompt + romance_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return RomancePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return RomancePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return RomancePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return RomancePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return RomancePrompts.get_enhancement_prompt(**kwargs)
