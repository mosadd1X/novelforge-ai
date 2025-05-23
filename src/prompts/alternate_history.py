"""
Alternate History genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class AlternateHistoryPrompts(FictionBasePrompts):
    GENRE_NAME = "Alternate History"
    GENRE_DESCRIPTION = "Alternate History explores 'what if' scenarios by diverging from established historical timelines. It examines the potential consequences of altered events, decisions, or technologies, creating worlds that are both familiar and strikingly different from our own. The genre often delves into the complex interplay of politics, society, culture, and individual lives within these altered realities."
    
    GENRE_CHARACTERISTICS = [
        "A clearly defined point of divergence (POD) from real history, which serves as the foundation for the altered timeline.",
        "Plausible and logically consistent consequences stemming from the POD, demonstrating how the altered event reshapes subsequent historical developments.",
        "Detailed world-building that reflects the changes in technology, culture, politics, and social structures resulting from the altered timeline.",
        "Exploration of the impact on individual lives and societies, showcasing how characters adapt to or are affected by the alternate reality.",
        "Examination of the ethical and moral implications of the altered timeline, often raising questions about progress, freedom, and the nature of history itself.",
        "A strong sense of verisimilitude, grounding the alternate reality in historical accuracy and believable extrapolations.",
        "Consideration of the butterfly effect, acknowledging that even small changes can have significant and far-reaching consequences.",
        "The presence of familiar historical figures in altered roles or circumstances, providing a point of connection to real history.",
        "Exploration of counterfactual scenarios, such as different outcomes of wars, technological breakthroughs, or political revolutions.",
        "A narrative that balances the fantastical elements of the alternate reality with the grounded realities of human experience."
    ]
    
    TYPICAL_ELEMENTS = [
        "A specific Point of Divergence (POD) clearly identified and explained.",
        "Altered political landscapes, such as different alliances, empires, or forms of government.",
        "Technological advancements or setbacks that deviate from the real-world timeline.",
        "Modified social structures and cultural norms reflecting the altered historical context.",
        "Different outcomes of major historical events, such as wars, revolutions, or discoveries.",
        "The rise and fall of alternate empires or nations.",
        "The survival or extinction of different cultures or languages.",
        "The altered roles and fates of historical figures.",
        "The emergence of new ideologies or philosophical movements.",
        "The development of alternate technologies and inventions.",
        "The exploration of different ethical and moral dilemmas.",
        "The presence of alternate historical documents or artifacts."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Writing Considerations
- **Historical Accuracy**: Demonstrate a strong understanding of the historical period you are altering. Research the social, political, and technological context thoroughly to ensure your point of divergence and its consequences are plausible.
- **Plausibility of Divergence**: The point of divergence should be believable and grounded in the realities of the historical period. Avoid introducing elements that are entirely anachronistic or defy the laws of physics without a clear explanation.
- **Consequence Mapping**: Carefully map out the consequences of your point of divergence. Consider how it would affect different aspects of society, technology, and politics. Use a cause-and-effect approach to build a believable alternate timeline.
- **World-Building Depth**: Create a detailed world that reflects the changes in your alternate timeline. Develop new cultures, languages, political systems, and technologies that are consistent with the altered historical context.
- **Character Adaptation**: Explore how your characters adapt to the altered reality. Consider how their beliefs, values, and relationships are shaped by the new historical context.
- **Ethical Implications**: Examine the ethical and moral implications of your alternate timeline. Consider the consequences of your point of divergence on issues such as freedom, equality, and progress.
- **Internal Consistency**: Maintain internal consistency throughout your story. Ensure that the rules and principles of your alternate world are consistent and that your characters act in accordance with those rules.
- **Avoid Presentism**: Avoid imposing modern values and perspectives on your historical characters. Strive to understand their motivations and beliefs within the context of their own time.
'''
        return base_prompt + alternate_history_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Outline Requirements
- **Establish the Point of Divergence (POD)**: Clearly define the specific event or decision that deviates from real history. Explain the circumstances surrounding the POD and its immediate consequences.
- **Map the Cascade of Effects**: Outline the major changes that result from the POD, tracing their impact on politics, technology, society, and culture. Create a timeline of key events in your alternate history.
- **Develop Key Characters**: Introduce the main characters and their roles in the alternate timeline. Consider how their lives are affected by the altered historical context.
- **Structure the Narrative Arc**: Outline the major plot points and conflicts in your story. Consider how the alternate history setting shapes the narrative arc.
- **World-Building Integration**: Integrate world-building details into the outline, showcasing the unique aspects of your alternate reality. Include descriptions of new technologies, cultures, and political systems.
- **Explore Ethical Dilemmas**: Identify the ethical dilemmas that arise from the alternate timeline. Consider how your characters grapple with these dilemmas.
- **Create a Compelling Climax**: Outline a climax that resolves the major conflicts in your story and showcases the consequences of the alternate history setting.
- **Provide a Satisfying Resolution**: Outline a resolution that provides closure to the characters' stories and reflects on the broader themes of the alternate history.
- **Consider Multiple Perspectives**: Outline how different characters or groups are affected by the altered timeline, showcasing diverse viewpoints.
- **Incorporate Historical Parallels**: Identify parallels between your alternate history and real history, highlighting the similarities and differences between the two timelines.
'''
        return base_prompt + alternate_history_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Character Development
- **Historical Context**: Ground your characters in the specific historical context of your alternate timeline. Consider how their beliefs, values, and relationships are shaped by the altered historical events.
- **Adaptation to Change**: Explore how your characters adapt to the changes in the alternate reality. Consider their reactions to new technologies, political systems, and social norms.
- **Moral Dilemmas**: Present your characters with moral dilemmas that arise from the alternate timeline. Consider how they grapple with these dilemmas and the choices they make.
- **Relationships and Conflicts**: Develop relationships and conflicts between characters that are shaped by the alternate historical context. Consider how their interactions reflect the broader themes of your story.
- **Historical Awareness**: Determine the level of historical awareness your characters possess. Do they know about the real history, or are they only aware of the alternate timeline?
- **Impact of Technology**: Consider how technology impacts your characters' lives. Are they early adopters of new technologies, or are they resistant to change?
- **Political Alignment**: Define your characters' political alignment within the alternate historical context. Are they supporters of the ruling regime, or are they rebels fighting for change?
- **Cultural Identity**: Explore your characters' cultural identity within the alternate timeline. How does their culture differ from the real-world equivalent, and how does it shape their worldview?
- **Personal Goals**: Define your characters' personal goals and motivations within the alternate historical context. How do their goals align with or conflict with the broader themes of your story?
'''
        return base_prompt + alternate_history_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        alternate_history_additions = '''
## Alternate History-Specific Chapter Writing
- **Contextual Setting**: Begin each chapter by establishing the historical context and setting. Describe the political climate, social norms, and technological advancements of the alternate timeline.
- **Character Actions**: Show how your characters' actions are influenced by the alternate historical context. Consider how their choices reflect the broader themes of your story.
- **World-Building Integration**: Weave world-building details into the narrative, showcasing the unique aspects of your alternate reality. Describe new technologies, cultures, and political systems through the characters' experiences.
- **Historical Parallels**: Draw parallels between your alternate history and real history, highlighting the similarities and differences between the two timelines. Use these parallels to create a sense of verisimilitude.
- **Ethical Dilemmas**: Present your characters with ethical dilemmas that arise from the alternate timeline. Explore the consequences of their choices and the impact on their relationships.
- **Suspense and Conflict**: Build suspense and conflict by introducing challenges and obstacles that are specific to the alternate historical context.
- **Character Development**: Use each chapter to develop your characters' personalities and motivations. Show how they grow and change as they navigate the challenges of the alternate timeline.
- **Show, Don't Tell**: Use vivid descriptions and engaging dialogue to bring your alternate history to life. Avoid simply telling the reader about the changes in the timeline; show them through the characters' experiences.
- **Maintain Consistency**: Ensure that your writing is consistent with the established rules and principles of your alternate world. Avoid introducing elements that contradict the existing historical context.
'''
        return base_prompt + alternate_history_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return AlternateHistoryPrompts.get_enhancement_prompt(**kwargs)