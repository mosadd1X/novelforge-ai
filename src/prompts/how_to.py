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

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating a compelling back cover description for a How-To book.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, topic, target audience,
        key benefits, unique selling points, etc.).

        Returns:
        str: A prompt string designed to guide AI in writing effective How-To back cover copy.
        """
        title = kwargs.get("title", "[Book Title]")
        author = kwargs.get("author", "[Author Name]")
        topic = kwargs.get("topic", "[Book's Main Topic]")
        target_audience = kwargs.get("target_audience", "[Target Audience Description]")
        key_benefits = kwargs.get("key_benefits", "[List of Key Benefits]")
        unique_selling_points = kwargs.get("unique_selling_points", "[Unique Aspects of the Book]")
        level = kwargs.get("level", "Beginner") # Beginner, Intermediate, Advanced
        book_structure = kwargs.get("book_structure", "[Describe the book's structure, e.g., step-by-step, project-based]")
        call_to_action = kwargs.get("call_to_action", "[Desired reader action after reading]")

        prompt = f"""
        Write a compelling back cover description for a How-To book titled '{title}' by {author}.

        The book's main topic is {topic}. It is targeted towards {target_audience}.  The book is designed for {level} level audience.

        The structure of the book is {book_structure}.

        The primary goal of this book is to help readers {key_benefits}.  It should emphasize practical skills and actionable advice.

        Unique selling points of this book include {unique_selling_points}. Highlight what makes this book different and better than other How-To books on the same topic.

        The back cover should clearly communicate the following:

        *   **Problem/Need:** What problem does this book solve for the reader?  What need does it fulfill?
        *   **Solution/Benefit:** How does this book provide a practical solution? What tangible benefits will the reader gain?
        *   **Credibility:** Why should the reader trust this author/book? (mention author expertise or unique approach)
        *   **Clarity and Conciseness:** Use clear, easy-to-understand language. Avoid jargon unless it's essential and well-defined.
        *   **Actionable Steps:** Emphasize the practical, step-by-step nature of the book.
        *   **Motivation and Empowerment:** Inspire the reader to take action and achieve their goals.

        Use a tone that is:

        *   Helpful and encouraging
        *   Confident and authoritative (but not arrogant)
        *   Enthusiastic and engaging
        *   Results-oriented

        The back cover should include a strong call to action, encouraging readers to {call_to_action}.

        Aim for a length of approximately 150-200 words.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short, impactful description (2-3 lines) of the How-To book, suitable for recommendations or social media.

        Args:
        **kwargs: Keyword arguments containing book details (title, topic, key benefit).

        Returns:
        str: A prompt string for generating concise How-To book descriptions.
        """
        title = kwargs.get("title", "[Book Title]")
        topic = kwargs.get("topic", "[Book's Main Topic]")
        key_benefit = kwargs.get("key_benefit", "[Key Benefit of the Book]")

        prompt = f"""
        Write a short (2-3 lines) description for the How-To book '{title}' on the topic of {topic}.

        Focus on the key benefit: {key_benefit}.

        The description should be:

        *   Concise and attention-grabbing
        *   Benefit-driven (what will the reader achieve?)
        *   Action-oriented (entice the reader to learn more)

        Example: "Master [Skill] with this step-by-step guide.  Unlock [Specific Result] and achieve [Desired Outcome]!"
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for a punchy, memorable marketing tagline for the How-To book.

        Args:
        **kwargs: Keyword arguments containing book details (topic, target audience, desired outcome).

        Returns:
        str: A prompt string for generating effective How-To marketing taglines.
        """
        topic = kwargs.get("topic", "[Book's Main Topic]")
        target_audience = kwargs.get("target_audience", "[Target Audience Description]")
        desired_outcome = kwargs.get("desired_outcome", "[Desired Outcome for the Reader]")

        prompt = f"""
        Create a punchy, memorable marketing tagline for a How-To book on {topic}, targeted at {target_audience}.

        The tagline should focus on the desired outcome: {desired_outcome}.

        The tagline should be:

        *   Short and catchy (ideally under 10 words)
        *   Benefit-driven (what will the reader gain?)
        *   Action-oriented (inspire the reader to take action)
        *   Unique and memorable

        Examples:

        *   "[Topic]: Your Step-by-Step Success Guide."
        *   "Unlock [Desired Outcome] with [Book Title]."
        *   "Master [Skill] in [Number] Days."

        Consider using power words like "Unlock," "Master," "Transform," "Achieve," "Discover."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt outlining visual style preferences for the back cover of a How-To book.

        Args:
        **kwargs: Keyword arguments containing book details (topic, target audience, tone).

        Returns:
        str: A prompt string for guiding the visual design of a How-To book's back cover.
        """
        topic = kwargs.get("topic", "[Book's Main Topic]")
        target_audience = kwargs.get("target_audience", "[Target Audience Description]")
        tone = kwargs.get("tone", "[Book's Tone, e.g., professional, friendly, playful]")
        visual_examples = kwargs.get("visual_examples", "[Examples of visually similar book covers or designs]")

        prompt = f"""
        Describe the desired visual style for the back cover of a How-To book on {topic}, targeted at {target_audience}.

        The overall tone of the book is {tone}.

        Consider the following elements:

        *   **Color Palette:** Suggest a color palette that reflects the book's topic and target audience. (e.g., professional/technical = blues, grays; creative/DIY = vibrant, warm colors).
        *   **Typography:** Recommend font styles that are clear, readable, and visually appealing. (e.g., sans-serif for modern, serif for traditional).  Consider the font size and spacing for readability.
        *   **Imagery:** Should the back cover include images? If so, what kind? (e.g., illustrations, photographs, diagrams). Are they stock photos, or should they be more unique?  Should there be images of the tools/materials required for the how-to process?
        *   **Layout:** How should the text and images be arranged on the back cover? (e.g., clean and minimal, bold and dynamic). Is there a hierarchical structure to the information presented?
        *   **Overall Impression:** The back cover should convey [Desired Impression - e.g., professionalism, trustworthiness, excitement, ease of use].

        Examples of visually similar book covers or designs that you like are: {visual_examples}

        The design should be visually appealing and communicate the book's value proposition at a glance.  Consider incorporating visual cues that reinforce the "how-to" aspect, such as step-by-step icons or diagrams.
        """
        return prompt


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

def get_back_cover_prompt(**kwargs) -> str:
    return HowToPrompts.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return HowToPrompts.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return HowToPrompts.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return HowToPrompts.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return HowToPrompts.get_series_book_prompt(**kwargs)
