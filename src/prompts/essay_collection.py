"""
Essay Collection genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class EssayCollectionPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Essay Collection"
    GENRE_DESCRIPTION = "An essay collection is a curated compilation of non-fiction essays, often exploring a central theme, authorial voice, or a range of interconnected subjects. The essays can vary in style, from personal and reflective to analytical and critical, but they are united by a common thread of intellectual curiosity and a desire to engage the reader in thoughtful exploration."

    GENRE_CHARACTERISTICS = [
        "Strong Authorial Voice: The author's personality, perspective, and experiences are central to the collection's appeal.",
        "Thematic Cohesion: Essays are often linked by a unifying theme, idea, or subject matter, creating a cohesive reading experience.",
        "Exploration of Ideas: The essays delve into complex topics, offering nuanced perspectives and challenging conventional wisdom.",
        "Personal Reflection: Many essays incorporate personal anecdotes and reflections, adding depth and emotional resonance.",
        "Intellectual Curiosity: The author demonstrates a genuine interest in learning and sharing knowledge with the reader.",
        "Varied Writing Styles: The collection may showcase a range of writing styles, from lyrical and descriptive to analytical and argumentative.",
        "Engaging Narrative: Even when dealing with abstract concepts, the essays maintain an engaging narrative flow.",
        "Critical Analysis: Essays often involve critical analysis of cultural, social, or political issues.",
        "Emotional Honesty: Authors are willing to be vulnerable and honest about their experiences and perspectives.",
        "Sense of Discovery: The essays create a sense of discovery, both for the author and the reader, as they explore new ideas and insights."
    ]

    TYPICAL_ELEMENTS = [
        "Introduction: A preface or introduction that sets the stage for the collection, outlining its themes and purpose.",
        "Personal Essays: Essays that focus on the author's personal experiences, reflections, and insights.",
        "Critical Essays: Essays that analyze cultural, social, or political issues from a specific perspective.",
        "Research-Based Essays: Essays that incorporate research and evidence to support their arguments.",
        "Memoiristic Elements: Incorporation of memoir-like passages to provide context and depth.",
        "Anecdotes: Use of personal anecdotes to illustrate points and engage the reader.",
        "Figurative Language: Use of metaphors, similes, and other figures of speech to enhance the writing.",
        "Vivid Descriptions: Detailed and evocative descriptions of people, places, and events.",
        "Thought-Provoking Questions: Posing questions that encourage the reader to think critically about the topics discussed.",
        "Concluding Remarks: Essays that end with a sense of closure, summarizing key points and offering final reflections.",
        "Epilogue (Optional): A concluding section that provides a final reflection on the collection as a whole.",
        "Notes and References (Optional): Inclusion of notes and references to support research-based essays."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        essay_collection_additions = '''
## Essay Collection-Specific Writing Considerations
- **Authorial Voice**: Develop a distinct and consistent authorial voice that resonates throughout the collection. Consider your tone, perspective, and level of formality.
- **Thematic Resonance**: Ensure that each essay contributes to the overall theme or message of the collection. Consider how the essays relate to one another and create a cohesive whole.
- **Personal Connection**: Identify your personal connection to the subject matter. What experiences or perspectives do you bring to the topic?
- **Intellectual Depth**: Conduct thorough research and engage with complex ideas in a thoughtful and nuanced way. Avoid superficial analysis and strive for intellectual rigor.
- **Emotional Honesty**: Be willing to be vulnerable and honest about your experiences and perspectives. Authenticity is key to connecting with readers.
- **Structural Variety**: Experiment with different essay structures and writing styles to keep the collection engaging and dynamic. Consider incorporating personal narratives, critical analysis, and research-based arguments.
- **Audience Engagement**: Consider your target audience and tailor your writing to their interests and knowledge level. Use clear and concise language, and avoid jargon or overly technical terms.
- **Ethical Considerations**: Be mindful of ethical considerations when writing about personal experiences or sensitive topics. Respect the privacy of others and avoid making generalizations or stereotypes.
'''
        return base_prompt + essay_collection_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        essay_collection_additions = '''
## Essay Collection-Specific Outline Requirements
- **Collection Theme**: Clearly define the overarching theme or purpose of the essay collection. This will guide the selection and arrangement of individual essays.
- **Essay Sequencing**: Determine the optimal sequence of essays to create a logical and engaging reading experience. Consider the flow of ideas, emotional arc, and thematic connections.
- **Individual Essay Structure**: For each essay, create a detailed outline that includes a clear thesis statement, supporting arguments, evidence, and concluding remarks.
- **Introduction and Conclusion**: Craft a compelling introduction that sets the stage for the collection and a thoughtful conclusion that summarizes key points and offers final reflections.
- **Transitional Elements**: Plan for transitional elements between essays to create a sense of continuity and flow. This could include brief introductions, thematic links, or recurring motifs.
- **Essay Variety**: Ensure that the collection includes a variety of essay types, such as personal narratives, critical analyses, and research-based arguments.
- **Pacing and Rhythm**: Consider the pacing and rhythm of the collection as a whole. Vary the length and complexity of essays to maintain reader interest.
- **Revision and Editing**: Allocate time for revision and editing to ensure that each essay is polished and error-free.
'''
        return base_prompt + essay_collection_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character/subject development prompt specifically for essay collections."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")
        target_audience = kwargs.get("target_audience", "Adult")
        subplot_info = kwargs.get("subplot_info", "")

        return f"""
# Essay Collection Character and Subject Development

Create key figures and subjects for the essay collection "{title}" for {target_audience}.

## Collection Information
- Title: {title}
- Description: {description}
- Genre: Essay Collection
- Target Audience: {target_audience}

## Collection Outline
{outline}

{subplot_info}

## Essay Collection Character Requirements

### Character/Subject Guidelines
1. **The Author as Central Figure**: The author/narrator is often the primary "character" in personal essays
2. **Real People as Characters**: When writing about others, develop them with complexity and respect
3. **Authentic Portrayal**: Characters should be based on real experiences and observations
4. **Ethical Considerations**: Respect privacy and avoid harmful portrayals of real people
5. **Character Evolution**: Show how people (including the author) change and grow across essays
6. **Distinct Voices**: Each person should have a unique voice and perspective
7. **Thematic Relevance**: Characters should connect to the collection's overall themes

### Character Types for Essay Collections
- **Author/Narrator**: The primary voice and perspective of the collection
- **Family Members**: Parents, siblings, relatives who appear in personal essays
- **Mentors/Influences**: Teachers, friends, or figures who shaped the author
- **Subjects of Study**: People the author observes, interviews, or writes about

## Character Object Format
For each character/subject, provide the following fields in a JSON object:
- "name": (string) Character's name (can be pseudonym for privacy)
- "role": (string) Their role (author/narrator, family member, mentor, subject, etc.)
- "appearance": (string) Physical description focusing on memorable, meaningful details
- "personality": (string) Key personality traits and characteristics
- "background": (string) Essential context about their life and experiences
- "goals": (string) What they seek or represent in the essays
- "arc": (string) How they develop or are revealed across the collection
- "relationships": (string) How they relate to the author and other figures
- "strengths": (string) Their positive qualities and contributions
- "flaws": (string) Their human weaknesses and complexities
- "voice": (string) How they speak and express themselves
- "significance": (string) What they represent or teach in the collection
- "ethical_considerations": (string) Privacy and portrayal considerations for this person

## Essay Collection Guidelines
- Characters should feel like real, complex human beings
- Respect the privacy and dignity of real people being portrayed
- Focus on authentic experiences and genuine insights
- Consider how characters connect to the collection's themes
- Balance honesty with compassion in character portrayal

Return ONLY a valid JSON array of character objects, nothing else.
Example format:
[
  {{
    "name": "The Author",
    "role": "author/narrator",
    "appearance": "A middle-aged writer with graying hair and thoughtful eyes, often seen with a notebook",
    "personality": "Introspective and curious, but sometimes overly self-critical",
    "background": "A lifelong observer of human nature, shaped by small-town upbringing and urban experiences",
    "goals": "To understand and articulate the complexities of modern life and relationships",
    "arc": "Grows from uncertainty to greater self-awareness and acceptance",
    "relationships": "Central figure who connects all other characters and experiences",
    "strengths": "Empathy, observational skills, ability to find meaning in everyday moments",
    "flaws": "Tendency toward overthinking, occasional self-doubt",
    "voice": "Reflective and honest, with touches of humor and vulnerability",
    "significance": "Represents the journey of understanding oneself and one's place in the world",
    "ethical_considerations": "Author's own experiences, told with honesty and self-reflection"
  }}
]
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        essay_collection_additions = '''
## Essay Collection-Specific Chapter Writing
- **Essay Focus**: Each essay (chapter) should have a clear and focused topic or argument. Avoid rambling or straying from the main point.
- **Engaging Opening**: Start each essay with an engaging opening that grabs the reader's attention and introduces the topic.
- **Clear Thesis Statement**: State your thesis statement clearly and concisely in the introduction. This will provide a roadmap for the essay.
- **Supporting Evidence**: Provide ample evidence to support your arguments, including personal anecdotes, research findings, and expert opinions.
- **Logical Organization**: Organize your essays in a logical and coherent manner. Use clear transitions to guide the reader from one point to the next.
- **Vivid Language**: Use vivid and descriptive language to bring your essays to life. Engage the reader's senses and create a memorable reading experience.
- **Personal Voice**: Infuse your essays with your own personal voice and perspective. Let your personality shine through in your writing.
- **Critical Thinking**: Engage in critical thinking and analysis. Challenge conventional wisdom and offer fresh insights.
- **Thoughtful Conclusion**: End each essay with a thoughtful conclusion that summarizes key points and offers final reflections.
- **Revision and Editing**: Revise and edit your essays carefully to ensure that they are polished and error-free.
'''
        return base_prompt + essay_collection_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a essaycollection-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        essaycollection_series_additions = """

## EssayCollection Series-Specific Planning Elements

### Artistic Progression for EssayCollection
- **Format Mastery**: Show increasing sophistication in essaycollection techniques across volumes
- **Creative Evolution**: Plan how the artistic vision develops throughout the essaycollection series
- **Thematic Development**: Create themes that deepen and evolve through the essaycollection format
- **Artistic Cohesion**: Maintain unified artistic vision while allowing creative growth
- **Format Innovation**: Explore different aspects of essaycollection across the series

### EssayCollection Series Continuity
- **Style Consistency**: Maintain recognizable artistic voice across essaycollection volumes
- **Technical Standards**: Maintain quality standards appropriate for essaycollection
- **Creative Connections**: Create meaningful artistic links between essaycollection volumes
- **Format Exploration**: Continue exploring the possibilities of essaycollection format
- **Reader Experience**: Create engaging progression for essaycollection enthusiasts

Create a essaycollection series that showcases artistic development and format mastery across multiple volumes.
"""

        return base_prompt + essaycollection_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a essaycollection-specific individual volume prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        essaycollection_book_additions = """

## EssayCollection Series Volume Integration

### EssayCollection Artistic Continuity
- **Style Consistency**: Maintain the artistic voice established in previous essaycollection volumes
- **Technical Standards**: Maintain quality standards established in the essaycollection series
- **Creative Evolution**: Show artistic growth from previous essaycollection volumes
- **Format Mastery**: Build upon essaycollection techniques established in the series
- **Thematic Connections**: Continue developing themes from earlier essaycollection works

### Volume-Specific EssayCollection Focus
- **Artistic Objectives**: What specific essaycollection artistic goals will this volume achieve?
- **Format Innovation**: What new essaycollection techniques or approaches will be introduced?
- **Creative Development**: How will this volume advance the artistic vision of the series?
- **Series Integration**: How does this volume connect meaningfully to other essaycollection works in the series?
- **Artistic Value**: What unique essaycollection artistic value does this volume add to the series?

Ensure this volume demonstrates essaycollection mastery while serving as an integral part of the artistic series.
"""

        return base_prompt + essaycollection_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return EssayCollectionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return EssayCollectionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return EssayCollectionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return EssayCollectionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return EssayCollectionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return EssayCollectionPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return EssayCollectionPrompts.get_series_book_prompt(**kwargs)
