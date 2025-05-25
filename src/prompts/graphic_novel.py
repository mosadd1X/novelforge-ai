"""
Graphic Novel genre-specific prompts for novel generation.
"""

from .base_prompts import SpecialFormatBasePrompts

class GraphicNovelPrompts(SpecialFormatBasePrompts):
    GENRE_NAME = "Graphic Novel"
    GENRE_DESCRIPTION = "A graphic novel is a narrative told through sequential art, combining illustrations and text to create a cohesive and engaging story. It is a longer-form work, typically more complex and sophisticated than a comic book, often exploring mature themes and complex character development. The visual storytelling is as crucial as the written narrative, with panel layouts, character design, and visual metaphors contributing significantly to the overall meaning and impact."

    GENRE_CHARACTERISTICS = [
        "Sequential Art: The story is told through a sequence of panels, each containing images and text that build upon each other to create a narrative flow.",
        "Panel Layout: The arrangement of panels on a page is a deliberate artistic choice that influences the pacing and emotional impact of the story.",
        "Visual Storytelling: The artwork conveys information, emotions, and subtext that may not be explicitly stated in the dialogue or narration.",
        "Character Design: The visual appearance of characters is carefully crafted to reflect their personality, background, and role in the story.",
        "Word Balloons and Captions: Dialogue and narration are presented in word balloons and captions, which are strategically placed within the panels to guide the reader's eye.",
        "Color Palette: The use of color can evoke specific moods, highlight important details, and establish the overall tone of the graphic novel.",
        "Themes and Symbolism: Graphic novels often explore complex themes and utilize visual symbolism to add layers of meaning to the story.",
        "Pacing and Rhythm: The combination of panel size, layout, and content creates a unique pacing and rhythm that controls the reader's experience.",
        "Genre Blending: Graphic novels can encompass a wide range of genres, from superhero stories and science fiction to historical fiction and memoirs.",
        "Target Audience: While often associated with younger readers, graphic novels cater to a diverse audience, including adults, with stories that address mature themes and complex issues."
    ]

    TYPICAL_ELEMENTS = [
        "Opening Scene: A visually compelling scene that introduces the main character(s) and establishes the setting and tone of the story.",
        "Inciting Incident: An event that disrupts the protagonist's normal life and sets them on a journey or quest.",
        "Character Introductions: Visual and textual introductions to key characters, revealing their personalities, motivations, and relationships.",
        "Panel Transitions: Deliberate choices in how panels connect to create a smooth and engaging reading experience (e.g., gutter space, panel shape).",
        "Dialogue and Narration: Well-written dialogue that reveals character and advances the plot, combined with concise and informative narration.",
        "Visual Metaphors: Symbolic imagery that represents abstract concepts or emotions, adding depth and complexity to the story.",
        "Action Sequences: Dynamic and visually exciting action scenes that showcase the characters' abilities and drive the plot forward.",
        "Emotional Moments: Panels that focus on characters' emotions, using facial expressions, body language, and visual cues to convey their feelings.",
        "Climax: A pivotal moment in the story where the protagonist faces their greatest challenge.",
        "Resolution: The aftermath of the climax, where the conflict is resolved and the characters' lives are changed.",
        "Epilogue (Optional): A final scene that provides closure and hints at the future of the characters and the world.",
        "Endpapers and Cover Art: Visually striking cover art and endpapers that capture the essence of the story and attract readers."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)

        graphic_novel_additions = '''
## Graphic Novel-Specific Writing Considerations
- **Visual Storytelling Expertise**: Demonstrate a strong understanding of visual storytelling techniques, including panel layout, composition, and character design.  Explain your ability to convey emotion and information through images, not just words.
- **Sequential Art Knowledge**: Showcase familiarity with the principles of sequential art and how to create a cohesive and engaging narrative flow through panels.
- **Character Design Skills**: Describe your approach to character design, including how you create visually distinct and memorable characters that reflect their personalities and roles in the story.
- **Dialogue and Narration Balance**: Explain how you balance dialogue and narration to create a compelling and informative narrative that complements the visual storytelling.
- **Pacing and Rhythm Control**: Detail your understanding of how panel size, layout, and content affect the pacing and rhythm of the story, and how you use these elements to control the reader's experience.
- **Collaboration with Artists**: If applicable, describe your experience collaborating with artists and how you communicate your vision effectively to ensure a cohesive and visually stunning final product.
- **Understanding of Genre Conventions**: Demonstrate a strong understanding of the conventions of the specific genre you are writing in (e.g., superhero, science fiction, fantasy) and how to use them effectively to create a compelling story.
- **Adaptation Skills**: If adapting existing material, describe your experience and approach to translating a novel, screenplay, or other source material into a visual narrative format.
'''
        return base_prompt + graphic_novel_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)

        graphic_novel_additions = '''
## Graphic Novel-Specific Outline Requirements
- **Panel Breakdown**: Include a detailed breakdown of each chapter into individual panels, describing the visual content, dialogue, and narration for each panel.
- **Page Layout Considerations**: Specify the desired page layout for each chapter, including the number of panels per page and their arrangement. Consider the visual impact and pacing of each page.
- **Visual Storytelling Notes**: Add notes on how to convey specific emotions, information, or subtext through visual elements, such as character expressions, body language, and symbolic imagery.
- **Character Design Sketches**: Include preliminary character design sketches to visualize the characters' appearances and ensure consistency throughout the graphic novel.
- **Setting and Environment Descriptions**: Provide detailed descriptions of the settings and environments, including visual references and notes on how to create a believable and immersive world.
- **Action Sequence Storyboarding**: For action sequences, create storyboards that outline the key moments and visual transitions, ensuring a dynamic and engaging reading experience.
- **Color Palette Planning**: Outline the intended color palette for each chapter or scene, considering the emotional impact and thematic significance of the colors used.
- **Panel Transition Types**: Specify the types of panel transitions to be used (e.g., moment-to-moment, action-to-action, scene-to-scene) and how they contribute to the overall flow of the story.
- **Visual Metaphor Identification**: Identify key visual metaphors to be used throughout the graphic novel and explain their symbolic meaning.
- **Pacing and Rhythm Markers**: Indicate points in the outline where the pacing should be accelerated or slowed down to create a desired emotional effect.
'''
        return base_prompt + graphic_novel_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a character development prompt specifically for graphic novels."""
        title = kwargs.get("title", "Untitled")
        description = kwargs.get("description", "")
        outline = kwargs.get("outline", "")
        target_audience = kwargs.get("target_audience", "Adult")
        subplot_info = kwargs.get("subplot_info", "")

        return f"""
# Graphic Novel Character Development

Create a set of visually compelling characters for the graphic novel "{title}" for {target_audience}.

## Graphic Novel Information
- Title: {title}
- Description: {description}
- Genre: Graphic Novel
- Target Audience: {target_audience}

## Story Outline
{outline}

{subplot_info}

## Graphic Novel Character Requirements

### Visual Character Guidelines
1. **Visual Representation**: Characters must be designed for visual storytelling with distinctive, memorable appearances
2. **Expressive Design**: Characters should be capable of conveying emotions through facial expressions and body language
3. **Distinctive Silhouettes**: Each character should have a unique silhouette that makes them instantly recognizable
4. **Visual Archetypes**: Characters should embody clear visual archetypes while maintaining originality
5. **Costume/Clothing Design**: Outfits should reflect personality, role, and story context
6. **Visual Motifs**: Each character should have associated visual elements (colors, symbols, objects)
7. **Sequential Art Compatibility**: Characters must work well across multiple panels and pages

### Character Types for Graphic Novels
- **Protagonists**: 1-2 main characters with strong visual presence and clear character arcs
- **Antagonists**: 1-2 opposing characters with compelling visual design and motivations
- **Supporting Characters**: 3-4 characters who enhance the story and provide visual variety
- **Visual Ensemble**: Characters should work together as a cohesive visual cast

## Character Object Format
For each character, provide the following fields in a JSON object:
- "name": (string) Character's full name
- "role": (string) Their role (protagonist, antagonist, supporting, etc.)
- "appearance": (string) Detailed visual description including distinctive features, clothing, and design elements
- "personality": (string) Key personality traits that can be expressed visually
- "background": (string) Essential backstory that informs their visual design and motivations
- "goals": (string) Primary objectives that drive their actions in the story
- "arc": (string) Character development and how their appearance might evolve
- "relationships": (string) How they relate to other characters visually and emotionally
- "strengths": (string) Their abilities and positive traits
- "flaws": (string) Their weaknesses and vulnerabilities
- "voice": (string) Their speech patterns and dialogue style
- "visual_motifs": (string) Colors, symbols, or design elements associated with this character
- "expressions": (string) Typical facial expressions and body language
- "costume_design": (string) Detailed description of their clothing/costume and its significance

## Graphic Novel Guidelines
- Characters should be visually distinctive and memorable
- Each character should have a unique visual identity
- Consider how characters will look in action sequences and quiet moments
- Ensure characters can convey emotion through visual design
- Plan for character interactions and visual chemistry

Return ONLY a valid JSON array of character objects, nothing else.
Example format:
[
  {{
    "name": "Maya Chen",
    "role": "protagonist",
    "appearance": "Petite Asian woman in her late twenties with short, asymmetrical black hair with blue streaks. Wears practical dark clothing with tech accessories",
    "personality": "Determined and tech-savvy, but struggles with trust and emotional vulnerability",
    "background": "Former corporate hacker turned freelance investigator after exposing corruption",
    "goals": "Wants to uncover the truth behind a conspiracy while protecting innocent people",
    "arc": "Learns to trust others and work as part of a team rather than alone",
    "relationships": "Initially distrustful but gradually opens up to allies",
    "strengths": "Technical expertise, problem-solving, determination",
    "flaws": "Paranoid, difficulty trusting others, tendency to work alone",
    "voice": "Direct and precise, uses technical jargon when nervous",
    "visual_motifs": "Blue color scheme, circuit patterns, geometric designs",
    "expressions": "Intense focus when working, guarded expressions in social situations",
    "costume_design": "Dark tactical clothing with blue accents, multiple pockets for tech gear, fingerless gloves"
  }}
]
"""

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)

        graphic_novel_additions = '''
## Graphic Novel-Specific Chapter Writing
- **Panel Composition**: Focus on creating visually dynamic and engaging panel compositions that guide the reader's eye and convey the intended mood and information.
- **Dialogue Placement**: Strategically place dialogue balloons within the panels to avoid obscuring important visual elements and to create a natural reading flow.
- **Sound Effects**: Use onomatopoeia and other visual sound effects to enhance the action and create a more immersive reading experience.
- **Visual Pacing**: Vary the size and layout of panels to control the pacing of the story, using larger panels for important moments and smaller panels for quick transitions.
- **Show, Don't Tell (Visually)**: Rely on visual storytelling to convey information and emotions, rather than relying solely on dialogue or narration.
- **Character Expressions**: Pay close attention to the characters' facial expressions and body language, using these visual cues to convey their emotions and intentions.
- **Setting and Atmosphere**: Create a believable and immersive setting through detailed backgrounds and atmospheric effects, such as lighting, shadows, and weather.
- **Visual Symbolism**: Incorporate visual symbols and metaphors to add layers of meaning to the story and enhance its thematic resonance.
- **Panel Transitions**: Use a variety of panel transitions to create a smooth and engaging reading experience, while also varying the pace and rhythm of the story.
- **Collaboration with Artist (if applicable)**: Maintain clear and consistent communication with the artist to ensure that your vision is accurately translated into the visual medium.
'''
        return base_prompt + graphic_novel_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a graphicnovel-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        graphicnovel_series_additions = """

## GraphicNovel Series-Specific Planning Elements

### Artistic Progression for GraphicNovel
- **Format Mastery**: Show increasing sophistication in graphicnovel techniques across volumes
- **Creative Evolution**: Plan how the artistic vision develops throughout the graphicnovel series
- **Thematic Development**: Create themes that deepen and evolve through the graphicnovel format
- **Artistic Cohesion**: Maintain unified artistic vision while allowing creative growth
- **Format Innovation**: Explore different aspects of graphicnovel across the series

### GraphicNovel Series Continuity
- **Style Consistency**: Maintain recognizable artistic voice across graphicnovel volumes
- **Technical Standards**: Maintain quality standards appropriate for graphicnovel
- **Creative Connections**: Create meaningful artistic links between graphicnovel volumes
- **Format Exploration**: Continue exploring the possibilities of graphicnovel format
- **Reader Experience**: Create engaging progression for graphicnovel enthusiasts

Create a graphicnovel series that showcases artistic development and format mastery across multiple volumes.
"""

        return base_prompt + graphicnovel_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a graphicnovel-specific individual volume prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class GraphicNovelMarketing:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover copy for a Graphic Novel.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, main character, plot summary, themes, target audience, etc.).

        Returns:
        A string containing the prompt for back cover copy generation.
        """
        prompt = f"""
        Create compelling back cover copy for a Graphic Novel titled "{kwargs.get('title', '[Title]')}".
        Written by {kwargs.get('author', '[Author]')}.

        Genre: Graphic Novel (emphasize visual storytelling, sequential art, and panel-by-panel narrative)

        Target Audience: {kwargs.get('target_audience', '[Target Audience - e.g., Young Adult, Adults, fans of specific genres]')}.
        Consider age range and interests. Is it appropriate for all ages, or does it have mature themes?

        Main Character(s): {kwargs.get('main_character', '[Main Character(s) - Name, brief description, and key traits]')}.
        Highlight their personality, motivations, and internal conflicts. Focus on visual distinctiveness - what makes them recognizable in the art?

        Plot Summary: {kwargs.get('plot_summary', '[Detailed plot summary - beginning, rising action, climax, resolution]')}.
        Focus on the most visually arresting moments and the central conflict. Emphasize the unique storytelling possibilities offered by the graphic novel format.

        Key Themes: {kwargs.get('themes', '[List of themes - e.g., identity, loss, redemption, power, social justice]')}.
        How are these themes explored visually and through dialogue?

        Emotional Hook: What emotions should the back cover evoke? (e.g., excitement, mystery, empathy, fear, hope).

        Visual Style: {kwargs.get('visual_style', '[Description of the art style - e.g., Manga, realistic, stylized, watercolor, black and white]')}.
        How does the art style contribute to the story's mood and atmosphere? Mention if it draws inspiration from specific artists or comics.

        Instructions:

        *   Craft a narrative hook that immediately grabs the reader's attention. Start with a question, a shocking statement, or an intriguing scene.
        *   Show, don't tell. Use vivid language that hints at the visual spectacle within the pages.
        *   Highlight the unique advantages of the graphic novel format: dynamic action sequences, expressive character designs, and immersive world-building.
        *   Emphasize the emotional impact of the story. Connect with readers on a personal level.
        *   Include a compelling "what if?" scenario that leaves the reader wanting more.
        *   Keep it concise and engaging. The back cover should be a visual and textual invitation to enter the world of the graphic novel.
        *   Mention any awards, accolades, or notable press coverage.
        *   End with a strong call to action: "Pick up [Title] and experience the unforgettable story for yourself!" or similar.

        Example Back Cover Copy Structure:

        [Hook] - A captivating opening line or two.

        [Brief Plot Summary] - Highlighting key characters, conflicts, and stakes.

        [Theme Emphasis] - Connecting the story to universal human experiences.

        [Visual Style Highlight] - Briefly mentioning the art style and its impact.

        [Emotional Hook] - What feeling will readers experience?

        [Call to Action] - Encouraging the reader to buy the book.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, 2-3 line description for a Graphic Novel, ideal for recommendation lists.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, main character, plot summary, genre elements).

        Returns:
        A string containing the prompt for the short description generation.
        """
        prompt = f"""
        Create a short, 2-3 line description for the Graphic Novel "{kwargs.get('title', '[Title]')}" by {kwargs.get('author', '[Author]')}.

        Genre: Graphic Novel (emphasize visual storytelling).

        Main Character: {kwargs.get('main_character', '[Main Character - Name and defining trait]')}.

        Plot Summary (Key Element): {kwargs.get('plot_summary', '[Highlight the most intriguing aspect of the plot]')}.

        Genre Elements: {kwargs.get('genre_elements', '[List subgenres or related genres - e.g., superhero, fantasy, sci-fi, slice-of-life]')}.

        Instructions:

        *   Focus on brevity and impact. Every word counts.
        *   Highlight the unique selling points of the graphic novel. What makes it stand out from other stories in the genre?
        *   Use strong verbs and evocative language to create a sense of excitement and intrigue.
        *   Emphasize the visual aspect of the story. Hint at the stunning artwork and dynamic panel layouts.
        *   Capture the essence of the story's emotional core.
        *   Consider using a comparison to other popular graphic novels or works of art to give readers a frame of reference (e.g., "Fans of [Graphic Novel] will love...").

        Example Short Description:

        "In a world where [brief plot setup], [Main Character] must [main objective]. Prepare for stunning visuals and a story that will leave you breathless!"
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for a Graphic Novel.

        Args:
        **kwargs: Keyword arguments containing book details (title, core concept, target audience, genre elements).

        Returns:
        A string containing the prompt for the tagline generation.
        """
        prompt = f"""
        Create a compelling marketing tagline for the Graphic Novel "{kwargs.get('title', '[Title]')}".

        Core Concept: {kwargs.get('core_concept', '[The central idea or conflict of the story]')}.

        Target Audience: {kwargs.get('target_audience', '[Target Audience - e.g., Teens, Adults, Comic Book Fans]')}.

        Genre Elements: {kwargs.get('genre_elements', '[List subgenres or related genres - e.g., mystery, horror, romance]')}.

        Instructions:

        *   Keep it short, memorable, and impactful. Aim for a tagline that is easily shareable.
        *   Focus on the emotional core of the story. What feeling should the tagline evoke?
        *   Highlight the unique aspects of the graphic novel format (visual storytelling, dynamic action, expressive characters).
        *   Use strong verbs and evocative language.
        *   Consider using a play on words or a clever metaphor.
        *   Think about what makes the graphic novel stand out from other stories in the genre.
        *   Test different taglines to see which ones resonate the most with your target audience.

        Example Taglines:

        *   "[Title]: Where words meet art, and legends are born."
        *   "Experience the story. See the legend. [Title]."
        *   "Beyond the page. Beyond belief. [Title]."
        *   "[Title]: Prepare to be drawn in."
        *   "The story unfolds panel by panel. [Title]."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for specifying visual style preferences for back cover design of a Graphic Novel.

        Args:
        **kwargs: Keyword arguments containing book details (title, author, visual style, color palette, target audience).

        Returns:
        A string containing the prompt for visual style preferences.
        """
        prompt = f"""
        Specify the visual style preferences for the back cover design of the Graphic Novel "{kwargs.get('title', '[Title]')}" by {kwargs.get('author', '[Author]')}.

        Overall Visual Style: {kwargs.get('visual_style', '[Detailed description of the art style - e.g., Manga, realistic, stylized, watercolor, black and white, cyberpunk, art deco]')}.  Be specific about the influences and characteristics of the art.

        Color Palette: {kwargs.get('color_palette', '[Description of the color palette - e.g., vibrant, muted, grayscale, limited palette]')}. How does the color palette contribute to the overall mood and atmosphere of the story?

        Target Audience: {kwargs.get('target_audience', '[Target Audience - e.g., Young Adults, Adults, fans of specific genres]')}. Consider what kind of visual elements will appeal to this audience.

        Key Visual Elements: {kwargs.get('key_visual_elements', '[List of key visual elements from the book - e.g., character designs, iconic locations, action sequences]')}.  Which of these elements should be featured on the back cover?

        Typography: {kwargs.get('typography', '[Description of the desired typography - e.g., bold, handwritten, futuristic]')}. The typography should complement the overall visual style.

        Layout: {kwargs.get('layout', '[Description of the desired layout - e.g., dynamic, minimalist, traditional comic book panel layout]')}. How should the text and images be arranged on the back cover?

        Instructions:

        *   The back cover design should be visually appealing and representative of the graphic novel's art style.
        *   It should immediately grab the attention of potential readers.
        *   Consider using a key image or panel from the graphic novel to create a strong visual impact.
        *   The back cover should convey the tone and atmosphere of the story.
        *   The typography should be legible and easy to read.
        *   The overall design should be clean and uncluttered.
        *   Provide examples of back covers or artwork that inspire the desired visual style.
        *   Think about how the back cover can be used to create a sense of mystery and intrigue.

        Example Visual Style Preferences:

        "The back cover should feature a dynamic action scene in a style reminiscent of classic Manga, with bold lines, vibrant colors, and a fast-paced layout. The typography should be bold and futuristic, reflecting the cyberpunk themes of the story."
        """
        return prompt
        ```
        graphicnovel_book_additions = """

## GraphicNovel Series Volume Integration

### GraphicNovel Artistic Continuity
- **Style Consistency**: Maintain the artistic voice established in previous graphicnovel volumes
- **Technical Standards**: Maintain quality standards established in the graphicnovel series
- **Creative Evolution**: Show artistic growth from previous graphicnovel volumes
- **Format Mastery**: Build upon graphicnovel techniques established in the series
- **Thematic Connections**: Continue developing themes from earlier graphicnovel works

### Volume-Specific GraphicNovel Focus
- **Artistic Objectives**: What specific graphicnovel artistic goals will this volume achieve?
- **Format Innovation**: What new graphicnovel techniques or approaches will be introduced?
- **Creative Development**: How will this volume advance the artistic vision of the series?
- **Series Integration**: How does this volume connect meaningfully to other graphicnovel works in the series?
- **Artistic Value**: What unique graphicnovel artistic value does this volume add to the series?

Ensure this volume demonstrates graphicnovel mastery while serving as an integral part of the artistic series.
"""

        return base_prompt + graphicnovel_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_series_book_prompt(**kwargs)
