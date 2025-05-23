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
        base_prompt = super().get_character_prompt(**kwargs)
        
        poetry_collection_additions = '''
## Poetry Collection-Specific Character Development
- **Character as Persona**: In poetry, characters often function as personae, representing aspects of the poet's own experiences or emotions. Consider how your characters can embody different facets of the human condition.
- **Symbolic Representation**: Characters can also serve as symbols, representing abstract concepts or ideas. Think about how your characters can be used to explore themes like love, loss, or justice.
- **Voice and Perspective**: Develop a distinct voice and perspective for each character. Consider their background, motivations, and beliefs.
- **Emotional Depth**: Explore the emotional depth of your characters. Show their vulnerabilities, fears, and desires.
- **Relationships**: Consider the relationships between your characters. How do they interact with each other? What conflicts or connections do they share?
- **Character Arc**: While not always present in individual poems, consider if a character arc develops across multiple poems within the collection. How does the character change or evolve over time?
- **Limited Detail**: Unlike novels, poetry often relies on suggestion rather than explicit detail. Use concise language and evocative imagery to create memorable characters.
- **Focus on Internal Landscape**: Prioritize exploring the character's internal thoughts, feelings, and motivations rather than providing extensive physical descriptions.
'''
        return base_prompt + poetry_collection_additions

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
'''
        return base_prompt + poetry_collection_additions

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