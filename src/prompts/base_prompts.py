"""
Base prompt templates for novel generation.

This module provides specialized foundation prompt templates for different
types of content: Fiction (narrative), Non-Fiction (informational), and
Special Formats (unique structures).
"""

from typing import Dict, Any, List, Optional

class BasePrompts:
    """Base class for all genre-specific prompts."""

    # Genre information (to be overridden by subclasses)
    GENRE_NAME = "Generic"
    GENRE_DESCRIPTION = "A general genre"
    GENRE_CHARACTERISTICS = []
    TYPICAL_ELEMENTS = []
    CONTENT_TYPE = "generic"  # "fiction", "non_fiction", or "special_format"

class FictionBasePrompts(BasePrompts):
    """Base class for narrative fiction genres."""

    CONTENT_TYPE = "fiction"

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        """Generate a writer profile prompt for fiction genres."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        target_audience = kwargs.get("target_audience", "Adult")

        return f"""
# Fiction Writer Profile Generation for {cls.GENRE_NAME}

Create a detailed writer profile for a {cls.GENRE_NAME.lower()} novel titled "{title}".

## Novel Information
- Title: {title}
- Description: {description}
- Target Audience: {target_audience}
- Genre: {cls.GENRE_NAME}
- Content Type: Narrative Fiction

## Genre Characteristics
{chr(10).join(f"- {char}" for char in cls.GENRE_CHARACTERISTICS)}

## Fiction Writing Profile Instructions
Generate a comprehensive writer profile that includes:

1. **Narrative Voice**: Point of view, narrative style, and voice characteristics for {cls.GENRE_NAME.lower()}
2. **Character-Driven Storytelling**: Approach to developing compelling characters and their arcs
3. **Plot Structure**: Story pacing, conflict development, and resolution style for {cls.GENRE_NAME.lower()}
4. **Dialogue Style**: How characters speak and interact in {cls.GENRE_NAME.lower()}
5. **Scene Construction**: How to build engaging scenes with action, dialogue, and description
6. **Thematic Integration**: Weaving themes naturally into the narrative
7. **Reader Engagement**: Creating emotional connection and page-turning momentum

The profile should guide the creation of a compelling {cls.GENRE_NAME.lower()} novel with strong narrative elements, well-developed characters, and engaging storytelling that meets genre conventions while offering fresh perspectives.

Return the writer profile as a detailed description focusing on the narrative approach for this specific {cls.GENRE_NAME.lower()} work.
"""

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        """Generate a fiction outline prompt."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        writer_profile = kwargs.get("writer_profile", "")
        target_length = kwargs.get("target_length", "medium")

        # Determine chapter count based on target length
        chapter_counts = {
            "short": "8-12",
            "medium": "15-20",
            "long": "25-30"
        }
        chapter_range = chapter_counts.get(target_length, "15-20")

        return f"""
# {cls.GENRE_NAME} Fiction Novel Outline Generation

Create a detailed narrative outline for a {cls.GENRE_NAME.lower()} novel titled "{title}".

## Novel Information
- Title: {title}
- Description: {description}
- Genre: {cls.GENRE_NAME}
- Content Type: Narrative Fiction
- Target Length: {target_length.title()}
- Recommended Chapters: {chapter_range}

## Writer Profile
{writer_profile}

## Genre Requirements for {cls.GENRE_NAME}
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Fiction Outline Instructions
Create a comprehensive narrative outline that includes:

1. **Story Arc Structure**: Three-act structure with compelling beginning, middle, and end
2. **Character Journey**: Protagonist's transformation and growth throughout the story
3. **Plot Development**: Major events, conflicts, and turning points that drive the narrative
4. **Chapter Breakdown**: Detailed summary for each chapter with scene descriptions
5. **Character Relationships**: How characters interact and influence each other
6. **Conflict Escalation**: How tension builds throughout the story
7. **Thematic Elements**: Core themes woven into the narrative structure

## Format Requirements
Return as a JSON object with:
- recommended_chapter_count: Number (within the {chapter_range} range)
- target_word_count: Number (appropriate for {target_length} length)
- chapters: Array of chapter objects with "title" and "summary" fields
- key_themes: Array of main themes
- character_arcs: Object describing main character development
- major_plot_points: Array of key story events
- conflict_structure: Description of how conflict develops

Ensure the outline follows {cls.GENRE_NAME.lower()} conventions while creating an engaging and original narrative story.
"""

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character development prompt for fiction."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")

        return f"""
# Fiction Character Development for {cls.GENRE_NAME}

Develop compelling characters for the {cls.GENRE_NAME.lower()} novel "{title}".

## Novel Information
- Title: {title}
- Description: {description}
- Genre: {cls.GENRE_NAME}
- Content Type: Narrative Fiction

## Story Outline
{outline}

## {cls.GENRE_NAME} Character Requirements
{chr(10).join(f"- {char}" for char in cls.GENRE_CHARACTERISTICS)}

## Fiction Character Development Instructions
Create detailed character profiles that include:

1. **Main Characters** (2-4 characters):
   - Name, age, and basic demographics
   - Physical appearance and distinctive features
   - Personality traits, quirks, and mannerisms
   - Background, history, and formative experiences
   - Goals, motivations, and internal conflicts
   - Character arc and transformation throughout the story
   - Relationships with other characters
   - Role and function in the {cls.GENRE_NAME.lower()} narrative
   - Dialogue voice and speaking patterns

2. **Supporting Characters** (2-3 characters):
   - Name and role in the story
   - Key personality traits and characteristics
   - Relationship to main characters
   - Purpose and function in the narrative
   - How they influence the protagonist's journey

## Fiction Character Guidelines for {cls.GENRE_NAME}
- Characters should feel like real people with depth and complexity
- Each character should have clear motivations that drive their actions
- Character conflicts should create tension and drive the plot forward
- Character growth should be earned through story events
- Dialogue should reflect each character's unique voice and background
- Characters should fit naturally within {cls.GENRE_NAME.lower()} conventions

Return detailed character descriptions that will bring this {cls.GENRE_NAME.lower()} story to life with memorable, three-dimensional characters.
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        """Generate a chapter writing prompt for fiction."""
        chapter_num = kwargs.get("chapter_num", 1)
        chapter_outline = kwargs.get("chapter_outline", "")
        previous_chapters = kwargs.get("previous_chapters", "")
        characters = kwargs.get("characters", "")
        title = kwargs.get("title", "Untitled")

        return f"""
# Chapter {chapter_num} - {cls.GENRE_NAME} Fiction Novel

Write Chapter {chapter_num} for the {cls.GENRE_NAME.lower()} novel "{title}".

## Chapter Outline
{chapter_outline}

## Previous Chapters Summary
{previous_chapters}

## Character Information
{characters}

## {cls.GENRE_NAME} Writing Guidelines
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Fiction Chapter Writing Instructions
Write a compelling narrative chapter that:

1. **Follows the Outline**: Adheres to the planned chapter summary while allowing for creative expansion
2. **Advances the Story**: Moves the plot forward through action, dialogue, and character development
3. **Develops Characters**: Shows character growth, relationships, and internal conflicts
4. **Creates Scenes**: Build vivid scenes with setting, action, and character interaction
5. **Maintains Pacing**: Uses appropriate rhythm and tension for {cls.GENRE_NAME.lower()}
6. **Includes Dialogue**: Natural conversations that reveal character and advance plot
7. **Shows Don't Tell**: Uses action and dialogue to convey information and emotion

## Fiction Writing Style for {cls.GENRE_NAME}
- Use vivid, immersive descriptions that put readers in the scene
- Create natural dialogue that reflects each character's unique voice
- Balance action, dialogue, and internal thoughts
- Maintain consistent point of view and narrative voice
- Include sensory details and emotional depth
- Build appropriate atmosphere and mood for {cls.GENRE_NAME.lower()}

Write the complete chapter with rich narrative detail, engaging dialogue, and strong storytelling that exemplifies excellent {cls.GENRE_NAME.lower()} fiction writing.
"""

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        """Generate a chapter enhancement prompt for fiction."""
        chapter_text = kwargs.get("chapter_text", "")
        chapter_num = kwargs.get("chapter_num", 1)
        chapter_title = kwargs.get("chapter_title", f"Chapter {kwargs.get('chapter_num', 1)}")

        return f"""
# Fiction Chapter Enhancement for {cls.GENRE_NAME}

Enhance and improve the following chapter from a {cls.GENRE_NAME.lower()} novel.

## Original Chapter Text
{chapter_text}

## Enhancement Guidelines for {cls.GENRE_NAME}
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Fiction Enhancement Instructions
Enhance the chapter by:

1. **Strengthening Narrative Elements**: Improve storytelling, pacing, and scene construction
2. **Deepening Character Development**: Add more personality, depth, and authentic dialogue
3. **Enhancing Prose Quality**: Improve sentence structure, word choice, and narrative flow
4. **Increasing Reader Engagement**: Make scenes more vivid and emotionally compelling
5. **Improving Genre Elements**: Strengthen aspects specific to {cls.GENRE_NAME.lower()}
6. **Maintaining Story Consistency**: Keep core plot and character voices intact

## Specific Fiction Enhancements for {cls.GENRE_NAME}
- Enhance dialogue to sound more natural and character-specific
- Add sensory details and vivid scene descriptions
- Improve pacing and tension appropriate to {cls.GENRE_NAME.lower()}
- Strengthen emotional resonance and character connections
- Ensure genre conventions are well-represented
- Add subtext and depth to character interactions

Return the enhanced chapter that exemplifies excellent {cls.GENRE_NAME.lower()} fiction writing while maintaining the original story structure.
"""


class NonFictionBasePrompts(BasePrompts):
    """Base class for informational non-fiction genres."""

    CONTENT_TYPE = "non_fiction"

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        """Generate a writer profile prompt for non-fiction genres."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        target_audience = kwargs.get("target_audience", "Adult")

        return f"""
# Non-Fiction Writer Profile Generation for {cls.GENRE_NAME}

Create a detailed writer profile for a {cls.GENRE_NAME.lower()} book titled "{title}".

## Book Information
- Title: {title}
- Description: {description}
- Target Audience: {target_audience}
- Genre: {cls.GENRE_NAME}
- Content Type: Informational Non-Fiction

## Genre Characteristics
{chr(10).join(f"- {char}" for char in cls.GENRE_CHARACTERISTICS)}

## Non-Fiction Writing Profile Instructions
Generate a comprehensive writer profile that includes:

1. **Expertise and Authority**: Establish credibility and knowledge in the subject area
2. **Information Architecture**: How to organize and present complex information clearly
3. **Research Methodology**: Approach to gathering, verifying, and citing sources
4. **Explanatory Style**: How to make complex topics accessible to the target audience
5. **Evidence Integration**: Incorporating data, examples, and case studies effectively
6. **Practical Application**: Providing actionable insights and takeaways for readers
7. **Reader Engagement**: Maintaining interest in informational content
8. **Ethical Considerations**: Responsible presentation of facts and balanced perspectives

The profile should guide the creation of an authoritative, well-researched {cls.GENRE_NAME.lower()} book that educates and informs readers while maintaining engagement and credibility.

Return the writer profile as a detailed description focusing on the informational approach for this specific {cls.GENRE_NAME.lower()} work.
"""

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        """Generate a non-fiction outline prompt."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        writer_profile = kwargs.get("writer_profile", "")
        target_length = kwargs.get("target_length", "medium")

        # Determine chapter count based on target length
        chapter_counts = {
            "short": "6-10",
            "medium": "10-15",
            "long": "15-20"
        }
        chapter_range = chapter_counts.get(target_length, "10-15")

        return f"""
# {cls.GENRE_NAME} Non-Fiction Book Outline Generation

Create a detailed informational outline for a {cls.GENRE_NAME.lower()} book titled "{title}".

## Book Information
- Title: {title}
- Description: {description}
- Genre: {cls.GENRE_NAME}
- Content Type: Informational Non-Fiction
- Target Length: {target_length.title()}
- Recommended Chapters: {chapter_range}

## Writer Profile
{writer_profile}

## Genre Requirements for {cls.GENRE_NAME}
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Non-Fiction Outline Instructions
Create a comprehensive informational outline that includes:

1. **Information Architecture**: Logical flow of topics from basic to advanced concepts
2. **Chapter Structure**: Clear organization of information within each chapter
3. **Knowledge Building**: How each chapter builds upon previous information
4. **Evidence and Examples**: Integration of research, data, and real-world examples
5. **Practical Applications**: Actionable insights and takeaways for readers
6. **Learning Objectives**: What readers will gain from each section
7. **Supporting Materials**: References, resources, and further reading

## Format Requirements
Return as a JSON object with:
- recommended_chapter_count: Number (within the {chapter_range} range)
- target_word_count: Number (appropriate for {target_length} length)
- chapters: Array of chapter objects with "title" and "summary" fields
- key_topics: Array of main subjects covered
- learning_objectives: Array of what readers will learn
- required_research: Array of research areas needed
- target_expertise_level: Description of assumed reader knowledge

Ensure the outline follows {cls.GENRE_NAME.lower()} conventions while creating an informative and well-structured educational resource.
"""

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character/subject development prompt for non-fiction."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")

        return f"""
# Non-Fiction Subject and Expert Development for {cls.GENRE_NAME}

Develop key subjects, experts, and case studies for the {cls.GENRE_NAME.lower()} book "{title}".

## Book Information
- Title: {title}
- Description: {description}
- Genre: {cls.GENRE_NAME}
- Content Type: Informational Non-Fiction

## Book Outline
{outline}

## {cls.GENRE_NAME} Subject Requirements
{chr(10).join(f"- {char}" for char in cls.GENRE_CHARACTERISTICS)}

## Non-Fiction Subject Development Instructions
Create detailed profiles for:

1. **Key Experts/Authorities** (2-3 profiles):
   - Name and credentials
   - Area of expertise relevant to the book
   - Key insights and perspectives they provide
   - Quotes or concepts attributed to them
   - Role in supporting the book's arguments

2. **Case Studies/Examples** (3-5 examples):
   - Specific situations or instances that illustrate key points
   - Background context and relevant details
   - How they support the book's main themes
   - Lessons learned or insights gained

3. **Research Sources** (5-8 sources):
   - Academic studies, reports, or data sources
   - How they support the book's claims
   - Key findings or statistics to highlight
   - Credibility and relevance to the topic

## Non-Fiction Development Guidelines for {cls.GENRE_NAME}
- All subjects should be factually accurate and well-researched
- Examples should be relevant and illustrative of key concepts
- Expert perspectives should add credibility and depth
- Case studies should be engaging while remaining informative
- Sources should be current, credible, and properly attributable

Return detailed subject profiles that will support and enhance this {cls.GENRE_NAME.lower()} book with authoritative, well-researched content.
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        """Generate a chapter writing prompt for non-fiction."""
        chapter_num = kwargs.get("chapter_num", 1)
        chapter_outline = kwargs.get("chapter_outline", "")
        previous_chapters = kwargs.get("previous_chapters", "")
        characters = kwargs.get("characters", "")  # In non-fiction, this would be experts/sources
        title = kwargs.get("title", "Untitled")

        return f"""
# Chapter {chapter_num} - {cls.GENRE_NAME} Non-Fiction Book

Write Chapter {chapter_num} for the {cls.GENRE_NAME.lower()} book "{title}".

## Chapter Outline
{chapter_outline}

## Previous Chapters Summary
{previous_chapters}

## Expert Sources and Case Studies
{characters}

## {cls.GENRE_NAME} Writing Guidelines
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Non-Fiction Chapter Writing Instructions
Write an informative and engaging chapter that:

1. **Follows the Outline**: Adheres to the planned chapter structure while allowing for detailed exploration
2. **Educates Readers**: Provides clear, accurate information on the chapter's topic
3. **Supports Claims**: Uses evidence, data, and expert opinions to back up statements
4. **Maintains Engagement**: Keeps readers interested through examples, stories, and clear explanations
5. **Builds Knowledge**: Connects to previous chapters and prepares for upcoming content
6. **Provides Value**: Offers actionable insights or deeper understanding
7. **Cites Sources**: Properly attributes information to credible sources

## Non-Fiction Writing Style for {cls.GENRE_NAME}
- Use clear, accessible language appropriate for the target audience
- Include relevant examples, case studies, and real-world applications
- Present information in a logical, easy-to-follow structure
- Balance authoritative tone with reader engagement
- Include data, statistics, and research findings where appropriate
- Maintain objectivity while presenting compelling arguments

Write the complete chapter with thorough research, clear explanations, and engaging presentation that exemplifies excellent {cls.GENRE_NAME.lower()} non-fiction writing.
"""

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        """Generate a chapter enhancement prompt for non-fiction."""
        chapter_text = kwargs.get("chapter_text", "")
        chapter_num = kwargs.get("chapter_num", 1)
        chapter_title = kwargs.get("chapter_title", f"Chapter {kwargs.get('chapter_num', 1)}")

        return f"""
# Non-Fiction Chapter Enhancement for {cls.GENRE_NAME}

Enhance and improve the following chapter from a {cls.GENRE_NAME.lower()} book.

## Original Chapter Text
{chapter_text}

## Enhancement Guidelines for {cls.GENRE_NAME}
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Non-Fiction Enhancement Instructions
Enhance the chapter by:

1. **Improving Information Clarity**: Make complex concepts more accessible and understandable
2. **Strengthening Evidence**: Add more credible sources, data, and supporting examples
3. **Enhancing Engagement**: Make the content more interesting and relatable to readers
4. **Improving Structure**: Organize information more logically and effectively
5. **Adding Practical Value**: Include more actionable insights and takeaways
6. **Maintaining Accuracy**: Ensure all facts and claims are properly supported

## Specific Non-Fiction Enhancements for {cls.GENRE_NAME}
- Add relevant examples and case studies to illustrate key points
- Improve transitions between concepts and sections
- Strengthen the evidence base with additional credible sources
- Make the writing more engaging while maintaining authority
- Ensure proper attribution and citation of sources
- Add practical applications and actionable advice where appropriate

Return the enhanced chapter that exemplifies excellent {cls.GENRE_NAME.lower()} non-fiction writing while maintaining accuracy and credibility.
"""


class SpecialFormatBasePrompts(BasePrompts):
    """Base class for special format genres (poetry, graphic novels, collections, etc.)."""

    CONTENT_TYPE = "special_format"

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        """Generate a writer profile prompt for special format genres."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        target_audience = kwargs.get("target_audience", "Adult")

        return f"""
# Special Format Writer Profile Generation for {cls.GENRE_NAME}

Create a detailed writer profile for a {cls.GENRE_NAME.lower()} work titled "{title}".

## Work Information
- Title: {title}
- Description: {description}
- Target Audience: {target_audience}
- Genre: {cls.GENRE_NAME}
- Content Type: Special Format

## Genre Characteristics
{chr(10).join(f"- {char}" for char in cls.GENRE_CHARACTERISTICS)}

## Special Format Writing Profile Instructions
Generate a comprehensive writer profile that includes:

1. **Format Mastery**: Understanding of the unique structural requirements of {cls.GENRE_NAME.lower()}
2. **Creative Approach**: How to work within the constraints and opportunities of this format
3. **Artistic Vision**: Aesthetic and conceptual approach specific to {cls.GENRE_NAME.lower()}
4. **Technical Skills**: Specific techniques and methods required for this format
5. **Audience Engagement**: How to connect with readers through this unique format
6. **Innovation Within Tradition**: Balancing format conventions with creative originality
7. **Presentation Considerations**: How the format affects layout, design, and reader experience

The profile should guide the creation of an innovative, well-crafted {cls.GENRE_NAME.lower()} work that honors the format's traditions while offering fresh perspectives and artistic merit.

Return the writer profile as a detailed description focusing on the format-specific approach for this {cls.GENRE_NAME.lower()} work.
"""

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        """Generate a special format outline prompt."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        writer_profile = kwargs.get("writer_profile", "")
        target_length = kwargs.get("target_length", "medium")

        # Determine structure based on target length (varies by format)
        structure_counts = {
            "short": "5-8 sections",
            "medium": "8-12 sections",
            "long": "12-20 sections"
        }
        structure_range = structure_counts.get(target_length, "8-12 sections")

        return f"""
# {cls.GENRE_NAME} Special Format Structure Generation

Create a detailed structural outline for a {cls.GENRE_NAME.lower()} work titled "{title}".

## Work Information
- Title: {title}
- Description: {description}
- Genre: {cls.GENRE_NAME}
- Content Type: Special Format
- Target Length: {target_length.title()}
- Recommended Structure: {structure_range}

## Writer Profile
{writer_profile}

## Genre Requirements for {cls.GENRE_NAME}
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Special Format Structure Instructions
Create a comprehensive structural outline that includes:

1. **Format Architecture**: Overall organization specific to {cls.GENRE_NAME.lower()}
2. **Section Planning**: Individual components and their relationships
3. **Thematic Development**: How themes unfold through the format structure
4. **Artistic Progression**: How the work builds artistically from beginning to end
5. **Format-Specific Elements**: Unique features that define {cls.GENRE_NAME.lower()}
6. **Reader Journey**: How readers will experience and navigate the work
7. **Technical Considerations**: Format requirements and constraints

## Format Requirements
Return as a JSON object with:
- recommended_section_count: Number (within the {structure_range})
- target_word_count: Number (appropriate for {target_length} length and format)
- sections: Array of section objects with "title" and "description" fields
- key_themes: Array of main themes
- format_elements: Array of special format features to include
- artistic_progression: Description of how the work develops
- technical_requirements: Array of format-specific needs

Ensure the outline follows {cls.GENRE_NAME.lower()} conventions while creating an innovative and artistically compelling work.
"""

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character/element development prompt for special formats."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")

        return f"""
# Special Format Element Development for {cls.GENRE_NAME}

Develop key elements, subjects, or characters for the {cls.GENRE_NAME.lower()} work "{title}".

## Work Information
- Title: {title}
- Description: {description}
- Genre: {cls.GENRE_NAME}
- Content Type: Special Format

## Work Outline
{outline}

## {cls.GENRE_NAME} Element Requirements
{chr(10).join(f"- {char}" for char in cls.GENRE_CHARACTERISTICS)}

## Special Format Element Development Instructions
Create detailed profiles for the key components of this {cls.GENRE_NAME.lower()} work:

1. **Primary Elements** (3-5 main components):
   - Name/title and description
   - Role and function within the work
   - Artistic or thematic significance
   - How they contribute to the overall format
   - Relationship to other elements

2. **Supporting Elements** (2-4 secondary components):
   - Description and purpose
   - How they enhance the primary elements
   - Technical or artistic requirements
   - Integration with the overall structure

3. **Format-Specific Features** (varies by genre):
   - Unique characteristics of this {cls.GENRE_NAME.lower()} format
   - Technical requirements or constraints
   - Artistic opportunities and innovations
   - Reader interaction considerations

## Special Format Guidelines for {cls.GENRE_NAME}
- Elements should work together to create a cohesive artistic experience
- Each component should serve the overall vision and format requirements
- Consider how the format affects presentation and reader engagement
- Balance innovation with respect for format traditions
- Ensure technical feasibility within the chosen format

Return detailed element descriptions that will create a compelling and well-crafted {cls.GENRE_NAME.lower()} work.
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        """Generate a section/piece writing prompt for special formats."""
        chapter_num = kwargs.get("chapter_num", 1)
        chapter_outline = kwargs.get("chapter_outline", "")
        previous_chapters = kwargs.get("previous_chapters", "")
        characters = kwargs.get("characters", "")  # In special formats, this would be elements/components
        title = kwargs.get("title", "Untitled")

        return f"""
# Section {chapter_num} - {cls.GENRE_NAME} Special Format Work

Create Section {chapter_num} for the {cls.GENRE_NAME.lower()} work "{title}".

## Section Outline
{chapter_outline}

## Previous Sections Summary
{previous_chapters}

## Key Elements and Components
{characters}

## {cls.GENRE_NAME} Writing Guidelines
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Special Format Creation Instructions
Create a compelling section that:

1. **Follows Format Conventions**: Adheres to the structural requirements of {cls.GENRE_NAME.lower()}
2. **Advances the Work**: Contributes meaningfully to the overall artistic vision
3. **Utilizes Format Strengths**: Takes advantage of what makes {cls.GENRE_NAME.lower()} unique
4. **Maintains Consistency**: Fits seamlessly with the established style and approach
5. **Engages the Audience**: Uses format-specific techniques to connect with readers
6. **Demonstrates Craft**: Shows mastery of the technical and artistic aspects
7. **Serves the Whole**: Functions as part of the larger artistic statement

## Special Format Style for {cls.GENRE_NAME}
- Use techniques and approaches specific to {cls.GENRE_NAME.lower()}
- Consider how format affects pacing, rhythm, and reader experience
- Employ format-specific devices and conventions appropriately
- Balance artistic expression with technical requirements
- Create work that honors the format while offering fresh perspectives
- Consider visual, auditory, or other sensory aspects as relevant

Create the complete section with attention to craft, artistic merit, and format mastery that exemplifies excellent {cls.GENRE_NAME.lower()} work.
"""

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        """Generate an enhancement prompt for special formats."""
        chapter_text = kwargs.get("chapter_text", "")
        chapter_num = kwargs.get("chapter_num", 1)
        chapter_title = kwargs.get("chapter_title", f"Section {kwargs.get('chapter_num', 1)}")

        return f"""
# Special Format Enhancement for {cls.GENRE_NAME}

Enhance and improve the following section from a {cls.GENRE_NAME.lower()} work.

## Original Section Text
{chapter_text}

## Enhancement Guidelines for {cls.GENRE_NAME}
{chr(10).join(f"- {element}" for element in cls.TYPICAL_ELEMENTS)}

## Special Format Enhancement Instructions
Enhance the section by:

1. **Strengthening Format Elements**: Improve use of {cls.GENRE_NAME.lower()}-specific techniques
2. **Enhancing Artistic Merit**: Increase the aesthetic and creative quality
3. **Improving Technical Craft**: Refine the execution of format requirements
4. **Increasing Impact**: Make the section more powerful and memorable
5. **Better Integration**: Improve how it fits with the overall work
6. **Format Innovation**: Add creative touches that push format boundaries appropriately

## Specific Enhancements for {cls.GENRE_NAME}
- Refine format-specific techniques and conventions
- Improve rhythm, pacing, or flow as appropriate to the format
- Enhance artistic expression while maintaining technical accuracy
- Strengthen the unique qualities that make {cls.GENRE_NAME.lower()} distinctive
- Consider presentation and reader experience factors
- Balance tradition with innovation in format approach

Return the enhanced section that exemplifies excellent {cls.GENRE_NAME.lower()} craft while maintaining the original artistic vision.
"""
