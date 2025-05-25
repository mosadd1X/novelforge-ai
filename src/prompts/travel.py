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


    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a travel-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)
        
        travel_series_additions = """

## Travel Series-Specific Planning Elements

### Educational Progression for Travel
- **Knowledge Building**: Structure learning progression appropriate for travel topics
- **Expertise Development**: Guide readers from basic to advanced understanding of travel subjects
- **Practical Applications**: Include actionable insights specific to travel throughout the series
- **Research Depth**: Plan comprehensive research appropriate for travel authority
- **Reader Value**: Ensure each book provides significant travel value while building series knowledge

### Travel Series Continuity
- **Subject Consistency**: Maintain consistent approach to travel topics across books
- **Authority Building**: Establish and maintain credibility in travel throughout the series
- **Information Architecture**: Structure information flow appropriate for travel learning
- **Cross-References**: Create meaningful connections between travel concepts across books
- **Updated Knowledge**: Plan for incorporating new travel research and developments

Create a travel series that provides comprehensive education with authoritative, well-researched content.
"""
        
        return base_prompt + travel_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a travel-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)
        
        travel_book_additions = """

## Travel Series Book Integration

### Travel Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon travel concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous travel books when relevant
- **Knowledge Progression**: Advance reader understanding of travel topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the travel series

### Book-Specific Travel Focus
- **Educational Objectives**: What specific travel knowledge will readers gain from this book?
- **Practical Applications**: What actionable travel insights will be provided?
- **Research Integration**: How will new travel research be incorporated?
- **Series Advancement**: How does this book advance the overall travel education series?
- **Reader Value**: What unique travel value does this book add to the series?

Ensure this book provides comprehensive travel education while serving as an integral part of the learning series.
"""
        
        return base_prompt + travel_book_additions

        ```python
        class TravelMarketing:
        """
        A class containing methods for generating back cover copy and marketing materials
        specifically for the Travel genre.
        """

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating compelling back cover descriptions
        for Travel books.

        Args:
        **kwargs: Keyword arguments to pass specific details about the book,
        such as target audience, travel destination, themes, etc.

        Returns:
        A string containing the prompt for the AI model.
        """
        prompt = f"""
        Craft a captivating back cover description for a Travel book.

        Genre: Travel

        Book Title: {kwargs.get('title', '[Insert Book Title Here]')}
        Author: {kwargs.get('author', '[Insert Author Name Here]')}
        Target Audience: {kwargs.get('target_audience', 'Travel enthusiasts, adventure seekers, armchair travelers')}
        Travel Destination: {kwargs.get('destination', '[Insert Destination Here: e.g., Tuscany, Nepal, Patagonia]')}
        Main Themes: {kwargs.get('themes', '[Insert Themes Here: e.g., self-discovery, cultural immersion, overcoming challenges]')}
        Emotional Hook: {kwargs.get('emotional_hook', 'Inspire wanderlust, evoke a sense of adventure, create a longing for exploration')}
        Unique Selling Proposition (USP): {kwargs.get('usp', '[Insert USP Here: e.g., off-the-beaten-path experiences, insider tips, stunning photography]')}
        Call to Action: {kwargs.get('call_to_action', 'Embark on your next adventure!')}

        Guidelines:

        *   **Evoke a sense of place:** Use vivid language and sensory details to transport the reader to the destination.  Describe the sights, sounds, smells, tastes, and textures of the location.
        *   **Highlight the journey:** Focus on the transformative power of travel.  Show how the journey changes the protagonist or the reader's perspective.
        *   **Emphasize discovery:**  Highlight the unique experiences and hidden gems that the book reveals.  Focus on cultural immersion, local encounters, and off-the-beaten-path adventures.
        *   **Create an emotional connection:** Tap into the reader's desire for adventure, exploration, and self-discovery.  Use language that is inspiring, evocative, and emotionally resonant.
        *   **Address the target audience:** Tailor the language and tone to the specific audience.  For example, a book for budget travelers will have a different tone than a book for luxury travelers.
        *   **Show, don't tell:** Use specific examples and anecdotes to illustrate the book's key themes and arguments.
        *   **Use strong verbs and descriptive adjectives:**  Make the language dynamic and engaging.
        *   **End with a compelling hook:** Leave the reader wanting to know more.
        *   **Consider including a quote from a review or endorsement.**
        *   **Mention any awards or recognition the book has received.**

        Example Structure:

        [Opening hook that grabs the reader's attention and introduces the destination.]

        [Briefly introduce the protagonist or the main focus of the book.]

        [Highlight the key themes and experiences of the journey.]

        [Emphasize the transformative power of travel and the unique insights the book offers.]

        [End with a call to action that encourages the reader to embark on their own adventure.]

        Write a back cover description that is approximately 150-200 words in length.  It should be concise, engaging, and persuasive.  It should accurately reflect the content and tone of the book.
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a short, impactful description
        for Travel books (2-3 lines).

        Args:
        **kwargs: Keyword arguments to pass specific details about the book.

        Returns:
        A string containing the prompt.
        """
        prompt = f"""
        Craft a short, compelling description (2-3 lines) for a Travel book.

        Genre: Travel

        Book Title: {kwargs.get('title', '[Insert Book Title Here]')}
        Destination: {kwargs.get('destination', '[Insert Destination Here]')}
        Core Idea: {kwargs.get('core_idea', '[Insert the core idea or unique selling proposition]')}

        Guidelines:

        *   **Focus on the essence:** Capture the most captivating element of the travel experience.
        *   **Highlight the destination's allure:** Use evocative language to paint a picture of the place.
        *   **Emphasize the unique perspective:** What makes this book different from other travel guides?
        *   **Inspire wanderlust:** Make the reader want to pack their bags and go.
        *   **Use concise and impactful language.**
        *   **Focus on the transformative power of travel.**
        *   **Consider using a question to pique the reader's interest.**

        Examples:

        *   "Escape to the sun-drenched shores of the Amalfi Coast, where ancient ruins whisper stories of empires past and the scent of lemon blossoms fills the air."
        *   "Discover the hidden trails of the Himalayas, where breathtaking landscapes and spiritual encounters await the intrepid traveler."
        *   "More than just a guide, this book is your passport to unlocking the soul of Kyoto, from serene Zen gardens to bustling geisha districts."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for creating a punchy marketing tagline for
        Travel books.

        Args:
        **kwargs: Keyword arguments to pass specific details about the book.

        Returns:
        A string containing the prompt.
        """
        prompt = f"""
        Craft a punchy and memorable marketing tagline for a Travel book.

        Genre: Travel

        Book Title: {kwargs.get('title', '[Insert Book Title Here]')}
        Destination: {kwargs.get('destination', '[Insert Destination Here]')}
        Key Selling Point: {kwargs.get('key_selling_point', '[Insert the most appealing aspect of the book]')}

        Guidelines:

        *   **Be concise and memorable:** Aim for a tagline that is easy to remember and repeat.
        *   **Highlight the destination's appeal:** Focus on what makes the location special.
        *   **Emphasize the transformative power of travel.**
        *   **Evoke a sense of adventure and excitement.**
        *   **Target the specific audience:** Tailor the language to resonate with the intended readers.
        *   **Use strong verbs and evocative language.**
        *   **Consider using a play on words or a clever pun.**

        Examples:

        *   "Unleash Your Inner Explorer."
        *   "Your Passport to Paradise."
        *   "The World Awaits."
        *   "Adventure Starts Here."
        *   "Discover. Dream. Travel."
        *   "Beyond the Guidebook."
        *   "Travel Deeper."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for defining visual style preferences for a Travel book's
        back cover design.

        Args:
        **kwargs: Keyword arguments to pass specific details about the book.

        Returns:
        A string containing the prompt.
        """
        prompt = f"""
        Define the visual style preferences for the back cover design of a Travel book.

        Genre: Travel

        Book Title: {kwargs.get('title', '[Insert Book Title Here]')}
        Destination: {kwargs.get('destination', '[Insert Destination Here]')}
        Target Audience: {kwargs.get('target_audience', '[Describe the target audience]')}
        Overall Tone: {kwargs.get('tone', '[Describe the desired tone: e.g., adventurous, romantic, sophisticated]')}

        Guidelines:

        *   **Imagery:**
        *   **Photography Style:** (e.g., vibrant, documentary, landscape, portrait, black and white, aerial)  Specify preferred photographic techniques (e.g., long exposure, shallow depth of field).
        *   **Subject Matter:** (e.g., landscapes, cityscapes, people, cultural events, food, wildlife)
        *   **Color Palette:** (e.g., bright and bold, muted and earthy, monochromatic, pastel) How does the color palette reflect the destination and tone?
        *   **Typography:**
        *   **Font Style:** (e.g., Serif, Sans-Serif, Script)  Consider legibility and readability.
        *   **Font Size and Weight:**  Ensure the text is easily readable.
        *   **Use of Hierarchy:**  How will different font sizes and styles be used to create visual hierarchy?
        *   **Layout:**
        *   **Overall Design:** (e.g., minimalist, cluttered, modern, vintage)
        *   **Use of White Space:**  How much white space should be used to create a clean and balanced design?
        *   **Placement of Elements:**  Where should the title, author name, tagline, and description be placed?
        *   **Branding:**
        *   **Logos and Trademarks:**  Include any relevant logos or trademarks.
        *   **Consistency:**  Ensure the design is consistent with the overall branding of the book and author.
        *   **Inspiration:**
        *   **Provide examples of back cover designs that you like.**  Explain what you like about them.
        *   **Consider the target audience:**  The visual style should appeal to the intended readers.  For example, a book for young adventurers might have a bold and colorful design, while a book for luxury travelers might have a more sophisticated and minimalist design.
        *   **Reflect the destination:**  The design should evoke the feeling and atmosphere of the destination.  For example, a book about Italy might use warm and earthy colors, while a book about Iceland might use cool and icy colors.
        """
        return prompt
        ```
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
def get_series_plan_prompt(**kwargs) -> str:
    return TravelPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return TravelPrompts.get_series_book_prompt(**kwargs)
