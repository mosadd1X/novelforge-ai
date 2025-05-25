"""
Popular Science genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class PopularSciencePrompts(NonFictionBasePrompts):
    GENRE_NAME = "Popular Science"
    GENRE_DESCRIPTION = "Popular science writing aims to make scientific topics accessible and engaging to a general audience. It bridges the gap between complex scientific research and the everyday reader, fostering scientific literacy and curiosity. The genre prioritizes clarity, accuracy, and compelling storytelling to convey scientific concepts in an understandable and enjoyable manner."
    
    GENRE_CHARACTERISTICS = [
        "Clarity and Accessibility: Uses simple language and avoids jargon to explain complex scientific concepts.",
        "Accuracy and Reliability: Presents scientifically accurate information, often drawing from peer-reviewed research and expert sources.",
        "Engaging Narrative: Employs storytelling techniques, anecdotes, and real-world examples to capture the reader's interest.",
        "Contextualization: Connects scientific concepts to everyday life, history, or current events to demonstrate their relevance.",
        "Visual Aids: Incorporates diagrams, illustrations, and photographs to enhance understanding and engagement.",
        "Explanation of Scientific Method: Often explains the process of scientific inquiry, including hypothesis formation, experimentation, and data analysis.",
        "Exploration of Implications: Discusses the potential implications of scientific discoveries for society, technology, and the environment.",
        "Enthusiasm and Passion: Conveys the author's genuine interest in the subject matter, inspiring curiosity in the reader.",
        "Ethical Considerations: Addresses ethical dilemmas and controversies related to scientific advancements.",
        "Future Outlook: Speculates on future developments and potential breakthroughs in the field."
    ]
    
    TYPICAL_ELEMENTS = [
        "Introduction of a Scientific Concept: Clearly defines the scientific concept being explored.",
        "Historical Background: Provides context by tracing the history of the concept's development.",
        "Explanation of Key Principles: Breaks down the concept into its fundamental principles and components.",
        "Real-World Examples: Illustrates the concept with concrete examples from everyday life or relevant applications.",
        "Analogies and Metaphors: Uses analogies and metaphors to simplify complex ideas.",
        "Visual Representations: Includes diagrams, charts, or illustrations to aid understanding.",
        "Expert Interviews: Features quotes or insights from leading scientists in the field.",
        "Case Studies: Presents detailed case studies to demonstrate the concept in action.",
        "Ethical Considerations: Discusses the ethical implications of the concept or its applications.",
        "Future Directions: Explores potential future developments and research avenues.",
        "Glossary of Terms: Provides a glossary of key scientific terms for easy reference.",
        "Further Reading: Suggests additional resources for readers who want to learn more."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        popular_science_additions = '''
## Popular Science-Specific Writing Considerations
- **Accuracy and Fact-Checking**: Ensure all scientific information is accurate and verifiable through reputable sources. Prioritize peer-reviewed research and consult with experts in the field.
- **Clarity and Simplicity**: Use clear, concise language and avoid jargon. Break down complex concepts into smaller, more manageable pieces. Employ analogies and metaphors to aid understanding.
- **Engaging Storytelling**: Craft a compelling narrative that captures the reader's attention. Use anecdotes, real-world examples, and relatable scenarios to illustrate scientific concepts.
- **Visual Communication**: Incorporate visual aids such as diagrams, illustrations, and photographs to enhance understanding and engagement. Ensure visuals are clear, accurate, and relevant to the text.
- **Ethical Responsibility**: Address the ethical implications of scientific advancements and potential controversies. Present a balanced perspective and encourage critical thinking.
- **Target Audience Awareness**: Tailor the writing style and level of detail to the intended audience. Consider their prior knowledge and interests when selecting topics and examples.
- **Maintaining Reader Interest**: Vary sentence structure, use active voice, and incorporate humor or personal anecdotes to keep the reader engaged. Avoid overly technical language or dense paragraphs.
- **Source Citation**: Properly cite all sources of information, including research papers, books, and websites. Use a consistent citation style and provide a bibliography or list of references.
'''
        return base_prompt + popular_science_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        popular_science_additions = '''
## Popular Science-Specific Outline Requirements
- **Introduction of the Core Concept**: Begin with a clear and concise introduction of the central scientific concept. State its significance and relevance to the reader's life.
- **Historical Context and Discovery**: Provide a brief history of the concept's discovery and development. Highlight key figures and milestones in its evolution.
- **Explanation of Underlying Principles**: Break down the concept into its fundamental principles and components. Use simple language and avoid jargon.
- **Real-World Applications and Examples**: Illustrate the concept with concrete examples from everyday life, technology, or current events. Show how it impacts the reader's world.
- **Supporting Evidence and Research**: Present scientific evidence and research findings that support the concept. Cite reputable sources and explain the methodology used.
- **Potential Implications and Future Directions**: Discuss the potential implications of the concept for society, technology, and the environment. Explore future research avenues and potential breakthroughs.
- **Ethical Considerations and Controversies**: Address any ethical dilemmas or controversies associated with the concept. Present different perspectives and encourage critical thinking.
- **Visual Aids and Illustrations**: Plan for the inclusion of diagrams, charts, and illustrations to enhance understanding and engagement.
- **Conclusion and Summary**: Summarize the key points of the chapter and reiterate the significance of the concept. Leave the reader with a sense of wonder and curiosity.
- **Call to Action (Optional)**: Encourage the reader to explore the topic further, conduct their own research, or apply the concept in their own life.
'''
        return base_prompt + popular_science_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        popular_science_additions = '''
## Popular Science-Specific Character Development
- **Expertise and Authority**: Characters should possess a credible level of expertise in the scientific field being discussed. This could be through formal education, research experience, or practical application.
- **Passion and Enthusiasm**: Characters should demonstrate a genuine passion for science and a desire to share their knowledge with others. Their enthusiasm should be contagious and inspire curiosity in the reader.
- **Communication Skills**: Characters should be able to communicate complex scientific concepts in a clear, concise, and engaging manner. They should be adept at using analogies, metaphors, and real-world examples to aid understanding.
- **Relatability and Approachability**: Characters should be relatable and approachable to the general reader. They should be able to connect with the audience on a personal level and avoid coming across as condescending or aloof.
- **Ethical Integrity**: Characters should demonstrate a strong sense of ethical integrity and a commitment to responsible scientific conduct. They should be transparent about their methods and motivations.
- **Curiosity and Open-Mindedness**: Characters should be curious and open-minded, always seeking new knowledge and challenging existing assumptions. They should be willing to consider alternative perspectives and embrace uncertainty.
- **Storytelling Ability**: Characters should be able to weave compelling narratives that bring scientific concepts to life. They should be able to use anecdotes, personal experiences, and historical accounts to engage the reader's imagination.
- **Humility and Self-Awareness**: Characters should be humble and self-aware, acknowledging the limitations of their knowledge and the potential for error. They should be willing to admit when they are wrong and learn from their mistakes.
'''
        return base_prompt + popular_science_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        popular_science_additions = '''
## Popular Science-Specific Chapter Writing
- **Start with a Hook**: Begin the chapter with an engaging hook that grabs the reader's attention. This could be a surprising statistic, a thought-provoking question, a compelling anecdote, or a real-world example.
- **Clearly Define the Core Concept**: Clearly define the central scientific concept that the chapter will explore. State its significance and relevance to the reader's life.
- **Provide Context and Background**: Provide historical context and background information to help the reader understand the concept's origins and evolution.
- **Break Down Complex Ideas**: Break down complex scientific ideas into smaller, more manageable pieces. Use simple language and avoid jargon.
- **Use Analogies and Metaphors**: Employ analogies and metaphors to help the reader visualize and understand abstract concepts.
- **Incorporate Visual Aids**: Incorporate visual aids such as diagrams, charts, and illustrations to enhance understanding and engagement.
- **Tell Stories and Use Examples**: Tell stories and use real-world examples to illustrate the concept in action. Show how it impacts the reader's world.
- **Cite Sources and Evidence**: Cite reputable sources and evidence to support your claims. Explain the methodology used in scientific studies.
- **Address Counterarguments and Criticisms**: Acknowledge and address any counterarguments or criticisms related to the concept. Present a balanced perspective.
- **Conclude with a Summary and Takeaway**: Conclude the chapter with a summary of the key points and a clear takeaway message. Leave the reader with a sense of understanding and appreciation for the concept.
- **Maintain a Conversational Tone**: Write in a conversational tone that is engaging and accessible to the general reader. Avoid sounding overly academic or technical.
- **End with a Question or Challenge**: End the chapter with a question or challenge that encourages the reader to think critically about the concept and its implications.
'''
        return base_prompt + popular_science_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a popularscience-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        popularscience_series_additions = """

## PopularScience Series-Specific Planning Elements

### Educational Progression for PopularScience
- **Knowledge Building**: Structure learning progression appropriate for popularscience topics
- **Expertise Development**: Guide readers from basic to advanced understanding of popularscience subjects
- **Practical Applications**: Include actionable insights specific to popularscience throughout the series
- **Research Depth**: Plan comprehensive research appropriate for popularscience authority
- **Reader Value**: Ensure each book provides significant popularscience value while building series knowledge

### PopularScience Series Continuity
- **Subject Consistency**: Maintain consistent approach to popularscience topics across books
- **Authority Building**: Establish and maintain credibility in popularscience throughout the series
- **Information Architecture**: Structure information flow appropriate for popularscience learning
- **Cross-References**: Create meaningful connections between popularscience concepts across books
- **Updated Knowledge**: Plan for incorporating new popularscience research and developments

Create a popularscience series that provides comprehensive education with authoritative, well-researched content.
"""
        
        return base_prompt + popularscience_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a popularscience-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        popularscience_book_additions = """

## PopularScience Series Book Integration

### PopularScience Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon popularscience concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous popularscience books when relevant
- **Knowledge Progression**: Advance reader understanding of popularscience topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the popularscience series

### Book-Specific PopularScience Focus
- **Educational Objectives**: What specific popularscience knowledge will readers gain from this book?
- **Practical Applications**: What actionable popularscience insights will be provided?
- **Research Integration**: How will new popularscience research be incorporated?
- **Series Advancement**: How does this book advance the overall popularscience education series?
- **Reader Value**: What unique popularscience value does this book add to the series?

Ensure this book provides comprehensive popularscience education while serving as an integral part of the learning series.
"""
        
        return base_prompt + popularscience_book_additions

        ```python
        class PopularScienceMarketing:
        """
        A class containing methods for generating marketing materials,
        specifically back cover copy, for Popular Science books.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions
        for Popular Science books.

        Args:
        **kwargs: Keyword arguments that might include information like:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - key_concepts (list): A list of the key scientific concepts covered.
        - target_audience (str): Description of the target audience (e.g., general readers, students).
        - author_credentials (str): Brief summary of the author's expertise.
        - book_summary (str): A brief summary of the book's content.
        - unique_selling_proposition (str): What makes this book different?

        Returns:
        str: A detailed prompt string for AI-powered back cover copy generation.
        """

        title = kwargs.get('title', 'The Book')
        author = kwargs.get('author', 'The Author')
        key_concepts = kwargs.get('key_concepts', ['Science', 'Technology'])
        target_audience = kwargs.get('target_audience', 'General Readers')
        author_credentials = kwargs.get('author_credentials', 'Expert in the field')
        book_summary = kwargs.get('book_summary', 'A fascinating journey through science.')
        unique_selling_proposition = kwargs.get('unique_selling_proposition', 'Explains complex topics in an accessible way.')

        prompt = f"""
        You are an expert in writing back cover copy for Popular Science books. Your goal is to generate a compelling and informative description that will entice readers to purchase the book.

        Book Title: {title}
        Author: {author}
        Key Concepts: {', '.join(key_concepts)}
        Target Audience: {target_audience}
        Author Credentials: {author_credentials}
        Book Summary: {book_summary}
        Unique Selling Proposition: {unique_selling_proposition}

        Guidelines:

        1. **Hook:** Start with a captivating hook that grabs the reader's attention. This could be a surprising statistic, a thought-provoking question, or a bold statement about the future of science. Think about the 'wow' factor.

        2. **Explain the Science:** Clearly and concisely explain the core scientific concepts explored in the book. Avoid jargon or overly technical language. Use analogies and real-world examples to make the science accessible to {target_audience}. Focus on the "why" and "how" of the science.

        3. **Highlight the Relevance:** Emphasize the relevance of the science to the reader's life and the world around them. How does this knowledge empower them? What problems does it solve? How does it shape our future?

        4. **Show the Impact:** Discuss the potential impact of the science on society, technology, or our understanding of the universe. Explore the ethical implications and potential future applications.

        5. **Author Authority:** Briefly mention the author's credentials and expertise, highlighting why they are uniquely qualified to write this book.

        6. **Call to Action:** End with a compelling call to action that encourages the reader to learn more. This could be a question, a challenge, or a promise of discovery.

        7. **Emotional Hook:** Appeal to the reader's sense of wonder, curiosity, and desire for knowledge. Emphasize the excitement of scientific discovery and the power of understanding the world around us.

        8. **Popular Science Tone:** Maintain a tone that is informative, engaging, and optimistic. Avoid being overly sensational or alarmist.

        9. **Word Count:** Aim for a description that is approximately 150-200 words.

        10. **Format:** Structure the description into short, digestible paragraphs. Use strong verbs and vivid language to create a sense of excitement and discovery.

        Example Back Cover Copy Structure:

        [Hook: Start with a captivating question or surprising fact.]

        [Explanation: Clearly explain the core scientific concepts in accessible language.]

        [Relevance: Highlight the relevance of the science to the reader's life.]

        [Impact: Discuss the potential impact on society and the future.]

        [Call to Action: Encourage the reader to learn more.]

        Generate a compelling back cover description for '{title}' by {author} that follows these guidelines.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, 2-3 line book recommendation
        for Popular Science books.

        Args:
        **kwargs: Keyword arguments, similar to get_back_cover_prompt.

        Returns:
        str: A prompt string for generating a concise book recommendation.
        """

        title = kwargs.get('title', 'The Book')
        author = kwargs.get('author', 'The Author')
        key_concepts = kwargs.get('key_concepts', ['Science', 'Technology'])
        target_audience = kwargs.get('target_audience', 'General Readers')

        prompt = f"""
        You are an expert in writing concise book recommendations, especially for Popular Science. Your goal is to create a short, engaging description (2-3 lines maximum) that will quickly capture the reader's interest and recommend the book.

        Book Title: {title}
        Author: {author}
        Key Concepts: {', '.join(key_concepts)}
        Target Audience: {target_audience}

        Guidelines:

        1. **Focus on the Core Idea:** Highlight the most fascinating and important concept explored in the book.

        2. **Intrigue and Curiosity:** Create a sense of mystery and wonder that makes the reader want to learn more.

        3. **Target Audience:** Tailor the recommendation to the intended audience.

        4. **Action-Oriented:** Use strong verbs and active voice to create a sense of excitement.

        5. **Keep it Short:** Adhere strictly to the 2-3 line limit.

        Examples:

        * "Unravel the mysteries of [key concept] in this accessible and mind-blowing exploration of science!"
        * "Discover the future of [field of science] and how it will transform our world in this captivating read."
        * "Perfect for curious minds! [Book title] demystifies complex scientific concepts and makes them accessible to everyone."

        Generate a short, 2-3 line book recommendation for '{title}' by {author} following these guidelines.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating punchy marketing taglines for
        Popular Science books.

        Args:
        **kwargs: Keyword arguments, similar to get_back_cover_prompt.

        Returns:
        str: A prompt string for generating impactful taglines.
        """

        title = kwargs.get('title', 'The Book')
        key_concepts = kwargs.get('key_concepts', ['Science', 'Technology'])
        target_audience = kwargs.get('target_audience', 'General Readers')

        prompt = f"""
        You are an expert in creating catchy and memorable marketing taglines, especially for Popular Science books. Your goal is to generate a short, impactful tagline that will grab the reader's attention and convey the essence of the book.

        Book Title: {title}
        Key Concepts: {', '.join(key_concepts)}
        Target Audience: {target_audience}

        Guidelines:

        1. **Keep it Concise:** Aim for a tagline that is no more than 5-7 words.

        2. **Highlight the Core Benefit:** What will the reader gain from reading this book?

        3. **Use Strong Verbs:** Create a sense of action and excitement.

        4. **Appeal to Curiosity:** Spark the reader's interest and make them want to learn more.

        5. **Focus on the "Wow" Factor:** What is the most surprising or fascinating aspect of the science?

        Examples:

        * "Unlock the secrets of the universe."
        * "Science made simple. Knowledge made powerful."
        * "Explore the future. Understand the present."
        * "The science that shapes your world."
        * "Ignite your curiosity. Discover the unknown."

        Generate a catchy marketing tagline for '{title}' that follows these guidelines.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining visual style preferences for back cover design
        of Popular Science books.

        Args:
        **kwargs: Keyword arguments including:
        - key_concepts (list): A list of the key scientific concepts covered.
        - target_audience (str): Description of the target audience.
        - cover_themes (list): List of potential themes. e.g., space, cells, technology.

        Returns:
        str: A prompt string for guiding visual design choices.
        """
        key_concepts = kwargs.get('key_concepts', ['Science', 'Technology'])
        target_audience = kwargs.get('target_audience', 'General Readers')
        cover_themes = kwargs.get('cover_themes', ['General Science'])

        prompt = f"""
        You are an expert in visual design for book covers, specifically for the Popular Science genre. Your task is to define the visual style preferences for the back cover of a Popular Science book.

        Key Concepts: {', '.join(key_concepts)}
        Target Audience: {target_audience}
        Potential Cover Themes: {', '.join(cover_themes)}

        Guidelines:

        1. **Imagery:**
        *   **Modern and Clean:** Emphasize a clean, modern aesthetic. Avoid cluttered or overly complex designs.
        *   **Visually Engaging:** Use high-quality, visually striking images that capture the essence of the science.
        *   **Representational or Abstract:** Decide whether the imagery should be representational (e.g., a photo of a galaxy, a diagram of a cell) or abstract (e.g., geometric patterns, color gradients). Abstract can work well if representational images are difficult to obtain or if a more conceptual feel is desired.
        *   **Color Palette:** Suggest a color palette that is both visually appealing and appropriate for the subject matter. Consider using blues, greens, and purples to evoke a sense of science and technology. Avoid overly bright or jarring colors. Consider the use of gradients and duotones for a modern look.
        *   **Iconography:** Suggest use of icons for key concepts.

        2. **Typography:**
        *   **Readability:** Prioritize readability. Choose fonts that are clear and easy to read, even at small sizes.
        *   **Modern and Professional:** Select fonts that convey a sense of professionalism and authority. Sans-serif fonts are often a good choice for Popular Science books.
        *   **Hierarchy:** Use different font sizes and weights to create a clear visual hierarchy and guide the reader's eye.
        *   **Consider fonts that evoke a sense of innovation and discovery.**

        3. **Layout:**
        *   **Clean and Organized:** Ensure that the layout is clean, organized, and easy to navigate.
        *   **Balance:** Achieve a balance between text and images. Avoid overcrowding the back cover with too much information.
        *   **Whitespace:** Use whitespace effectively to create visual breathing room and improve readability.
        *   **Consider a modular or grid-based layout for a modern and structured look.**

        4. **Overall Impression:**
        *   **Informative and Engaging:** The back cover should be both informative and engaging, conveying the essence of the book in a visually appealing way.
        *   **Credible and Authoritative:** The design should convey a sense of credibility and authority, reflecting the author's expertise and the scientific rigor of the book.
        *   **Appealing to {target_audience}:** Ensure that the visual style is appropriate for the intended audience.

        Based on these guidelines, describe the ideal visual style for the back cover of a Popular Science book focusing on {', '.join(key_concepts)} for {target_audience}, and with potential themes of {', '.join(cover_themes)}.
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return PopularSciencePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return PopularSciencePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return PopularSciencePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return PopularSciencePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return PopularSciencePrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return PopularSciencePrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return PopularSciencePrompts.get_series_book_prompt(**kwargs)
