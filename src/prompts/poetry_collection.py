"""
Poetry Collection genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class PoetryCollectionPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Poetry Collection"
    GENRE_DESCRIPTION = "A poetry collection is a curated compilation of poems, often unified by a central theme, style, or emotional arc. It's a deliberate arrangement of individual pieces to create a larger, resonant artistic statement. The poems within can explore diverse subjects, forms, and perspectives, but they are ultimately bound together by the poet's unique voice and vision."

    GENRE_CHARACTERISTICS = [
        "Strong thematic coherence: The poems are often linked by a central theme, concept, or emotional thread, creating a unified reading experience.",
        "Distinct poetic voice: The collection showcases the poet's unique style, perspective, and use of language.",
        "Varied poetic forms: The collection may include a range of poetic forms, such as sonnets, free verse, haikus, and villanelles, demonstrating the poet's versatility.",
        "Emotional depth and resonance: The poems evoke strong emotions and create a lasting impact on the reader.",
        "Imagery and symbolism: The poems are rich in imagery and symbolism, inviting multiple interpretations and deeper understanding.",
        "Musicality and rhythm: The poems utilize sound devices such as alliteration, assonance, and consonance to create a musical effect.",
        "Exploration of personal experiences: The poems often draw on the poet's personal experiences, observations, and reflections.",
        "Social commentary: The poems may address social issues, political concerns, and cultural trends.",
        "Narrative elements: Some poems may tell stories or present characters, adding a narrative dimension to the collection.",
        "Careful arrangement: The order of the poems is carefully considered to create a specific flow and build towards a cohesive whole."
    ]

    TYPICAL_ELEMENTS = [
        "A title that reflects the collection's theme or central idea.",
        "A table of contents listing the poems in the collection.",
        "An introductory note or preface by the poet, providing context or insights into the collection.",
        "Poems exploring a range of emotions, such as love, loss, joy, and grief.",
        "Poems that use vivid imagery and sensory details to create a strong sense of place or atmosphere.",
        "Poems that employ various poetic devices, such as metaphor, simile, personification, and hyperbole.",
        "Poems that experiment with different forms and structures, such as sonnets, haikus, and free verse.",
        "Poems that address social or political issues.",
        "Poems that reflect on personal experiences and relationships.",
        "Poems that explore themes of nature, spirituality, or the human condition.",
        "A concluding poem that provides a sense of closure or resolution.",
        "An acknowledgments section, thanking individuals or organizations that supported the poet's work."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        poetry_collection_additions = '''
## Poetry Collection-Specific Writing Considerations
- **Voice and Style**: Develop a distinct poetic voice that is consistent throughout the collection. Experiment with different styles, such as confessional, lyrical, or narrative, to find the one that best suits your subject matter and perspective.
- **Thematic Unity**: Ensure that the poems in the collection are unified by a central theme or concept. Consider how each poem contributes to the overall message or emotional arc of the collection.
- **Form and Structure**: Explore different poetic forms and structures to create variety and interest. Experiment with traditional forms like sonnets and haikus, as well as free verse and experimental forms.
- **Imagery and Symbolism**: Use vivid imagery and symbolism to create a rich and evocative reading experience. Consider how specific images and symbols can reinforce the themes and emotions of the poems.
- **Sound and Rhythm**: Pay attention to the sound and rhythm of your poems. Use sound devices like alliteration, assonance, and consonance to create a musical effect. Experiment with different rhythms and line breaks to enhance the impact of your words.
- **Emotional Honesty**: Be honest and authentic in your expression of emotions. Don't be afraid to explore difficult or uncomfortable feelings.
- **Revision and Refinement**: Revise and refine your poems carefully. Pay attention to every word and line break. Seek feedback from other poets and writers.
- **Arrangement and Flow**: Consider the arrangement of the poems in the collection. Think about how the poems flow from one to the next and how the collection builds towards a cohesive whole.
'''
        return base_prompt + poetry_collection_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        poetry_collection_additions = '''
## Poetry Collection-Specific Outline Requirements
- **Thematic Sections**: Organize the collection into thematic sections, each exploring a different aspect of the central theme. For example, a collection about grief might have sections on denial, anger, bargaining, depression, and acceptance.
- **Emotional Arc**: Consider the emotional arc of the collection. How do you want the reader to feel as they move through the poems? Start with poems that introduce the theme and gradually build towards a climax or resolution.
- **Poem Selection**: Choose poems that are strong and representative of your best work. Include a variety of forms and styles to keep the collection interesting.
- **Order and Flow**: Arrange the poems in a way that creates a logical and engaging flow. Consider the transitions between poems and how they build upon each other.
- **Title and Introduction**: Develop a title that accurately reflects the theme and tone of the collection. Write an introduction that provides context and insights into your work.
- **Individual Poem Outlines**: For each poem, create a brief outline that identifies the main theme, imagery, and emotional tone. This will help you stay focused as you write.
- **Consider a Prologue/Epilogue**: Think about including a prologue poem to set the stage and an epilogue poem to provide closure.
- **Vary the Pace**: Mix longer, more complex poems with shorter, more accessible ones to create a varied reading experience.
'''
        return base_prompt + poetry_collection_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character/persona development prompt specifically for poetry collections."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")
        target_audience = kwargs.get("target_audience", "Adult")
        subplot_info = kwargs.get("subplot_info", "")

        return f"""
# Poetry Collection Persona and Voice Development

Create poetic personas and voices for the poetry collection "{title}" for {target_audience}.

## Collection Information
- Title: {title}
- Description: {description}
- Genre: Poetry Collection
- Target Audience: {target_audience}

## Collection Outline
{outline}

{subplot_info}

## Poetry Collection Persona Requirements

### Poetic Persona Guidelines
1. **Persona as Voice**: In poetry, characters function as personae - distinct voices that express different aspects of human experience
2. **Symbolic Representation**: Personas can represent abstract concepts, emotions, or universal themes
3. **Emotional Depth**: Focus on internal landscapes, feelings, and psychological states
4. **Voice Distinctiveness**: Each persona should have a unique poetic voice and perspective
5. **Thematic Connection**: Personas should connect to the collection's overall themes
6. **Poetic Language**: Personas should speak in language appropriate for poetry - evocative, metaphorical, condensed
7. **Universal Resonance**: While specific, personas should touch on universal human experiences

### Persona Types for Poetry Collections
- **Primary Voices**: 2-3 main personas who anchor major sections or themes
- **Thematic Personas**: 2-3 voices that embody specific themes or emotions
- **Narrative Voices**: 1-2 personas who might appear in narrative poems
- **Symbolic Figures**: 1-2 archetypal or symbolic personas

## Persona Object Format
For each persona, provide the following fields in a JSON object:
- "name": (string) Persona's name or title (can be symbolic like "The Wanderer" or "Night Voice")
- "role": (string) Their function (primary voice, thematic persona, symbolic figure, etc.)
- "appearance": (string) Poetic description focusing on symbolic or evocative details
- "personality": (string) Emotional characteristics and psychological traits
- "background": (string) Essential context that informs their voice and perspective
- "goals": (string) What they seek to express or explore through poetry
- "arc": (string) How their voice might evolve across the collection
- "relationships": (string) How they relate to other personas or themes
- "strengths": (string) Their emotional or spiritual strengths
- "flaws": (string) Their vulnerabilities or shadows
- "voice": (string) Their distinctive poetic voice and language patterns
- "thematic_focus": (string) What themes or emotions this persona primarily explores

## Poetry Collection Guidelines
- Personas should work well in the compressed, metaphorical language of poetry
- Each voice should be emotionally resonant and memorable
- Consider how personas might dialogue with each other across poems
- Focus on internal landscapes rather than external plot
- Ensure personas can carry the weight of poetic expression

Return ONLY a valid JSON array of persona objects, nothing else.
Example format:
[
  {{
    "name": "The Lighthouse Keeper",
    "role": "primary voice",
    "appearance": "Weathered hands that know the weight of solitude, eyes that have watched countless storms",
    "personality": "Contemplative and steadfast, carries both wisdom and loneliness",
    "background": "A guardian of safe passage who has spent years in isolation watching over others",
    "goals": "To explore themes of duty, solitude, and the meaning found in service to others",
    "arc": "Moves from isolation toward understanding connection across distance",
    "relationships": "Speaks to the ships that pass, communes with the sea and storms",
    "strengths": "Patience, dedication, deep observation of natural cycles",
    "flaws": "Tendency toward isolation, difficulty with human intimacy",
    "voice": "Measured and reflective, uses maritime and natural imagery",
    "thematic_focus": "Solitude, duty, the relationship between isolation and service"
  }}
]
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        poetry_collection_additions = '''
## Poetry Collection-Specific Chapter Writing
- **Focus on a Single Theme**: Each poem should focus on a single theme or idea. Avoid trying to cram too much into one poem.
- **Use Vivid Imagery**: Use vivid imagery and sensory details to create a strong sense of place or atmosphere.
- **Experiment with Form**: Experiment with different poetic forms and structures. Don't be afraid to break the rules.
- **Pay Attention to Sound**: Pay attention to the sound of your words. Use sound devices like alliteration, assonance, and consonance to create a musical effect.
- **Revise and Refine**: Revise and refine your poems carefully. Pay attention to every word and line break.
- **Create a Sense of Closure**: Each poem should have a sense of closure, even if it's just a subtle shift in tone or perspective.
- **Vary Length and Style**: Within a section, vary the length and style of the poems to maintain reader interest.
- **Consider White Space**: Use white space effectively to create pauses and emphasize certain words or phrases.

## CRITICAL POETRY REQUIREMENTS
**IMPORTANT**: This section must contain ACTUAL POEMS, not narrative prose or story content. Generate:
- Multiple individual poems (3-8 poems per section)
- Proper poetic structure with line breaks and stanzas
- Various poetic forms (free verse, sonnets, haikus, etc.)
- Poetic language with metaphors, imagery, and literary devices
- NO character development, plot progression, or narrative storytelling
- Focus on emotional expression, imagery, and poetic craft

**FORMAT REQUIREMENTS**:
- Each poem should have a title
- Use proper line breaks for poetic effect
- Include stanza breaks (empty lines between stanzas)
- Vary poem lengths and styles within the section
- End each poem with clear separation (*** or similar)
'''
        return base_prompt + poetry_collection_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a poetrycollection-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        poetrycollection_series_additions = """

## PoetryCollection Series-Specific Planning Elements

### Artistic Progression for PoetryCollection
- **Format Mastery**: Show increasing sophistication in poetrycollection techniques across volumes
- **Creative Evolution**: Plan how the artistic vision develops throughout the poetrycollection series
- **Thematic Development**: Create themes that deepen and evolve through the poetrycollection format
- **Artistic Cohesion**: Maintain unified artistic vision while allowing creative growth
- **Format Innovation**: Explore different aspects of poetrycollection across the series

### PoetryCollection Series Continuity
- **Style Consistency**: Maintain recognizable artistic voice across poetrycollection volumes
- **Technical Standards**: Maintain quality standards appropriate for poetrycollection
- **Creative Connections**: Create meaningful artistic links between poetrycollection volumes
- **Format Exploration**: Continue exploring the possibilities of poetrycollection format
- **Reader Experience**: Create engaging progression for poetrycollection enthusiasts

Create a poetrycollection series that showcases artistic development and format mastery across multiple volumes.
"""

        return base_prompt + poetrycollection_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a poetrycollection-specific individual volume prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        poetrycollection_book_additions = """

## PoetryCollection Series Volume Integration

### PoetryCollection Artistic Continuity
- **Style Consistency**: Maintain the artistic voice established in previous poetrycollection volumes
- **Technical Standards**: Maintain quality standards established in the poetrycollection series
- **Creative Evolution**: Show artistic growth from previous poetrycollection volumes
- **Format Mastery**: Build upon poetrycollection techniques established in the series
- **Thematic Connections**: Continue developing themes from earlier poetrycollection works

### Volume-Specific PoetryCollection Focus
- **Artistic Objectives**: What specific poetrycollection artistic goals will this volume achieve?
- **Format Innovation**: What new poetrycollection techniques or approaches will be introduced?
- **Creative Development**: How will this volume advance the artistic vision of the series?
- **Series Integration**: How does this volume connect meaningfully to other poetrycollection works in the series?
- **Artistic Value**: What unique poetrycollection artistic value does this volume add to the series?

Ensure this volume demonstrates poetrycollection mastery while serving as an integral part of the artistic series.
"""

        return base_prompt + poetrycollection_book_additions

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        """Generate a poetry collection-specific enhancement prompt."""
        base_prompt = super().get_enhancement_prompt(**kwargs)

        poetry_enhancement_additions = '''

## CRITICAL POETRY COLLECTION ENHANCEMENT REQUIREMENTS
**ABSOLUTELY ESSENTIAL**: This is a POETRY COLLECTION enhancement. You must:
- PRESERVE the poetic structure and format of the original content
- ENHANCE the poetic quality, imagery, and literary devices
- MAINTAIN proper line breaks, stanza breaks, and poetic formatting
- IMPROVE word choice, rhythm, and sound devices
- STRENGTHEN metaphors, imagery, and emotional impact
- DO NOT convert poems into narrative prose or story content
- DO NOT add character development or plot elements
- KEEP the focus on poetic expression and artistic merit

**ENHANCEMENT FOCUS**:
- Refine poetic language and word choice
- Strengthen imagery and sensory details
- Improve rhythm and sound patterns
- Enhance metaphors and literary devices
- Perfect line breaks and stanza structure
- Maintain the authentic poetic voice
'''
        return base_prompt + poetry_enhancement_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return PoetryCollectionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return PoetryCollectionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return PoetryCollectionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return PoetryCollectionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return PoetryCollectionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return PoetryCollectionPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return PoetryCollectionPrompts.get_series_book_prompt(**kwargs)
