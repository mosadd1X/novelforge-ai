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
        base_prompt = super().get_character_prompt(**kwargs)
        
        graphic_novel_additions = '''
## Graphic Novel-Specific Character Development
- **Visual Representation**: Describe the character's physical appearance in detail, including their clothing, hairstyle, and any distinguishing features. Consider how their appearance reflects their personality and background.
- **Facial Expressions and Body Language**: Outline the character's typical facial expressions and body language, and how these visual cues can be used to convey their emotions and intentions.
- **Costume Design (if applicable)**: If the character wears a costume, provide a detailed description of its design, including its colors, materials, and any symbolic elements.
- **Character Archetype**: Identify the character's archetype (e.g., hero, villain, mentor, sidekick) and how they embody the traits and characteristics associated with that archetype.
- **Visual Motifs**: Establish visual motifs that are associated with the character, such as a specific color, symbol, or object, and explain their significance.
- **Character Poses and Stances**: Describe the character's typical poses and stances, and how these visual cues can be used to convey their personality and attitude.
- **Character Evolution (Visual)**: Outline how the character's appearance changes over the course of the story, reflecting their growth, experiences, and emotional state.
- **Relationship to Visual Environment**: Describe how the character interacts with their environment and how their surroundings influence their appearance and behavior.
- **Exaggeration and Caricature**: Consider whether to use exaggeration or caricature in the character's design to emphasize certain traits or create a humorous effect.
'''
        return base_prompt + graphic_novel_additions

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

def get_series_book_prompt(**kwargs) -> str:
    return GraphicNovelPrompts.get_series_book_prompt(**kwargs)
