"""
Business genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class BusinessPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Business"
    GENRE_DESCRIPTION = "The Business genre encompasses narratives centered around the world of commerce, entrepreneurship, and organizational dynamics. These stories often explore themes of ambition, innovation, competition, ethical dilemmas, and the pursuit of success within a corporate or entrepreneurial setting. They can range from high-stakes dramas in the boardroom to the gritty realities of startups and the personal sacrifices required to build an empire."
    
    GENRE_CHARACTERISTICS = [
        "Focus on strategic decision-making and its consequences within a business context.",
        "Exploration of ethical dilemmas and moral compromises faced by business leaders.",
        "Detailed portrayal of corporate culture, power dynamics, and office politics.",
        "Emphasis on financial performance, market trends, and economic factors influencing the narrative.",
        "Examination of the impact of technology and innovation on business models and competitive landscapes.",
        "Realistic depiction of the challenges and rewards of entrepreneurship, including fundraising, scaling, and managing risk.",
        "Exploration of leadership styles, management techniques, and organizational structures.",
        "Portrayal of the human cost of business decisions, including employee morale, work-life balance, and personal relationships.",
        "Use of industry-specific jargon and terminology to enhance authenticity.",
        "Focus on the importance of networking, partnerships, and strategic alliances."
    ]
    
    TYPICAL_ELEMENTS = [
        "A compelling business idea or innovative product/service.",
        "A charismatic and driven protagonist, often an entrepreneur or CEO.",
        "A detailed business plan outlining the company's strategy and financial projections.",
        "A competitive market environment with established players and emerging threats.",
        "A team of skilled and dedicated employees, each with their own strengths and weaknesses.",
        "A funding round or investment opportunity that could make or break the company.",
        "A major deal or acquisition that could transform the business landscape.",
        "A crisis or scandal that threatens the company's reputation and financial stability.",
        "A mentor or advisor who provides guidance and support to the protagonist.",
        "A rival or competitor who seeks to undermine the protagonist's success.",
        "A detailed portrayal of the company's operations, including marketing, sales, and product development.",
        "A satisfying resolution that reflects the protagonist's growth and the company's ultimate fate."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        business_additions = '''
## Business-Specific Writing Considerations
- **Financial Acumen**: Demonstrate a strong understanding of financial statements, key performance indicators (KPIs), and investment strategies. Research industry-specific financial metrics to enhance realism.
- **Industry Knowledge**: Possess in-depth knowledge of the specific industry in which the story is set, including market trends, regulatory environment, and competitive landscape.
- **Corporate Culture**: Accurately portray the nuances of corporate culture, including communication styles, power dynamics, and employee morale.
- **Ethical Considerations**: Explore the ethical dilemmas faced by business leaders and the consequences of their decisions. Consider the impact on stakeholders, including employees, customers, and shareholders.
- **Strategic Thinking**: Develop compelling strategies and tactics that drive the plot forward. Show how characters analyze market opportunities, assess risks, and make critical decisions.
- **Realistic Dialogue**: Write dialogue that reflects the language and communication styles of business professionals. Use industry-specific jargon sparingly and only when appropriate.
- **Conflict and Tension**: Create conflict and tension through competition, ethical disagreements, and power struggles. Use these conflicts to drive character development and plot progression.
- **Pacing and Structure**: Maintain a brisk pace and a clear structure that reflects the fast-paced nature of the business world. Use short, concise chapters to keep the reader engaged.
'''
        return base_prompt + business_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        business_additions = '''
## Business-Specific Outline Requirements
- **Executive Summary**: Begin with an executive summary that outlines the core business idea, the protagonist's goals, and the central conflict.
- **Market Analysis**: Include a section that details the market environment, including competitors, target customers, and market trends.
- **Strategic Plan**: Outline the protagonist's strategic plan for achieving their business goals, including key milestones and potential challenges.
- **Financial Projections**: Incorporate financial projections that demonstrate the viability of the business idea and the potential for growth.
- **Key Partnerships**: Identify key partnerships and alliances that will be crucial to the protagonist's success.
- **Crisis Management**: Plan for potential crises or setbacks that could threaten the business, and outline how the protagonist will respond.
- **Ethical Dilemmas**: Integrate ethical dilemmas into the plot that force the protagonist to make difficult choices with significant consequences.
- **Climax and Resolution**: Structure the climax around a major business event, such as a deal closing, product launch, or financial crisis. The resolution should reflect the protagonist's growth and the ultimate fate of the company.
'''
        return base_prompt + business_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        business_additions = '''
## Business-Specific Character Development
- **Entrepreneurial Drive**: The protagonist should possess a strong entrepreneurial drive, a willingness to take risks, and a relentless pursuit of their goals.
- **Leadership Qualities**: Develop strong leadership qualities in the protagonist, including the ability to inspire, motivate, and delegate effectively.
- **Financial Savvy**: The protagonist should have a solid understanding of financial principles and the ability to make sound financial decisions.
- **Ethical Compass**: Define the protagonist's ethical compass and explore how their values are tested throughout the story.
- **Supporting Characters**: Create a diverse cast of supporting characters, including mentors, rivals, employees, and investors, each with their own motivations and agendas.
- **Character Flaws**: Give the protagonist and supporting characters flaws that make them relatable and add depth to the story.
- **Character Growth**: Show how the characters grow and evolve as they face challenges and make difficult decisions.
- **Motivation and Goals**: Clearly define each character's motivations and goals, and how they contribute to the overall plot.
'''
        return base_prompt + business_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        business_additions = '''
## Business-Specific Chapter Writing
- **Focus on Action**: Each chapter should focus on a specific action or event that drives the plot forward, such as a meeting, negotiation, or product launch.
- **Incorporate Data**: Use data and statistics to support your descriptions and add credibility to the story.
- **Show, Don't Tell**: Show the reader what is happening through vivid descriptions and compelling dialogue, rather than simply telling them.
- **Build Suspense**: Build suspense by creating uncertainty and raising the stakes.
- **Use Cliffhangers**: End each chapter with a cliffhanger to keep the reader engaged and eager to find out what happens next.
- **Maintain a Fast Pace**: Maintain a fast pace by using short, concise sentences and avoiding unnecessary details.
- **Focus on Conflict**: Focus on conflict and tension to create drama and keep the reader engaged.
- **Use Industry Jargon Appropriately**: Use industry jargon sparingly and only when it is necessary to enhance authenticity.
'''
        return base_prompt + business_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a business-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        business_series_additions = """

## Business Series-Specific Planning Elements

### Educational Progression for Business
- **Knowledge Building**: Structure learning progression appropriate for business topics
- **Expertise Development**: Guide readers from basic to advanced understanding of business subjects
- **Practical Applications**: Include actionable insights specific to business throughout the series
- **Research Depth**: Plan comprehensive research appropriate for business authority
- **Reader Value**: Ensure each book provides significant business value while building series knowledge

### Business Series Continuity
- **Subject Consistency**: Maintain consistent approach to business topics across books
- **Authority Building**: Establish and maintain credibility in business throughout the series
- **Information Architecture**: Structure information flow appropriate for business learning
- **Cross-References**: Create meaningful connections between business concepts across books
- **Updated Knowledge**: Plan for incorporating new business research and developments

Create a business series that provides comprehensive education with authoritative, well-researched content.
"""
        
        return base_prompt + business_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a business-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        business_book_additions = """

## Business Series Book Integration

### Business Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon business concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous business books when relevant
- **Knowledge Progression**: Advance reader understanding of business topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the business series

### Book-Specific Business Focus
- **Educational Objectives**: What specific business knowledge will readers gain from this book?
- **Practical Applications**: What actionable business insights will be provided?
- **Research Integration**: How will new business research be incorporated?
- **Series Advancement**: How does this book advance the overall business education series?
- **Reader Value**: What unique business value does this book add to the series?

Ensure this book provides comprehensive business education while serving as an integral part of the learning series.
"""
        
        return base_prompt + business_book_additions

        ```python
        class BusinessBackCover:
        """
        A class containing methods for generating back cover copy and design prompts for Business books.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs) -> str:
        """
        Generates a comprehensive prompt for creating a compelling back cover description for a Business book.

        Args:
        **kwargs: Keyword arguments containing book details such as title, author, target audience,
        key takeaways, unique selling proposition (USP), and comparable titles.

        Returns:
        A detailed prompt string tailored for the Business genre.
        """
        prompt = f"""
        Craft a compelling back cover description for a Business book titled "{kwargs.get('title', '[Title Placeholder]')}" by {kwargs.get('author', '[Author Placeholder]')}.

        **Target Audience:** {kwargs.get('target_audience', '[Target Audience Placeholder, e.g., Aspiring Entrepreneurs, Seasoned CEOs, Marketing Professionals]')}.  Specifically address their pain points and aspirations.

        **Core Message:**  The book's central argument or promise is: {kwargs.get('core_message', '[Core Message Placeholder, e.g., to provide a proven framework for scaling a startup, to offer actionable strategies for improving team performance]')}.

        **Key Takeaways:**  Readers will learn:
        - {kwargs.get('key_takeaway_1', '[Key Takeaway 1 Placeholder]')}
        - {kwargs.get('key_takeaway_2', '[Key Takeaway 2 Placeholder]')}
        - {kwargs.get('key_takeaway_3', '[Key Takeaway 3 Placeholder]')}
        Focus on tangible results and measurable improvements.

        **Unique Selling Proposition (USP):** What makes this book different and better than existing alternatives? {kwargs.get('usp', '[USP Placeholder, e.g., a data-driven approach, real-world case studies from Fortune 500 companies, a focus on ethical and sustainable business practices]')}.  Emphasize quantifiable benefits.

        **Problem/Solution:** Clearly articulate the business problem this book solves and how it provides a practical solution.
        Problem: {kwargs.get('problem', '[Problem Placeholder, e.g., Lack of effective leadership skills, Inability to adapt to market changes, Poor financial management]')}.
        Solution: {kwargs.get('solution', '[Solution Placeholder, e.g., Proven leadership techniques, Agile strategies for innovation, Practical budgeting and forecasting methods]')}.

        **Call to Action:**  What should the reader do after reading the back cover?  Encourage them to buy the book and outline the potential positive outcomes.  Example: "Unlock your business's full potential.  Start building a thriving and sustainable future today."

        **Tone:** Authoritative, professional, yet engaging and accessible.  Avoid jargon unless it's essential and clearly defined.  Focus on providing value and building trust.

        **Comparable Titles (for positioning):**  Books similar to this one include: {kwargs.get('comparable_titles', '[Comparable Titles Placeholder, e.g., Good to Great, The Lean Startup, Zero to One]')}.  Explain how this book is similar and different (better) than these titles.

        **Length:** Aim for approximately 150-200 words.

        **Important Considerations for Business Genre:**
        *   Highlight ROI (Return on Investment) and tangible benefits.
        *   Showcase expertise and credibility (author's background, credentials).
        *   Use data and statistics to support claims.
        *   Focus on practicality and actionable advice.
        *   Emphasize innovation, efficiency, and growth.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs) -> str:
        """
        Generates a prompt for creating a short, impactful book description for the Business genre (2-3 lines).

        Args:
        **kwargs: Keyword arguments containing book details such as title, target audience, and core benefit.

        Returns:
        A prompt string for a concise Business book description.
        """
        prompt = f"""
        Create a short, punchy book description (2-3 lines) for a Business book titled "{kwargs.get('title', '[Title Placeholder]')}".

        **Target Audience:** {kwargs.get('target_audience', '[Target Audience Placeholder, e.g., Small Business Owners, Marketing Managers, Financial Analysts]')}.

        **Core Benefit:** What is the single most important benefit readers will gain from this book? {kwargs.get('core_benefit', '[Core Benefit Placeholder, e.g., Increased profits, Improved efficiency, Better leadership skills]')}.

        **Tone:**  Concise, confident, and benefit-driven.

        **Example:** "Unlock exponential growth with [Book Title].  Proven strategies for [Target Audience] to [Core Benefit]."

        **Important Considerations for Business Genre:**
        *   Focus on immediate value and results.
        *   Use strong action verbs.
        *   Highlight the book's unique selling proposition in a concise way.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs) -> str:
        """
        Generates a prompt for creating a memorable and effective marketing tagline for a Business book.

        Args:
        **kwargs: Keyword arguments containing book details such as title, target audience, and USP.

        Returns:
        A prompt string for a Business book tagline.
        """
        prompt = f"""
        Create a compelling marketing tagline for a Business book titled "{kwargs.get('title', '[Title Placeholder]')}".

        **Target Audience:** {kwargs.get('target_audience', '[Target Audience Placeholder, e.g., Entrepreneurs, Executives, Investors]')}.

        **Unique Selling Proposition (USP):** What is the key differentiator of this book? {kwargs.get('usp', '[USP Placeholder, e.g., A revolutionary new business model, A data-driven approach to decision-making, A focus on sustainable and ethical practices]')}.

        **Desired Emotion:** What feeling should the tagline evoke in the reader? (e.g., excitement, confidence, trust, urgency). {kwargs.get('desired_emotion', '[Desired Emotion Placeholder]')}

        **Tone:**  Bold, impactful, and memorable.

        **Examples:**
        *   "Innovate or Die."
        *   "The Future of [Industry] Starts Now."
        *   "Unlock Your Business Potential."
        *   "Profit with Purpose."

        **Important Considerations for Business Genre:**
        *   Focus on results, innovation, and leadership.
        *   Use strong, action-oriented language.
        *   Keep it short, memorable, and easy to understand.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs) -> str:
        """
        Generates a prompt for defining the visual style preferences for a Business book's back cover.

        Args:
        **kwargs: Keyword arguments containing information about the book's theme, target audience, and overall tone.

        Returns:
        A prompt string detailing visual style preferences for the Business genre.
        """
        prompt = f"""
        Define the visual style preferences for the back cover of a Business book titled "{kwargs.get('title', '[Title Placeholder]')}".

        **Target Audience:** {kwargs.get('target_audience', '[Target Audience Placeholder, e.g., Tech Startups, Established Corporations, Finance Professionals]')}.

        **Overall Tone:**  (e.g., Modern, Classic, Innovative, Trustworthy) {kwargs.get('overall_tone', '[Overall Tone Placeholder]')}.

        **Color Palette:**  Suggest a color palette that reflects the book's tone and target audience.  Consider using colors that convey professionalism, innovation, and trustworthiness. (e.g., Blues and grays for trustworthiness, Greens for sustainability, Bright colors for innovation). {kwargs.get('color_palette', '[Color Palette Suggestions]')}.

        **Imagery:**  Should the back cover include images? If so, what kind? (e.g., Abstract graphics, Business professionals, Data visualizations, Cityscapes). {kwargs.get('imagery', '[Imagery Suggestions]')}.  Consider images that convey success, growth, and innovation.

        **Typography:**  What font styles would be appropriate? (e.g., Clean and modern sans-serif fonts, Classic serif fonts for a more traditional look). {kwargs.get('typography', '[Typography Suggestions]')}.  Ensure readability and professionalism.

        **Layout:**  How should the text and images be arranged on the back cover? (e.g., Clean and minimalist layout, Bold and dynamic layout). {kwargs.get('layout', '[Layout Suggestions]')}.  Prioritize clarity and visual appeal.

        **Overall Impression:**  The back cover should convey a sense of: {kwargs.get('overall_impression', '[Overall Impression Placeholder, e.g., Professionalism, Expertise, Innovation, Trustworthiness]')}.

        **Important Considerations for Business Genre:**
        *   Avoid overly flashy or distracting visuals.
        *   Focus on conveying credibility and expertise.
        *   Use high-quality images and graphics.
        *   Ensure the design is clean, modern, and professional.
        *   Consider incorporating data visualizations or charts if relevant to the book's content.
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return BusinessPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return BusinessPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return BusinessPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return BusinessPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return BusinessPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return BusinessPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return BusinessPrompts.get_series_book_prompt(**kwargs)
