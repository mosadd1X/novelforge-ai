"""
History genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class HistoryPrompts(NonFictionBasePrompts):
    GENRE_NAME = "History"
    GENRE_DESCRIPTION = "Historical fiction immerses readers in the past, blending factual events with fictional narratives. It strives for authenticity in depicting the social, political, and cultural contexts of a specific historical period, while also exploring universal human themes through compelling characters and storylines."
    
    GENRE_CHARACTERISTICS = [
        "Authenticity: Meticulous research and accurate portrayal of historical events, customs, and settings.",
        "Immersion: Vivid descriptions that transport the reader to the past, creating a believable and engaging experience.",
        "Character-Driven Narratives: Compelling characters whose lives are shaped by historical events and who grapple with the challenges of their time.",
        "Exploration of Themes: Examination of universal human themes such as love, loss, ambition, betrayal, and the struggle for survival within a historical context.",
        "Conflict and Intrigue: Highlighting the political, social, and personal conflicts that defined the historical period.",
        "Moral Ambiguity: Presenting characters and events with nuance, avoiding simplistic good vs. evil portrayals and exploring the complexities of historical decisions.",
        "Detailed World-Building: Creating a rich and detailed world that reflects the social hierarchies, cultural norms, and technological limitations of the time.",
        "Impact of Historical Events: Demonstrating how significant historical events shape the lives of individual characters and the course of the narrative.",
        "Sense of Place: Strong evocation of the physical environment and its influence on the characters and events.",
        "Use of Primary and Secondary Sources: Drawing upon historical documents, accounts, and scholarly research to ensure accuracy and depth."
    ]
    
    TYPICAL_ELEMENTS = [
        "Historical Setting: A clearly defined historical period and geographical location that serves as the backdrop for the story.",
        "Historical Figures: Inclusion of real historical figures, either as major characters or as supporting roles.",
        "Significant Historical Events: Incorporation of major historical events that impact the plot and characters.",
        "Social and Political Context: Exploration of the social hierarchies, political systems, and cultural norms of the time.",
        "Costumes and Customs: Detailed descriptions of clothing, food, rituals, and other customs that define the historical period.",
        "Technology and Innovation: Accurate portrayal of the technological advancements and limitations of the time.",
        "Dialogue and Language: Use of language that reflects the speech patterns and vocabulary of the historical period.",
        "Primary Source Integration: Incorporation of excerpts from historical documents, letters, or diaries to enhance authenticity.",
        "Maps and Visual Aids: Inclusion of maps, illustrations, or other visual aids to help readers visualize the historical setting.",
        "Themes of Power and Authority: Examination of the dynamics of power and authority within the historical context.",
        "Cultural Clash: Exploration of the conflicts and interactions between different cultures or social groups.",
        "Personal Journeys: Focus on the personal journeys of characters as they navigate the challenges and opportunities of their time."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Writing Considerations
- **Historical Accuracy**: Prioritize meticulous research and fact-checking to ensure the historical accuracy of your narrative. Consult primary and secondary sources, and be prepared to revise your work based on new information.
- **Authenticity of Voice**: Develop a writing style that reflects the language and tone of the historical period. Consider using archaic vocabulary and sentence structures sparingly to enhance authenticity without sacrificing readability.
- **World-Building Depth**: Create a rich and detailed world that immerses the reader in the past. Pay attention to the social, political, economic, and cultural aspects of the historical period, and incorporate these details into your narrative.
- **Character Believability**: Develop characters whose motivations, beliefs, and actions are consistent with the historical context. Avoid anachronisms in their thoughts, behaviors, and dialogue.
- **Avoiding Presentism**: Be mindful of projecting modern values and perspectives onto historical characters and events. Strive to understand the past on its own terms, without imposing contemporary judgments.
- **Balancing Fact and Fiction**: Find a balance between historical accuracy and narrative license. While it is important to remain true to the historical record, you also have the freedom to create fictional characters and storylines that explore the human experience within that context.
- **Sensitivity to Historical Trauma**: Approach sensitive historical topics with respect and empathy. Avoid trivializing or sensationalizing events that caused suffering and injustice.
- **Understanding Causality**: Demonstrate a clear understanding of the causes and consequences of historical events. Show how individual actions and decisions contribute to the larger historical narrative.
'''
        return base_prompt + history_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Outline Requirements
- **Chronological Structure**: Consider organizing your outline chronologically to reflect the sequence of historical events. This can help readers follow the narrative and understand the cause-and-effect relationships between events.
- **Key Historical Events**: Identify the key historical events that will shape your story and incorporate them into your outline. Determine how these events will impact your characters and drive the plot forward.
- **Character Arcs**: Outline the character arcs of your main characters, showing how they change and develop over the course of the story in response to historical events and personal challenges.
- **Setting and Atmosphere**: Include details about the setting and atmosphere in your outline, noting how the physical environment and social context contribute to the overall mood and tone of the story.
- **Themes and Motifs**: Identify the major themes and motifs that you want to explore in your novel and incorporate them into your outline. Consider how these themes will resonate with readers and provide insight into the human condition.
- **Historical Context**: Provide a brief overview of the historical context for each section of your outline, highlighting the key political, social, and cultural factors that are relevant to the story.
- **Research Notes**: Include research notes in your outline to remind yourself of important historical details and sources that you need to consult as you write.
- **Multiple Perspectives**: If your story involves multiple perspectives, outline each character's point of view separately to ensure that their voices are distinct and authentic.
'''
        return base_prompt + history_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Character Development
- **Historical Accuracy of Background**: Ensure your character's background, including their social class, family history, and education, is consistent with the historical period. Research the typical life experiences of people in their position.
- **Believable Motivations**: Develop motivations that are rooted in the historical context. Consider the social, political, and economic factors that would influence their desires and goals.
- **Authentic Language and Dialogue**: Craft dialogue that reflects the speech patterns and vocabulary of the time. Avoid using modern slang or idioms that would sound out of place.
- **Impact of Historical Events on Character**: Show how historical events shape your character's personality, beliefs, and actions. Explore how they react to challenges and opportunities presented by their time.
- **Moral Complexity**: Avoid creating simplistic good vs. evil characters. Explore the moral ambiguities of the historical period and allow your characters to make difficult choices with complex consequences.
- **Internal Conflicts**: Develop internal conflicts that reflect the tensions and contradictions of the historical period. Consider how your character grapples with conflicting loyalties, beliefs, and desires.
- **Relationships with Historical Figures**: If your character interacts with real historical figures, ensure that these interactions are consistent with the historical record and that they reveal something about both characters.
- **Character Arc and Transformation**: Plan a character arc that shows how your character changes and develops over the course of the story in response to historical events and personal experiences.
'''
        return base_prompt + history_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        history_additions = '''
## History-Specific Chapter Writing
- **Setting the Scene**: Begin each chapter by vividly describing the historical setting, including the physical environment, social atmosphere, and cultural details.
- **Historical Context**: Provide relevant historical context to help readers understand the events and characters in the chapter. This could include brief explanations of political events, social customs, or economic conditions.
- **Character Development**: Use each chapter to further develop your characters, revealing their motivations, beliefs, and relationships. Show how they are affected by the historical events unfolding around them.
- **Pacing and Tension**: Control the pacing of each chapter to build tension and keep readers engaged. Use cliffhangers, foreshadowing, and dramatic irony to create suspense.
- **Authentic Dialogue**: Write dialogue that reflects the speech patterns and vocabulary of the historical period. Avoid using modern slang or idioms that would sound out of place.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show readers what is happening, rather than simply telling them. This will help to immerse them in the historical setting.
- **Historical Accuracy**: Ensure that all historical details in the chapter are accurate and consistent with your research. Double-check facts, dates, and names to avoid errors.
- **Emotional Impact**: Aim to create an emotional impact on readers by exploring the human experiences of your characters. Show how they cope with challenges, celebrate victories, and grieve losses.
'''
        return base_prompt + history_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a history-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        history_series_additions = """

## History Series-Specific Planning Elements

### Educational Progression for History
- **Knowledge Building**: Structure learning progression appropriate for history topics
- **Expertise Development**: Guide readers from basic to advanced understanding of history subjects
- **Practical Applications**: Include actionable insights specific to history throughout the series
- **Research Depth**: Plan comprehensive research appropriate for history authority
- **Reader Value**: Ensure each book provides significant history value while building series knowledge

### History Series Continuity
- **Subject Consistency**: Maintain consistent approach to history topics across books
- **Authority Building**: Establish and maintain credibility in history throughout the series
- **Information Architecture**: Structure information flow appropriate for history learning
- **Cross-References**: Create meaningful connections between history concepts across books
- **Updated Knowledge**: Plan for incorporating new history research and developments

Create a history series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + history_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a history-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        history_book_additions = """

## History Series Book Integration

### History Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon history concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous history books when relevant
- **Knowledge Progression**: Advance reader understanding of history topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the history series

### Book-Specific History Focus
- **Educational Objectives**: What specific history knowledge will readers gain from this book?
- **Practical Applications**: What actionable history insights will be provided?
- **Research Integration**: How will new history research be incorporated?
- **Series Advancement**: How does this book advance the overall history education series?
- **Reader Value**: What unique history value does this book add to the series?

Ensure this book provides comprehensive history education while serving as an integral part of the learning series.
"""

        return base_prompt + history_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return HistoryPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return HistoryPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return HistoryPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return HistoryPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return HistoryPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return HistoryPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return HistoryPrompts.get_series_book_prompt(**kwargs)
