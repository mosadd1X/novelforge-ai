"""
Commercial Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class CommercialFictionPrompts(FictionBasePrompts):
    GENRE_NAME = "Commercial Fiction"
    GENRE_DESCRIPTION = "Commercial fiction is characterized by its broad appeal and focus on entertainment. It prioritizes plot, pacing, and relatable characters to engage a wide readership. These novels often explore universal themes and offer satisfying resolutions, making them highly accessible and enjoyable for a diverse audience."
    
    GENRE_CHARACTERISTICS = [
        "Strong, Hooking Opening: Immediately grabs the reader's attention and establishes the central conflict or intrigue.",
        "Fast-Paced Plot: Maintains a brisk pace with frequent plot developments and minimal downtime to keep readers engaged.",
        "Relatable and Likeable Protagonist: Features a protagonist that readers can easily empathize with and root for, often facing relatable challenges.",
        "Clear and Concise Writing Style: Employs straightforward language and avoids overly complex sentence structures or obscure vocabulary.",
        "High Stakes and Conflict: Presents significant challenges and obstacles for the protagonist to overcome, creating tension and suspense.",
        "Emotional Resonance: Evokes strong emotions in the reader, such as joy, sadness, fear, or excitement, through compelling storytelling.",
        "Satisfying Resolution: Provides a clear and conclusive ending that resolves the central conflict and ties up loose ends, leaving the reader feeling satisfied.",
        "Universal Themes: Explores themes that resonate with a broad audience, such as love, loss, betrayal, redemption, or the pursuit of happiness.",
        "Predictable Structure: Often follows a familiar narrative structure, such as the hero's journey or a three-act structure, providing a sense of familiarity and comfort.",
        "Marketability: Designed to appeal to a large readership and generate significant sales, often incorporating elements that are currently popular or trending."
    ]
    
    TYPICAL_ELEMENTS = [
        "Love Triangle: A romantic plot involving a protagonist torn between two potential partners.",
        "Fish-Out-of-Water Scenario: Placing a character in an unfamiliar environment or situation to create conflict and humor.",
        "Secret Identity: A character concealing their true identity, leading to suspense and intrigue.",
        "Race Against Time: A plot driven by a ticking clock, forcing the protagonist to act quickly to avert disaster.",
        "Revenge Plot: A character seeking retribution for a past wrong, fueling the narrative with anger and determination.",
        "Underdog Story: A protagonist who overcomes adversity and achieves success against all odds.",
        "Family Saga: A multi-generational story exploring the complex relationships and dynamics within a family.",
        "Quest for Self-Discovery: A character embarking on a journey to find their true purpose or identity.",
        "Betrayal and Forgiveness: A plot involving betrayal by a trusted friend or loved one, followed by a path to forgiveness.",
        "Redemption Arc: A character who starts out flawed or morally ambiguous and undergoes a transformation to become a better person.",
        "Unexpected Twist: A plot twist that subverts the reader's expectations and adds a layer of surprise.",
        "Happily Ever After: A satisfying and optimistic ending that leaves the reader feeling hopeful and content."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        commercial_fiction_additions = '''
## Commercial Fiction-Specific Writing Considerations
- **Target Audience**: Understand the demographics and preferences of your target audience (e.g., age, gender, interests) to tailor your writing accordingly. Consider current trends in commercial fiction.
- **Pacing and Suspense**: Master the art of pacing to maintain reader engagement. Use techniques like cliffhangers, foreshadowing, and red herrings to build suspense and keep readers turning the pages.
- **Emotional Connection**: Create characters and situations that evoke strong emotions in the reader. Explore universal themes and relatable experiences to foster empathy and connection.
- **Market Awareness**: Stay informed about current trends and popular tropes in commercial fiction. Analyze bestselling novels in your chosen subgenre to identify successful elements and avoid clichés.
- **Readability**: Prioritize clarity and conciseness in your writing style. Avoid overly complex language or convoluted sentence structures that could alienate readers.
- **Strong Hook**: Craft a compelling opening that immediately grabs the reader's attention and establishes the central conflict or intrigue. A strong hook is crucial for attracting readers and keeping them engaged.
- **Satisfying Resolution**: Plan a satisfying and conclusive ending that resolves the central conflict and ties up loose ends. A well-executed resolution is essential for leaving readers feeling fulfilled and recommending your book to others.
- **Emotional Payoff**: Ensure that the emotional journey of the characters culminates in a satisfying emotional payoff for the reader. This can involve catharsis, resolution of conflicts, or a sense of hope and optimism.
'''
        return base_prompt + commercial_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        commercial_fiction_additions = '''
## Commercial Fiction-Specific Outline Requirements
- **Opening Hook**: The first chapter or prologue must immediately grab the reader's attention with a compelling hook, introducing the central conflict or a captivating character.
- **Inciting Incident**: Clearly define the inciting incident that sets the protagonist on their journey and establishes the main conflict. This should occur early in the story.
- **Rising Action**: Develop a series of escalating conflicts and obstacles that challenge the protagonist and build suspense. Each scene should contribute to the overall plot and character development.
- **Midpoint Twist**: Introduce a significant plot twist or revelation at the midpoint of the story that changes the direction of the narrative and raises the stakes.
- **Climax**: Plan a high-stakes climax where the protagonist confronts the main antagonist or overcomes the central conflict. This should be the most exciting and dramatic part of the story.
- **Falling Action**: Resolve any remaining subplots or conflicts and show the immediate aftermath of the climax. This section should provide a sense of closure and transition to the resolution.
- **Resolution**: Provide a clear and satisfying resolution that ties up loose ends and leaves the reader feeling fulfilled. The ending should be consistent with the themes and tone of the story.
- **Emotional Arc**: Map out the emotional journey of the protagonist, ensuring that their feelings and motivations are clear and relatable to the reader.
- **Pacing**: Consider the pacing of each section of the outline, ensuring that the story moves at a brisk pace and maintains reader engagement. Avoid unnecessary scenes or descriptions that could slow down the narrative.
- **Subplots**: Integrate subplots that complement the main plot and add depth to the story. Subplots should be resolved in a satisfying manner and contribute to the overall themes of the novel.
'''
        return base_prompt + commercial_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        commercial_fiction_additions = '''
## Commercial Fiction-Specific Character Development
- **Relatability**: Ensure the protagonist is relatable to a broad audience. Give them flaws, vulnerabilities, and desires that readers can connect with.
- **Clear Motivation**: Define the protagonist's goals and motivations clearly. What do they want to achieve, and why is it important to them?
- **Character Arc**: Plan a compelling character arc for the protagonist, showing how they change and grow throughout the story. This arc should be believable and emotionally resonant.
- **Supporting Characters**: Develop supporting characters who are distinct and memorable. Give them their own motivations and backstories that contribute to the overall plot.
- **Antagonist**: Create a compelling antagonist who poses a significant challenge to the protagonist. The antagonist's motivations should be understandable, even if their actions are reprehensible.
- **Emotional Depth**: Explore the emotional lives of your characters, showing their feelings, fears, and hopes. This will make them more believable and engaging to readers.
- **Internal Conflict**: Give your characters internal conflicts that they must overcome. This adds depth and complexity to their personalities and makes their choices more meaningful.
- **External Conflict**: Place your characters in external conflicts that force them to make difficult decisions and test their limits. This creates tension and drives the plot forward.
- **Likeability**: While not always necessary, consider making your protagonist likeable. Readers are more likely to root for a character they admire or empathize with.
- **Backstory**: Develop a detailed backstory for each major character, explaining their past experiences and how they have shaped their present selves.
'''
        return base_prompt + commercial_fiction_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        commercial_fiction_additions = '''
## Commercial Fiction-Specific Chapter Writing
- **Clear Focus**: Each chapter should have a clear focus and contribute to the overall plot or character development. Avoid unnecessary scenes or descriptions that could slow down the narrative.
- **Strong Opening**: Start each chapter with a strong opening that grabs the reader's attention and sets the scene for what is to come.
- **Pacing**: Maintain a brisk pace throughout the chapter, using short sentences and paragraphs to keep readers engaged.
- **Conflict and Tension**: Introduce conflict or tension in each chapter to keep readers invested in the story. This could be a physical conflict, an emotional conflict, or a plot-related conflict.
- **Show, Don't Tell**: Use vivid descriptions and sensory details to show readers what is happening, rather than simply telling them.
- **Dialogue**: Write realistic and engaging dialogue that reveals character and moves the plot forward.
- **Cliffhangers**: End each chapter with a cliffhanger or a question that will keep readers turning the pages.
- **Emotional Impact**: Aim to evoke strong emotions in the reader through compelling storytelling and relatable characters.
- **Scene Setting**: Establish the setting of each scene clearly, using descriptive language to create a vivid picture in the reader's mind.
- **Character Development**: Use each chapter to further develop the characters, revealing their personalities, motivations, and relationships.
'''
        return base_prompt + commercial_fiction_additions

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_enhancement_prompt(**kwargs)

        commercial_fiction_additions = '''
## Commercial Fiction-Specific Enhancement Considerations
- **Marketability**: Assess the text for elements that enhance its marketability, such as trending themes, relatable characters, and a compelling plot.
- **Pacing**: Evaluate the pacing of the text and identify areas where it could be sped up or slowed down to maintain reader engagement.
- **Emotional Resonance**: Ensure that the text evokes strong emotions in the reader and creates a connection with the characters and their experiences.
- **Clarity**: Review the text for clarity and conciseness, ensuring that the language is accessible and easy to understand for a broad audience.
- **Suspense**: Enhance the suspense in the text by adding foreshadowing, red herrings, and cliffhangers to keep readers guessing.
- **Character Development**: Deepen the character development by adding more layers to their personalities, motivations, and relationships.
- **Plot Twists**: Consider adding unexpected plot twists to surprise readers and keep them engaged.
- **Resolution**: Ensure that the resolution is satisfying and provides closure for the reader, while also leaving them with a sense of hope or optimism.
'''
        return base_prompt + commercial_fiction_additions



    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a commercialfiction-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        commercialfiction_series_additions = """

## CommercialFiction Series-Specific Planning Elements

### Genre-Specific Series Development
- **CommercialFiction Conventions**: Ensure each book fulfills commercialfiction reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to commercialfiction
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to commercialfiction
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore commercialfiction themes with increasing depth and complexity

### CommercialFiction Series Continuity
- **Genre Elements**: Maintain consistent commercialfiction elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy commercialfiction readers
- **Series Identity**: Establish a strong series identity that feels authentically commercialfiction
- **World Building**: Develop the story world in ways that enhance the commercialfiction experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the commercialfiction genre

Create a commercialfiction series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + commercialfiction_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a commercialfiction-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        commercialfiction_book_additions = """

## CommercialFiction Series Book Integration

### CommercialFiction Continuity for This Book
- **Genre Consistency**: Maintain established commercialfiction elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to commercialfiction
- **Plot Advancement**: Continue series plot threads while telling a complete commercialfiction story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill commercialfiction reader expectations while advancing the series narrative

### Book-Specific CommercialFiction Focus
- **Central Conflict**: What commercialfiction-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new commercialfiction elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent commercialfiction while serving the series?

Ensure this book feels like an authentic continuation of the commercialfiction series while telling a complete, satisfying story.
"""
        
        return base_prompt + commercialfiction_book_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return CommercialFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return CommercialFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return CommercialFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return CommercialFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return CommercialFictionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return CommercialFictionPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return CommercialFictionPrompts.get_series_book_prompt(**kwargs)
