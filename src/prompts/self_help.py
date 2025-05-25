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

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a selfhelp-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        selfhelp_series_additions = """

## SelfHelp Series-Specific Planning Elements

### Educational Progression for SelfHelp
- **Knowledge Building**: Structure learning progression appropriate for selfhelp topics
- **Expertise Development**: Guide readers from basic to advanced understanding of selfhelp subjects
- **Practical Applications**: Include actionable insights specific to selfhelp throughout the series
- **Research Depth**: Plan comprehensive research appropriate for selfhelp authority
- **Reader Value**: Ensure each book provides significant selfhelp value while building series knowledge

### SelfHelp Series Continuity
- **Subject Consistency**: Maintain consistent approach to selfhelp topics across books
- **Authority Building**: Establish and maintain credibility in selfhelp throughout the series
- **Information Architecture**: Structure information flow appropriate for selfhelp learning
- **Cross-References**: Create meaningful connections between selfhelp concepts across books
- **Updated Knowledge**: Plan for incorporating new selfhelp research and developments

Create a selfhelp series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + selfhelp_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a selfhelp-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        selfhelp_book_additions = """

## SelfHelp Series Book Integration

### SelfHelp Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon selfhelp concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous selfhelp books when relevant
- **Knowledge Progression**: Advance reader understanding of selfhelp topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the selfhelp series

### Book-Specific SelfHelp Focus
- **Educational Objectives**: What specific selfhelp knowledge will readers gain from this book?
- **Practical Applications**: What actionable selfhelp insights will be provided?
- **Research Integration**: How will new selfhelp research be incorporated?
- **Series Advancement**: How does this book advance the overall selfhelp education series?
- **Reader Value**: What unique selfhelp value does this book add to the series?

Ensure this book provides comprehensive selfhelp education while serving as an integral part of the learning series.
"""

        return base_prompt + selfhelp_book_additions

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a prompt for creating compelling back cover descriptions for Self-Help books.

        Args:
        **kwargs: Keyword arguments that can be used to provide additional context.
        Examples: title, author, target_audience, key_benefits, unique_selling_proposition.

        Returns:
        str: A detailed prompt string for back cover copy generation.
        """
        prompt = f"""
        Write a captivating back cover description for a Self-Help book.

        **Genre:** Self-Help

        **Book Title:** {kwargs.get('title', '[Insert Book Title Here]')}
        **Author:** {kwargs.get('author', '[Insert Author Name Here]')}
        **Target Audience:** {kwargs.get('target_audience', '[Specify Target Audience: e.g., Millennial Women Struggling with Anxiety, Entrepreneurs Seeking Productivity Hacks, Individuals Recovering from Trauma]')}
        **Key Benefits:** {kwargs.get('key_benefits', '[List 3-5 Key Benefits Readers Will Gain: e.g., Reduced Stress, Increased Self-Esteem, Improved Relationships, Greater Productivity, Enhanced Mindfulness]')}
        **Unique Selling Proposition (USP):** {kwargs.get('unique_selling_proposition', '[Describe what makes this book different and better than other Self-Help books on the market. Is it a unique methodology, a specific personal story, a scientifically backed approach, or a fresh perspective?]')}

        **Instructions:**

        1. **Start with a Hook:** Begin with a compelling question or statement that grabs the reader's attention and speaks directly to their pain points, aspirations, or desires. Focus on the core problem the book solves.  Examples: "Are you tired of feeling stuck?", "Unlock the secrets to lasting happiness...", "Imagine a life free from anxiety..."

        2. **Highlight the Problem:** Clearly articulate the problem the book addresses. Emphasize the emotional impact of this problem on the reader's life. Use empathetic language. Examples: "The constant pressure to succeed leaves you feeling drained and overwhelmed...", "Anxiety steals your joy and prevents you from living your best life...", "Toxic relationships leave you feeling unworthy and unloved..."

        3. **Introduce the Solution:** Briefly introduce the book's approach to solving the problem. Highlight the book's unique methodology, tools, or techniques. Examples: "This book offers a proven, step-by-step guide to...", "Discover a revolutionary new framework for...", "Learn powerful mindfulness techniques to..."

        4. **Emphasize Transformation:** Focus on the positive transformation readers will experience by implementing the book's advice. Use aspirational language. Examples: "Transform your life from the inside out...", "Unlock your full potential and achieve your dreams...", "Create lasting change and build a happier, more fulfilling life..."

        5. **Include a Credibility Statement (Optional):** If the author has relevant credentials or expertise, briefly mention them to build trust and authority. Examples: "Dr. [Author Name], a leading expert in...", "[Author Name] has helped thousands of people overcome...", "Based on years of research and clinical experience..."

        6. **End with a Call to Action:** Encourage readers to take action and purchase the book. Examples: "Start your journey to a better you today!", "Unlock the life you deserve!", "Discover the secrets to lasting happiness. Get your copy now!"

        7. **Maintain a Positive and Encouraging Tone:** The overall tone should be optimistic, supportive, and empowering. Avoid negativity or judgment.

        8. **Length:** Aim for approximately 150-200 words.

        9. **Keywords:** Incorporate relevant keywords related to the book's topic (e.g., anxiety, mindfulness, productivity, self-esteem, relationships).

        **Example Structure:**

        *   Hook: Compelling question or statement
        *   Problem: Articulation of the reader's pain points
        *   Solution: Introduction to the book's approach
        *   Transformation: Emphasis on the positive outcomes
        *   Credibility (Optional): Author's expertise
        *   Call to Action: Encouragement to purchase the book
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating short, impactful book recommendations (2-3 lines) for Self-Help books.

        Args:
        **kwargs: Keyword arguments that can be used to provide additional context.
        Examples: title, author, target_audience, key_benefit.

        Returns:
        str: A detailed prompt string for short description generation.
        """
        prompt = f"""
        Write a concise and compelling 2-3 line book recommendation for a Self-Help book.

        **Genre:** Self-Help

        **Book Title:** {kwargs.get('title', '[Insert Book Title Here]')}
        **Author:** {kwargs.get('author', '[Insert Author Name Here]')}
        **Target Audience:** {kwargs.get('target_audience', '[Specify Target Audience: e.g., Stressed-Out Professionals, Individuals Seeking Personal Growth]')}
        **Key Benefit:** {kwargs.get('key_benefit', '[State the Main Benefit Readers Will Gain: e.g., Reduced Stress, Increased Confidence, Improved Focus]')}

        **Instructions:**

        1. **Focus on the Core Benefit:** Highlight the single most important benefit readers will receive from the book.

        2. **Use Action-Oriented Language:** Employ strong verbs that convey the transformative power of the book.

        3. **Keep it Concise:** Each line should be impactful and easy to understand.

        4. **Target the Reader's Desires:** Speak directly to their aspirations and pain points.

        5. **Example Structure:**

        *   Line 1: Identify the problem or desire.
        *   Line 2: Introduce the book as the solution.
        *   Line 3: State the key benefit.

        **Example:**

        "Feeling overwhelmed and burnt out?  [Book Title] provides practical strategies to reclaim your time and energy.  Discover how to achieve a better work-life balance and rediscover your joy."

        **Another Example:**

        "Struggling with self-doubt and negative thoughts?  [Book Title] empowers you to build unshakeable confidence and self-esteem.  Unlock your inner strength and start living the life you deserve."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating punchy and memorable marketing taglines for Self-Help books.

        Args:
        **kwargs: Keyword arguments that can be used to provide additional context.
        Examples: title, author, book_topic, target_emotion.

        Returns:
        str: A detailed prompt string for tagline generation.
        """
        prompt = f"""
        Create a powerful and memorable marketing tagline for a Self-Help book.

        **Genre:** Self-Help

        **Book Title:** {kwargs.get('title', '[Insert Book Title Here]')}
        **Book Topic:** {kwargs.get('book_topic', '[Specify the Book Main Topic: e.g., Overcoming Anxiety, Building Confidence, Mastering Productivity]')}
        **Target Emotion:** {kwargs.get('target_emotion', '[Identify the Primary Emotion You Want to Evoke: e.g., Hope, Empowerment, Inspiration, Relief]')}

        **Instructions:**

        1. **Keep it Short and Sweet:** Aim for a tagline that is no more than 5-7 words.

        2. **Focus on the Core Benefit:** Highlight the main outcome readers will achieve.

        3. **Use Strong Verbs:** Employ action-oriented verbs that convey transformation.

        4. **Evoke Emotion:** Tap into the reader's desires, fears, or aspirations.

        5. **Be Unique and Memorable:** Stand out from the crowd with a tagline that is original and catchy.

        6. **Examples:**

        *   Overcome Anxiety. Reclaim Your Life.
        *   Unlock Your Inner Potential.
        *   Confidence Starts Here.
        *   The Path to Lasting Happiness.
        *   Master Your Mind. Master Your Life.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining visual style preferences for the back cover design of Self-Help books.

        Args:
        **kwargs: Keyword arguments that can be used to provide additional context.
        Examples: book_topic, target_audience, desired_tone, imagery_keywords.

        Returns:
        str: A detailed prompt string for visual style preferences.
        """
        prompt = f"""
        Define the desired visual style for the back cover design of a Self-Help book.

        **Genre:** Self-Help

        **Book Topic:** {kwargs.get('book_topic', '[Specify the Book Main Topic: e.g., Mindfulness, Self-Love, Goal Setting]')}
        **Target Audience:** {kwargs.get('target_audience', '[Specify the Target Audience: e.g., Young Adults, Busy Professionals, Seniors]')}
        **Desired Tone:** {kwargs.get('desired_tone', '[Describe the Desired Tone: e.g., Calming, Inspiring, Empowering, Optimistic]')}
        **Imagery Keywords:** {kwargs.get('imagery_keywords', '[List Keywords for Relevant Imagery: e.g., Nature, Light, Abstract Shapes, People Meditating, Sunrise, Growth]')}

        **Instructions:**

        1. **Color Palette:** Specify the preferred color palette. Consider the psychological effects of colors. Examples:
        *   **Calming:** Blues, Greens, Soft Pinks
        *   **Inspiring:** Bright Yellows, Oranges, Turquoise
        *   **Empowering:** Deep Blues, Purples, Golds
        *   **Optimistic:** Pastel Colors, Light Greens, Sunny Yellows

        2. **Typography:** Describe the desired font style. Consider readability and the overall tone. Examples:
        *   **Serif Fonts:** Traditional, trustworthy (e.g., Times New Roman, Garamond)
        *   **Sans-Serif Fonts:** Modern, clean (e.g., Arial, Helvetica, Open Sans)
        *   **Script Fonts:** Elegant, personal (Use sparingly for headings)

        3. **Imagery:** Describe the type of imagery to use. Consider the book's topic and target audience. Examples:
        *   **Nature Scenes:** Serene landscapes, blooming flowers, calming water
        *   **Abstract Designs:** Geometric shapes, flowing lines, minimalist patterns
        *   **People:** Smiling faces, people meditating, people achieving goals

        4. **Overall Aesthetic:** Describe the overall look and feel of the back cover. Examples:
        *   **Minimalist:** Clean lines, white space, simple design
        *   **Modern:** Bold colors, geometric shapes, contemporary typography
        *   **Organic:** Natural textures, earthy tones, hand-drawn elements
        *   **Inspirational:** Uplifting imagery, positive affirmations, motivational quotes

        5. **Examples:**

        *   "For a book on mindfulness for young adults, I want a calming and modern design with a color palette of soft blues and greens. Use a sans-serif font for readability and include imagery of people meditating in nature."

        *   "For a book on goal setting for entrepreneurs, I want an empowering and optimistic design with a color palette of bright yellows and oranges. Use a bold sans-serif font and include imagery of people achieving their goals."
        """
        return prompt

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
def get_series_plan_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return SelfHelpPrompts.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return SelfHelpPrompts.get_series_book_prompt(**kwargs)
