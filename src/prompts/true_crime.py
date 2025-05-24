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

def get_series_book_prompt(**kwargs) -> str:
    return TrueCrimePrompts.get_series_book_prompt(**kwargs)
