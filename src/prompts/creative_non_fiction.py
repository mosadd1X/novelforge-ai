"""
Creative Non-Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class CreativeNonFictionPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Creative Non-Fiction"
    GENRE_DESCRIPTION = "Creative Non-Fiction blends factual accuracy with literary flair. It employs narrative techniques typically associated with fiction, such as character development, plot structure, and vivid imagery, to tell true stories. The genre encompasses a wide range of forms, including memoir, personal essay, literary journalism, and travel writing, all grounded in verifiable reality but elevated by artistic expression."
    
    GENRE_CHARACTERISTICS = [
        "Personal Voice: The author's unique perspective and experiences are central to the narrative.",
        "Factual Accuracy: While employing creative techniques, the work remains committed to truth and verifiable facts.",
        "Narrative Structure: Employs storytelling techniques like plot, pacing, and suspense to engage the reader.",
        "Character Development: Real people are portrayed as complex characters with motivations, flaws, and growth.",
        "Setting and Atmosphere: Vivid descriptions of places and environments contribute to the overall impact.",
        "Thematic Exploration: Explores universal themes and ideas through personal experiences and observations.",
        "Reflective Tone: Often includes introspection and analysis of the events and their significance.",
        "Emotional Resonance: Aims to evoke emotional responses in the reader through relatable experiences.",
        "Immersive Detail: Uses sensory details and specific anecdotes to create a sense of immediacy and authenticity.",
        "Ethical Considerations: Navigates the ethical complexities of representing real people and events responsibly."
    ]
    
    TYPICAL_ELEMENTS = [
        "Memoir: Focuses on a specific period or theme in the author's life.",
        "Personal Essay: Explores a topic through the lens of the author's personal experiences and reflections.",
        "Literary Journalism: Combines journalistic reporting with literary techniques to tell true stories.",
        "Travel Writing: Documents journeys and cultural encounters with a focus on personal observations and insights.",
        "Biography/Autobiography: Tells the life story of a real person, either by themselves or another author.",
        "Creative Biography: A biography that employs creative writing techniques to bring the subject to life.",
        "Flash Nonfiction: Short, impactful pieces that capture a moment or idea with brevity and precision.",
        "Lyric Essay: Blends elements of poetry and prose to explore a subject in a fragmented and evocative way.",
        "Immersion Journalism: The author embeds themselves in a situation to report on it firsthand.",
        "Anecdotes: Short, engaging stories that illustrate a point or reveal character.",
        "Dialogue: Realistic conversations that reveal character and advance the narrative.",
        "Reflection: Introspective passages that explore the meaning and significance of events."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        creative_non_fiction_additions = '''
## Creative Non-Fiction-Specific Writing Considerations
- **Ethical Responsibility**: Understand the ethical implications of writing about real people and events. Prioritize accuracy, fairness, and respect for privacy. Consider obtaining consent when necessary and avoiding sensationalism.
- **Voice and Authenticity**: Cultivate a unique and authentic voice that resonates with readers. Be honest and vulnerable in your writing, sharing your personal experiences and perspectives with sincerity.
- **Memory and Recall**: Develop techniques for accurately recalling and representing past events. Utilize journals, photographs, interviews, and research to enhance memory and ensure factual accuracy.
- **Emotional Honesty**: Explore your emotions and motivations with honesty and introspection. Be willing to confront difficult truths and share your vulnerabilities with readers.
- **Balancing Fact and Art**: Master the art of blending factual accuracy with literary techniques. Use vivid language, imagery, and narrative structure to engage readers while remaining true to the facts.
- **Research and Verification**: Conduct thorough research to support your writing and ensure accuracy. Verify facts, dates, and details to maintain credibility and avoid misinformation.
- **Audience Awareness**: Consider your target audience and tailor your writing to their interests and expectations. Choose a tone, style, and level of detail that will resonate with your readers.
- **Self-Reflection**: Regularly reflect on your writing process and identify areas for improvement. Seek feedback from trusted sources and be open to constructive criticism.
'''
        return base_prompt + creative_non_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        creative_non_fiction_additions = '''
## Creative Non-Fiction-Specific Outline Requirements
- **Theme Identification**: Clearly define the central theme or message you want to convey. Ensure that each section of the outline contributes to the exploration of this theme.
- **Chronological vs. Thematic Structure**: Decide whether to structure your narrative chronologically or thematically. A chronological structure follows a linear timeline, while a thematic structure groups events and experiences around specific themes.
- **Character Arcs**: Map out the character arcs of the real people in your story. Consider how they change and evolve throughout the narrative.
- **Setting the Scene**: Outline the key settings and environments that will be featured in your narrative. Include details about the atmosphere, sensory details, and significance of each setting.
- **Anecdotal Integration**: Identify key anecdotes and stories that will illustrate your points and engage readers. Plan where to incorporate these anecdotes into your outline.
- **Reflective Passages**: Allocate space for reflective passages where you can explore your thoughts, feelings, and insights about the events and experiences you are describing.
- **Ethical Considerations**: Consider any ethical implications of your story and plan how to address them in your narrative.
- **Dramatic Tension**: Identify moments of conflict, tension, or suspense that will keep readers engaged. Plan how to build and release tension throughout the narrative.
- **Resolution and Reflection**: Plan how to bring your narrative to a satisfying resolution. Include a final reflective passage that summarizes your key insights and takeaways.
'''
        return base_prompt + creative_non_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        creative_non_fiction_additions = '''
## Creative Non-Fiction-Specific Character Development
- **Authenticity and Complexity**: Strive to portray real people with authenticity and complexity. Avoid stereotypes and caricatures, and instead focus on capturing their unique personalities, motivations, and flaws.
- **Multiple Perspectives**: Consider incorporating multiple perspectives to provide a more nuanced and complete picture of the characters and events.
- **Inner Life**: Explore the inner lives of your characters, including their thoughts, feelings, and motivations. Use introspection and reflection to reveal their inner worlds to readers.
- **Dialogue and Interaction**: Use dialogue and interaction to reveal character and advance the narrative. Pay attention to the way people speak and interact with each other.
- **Physical Description**: Provide vivid physical descriptions of your characters, including their appearance, mannerisms, and body language.
- **Backstory and Context**: Provide relevant backstory and context to help readers understand your characters' motivations and actions.
- **Ethical Considerations**: Be mindful of the ethical implications of portraying real people in your writing. Respect their privacy and avoid sensationalizing their stories.
- **Character Arc**: Consider the character arc of each person in your story. How do they change and evolve throughout the narrative?
'''
        return base_prompt + creative_non_fiction_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        creative_non_fiction_additions = '''
## Creative Non-Fiction-Specific Chapter Writing
- **Scene Setting**: Begin each chapter with a vivid description of the setting, including sensory details, atmosphere, and significance.
- **Anecdotal Storytelling**: Weave anecdotes and personal stories into your chapters to illustrate your points and engage readers.
- **Character Development**: Use each chapter to further develop your characters, revealing their personalities, motivations, and flaws.
- **Dialogue Integration**: Incorporate realistic dialogue to reveal character and advance the narrative.
- **Reflective Passages**: Include reflective passages where you explore your thoughts, feelings, and insights about the events and experiences you are describing.
- **Pacing and Structure**: Vary the pacing and structure of your chapters to keep readers engaged. Use short, punchy sentences to create a sense of urgency, and longer, more descriptive sentences to create a sense of atmosphere.
- **Thematic Focus**: Ensure that each chapter contributes to the overall theme or message of your narrative.
- **Ethical Considerations**: Be mindful of the ethical implications of your writing and avoid sensationalizing or exploiting your subjects.
- **Show, Don't Tell**: Use vivid language and imagery to show readers what is happening, rather than simply telling them.
'''
        return base_prompt + creative_non_fiction_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return CreativeNonFictionPrompts.get_enhancement_prompt(**kwargs)