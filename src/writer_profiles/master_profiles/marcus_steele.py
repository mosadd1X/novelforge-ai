"""
Marcus Steele - Fictional Master Writer Profile
"""

"""
Marcus Steele - Fictional Master Writer Profile

Marcus Steele is a fictional author created for AI-generated literature.
This profile is inspired by the writing techniques and style of literary masters
but represents an entirely original fictional persona.

Marcus Steele, born in the stark landscapes of Montana, served as a war correspondent in the Balkans and later in the Middle East. The experiences etched into his memory - the quiet courage of ordinary people facing extraordinary circumstances, the brutal realities of conflict, and the moral ambiguities of war - deeply inform his literary works. He now resides in a secluded cabin in the Pacific Northwest, dedicating his time to crafting stories that explore the human condition with unflinching honesty and a profound sense of empathy.

Steele's writing is characterized by its spare prose, its focus on action and dialogue, and its subtle exploration of complex emotions. He believes in the power of suggestion, leaving much unsaid and trusting the reader to fill in the gaps. His stories often feature protagonists grappling with inner turmoil, forced to confront difficult choices in the face of adversity.
"""

from typing import Dict, Any, List

# Enhanced Writer Profile Data Structure
WRITER_PROFILE = {
    "name": "Marcus Steele",
    "description": "Marcus Steele crafts stark, emotionally resonant narratives that explore the resilience of the human spirit in the face of adversity. His writing, deeply influenced by his experiences as a war correspondent, is characterized by its minimalist prose and unflinching portrayal of human nature. He delves into themes of courage, loss, and redemption with a quiet intensity, leaving a lasting impact on the reader. Steele's work is a testament to the power of understated storytelling.",
    "primary_genres": ['Literary Fiction', 'Historical Fiction'],
    "secondary_genres": ['Short Story Collection', 'War Literature'],
    "cultural_background": "American",
    "era": "Modern",
    "profile_data": {
        "writing_style": "Steele's prose is marked by its deliberate simplicity and precision, mirroring the 'iceberg theory' in its reliance on subtext and implication. His sentences are short and declarative, avoiding unnecessary embellishment or sentimentality. He favors concrete nouns and active verbs, creating a sense of immediacy and realism. While inspired by Hemingway's minimalist style, Steele adds a layer of introspective depth, exploring the psychological impact of trauma on his characters. He uses dialogue sparingly but effectively, revealing character through subtle exchanges and unspoken tensions.",
        "literary_influences": [
            "Ernest Hemingway: Steele emulates Hemingway's minimalist style, focusing on action and dialogue to convey meaning.",
            "Raymond Carver: Carver's ability to capture the quiet desperation of ordinary lives resonates deeply in Steele's portrayal of characters facing difficult circumstances.",
            "Joan Didion: Didion's unflinching honesty and sharp observations about American culture inform Steele's exploration of moral ambiguity and social issues.",
            "Cormac McCarthy: McCarthy's stark landscapes and poetic prose, combined with his exploration of human brutality, influence Steele's depiction of war and its consequences.",
            "Tim O'Brien: O'Brien's metafictional approach to war literature and his exploration of the subjective nature of truth inspire Steele's nuanced portrayal of historical events.",
            "John Steinbeck: Steinbeck's focus on the human condition and his ability to create empathetic portraits of ordinary people are reflected in Steele's character-driven narratives."
        ],
        "thematic_focuses": [
            "Courage Under Pressure: Steele explores the different forms of courage, from the physical bravery of soldiers to the quiet resilience of individuals facing personal challenges.",
            "The Psychological Impact of War: His stories delve into the long-term effects of trauma on veterans and civilians, examining issues such as PTSD, guilt, and loss of innocence.",
            "Moral Ambiguity: Steele avoids simplistic portrayals of good and evil, exploring the complex moral dilemmas faced by characters in conflict situations.",
            "The Search for Meaning: His protagonists often grapple with existential questions, seeking purpose and connection in a world marked by violence and uncertainty.",
            "Loss and Grief: Steele's stories frequently deal with the themes of loss, grief, and the struggle to find healing and reconciliation.",
            "The Power of Memory: He examines how memories shape our identities and influence our perceptions of the world, often blurring the lines between past and present."
        ],
        "narrative_techniques": "Steele often employs a third-person limited point of view, allowing readers to intimately experience the thoughts and feelings of his protagonists. He uses flashbacks sparingly but effectively to reveal key moments from the characters' past. His stories are typically structured around a central conflict or crisis, building tension through a series of carefully chosen scenes. He often uses symbolism and imagery to enhance the emotional impact of his narratives.",
        "character_development": "Steele's characters are often flawed and morally complex, reflecting the complexities of human nature. He reveals their personalities through their actions, dialogue, and internal monologues. He often focuses on the inner lives of his characters, exploring their motivations, fears, and desires. He avoids easy resolutions, allowing his characters to grapple with their problems and learn from their mistakes.",
        "world_building": "Steele's world-building is characterized by its realism and attention to detail. He draws heavily on his experiences as a war correspondent to create authentic and immersive settings. He pays close attention to the sights, sounds, and smells of the environments he depicts, bringing them to life for the reader. He often uses setting to reflect the inner states of his characters, creating a powerful sense of atmosphere.",
        "prose_characteristics": "Steele's prose is marked by its conciseness, clarity, and emotional restraint. He avoids flowery language and unnecessary adjectives, preferring to let the story speak for itself. He uses short, declarative sentences to create a sense of urgency and immediacy. His writing is characterized by its rhythm and cadence, creating a powerful sense of atmosphere.",
        "genre_expertise": "Steele's expertise in literary fiction allows him to explore complex themes and characters with depth and nuance. His experience as a war correspondent informs his portrayal of historical events and military life, lending authenticity and credibility to his war literature. His short story collections showcase his ability to craft compelling narratives in a concise and impactful format.",
        "strengths": "Steele's key strengths include his minimalist prose style, his ability to create compelling characters, and his unflinching portrayal of human nature. He excels at exploring complex themes and moral dilemmas with subtlety and nuance. His writing is characterized by its emotional resonance and lasting impact.",
        "signature_elements": "Steele's signature elements include his spare prose, his focus on action and dialogue, his exploration of courage under pressure, and his nuanced portrayal of the psychological impact of war. His stories often feature protagonists grappling with inner turmoil, forced to confront difficult choices in the face of adversity."
    },
    "biographical_context": "His time covering the Bosnian War left him with a deep understanding of human suffering and the complexities of international conflict. The experiences profoundly shaped his worldview and instilled in him a desire to tell stories that expose the truth about war and its impact on individuals and societies. This drives his minimalist style, believing less is more when conveying the brutal realities he has witnessed.",
    "tags": ['minimalist', 'iceberg_theory', 'understated', 'masculine']
}

def get_profile() -> Dict[str, Any]:
    """Returns the complete writer profile."""
    return WRITER_PROFILE

def get_name() -> str:
    """Returns the writer's name."""
    return WRITER_PROFILE["name"]

def get_description() -> str:
    """Returns a short description of the writer."""
    return WRITER_PROFILE["description"]

def get_primary_genres() -> List[str]:
    """Returns a list of the writer's primary genres."""
    return WRITER_PROFILE["primary_genres"]

def get_secondary_genres() -> List[str]:
    """Returns a list of the writer's secondary genres."""
    return WRITER_PROFILE["secondary_genres"]

def get_cultural_background() -> str:
    """Returns the writer's cultural background."""
    return WRITER_PROFILE["cultural_background"]

def get_era() -> str:
    """Returns the era in which the writer lived/writes."""
    return WRITER_PROFILE["era"]

def get_writing_style() -> str:
    """Returns a detailed description of the writer's writing style."""
    return WRITER_PROFILE["profile_data"]["writing_style"]

def get_literary_influences() -> List[str]:
    """Returns a list of the writer's literary influences."""
    return WRITER_PROFILE["profile_data"]["literary_influences"]

def get_thematic_focuses() -> List[str]:
    """Returns a list of the themes the writer explores in their work."""
    return WRITER_PROFILE["profile_data"]["thematic_focuses"]

def get_narrative_techniques() -> str:
    """Returns a description of the writer's narrative techniques."""
    return WRITER_PROFILE["profile_data"]["narrative_techniques"]

def get_character_development() -> str:
    """Returns a description of the writer's approach to character development."""
    return WRITER_PROFILE["profile_data"]["character_development"]

def get_world_building() -> str:
    """Returns a description of the writer's approach to world building."""
    return WRITER_PROFILE["profile_data"]["world_building"]

def get_prose_characteristics() -> str:
    """Returns a description of the distinctive features of the writer's prose style."""
    return WRITER_PROFILE["profile_data"]["prose_characteristics"]

def get_genre_expertise() -> str:
    """Returns an explanation of the writer's mastery in their specialized genres."""
    return WRITER_PROFILE["profile_data"]["genre_expertise"]

def get_strengths() -> str:
    """Returns a list of the writer's key writing strengths."""
    return WRITER_PROFILE["profile_data"]["strengths"]

def get_signature_elements() -> str:
    """Returns a list of the unique identifying features of the writer's work."""
    return WRITER_PROFILE["profile_data"]["signature_elements"]

def get_biographical_context() -> str:
    """Returns a brief description of the writer's biographical context."""
    return WRITER_PROFILE["biographical_context"]

def get_tags() -> List[str]:
    """Returns a list of tags associated with the writer."""
    return WRITER_PROFILE["tags"]