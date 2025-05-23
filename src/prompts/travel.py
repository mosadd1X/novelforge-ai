"""
Travel genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class TravelPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Travel"
    GENRE_DESCRIPTION = "The Travel genre encompasses narratives centered around journeys, exploration, and experiences in different locations. It focuses on the transformative power of travel, highlighting cultural immersion, personal growth, and the discovery of new perspectives. The genre can range from personal memoirs and adventure stories to informative guides and fictional accounts of travel experiences."
    
    GENRE_CHARACTERISTICS = [
        "Emphasis on sensory details to vividly portray locations and experiences, engaging the reader's senses of sight, sound, smell, taste, and touch.",
        "Exploration of cultural differences and similarities, fostering understanding and appreciation for diverse customs, traditions, and ways of life.",
        "Focus on personal growth and transformation, showcasing how travel can challenge perspectives, broaden horizons, and lead to self-discovery.",
        "Incorporation of historical and geographical context, providing readers with a deeper understanding of the places visited and their significance.",
        "Use of evocative language and imagery to capture the beauty and wonder of the natural world and human-made environments.",
        "Inclusion of practical information and tips for travelers, such as transportation options, accommodation recommendations, and cultural etiquette.",
        "Exploration of the challenges and rewards of travel, including overcoming obstacles, adapting to unfamiliar situations, and embracing the unexpected.",
        "Reflection on the impact of tourism on local communities and environments, promoting responsible and sustainable travel practices.",
        "Use of anecdotes and personal stories to create a connection with the reader and share authentic travel experiences.",
        "A sense of adventure and discovery, inspiring readers to explore the world and embark on their own journeys."
    ]
    
    TYPICAL_ELEMENTS = [
        "Detailed descriptions of landscapes, cities, and cultural landmarks.",
        "Encounters with local people and their customs.",
        "Experiences with local cuisine and culinary traditions.",
        "Transportation methods and travel logistics (e.g., trains, planes, buses, boats).",
        "Accommodation experiences (e.g., hotels, hostels, guesthouses, camping).",
        "Cultural immersion activities (e.g., language learning, cooking classes, traditional ceremonies).",
        "Challenges and obstacles encountered during the journey (e.g., language barriers, cultural misunderstandings, logistical problems).",
        "Moments of personal reflection and self-discovery.",
        "Historical and geographical information about the places visited.",
        "Practical travel tips and advice for readers.",
        "Photographs or illustrations that complement the text.",
        "Maps and itineraries to guide readers through the journey."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        travel_additions = '''
## Travel-Specific Writing Considerations
- **Authenticity and Voice**: Capture the unique perspective and voice of the traveler, ensuring the narrative feels genuine and relatable. Avoid clichés and strive for originality in describing experiences.
- **Sensory Detail and Imagery**: Emphasize sensory details (sight, sound, smell, taste, touch) to transport the reader to the destination. Use vivid imagery and descriptive language to paint a picture of the environment and culture.
- **Cultural Sensitivity**: Approach cultural differences with respect and understanding. Avoid stereotypes and generalizations. Research and accurately represent the customs, traditions, and beliefs of the local people.
- **Balancing Information and Narrative**: Integrate practical travel information (e.g., transportation, accommodation, costs) seamlessly into the narrative. Avoid overwhelming the reader with dry facts; instead, weave information into the story in an engaging way.
- **Personal Growth and Reflection**: Explore the personal impact of the travel experience. Reflect on how the journey has changed the traveler's perspective, broadened their horizons, or led to self-discovery.
- **Ethical Considerations**: Address the ethical implications of travel, such as environmental impact, cultural preservation, and responsible tourism. Encourage readers to travel in a sustainable and respectful manner.
- **Structure and Pacing**: Maintain a clear narrative structure with a compelling beginning, middle, and end. Vary the pacing to keep the reader engaged, balancing descriptive passages with action and dialogue.
- **Target Audience**: Consider the intended audience and tailor the writing style and content accordingly. A travel guide for backpackers will differ significantly from a memoir about a luxury cruise.
'''
        return base_prompt + travel_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        travel_additions = '''
## Travel-Specific Outline Requirements
- **Introduction (Setting the Stage)**: Introduce the destination, the purpose of the trip, and the traveler's initial expectations. Capture the reader's attention with a compelling opening scene or anecdote.
- **Journey Begins (Arrival and Initial Impressions)**: Describe the arrival at the destination and the traveler's first impressions. Highlight the sensory details that create a sense of place.
- **Cultural Immersion (Exploring Local Customs)**: Detail interactions with local people, participation in cultural activities, and experiences with local cuisine. Focus on the unique aspects of the culture and the traveler's reactions to them.
- **Challenges and Obstacles (Overcoming Difficulties)**: Describe any challenges or obstacles encountered during the journey, such as language barriers, logistical problems, or cultural misunderstandings. Explain how the traveler overcame these difficulties.
- **Personal Growth (Moments of Reflection)**: Include moments of personal reflection and self-discovery. Explore how the travel experience has changed the traveler's perspective, broadened their horizons, or led to new insights.
- **Adventure and Exploration (Discovering Hidden Gems)**: Highlight any adventurous activities or explorations of hidden gems. Describe the excitement and wonder of discovering new places and experiences.
- **Ethical Considerations (Responsible Travel)**: Address the ethical implications of travel, such as environmental impact, cultural preservation, and responsible tourism. Encourage readers to travel in a sustainable and respectful manner.
- **Return and Reflection (Lessons Learned)**: Describe the return journey and the traveler's reflections on the overall experience. Summarize the key lessons learned and the lasting impact of the trip.
- **Conclusion (Final Thoughts and Recommendations)**: Offer final thoughts and recommendations for readers who are planning a similar trip. Inspire them to explore the world and embark on their own adventures.
- **Visual Elements (Photographs and Maps)**: Consider incorporating photographs or illustrations to complement the text and enhance the reader's experience. Include maps to guide readers through the journey.
'''
        return base_prompt + travel_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        travel_additions = '''
## Travel-Specific Character Development
- **The Traveler (Protagonist)**: Define the traveler's personality, motivations, and background. Consider their reasons for traveling, their level of experience, and their expectations for the journey. Are they seeking adventure, self-discovery, or cultural immersion?
- **Local Guides (Supporting Characters)**: Develop local guides or mentors who can provide insights into the culture and help the traveler navigate unfamiliar situations. Give them distinct personalities and motivations.
- **Fellow Travelers (Supporting Characters)**: Create memorable fellow travelers who can add depth and complexity to the story. Explore their backgrounds, motivations, and relationships with the protagonist.
- **Antagonists (Challenges and Conflicts)**: Introduce antagonists or challenges that create conflict and tension in the narrative. These could be cultural misunderstandings, logistical problems, or personal struggles.
- **Character Arc (Transformation)**: Focus on the traveler's character arc and how they change throughout the journey. Explore their personal growth, self-discovery, and transformation as a result of their experiences.
- **Authenticity and Relatability**: Ensure that the characters are authentic and relatable to the reader. Avoid stereotypes and create nuanced personalities with flaws and strengths.
- **Cultural Sensitivity**: Portray characters from different cultures with respect and understanding. Avoid generalizations and accurately represent their customs, traditions, and beliefs.
- **Internal Conflicts**: Explore the internal conflicts and struggles that the traveler faces during the journey. These could be doubts, fears, or moral dilemmas.
'''
        return base_prompt + travel_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        travel_additions = '''
## Travel-Specific Chapter Writing
- **Setting the Scene**: Begin each chapter by vividly describing the setting, using sensory details to transport the reader to the location. Focus on the sights, sounds, smells, tastes, and textures of the environment.
- **Introducing Characters**: Introduce new characters or develop existing ones within the context of the chapter's events. Reveal their personalities, motivations, and relationships with the protagonist.
- **Describing Experiences**: Detail the traveler's experiences, both positive and negative, in a compelling and engaging way. Focus on the emotional impact of these experiences and how they contribute to the overall narrative.
- **Incorporating Dialogue**: Use dialogue to bring the characters to life and reveal their thoughts and feelings. Ensure that the dialogue is authentic and reflects the cultural context of the setting.
- **Building Tension**: Create tension and suspense by introducing challenges, obstacles, or conflicts that the traveler must overcome. Use foreshadowing and pacing to keep the reader engaged.
- **Reflecting on Themes**: Explore the underlying themes of the travel experience, such as cultural understanding, personal growth, and the search for meaning. Use the chapter's events to illustrate these themes.
- **Providing Information**: Integrate practical travel information seamlessly into the narrative, such as transportation options, accommodation recommendations, and cultural etiquette.
- **Ending with a Hook**: End each chapter with a hook that compels the reader to continue reading. This could be a cliffhanger, a question, or a moment of suspense.
'''
        return base_prompt + travel_additions

# Convenience functions for direct access
def get_writer_profile_prompt(**kwargs) -> str:
    return TravelPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return TravelPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return TravelPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return TravelPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return TravelPrompts.get_enhancement_prompt(**kwargs)