"""
Memoir genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class MemoirPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Memoir"
    GENRE_DESCRIPTION = "A memoir is a non-fiction narrative recounting specific events and themes in the author's life. It focuses on a particular aspect, relationship, or time period, offering personal reflections and insights rather than a comprehensive autobiography. The narrative voice is deeply personal and subjective, emphasizing emotional truth and the author's evolving understanding of their experiences."
    
    GENRE_CHARACTERISTICS = [
        "Focus on a specific theme or period: Memoirs typically center around a particular event, relationship, or period in the author's life, rather than attempting to cover their entire biography.",
        "Subjective and personal voice: The narrative is told from the author's unique perspective, emphasizing their feelings, thoughts, and interpretations of events.",
        "Emotional honesty and vulnerability: Memoirs require the author to be open and honest about their experiences, including their flaws, mistakes, and vulnerabilities.",
        "Reflection and insight: The author reflects on their experiences, drawing meaningful conclusions and insights about themselves, others, and the world.",
        "Strong narrative arc: While based on real events, memoirs should have a compelling narrative structure with a clear beginning, middle, and end.",
        "Vivid sensory details: The author uses descriptive language to bring scenes and characters to life, immersing the reader in their experiences.",
        "Exploration of universal themes: While personal, memoirs often explore universal themes such as love, loss, identity, resilience, and the search for meaning.",
        "Authenticity and truthfulness: While memoirs allow for subjective interpretation, they should be grounded in factual accuracy and a commitment to telling the truth as the author understands it.",
        "Character development: The author, and other key figures, should undergo a clear process of character development throughout the narrative.",
        "Use of flashbacks and reflection: Memoirs often interweave past experiences with present-day reflections to provide context and deeper understanding."
    ]
    
    TYPICAL_ELEMENTS = [
        "A compelling opening scene: Grabs the reader's attention and introduces the central theme or conflict of the memoir.",
        "Clearly defined scope: Establishes the specific focus and boundaries of the narrative.",
        "Vivid descriptions of settings: Creates a strong sense of place and time, immersing the reader in the author's world.",
        "Well-developed characters: Presents the author and other key figures as complex and relatable individuals.",
        "Significant events and turning points: Highlights key moments that shaped the author's life and understanding.",
        "Emotional arc: Tracks the author's emotional journey and transformation throughout the narrative.",
        "Internal monologue and reflections: Reveals the author's thoughts, feelings, and insights.",
        "Dialogue: Brings scenes to life and reveals character relationships.",
        "Use of imagery and metaphor: Enhances the emotional impact and thematic resonance of the narrative.",
        "Exploration of relationships: Examines the author's relationships with family, friends, and others.",
        "A satisfying resolution: Provides closure and offers a sense of hope or understanding.",
        "Thematic coherence: Ensures that all elements of the memoir contribute to the central theme or message."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Writing Considerations
- **Authenticity and Voice**: Develop a unique and authentic voice that reflects your personality and perspective. Prioritize honesty and vulnerability in your writing.
- **Emotional Recall**: Practice techniques for accessing and vividly recreating past emotions and sensations. Use sensory details to bring your experiences to life.
- **Ethical Considerations**: Be mindful of the impact your story may have on others. Consider obtaining consent or changing names to protect privacy.
- **Self-Reflection**: Engage in deep self-reflection to understand the motivations, beliefs, and values that shaped your experiences.
- **Narrative Structure**: Craft a compelling narrative arc with a clear beginning, middle, and end. Use flashbacks and foreshadowing to create suspense and intrigue.
- **Thematic Resonance**: Identify the universal themes that resonate within your personal story. Explore how your experiences connect to broader human experiences.
- **Objectivity vs. Subjectivity**: Strive for a balance between objective reporting of events and subjective interpretation. Acknowledge your biases and limitations.
- **Accuracy and Fact-Checking**: While memoirs prioritize emotional truth, ensure that factual details are as accurate as possible. Verify dates, names, and other relevant information.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Outline Requirements
- **Theme Identification**: Clearly define the central theme or message of your memoir. Ensure that all chapters and scenes contribute to this theme.
- **Chronological vs. Thematic Structure**: Decide whether to structure your memoir chronologically or thematically. Consider the advantages and disadvantages of each approach.
- **Key Events and Turning Points**: Identify the key events and turning points that shaped your life and understanding. Structure your outline around these pivotal moments.
- **Character Arcs**: Map out the character arcs of yourself and other key figures. Show how your relationships and perspectives evolved over time.
- **Emotional Journey**: Outline the emotional journey you experienced throughout the events of your memoir. Identify the highs, lows, and turning points in your emotional arc.
- **Reflection and Insight**: Allocate space in your outline for reflection and insight. Plan where you will interweave your present-day understanding with past experiences.
- **Balancing Act**: Ensure a balance between narrative storytelling, emotional reflection, and thematic exploration.
- **Ethical Considerations**: Outline how you will address any ethical considerations or potential sensitivities in your story.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Character Development
- **Self-Portrait**: Develop a nuanced and honest self-portrait. Explore your strengths, weaknesses, motivations, and flaws.
- **Authenticity**: Strive for authenticity in your portrayal of yourself and others. Avoid idealizing or demonizing characters.
- **Relationship Dynamics**: Explore the dynamics of your relationships with other characters. Show how your interactions shaped your experiences and perspectives.
- **Character Flaws**: Embrace the flaws and imperfections of your characters. These flaws make them relatable and human.
- **Motivation and Intentions**: Understand the motivations and intentions of each character. Explore the reasons behind their actions and decisions.
- **Change and Growth**: Show how characters change and grow throughout the narrative. Highlight the lessons they learned and the transformations they underwent.
- **Perspective**: Consider the perspectives of other characters. Acknowledge that your interpretation of events may differ from theirs.
- **Ethical Considerations**: Be mindful of the impact your portrayal of others may have on their lives. Consider obtaining consent or changing names to protect privacy.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        memoir_additions = '''
## Memoir-Specific Chapter Writing
- **Scene Setting**: Begin each chapter with a vivid description of the setting. Immerse the reader in the time and place of the events.
- **Emotional Resonance**: Focus on conveying the emotional impact of the events you are describing. Use sensory details and evocative language to create a strong emotional connection with the reader.
- **Internal Monologue**: Incorporate internal monologue to reveal your thoughts, feelings, and reactions to events.
- **Dialogue**: Use dialogue to bring scenes to life and reveal character relationships. Make sure the dialogue sounds authentic and natural.
- **Reflection and Insight**: Interweave reflections and insights throughout the chapter. Connect past experiences to present-day understanding.
- **Pacing**: Vary the pacing of your chapters to create a sense of rhythm and momentum. Use shorter sentences and paragraphs to create a sense of urgency, and longer sentences and paragraphs to create a sense of reflection.
- **Thematic Connection**: Ensure that each chapter contributes to the central theme or message of your memoir.
- **Honesty and Vulnerability**: Write with honesty and vulnerability. Share your fears, doubts, and insecurities with the reader.
'''
        return base_prompt + memoir_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a memoir-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        memoir_series_additions = """

## Memoir Series-Specific Planning Elements

### Educational Progression for Memoir
- **Knowledge Building**: Structure learning progression appropriate for memoir topics
- **Expertise Development**: Guide readers from basic to advanced understanding of memoir subjects
- **Practical Applications**: Include actionable insights specific to memoir throughout the series
- **Research Depth**: Plan comprehensive research appropriate for memoir authority
- **Reader Value**: Ensure each book provides significant memoir value while building series knowledge

### Memoir Series Continuity
- **Subject Consistency**: Maintain consistent approach to memoir topics across books
- **Authority Building**: Establish and maintain credibility in memoir throughout the series
- **Information Architecture**: Structure information flow appropriate for memoir learning
- **Cross-References**: Create meaningful connections between memoir concepts across books
- **Updated Knowledge**: Plan for incorporating new memoir research and developments

Create a memoir series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + memoir_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a memoir-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        memoir_book_additions = """

## Memoir Series Book Integration

### Memoir Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon memoir concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous memoir books when relevant
- **Knowledge Progression**: Advance reader understanding of memoir topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the memoir series

### Book-Specific Memoir Focus
- **Educational Objectives**: What specific memoir knowledge will readers gain from this book?
- **Practical Applications**: What actionable memoir insights will be provided?
- **Research Integration**: How will new memoir research be incorporated?
- **Series Advancement**: How does this book advance the overall memoir education series?
- **Reader Value**: What unique memoir value does this book add to the series?

Ensure this book provides comprehensive memoir education while serving as an integral part of the learning series.
"""

        return base_prompt + memoir_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return MemoirPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return MemoirPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return MemoirPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return MemoirPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return MemoirPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return MemoirPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return MemoirPrompts.get_series_book_prompt(**kwargs)
