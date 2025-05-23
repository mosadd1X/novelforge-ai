"""
Philosophy genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class PhilosophyPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Philosophy"
    GENRE_DESCRIPTION = "Philosophy explores fundamental questions about existence, knowledge, values, reason, mind, and language. It often involves critical thinking, logical argumentation, and conceptual analysis to develop coherent and justified perspectives on these questions. Philosophical works can range from abstract theoretical treatises to practical ethical guides."
    
    GENRE_CHARACTERISTICS = [
        "Rigorous argumentation: Claims are supported by logical reasoning and evidence.",
        "Conceptual clarity: Terms and concepts are precisely defined and consistently used.",
        "Critical analysis: Assumptions and presuppositions are questioned and examined.",
        "Exploration of fundamental questions: Addresses core issues about reality, knowledge, morality, and meaning.",
        "Systematic thinking: Ideas are organized into coherent and comprehensive frameworks.",
        "Abstract reasoning: Deals with abstract concepts and theoretical models.",
        "Ethical considerations: Explores moral principles, values, and their implications.",
        "Epistemological inquiry: Investigates the nature, scope, and limits of knowledge.",
        "Metaphysical speculation: Considers the nature of being, existence, and reality.",
        "Dialectical approach: Presents and evaluates opposing viewpoints to arrive at a more nuanced understanding."
    ]
    
    TYPICAL_ELEMENTS = [
        "Thesis statement: A clear and concise statement of the main argument or position.",
        "Premises: Supporting statements or assumptions that lead to a conclusion.",
        "Arguments: Logical reasoning used to support the thesis, often employing deductive or inductive reasoning.",
        "Counterarguments: Addressing and refuting opposing viewpoints.",
        "Thought experiments: Hypothetical scenarios used to illustrate or test philosophical concepts.",
        "Definitions: Precise explanations of key terms and concepts.",
        "Examples: Concrete instances used to clarify abstract ideas.",
        "Analogies: Comparisons used to highlight similarities between different concepts or situations.",
        "Conceptual analysis: Breaking down complex concepts into their constituent parts.",
        "Historical context: Referencing and engaging with previous philosophical works and thinkers.",
        "Ethical dilemmas: Presenting complex moral situations with conflicting values.",
        "Critiques: Identifying and evaluating weaknesses in existing philosophical theories."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        philosophy_additions = '''
## Philosophy-Specific Writing Considerations
- **Argumentative Rigor**: Ensure all claims are supported by sound reasoning and evidence. Avoid logical fallacies and unsubstantiated assertions.
- **Conceptual Precision**: Define key terms clearly and use them consistently throughout the work. Be aware of potential ambiguities and address them explicitly.
- **Historical Awareness**: Demonstrate familiarity with relevant philosophical traditions and thinkers. Acknowledge and engage with existing scholarship.
- **Critical Self-Reflection**: Be aware of your own biases and assumptions. Critically examine your own arguments and be open to alternative perspectives.
- **Clarity of Expression**: Write in a clear and concise style, avoiding jargon and overly complex sentence structures. Aim for accessibility without sacrificing intellectual depth.
- **Engagement with Counterarguments**: Anticipate and address potential objections to your arguments. Demonstrate a willingness to engage with opposing viewpoints.
- **Ethical Responsibility**: Consider the ethical implications of your ideas and arguments. Avoid promoting harmful or discriminatory views.
- **Originality and Insight**: Strive to offer novel perspectives and insights on philosophical questions. Contribute to the ongoing conversation in a meaningful way.
'''
        return base_prompt + philosophy_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        philosophy_additions = '''
## Philosophy-Specific Outline Requirements
- **Introduction (Thesis Statement)**: Clearly state the central argument or thesis of the philosophical work. Provide a brief overview of the topics to be covered.
- **Background and Context**: Introduce the relevant philosophical background and historical context. Explain the significance of the problem or question being addressed.
- **Definition of Terms**: Define key terms and concepts that will be used throughout the work. Ensure clarity and consistency in their usage.
- **Presentation of Arguments**: Develop a series of logical arguments to support the thesis. Each argument should be presented in a clear and structured manner, with premises and conclusions.
- **Analysis of Counterarguments**: Address and refute potential objections to the arguments. Demonstrate a thorough understanding of opposing viewpoints.
- **Development of Thought Experiments (Optional)**: Include thought experiments to illustrate or test philosophical concepts. Explain the implications of the thought experiment for the argument.
- **Consideration of Ethical Implications**: Explore the ethical implications of the philosophical position. Discuss the potential consequences of adopting the proposed view.
- **Conclusion (Restatement and Implications)**: Restate the thesis and summarize the main arguments. Discuss the broader implications of the philosophical work and suggest avenues for further research.
- **Logical Flow**: Ensure a clear and logical flow of ideas throughout the outline. Each section should build upon the previous one, leading to a coherent and well-supported conclusion.
- **Balance**: Allocate sufficient space to each section of the outline, ensuring that all key arguments and counterarguments are adequately addressed.
'''
        return base_prompt + philosophy_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        philosophy_additions = '''
## Philosophy-Specific Character Development
- **Intellectual Curiosity**: Characters should possess a strong desire to understand the world and explore fundamental questions.
- **Critical Thinking Skills**: Characters should be able to analyze information, identify assumptions, and evaluate arguments.
- **Moral Compass**: Characters should grapple with ethical dilemmas and strive to act in accordance with their values.
- **Open-Mindedness**: Characters should be willing to consider alternative perspectives and challenge their own beliefs.
- **Dialogue and Debate**: Characters should engage in philosophical discussions and debates, presenting and defending their ideas.
- **Internal Conflict**: Characters should experience internal conflict as they grapple with complex philosophical issues.
- **Impact on Others**: Characters' philosophical beliefs and actions should have a significant impact on the lives of others.
- **Flaws and Limitations**: Characters should have flaws and limitations that make them relatable and human.
'''
        return base_prompt + philosophy_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        philosophy_additions = '''
## Philosophy-Specific Chapter Writing
- **Clear Thesis Statement**: Each chapter should have a clear thesis statement that outlines the main argument or point being made.
- **Logical Structure**: The chapter should be organized in a logical and coherent manner, with clear transitions between sections.
- **Rigorous Argumentation**: All claims should be supported by sound reasoning and evidence. Avoid logical fallacies and unsubstantiated assertions.
- **Conceptual Clarity**: Define key terms clearly and use them consistently throughout the chapter.
- **Engagement with Existing Literature**: Refer to and engage with relevant philosophical works and thinkers.
- **Analysis of Counterarguments**: Address and refute potential objections to the arguments presented in the chapter.
- **Use of Examples and Analogies**: Use examples and analogies to illustrate abstract concepts and make them more accessible to the reader.
- **Consideration of Ethical Implications**: Explore the ethical implications of the philosophical position being presented.
- **Concluding Summary**: Each chapter should end with a summary of the main points and a transition to the next chapter.
- **Precise Language**: Use precise and unambiguous language to avoid misinterpretations.
'''
        return base_prompt + philosophy_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return PhilosophyPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return PhilosophyPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return PhilosophyPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return PhilosophyPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return PhilosophyPrompts.get_enhancement_prompt(**kwargs)