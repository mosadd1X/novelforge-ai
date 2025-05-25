"""
True Crime genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class TrueCrimePrompts(NonFictionBasePrompts):
    GENRE_NAME = "True Crime"
    GENRE_DESCRIPTION = "True Crime explores real-life criminal events, often focusing on the perpetrators, victims, and the investigative process. It aims to reconstruct the crime, understand the motivations behind it, and examine the impact on individuals and society. Accuracy, ethical considerations, and compelling storytelling are paramount."
    
    GENRE_CHARACTERISTICS = [
        "Meticulous factual accuracy and attention to detail are crucial; any deviation can undermine the narrative's credibility.",
        "A strong narrative voice that balances objectivity with empathy for the victims and their families.",
        "Exploration of the psychological profiles of both the perpetrator and the victim, delving into their backgrounds and motivations.",
        "Detailed reconstruction of the crime scene, timeline, and investigative procedures, often relying on police reports, court documents, and witness testimonies.",
        "Examination of the social, cultural, and economic factors that may have contributed to the crime.",
        "Ethical considerations regarding the privacy of victims and their families, as well as the potential for sensationalism or exploitation.",
        "A focus on the legal and judicial processes involved in solving the crime, including trials, appeals, and sentencing.",
        "The use of primary source materials, such as interviews, letters, and diaries, to provide firsthand accounts and insights.",
        "Exploration of the long-term consequences of the crime on the victims, their families, and the community.",
        "A compelling narrative structure that builds suspense and maintains reader engagement while adhering to factual accuracy."
    ]
    
    TYPICAL_ELEMENTS = [
        "A detailed description of the crime scene, including physical evidence and environmental factors.",
        "Profiles of the victims, including their backgrounds, relationships, and last known activities.",
        "Profiles of the perpetrators, including their motivations, psychological state, and criminal history.",
        "A timeline of events leading up to, during, and after the crime.",
        "Interviews with law enforcement officials, witnesses, and family members.",
        "Excerpts from police reports, court documents, and forensic analyses.",
        "Analysis of the evidence presented at trial, including witness testimonies and expert opinions.",
        "Exploration of the legal and judicial processes involved in the case.",
        "Discussion of the social and cultural context in which the crime occurred.",
        "Examination of the impact of the crime on the victims, their families, and the community.",
        "Photographs, maps, and other visual aids to enhance the reader's understanding of the crime.",
        "A concluding chapter that reflects on the significance of the case and its broader implications."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        true_crime_additions = '''
## True Crime-Specific Writing Considerations
- **Accuracy and Verification**: Prioritize meticulous research and fact-checking. All claims must be verifiable through reliable sources like police reports, court documents, and credible news outlets. Avoid speculation and present information objectively.
- **Ethical Responsibility**: Approach the subject matter with sensitivity and respect for the victims and their families. Avoid sensationalism or exploitation of their suffering. Obtain necessary permissions and adhere to privacy laws.
- **Narrative Objectivity**: Maintain a neutral and unbiased perspective. Present all sides of the story fairly and avoid expressing personal opinions or judgments. Let the facts speak for themselves.
- **Legal Considerations**: Be aware of potential legal ramifications, such as libel or defamation. Consult with legal counsel to ensure compliance with relevant laws and regulations.
- **Source Transparency**: Clearly identify and cite all sources of information. Provide detailed footnotes, endnotes, or a bibliography to allow readers to verify the accuracy of your claims.
- **Emotional Impact**: Recognize the emotional impact of the story on both the writer and the reader. Be prepared to deal with potentially disturbing or traumatic content.
- **Balancing Detail and Pacing**: Provide sufficient detail to create a compelling narrative, but avoid overwhelming the reader with unnecessary information. Maintain a brisk and engaging pace.
- **Understanding Criminal Psychology**: Develop a solid understanding of criminal psychology and behavior to provide insightful analysis of the perpetrator's motivations and actions.
'''
        return base_prompt + true_crime_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        true_crime_additions = '''
## True Crime-Specific Outline Requirements
- **Introduction**: Begin with a compelling hook that introduces the crime and its significance. Clearly state the scope and purpose of the book.
- **Victim Profiles**: Develop detailed profiles of the victims, including their backgrounds, relationships, and last known activities. Humanize the victims and emphasize their loss.
- **Perpetrator Profiles**: Explore the backgrounds, motivations, and psychological state of the perpetrators. Examine their criminal history and any relevant social or environmental factors.
- **Crime Scene Reconstruction**: Reconstruct the crime scene in detail, including physical evidence, environmental factors, and witness testimonies. Use maps, diagrams, and photographs to enhance the reader's understanding.
- **Investigation Timeline**: Create a chronological timeline of the investigation, including key events, breakthroughs, and setbacks. Highlight the roles of law enforcement officials and forensic experts.
- **Legal Proceedings**: Outline the legal proceedings, including arrests, indictments, trials, and appeals. Summarize the evidence presented at trial and the arguments made by both sides.
- **Impact on Victims' Families**: Explore the long-term impact of the crime on the victims' families, including their emotional struggles, financial hardships, and legal battles.
- **Social and Cultural Context**: Examine the social and cultural context in which the crime occurred. Discuss any relevant social issues, political factors, or economic conditions.
- **Ethical Considerations**: Address any ethical considerations related to the case, such as privacy concerns, media coverage, and the potential for exploitation.
- **Conclusion**: Summarize the key findings of the book and reflect on the significance of the case. Discuss any lessons learned or broader implications.
- **Epilogue (Optional)**: Provide an update on the current status of the case, including the perpetrators' sentences, any ongoing legal battles, and the victims' families' efforts to heal and rebuild their lives.
'''
        return base_prompt + true_crime_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        true_crime_additions = '''
## True Crime-Specific Character Development
- **Victims**: Focus on humanizing the victims. Provide detailed backgrounds, relationships, and aspirations. Emphasize their individuality and the tragedy of their loss. Avoid reducing them to mere statistics.
- **Perpetrators**: Explore the perpetrators' motivations, psychological state, and criminal history. Avoid glorifying or romanticizing their actions. Present them as complex individuals with flaws and vulnerabilities.
- **Law Enforcement**: Develop realistic and nuanced portrayals of law enforcement officials. Show their dedication, challenges, and ethical dilemmas. Avoid portraying them as infallible heroes or corrupt villains.
- **Witnesses**: Create believable and relatable witnesses. Explore their perspectives, biases, and emotional reactions to the crime. Highlight the importance of their testimonies in solving the case.
- **Family Members**: Portray the family members of both the victims and the perpetrators with sensitivity and empathy. Show their grief, anger, and resilience. Avoid exploiting their emotions for sensationalism.
- **Legal Professionals**: Develop realistic portrayals of lawyers, judges, and other legal professionals. Show their expertise, ethical considerations, and the pressures they face in the courtroom.
- **Forensic Experts**: Create compelling portrayals of forensic experts, including their scientific knowledge, analytical skills, and attention to detail. Highlight the importance of forensic evidence in solving the crime.
- **Character Arcs**: Consider the character arcs of the key players in the story. How do their experiences with the crime change them over time? How do they cope with trauma, loss, and the pursuit of justice?
'''
        return base_prompt + true_crime_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        true_crime_additions = '''
## True Crime-Specific Chapter Writing
- **Opening Hook**: Start each chapter with a compelling hook that grabs the reader's attention and introduces the main theme or event of the chapter.
- **Detailed Descriptions**: Provide vivid and detailed descriptions of the crime scene, the victims, the perpetrators, and the investigative process. Use sensory details to create a sense of realism and immersion.
- **Chronological Structure**: Maintain a clear and chronological structure, guiding the reader through the events of the case in a logical and easy-to-follow manner.
- **Primary Source Integration**: Incorporate primary source materials, such as interviews, police reports, court documents, and forensic analyses, to support your claims and add credibility to your narrative.
- **Character Development**: Develop the characters of the key players in the story, including the victims, the perpetrators, the law enforcement officials, and the family members. Show their motivations, emotions, and relationships.
- **Suspense and Tension**: Build suspense and tension throughout the chapter, gradually revealing new information and raising questions that keep the reader engaged.
- **Ethical Considerations**: Address any ethical considerations related to the chapter's content, such as privacy concerns, the potential for exploitation, and the need for sensitivity.
- **Transitions**: Use smooth and logical transitions to connect the different sections of the chapter and maintain a consistent flow of information.
- **Concluding Summary**: End each chapter with a brief summary of the key points and a preview of what's to come in the next chapter.
- **Maintaining Objectivity**: Ensure the chapter maintains an objective tone, presenting facts without bias or personal opinion.
'''
        return base_prompt + true_crime_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a truecrime-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        truecrime_series_additions = """

## TrueCrime Series-Specific Planning Elements

### Educational Progression for TrueCrime
- **Knowledge Building**: Structure learning progression appropriate for truecrime topics
- **Expertise Development**: Guide readers from basic to advanced understanding of truecrime subjects
- **Practical Applications**: Include actionable insights specific to truecrime throughout the series
- **Research Depth**: Plan comprehensive research appropriate for truecrime authority
- **Reader Value**: Ensure each book provides significant truecrime value while building series knowledge

### TrueCrime Series Continuity
- **Subject Consistency**: Maintain consistent approach to truecrime topics across books
- **Authority Building**: Establish and maintain credibility in truecrime throughout the series
- **Information Architecture**: Structure information flow appropriate for truecrime learning
- **Cross-References**: Create meaningful connections between truecrime concepts across books
- **Updated Knowledge**: Plan for incorporating new truecrime research and developments

Create a truecrime series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + truecrime_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a truecrime-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class TrueCrimeMarketing:
        """
        A class containing methods for generating marketing materials for True Crime books,
        specifically focused on back cover copy and visual design prompts.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions
        for True Crime books.

        Args:
        **kwargs:  Keyword arguments for customizing the prompt.  Possible keys:
        * target_reader (str): Description of the target reader (e.g., "armchair detective").
        * crime_type (str): Type of crime (e.g., "serial murder," "financial fraud").
        * location (str): Geographic location of the crime.
        * time_period (str): Time period in which the crime occurred.
        * victim_profile (str): Description of the victim(s).
        * perpetrator_profile (str): Description of the perpetrator(s).
        * central_question (str):  The core mystery or question the book explores.
        * unique_angle (str):  What makes this book different from other true crime books?
        * emotional_hook (str):  The primary emotion the book aims to evoke in the reader.
        * narrative_style (str):  The writing style (e.g., "investigative," "narrative nonfiction").
        * inclusion_statement (str): Information on inclusivity and representation of the victim(s).
        * themes (str): Primary themes the book explores (e.g., justice, corruption, societal issues).

        Returns:
        str: A detailed prompt string for generating back cover copy.
        """

        target_reader = kwargs.get("target_reader", "True crime enthusiasts and armchair detectives")
        crime_type = kwargs.get("crime_type", "a shocking and disturbing crime")
        location = kwargs.get("location", "a seemingly ordinary town")
        time_period = kwargs.get("time_period", "a time when secrets were easily buried")
        victim_profile = kwargs.get("victim_profile", "an innocent victim")
        perpetrator_profile = kwargs.get("perpetrator_profile", "a seemingly normal individual harboring dark secrets")
        central_question = kwargs.get("central_question", "the question of why this happened")
        unique_angle = kwargs.get("unique_angle", "unprecedented access to key evidence")
        emotional_hook = kwargs.get("emotional_hook", "a sense of outrage and a desire for justice")
        narrative_style = kwargs.get("narrative_style", "a gripping, investigative style")
        inclusion_statement = kwargs.get("inclusion_statement", "This book is committed to telling the victim's story with respect and sensitivity.")
        themes = kwargs.get("themes", "themes of justice, betrayal, and the dark side of human nature")


        prompt = f"""
        Write a compelling back cover description for a True Crime book that will captivate {target_reader}.
        The book details {crime_type} that took place in {location} during {time_period}.
        The victim was {victim_profile}, and the perpetrator was {perpetrator_profile}.

        The description should:
        *   Immediately grab the reader's attention with a chilling opening.
        *   Highlight the central mystery: {central_question}.
        *   Emphasize the unique angle: {unique_angle}.
        *   Evoke {emotional_hook} in the reader.
        *   Use language that is suspenseful and evocative.
        *   Hint at twists and turns in the investigation.
        *   Promise a deep dive into the psychology of both the victim and the perpetrator.
        *   Reference the {narrative_style}.
        *   Include the following: {inclusion_statement}.
        *   Incorporate themes of {themes}.
        *   End with a hook that leaves the reader wanting more, urging them to delve into the book.

        Example opening lines (adapt these to the specific case):
        *   "In the quiet town of [Location], a nightmare unfolded..."
        *   "Behind the facade of normalcy, a killer lurked..."
        *   "The truth is darker than you can imagine..."

        The description should be approximately 150-200 words.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short, impactful book recommendation blurb (2-3 lines) for a True Crime book.

        Args:
        **kwargs: Keyword arguments for customization. Possible keys:
        * subject (str): Subject of the book (e.g., "the chilling case of the Zodiac Killer").
        * hook (str): A captivating hook or detail.
        * target_reader (str): Target audience.
        * emotional_response (str): Desired emotional response.

        Returns:
        str: A prompt for a short book recommendation blurb.
        """
        subject = kwargs.get("subject", "a gripping true crime story")
        hook = kwargs.get("hook", "unravels a web of lies and deceit")
        target_reader = kwargs.get("target_reader", "fans of true crime")
        emotional_response = kwargs.get("emotional_response", "shock and fascination")

        prompt = f"""
        Write a short, impactful book recommendation blurb (2-3 lines) for {target_reader} who enjoy {emotional_response}.

        The blurb should:
        *   Focus on {subject}.
        *   Highlight the captivating hook: {hook}.
        *   Use strong verbs and evocative language.
        *   Create a sense of urgency and intrigue.
        *   Be concise and memorable.

        Example:
        "A must-read for true crime aficionados. [Book Title] delves into the darkest corners of the human psyche, leaving you questioning everything you thought you knew."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for a punchy, attention-grabbing marketing tagline for a True Crime book.

        Args:
        **kwargs: Keyword arguments for customization. Possible keys:
        * crime_type (str): Type of crime.
        * emotional_impact (str): The emotional impact of the story.
        * key_element (str): A key element of the story.
        * tone (str): The overall tone (e.g., "dark," "disturbing," "revealing").

        Returns:
        str: A prompt for a marketing tagline.
        """

        crime_type = kwargs.get("crime_type", "The ultimate betrayal")
        emotional_impact = kwargs.get("emotional_impact", "will leave you breathless")
        key_element = kwargs.get("key_element", "the shocking truth")
        tone = kwargs.get("tone", "dark and unsettling")

        prompt = f"""
        Create a punchy, attention-grabbing marketing tagline for a True Crime book. The tone is {tone}.

        The tagline should:
        *   Be short and memorable (ideally under 10 words).
        *   Highlight the type of crime: {crime_type}.
        *   Emphasize the emotional impact: {emotional_impact}.
        *   Hint at a key element of the story: {key_element}.
        *   Be intriguing and create a sense of mystery.
        *   Avoid being overly sensationalistic or exploitative.  Focus on the story and the search for truth.

        Examples:
        *   "Evil walks among us."
        *   "The truth is a killer."
        *   "Some secrets are best left buried...but not this one."
        *   "Justice is a long, dark road."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for describing visual style preferences for the back cover design of a True Crime book.

        Args:
        **kwargs: Keyword arguments for customization. Possible keys:
        * color_palette (str): Preferred color palette (e.g., "dark and muted," "high contrast black and white").
        * imagery (str): Types of imagery to use or avoid (e.g., "avoid graphic images," "use evocative landscapes").
        * typography (str): Preferred typography styles (e.g., "clean and modern," "vintage and gritty").
        * overall_mood (str): The desired overall mood (e.g., "somber," "ominous," "intriguing").
        * target_audience (str): Description of the target audience to tailor the design.
        * symbolic_elements (str): Suggested symbolic elements (e.g., a broken mirror, a shadowed figure).
        * avoidance (str): Things to avoid (e.g., bright colors, overtly sensational images).

        Returns:
        str: A prompt for describing visual style preferences.
        """

        color_palette = kwargs.get("color_palette", "a dark and muted color palette with shades of grey, black, and deep red or blue")
        imagery = kwargs.get("imagery", "evocative landscapes or symbolic objects rather than graphic crime scene photos")
        typography = kwargs.get("typography", "a clean and modern sans-serif font for readability, with a slightly distressed or vintage font for the title to add a sense of history and unease")
        overall_mood = kwargs.get("overall_mood", "somber, ominous, and intriguing")
        target_audience = kwargs.get("target_audience", "true crime enthusiasts who appreciate thoughtful and respectful storytelling")
        symbolic_elements = kwargs.get("symbolic_elements", "a single, impactful symbolic element such as a broken mirror, a blurred figure in the shadows, or a decaying object")
        avoidance = kwargs.get("avoidance", "bright colors, overly sensational images, and anything that could be perceived as exploitative or disrespectful to the victim")

        prompt = f"""
        Describe the desired visual style for the back cover design of a True Crime book.

        Consider the following:
        *   Color Palette: {color_palette}.
        *   Imagery: Use {imagery}.
        *   Typography: Choose {typography}.
        *   Overall Mood: Create a design that feels {overall_mood}.
        *   Target Audience: Design for {target_audience}.
        *   Symbolic Elements: Consider incorporating {symbolic_elements}.
        *   Avoid: {avoidance}.

        The design should:
        *   Be respectful of the victim(s) and their story.
        *   Convey a sense of unease and mystery.
        *   Reflect the tone and themes of the book.
        *   Be visually appealing and professional.
        *   Avoid being overly graphic or sensationalistic.

        Describe the desired layout, placement of text, and overall visual impact.
        """
        return prompt
        ```
        truecrime_book_additions = """

## TrueCrime Series Book Integration

### TrueCrime Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon truecrime concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous truecrime books when relevant
- **Knowledge Progression**: Advance reader understanding of truecrime topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the truecrime series

### Book-Specific TrueCrime Focus
- **Educational Objectives**: What specific truecrime knowledge will readers gain from this book?
- **Practical Applications**: What actionable truecrime insights will be provided?
- **Research Integration**: How will new truecrime research be incorporated?
- **Series Advancement**: How does this book advance the overall truecrime education series?
- **Reader Value**: What unique truecrime value does this book add to the series?

Ensure this book provides comprehensive truecrime education while serving as an integral part of the learning series.
"""

        return base_prompt + truecrime_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_series_book_prompt(**kwargs)
