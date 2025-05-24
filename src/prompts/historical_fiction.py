"""
Historical Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class HistoricalFictionPrompts(FictionBasePrompts):
    GENRE_NAME = "Historical Fiction"
    GENRE_DESCRIPTION = "Historical fiction is a genre that blends fictional narratives with historical settings and events. It aims to transport readers to the past, immersing them in the social, political, and cultural landscapes of a specific era. While the characters and plot are often fictional, the historical backdrop is meticulously researched and accurately portrayed, providing both entertainment and a deeper understanding of history."
    
    GENRE_CHARACTERISTICS = [
        "Authentic Historical Setting: The story is set in a specific historical period, meticulously researched to ensure accuracy in details such as clothing, customs, architecture, and social norms.",
        "Plausible Plot: The plot is interwoven with actual historical events and figures, making the fictional narrative feel plausible within the context of the time.",
        "Fictional Characters in Historical Context: The characters, though fictional, interact with real historical figures and are shaped by the events and societal conditions of the era.",
        "Exploration of Social and Political Issues: The narrative often explores the social and political issues prevalent during the historical period, such as class struggles, religious conflicts, or wars.",
        "Attention to Detail: The author pays close attention to details that evoke the atmosphere of the historical period, including language, food, music, and daily life.",
        "Historical Accuracy vs. Dramatic License: While striving for historical accuracy, the author may take some dramatic license to enhance the narrative, but these liberties should not contradict established historical facts.",
        "Immersive World-Building: The author creates a vivid and immersive world that transports the reader to the past, making them feel as though they are experiencing the historical period firsthand.",
        "Themes of Change and Continuity: The story often explores themes of change and continuity, examining how people's lives were affected by historical events and how certain aspects of human nature remain constant across time.",
        "Educational Value: Historical fiction can provide readers with a deeper understanding of history, sparking their interest in learning more about the past.",
        "Moral and Ethical Dilemmas: Characters often face moral and ethical dilemmas shaped by the values and constraints of their historical context."
    ]
    
    TYPICAL_ELEMENTS = [
        "A compelling protagonist whose life is intertwined with historical events.",
        "A clearly defined historical setting with accurate details.",
        "Conflict arising from social, political, or religious tensions of the era.",
        "Interaction between fictional characters and real historical figures.",
        "A plot that incorporates actual historical events and battles.",
        "Themes of love, loss, betrayal, and redemption within the historical context.",
        "Detailed descriptions of clothing, food, and customs of the time.",
        "Exploration of the daily lives of people from different social classes.",
        "A climax that coincides with a significant historical event.",
        "A resolution that reflects the historical outcome and its impact on the characters.",
        "Use of language and dialogue appropriate to the historical period.",
        "Inclusion of historical documents, letters, or artifacts to enhance authenticity."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        historical_fiction_additions = '''
## Historical Fiction-Specific Writing Considerations
- **Historical Accuracy**: Demonstrate a commitment to thorough research and accurate portrayal of the historical period, including social customs, political climate, and technological advancements. Avoid anachronisms and ensure consistency with known historical facts.
- **Authenticity of Voice**: Develop a writing style that reflects the language and tone of the historical period. Consider using vocabulary, sentence structures, and idioms that were common during that time, while remaining accessible to modern readers.
- **Character Believability**: Create characters whose motivations, beliefs, and actions are consistent with the values and norms of their historical context. Avoid imposing modern sensibilities on historical figures.
- **World-Building Depth**: Craft a vivid and immersive world that transports the reader to the past. Pay attention to details such as architecture, clothing, food, music, and daily life to create a sense of authenticity.
- **Balancing Fact and Fiction**: Skillfully weave fictional narratives into the fabric of historical events, creating a compelling story that is both entertaining and informative. Clearly distinguish between factual events and fictional embellishments.
- **Sensitivity to Cultural Differences**: Approach the portrayal of different cultures and societies with sensitivity and respect. Avoid stereotypes and strive for a nuanced understanding of their beliefs, values, and customs.
- **Ethical Considerations**: Address the ethical dilemmas and moral complexities of the historical period in a thoughtful and nuanced manner. Explore the consequences of historical events on individuals and societies.
- **Avoiding Presentism**: Be mindful of presentism, the tendency to interpret the past through the lens of modern values and beliefs. Strive to understand the historical context on its own terms, without imposing contemporary judgments.
'''
        return base_prompt + historical_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        historical_fiction_additions = '''
## Historical Fiction-Specific Outline Requirements
- **Historical Context Establishment**: The outline should clearly establish the historical context of the story, including the specific time period, location, and key historical events that will influence the plot.
- **Character Arc Integration**: The character arcs should be intricately woven into the historical events, showing how the characters are shaped by and react to the circumstances of their time.
- **Plausible Plot Development**: The plot points should be plausible within the historical context, avoiding anachronisms or events that contradict established historical facts.
- **Key Historical Event Milestones**: Identify key historical events that will serve as milestones in the plot, marking significant turning points in the story and the characters' lives.
- **Social and Political Landscape**: The outline should incorporate the social and political landscape of the historical period, including class structures, religious beliefs, and political tensions.
- **Authentic Setting Descriptions**: Include detailed descriptions of the settings, ensuring they accurately reflect the architecture, customs, and daily life of the historical period.
- **Conflict and Resolution**: The conflict should arise from the historical context, and the resolution should be plausible given the historical circumstances and the characters' actions.
- **Thematic Exploration**: The outline should identify the key themes that will be explored in the story, such as love, loss, betrayal, redemption, or the impact of historical events on individuals and societies.
- **Research Integration**: The outline should demonstrate a clear understanding of the historical period, incorporating research findings into the plot, characters, and setting.
- **Balancing Fact and Fiction**: The outline should indicate where historical facts will be used and where fictional elements will be added to enhance the narrative.
'''
        return base_prompt + historical_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        historical_fiction_additions = '''
## Historical Fiction-Specific Character Development
- **Historical Accuracy in Background**: Character backgrounds should be consistent with the social class, occupation, and historical context in which they live. Research the typical life experiences of people in similar circumstances.
- **Authentic Motivations**: Character motivations should be rooted in the values, beliefs, and social pressures of their time. Avoid imposing modern sensibilities on historical characters.
- **Interaction with Historical Figures**: If the character interacts with real historical figures, ensure that these interactions are plausible and consistent with the known personalities and actions of those figures.
- **Impact of Historical Events**: Consider how historical events shape the character's personality, beliefs, and actions. Show how they are affected by the social, political, and economic conditions of their time.
- **Language and Dialogue**: Use language and dialogue that is appropriate to the character's social class, education, and historical period. Research the common vocabulary and speech patterns of the time.
- **Costuming and Appearance**: Describe the character's clothing and appearance in detail, ensuring that it is consistent with the fashion and social norms of the historical period.
- **Moral and Ethical Dilemmas**: Place the character in moral and ethical dilemmas that are specific to the historical context, forcing them to make difficult choices that reflect the values and constraints of their time.
- **Character Arc and Transformation**: Show how the character changes and evolves over the course of the story, as they are influenced by historical events and their own experiences.
- **Avoiding Stereotypes**: Avoid perpetuating stereotypes about people from different historical periods or social classes. Strive for nuanced and realistic portrayals of characters.
- **Internal Consistency**: Ensure that the character's actions and beliefs are internally consistent, reflecting a coherent and believable personality within the historical context.
'''
        return base_prompt + historical_fiction_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        historical_fiction_additions = '''
## Historical Fiction-Specific Chapter Writing
- **Setting the Scene**: Begin each chapter with a vivid description of the historical setting, including details about the architecture, landscape, and atmosphere. Use sensory details to immerse the reader in the past.
- **Character Introductions**: Introduce characters in a way that reveals their social class, occupation, and historical context. Use their dialogue and actions to establish their personalities and motivations.
- **Historical Context Integration**: Weave historical events and details into the narrative seamlessly, showing how they affect the characters and the plot. Avoid info-dumping; instead, reveal information gradually through the characters' experiences.
- **Authentic Dialogue**: Use dialogue that is appropriate to the historical period, reflecting the language, vocabulary, and speech patterns of the time. Research common idioms and expressions.
- **Conflict and Tension**: Create conflict and tension that arises from the historical context, such as social unrest, political intrigue, or religious persecution. Use these conflicts to drive the plot forward.
- **Pacing and Structure**: Structure each chapter with a clear beginning, middle, and end, building suspense and anticipation as the story progresses. Use cliffhangers to encourage readers to continue reading.
- **Show, Don't Tell**: Show the reader what is happening through the characters' actions, thoughts, and feelings, rather than simply telling them. Use vivid imagery and sensory details to bring the story to life.
- **Emotional Impact**: Evoke emotions in the reader by showing the characters' reactions to historical events and personal challenges. Use empathy and compassion to connect the reader to the characters' experiences.
- **Research and Accuracy**: Ensure that all historical details are accurate and consistent with your research. Double-check facts and avoid anachronisms.
- **Chapter Endings**: End each chapter with a compelling image, a thought-provoking question, or a surprising revelation that leaves the reader wanting more.
'''
        return base_prompt + historical_fiction_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a historicalfiction-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        historicalfiction_series_additions = """

## HistoricalFiction Series-Specific Planning Elements

### Genre-Specific Series Development
- **HistoricalFiction Conventions**: Ensure each book fulfills historicalfiction reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to historicalfiction
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to historicalfiction
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore historicalfiction themes with increasing depth and complexity

### HistoricalFiction Series Continuity
- **Genre Elements**: Maintain consistent historicalfiction elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy historicalfiction readers
- **Series Identity**: Establish a strong series identity that feels authentically historicalfiction
- **World Building**: Develop the story world in ways that enhance the historicalfiction experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the historicalfiction genre

Create a historicalfiction series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + historicalfiction_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a historicalfiction-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        historicalfiction_book_additions = """

## HistoricalFiction Series Book Integration

### HistoricalFiction Continuity for This Book
- **Genre Consistency**: Maintain established historicalfiction elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to historicalfiction
- **Plot Advancement**: Continue series plot threads while telling a complete historicalfiction story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill historicalfiction reader expectations while advancing the series narrative

### Book-Specific HistoricalFiction Focus
- **Central Conflict**: What historicalfiction-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new historicalfiction elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent historicalfiction while serving the series?

Ensure this book feels like an authentic continuation of the historicalfiction series while telling a complete, satisfying story.
"""

        return base_prompt + historicalfiction_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return HistoricalFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return HistoricalFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return HistoricalFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return HistoricalFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return HistoricalFictionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return HistoricalFictionPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return HistoricalFictionPrompts.get_series_book_prompt(**kwargs)
