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
        base_prompt = super().get_character_prompt(**kwargs)
        
        essay_collection_additions = '''
## Essay Collection-Specific Character Development
- **The Author as Character**: In personal essays, the author themselves is a central character. Develop a nuanced and authentic portrayal of your own personality, experiences, and perspectives.
- **Secondary Characters**: When writing about other people, develop them as characters with their own motivations, flaws, and complexities. Avoid reducing them to stereotypes or caricatures.
- **Character Arc**: Consider the character arc of the author or other individuals featured in the essays. How do they change or evolve over the course of the narrative?
- **Internal Conflict**: Explore the internal conflicts and struggles of the characters. This can add depth and emotional resonance to the essays.
- **Relationships**: Examine the relationships between characters and how these relationships shape their experiences and perspectives.
- **Voice and Dialogue**: Develop distinct voices for each character, including the author. Use dialogue to reveal character traits and advance the narrative.
- **Ethical Considerations**: Be mindful of ethical considerations when writing about real people. Respect their privacy and avoid portraying them in a negative or misleading light.
- **Authenticity**: Strive for authenticity in your character portrayals. Avoid embellishing or fabricating details to create a more dramatic or compelling narrative.
'''
        return base_prompt + essay_collection_additions

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