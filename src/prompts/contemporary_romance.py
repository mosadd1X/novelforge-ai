"""
Contemporary Romance genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ContemporaryRomancePrompts(FictionBasePrompts):
    """Contemporary Romance-specific prompts for novel generation."""

    GENRE_NAME = "Contemporary Romance"
    GENRE_DESCRIPTION = "Contemporary Romance combines the emotional intensity of romance with modern, realistic settings and current social issues. It features relatable characters navigating love in today's world, often incorporating cultural authenticity, career challenges, family dynamics, and contemporary relationship issues."

    GENRE_CHARACTERISTICS = [
        "Modern, realistic settings and contemporary issues",
        "Central romantic relationship with emotional depth",
        "Cultural authenticity and diverse perspectives",
        "Career-focused characters balancing work and love",
        "Family dynamics and generational expectations",
        "Contemporary social issues affecting relationships",
        "Realistic dialogue reflecting modern communication",
        "Technology's impact on modern relationships",
        "Personal growth through romantic connection",
        "Happy ending with authentic relationship resolution"
    ]

    TYPICAL_ELEMENTS = [
        "Meet-cute in contemporary settings (workplace, social media, etc.)",
        "Modern relationship obstacles (career demands, distance, family)",
        "Cultural identity and heritage exploration",
        "Technology-mediated communication and misunderstandings",
        "Contemporary social issues affecting the relationship",
        "Career ambitions vs. romantic priorities",
        "Family expectations and cultural traditions",
        "Modern dating challenges and relationship dynamics",
        "Personal growth through love and partnership",
        "Realistic resolution honoring both love and individual goals"
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        """Generate a contemporary romance-specific writer profile prompt."""
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        contemporary_romance_additions = """

## Contemporary Romance Writer Profile Requirements
- **Modern Authenticity**: Expertise in contemporary relationship dynamics and current social issues
- **Cultural Sensitivity**: Ability to authentically portray diverse cultural backgrounds and experiences
- **Career Integration**: Skill in weaving professional ambitions into romantic narratives
- **Family Dynamics**: Understanding of modern family structures and generational differences
- **Technology Awareness**: Knowledge of how technology affects modern relationships and communication
- **Social Issues**: Awareness of contemporary challenges affecting relationships (mental health, social media, etc.)

## Contemporary Romance Reader Expectations
- Relatable characters facing modern relationship challenges
- Authentic portrayal of contemporary life and culture
- Emotional depth combined with realistic relationship progression
- Happy ending that feels earned and sustainable in modern context
- Representation of diverse backgrounds and experiences
- Balance between romantic fantasy and realistic relationship dynamics
"""

        return base_prompt + contemporary_romance_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        """Generate a contemporary romance-specific outline prompt."""
        base_prompt = super().get_outline_prompt(**kwargs)

        contemporary_romance_additions = """

## Contemporary Romance-Specific Outline Requirements
- **Modern Meet-Cute**: How protagonists meet in contemporary settings (workplace, apps, social events)
- **Contemporary Obstacles**: Modern challenges like career demands, social media, family expectations
- **Cultural Context**: How cultural background influences relationship development and conflicts
- **Career Integration**: How professional lives impact and intersect with romantic development
- **Family Dynamics**: Role of modern family structures and generational differences
- **Technology Role**: How digital communication affects relationship progression
- **Social Issues**: Contemporary challenges that test the relationship
- **Personal Growth**: How each character evolves through modern relationship challenges
- **Realistic Resolution**: Ending that honors both romantic satisfaction and contemporary realities

## Contemporary Romance Conflict Types
- **Career vs. Love**: Professional ambitions conflicting with relationship priorities
- **Cultural Expectations**: Traditional family values vs. modern relationship choices
- **Digital Miscommunication**: Social media misunderstandings and technology barriers
- **Geographic Challenges**: Modern mobility and long-distance relationship issues
- **Social Pressures**: Contemporary social expectations and peer influences
- **Mental Health**: Modern awareness of psychological well-being in relationships
- **Financial Stress**: Economic pressures affecting relationship stability
- **Time Management**: Busy modern lifestyles impacting relationship development

## Modern Relationship Milestones
- First digital interaction (text, social media, dating app)
- Transition from online to in-person communication
- Meeting friends and family in contemporary contexts
- Navigating social media relationship status
- Balancing career demands with relationship time
- Addressing cultural differences and family expectations
- Overcoming modern communication challenges
- Commitment in the context of contemporary relationship norms

Create a contemporary romance outline that reflects authentic modern relationship dynamics while delivering emotional satisfaction.
"""

        return base_prompt + contemporary_romance_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a contemporary romance-specific character development prompt."""
        base_prompt = super().get_character_prompt(**kwargs)

        # Extract context for cultural authenticity
        title = kwargs.get("title", "")
        description = kwargs.get("description", "")

        contemporary_romance_additions = f"""

## 🚨 CONTEMPORARY ROMANCE CHARACTER NAMING - CULTURAL AUTHENTICITY REQUIRED 🚨
**CRITICAL**: Create characters with authentic names that reflect the contemporary cultural setting.

### MANDATORY CHARACTER NAMING GUIDELINES FOR CONTEMPORARY ROMANCE
- **Indian/South Asian Names**: Ayaan, Arjun, Rohan, Vikram, Aarav, Karan, Dev, Ravi, Aditya, Ishaan
- **Indian Female Names**: Priya, Ananya, Kavya, Meera, Ishita, Rhea, Aditi, Shreya, Diya, Naina
- **Family Names**: Sharma, Gupta, Patel, Singh, Agarwal, Joshi, Malhotra, Kapoor, Verma, Rao
- **Cultural Context**: Names should reflect the story setting: "{title}" - {description}
- **NO WESTERN NAMES**: Do NOT use names like Amelia, Sarah, John, Michael, Emma, etc.
- **Contemporary Relevance**: Names should suit modern, professional characters

### CHARACTER VERIFICATION CHECKLIST
✓ All character names are culturally appropriate for the setting
✓ Names reflect contemporary, educated professionals
✓ No Western or inappropriate names have been used
✓ Characters embody modern relationship dynamics

## Contemporary Romance Character Archetypes
- **The Career-Driven Professional**: Ambitious individual balancing success with love
- **The Cultural Bridge-Builder**: Character navigating traditional and modern values
- **The Digital Native**: Tech-savvy character comfortable with modern communication
- **The Family-Oriented Modern**: Balancing family expectations with personal desires
- **The Independent Spirit**: Self-sufficient character learning to compromise for love
- **The Wounded Professional**: Career success masking emotional vulnerability
- **The Cultural Traditionalist**: Honoring heritage while embracing modern love
- **The Social Media Influencer**: Navigating public vs. private relationship dynamics

## Contemporary Romance Character Development
- **Modern Professions**: Realistic careers that create interesting dynamics (tech, healthcare, media, etc.)
- **Cultural Authenticity**: Characters should authentically represent their cultural background
- **Technology Integration**: Comfortable with modern communication and social media
- **Family Dynamics**: Complex relationships with modern family structures
- **Personal Growth**: Characters evolving through contemporary relationship challenges
- **Social Awareness**: Understanding of current social issues and their impact on relationships
- **Financial Independence**: Characters with their own economic agency and goals
- **Mental Health Awareness**: Modern understanding of psychological well-being

## Contemporary Romance Relationship Dynamics
- **Equal Partnership**: Both characters contributing equally to relationship development
- **Career Integration**: Professional lives enhancing rather than competing with romance
- **Cultural Celebration**: Heritage and traditions enriching the relationship
- **Modern Communication**: Healthy use of technology and digital platforms
- **Family Inclusion**: Navigating family relationships in contemporary contexts
- **Social Circle Integration**: Friends and community supporting the relationship
- **Conflict Resolution**: Modern approaches to addressing relationship challenges
- **Future Planning**: Realistic discussions about life goals and compatibility

### 🚨 FINAL CHARACTER VERIFICATION FOR CONTEMPORARY ROMANCE 🚨
Before submitting characters, verify:
✓ All names are culturally authentic and contemporary
✓ Characters reflect modern professionals with realistic careers
✓ No Western names have been used inappropriately
✓ Characters are suitable for contemporary romance development
✓ Cultural background is authentically represented
✓ Characters embody modern relationship values and communication styles

Create characters whose contemporary romance journey feels authentic to modern readers while honoring cultural heritage and contemporary relationship dynamics.
"""

        return base_prompt + contemporary_romance_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        """Generate a contemporary romance-specific chapter prompt."""
        base_prompt = super().get_chapter_prompt(**kwargs)

        # Extract parameters for aggressive word count requirements
        min_chapter_length = kwargs.get("min_chapter_length", 4000)
        target_chapter_length = kwargs.get("target_chapter_length", "4,500-6,000")
        character_info = kwargs.get("character_info", "")

        contemporary_romance_additions = f"""

## 🚨 CRITICAL CONTEMPORARY ROMANCE CHAPTER REQUIREMENTS - MANDATORY COMPLIANCE 🚨
- **MINIMUM WORD COUNT**: This chapter MUST be AT LEAST {min_chapter_length:,} words - NO EXCEPTIONS
- **ABSOLUTE MINIMUM**: This chapter MUST be AT LEAST {min_chapter_length:,} words - NO EXCEPTIONS
- **OPTIMAL TARGET**: Write {target_chapter_length} words for perfect Contemporary Romance pacing
- **WORD COUNT PRIORITY**: Meeting word count is MORE IMPORTANT than rushing to plot points
- **SCENE REQUIREMENT**: Include 4-5 fully developed scenes (800-1,000 words each minimum)
- **EMOTIONAL EXPANSION**: Contemporary Romance demands extensive emotional interiority - elaborate extensively
- **DIALOGUE DEPTH**: Include substantial dialogue with subtext and emotional layers
- **RELATIONSHIP FOCUS**: Dedicate 60%+ of word count to relationship development and emotional content

## 🚨 CHARACTER NAME COMPLIANCE - USE THESE EXACT NAMES 🚨
{character_info}
**CRITICAL**: Use ONLY the character names listed above. Do NOT create new names like "Amelia" or "Sarah".
The characters have been specifically created for this story - USE THEIR EXACT NAMES throughout the chapter.

## CONTEMPORARY ROMANCE CHAPTER STRUCTURE REQUIREMENTS (to ensure adequate length)
1. **Opening Scene** (800-1,000 words): Establish contemporary setting, character emotional state, modern context
2. **Development Scene** (1,000-1,200 words): Advance relationship through modern interactions (work, technology, family)
3. **Conflict/Tension Scene** (800-1,000 words): Contemporary obstacles or cultural tensions
4. **Emotional Climax Scene** (800-1,000 words): Peak emotional moment reflecting modern relationship dynamics
5. **Transition/Setup Scene** (600-800 words): Bridge to next chapter with contemporary elements

## Contemporary Romance Writing Techniques
- **Modern Dialogue**: Authentic contemporary speech patterns and cultural expressions
- **Technology Integration**: Natural use of phones, social media, and digital communication
- **Cultural Authenticity**: Genuine representation of cultural background and traditions
- **Career Integration**: Professional life naturally woven into romantic development
- **Family Dynamics**: Modern family relationships and generational differences
- **Social Context**: Contemporary social issues and their impact on relationships
- **Emotional Interiority**: Deep exploration of modern relationship psychology
- **Physical and Emotional Intimacy**: Contemporary approach to romantic and physical connection

## Contemporary Romance Scene Types to Include
- **Workplace Interactions**: Professional settings creating romantic tension
- **Family Gatherings**: Cultural traditions and modern family dynamics
- **Digital Communication**: Texts, calls, and social media interactions
- **Social Events**: Contemporary social settings and peer interactions
- **Cultural Celebrations**: Authentic cultural events and traditions
- **Career Moments**: Professional achievements and challenges affecting romance
- **Intimate Conversations**: Deep emotional sharing in contemporary contexts
- **Conflict Resolution**: Modern approaches to addressing relationship challenges

## MANDATORY WORD COUNT VERIFICATION
- Count your words as you write - aim for 5,000+ words minimum
- Each scene should be substantial and fully developed
- Do NOT summarize or rush through emotional moments
- Expand on internal thoughts, feelings, and cultural context
- Include rich descriptions of contemporary settings and cultural elements
- Develop authentic dialogue that reflects cultural background and modern communication

## FINAL CONTEMPORARY ROMANCE CHAPTER CHECKLIST
Before completing this chapter, ensure you have:
✓ Written AT LEAST {min_chapter_length:,} words (count carefully!)
✓ Included 4-5 fully-developed scenes with rich contemporary detail
✓ Explored character emotions with extensive internal monologue
✓ Included substantial dialogue with cultural authenticity
✓ Advanced romantic tension through contemporary interactions
✓ Described modern settings, technology, and cultural elements in rich detail
✓ Created natural pacing with NO rushed or summarized moments
✓ Dedicated majority of word count to relationship development

## 🚨 ULTRA-CRITICAL FINAL REQUIREMENTS 🚨
1. **WORD COUNT VERIFICATION**: Your chapter MUST be {min_chapter_length:,}+ words. Count them!
2. **CHARACTER NAME VERIFICATION**: Use ONLY the provided character names - no substitutions!
3. **SCENE COUNT VERIFICATION**: Include 4-5 substantial scenes (800+ words each)
4. **CULTURAL AUTHENTICITY VERIFICATION**: Authentic representation of cultural background
5. **CONTEMPORARY RELEVANCE VERIFICATION**: Modern settings, technology, and social context
6. **ROMANCE FOCUS VERIFICATION**: 60%+ of content must focus on romantic relationship development

IF ANY OF THESE REQUIREMENTS ARE NOT MET, THE CHAPTER IS INCOMPLETE AND UNACCEPTABLE.
Contemporary Romance readers deserve substantial, emotionally rich content with authentic cultural representation and modern relationship dynamics.
"""

        return base_prompt + contemporary_romance_additions

        ```python
        class ContemporaryRomanceMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover copy for a Contemporary Romance novel.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, hero character description,
        heroine character description, setting, plot summary, key themes, emotional stakes,
        trope, target audience, comparable titles).

        Returns:
        str: A detailed prompt string for AI-powered back cover copy generation.
        """
        return f"""
        Write a captivating back cover description for a Contemporary Romance novel.

        Genre: Contemporary Romance

        Target Audience: Readers who enjoy heartwarming, relatable, and emotionally engaging love stories set in modern times. Think fans of authors like Emily Henry, Tessa Bailey, and Christina Lauren.

        Key Elements to Include:

        *   **Emotional Hook:** Emphasize the emotional connection between the hero and heroine. Focus on the vulnerability, desires, and internal conflicts that drive their relationship. What are they searching for? What are they afraid of?
        *   **Relatable Characters:** Highlight the characters' flaws, insecurities, and everyday struggles. Make them feel authentic and relatable to the reader. Avoid overly perfect or idealized depictions.
        *   **Realistic Setting:** Ground the story in a believable and contemporary setting. Use vivid descriptions to bring the location to life and make it feel like a place the reader could actually visit.
        *   **High Stakes (Emotional):** Even though it's Contemporary Romance, there should still be something at stake. This could be a career, a family relationship, a secret from the past, or simply the risk of heartbreak.
        *   **Tension and Chemistry:** Create a palpable sense of tension and chemistry between the hero and heroine. Hint at the obstacles they must overcome to be together. Use suggestive but tasteful language.
        *   **Hopeful Ending:** While the road to love may be bumpy, the ending should ultimately be optimistic and satisfying. Leave the reader feeling happy and hopeful.
        *   **Trope Awareness:** If the story utilizes a popular romance trope (e.g., enemies to lovers, second chance romance, fake dating), subtly incorporate it into the description.

        Tone: Warm, engaging, witty, and emotionally resonant. Avoid overly dramatic or melodramatic language.

        Do NOT include:
        * Spoilers for major plot twists or the ending.
        * Cliches or overused phrases.
        * Generic descriptions that could apply to any romance novel.

        Consider these questions to spark interest:

        *   What is the central conflict that keeps the hero and heroine apart?
        *   What are their deepest desires and fears?
        *   What makes their connection unique and special?
        *   What will they risk to be together?

        Book Details:

        *   Title: {kwargs.get('title', '[Insert Title Here]')}
        *   Author: {kwargs.get('author', '[Insert Author Name Here]')}
        *   Hero Description: {kwargs.get('hero_description', '[Insert Hero Description Here]')}
        *   Heroine Description: {kwargs.get('heroine_description', '[Insert Heroine Description Here]')}
        *   Setting: {kwargs.get('setting', '[Insert Setting Description Here]')}
        *   Plot Summary: {kwargs.get('plot_summary', '[Insert Plot Summary Here]')}
        *   Key Themes: {kwargs.get('key_themes', '[Insert Key Themes Here]')} (e.g., self-discovery, forgiveness, second chances)
        *   Emotional Stakes: {kwargs.get('emotional_stakes', '[Insert Emotional Stakes Here]')}
        *   Trope: {kwargs.get('trope', '[Insert Trope Here, if applicable]')} (e.g., enemies to lovers, friends to lovers, fake dating)
        *   Comparable Titles: {kwargs.get('comparable_titles', '[Insert Comparable Titles Here]')} (e.g., books by Emily Henry, Tessa Bailey, Christina Lauren)
        """

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, punchy description (2-3 lines) for a Contemporary Romance novel, suitable for book recommendations.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, hero character, heroine character, key conflict).

        Returns:
        str: A prompt string for AI-powered short description generation.
        """
        return f"""
        Write a short, engaging description (2-3 lines) for a Contemporary Romance novel, suitable for a book recommendation.

        Genre: Contemporary Romance

        Focus: Capture the essence of the story in a concise and intriguing way. Highlight the central conflict and the emotional connection between the hero and heroine.

        Tone: Playful, intriguing, and emotionally resonant.

        Include:

        *   The core relationship dynamic.
        *   A hint of the central conflict.
        *   A sense of emotional stakes.

        Avoid:

        *   Spoilers.
        *   Generic phrases.

        Book Details:

        *   Title: {kwargs.get('title', '[Insert Title Here]')}
        *   Author: {kwargs.get('author', '[Insert Author Name Here]')}
        *   Hero Character: {kwargs.get('hero_character', '[Insert Hero Character Description Here]')}
        *   Heroine Character: {kwargs.get('heroine_character', '[Insert Heroine Character Description Here]')}
        *   Key Conflict: {kwargs.get('key_conflict', '[Insert Key Conflict Here]')}
        """

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy and memorable marketing tagline for a Contemporary Romance novel.

        Args:
        **kwargs: Keyword arguments containing book details (title, key theme, emotional hook, unique selling point).

        Returns:
        str: A prompt string for AI-powered tagline generation.
        """
        return f"""
        Write a catchy and memorable marketing tagline for a Contemporary Romance novel.

        Genre: Contemporary Romance

        Goal: To grab the reader's attention and make them want to learn more about the book.

        Characteristics:

        *   Short and concise (ideally under 10 words).
        *   Intriguing and thought-provoking.
        *   Emotionally resonant.
        *   Reflects the core theme or conflict of the story.
        *   Highlights the unique selling point of the book.

        Examples of Effective Taglines:

        *   Love is the ultimate risk.
        *   Sometimes, the greatest love stories start with the biggest mistakes.
        *   One summer can change everything.
        *   Finding love where you least expect it.

        Book Details:

        *   Title: {kwargs.get('title', '[Insert Title Here]')}
        *   Key Theme: {kwargs.get('key_theme', '[Insert Key Theme Here]')} (e.g., second chances, self-discovery, overcoming fear)
        *   Emotional Hook: {kwargs.get('emotional_hook', '[Insert Emotional Hook Here]')} (e.g., forbidden love, overcoming grief, finding your voice)
        *   Unique Selling Point: {kwargs.get('unique_selling_point', '[Insert Unique Selling Point Here]')} (e.g., unusual setting, quirky characters, unexpected twist)
        """

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining visual style preferences for the back cover of a Contemporary Romance novel.

        Args:
        **kwargs: Keyword arguments containing book details (setting, tone, target audience, character archetypes).

        Returns:
        str: A prompt string for AI-powered visual style suggestions.
        """
        return f"""
        Describe the ideal visual style for the back cover of a Contemporary Romance novel.

        Genre: Contemporary Romance

        Considerations:

        *   **Color Palette:** Should evoke feelings of warmth, happiness, and romance. Consider using soft pastels, vibrant hues, or a combination of both. The color choices should align with the overall tone of the book.
        *   **Imagery:** May include photographs or illustrations. Photographs should feature attractive but relatable models who embody the characters. Illustrations can be more abstract and symbolic. Focus on conveying the mood and setting of the story. Avoid overly posed or staged images.
        *   **Typography:** Choose fonts that are easy to read and visually appealing. The font should reflect the tone of the book (e.g., playful, elegant, modern).
        *   **Overall Design:** The design should be clean, uncluttered, and visually engaging. Avoid overcrowding the cover with too many elements. The focus should be on creating a sense of romance and intrigue.

        Specific Guidelines:

        *   Avoid overly sexualized or suggestive imagery. Focus on conveying emotional connection and intimacy.
        *   Consider incorporating elements that reflect the setting of the story (e.g., a beach, a city skyline, a cozy cafe).
        *   The overall design should appeal to a female audience aged 25-45.

        Book Details:

        *   Setting: {kwargs.get('setting', '[Insert Setting Description Here]')}
        *   Tone: {kwargs.get('tone', '[Insert Tone Description Here]')} (e.g., lighthearted, emotional, witty)
        *   Target Audience: {kwargs.get('target_audience', '[Insert Target Audience Description Here]')}
        *   Character Archetypes: {kwargs.get('character_archetypes', '[Insert Character Archetypes Here]')} (e.g., the girl next door, the brooding hero, the charming best friend)
        """
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return ContemporaryRomancePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ContemporaryRomancePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ContemporaryRomancePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ContemporaryRomancePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ContemporaryRomancePrompts.get_enhancement_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_plan_prompt(**kwargs) -> str:
    return ContemporaryRomancePrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return ContemporaryRomancePrompts.get_series_book_prompt(**kwargs)
