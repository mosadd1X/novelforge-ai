"""
Mystery genre-specific prompts for novel generation.
"""

from .base_prompts import FictionBasePrompts

class MysteryPrompts(FictionBasePrompts):
    """Mystery-specific prompts for novel generation."""
    
    GENRE_NAME = "Mystery"
    GENRE_DESCRIPTION = "A genre focused on solving crimes, puzzles, or unexplained events through investigation and deduction"
    
    GENRE_CHARACTERISTICS = [
        "Central puzzle or crime that drives the narrative",
        "Detective or investigator protagonist",
        "Clues planted throughout the story for readers to discover",
        "Red herrings and misdirection to maintain suspense",
        "Logical deduction and problem-solving",
        "Atmospheric settings that enhance mystery",
        "Multiple suspects with motives and opportunities",
        "Satisfying revelation that ties all clues together"
    ]
    
    TYPICAL_ELEMENTS = [
        "Crime scene investigation and forensic details",
        "Interrogation scenes and witness interviews",
        "Discovery of crucial evidence and clues",
        "False leads and misleading information",
        "Suspects with secrets and hidden motives",
        "Atmospheric locations (old mansions, foggy streets, isolated settings)",
        "Time pressure and escalating stakes",
        "Logical deduction and 'aha!' moments",
        "Final revelation scene where the solution is explained",
        "Justice served or moral resolution"
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        """Generate a mystery-specific writer profile prompt."""
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        mystery_additions = """

## Mystery-Specific Writing Considerations
- **Fair Play Principle**: Provide readers with all necessary clues to solve the mystery
- **Pacing Control**: Balance investigation scenes with action and character development
- **Clue Integration**: Plant evidence naturally within the narrative flow
- **Misdirection Mastery**: Create believable red herrings without cheating the reader
- **Logical Structure**: Ensure the solution follows logically from presented evidence
- **Atmospheric Building**: Use setting and mood to enhance suspense and mystery

## Mystery Reader Expectations
- A puzzle that can be solved through careful attention to clues
- Fair presentation of evidence without withholding crucial information
- Satisfying resolution that explains all mysterious elements
- Engaging detective work and investigation process
- Believable motives and realistic character behavior
- Appropriate pacing that maintains suspense throughout
"""
        
        return base_prompt + mystery_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        """Generate a mystery-specific outline prompt."""
        base_prompt = super().get_outline_prompt(**kwargs)
        
        mystery_additions = """

## Mystery-Specific Outline Requirements
- **The Crime/Mystery**: Clearly establish what needs to be solved
- **Clue Distribution**: Plan where and how clues will be revealed
- **Suspect Development**: Create multiple viable suspects with motives
- **Investigation Process**: Structure the detective work and discovery sequence
- **Red Herrings**: Plan false leads that seem plausible but mislead
- **Resolution Logic**: Ensure the solution follows logically from all clues

## Mystery Plot Structure Elements
- Opening hook that establishes the mystery or crime
- Introduction of the detective/investigator and initial investigation
- Discovery of first clues and establishment of suspects
- Deepening investigation with new evidence and complications
- False solutions and red herrings that mislead
- Crisis point where the case seems unsolvable
- Breakthrough discovery that provides the key insight
- Final confrontation and revelation of the truth
- Resolution showing justice served and loose ends tied up

## Clue Planning Guidelines
- Plant at least 3-5 major clues that point to the solution
- Include 2-3 red herrings that seem significant but mislead
- Ensure clues are discoverable through logical investigation
- Balance obvious clues with subtle ones requiring deduction
- Make sure the final solution accounts for all presented evidence

Create a mystery outline that provides a fair, engaging puzzle for readers to solve.
"""
        
        return base_prompt + mystery_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        """Generate a mystery-specific character development prompt."""
        base_prompt = super().get_character_prompt(**kwargs)
        
        mystery_additions = """

## Mystery Character Archetypes and Roles
- **The Detective/Investigator**: Professional or amateur sleuth with keen observation skills
- **The Victim**: Person whose death/disappearance/problem drives the mystery
- **The Suspects**: Multiple characters with motive, means, and opportunity
- **The Witness**: Character who saw something important but may not realize it
- **The Red Herring**: Character who appears guilty but is innocent
- **The Accomplice**: Character who helped cover up or commit the crime
- **The Authority Figure**: Police, lawyers, or officials involved in the case

## Mystery Character Development Guidelines
- Give each suspect a believable motive for the crime
- Create alibis that can be questioned and investigated
- Develop secrets and hidden relationships between characters
- Show how each character reacts under pressure and questioning
- Include characters who lie for reasons unrelated to the main crime
- Design personalities that create natural conflict and suspicion

## Suspect Development Checklist
For each major suspect, establish:
- **Motive**: Why they would want to commit the crime
- **Means**: How they could have done it (access, ability, resources)
- **Opportunity**: When they could have committed the crime
- **Alibi**: Where they claim to have been (true or false)
- **Secret**: Hidden information that makes them seem guilty
- **Relationship**: Connection to victim and other characters

## Detective Character Traits
Consider giving your investigator:
- Unique observation skills or deductive methods
- Personal flaws that complicate the investigation
- Relevant background or expertise
- Compelling reason for solving this particular case
- Distinctive personality quirks or habits
- Relationships that affect their objectivity

Create characters that serve the mystery while feeling like real, complex people.
"""
        
        return base_prompt + mystery_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        """Generate a mystery-specific chapter writing prompt."""
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        mystery_additions = """

## Mystery Writing Techniques
- **Clue Presentation**: Introduce evidence naturally through investigation and observation
- **Suspense Building**: Use pacing and information control to maintain tension
- **Fair Play**: Show clues clearly without hiding crucial information from readers
- **Misdirection**: Present information that can be interpreted multiple ways
- **Deductive Reasoning**: Show logical thought processes and investigation methods
- **Atmospheric Details**: Use setting and mood to enhance mystery and suspense

## Investigation Scene Guidelines
- Show the detective's thought process and deductive reasoning
- Include physical evidence discovery and analysis
- Present witness interviews and interrogations realistically
- Reveal character motivations and secrets gradually
- Use dialogue to expose lies and inconsistencies
- Build tension through time pressure or escalating stakes

## Clue Integration Techniques
- Embed clues in natural dialogue and action
- Use environmental details to hide evidence in plain sight
- Show multiple interpretations of the same evidence
- Let characters draw wrong conclusions from correct observations
- Present information that gains significance later in the story

## Mystery Dialogue Considerations
- Characters should have reasons to lie or withhold information
- Include subtext where characters say one thing but mean another
- Show nervous behavior and tells when characters are hiding something
- Use questioning techniques that reveal character and advance plot
- Balance exposition with natural conversation flow

Write with careful attention to logic, fair play, and maintaining reader engagement in the puzzle.
"""
        
        return base_prompt + mystery_additions


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a mystery-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        mystery_series_additions = """

## Mystery Series-Specific Planning Elements

### Genre-Specific Series Development
- **Mystery Conventions**: Ensure each book fulfills mystery reader expectations while advancing the series
- **Escalating Complexity**: Increase sophistication and depth across books appropriate to mystery
- **Character Arcs**: Develop character growth that spans multiple books in ways authentic to mystery
- **Plot Progression**: Create overarching plot threads that build tension and stakes across the series
- **Thematic Development**: Explore mystery themes with increasing depth and complexity

### Mystery Series Continuity
- **Genre Elements**: Maintain consistent mystery elements while introducing new aspects
- **Reader Engagement**: Create compelling book-to-book connections that satisfy mystery readers
- **Series Identity**: Establish a strong series identity that feels authentically mystery
- **World Building**: Develop the story world in ways that enhance the mystery experience
- **Character Relationships**: Evolve relationships in ways that feel natural to the mystery genre

Create a mystery series that builds compelling narratives with authentic genre elements and engaging character development.
"""
        
        return base_prompt + mystery_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a mystery-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        mystery_book_additions = """

## Mystery Series Book Integration

### Mystery Continuity for This Book
- **Genre Consistency**: Maintain established mystery elements while potentially introducing new aspects
- **Character Development**: Show how characters have grown since previous books in ways authentic to mystery
- **Plot Advancement**: Continue series plot threads while telling a complete mystery story
- **World Consistency**: Maintain established world elements while expanding appropriately
- **Reader Expectations**: Fulfill mystery reader expectations while advancing the series narrative

### Book-Specific Mystery Focus
- **Central Conflict**: What mystery-appropriate conflict drives this book's plot?
- **Character Growth**: Which characters will experience the most development in this book?
- **New Elements**: What new mystery elements will be introduced that fit the established series?
- **Series Advancement**: How does this book move the overall series arc forward significantly?
- **Genre Authenticity**: How does this book exemplify excellent mystery while serving the series?

Ensure this book feels like an authentic continuation of the mystery series while telling a complete, satisfying story.
"""
        
        return base_prompt + mystery_book_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return MysteryPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return MysteryPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return MysteryPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return MysteryPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return MysteryPrompts.get_enhancement_prompt(**kwargs)

def get_series_plan_prompt(**kwargs) -> str:
    return MysteryPrompts.get_series_plan_prompt(**kwargs)

def get_series_book_prompt(**kwargs) -> str:
    return MysteryPrompts.get_series_book_prompt(**kwargs)
