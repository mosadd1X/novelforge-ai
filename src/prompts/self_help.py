"""
Self-Help genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class SelfHelpPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Self-Help"
    GENRE_DESCRIPTION = "The Self-Help genre focuses on providing readers with practical advice, strategies, and techniques to improve their lives in various areas, such as personal development, relationships, career, health, and finances. It aims to empower readers to overcome challenges, achieve goals, and enhance their overall well-being through actionable steps and insightful perspectives."
    
    GENRE_CHARACTERISTICS = [
        "Focus on practical advice and actionable strategies that readers can implement immediately.",
        "Emphasis on personal growth, self-improvement, and achieving a better quality of life.",
        "Clear and concise language, avoiding jargon and complex terminology to ensure accessibility.",
        "Use of real-life examples, case studies, and anecdotes to illustrate concepts and make them relatable.",
        "Inspirational and motivational tone to encourage readers to take action and persevere through challenges.",
        "Structured approach with clear frameworks, models, and step-by-step guides to facilitate understanding and application.",
        "Evidence-based information, drawing on research, psychology, and other relevant fields to support claims and recommendations.",
        "Focus on identifying and addressing common problems, challenges, and obstacles that readers face.",
        "Emphasis on self-reflection, introspection, and understanding one's own thoughts, feelings, and behaviors.",
        "Provision of tools, exercises, and techniques to help readers develop new skills, habits, and mindsets."
    ]
    
    TYPICAL_ELEMENTS = [
        "Introduction that clearly defines the problem or area of focus and explains why it matters to the reader.",
        "Identification of the root causes of the problem or challenge being addressed.",
        "Presentation of a clear and concise framework or model for understanding the problem and its solutions.",
        "Step-by-step guide or action plan for implementing the recommended strategies and techniques.",
        "Real-life examples, case studies, and anecdotes to illustrate the concepts and make them relatable.",
        "Exercises, questionnaires, and self-assessment tools to help readers apply the concepts to their own lives.",
        "Tips, tricks, and shortcuts for overcoming common obstacles and challenges.",
        "Motivational stories and inspirational quotes to encourage readers to stay committed to their goals.",
        "Summary of key takeaways and action items at the end of each chapter or section.",
        "Resources and further reading suggestions for readers who want to learn more.",
        "Emphasis on the importance of consistency, patience, and perseverance in achieving lasting results.",
        "Call to action that encourages readers to take the next step and implement what they have learned."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        self_help_additions = '''
## Self-Help-Specific Writing Considerations
- **Expertise and Authority**: Establish credibility by highlighting relevant qualifications, experience, and expertise in the specific area of self-help. Readers need to trust that you are a reliable source of information.
- **Empathy and Understanding**: Demonstrate empathy for the reader's struggles and challenges. Show that you understand their pain points and are genuinely invested in helping them improve their lives.
- **Clarity and Simplicity**: Use clear, concise language and avoid jargon or technical terms that may confuse readers. Break down complex concepts into easily digestible steps.
- **Actionable Advice**: Focus on providing practical, actionable advice that readers can implement immediately. Avoid vague or abstract concepts that are difficult to apply.
- **Relatability and Authenticity**: Share personal stories and experiences to connect with readers on a deeper level. Be authentic and genuine in your writing, and avoid sounding preachy or judgmental.
- **Motivational Tone**: Maintain a positive and encouraging tone throughout the book. Inspire readers to take action and believe in their ability to achieve their goals.
- **Evidence-Based Approach**: Support your claims and recommendations with research, data, and scientific evidence whenever possible. This will enhance your credibility and make your advice more persuasive.
- **Ethical Considerations**: Ensure that your advice is ethical, responsible, and aligned with professional standards. Avoid making unrealistic promises or promoting harmful practices.
'''
        return base_prompt + self_help_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        self_help_additions = '''
## Self-Help-Specific Outline Requirements
- **Problem Definition**: Clearly define the problem or challenge that the book will address. Explain why it is important to the reader and what the potential consequences are of not addressing it.
- **Solution Overview**: Provide a high-level overview of the solution or approach that the book will present. Explain the key principles and concepts that underpin the solution.
- **Step-by-Step Guide**: Break down the solution into a series of actionable steps or stages. Each step should be clearly defined and easy to follow.
- **Real-Life Examples**: Include real-life examples, case studies, and anecdotes to illustrate the concepts and make them relatable to the reader.
- **Exercises and Activities**: Incorporate exercises, questionnaires, and self-assessment tools to help readers apply the concepts to their own lives.
- **Overcoming Obstacles**: Address common obstacles and challenges that readers may encounter when implementing the solution. Provide tips and strategies for overcoming these obstacles.
- **Maintaining Progress**: Offer advice on how to maintain progress and avoid relapse. Emphasize the importance of consistency, patience, and self-compassion.
- **Resources and Support**: Provide a list of resources and support networks that readers can turn to for further assistance.
- **Conclusion and Call to Action**: Summarize the key takeaways from the book and encourage readers to take the next step in their journey.
'''
        return base_prompt + self_help_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        self_help_additions = '''
## Self-Help-Specific Character Development
- **Relatable Protagonist**: If using a narrative structure, the protagonist should be relatable to the target audience, facing similar struggles and challenges.
- **Transformation Arc**: The protagonist should undergo a significant transformation throughout the book, demonstrating the effectiveness of the self-help principles being taught.
- **Realistic Flaws**: The protagonist should have realistic flaws and weaknesses that readers can identify with. This will make their journey more believable and inspiring.
- **Internal Motivation**: The protagonist's motivation for change should come from within, rather than being imposed by external forces.
- **Credible Mentor**: If a mentor figure is present, they should be knowledgeable, experienced, and genuinely invested in the protagonist's success.
- **Supporting Characters**: Supporting characters can provide different perspectives, challenges, and sources of support for the protagonist.
- **Character Backstory**: The protagonist's backstory should be relevant to the problem or challenge being addressed in the book.
- **Emotional Depth**: The protagonist should experience a range of emotions throughout the book, including hope, fear, frustration, and joy.
'''
        return base_prompt + self_help_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        self_help_additions = '''
## Self-Help-Specific Chapter Writing
- **Clear Chapter Objective**: Each chapter should have a clear and specific objective that is aligned with the overall goals of the book.
- **Engaging Introduction**: Start each chapter with an engaging introduction that grabs the reader's attention and sets the stage for the content to come.
- **Concise Explanations**: Explain complex concepts in a clear and concise manner, using simple language and avoiding jargon.
- **Actionable Steps**: Provide actionable steps that readers can take to implement the concepts being taught.
- **Real-Life Examples**: Include real-life examples, case studies, and anecdotes to illustrate the concepts and make them relatable.
- **Exercises and Activities**: Incorporate exercises, questionnaires, and self-assessment tools to help readers apply the concepts to their own lives.
- **Overcoming Obstacles**: Address common obstacles and challenges that readers may encounter when implementing the concepts.
- **Summary and Review**: Summarize the key takeaways from the chapter and provide a brief review of the concepts covered.
- **Transition to Next Chapter**: Smoothly transition to the next chapter by previewing the topics that will be covered.
'''
        return base_prompt + self_help_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_enhancement_prompt(**kwargs)