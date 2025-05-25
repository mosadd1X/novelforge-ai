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

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a academic-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        academic_series_additions = """

## Academic Series-Specific Planning Elements

### Educational Progression for Academic
- **Knowledge Building**: Structure learning progression appropriate for academic topics
- **Expertise Development**: Guide readers from basic to advanced understanding of academic subjects
- **Practical Applications**: Include actionable insights specific to academic throughout the series
- **Research Depth**: Plan comprehensive research appropriate for academic authority
- **Reader Value**: Ensure each book provides significant academic value while building series knowledge

### Academic Series Continuity
- **Subject Consistency**: Maintain consistent approach to academic topics across books
- **Authority Building**: Establish and maintain credibility in academic throughout the series
- **Information Architecture**: Structure information flow appropriate for academic learning
- **Cross-References**: Create meaningful connections between academic concepts across books
- **Updated Knowledge**: Plan for incorporating new academic research and developments

Create a academic series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + academic_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a academic-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class AcademicBackCover:
        """
        A class containing methods for generating back cover copy and visual style preferences
        specifically tailored for the Academic genre.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for crafting compelling back cover descriptions for academic books.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., book_title, author_name,
        target_audience, key_arguments, related_works).

        Returns:
        A string containing a detailed prompt for generating back cover copy.
        """
        book_title = kwargs.get("book_title", "[Book Title]")
        author_name = kwargs.get("author_name", "[Author Name]")
        target_audience = kwargs.get("target_audience", "[Target Audience: e.g., upper-level undergraduates, graduate students, specialists in X field]")
        key_arguments = kwargs.get("key_arguments", "[Briefly list 3-5 key arguments or findings]")
        related_works = kwargs.get("related_works", "[Mention 2-3 influential works this book builds upon or challenges]")
        discipline = kwargs.get("discipline", "[Academic Discipline: e.g., History, Sociology, Literature]")
        methodology = kwargs.get("methodology", "[Methodology used: e.g., quantitative analysis, qualitative interviews, textual analysis]")
        impact = kwargs.get("impact", "[Potential impact of the book on the field]")
        thesis_statement = kwargs.get("thesis_statement", "[One-sentence summary of the book's central thesis]")

        prompt = f"""
        Craft a compelling back cover description for the academic book '{book_title}' by {author_name}.
        The target audience is {target_audience} within the field of {discipline}.

        **Focus:**
        *   Clearly articulate the book's central argument or thesis: {thesis_statement}.
        *   Highlight the significance and originality of the research. What new insights does it offer?
        *   Emphasize the book's rigorous methodology: {methodology}.
        *   Show how the book engages with existing scholarship, building upon {related_works} or offering a critical alternative.
        *   Explain the potential impact of the book on the field: {impact}.
        *   Concisely summarize the key arguments: {key_arguments}.
        *   Avoid overly simplistic language or jargon. Maintain a tone of intellectual authority and precision.

        **Structure:**
        1.  Start with a hook that grabs the reader's attention and establishes the book's relevance. Consider using a provocative question or a surprising statistic.
        2.  Clearly state the book's thesis or central argument.
        3.  Briefly outline the key arguments or findings.
        4.  Explain the methodology used and why it is appropriate for the research question.
        5.  Highlight the book's originality and contribution to the field.
        6.  Indicate the book's potential impact on future research and practice.
        7.  End with a call to action, encouraging readers to delve deeper into the subject matter.

        **Specific Instructions:**
        *   Keep the description concise (approximately 150-200 words).
        *   Use strong verbs and active voice.
        *   Proofread carefully for errors in grammar and spelling.
        *   Consider including a quote from a prominent scholar in the field (if available).
        *   Emphasize the book's intellectual rigor and scholarly value.

        **Tone:** Authoritative, insightful, engaging, and intellectually stimulating.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, impactful description (2-3 lines) for academic book recommendations.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., book_title, author_name, key_concept).

        Returns:
        A string containing a prompt for generating a short description.
        """
        book_title = kwargs.get("book_title", "[Book Title]")
        author_name = kwargs.get("author_name", "[Author Name]")
        key_concept = kwargs.get("key_concept", "[Key Concept or Argument]")
        discipline = kwargs.get("discipline", "[Academic Discipline]")

        prompt = f"""
        Create a concise (2-3 lines) description of the academic book '{book_title}' by {author_name} within the field of {discipline}.

        **Focus:**
        *   Highlight the book's core argument or contribution: {key_concept}.
        *   Emphasize its intellectual rigor and relevance to the field.
        *   Use precise language and avoid overly general statements.
        *   Target an audience of scholars and researchers.

        **Examples:**
        *   "A groundbreaking study that challenges conventional wisdom about [topic] and offers a fresh perspective on [related issue]."
        *   "An essential resource for anyone interested in [topic], providing a comprehensive analysis of [key concepts] and their implications for [field]."
        *   "This book offers a nuanced and insightful examination of [topic], drawing on [methodology] to shed new light on [issue]."

        **Tone:** Informative, authoritative, and intellectually stimulating.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for developing a punchy and memorable marketing tagline for an academic book.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., book_title, key_argument, target_audience).

        Returns:
        A string containing a prompt for generating a marketing tagline.
        """
        book_title = kwargs.get("book_title", "[Book Title]")
        key_argument = kwargs.get("key_argument", "[Key Argument]")
        target_audience = kwargs.get("target_audience", "[Target Audience]")
        discipline = kwargs.get("discipline", "[Academic Discipline]")

        prompt = f"""
        Develop a compelling marketing tagline for the academic book '{book_title}' within the field of {discipline}.

        **Focus:**
        *   Highlight the book's key argument or contribution: {key_argument}.
        *   Target the specific audience for the book: {target_audience}.
        *   Use concise and memorable language.
        *   Create a sense of intellectual curiosity and excitement.
        *   Taglines should be around 5-10 words.

        **Examples:**
        *   "[Book Title]: Redefining the landscape of [field]."
        *   "[Book Title]: Essential reading for scholars of [topic]."
        *   "[Book Title]: Unlocking the secrets of [key concept]."
        *   "[Book Title]: A groundbreaking analysis of [complex issue]."
        *   "[Book Title]: The definitive guide to [specific topic]."

        **Tone:** Provocative, insightful, and intellectually stimulating.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt outlining visual style preferences for the back cover design of an academic book.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., subject_matter, target_audience).

        Returns:
        A string containing a prompt for guiding the back cover visual design.
        """
        subject_matter = kwargs.get("subject_matter", "[Subject Matter]")
        target_audience = kwargs.get("target_audience", "[Target Audience]")
        discipline = kwargs.get("discipline", "[Academic Discipline]")

        prompt = f"""
        Outline visual style preferences for the back cover design of an academic book focused on {subject_matter} within the field of {discipline}, targeting {target_audience}.

        **Focus:**
        *   Convey a sense of intellectual authority and credibility.
        *   Maintain a clean, professional, and uncluttered appearance.
        *   Use a color palette that is sophisticated and visually appealing (e.g., blues, grays, greens, earth tones).
        *   Consider using a relevant image or graphic that reflects the book's subject matter, but avoid overly literal or simplistic representations.
        *   Typography should be clear, legible, and appropriate for academic writing (e.g., serif or sans-serif fonts).
        *   Avoid overly flashy or distracting design elements.
        *   The design should be consistent with the book's overall tone and content.

        **Specific Considerations:**
        *   For books in the humanities, consider using images of historical artifacts, works of art, or landscapes.
        *   For books in the social sciences, consider using charts, graphs, or photographs of people or places.
        *   For books in the sciences, consider using diagrams, illustrations, or photographs of scientific phenomena.
        *   The design should be visually appealing to scholars and researchers.

        **Overall Impression:**  Sophisticated, intellectual, credible, and visually engaging.
        """
        return prompt
        ```
        academic_book_additions = """

## Academic Series Book Integration

### Academic Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon academic concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous academic books when relevant
- **Knowledge Progression**: Advance reader understanding of academic topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the academic series

### Book-Specific Academic Focus
- **Educational Objectives**: What specific academic knowledge will readers gain from this book?
- **Practical Applications**: What actionable academic insights will be provided?
- **Research Integration**: How will new academic research be incorporated?
- **Series Advancement**: How does this book advance the overall academic education series?
- **Reader Value**: What unique academic value does this book add to the series?

Ensure this book provides comprehensive academic education while serving as an integral part of the learning series.
"""

        return base_prompt + academic_book_additions

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
def get_series_plan_prompt(**kwargs) -> str:
    return AcademicPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return AcademicPrompts.get_series_book_prompt(**kwargs)
