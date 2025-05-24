"""
Thriller genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ThrillerPrompts(FictionBasePrompts):
    GENRE_NAME = "Thriller"
    GENRE_DESCRIPTION = "The Thriller genre is characterized by its focus on suspense, tension, and excitement. It often involves high stakes, dangerous situations, and a race against time. The protagonist typically faces a formidable antagonist or a complex web of conspiracies, forcing them to use their wits and courage to survive and uncover the truth. Psychological elements, moral ambiguity, and unexpected twists are common features, creating a gripping and immersive reading experience."
    
    GENRE_CHARACTERISTICS = [
        "Pace and Suspense: A relentless pace that builds suspense through carefully crafted plot twists and cliffhangers, keeping the reader constantly on edge.",
        "High Stakes: The protagonist faces significant personal risk, often involving life-or-death situations or the potential for catastrophic consequences.",
        "Formidable Antagonist: A cunning and resourceful antagonist who poses a credible threat to the protagonist, driving the conflict and raising the stakes.",
        "Moral Ambiguity: Characters often operate in shades of gray, blurring the lines between good and evil and forcing the reader to question their allegiances.",
        "Psychological Depth: Explores the psychological impact of fear, trauma, and paranoia on the characters, adding layers of complexity to their motivations and actions.",
        "Twists and Turns: Unexpected plot twists and revelations that challenge the reader's assumptions and keep them guessing until the very end.",
        "Red Herrings: Deliberate misdirection and false leads that create confusion and uncertainty, adding to the suspense and intrigue.",
        "Atmospheric Setting: A vivid and immersive setting that enhances the sense of danger and isolation, often featuring dark, claustrophobic, or unfamiliar environments.",
        "Race Against Time: The protagonist is often under pressure to solve a mystery or prevent a disaster before it's too late, adding urgency to the narrative.",
        "Unreliable Narrator: A narrator whose perspective is biased, deceptive, or incomplete, forcing the reader to question the truth and piece together the real story."
    ]
    
    TYPICAL_ELEMENTS = [
        "A protagonist with a hidden past or a secret vulnerability.",
        "A conspiracy that reaches the highest levels of power.",
        "A ticking clock scenario that adds urgency to the plot.",
        "A series of escalating threats and challenges.",
        "A cat-and-mouse game between the protagonist and the antagonist.",
        "A double-crossing character who betrays the protagonist's trust.",
        "A shocking revelation that changes everything.",
        "A chase scene that puts the protagonist in mortal danger.",
        "A suspenseful interrogation scene.",
        "A climactic confrontation that tests the protagonist's limits.",
        "A lingering sense of unease or paranoia.",
        "A resolution that leaves some questions unanswered or open to interpretation."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Writing Considerations
- **Pacing and Tension**: Master the art of building suspense through carefully controlled pacing. Use short, impactful sentences and paragraphs to create a sense of urgency, and strategically deploy cliffhangers to keep the reader hooked.
- **Creating Believable Threats**: Develop antagonists who are not only formidable but also believable. Give them clear motivations and a plausible plan, making their actions feel grounded in reality.
- **Red Herrings and Misdirection**: Skillfully weave in red herrings and misdirection to keep the reader guessing. Plant false clues and create misleading scenarios that lead them down the wrong path.
- **Psychological Realism**: Explore the psychological impact of fear, trauma, and paranoia on your characters. Show how these emotions affect their decision-making and behavior, adding depth and complexity to their portrayal.
- **Atmospheric Detail**: Pay close attention to the setting and atmosphere. Use vivid descriptions to create a sense of unease and foreboding, immersing the reader in the world of the story.
- **Twist Endings and Resolutions**: Craft a satisfying twist ending that subverts expectations but remains logically consistent with the established plot. Ensure that the resolution provides closure while leaving a lasting impact on the reader.
- **Moral Ambiguity**: Embrace moral ambiguity in your characters and plot. Explore the gray areas of right and wrong, forcing the reader to question their own values and beliefs.
- **Research and Authenticity**: Conduct thorough research to ensure the authenticity of your story. Pay attention to details about law enforcement, technology, and other relevant fields to create a believable and immersive experience.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Outline Requirements
- **Inciting Incident**: The inciting incident should immediately thrust the protagonist into a dangerous or unsettling situation, setting the stage for the escalating conflict.
- **Rising Action and Suspense**: The rising action should be structured to gradually increase the tension and suspense, with each scene presenting new challenges and obstacles for the protagonist.
- **Midpoint Twist**: Introduce a significant twist or revelation at the midpoint of the story that changes the protagonist's understanding of the situation and raises the stakes even higher.
- **False Climax**: Include a false climax that appears to resolve the conflict but ultimately leads to an even greater threat or challenge.
- **Climax and Confrontation**: The climax should be a high-stakes confrontation between the protagonist and the antagonist, where the protagonist must use all their skills and resources to survive.
- **Resolution and Aftermath**: The resolution should provide closure to the main plot threads while leaving a lasting impact on the protagonist and the reader. Consider including a final twist or revelation that adds a layer of complexity to the ending.
- **Subplot Integration**: Subplots should be carefully integrated into the main plot, adding depth and complexity to the story while also contributing to the overall suspense and tension.
- **Pacing and Momentum**: Maintain a relentless pace throughout the story, with short, impactful scenes and frequent cliffhangers to keep the reader engaged.
- **Red Herring Placement**: Strategically place red herrings throughout the outline to mislead the reader and create a sense of uncertainty.
- **Character Arc Integration**: Ensure that the protagonist's character arc is closely tied to the plot, with their growth and development influencing their ability to overcome the challenges they face.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Character Development
- **Protagonist Vulnerability**: Give the protagonist a vulnerability or a hidden flaw that makes them relatable and sympathetic, but also creates opportunities for the antagonist to exploit them.
- **Antagonist Motivation**: Develop a clear and compelling motivation for the antagonist's actions, making them more than just a one-dimensional villain. Explore their backstory and psychological makeup to create a complex and believable character.
- **Moral Ambiguity**: Explore the moral ambiguity of your characters, blurring the lines between good and evil and forcing the reader to question their allegiances.
- **Psychological Depth**: Delve into the psychological impact of fear, trauma, and paranoia on your characters, showing how these emotions affect their decision-making and behavior.
- **Hidden Agendas**: Give your characters hidden agendas and secret motivations that add layers of complexity to their interactions and relationships.
- **Character Arcs**: Develop clear character arcs for your protagonist and antagonist, showing how they change and evolve throughout the story in response to the challenges they face.
- **Supporting Characters**: Use supporting characters to provide contrast and support for the protagonist, while also adding depth and complexity to the world of the story.
- **Unreliable Narrators**: Consider using an unreliable narrator to create a sense of uncertainty and suspense, forcing the reader to question the truth and piece together the real story.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        thriller_additions = '''
## Thriller-Specific Chapter Writing
- **Opening Hook**: Start each chapter with a compelling hook that grabs the reader's attention and immediately draws them into the scene.
- **Pacing and Tension**: Maintain a relentless pace throughout the chapter, using short, impactful sentences and paragraphs to create a sense of urgency.
- **Cliffhangers**: End each chapter with a cliffhanger that leaves the reader wanting more and eager to turn the page.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show the reader what is happening, rather than simply telling them.
- **Dialogue**: Write realistic and engaging dialogue that reveals character, advances the plot, and builds tension.
- **Suspenseful Atmosphere**: Create a suspenseful atmosphere through the use of setting, imagery, and sound.
- **Red Herrings**: Weave in red herrings and misdirection to keep the reader guessing and create a sense of uncertainty.
- **Character Development**: Use each chapter to further develop your characters, revealing their motivations, flaws, and strengths.
- **Plot Advancement**: Ensure that each chapter advances the plot in a meaningful way, either by introducing new information, raising the stakes, or creating new challenges for the protagonist.
- **Point of View**: Maintain a consistent point of view throughout the chapter, using it to create suspense and build empathy for the protagonist.
'''
        return base_prompt + thriller_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a thriller-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        thriller_series_additions = """

## Thriller Series-Specific Planning Elements

### Genre-Specific Series Development
- **Thriller Conventions**: Ensure each book fulfills thriller reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to thriller
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to thriller
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore thriller themes with increasing depth and complexity

### Thriller Series Continuity
- **Genre Elements**: Maintain consistent thriller elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy thriller readers
- **Series Identity**: Establish a strong series identity that feels authentically thriller
- **World Building**: Develop the story world in ways that enhance the thriller experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the thriller genre

Create a thriller series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + thriller_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a thriller-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        thriller_book_additions = """

## Thriller Series Book Integration

### Thriller Continuity for This Book
- **Genre Consistency**: Maintain established thriller elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to thriller
- **Plot Advancement**: Continue series plot threads while telling a complete thriller story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill thriller reader expectations while advancing the series narrative

### Book-Specific Thriller Focus
- **Central Conflict**: What thriller-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new thriller elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent thriller while serving the series?

Ensure this book feels like an authentic continuation of the thriller series while telling a complete, satisfying story.
"""

        return base_prompt + thriller_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return ThrillerPrompts.get_series_book_prompt(**kwargs)
