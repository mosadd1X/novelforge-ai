"""
Novella genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class NovellaPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Novella"
    GENRE_DESCRIPTION = "A novella is a work of narrative prose fiction longer than a short story but shorter than a novel. Its length allows for more developed characters and plot than a short story, but it maintains a focused scope and intensity often absent in longer novels. Novellas often explore a single, significant event or theme in a character's life, leading to a concentrated and impactful reading experience."

    GENRE_CHARACTERISTICS = [
        "Focused Scope: Novellas typically center on a single, significant event, conflict, or transformation in a character's life, avoiding sprawling subplots or multiple perspectives.",
        "Limited Cast: The number of characters is usually smaller compared to a novel, allowing for deeper exploration of their motivations and relationships.",
        "Concise Plot: The plot is streamlined and efficient, with minimal digressions or unnecessary details, driving directly towards a resolution.",
        "Intense Atmosphere: Novellas often create a strong sense of atmosphere or mood, contributing to the overall impact of the story.",
        "Significant Character Arc: While the plot may be simple, the protagonist often undergoes a significant change or realization by the story's end.",
        "Unified Theme: A central theme or idea is explored in depth, providing a cohesive and meaningful reading experience.",
        "Fast Pacing: Compared to novels, novellas tend to have a quicker pace, maintaining reader engagement through focused storytelling.",
        "Single Setting: Many novellas take place primarily in a single location or a limited number of settings, enhancing the sense of intimacy and focus.",
        "Exploration of a Moral Dilemma: Novellas often present characters facing difficult moral choices, exploring the complexities of human nature.",
        "Subtle Symbolism: Novellas frequently employ symbolism to enrich the narrative and add layers of meaning."
    ]

    TYPICAL_ELEMENTS = [
        "A clear inciting incident that sets the plot in motion.",
        "A protagonist with a distinct flaw or vulnerability.",
        "A central conflict that drives the narrative forward.",
        "A limited number of supporting characters who play crucial roles.",
        "A well-defined setting that contributes to the story's atmosphere.",
        "A rising action that builds tension and suspense.",
        "A climax that represents the peak of the conflict.",
        "A resolution that provides closure to the main storyline.",
        "A thematic exploration of a universal human experience.",
        "Use of vivid imagery and sensory details to create a strong sense of place and atmosphere.",
        "Internal monologue or flashbacks to reveal character motivations and backstories.",
        "Symbolic elements that add depth and meaning to the narrative."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        novella_additions = '''
## Novella-Specific Writing Considerations
- **Pacing and Economy**: Maintain a brisk pace, ensuring every scene and sentence contributes to the overall narrative. Avoid unnecessary exposition or digressions.
- **Character Focus**: Prioritize depth over breadth in character development. Focus on a small number of characters and explore their motivations and inner lives thoroughly.
- **Thematic Resonance**: Ensure the story's theme is subtly woven throughout the narrative, emerging organically from the plot and character interactions.
- **Atmospheric Detail**: Use vivid language and sensory details to create a strong sense of atmosphere and immerse the reader in the story's world.
- **Structural Integrity**: Pay close attention to the novella's structure, ensuring a clear beginning, rising action, climax, and resolution. The shorter length demands a tight, well-constructed plot.
- **Impactful Ending**: Craft an ending that is both satisfying and thought-provoking, leaving a lasting impression on the reader. Consider the emotional resonance and thematic implications of the final scene.
- **Subtext and Symbolism**: Employ subtext and symbolism to add layers of meaning to the narrative, enriching the reader's experience and encouraging deeper interpretation.
- **Revision and Refinement**: Given the novella's concise nature, meticulous revision is crucial. Pay attention to every word and sentence, ensuring clarity, precision, and impact.
'''
        return base_prompt + novella_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        novella_additions = '''
## Novella-Specific Outline Requirements
- **Inciting Incident**: Clearly define the event that sets the story in motion and disrupts the protagonist's status quo. This should occur early in the novella.
- **Rising Action (3-5 Key Scenes)**: Outline 3-5 key scenes that build tension and develop the central conflict. Each scene should escalate the stakes and reveal more about the characters and their motivations.
- **Midpoint Shift**: Identify a turning point or significant event that alters the direction of the plot and raises the stakes even higher. This should occur roughly halfway through the novella.
- **Climax**: Plan a single, decisive climax that represents the peak of the conflict. This should be a high-stakes scene with significant consequences for the protagonist.
- **Falling Action (2-3 Key Scenes)**: Outline 2-3 key scenes that show the immediate aftermath of the climax and begin to resolve the central conflict.
- **Resolution**: Define a clear resolution that provides closure to the main storyline and reveals the protagonist's transformation.
- **Thematic Elements**: Identify specific scenes or moments where the novella's central theme will be explored and reinforced.
- **Character Arc Milestones**: Outline key moments in the protagonist's journey that demonstrate their growth or change throughout the story.
- **Setting Integration**: Plan how the setting will be used to enhance the story's atmosphere and contribute to the overall narrative.
- **Word Count Targets**: Break down the outline into approximate word count targets for each section (e.g., Inciting Incident: 500 words, Rising Action: 2000 words, etc.) to ensure the novella stays within its target length.
'''
        return base_prompt + novella_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character development prompt specifically for novellas."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")
        target_audience = kwargs.get("target_audience", "Adult")
        subplot_info = kwargs.get("subplot_info", "")

        return f"""
# Novella Character Development

Create a focused set of characters for the novella "{title}" for {target_audience}.

## Novella Information
- Title: {title}
- Description: {description}
- Genre: Novella
- Target Audience: {target_audience}

## Story Outline
{outline}

{subplot_info}

## Novella Character Requirements

### Character Development Guidelines
1. **Focused Cast**: Novellas require a small, focused cast of essential characters only
2. **Protagonist's Central Flaw**: The main character should have a specific flaw that drives the story
3. **Limited Supporting Cast**: Include only supporting characters crucial to the protagonist's journey
4. **Clear Relationships**: Define key relationships and how they evolve throughout the story
5. **Internal Motivations**: Explore what drives each character's actions and decisions
6. **Relevant Backstory**: Include only backstory directly relevant to the plot and motivations
7. **Character Transformation**: Plan clear character growth and what triggers it

### Character Types for Novellas
- **Protagonist**: 1 main character with a clear arc and central flaw
- **Key Supporting Characters**: 2-3 characters essential to the protagonist's journey
- **Antagonist/Obstacle**: 1 character or force that creates conflict
- **Catalyst Character**: 1 character who triggers change or revelation

## Character Object Format
For each character, provide the following fields in a JSON object:
- "name": (string) Character's full name
- "role": (string) Their role (protagonist, supporting, antagonist, catalyst)
- "appearance": (string) Concise but memorable physical description
- "personality": (string) Key personality traits focused on story relevance
- "background": (string) Essential backstory that directly impacts the plot
- "goals": (string) What they want to achieve in the story
- "arc": (string) How they change or develop throughout the novella
- "relationships": (string) Key relationships with other characters
- "strengths": (string) Their abilities and positive traits
- "flaws": (string) Their central flaw or vulnerability (especially for protagonist)
- "voice": (string) Their distinctive speech patterns and dialogue style
- "motivation": (string) Internal drives and desires that fuel their actions
- "obstacles": (string) What stands in their way or creates conflict
- "transformation": (string) Specific events or realizations that trigger character growth

## Novella Guidelines
- Keep the cast small and focused on essential characters only
- Each character should serve a specific purpose in the story
- Focus on one main character arc with clear development
- Ensure characters can be fully developed within the novella's length
- Avoid unnecessary characters or subplots that don't serve the main story

Return ONLY a valid JSON array of character objects, nothing else.
Example format:
[
  {{
    "name": "Elena Rodriguez",
    "role": "protagonist",
    "appearance": "A woman in her thirties with tired eyes and paint-stained fingers",
    "personality": "Creative and passionate, but struggles with self-doubt and perfectionism",
    "background": "Former art teacher who left her job to pursue painting full-time",
    "goals": "To complete her first solo art exhibition and prove her worth as an artist",
    "arc": "Learns to embrace imperfection and find confidence in her unique artistic voice",
    "relationships": "Estranged from her practical sister, mentored by an elderly gallery owner",
    "strengths": "Artistic talent, determination, empathy for others' struggles",
    "flaws": "Perfectionism that paralyzes her creativity, fear of failure and judgment",
    "voice": "Thoughtful and introspective, uses art metaphors when explaining emotions",
    "motivation": "Deep need to prove she made the right choice leaving teaching",
    "obstacles": "Financial pressure, self-doubt, competitive art world",
    "transformation": "A failed painting leads her to discover beauty in imperfection"
  }}
]
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        novella_additions = '''
## Novella-Specific Chapter Writing
- **Focused Scene Objectives**: Each chapter should have a clear objective that contributes to the overall plot and character development. Avoid aimless or meandering scenes.
- **Pacing and Tension**: Maintain a brisk pace throughout each chapter, building tension and suspense with each scene. Use cliffhangers or unresolved conflicts to keep the reader engaged.
- **Concise Descriptions**: Use vivid language and sensory details to create a strong sense of place and atmosphere, but avoid lengthy or unnecessary descriptions.
- **Dialogue Purpose**: Ensure that all dialogue serves a purpose, whether it's to reveal character traits, advance the plot, or create conflict.
- **Show, Don't Tell**: Use actions, dialogue, and internal monologue to reveal information and develop characters, rather than simply stating it outright.
- **Chapter Endings**: End each chapter with a hook or a question that compels the reader to continue reading.
- **Word Count Awareness**: Be mindful of the overall word count and ensure that each chapter contributes to the novella's target length.
- **Transitions**: Use smooth transitions between scenes and chapters to maintain the flow of the narrative.
'''
        return base_prompt + novella_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a novella-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        novella_series_additions = """

## Novella Series-Specific Planning Elements

### Artistic Progression for Novella
- **Format Mastery**: Show increasing sophistication in novella techniques across volumes
- **Creative Evolution**: Plan how the artistic vision develops throughout the novella series
- **Thematic Development**: Create themes that deepen and evolve through the novella format
- **Artistic Cohesion**: Maintain unified artistic vision while allowing creative growth
- **Format Innovation**: Explore different aspects of novella across the series

### Novella Series Continuity
- **Style Consistency**: Maintain recognizable artistic voice across novella volumes
- **Technical Standards**: Maintain quality standards appropriate for novella
- **Creative Connections**: Create meaningful artistic links between novella volumes
- **Format Exploration**: Continue exploring the possibilities of novella format
- **Reader Experience**: Create engaging progression for novella enthusiasts

Create a novella series that showcases artistic development and format mastery across multiple volumes.
"""

        return base_prompt + novella_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a novella-specific individual volume prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class NovellaMarketing:
        """
        A class containing methods for generating marketing materials specifically
        tailored for the Novella genre.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions
        for Novellas.

        Args:
        **kwargs: Keyword arguments to pass genre-specific details.

        Returns:
        str: A detailed prompt string for AI content generation.
        """
        prompt = f"""
        Create a captivating back cover description for a novella.  Remember, novellas are all about impact.
        They offer a concentrated dose of story, focusing on a specific theme, character arc, or pivotal event.

        **Genre:** Novella

        **Guidelines:**

        *   **Brevity is Key:** The description must be concise and engaging, reflecting the novella's shorter length. Aim for approximately 150-200 words. Every word must count.

        *   **Intrigue and Mystery:**  Hook the reader immediately. Pose a compelling question or hint at a central conflict that drives the narrative. Don't give away too much.

        *   **Highlight the Core Theme:** Clearly identify the central theme or message of the novella. Is it about love, loss, redemption, revenge, self-discovery, or something else? Make this theme resonant.

        *   **Character Focus:** Emphasize the protagonist's internal struggles and their journey. What are their motivations, flaws, and desires?  Show the reader why they should care about this character.

        *   **Emotional Resonance:** Novellas often pack a powerful emotional punch. Evoke the feelings and atmosphere of the story. Use vivid language and sensory details to immerse the reader.

        *   **Unique Selling Proposition:** What makes this novella stand out from others in its subgenre (e.g., science fiction, fantasy, romance, thriller)?  Is it a unique premise, a compelling voice, or a surprising twist?

        *   **End with a Hook:** Leave the reader wanting more. End the description with a question or a cliffhanger that compels them to open the book and start reading.

        **Input:**

        *   **Title:** {kwargs.get('title', '[Title of Novella]')}
        *   **Author:** {kwargs.get('author', '[Author Name]')}
        *   **Genre/Subgenre:** {kwargs.get('genre', '[e.g., Historical Romance, Sci-Fi Thriller, Literary Fiction]')}
        *   **Main Character(s):** {kwargs.get('main_characters', '[Brief description of main characters]')}
        *   **Setting:** {kwargs.get('setting', '[Time and place of the story]')}
        *   **Core Conflict:** {kwargs.get('core_conflict', '[Central problem or challenge the character faces]')}
        *   **Theme(s):** {kwargs.get('themes', '[Main themes explored in the novella]')}
        *   **Target Audience:** {kwargs.get('target_audience', '[Who is most likely to enjoy this novella?]')}
        *   **Keywords:** {kwargs.get('keywords', '[Keywords related to plot, setting, theme, etc. for SEO]')}

        **Example Structure:**

        [Opening hook - a question or intriguing statement]

        [Briefly introduce the main character(s) and their situation.]

        [Describe the central conflict and the stakes involved.]

        [Highlight the emotional impact and thematic resonance of the story.]

        [End with a compelling question or cliffhanger.]

        **Tone:**  [Specify the desired tone: e.g., suspenseful, romantic, humorous, thought-provoking, dark, hopeful]

        Write a description that makes the reader feel like they absolutely NEED to read this novella right now.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, 2-3 line book recommendation
        specifically for Novellas.

        Args:
        **kwargs: Keyword arguments to pass genre-specific details.

        Returns:
        str: A detailed prompt string for AI content generation.
        """
        prompt = f"""
        Create a concise, 2-3 line book recommendation for a novella. This should be used for social media,
        email marketing, or online retailers where space is limited.

        **Genre:** Novella

        **Guidelines:**

        *   **Focus on Impact:** Emphasize the concentrated storytelling and emotional resonance that novellas offer.
        *   **Highlight the Unique Selling Point:** What makes this novella stand out?
        *   **Intrigue and Hook:** Grab the reader's attention immediately.
        *   **Target Audience:** Keep the target audience in mind.

        **Input:**

        *   **Title:** {kwargs.get('title', '[Title of Novella]')}
        *   **Author:** {kwargs.get('author', '[Author Name]')}
        *   **Genre/Subgenre:** {kwargs.get('genre', '[e.g., Historical Romance, Sci-Fi Thriller, Literary Fiction]')}
        *   **Core Theme:** {kwargs.get('core_theme', '[Central theme of the novella]')}
        *   **Target Audience:** {kwargs.get('target_audience', '[Who is most likely to enjoy this novella?]')}

        **Example:**

        "A gripping [Genre] novella about [Main Character] facing [Core Conflict]. Perfect for readers who love fast-paced stories with a powerful emotional punch."

        **Tone:** [Specify the desired tone: e.g., Exciting, Romantic, Thought-provoking, Suspenseful]

        Craft a short description that convinces someone to read this novella immediately.
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for Novellas.

        Args:
        **kwargs: Keyword arguments to pass genre-specific details.

        Returns:
        str: A detailed prompt string for AI content generation.
        """
        prompt = f"""
        Create a short, memorable, and impactful marketing tagline for a novella.

        **Genre:** Novella

        **Guidelines:**

        *   **Brevity is Essential:** Taglines should be extremely short and easy to remember.
        *   **Highlight the Essence:** Capture the core theme or conflict of the novella.
        *   **Intrigue and Emotion:** Evoke curiosity and emotional resonance.
        *   **Target Audience:** Tailor the tagline to appeal to the target audience.
        *   **Consider the emotional hook:** What feeling does this novella evoke?

        **Input:**

        *   **Title:** {kwargs.get('title', '[Title of Novella]')}
        *   **Author:** {kwargs.get('author', '[Author Name]')}
        *   **Genre/Subgenre:** {kwargs.get('genre', '[e.g., Historical Romance, Sci-Fi Thriller, Literary Fiction]')}
        *   **Core Theme:** {kwargs.get('core_theme', '[Central theme of the novella]')}
        *   **Target Audience:** {kwargs.get('target_audience', '[Who is most likely to enjoy this novella?]')}
        *   **Emotional Hook:** {kwargs.get('emotional_hook', '[The primary emotion the novella evokes: e.g., hope, fear, love, sadness]')}

        **Examples:**

        *   "A short story. A lifetime impact."
        *   "Intense. Immersive. Unforgettable."
        *   "Get lost in a world in a single sitting."
        *   "A novella of [Emotion]."

        **Tone:** [Specify the desired tone: e.g., Dramatic, Romantic, Mysterious, Bold]

        Craft a tagline that grabs attention and makes people want to know more about this novella.
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for guiding the visual design of the back cover for
        a Novella.

        Args:
        **kwargs: Keyword arguments to pass genre-specific details.

        Returns:
        str: A detailed prompt string for AI content generation.
        """
        prompt = f"""
        Describe the desired visual style for the back cover of a novella. Consider the novella's genre,
        themes, and target audience.

        **Genre:** Novella

        **Guidelines:**

        *   **Reflect the Story's Essence:** The visual style should complement the tone and themes of the novella.
        *   **Simplicity and Impact:** Given the novella's shorter length, the design should be clean and impactful. Avoid clutter.
        *   **Target Audience Appeal:** The design should resonate with the target audience.
        *   **Consider Cover Art Integration:** How will the back cover design complement the front cover art?
        *   **Typography:** Specify font styles, sizes, and colors.

        **Input:**

        *   **Title:** {kwargs.get('title', '[Title of Novella]')}
        *   **Author:** {kwargs.get('author', '[Author Name]')}
        *   **Genre/Subgenre:** {kwargs.get('genre', '[e.g., Historical Romance, Sci-Fi Thriller, Literary Fiction]')}
        *   **Core Theme:** {kwargs.get('core_theme', '[Central theme of the novella]')}
        *   **Target Audience:** {kwargs.get('target_audience', '[Who is most likely to enjoy this novella?]')}
        *   **Cover Art Style:** {kwargs.get('cover_art_style', '[Description of the front cover art style]')}
        *   **Color Palette:** {kwargs.get('color_palette', '[Desired color scheme for the back cover]')}
        *   **Imagery:** {kwargs.get('imagery', '[Any specific imagery or symbols to incorporate: e.g., a silhouette, a specific object, a landscape]')}
        *   **Typography:** {kwargs.get('typography', '[Font styles and sizes to use]')}
        *   **Overall Mood:** {kwargs.get('overall_mood', '[The desired mood or feeling conveyed by the back cover: e.g., mysterious, romantic, suspenseful, elegant]')}

        **Examples:**

        *   "For a dark fantasy novella, use a gothic-inspired font, a dark color palette (e.g., black, deep purple, silver), and incorporate imagery of ravens or shadows."
        *   "For a contemporary romance novella, use a clean and modern font, a warm color palette (e.g., pastel pinks, soft blues), and incorporate imagery of flowers or a couple holding hands."

        Describe the visual style in detail, including specific examples and references if possible.  Consider the overall aesthetic and how it will attract the right readers.
        """
        return prompt
        ```
        novella_book_additions = """

## Novella Series Volume Integration

### Novella Artistic Continuity
- **Style Consistency**: Maintain the artistic voice established in previous novella volumes
- **Technical Standards**: Maintain quality standards established in the novella series
- **Creative Evolution**: Show artistic growth from previous novella volumes
- **Format Mastery**: Build upon novella techniques established in the series
- **Thematic Connections**: Continue developing themes from earlier novella works

### Volume-Specific Novella Focus
- **Artistic Objectives**: What specific novella artistic goals will this volume achieve?
- **Format Innovation**: What new novella techniques or approaches will be introduced?
- **Creative Development**: How will this volume advance the artistic vision of the series?
- **Series Integration**: How does this volume connect meaningfully to other novella works in the series?
- **Artistic Value**: What unique novella artistic value does this volume add to the series?

Ensure this volume demonstrates novella mastery while serving as an integral part of the artistic series.
"""

        return base_prompt + novella_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return NovellaPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return NovellaPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return NovellaPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return NovellaPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return NovellaPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return NovellaPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return NovellaPrompts.get_series_book_prompt(**kwargs)
