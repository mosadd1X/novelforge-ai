"""
Biography genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class BiographyPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Biography"
    GENRE_DESCRIPTION = "A biography is a detailed account of a person's life, written by someone else. It explores their experiences, achievements, failures, and impact on the world, aiming to provide a comprehensive and insightful portrait of the subject."
    
    GENRE_CHARACTERISTICS = [
        "Thorough Research: Based on extensive research, including primary and secondary sources, interviews, and archival materials.",
        "Chronological Narrative: Typically follows a chronological structure, tracing the subject's life from birth to death or the present day.",
        "Objective Perspective: Strives for objectivity, presenting a balanced view of the subject, acknowledging both strengths and weaknesses.",
        "Contextualization: Places the subject within their historical, social, and cultural context, explaining how these factors influenced their life and work.",
        "Psychological Insight: Explores the subject's motivations, personality traits, and inner conflicts, offering insights into their character.",
        "Anecdotal Evidence: Incorporates anecdotes, personal stories, and memorable incidents to bring the subject to life and illustrate key aspects of their personality.",
        "Analysis and Interpretation: Goes beyond mere recounting of events, offering analysis and interpretation of the subject's actions and decisions.",
        "Engaging Narrative: Presents the subject's life in a compelling and engaging manner, captivating the reader's attention and maintaining their interest.",
        "Source Citation: Provides clear and accurate citations for all sources used, ensuring transparency and credibility.",
        "Ethical Considerations: Addresses ethical considerations related to privacy, accuracy, and fairness in representing the subject's life."
    ]
    
    TYPICAL_ELEMENTS = [
        "Birth and Early Life: Details about the subject's birth, family background, and childhood experiences.",
        "Education and Intellectual Development: Information about the subject's education, intellectual influences, and formative experiences.",
        "Career and Achievements: A comprehensive account of the subject's career, accomplishments, and contributions to their field.",
        "Relationships and Personal Life: Exploration of the subject's relationships with family, friends, colleagues, and romantic partners.",
        "Challenges and Obstacles: Examination of the challenges, obstacles, and setbacks the subject faced throughout their life.",
        "Turning Points and Key Decisions: Identification of critical moments and decisions that shaped the subject's life and career.",
        "Public Image and Reputation: Analysis of the subject's public image, reputation, and impact on society.",
        "Legacy and Influence: Assessment of the subject's lasting legacy and influence on future generations.",
        "Personal Beliefs and Values: Exploration of the subject's personal beliefs, values, and philosophical outlook.",
        "Physical and Mental Health: Discussion of the subject's physical and mental health, including any illnesses or disabilities.",
        "Death and Memorialization: Account of the subject's death, funeral, and memorialization.",
        "Critical Reception: Overview of how the subject and their work were received by critics and the public."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Writing Considerations
- **Historical Accuracy**: Ensure meticulous accuracy in all historical details, dates, and events. Cross-reference multiple reliable sources to verify information.
- **Objectivity and Fairness**: Strive for objectivity in portraying the subject, avoiding hagiography or demonization. Present a balanced view, acknowledging both strengths and weaknesses.
- **Source Material Management**: Develop a robust system for managing and citing source materials, including primary documents, interviews, and secondary sources. Use footnotes, endnotes, or a bibliography to provide clear attribution.
- **Ethical Considerations**: Be mindful of ethical considerations related to privacy, confidentiality, and potential harm to living individuals. Obtain necessary permissions and approvals before publishing sensitive information.
- **Narrative Voice and Tone**: Choose a narrative voice and tone that is appropriate for the subject and the intended audience. Consider whether to adopt a formal, academic style or a more informal, accessible style.
- **Contextual Understanding**: Demonstrate a deep understanding of the historical, social, and cultural context in which the subject lived and worked. Explain how these factors influenced their life and achievements.
- **Psychological Depth**: Explore the subject's motivations, personality traits, and inner conflicts, offering insights into their character and behavior. Avoid speculative or unsubstantiated psychological interpretations.
- **Engaging Storytelling**: Craft a compelling and engaging narrative that captures the reader's attention and maintains their interest. Use vivid language, anecdotes, and memorable details to bring the subject to life.
'''
        return base_prompt + biography_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Outline Requirements
- **Chronological Structure**: Organize the outline chronologically, following the subject's life from birth to death or the present day. Divide the life into distinct periods or phases, such as childhood, adolescence, early career, and later years.
- **Key Events and Turning Points**: Identify key events and turning points in the subject's life that had a significant impact on their development and career. Dedicate specific chapters or sections to these pivotal moments.
- **Thematic Organization**: Consider incorporating thematic elements into the outline, such as the subject's relationship with family, their intellectual development, or their contributions to society.
- **Relationship Mapping**: Include sections that specifically explore the subject's relationships with key individuals, such as family members, friends, mentors, and rivals. Analyze the dynamics of these relationships and their impact on the subject's life.
- **Contextual Background**: Integrate contextual background information into the outline, providing historical, social, and cultural context for the subject's life and work.
- **Source Material Integration**: Indicate where specific source materials will be used in each chapter or section, ensuring that the narrative is grounded in evidence and research.
- **Analysis and Interpretation**: Include sections that offer analysis and interpretation of the subject's actions, decisions, and legacy. Avoid simply recounting events; instead, provide insights and perspectives.
- **Conclusion and Reflection**: End the outline with a conclusion that summarizes the subject's life and legacy, reflecting on their impact and significance.
'''
        return base_prompt + biography_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Character Development
- **Authenticity and Accuracy**: Prioritize authenticity and accuracy in portraying the subject's character. Base all characterizations on verifiable evidence and reliable sources.
- **Complexity and Nuance**: Avoid simplistic or one-dimensional portrayals. Acknowledge the subject's complexities, contradictions, and internal conflicts.
- **Psychological Depth**: Explore the subject's motivations, personality traits, and emotional responses. Use psychological insights to illuminate their character and behavior.
- **Voice and Dialogue**: Recreate the subject's voice and dialogue as accurately as possible, drawing on primary sources such as letters, speeches, and interviews.
- **Physical Description**: Provide a detailed physical description of the subject, based on photographs, portraits, and eyewitness accounts.
- **Habits and Mannerisms**: Include details about the subject's habits, mannerisms, and quirks, adding depth and personality to the portrayal.
- **Relationships and Interactions**: Show how the subject interacted with others, highlighting their relationships with family, friends, colleagues, and rivals.
- **Evolution and Change**: Trace the evolution of the subject's character over time, showing how they changed and developed in response to their experiences.
'''
        return base_prompt + biography_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        biography_additions = '''
## Biography-Specific Chapter Writing
- **Contextual Setting**: Begin each chapter by establishing the historical, social, and cultural context in which the events take place.
- **Chronological Flow**: Maintain a clear chronological flow, guiding the reader through the subject's life in a logical and coherent manner.
- **Anecdotal Integration**: Incorporate anecdotes, personal stories, and memorable incidents to bring the subject to life and illustrate key aspects of their personality.
- **Source Material Incorporation**: Seamlessly integrate source material into the narrative, using quotes, paraphrases, and summaries to support your claims.
- **Descriptive Language**: Use vivid and descriptive language to paint a picture of the subject's world, capturing the sights, sounds, and smells of their environment.
- **Emotional Resonance**: Evoke emotional resonance in the reader, allowing them to connect with the subject on a personal level.
- **Analytical Insights**: Offer analytical insights and interpretations of the subject's actions and decisions, providing context and meaning.
- **Transition Smoothly**: Transition smoothly between different topics and time periods, maintaining a consistent narrative flow.
- **Concluding Summary**: End each chapter with a brief summary of the key events and themes, preparing the reader for the next stage of the subject's life.
'''
        return base_prompt + biography_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return BiographyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return BiographyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return BiographyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return BiographyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return BiographyPrompts.get_enhancement_prompt(**kwargs)