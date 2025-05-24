"""
How-To genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class HowToPrompts(NonFictionBasePrompts):
    GENRE_NAME = "How-To"
    GENRE_DESCRIPTION = "The How-To genre provides clear, step-by-step instructions and guidance on how to accomplish a specific task, learn a new skill, or solve a particular problem. It emphasizes practicality, clarity, and actionable advice, often incorporating visuals and examples to enhance understanding and facilitate successful implementation."
    
    GENRE_CHARACTERISTICS = [
        "Clear and concise language, avoiding jargon or technical terms without proper explanation.",
        "Step-by-step instructions presented in a logical and sequential order.",
        "Use of numbered lists, bullet points, or other formatting techniques to enhance readability.",
        "Inclusion of visuals such as diagrams, illustrations, or photographs to clarify complex steps.",
        "Provision of practical tips, tricks, and best practices to optimize the process.",
        "Anticipation and addressing of potential challenges, pitfalls, or common mistakes.",
        "Emphasis on safety precautions and warnings where applicable.",
        "Inclusion of real-world examples, case studies, or demonstrations to illustrate the effectiveness of the method.",
        "A focus on achieving a specific, measurable, achievable, relevant, and time-bound (SMART) goal.",
        "Provision of resources, tools, or materials needed to complete the task."
    ]
    
    TYPICAL_ELEMENTS = [
        "A clear and concise title that accurately reflects the topic.",
        "An introduction that explains the purpose and benefits of the how-to guide.",
        "A list of required materials, tools, or prerequisites.",
        "Step-by-step instructions, each with a clear heading or label.",
        "Visual aids (images, diagrams, videos) to illustrate each step.",
        "Tips and tricks to improve efficiency or avoid common errors.",
        "Troubleshooting advice for common problems.",
        "Safety warnings and precautions.",
        "Examples or case studies to demonstrate the process.",
        "A conclusion that summarizes the key steps and reinforces the benefits.",
        "A call to action, encouraging the reader to try the method.",
        "A list of additional resources for further learning."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        how_to_additions = '''
## How-To-Specific Writing Considerations
- **Accuracy and Expertise**: Demonstrate a thorough understanding of the subject matter and ensure all information is accurate and up-to-date. Back up claims with credible sources where necessary.
- **Clarity and Simplicity**: Use clear, concise language that is easy for the target audience to understand. Avoid jargon or technical terms unless they are properly defined.
- **Action-Oriented Language**: Employ verbs that encourage action and participation from the reader. Use phrases like "try this," "follow these steps," and "see how easy it is."
- **Visual Communication**: Plan for the effective integration of visuals (images, diagrams, videos) to enhance understanding and engagement. Describe the purpose and content of each visual clearly.
- **Anticipate User Needs**: Consider the potential challenges and questions that readers might encounter and address them proactively within the instructions.
- **Maintain a Positive and Encouraging Tone**: Motivate readers to complete the task successfully by offering encouragement and highlighting the benefits of following the instructions.
- **Focus on Practical Application**: Emphasize the practical application of the information and provide real-world examples to illustrate the effectiveness of the method.
- **Iterative Refinement**: Be prepared to revise and refine the instructions based on feedback from beta readers or user testing to ensure clarity and accuracy.
'''
        return base_prompt + how_to_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        how_to_additions = '''
## How-To-Specific Outline Requirements
- **Introduction**: Clearly state the purpose and scope of the how-to guide. Include a brief overview of the steps involved and the benefits of following the instructions.
- **Materials/Tools List**: Provide a comprehensive list of all materials, tools, or software required to complete the task. Specify quantities, sizes, or versions where necessary.
- **Step-by-Step Instructions**: Break down the process into a series of clear, sequential steps. Each step should have a concise heading and detailed instructions.
- **Visual Integration**: Plan for the inclusion of visuals (images, diagrams, videos) at appropriate points in the instructions to illustrate key steps or concepts. Indicate the type of visual and its purpose.
- **Tips and Tricks**: Incorporate practical tips, shortcuts, or best practices to improve efficiency or avoid common errors.
- **Troubleshooting**: Address potential problems or challenges that readers might encounter and provide solutions or workarounds.
- **Safety Precautions**: Include safety warnings and precautions where applicable to prevent injury or damage.
- **Examples/Case Studies**: Provide real-world examples or case studies to demonstrate the application of the method and its benefits.
- **Conclusion**: Summarize the key steps and reinforce the benefits of following the instructions.
- **Call to Action**: Encourage the reader to try the method and provide a clear call to action.
- **Additional Resources**: Include a list of additional resources, such as websites, books, or videos, for further learning.
'''
        return base_prompt + how_to_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        how_to_additions = '''
## How-To-Specific Character Development
- **Expertise and Authority**: While not always necessary to have a "character" in the traditional sense, consider the persona of the guide. They should project expertise and authority in the subject matter.
- **Relatability and Empathy**: The guide should be relatable and empathetic to the reader's needs and challenges. They should understand the reader's perspective and offer encouragement and support.
- **Clarity and Communication**: The guide should be able to communicate complex information in a clear, concise, and easy-to-understand manner.
- **Patience and Understanding**: The guide should be patient and understanding, recognizing that readers may have different levels of experience and knowledge.
- **Enthusiasm and Passion**: The guide should be enthusiastic and passionate about the subject matter, inspiring readers to learn and try new things.
- **Accessibility and Approachability**: The guide should be accessible and approachable, making readers feel comfortable asking questions and seeking help.
'''
        return base_prompt + how_to_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        how_to_additions = '''
## How-To-Specific Chapter Writing
- **Clear Chapter Goal**: Each chapter should focus on a specific aspect or step of the overall process. Clearly state the goal of the chapter in the introduction.
- **Logical Flow**: Ensure a logical flow of information within the chapter, building upon previous steps and concepts.
- **Detailed Instructions**: Provide detailed, step-by-step instructions for each task or activity. Use clear and concise language, avoiding jargon or technical terms without explanation.
- **Visual Aids**: Integrate visual aids (images, diagrams, videos) to illustrate key steps or concepts. Provide clear captions and explanations for each visual.
- **Practical Tips**: Incorporate practical tips, shortcuts, or best practices to improve efficiency or avoid common errors.
- **Troubleshooting**: Address potential problems or challenges that readers might encounter and provide solutions or workarounds.
- **Safety Precautions**: Include safety warnings and precautions where applicable to prevent injury or damage.
- **Examples/Case Studies**: Provide real-world examples or case studies to demonstrate the application of the method and its benefits.
- **Chapter Summary**: Summarize the key steps and concepts covered in the chapter at the end.
- **Transition to Next Chapter**: Provide a smooth transition to the next chapter, highlighting the connection between the topics.
'''
        return base_prompt + how_to_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a howto-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        howto_series_additions = """

## HowTo Series-Specific Planning Elements

### Educational Progression for HowTo
- **Knowledge Building**: Structure learning progression appropriate for howto topics
- **Expertise Development**: Guide readers from basic to advanced understanding of howto subjects
- **Practical Applications**: Include actionable insights specific to howto throughout the series
- **Research Depth**: Plan comprehensive research appropriate for howto authority
- **Reader Value**: Ensure each book provides significant howto value while building series knowledge

### HowTo Series Continuity
- **Subject Consistency**: Maintain consistent approach to howto topics across books
- **Authority Building**: Establish and maintain credibility in howto throughout the series
- **Information Architecture**: Structure information flow appropriate for howto learning
- **Cross-References**: Create meaningful connections between howto concepts across books
- **Updated Knowledge**: Plan for incorporating new howto research and developments

Create a howto series that provides comprehensive education with authoritative, well-researched content.
"""
        
        return base_prompt + howto_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a howto-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        howto_book_additions = """

## HowTo Series Book Integration

### HowTo Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon howto concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous howto books when relevant
- **Knowledge Progression**: Advance reader understanding of howto topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the howto series

### Book-Specific HowTo Focus
- **Educational Objectives**: What specific howto knowledge will readers gain from this book?
- **Practical Applications**: What actionable howto insights will be provided?
- **Research Integration**: How will new howto research be incorporated?
- **Series Advancement**: How does this book advance the overall howto education series?
- **Reader Value**: What unique howto value does this book add to the series?

Ensure this book provides comprehensive howto education while serving as an integral part of the learning series.
"""
        
        return base_prompt + howto_book_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return HowToPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return HowToPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return HowToPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return HowToPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return HowToPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return HowToPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return HowToPrompts.get_series_book_prompt(**kwargs)
