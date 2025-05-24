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

        # Extract context for cultural authenticity
        title = kwargs.get("title", "")
        description = kwargs.get("description", "")

        romance_additions = f"""

## 🚨 ROMANCE CHARACTER NAMING - CULTURAL AUTHENTICITY REQUIRED 🚨
**CRITICAL**: Create characters with authentic Indian/South Asian names that reflect the cultural setting.

### MANDATORY CHARACTER NAMING GUIDELINES
- **Indian Male Names**: Ayaan, Arjun, Rohan, Vikram, Aarav, Karan, Dev, Ravi, Aditya, Ishaan
- **Indian Female Names**: Priya, Ananya, Kavya, Meera, Ishita, Rhea, Aditi, Shreya, Diya, Naina
- **Family Names**: Sharma, Gupta, Patel, Singh, Agarwal, Joshi, Malhotra, Kapoor, Verma, Rao
- **NO WESTERN NAMES**: Do NOT use names like Amelia, Sarah, John, Michael, Emma, etc.
- **Cultural Context**: Names should reflect the story setting: "{title}" - {description}

### CHARACTER VERIFICATION CHECKLIST
✓ All character names are authentically Indian/South Asian
✓ Names match the cultural setting of the story
✓ No Western or non-Indian names have been used
✓ Characters reflect contemporary Indian society

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

        # Extract word count parameters for emphasis
        target_chapter_length = kwargs.get("target_chapter_length", "4,000-5,000")
        min_chapter_length = kwargs.get("min_chapter_length", 4000)

        # Extract character information for emphasis
        character_info = kwargs.get("character_info", "")

        romance_additions = f"""

## CRITICAL ROMANCE CHAPTER REQUIREMENTS - MANDATORY COMPLIANCE
- **MINIMUM WORD COUNT**: This chapter MUST be AT LEAST {min_chapter_length:,} words - NO EXCEPTIONS
- **ABSOLUTE MINIMUM**: This chapter MUST be AT LEAST {min_chapter_length:,} words - NO EXCEPTIONS
- **OPTIMAL TARGET**: Write {target_chapter_length} words for perfect Romance pacing
- **WORD COUNT PRIORITY**: Meeting word count is MORE IMPORTANT than rushing to plot points
- **SCENE REQUIREMENT**: Include 4-5 fully developed scenes (800-1,000 words each minimum)
- **EMOTIONAL EXPANSION**: Romance demands extensive emotional interiority - elaborate extensively
- **DIALOGUE DEPTH**: Include substantial dialogue with subtext and emotional layers
- **RELATIONSHIP FOCUS**: Dedicate 60%+ of word count to relationship development and emotional content

## 🚨 CHARACTER NAME COMPLIANCE - USE THESE EXACT NAMES 🚨
{character_info}
**CRITICAL**: Use ONLY the character names listed above. Do NOT create new names like "Amelia" or "Sarah".
The characters have been specifically created for this story - USE THEIR EXACT NAMES throughout the chapter.

## ROMANCE CHAPTER STRUCTURE REQUIREMENTS (to ensure adequate length)
1. **Opening Scene** (800-1,000 words): Establish mood, setting, character emotional state
2. **Development Scene** (1,000-1,200 words): Advance relationship or create tension
3. **Conflict/Tension Scene** (800-1,000 words): Introduce obstacles or deepen connection
4. **Emotional Climax Scene** (800-1,000 words): Peak emotional moment for the chapter
5. **Transition/Setup Scene** (600-800 words): Bridge to next chapter, leave reader wanting more

## MANDATORY WORD COUNT VERIFICATION
- Count your words as you write - aim for 4,500+ words minimum
- Each scene should be substantial and fully developed
- Do NOT summarize or rush through emotional moments
- Expand on internal thoughts, feelings, and sensory details
- Include rich descriptions of settings, characters, and emotions

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

## 🚨 FINAL ROMANCE CHAPTER CHECKLIST - MANDATORY VERIFICATION 🚨
Before completing this chapter, VERIFY you have:
✓ Written AT LEAST {min_chapter_length:,} words (COUNT EVERY WORD - this is critical!)
✓ Included 4-5 fully-developed scenes (each 800+ words minimum)
✓ Explored character emotions with extensive internal monologue
✓ Included substantial dialogue with emotional subtext
✓ Advanced romantic tension through detailed interactions
✓ Described settings, emotions, and physical reactions in rich detail
✓ Created natural pacing with NO rushed or summarized moments
✓ Dedicated majority of word count to relationship development

## CRITICAL WORD COUNT REMINDER
- If your chapter is under {min_chapter_length:,} words, it is INCOMPLETE
- Romance chapters MUST be substantial to satisfy readers
- Better to write 5,000 words than risk a short chapter
- Each emotional moment deserves full exploration
- Every dialogue exchange should include internal reactions
- Describe body language, facial expressions, and emotional responses in detail

FINAL CHECK: Count your words one more time before submitting. Romance readers expect and deserve substantial, emotionally rich chapters that fully develop the romantic relationship.

## 🚨 ULTRA-CRITICAL FINAL REQUIREMENTS 🚨
1. **WORD COUNT VERIFICATION**: Your chapter MUST be {min_chapter_length:,}+ words. Count them!
2. **CHARACTER NAME VERIFICATION**: Use ONLY the provided character names - no substitutions!
3. **SCENE COUNT VERIFICATION**: Include 4-5 substantial scenes (800+ words each)
4. **EMOTIONAL DEPTH VERIFICATION**: Every scene must have rich emotional content
5. **ROMANCE FOCUS VERIFICATION**: 60%+ of content must focus on romantic relationship

IF ANY OF THESE REQUIREMENTS ARE NOT MET, THE CHAPTER IS INCOMPLETE AND UNACCEPTABLE.
Romance readers deserve substantial, emotionally rich content with proper character consistency.
"""

        return base_prompt + romance_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a romance-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        romance_series_additions = """

## Romance Series-Specific Planning Elements

### Genre-Specific Series Development
- **Romance Conventions**: Ensure each book fulfills romance reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to romance
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to romance
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore romance themes with increasing depth and complexity

### Romance Series Continuity
- **Genre Elements**: Maintain consistent romance elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy romance readers
- **Series Identity**: Establish a strong series identity that feels authentically romance
- **World Building**: Develop the story world in ways that enhance the romance experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the romance genre

Create a romance series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + romance_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a romance-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        romance_book_additions = """

## Romance Series Book Integration

### Romance Continuity for This Book
- **Genre Consistency**: Maintain established romance elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to romance
- **Plot Advancement**: Continue series plot threads while telling a complete romance story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill romance reader expectations while advancing the series narrative

### Book-Specific Romance Focus
- **Central Conflict**: What romance-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new romance elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent romance while serving the series?

Ensure this book feels like an authentic continuation of the romance series while telling a complete, satisfying story.
"""

        return base_prompt + romance_book_additions

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

def get_series_plan_prompt(**kwargs) -> str:
    return RomancePrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return RomancePrompts.get_series_book_prompt(**kwargs)
