"""
Academic genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class AcademicPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Academic"
    GENRE_DESCRIPTION = "Academic writing is a style of expression that researchers use to define the intellectual boundaries of their disciplines and specific areas of expertise. It is characterized by its rigor, precision, objectivity, and adherence to specific conventions of citation and argumentation. Academic writing aims to inform, persuade, and contribute to the existing body of knowledge within a particular field."
    
    GENRE_CHARACTERISTICS = [
        "Formal Tone: Employs a serious, objective, and impersonal tone, avoiding colloquialisms, slang, and subjective language.",
        "Precise Language: Uses specific and unambiguous terminology, defining key concepts and avoiding vague or overly general statements.",
        "Evidence-Based Reasoning: Supports claims with credible evidence, including empirical data, scholarly research, and established theories.",
        "Logical Organization: Presents information in a clear, coherent, and logical manner, typically following a structured format such as introduction, literature review, methodology, results, discussion, and conclusion.",
        "Objective Perspective: Maintains an objective viewpoint, minimizing personal opinions and biases, and acknowledging alternative perspectives.",
        "Proper Citation: Accurately cites all sources of information using a consistent citation style (e.g., APA, MLA, Chicago) to avoid plagiarism and give credit to original authors.",
        "Critical Analysis: Engages in critical evaluation of existing research, identifying strengths, weaknesses, and gaps in the literature.",
        "Scholarly Rigor: Adheres to the standards of scholarly research, including rigorous methodology, data analysis, and interpretation.",
        "Focus on Argumentation: Presents a clear and well-supported argument or thesis statement, providing evidence and reasoning to persuade the reader.",
        "Contribution to Knowledge: Aims to contribute to the existing body of knowledge within a specific field, either by presenting new findings, offering novel interpretations, or synthesizing existing research."
    ]
    
    TYPICAL_ELEMENTS = [
        "Abstract: A concise summary of the research, including the purpose, methods, results, and conclusions.",
        "Introduction: Provides background information, defines the research problem, states the thesis statement, and outlines the scope of the study.",
        "Literature Review: Critically analyzes existing research on the topic, identifying key themes, debates, and gaps in the literature.",
        "Methodology: Describes the research methods used to collect and analyze data, including the sample, instruments, and procedures.",
        "Results: Presents the findings of the research in a clear and objective manner, using tables, figures, and statistical analysis.",
        "Discussion: Interprets the results of the research, relating them to the existing literature and discussing their implications.",
        "Conclusion: Summarizes the main findings of the research, draws conclusions, and suggests directions for future research.",
        "References/Bibliography: Lists all sources cited in the paper, following a specific citation style.",
        "Appendices: Includes supplementary materials, such as questionnaires, interview transcripts, or detailed statistical analyses.",
        "Figures and Tables: Visual representations of data that enhance understanding and support the research findings.",
        "Footnotes/Endnotes: Provide additional information or clarification that is not essential to the main text.",
        "Keywords: A list of relevant terms that describe the research topic and facilitate indexing and retrieval."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        academic_additions = '''
## Academic-Specific Writing Considerations
- **Scholarly Authority**: Establish credibility by demonstrating a deep understanding of the relevant literature and research methodologies. Cite sources meticulously and accurately.
- **Conceptual Clarity**: Define key terms and concepts precisely to avoid ambiguity. Ensure that your arguments are logically sound and easy to follow.
- **Methodological Rigor**: Describe your research methods in detail, including the rationale for your choices, the procedures you followed, and any limitations of your approach.
- **Data Interpretation**: Analyze your data objectively and critically. Avoid overstating your findings or drawing conclusions that are not supported by the evidence.
- **Ethical Considerations**: Adhere to ethical guidelines for research, including informed consent, confidentiality, and data security.
- **Audience Awareness**: Tailor your writing to the specific audience you are trying to reach. Consider their level of expertise and their familiarity with the topic.
- **Peer Review**: Be prepared to submit your work for peer review and to revise it based on the feedback you receive.
- **Contribution to the Field**: Clearly articulate how your research contributes to the existing body of knowledge and what implications it has for future research or practice.
'''
        return base_prompt + academic_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        academic_additions = '''
## Academic-Specific Outline Requirements
- **Introduction Structure**: Begin with a broad overview of the topic, narrowing down to the specific research question or thesis statement. Clearly state the purpose and scope of the study.
- **Literature Review Organization**: Organize the literature review thematically or chronologically, highlighting key debates and identifying gaps in the research.
- **Methodology Detail**: Provide a detailed description of the research design, sample, data collection methods, and data analysis techniques.
- **Results Presentation**: Present the findings in a clear and concise manner, using tables, figures, and statistical analysis to support your claims.
- **Discussion Depth**: Interpret the results in relation to the existing literature, discussing their implications for theory and practice. Acknowledge any limitations of the study.
- **Conclusion Summary**: Summarize the main findings, draw conclusions, and suggest directions for future research. Emphasize the contribution of the study to the field.
- **Logical Flow**: Ensure a logical flow of ideas throughout the paper, with clear transitions between sections and paragraphs.
- **Consistent Formatting**: Adhere to a consistent formatting style (e.g., APA, MLA, Chicago) for headings, subheadings, citations, and references.
'''
        return base_prompt + academic_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        academic_additions = '''
## Academic-Specific Character Development
- **Researcher Profile**: If applicable, develop characters (e.g., researchers, subjects) with realistic motivations, backgrounds, and perspectives related to the research topic.
- **Ethical Considerations in Character Portrayal**: Ensure that the portrayal of characters adheres to ethical guidelines, protecting their privacy and avoiding stereotypes.
- **Expertise and Knowledge**: Depict characters with appropriate levels of expertise and knowledge in their respective fields.
- **Bias and Objectivity**: Explore how characters' biases and perspectives might influence their research or interpretations.
- **Collaboration and Conflict**: Illustrate the dynamics of collaboration and conflict among researchers, highlighting the challenges and rewards of teamwork.
- **Impact of Research on Characters**: Show how the research process and findings affect the characters' lives, beliefs, or careers.
'''
        return base_prompt + academic_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        academic_additions = '''
## Academic-Specific Chapter Writing
- **Introduction Chapter**: Clearly state the research question, thesis statement, and scope of the study. Provide background information and context for the research.
- **Literature Review Chapter**: Critically analyze existing research on the topic, identifying key themes, debates, and gaps in the literature.
- **Methodology Chapter**: Describe the research design, sample, data collection methods, and data analysis techniques in detail.
- **Results Chapter**: Present the findings of the research in a clear and objective manner, using tables, figures, and statistical analysis to support your claims.
- **Discussion Chapter**: Interpret the results in relation to the existing literature, discussing their implications for theory and practice. Acknowledge any limitations of the study.
- **Conclusion Chapter**: Summarize the main findings, draw conclusions, and suggest directions for future research. Emphasize the contribution of the study to the field.
- **Clarity and Precision**: Use precise language and avoid jargon or ambiguous terms. Define key concepts and provide clear explanations.
- **Evidence-Based Arguments**: Support all claims with credible evidence from scholarly sources. Cite sources accurately and consistently.
'''
        return base_prompt + academic_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return AcademicPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return AcademicPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return AcademicPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return AcademicPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return AcademicPrompts.get_enhancement_prompt(**kwargs)