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


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a philosophy-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        philosophy_series_additions = """

## Philosophy Series-Specific Planning Elements

### Educational Progression for Philosophy
- **Knowledge Building**: Structure learning progression appropriate for philosophy topics
- **Expertise Development**: Guide readers from basic to advanced understanding of philosophy subjects
- **Practical Applications**: Include actionable insights specific to philosophy throughout the series
- **Research Depth**: Plan comprehensive research appropriate for philosophy authority
- **Reader Value**: Ensure each book provides significant philosophy value while building series knowledge

### Philosophy Series Continuity
- **Subject Consistency**: Maintain consistent approach to philosophy topics across books
- **Authority Building**: Establish and maintain credibility in philosophy throughout the series
- **Information Architecture**: Structure information flow appropriate for philosophy learning
- **Cross-References**: Create meaningful connections between philosophy concepts across books
- **Updated Knowledge**: Plan for incorporating new philosophy research and developments

Create a philosophy series that provides comprehensive education with authoritative, well-researched content.
"""
        
        return base_prompt + philosophy_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a philosophy-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        philosophy_book_additions = """

## Philosophy Series Book Integration

### Philosophy Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon philosophy concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous philosophy books when relevant
- **Knowledge Progression**: Advance reader understanding of philosophy topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the philosophy series

### Book-Specific Philosophy Focus
- **Educational Objectives**: What specific philosophy knowledge will readers gain from this book?
- **Practical Applications**: What actionable philosophy insights will be provided?
- **Research Integration**: How will new philosophy research be incorporated?
- **Series Advancement**: How does this book advance the overall philosophy education series?
- **Reader Value**: What unique philosophy value does this book add to the series?

Ensure this book provides comprehensive philosophy education while serving as an integral part of the learning series.
"""
        
        return base_prompt + philosophy_book_additions

        ```python
        class PhilosophyBackCover:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for crafting compelling back cover copy for a Philosophy book.

        Args:
        **kwargs:  Keyword arguments to customize the prompt (e.g., target_audience, book_theme).

        Returns:
        str: A prompt string tailored for generating Philosophy back cover descriptions.
        """
        target_audience = kwargs.get('target_audience', 'General readers interested in philosophical inquiry')
        book_theme = kwargs.get('book_theme', 'The nature of consciousness and existence')
        author_expertise = kwargs.get('author_expertise', 'Expert in existential phenomenology')
        key_concepts = kwargs.get('key_concepts', 'Being, Nothingness, Subjectivity, Objectivity')
        philosophical_school = kwargs.get('philosophical_school', 'Existentialism')
        emotional_hook = kwargs.get('emotional_hook', 'The search for meaning in a seemingly absurd world')

        prompt = f"""
        Write a compelling and thought-provoking back cover description for a Philosophy book.

        **Genre:** Philosophy

        **Target Audience:** {target_audience}

        **Book Theme:** {book_theme}

        **Author Expertise:** {author_expertise}

        **Key Philosophical Concepts:** {key_concepts}

        **Philosophical School/Movement:** {philosophical_school}

        **Emotional Hook:** {emotional_hook}

        **Guidelines:**

        *   **Engage the Reader's Intellect:** Philosophy readers are driven by curiosity and a desire to understand complex ideas. Pose questions that challenge their assumptions and invite them to explore new perspectives.

        *   **Highlight the Book's Unique Contribution:**  What makes this book stand out from other philosophical works on the same topic? Does it offer a new interpretation, a novel argument, or a fresh application of existing theories?

        *   **Emphasize the Practical Relevance (if applicable):** While Philosophy often deals with abstract concepts, connect the ideas to real-world concerns and show how they can impact the reader's life, understanding of society, or ethical decision-making.

        *   **Use Clear and Accessible Language (while maintaining intellectual rigor):** Avoid overly technical jargon unless the target audience is exclusively academic. Strive for clarity and precision in your writing.

        *   **Incorporate a Sense of Wonder and Awe:** Philosophy at its best can inspire a sense of wonder about the universe and our place within it. Capture this feeling in your description.

        *   **Consider the Tone:**  The tone should be intelligent, thoughtful, and engaging. Avoid being preachy or condescending.

        *   **Include a Hook:** Start with a captivating question, a provocative statement, or a brief anecdote that grabs the reader's attention.

        *   **Mention the Author's Credentials Briefly:** Highlight the author's expertise without being overly boastful.

        *   **End with a Call to Action:** Encourage the reader to delve into the book and embark on a philosophical journey.

        *   **Consider these questions when writing the description:**
        * What fundamental questions about existence, knowledge, values, reason, mind, and language does this book address?
        * What are the key arguments and insights presented in the book?
        * How does this book challenge conventional wisdom or offer a new perspective on familiar problems?
        * What are the potential implications of the book's ideas for the reader's understanding of the world?

        **Example Start:**
        "What if everything you thought you knew about [philosophical concept] was wrong?..."

        **Example End:**
        "Prepare to have your assumptions challenged and your understanding of reality transformed."
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, impactful description (2-3 lines) for Philosophy book recommendations.

        Args:
        **kwargs: Keyword arguments for customization (e.g., book_theme, target_audience).

        Returns:
        str: A prompt string for generating concise Philosophy book descriptions.
        """
        book_theme = kwargs.get('book_theme', 'The ethics of artificial intelligence')
        target_audience = kwargs.get('target_audience', 'Readers interested in technology and its implications')
        philosophical_school = kwargs.get('philosophical_school', 'Utilitarianism and Deontology')

        prompt = f"""
        Write a very short (2-3 lines) description of a Philosophy book for a recommendation list.

        **Genre:** Philosophy

        **Book Theme:** {book_theme}

        **Target Audience:** {target_audience}

        **Philosophical School/Movement:** {philosophical_school}

        **Guidelines:**

        *   **Focus on the Core Idea:** Distill the book's central argument or theme into a single, compelling sentence.
        *   **Highlight the Relevance:** Briefly explain why this book is important or interesting to the target audience.
        *   **Use Strong Verbs and Concise Language:** Every word should count.
        *   **End with a Hook:** Leave the reader wanting to know more.
        *   **Emphasize the Thought-Provoking Nature:** Philosophy should make you think.

        **Example:**
        "A groundbreaking exploration of [philosophical concept] that will challenge your assumptions about [related topic]."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for crafting a punchy and memorable marketing tagline for a Philosophy book.

        Args:
        **kwargs: Keyword arguments to customize the prompt (e.g., book_theme, key_concept).

        Returns:
        str: A prompt string for generating catchy Philosophy marketing taglines.
        """
        book_theme = kwargs.get('book_theme', 'The problem of free will')
        key_concept = kwargs.get('key_concept', 'Determinism vs. Libertarianism')
        target_audience = kwargs.get('target_audience', 'Anyone questioning their choices')

        prompt = f"""
        Write a short, punchy, and memorable marketing tagline for a Philosophy book.

        **Genre:** Philosophy

        **Book Theme:** {book_theme}

        **Key Concept:** {key_concept}

        **Target Audience:** {target_audience}

        **Guidelines:**

        *   **Keep it Short and Sweet:** Aim for a tagline that is easy to remember and repeat.
        *   **Highlight the Central Question:** Philosophy is often about asking big questions.
        *   **Provoke Curiosity:** Make the reader want to know more.
        *   **Emphasize the Transformative Potential:** Philosophy can change the way we see the world.
        *   **Use Strong Language:** Verbs and nouns should be impactful.
        *   **Consider a Rhetorical Question:** This can be a very effective way to engage the reader.

        **Examples:**

        *   "Do you really have a choice?"
        *   "Question Everything."
        *   "Unlock the Secrets of Existence."
        *   "The Philosophy That Will Change Your Life."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt outlining visual style preferences for the back cover design of a Philosophy book.

        Args:
        **kwargs: Keyword arguments to specify visual elements and design themes.

        Returns:
        str: A prompt string describing visual style preferences for Philosophy book covers.
        """
        book_theme = kwargs.get('book_theme', 'The nature of reality')
        philosophical_school = kwargs.get('philosophical_school', 'Idealism')
        desired_mood = kwargs.get('desired_mood', 'Intriguing and thought-provoking')

        prompt = f"""
        Describe the desired visual style for the back cover of a Philosophy book.

        **Genre:** Philosophy

        **Book Theme:** {book_theme}

        **Philosophical School/Movement (Influence):** {philosophical_school}

        **Desired Mood:** {desired_mood}

        **Visual Elements:**

        *   **Imagery:** Consider abstract imagery, symbolic representations, or thought-provoking visuals that relate to the book's theme.  Avoid literal depictions unless they are highly symbolic. Think about using images related to:
        *   Metaphysics: Abstract concepts like time, space, and existence.
        *   Epistemology: The nature of knowledge, perception, and truth.
        *   Ethics: Moral dilemmas, justice, and the good life.
        *   Logic: Reasoning, arguments, and patterns.

        *   **Typography:** Choose a font that is clean, readable, and conveys a sense of intelligence and sophistication. Serif fonts can suggest tradition and authority, while sans-serif fonts can convey modernity and clarity.

        *   **Color Palette:** Use a color palette that reflects the book's mood and theme.  Consider:
        *   Dark and muted tones:  Suggest mystery, depth, and seriousness.
        *   Light and airy tones: Suggest clarity, enlightenment, and hope.
        *   Contrasting colors:  Highlight key concepts and create visual interest.

        *   **Layout:** The layout should be clean, uncluttered, and easy to read. Use whitespace effectively to create a sense of balance and order.

        **Overall Aesthetic:**

        The overall aesthetic should be intelligent, thought-provoking, and visually appealing.  Avoid being overly flashy or sensational. The design should complement the intellectual content of the book and appeal to readers who are interested in philosophical inquiry. Consider the historical period of the philosophy discussed. A book on ancient Greek philosophy might benefit from classical design elements.

        **Examples:**

        *   Abstract geometric patterns with a muted color palette.
        *   A single, symbolic image with a clean, minimalist layout.
        *   A portrait of a historical philosopher with a modern twist.
        """
        return prompt
        ```
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
def get_series_plan_prompt(**kwargs) -> str:
    return PhilosophyPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return PhilosophyPrompts.get_series_book_prompt(**kwargs)
