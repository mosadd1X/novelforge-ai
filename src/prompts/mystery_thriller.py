"""
Mystery Thriller genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class MysteryThrillerPrompts(FictionBasePrompts):
    GENRE_NAME = "Mystery Thriller"
    GENRE_DESCRIPTION = "Mystery Thrillers combine the suspenseful elements of a thriller with the intricate puzzle-solving of a mystery. They typically involve a crime or a series of crimes, often violent, that the protagonist must unravel while facing escalating danger and moral dilemmas. The focus is on both the 'who' and the 'why,' with a strong emphasis on psychological tension, red herrings, and unexpected twists."

    GENRE_CHARACTERISTICS = [
        "A compelling central mystery or crime that drives the plot forward.",
        "A protagonist, often flawed or with a troubled past, who is determined to solve the mystery.",
        "A high level of suspense and tension, created through pacing, foreshadowing, and cliffhangers.",
        "Red herrings and misleading clues designed to keep the reader guessing.",
        "A complex plot with multiple layers and interconnected subplots.",
        "A sense of danger and threat, with the protagonist often facing physical or psychological peril.",
        "Moral ambiguity and ethical dilemmas for the characters, blurring the lines between right and wrong.",
        "Psychological depth, exploring the motivations and inner conflicts of the characters.",
        "A fast-paced narrative that keeps the reader engaged and on the edge of their seat.",
        "A satisfying resolution that ties up loose ends and reveals the truth behind the mystery."
    ]

    TYPICAL_ELEMENTS = [
        "A dead body or a missing person that initiates the investigation.",
        "A detective, amateur sleuth, or law enforcement officer as the protagonist.",
        "A series of clues and leads that the protagonist must follow.",
        "Interviews with suspects and witnesses to gather information.",
        "A crime scene that provides vital evidence.",
        "Red herrings that lead the protagonist down false paths.",
        "A ticking clock or deadline that adds urgency to the investigation.",
        "A conspiracy or cover-up that complicates the case.",
        "A confrontation with the antagonist or killer.",
        "A plot twist that changes the course of the investigation.",
        "A final showdown where the truth is revealed.",
        "A sense of closure and justice at the end of the story."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        mystery_thriller_additions = '''
## Mystery Thriller-Specific Writing Considerations
- **Pacing and Suspense**: Master the art of pacing to build suspense gradually. Use short, impactful sentences and cliffhangers at the end of chapters to keep readers hooked. Vary sentence length and structure to control the rhythm of the narrative.
- **Red Herrings and Misdirection**: Strategically plant red herrings to mislead the reader and create doubt. Ensure these red herrings are plausible but ultimately lead to dead ends. Avoid making them too obvious or too obscure.
- **Character Motivation and Backstory**: Develop compelling character backstories that explain their motivations and actions. Explore their inner conflicts and moral dilemmas to add depth and complexity.
- **Plot Complexity and Twists**: Craft a multi-layered plot with unexpected twists and turns. Ensure that these twists are logical and well-integrated into the story, rather than feeling arbitrary or forced.
- **Foreshadowing and Clues**: Subtly foreshadow key events and provide clues that the reader can pick up on. These clues should be subtle enough to not give away the ending but clear enough to be satisfying when revealed.
- **Atmosphere and Setting**: Create a vivid and immersive atmosphere that enhances the suspense and tension. Use descriptive language to evoke a sense of unease, danger, or mystery.
- **Dialogue and Interrogation**: Write realistic and engaging dialogue, especially during interrogations. Use dialogue to reveal character traits, advance the plot, and create conflict.
- **Research and Accuracy**: Conduct thorough research to ensure the accuracy of your portrayal of law enforcement procedures, forensic science, and other relevant details. Inaccuracies can break the reader's immersion.
'''
        return base_prompt + mystery_thriller_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        mystery_thriller_additions = '''
## Mystery Thriller-Specific Outline Requirements
- **Inciting Incident**: Clearly define the inciting incident that sets the mystery in motion (e.g., a murder, a disappearance, a theft). This should occur early in the story.
- **Rising Action (Suspense Building)**: Outline the key events that escalate the tension and raise the stakes. Include specific scenes where the protagonist encounters obstacles, uncovers clues, and faces danger.
- **Midpoint Twist**: Plan a significant plot twist or revelation at the midpoint of the story that changes the direction of the investigation and raises new questions.
- **Red Herring Placement**: Strategically place red herrings throughout the outline to mislead the reader and create doubt. Note where each red herring will be introduced and how it will be debunked.
- **Climax (Confrontation)**: Outline the climactic confrontation between the protagonist and the antagonist. This should be a high-stakes scene where the truth is revealed and the conflict is resolved.
- **Resolution (Denouement)**: Plan the resolution of the mystery, including the explanation of the crime, the capture or defeat of the antagonist, and the aftermath for the protagonist.
- **Subplot Integration**: Integrate any subplots into the main plot in a way that enhances the suspense and complexity of the story. Ensure that subplots are relevant to the central mystery.
- **Character Arc Mapping**: Map out the character arc of the protagonist, including their initial state, their transformation throughout the story, and their final state after solving the mystery.
- **Timeline Construction**: Create a detailed timeline of events, including the crime, the investigation, and the key moments in the story. This will help ensure consistency and avoid plot holes.
- **Evidence Tracking**: Keep track of all the evidence, clues, and leads that are uncovered throughout the story. Note where each piece of evidence is introduced and how it contributes to the investigation.
'''
        return base_prompt + mystery_thriller_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)

        mystery_thriller_additions = '''
## Mystery Thriller-Specific Character Development
- **Protagonist's Flaws and Strengths**: Define the protagonist's flaws and weaknesses, as well as their strengths and skills. These should be relevant to the mystery and influence their actions and decisions.
- **Antagonist's Motivation**: Develop a compelling motivation for the antagonist's actions. Explore their backstory and psychological profile to understand why they committed the crime.
- **Supporting Characters' Roles**: Define the roles of supporting characters in the investigation. Consider how they contribute to the plot, provide clues, or act as red herrings.
- **Moral Ambiguity**: Explore the moral ambiguity of the characters, blurring the lines between right and wrong. Consider how their actions are influenced by their past experiences and personal values.
- **Psychological Depth**: Delve into the psychological depth of the characters, exploring their inner conflicts, fears, and desires. Use their thoughts and emotions to create suspense and tension.
- **Character Relationships**: Develop complex and believable relationships between the characters. Consider how their interactions influence the plot and reveal their true nature.
- **Detective's Methods**: If the protagonist is a detective, define their investigative methods and techniques. Consider how they approach the case, gather evidence, and interrogate suspects.
- **Victim's Backstory**: Provide a backstory for the victim, even if they are deceased. This can add emotional weight to the story and provide clues about the motive for the crime.
- **Suspect Profiles**: Create detailed profiles for each suspect, including their background, alibi, and potential motive. Use these profiles to create red herrings and mislead the reader.
- **Character Transformation**: Consider how the characters change and evolve throughout the story. The protagonist, in particular, should undergo a significant transformation as a result of the investigation.
'''
        return base_prompt + mystery_thriller_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        mystery_thriller_additions = '''
## Mystery Thriller-Specific Chapter Writing
- **Opening Hook**: Start each chapter with a compelling hook that grabs the reader's attention and creates suspense. This could be a shocking revelation, a dangerous situation, or a mysterious clue.
- **Pacing and Tension**: Control the pacing of each chapter to build tension gradually. Use short, impactful sentences and cliffhangers at the end of the chapter to keep readers hooked.
- **Clue Revelation**: Introduce new clues and leads in each chapter, but avoid revealing too much too soon. Stagger the information to keep the reader guessing and engaged.
- **Character Interaction**: Use character interactions to reveal their personalities, motivations, and relationships. Write realistic and engaging dialogue that advances the plot.
- **Setting Description**: Use vivid descriptions of the setting to create atmosphere and enhance the suspense. Focus on details that evoke a sense of unease, danger, or mystery.
- **Internal Monologue**: Use internal monologue to reveal the protagonist's thoughts, feelings, and doubts. This can help create empathy and build suspense as they grapple with the mystery.
- **Red Herring Placement**: Strategically place red herrings in each chapter to mislead the reader and create doubt. Ensure these red herrings are plausible but ultimately lead to dead ends.
- **Cliffhanger Endings**: End each chapter with a cliffhanger that leaves the reader wanting more. This could be a shocking revelation, a dangerous situation, or a mysterious clue.
- **Show, Don't Tell**: Use the "show, don't tell" technique to bring the story to life. Instead of simply stating facts, use descriptive language and action to reveal information.
- **Point of View Consistency**: Maintain a consistent point of view throughout each chapter. Avoid head-hopping or switching perspectives without a clear reason.
'''
        return base_prompt + mystery_thriller_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a mysterythriller-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        mysterythriller_series_additions = """

## MysteryThriller Series-Specific Planning Elements

### Genre-Specific Series Development
- **MysteryThriller Conventions**: Ensure each book fulfills mysterythriller reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to mysterythriller
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to mysterythriller
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore mysterythriller themes with increasing depth and complexity

### MysteryThriller Series Continuity
- **Genre Elements**: Maintain consistent mysterythriller elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy mysterythriller readers
- **Series Identity**: Establish a strong series identity that feels authentically mysterythriller
- **World Building**: Develop the story world in ways that enhance the mysterythriller experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the mysterythriller genre

Create a mysterythriller series that builds compelling narratives with authentic genre elements and engaging character development.
"""

        return base_prompt + mysterythriller_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a mysterythriller-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        mysterythriller_book_additions = """

## MysteryThriller Series Book Integration

### MysteryThriller Continuity for This Book
- **Genre Consistency**: Maintain established mysterythriller elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to mysterythriller
- **Plot Advancement**: Continue series plot threads while telling a complete mysterythriller story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill mysterythriller reader expectations while advancing the series narrative

### Book-Specific MysteryThriller Focus
- **Central Conflict**: What mysterythriller-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new mysterythriller elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent mysterythriller while serving the series?

Ensure this book feels like an authentic continuation of the mysterythriller series while telling a complete, satisfying story.
"""

        return base_prompt + mysterythriller_book_additions

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions for
        Mystery/Thriller novels.

        Args:
        **kwargs:  Optional keyword arguments to further customize the prompt.
        Examples:
        - title (str): The title of the book.
        - author (str): The author of the book.
        - target_audience (str): Description of target audience.
        - central_mystery (str): A brief summary of the central mystery.
        - stakes (str): What's at stake if the mystery isn't solved?
        - tone (str): The overall tone of the book (e.g., gritty, suspenseful, atmospheric).
        - key_characters (list of str): List of key characters and their brief descriptions.
        - keywords (list of str): List of keywords related to the book to improve AI generation.

        Returns:
        str: A detailed prompt string to guide the AI in generating back cover copy.
        """

        title = kwargs.get('title', '[Book Title]')
        author = kwargs.get('author', '[Author Name]')
        target_audience = kwargs.get('target_audience', 'Fans of twisty thrillers and intricate mysteries.')
        central_mystery = kwargs.get('central_mystery', '[Briefly describe the central mystery of the book.]')
        stakes = kwargs.get('stakes', '[What are the consequences if the mystery remains unsolved?]')
        tone = kwargs.get('tone', 'Suspenseful and gripping.')
        key_characters = kwargs.get('key_characters', ['A flawed detective with a troubled past', 'A mysterious suspect with a hidden agenda'])
        keywords = kwargs.get('keywords', ['mystery', 'thriller', 'suspense', 'crime', 'investigation', 'secrets', 'twists', 'red herrings', 'deception'])

        prompt = f"""
        Write a compelling back cover description for the Mystery/Thriller novel, "{title}" by {author}.

        Target Audience: {target_audience}

        Central Mystery: {central_mystery}

        Stakes: {stakes}

        Overall Tone: {tone}

        Key Characters:
        {chr(10).join([f"- {char}" for char in key_characters])}

        Focus on creating a sense of suspense, intrigue, and urgency.  Hint at the dark secrets and hidden dangers lurking beneath the surface.  Don't give away the ending, but leave the reader desperate to know the truth.

        Key elements to include:

        *   **A Hook:** Start with a gripping opening line that immediately grabs the reader's attention.
        *   **Intriguing Questions:** Pose questions that the reader will want answered.  What secrets are being kept? Who can be trusted? What will happen next?
        *   **A Sense of Danger:** Highlight the potential risks and consequences faced by the characters.
        *   **Twists and Turns:** Suggest unexpected developments and shocking revelations.
        *   **Emotional Resonance:** Tap into the reader's emotions, such as fear, anxiety, or curiosity.
        *   **High Stakes:** Emphasize what the characters stand to lose if they fail.

        The description should be between 150 and 200 words.  Use vivid language and evocative imagery to create a memorable and impactful reading experience.  Use keywords: {', '.join(keywords)}.

        Examples of effective phrasing to use:

        *   "A dark secret threatens to unravel..."
        *   "In a world where nothing is as it seems..."
        *   "The clock is ticking..."
        *   "Every clue leads them closer to danger..."
        *   "But the truth comes at a price..."
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, punchy 2-3 line book recommendation for
        Mystery/Thriller novels.

        Args:
        **kwargs: Optional keyword arguments (title, author, central_theme, similar_books)

        Returns:
        str: A prompt string.
        """
        title = kwargs.get('title', '[Book Title]')
        author = kwargs.get('author', '[Author Name]')
        central_theme = kwargs.get('central_theme', '[Briefly describe the central theme of the book.]')
        similar_books = kwargs.get('similar_books', ['Gone Girl', 'The Girl on the Train'])

        prompt = f"""
        Write a short, attention-grabbing book recommendation (2-3 lines) for the Mystery/Thriller novel, "{title}" by {author}.

        Central Theme: {central_theme}

        Similar Books: {', '.join(similar_books)}

        Focus on:

        *   Creating a sense of urgency and suspense.
        *   Highlighting the unique aspects of the story.
        *   Appealing to fans of similar books.

        The recommendation should be concise and impactful, leaving the reader wanting more.  Use language that is both engaging and informative.  Emphasize the twists, turns, and psychological elements that make Mystery/Thrillers so captivating.

        Examples:

        *   "A web of lies, a desperate search for the truth. If you loved Gone Girl, you won't be able to put this down!"
        *   "When a detective's past comes back to haunt him, no one is safe. Prepare for a thrilling ride!"
        *   "Secrets, obsession, and a killer on the loose. This is one mystery you won't soon forget."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for Mystery/Thriller novels.

        Args:
        **kwargs: Optional keyword arguments (title, author, core_emotion, target_audience)

        Returns:
        str: A prompt string.
        """
        title = kwargs.get('title', '[Book Title]')
        author = kwargs.get('author', '[Author Name]')
        core_emotion = kwargs.get('core_emotion', 'Fear, suspense, and intrigue.')
        target_audience = kwargs.get('target_audience', 'Fans of fast-paced thrillers and psychological suspense.')

        prompt = f"""
        Write a punchy, memorable marketing tagline for the Mystery/Thriller novel, "{title}" by {author}.

        Core Emotion: {core_emotion}

        Target Audience: {target_audience}

        Focus on:

        *   Creating a sense of mystery and suspense.
        *   Highlighting the key themes and emotions of the story.
        *   Being short, catchy, and easy to remember.
        *   Emphasizing the unique selling points of the book.

        The tagline should be no more than 5-7 words.  Use strong verbs and evocative language to create a lasting impression. Think about the core of the story and what will resonate most with readers of the Mystery/Thriller genre.

        Examples:

        *   "Every secret has a price."
        *   "The truth will bury you."
        *   "No one can be trusted."
        *   "The past never stays buried."
        *   "Fear is the only witness."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for describing visual style preferences for the back cover design of
        Mystery/Thriller novels.

        Args:
        **kwargs: Optional keyword arguments (title, themes, color_palette, imagery)

        Returns:
        str: A prompt string.
        """
        title = kwargs.get('title', '[Book Title]')
        themes = kwargs.get('themes', 'Dark secrets, hidden identities, and dangerous obsessions.')
        color_palette = kwargs.get('color_palette', 'Dark blues, blacks, grays, and reds.')
        imagery = kwargs.get('imagery', 'Shadowy figures, crime scenes, and symbolic objects.')

        prompt = f"""
        Describe the visual style preferences for the back cover design of the Mystery/Thriller novel, "{title}".

        Themes: {themes}

        Color Palette: {color_palette}

        Imagery: {imagery}

        Focus on:

        *   Creating a sense of mystery, suspense, and danger.
        *   Using dark and moody colors to evoke a feeling of unease.
        *   Incorporating imagery that hints at the story's themes and plot.
        *   Using typography that is both legible and visually striking.
        *   Consider elements like silhouettes, blurred images, and unsettling compositions.

        The overall design should be visually arresting and create a sense of intrigue that compels readers to pick up the book.  Think about the tone and atmosphere of the story and how that can be translated into visual elements.  The design should be professional, polished, and reflective of the high-stakes nature of the genre.

        Examples:

        *   "A close-up of a single, bloodshot eye in shadow."
        *   "A silhouette of a figure running through a dark alleyway."
        *   "A shattered mirror reflecting a distorted image."
        *   "A crime scene with evidence scattered around."
        *   "A vintage key with a mysterious inscription."
        """
        return prompt

def get_writer_profile_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return MysteryThrillerPrompts.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return MysteryThrillerPrompts.get_series_book_prompt(**kwargs)
