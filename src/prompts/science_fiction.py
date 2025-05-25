"""
Science Fiction genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class ScienceFictionPrompts(FictionBasePrompts):
    GENRE_NAME = "Science Fiction"
    GENRE_DESCRIPTION = "Science Fiction is a genre of speculative fiction dealing with imaginative and futuristic concepts such as advanced science and technology, space exploration, time travel, parallel universes, and extraterrestrial life. It often explores the potential consequences of scientific, social, and technological innovations, examining their impact on individuals, societies, and the human condition. Science fiction can range from optimistic visions of utopian futures to dystopian warnings about the dangers of unchecked progress."
    
    GENRE_CHARACTERISTICS = [
        "Plausible extrapolation: Grounding futuristic concepts in established scientific principles, even when stretching the boundaries of current knowledge.",
        "Technological focus: Featuring advanced technologies, inventions, and scientific theories that drive the plot and shape the world.",
        "Exploration of societal impact: Examining the social, political, ethical, and philosophical implications of technological advancements and scientific discoveries.",
        "World-building: Creating detailed and internally consistent fictional worlds with unique environments, cultures, and histories.",
        "Speculative elements: Introducing elements that are currently beyond the realm of possibility but are presented as potentially achievable in the future.",
        "Sense of wonder: Evoking a sense of awe and curiosity about the universe and the possibilities it holds.",
        "Dystopian or utopian settings: Exploring contrasting visions of the future, ranging from ideal societies to oppressive regimes.",
        "Extraterrestrial encounters: Featuring interactions with alien civilizations, exploring themes of first contact, cultural exchange, and interspecies conflict.",
        "Time travel paradoxes: Delving into the complexities and potential consequences of manipulating the space-time continuum.",
        "Cyberpunk themes: Exploring the intersection of technology and society, often focusing on marginalized communities and the dangers of corporate control."
    ]
    
    TYPICAL_ELEMENTS = [
        "Spaceships capable of interstellar travel.",
        "Artificial intelligence with varying degrees of sentience.",
        "Robots and androids performing diverse tasks.",
        "Cybernetic implants and enhancements.",
        "Virtual reality and augmented reality environments.",
        "Genetic engineering and manipulation.",
        "Advanced weaponry and defense systems.",
        "Dystopian societies controlled by corporations or governments.",
        "Utopian societies based on advanced technology and social harmony.",
        "Extraterrestrial civilizations with unique cultures and technologies.",
        "Time travel devices and paradoxes.",
        "Warp drives and faster-than-light communication."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        science_fiction_additions = '''
## Science Fiction-Specific Writing Considerations
- **Scientific Accuracy**: While speculative, strive for internal consistency and grounding in established scientific principles. Research relevant scientific concepts to lend credibility to your world-building. Avoid technobabble without substance.
- **World-Building Depth**: Create a detailed and believable fictional world with its own history, culture, technology, and social structures. Consider the environmental, economic, and political factors that shape your world.
- **Technological Impact**: Explore the potential consequences of technological advancements on individuals, societies, and the environment. Consider both the positive and negative impacts of technology.
- **Ethical Dilemmas**: Introduce ethical dilemmas related to scientific advancements, such as genetic engineering, artificial intelligence, and space exploration. Explore the moral implications of these technologies.
- **Character Motivation**: Ensure that your characters' motivations are believable within the context of your fictional world. Consider how their environment and experiences shape their beliefs and actions.
- **Plausible Conflict**: Create conflicts that are rooted in the social, political, or technological realities of your world. Avoid contrived conflicts that undermine the story's credibility.
- **Sense of Wonder**: Evoke a sense of awe and curiosity about the universe and the possibilities it holds. Use vivid descriptions and imaginative concepts to capture the reader's imagination.
- **Avoid Clichés**: Be mindful of common science fiction tropes and strive to create original and innovative ideas. Subvert expectations and challenge conventional thinking.
'''
        return base_prompt + science_fiction_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        science_fiction_additions = '''
## Science Fiction-Specific Outline Requirements
- **World Introduction**: The outline should clearly establish the setting, including key technological advancements, social structures, and environmental conditions.
- **Technological Premise**: The central technological or scientific concept driving the plot should be clearly defined and its implications explored.
- **Character Arcs**: Character arcs should be influenced by the technological and social environment, demonstrating how individuals adapt to or challenge the status quo.
- **Conflict Escalation**: The conflict should arise from the interplay between characters, technology, and the environment, escalating logically and plausibly.
- **Thematic Exploration**: The outline should identify the core themes being explored, such as the dangers of unchecked technological progress, the nature of humanity, or the consequences of environmental destruction.
- **Plot Twists**: Include at least one major plot twist that challenges the reader's assumptions about the world or the characters.
- **Resolution**: The resolution should provide a satisfying conclusion to the conflict while leaving the reader with a sense of wonder or contemplation about the future.
- **Subplots**: Subplots should be interwoven with the main plot, enriching the world-building and providing additional character development.
'''
        return base_prompt + science_fiction_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        science_fiction_additions = '''
## Science Fiction-Specific Character Development
- **Technological Integration**: Consider how technology has shaped the character's physical and mental abilities. Are they augmented, modified, or dependent on technology?
- **Social Standing**: Define the character's social standing within the context of the fictional world. Are they part of the ruling elite, a marginalized group, or something in between?
- **Motivations**: Explore the character's motivations in relation to the technological and social environment. Are they seeking to improve society, overthrow the government, or simply survive?
- **Flaws**: Give the character flaws that make them relatable and human, even if they are not human. These flaws should be relevant to the challenges they face in the story.
- **Skills**: Define the character's skills and abilities, both technical and interpersonal. These skills should be relevant to their role in the story.
- **Backstory**: Develop a backstory that explains how the character became who they are. This backstory should be consistent with the world-building and the character's motivations.
- **Relationships**: Explore the character's relationships with other characters, both positive and negative. These relationships should be complex and nuanced.
- **Evolution**: Show how the character changes and evolves throughout the story. This evolution should be driven by their experiences and their interactions with other characters.
'''
        return base_prompt + science_fiction_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        science_fiction_additions = '''
## Science Fiction-Specific Chapter Writing
- **World Immersion**: Begin each chapter with vivid descriptions of the setting, immersing the reader in the sights, sounds, and smells of the fictional world.
- **Technological Exposition**: Introduce new technologies and scientific concepts gradually, explaining their function and impact on the characters and the environment.
- **Character Interaction**: Focus on the interactions between characters, revealing their personalities, motivations, and relationships through dialogue and action.
- **Conflict Progression**: Advance the plot by introducing new conflicts or escalating existing ones, creating tension and suspense.
- **Thematic Resonance**: Reinforce the core themes of the story through the events and dialogue in each chapter.
- **Pacing**: Vary the pacing of each chapter to maintain reader engagement, alternating between action-packed scenes and moments of reflection.
- **Cliffhangers**: End each chapter with a cliffhanger to encourage the reader to continue reading.
- **Show, Don't Tell**: Use vivid descriptions and character actions to show the reader what is happening, rather than simply telling them.
'''
        return base_prompt + science_fiction_additions

    @classmethod
    def get_enhancement_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_enhancement_prompt(**kwargs)

        science_fiction_additions = '''
## Science Fiction-Specific Enhancement Considerations

- **Technological Detail**: Add more specific and plausible details about the technology being used, focusing on its functionality and limitations.
- **World-Building Consistency**: Ensure that all elements of the story are consistent with the established world-building, including the laws of physics and the social norms.
- **Character Depth**: Explore the characters' motivations and backstories in greater detail, revealing their inner thoughts and feelings.
- **Plot Complexity**: Introduce new subplots or twists to add complexity and intrigue to the story.
- **Thematic Resonance**: Strengthen the thematic elements of the story by adding more subtle and nuanced details.
- **Scientific Accuracy**: Verify the scientific accuracy of the story's concepts and technologies, consulting with experts if necessary.
- **Sensory Details**: Enhance the sensory details of the story, immersing the reader in the sights, sounds, smells, tastes, and textures of the fictional world.
- **Emotional Impact**: Increase the emotional impact of the story by focusing on the characters' feelings and reactions to the events that are unfolding.
'''
        return base_prompt + science_fiction_additions



    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a sciencefiction-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        sciencefiction_series_additions = """

## ScienceFiction Series-Specific Planning Elements

### Genre-Specific Series Development
- **ScienceFiction Conventions**: Ensure each book fulfills sciencefiction reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to sciencefiction
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to sciencefiction
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore sciencefiction themes with increasing depth and complexity

### ScienceFiction Series Continuity
- **Genre Elements**: Maintain consistent sciencefiction elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy sciencefiction readers
- **Series Identity**: Establish a strong series identity that feels authentically sciencefiction
- **World Building**: Develop the story world in ways that enhance the sciencefiction experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the sciencefiction genre

Create a sciencefiction series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + sciencefiction_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a sciencefiction-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        sciencefiction_book_additions = """

## ScienceFiction Series Book Integration

### ScienceFiction Continuity for This Book
- **Genre Consistency**: Maintain established sciencefiction elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to sciencefiction
- **Plot Advancement**: Continue series plot threads while telling a complete sciencefiction story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill sciencefiction reader expectations while advancing the series narrative

### Book-Specific ScienceFiction Focus
- **Central Conflict**: What sciencefiction-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new sciencefiction elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent sciencefiction while serving the series?

Ensure this book feels like an authentic continuation of the sciencefiction series while telling a complete, satisfying story.
"""
        
        return base_prompt + sciencefiction_book_additions

        ```python
        class ScienceFictionBackCover:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating a full back cover description for a Science Fiction novel.

        Args:
        **kwargs: Keyword arguments containing book details such as title, author, main character,
        setting, central conflict, themes, and target audience.  Crucially includes 'keywords'
        for targeted marketing.

        Returns:
        str: A detailed prompt string for AI content generation.
        """
        prompt = f"""
        Write a compelling and intriguing back cover description for a Science Fiction novel.

        **Book Details:**
        Title: {kwargs.get('title', '[Title]')}
        Author: {kwargs.get('author', '[Author]')}
        Main Character(s): {kwargs.get('main_character', '[Main Character(s)]')}
        Setting: {kwargs.get('setting', '[Setting - e.g., a dystopian future on Mars, a cyberpunk city, a generation ship]')}
        Central Conflict: {kwargs.get('central_conflict', '[Central Conflict - e.g., a rebellion against a tyrannical AI, a desperate search for a cure for a deadly virus, a first contact gone wrong]')}
        Themes: {kwargs.get('themes', '[Themes - e.g., artificial intelligence, transhumanism, societal collapse, exploration, the nature of consciousness]')}
        Target Audience: {kwargs.get('target_audience', '[Target Audience - e.g., fans of space operas, readers interested in hard science fiction, young adults looking for adventure]')}
        Keywords: {kwargs.get('keywords', '[Keywords - e.g., cyberpunk, space opera, dystopian, AI, alien, first contact, time travel, transhumanism, genetic engineering]')}

        **Description Guidelines:**

        *   **Genre Focus:** Emphasize the Science Fiction elements. Highlight the technological advancements, the speculative concepts, and the exploration of future possibilities or alternate realities.
        *   **Intrigue and Mystery:** Start with a hook that grabs the reader's attention. Pose a question, hint at a secret, or introduce a compelling problem.
        *   **Character Connection:** Introduce the main character(s) and their motivations. Make the reader care about their journey and their fate.  Highlight their internal struggles alongside external challenges.
        *   **World-Building:** Briefly paint a picture of the world.  Is it a utopia, a dystopia, or something in between? What are the unique aspects of this future society or alien world?  Use evocative language to bring the setting to life.
        *   **Conflict and Stakes:** Clearly define the central conflict and the stakes involved. What will happen if the protagonist(s) fail? What are the consequences for the world and its inhabitants?
        *   **Emotional Hook:** Tap into emotions like wonder, fear, hope, or despair. Science Fiction often explores complex ethical and philosophical questions, so consider incorporating these elements to add depth.
        *   **Avoid Spoilers:** Tease the plot without giving away major twists or the ending.
        *   **Call to Action:** End with a sentence or two that encourages the reader to pick up the book.  Use phrases like "Embark on a thrilling journey," "Discover the truth," or "The future hangs in the balance."
        *   **Length:** Aim for approximately 150-200 words.
        *   **Tone:** The tone should be exciting, thought-provoking, and suspenseful. Match the tone to the specific subgenre of Science Fiction (e.g., gritty for cyberpunk, optimistic for space opera).

        **Example Sentence Starters (Feel free to adapt):**

        *   "In a future where..."
        *   "When [main character] discovers..."
        *   "The fate of humanity rests on..."
        *   "On a distant planet, a hidden danger lurks..."
        *   "The line between human and machine blurs as..."
        *   "They thought they were alone, but they were wrong."
        *   "The secrets of the past hold the key to the future."

        Write a back cover description that will make readers eager to dive into this Science Fiction world.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short, punchy 2-3 line book recommendation for a Science Fiction novel.

        Args:
        **kwargs: Keyword arguments containing book details like title, author, and a brief summary.

        Returns:
        str: A prompt string for AI content generation.
        """
        prompt = f"""
        Write a short, compelling 2-3 line book recommendation for a Science Fiction novel.

        **Book Details:**
        Title: {kwargs.get('title', '[Title]')}
        Author: {kwargs.get('author', '[Author]')}
        Brief Summary: {kwargs.get('brief_summary', '[Brief Summary of the book]')}
        Keywords: {kwargs.get('keywords', '[Keywords - e.g., cyberpunk, space opera, dystopian, AI, alien, first contact, time travel, transhumanism, genetic engineering]')}

        **Guidelines:**

        *   **Conciseness:** Be extremely brief and to the point. Every word counts.
        *   **Intrigue:** Focus on the most intriguing aspect of the story.
        *   **Hook:** Grab the reader's attention immediately.
        *   **Genre Appeal:** Clearly indicate that it is Science Fiction.
        *   **Action-Oriented:** Use strong verbs and active voice.
        *   **Example:** "In a world consumed by AI, one hacker fights for humanity's survival. A thrilling cyberpunk adventure you won't want to miss."
        *   **Target Audience:** Consider who you want to attract with this recommendation.

        Write a short and powerful recommendation that will make readers want to learn more about this Science Fiction novel.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for a punchy marketing tagline for a Science Fiction novel.

        Args:
        **kwargs: Keyword arguments containing key themes, concepts, and target audience information.

        Returns:
        str: A prompt string for AI content generation.
        """
        prompt = f"""
        Write a punchy and memorable marketing tagline for a Science Fiction novel.

        **Book Details:**
        Key Themes: {kwargs.get('key_themes', '[Key Themes - e.g., AI rebellion, space exploration, time travel paradoxes]')}
        Key Concepts: {kwargs.get('key_concepts', '[Key Concepts - e.g., singularity, wormholes, genetic manipulation]')}
        Target Audience: {kwargs.get('target_audience', '[Target Audience - e.g., fans of hard sci-fi, readers interested in philosophical sci-fi]')}
        Keywords: {kwargs.get('keywords', '[Keywords - e.g., cyberpunk, space opera, dystopian, AI, alien, first contact, time travel, transhumanism, genetic engineering]')}

        **Tagline Guidelines:**

        *   **Brevity:** Keep it short and sweet – ideally under 10 words.
        *   **Impact:** Make it memorable and attention-grabbing.
        *   **Intrigue:** Hint at the story's core conflict or mystery.
        *   **Genre Focus:** Clearly communicate that it's Science Fiction.
        *   **Emotional Connection:** Evoke a feeling of wonder, excitement, or suspense.
        *   **Examples:**
        *   "The future is here. And it's terrifying."
        *   "Beyond the stars, a new war begins."
        *   "Time is a weapon. They're running out."
        *   "Humanity's last hope lies in the machine."
        *   "What if the aliens aren't who we think they are?"

        Write a tagline that will instantly capture the essence of this Science Fiction novel and entice readers.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt describing visual style preferences for the back cover design of a Science Fiction novel.

        Args:
        **kwargs: Keyword arguments containing information about the book's setting, themes, and target audience.

        Returns:
        str: A prompt string for AI content generation or for briefing a graphic designer.
        """
        prompt = f"""
        Describe the visual style preferences for the back cover design of a Science Fiction novel.

        **Book Details:**
        Setting: {kwargs.get('setting', '[Setting - e.g., a futuristic cityscape, a desolate alien planet, a sleek spaceship]')}
        Themes: {kwargs.get('themes', '[Themes - e.g., artificial intelligence, societal collapse, space exploration]')}
        Target Audience: {kwargs.get('target_audience', '[Target Audience - e.g., young adults, adults, fans of hard sci-fi]')}
        Keywords: {kwargs.get('keywords', '[Keywords - e.g., cyberpunk, space opera, dystopian, AI, alien, first contact, time travel, transhumanism, genetic engineering]')}
        Overall Tone: {kwargs.get('tone', '[Overall Tone - e.g., dark, optimistic, gritty, hopeful]')}

        **Visual Style Guidelines:**

        *   **Color Palette:** Suggest specific colors that evoke the book's atmosphere and themes.  Consider using blues and purples for a futuristic feel, or oranges and reds for a more dystopian vibe.
        *   **Imagery:** Describe the type of imagery that would be appropriate.  Should it feature spaceships, robots, alien landscapes, futuristic technology, or abstract designs? Consider the level of realism vs. stylization.  Should the imagery be photorealistic, or more stylized and artistic?
        *   **Typography:** Suggest fonts that complement the overall design.  Consider using modern, geometric fonts for a futuristic look, or more classic fonts for a retro sci-fi feel.
        *   **Layout:** Describe the desired layout of the back cover.  Should it be clean and minimalist, or more complex and layered?  How should the text and imagery be arranged to create a visually appealing and informative design?
        *   **Inspiration:** Provide examples of existing Science Fiction book covers or artwork that align with the desired visual style. Mention specific artists or designers whose work is relevant.
        *   **Overall Impression:** The back cover should convey the essence of the book and appeal to the target audience.  It should be visually striking and memorable, and it should accurately reflect the book's genre and tone.  Should it be a minimalist design or a complex and visually rich one?

        Example: "For a cyberpunk novel set in a neon-lit metropolis, the back cover should feature a dark color palette with pops of vibrant color. The imagery should depict a gritty cityscape with towering skyscrapers and flying vehicles. The typography should be modern and edgy, and the layout should be dynamic and visually engaging."

        Generate a detailed description of the visual style preferences for the back cover design, ensuring it aligns with the book's Science Fiction genre and appeals to its target audience.
        """
        return prompt
        ```
# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return ScienceFictionPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return ScienceFictionPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return ScienceFictionPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return ScienceFictionPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return ScienceFictionPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return ScienceFictionPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return ScienceFictionPrompts.get_series_book_prompt(**kwargs)
