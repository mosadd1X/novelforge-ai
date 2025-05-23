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