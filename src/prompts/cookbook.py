"""
Cookbook genre-specific prompts for novel generation.
"""

from .base_prompts import NonFictionBasePrompts

class CookbookPrompts(NonFictionBasePrompts):
    GENRE_NAME = "Cookbook"
    GENRE_DESCRIPTION = "A cookbook is a collection of recipes, often organized by category, cuisine, or dietary restriction. It provides detailed instructions for preparing specific dishes and may include information on ingredients, cooking techniques, nutritional value, and cultural context."
    
    GENRE_CHARACTERISTICS = [
        "Detailed and precise recipe instructions, including ingredient lists with specific measurements and cooking times.",
        "Clear and concise language, avoiding jargon or overly technical terms that may confuse novice cooks.",
        "Logical organization of recipes, often grouped by course (appetizers, entrees, desserts), cuisine (Italian, Mexican, Asian), or dietary restriction (vegetarian, gluten-free, vegan).",
        "Visually appealing presentation, including high-quality photographs of finished dishes to inspire readers.",
        "Helpful tips and techniques to improve cooking skills and ensure successful results.",
        "Information on ingredient sourcing, storage, and preparation to enhance the cooking experience.",
        "Nutritional information for each recipe, including calorie counts, macronutrient breakdowns, and potential allergens.",
        "Personal anecdotes or stories related to the recipes, adding a personal touch and cultural context.",
        "Variations and substitutions for ingredients to accommodate dietary restrictions or personal preferences.",
        "Equipment recommendations, specifying the necessary tools and appliances for each recipe."
    ]
    
    TYPICAL_ELEMENTS = [
        "Table of Contents: A comprehensive list of recipes organized by category.",
        "Introduction: An overview of the cookbook's purpose, target audience, and culinary philosophy.",
        "Ingredient Glossary: A list of common ingredients with definitions and usage tips.",
        "Equipment Guide: A guide to essential kitchen tools and appliances.",
        "Recipe Headnotes: Brief introductions to each recipe, providing context and inspiration.",
        "Ingredient Lists: Detailed lists of ingredients with precise measurements.",
        "Step-by-Step Instructions: Clear and concise instructions for preparing each recipe.",
        "Cooking Times and Temperatures: Specific cooking times and temperatures for optimal results.",
        "Serving Suggestions: Ideas for plating and serving each dish.",
        "Nutritional Information: Calorie counts, macronutrient breakdowns, and allergen information.",
        "Photographs: High-quality images of finished dishes.",
        "Index: An alphabetical listing of ingredients, dishes, and cooking techniques for easy reference."
    ]

    @classmethod
    def get_writer_profile_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_writer_profile_prompt(**kwargs)
        
        cookbook_additions = '''
## Cookbook-Specific Writing Considerations
- **Culinary Expertise**: Demonstrate a deep understanding of cooking techniques, ingredients, and flavor profiles. Highlight your experience in the specific cuisine or dietary area covered by the cookbook.
- **Recipe Development Process**: Explain your approach to recipe development, including sourcing inspiration, testing and refining recipes, and ensuring accuracy and consistency.
- **Target Audience**: Clearly define your target audience (e.g., beginner cooks, experienced chefs, individuals with dietary restrictions) and tailor your writing style and recipe complexity accordingly.
- **Voice and Tone**: Establish a consistent and engaging voice that reflects your personality and culinary philosophy. Consider whether you want to be informative, humorous, or inspirational.
- **Accuracy and Clarity**: Prioritize accuracy in ingredient measurements, cooking times, and instructions. Use clear and concise language to avoid ambiguity and ensure successful results.
- **Visual Presentation**: Emphasize the importance of visually appealing photographs and layout design to enhance the cookbook's overall appeal and inspire readers.
- **Testing and Feedback**: Describe your process for testing recipes and incorporating feedback from other cooks to ensure reliability and user-friendliness.
- **Ethical Considerations**: Address any ethical considerations related to food sourcing, sustainability, or cultural appropriation.
'''
        return base_prompt + cookbook_additions

    @classmethod
    def get_outline_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_outline_prompt(**kwargs)
        
        cookbook_additions = '''
## Cookbook-Specific Outline Requirements
- **Introduction**: Start with an introduction that outlines the cookbook's purpose, target audience, and culinary philosophy. Include a personal anecdote or story to connect with readers.
- **Ingredient Glossary**: Provide a comprehensive glossary of key ingredients, including definitions, sourcing information, and usage tips.
- **Equipment Guide**: Offer a guide to essential kitchen tools and appliances, explaining their functions and providing recommendations.
- **Recipe Categories**: Organize recipes into logical categories based on course, cuisine, dietary restriction, or theme.
- **Recipe Headnotes**: Include a brief introduction to each recipe, providing context, inspiration, and personal anecdotes.
- **Recipe Structure**: Ensure each recipe follows a consistent structure, including ingredient list, step-by-step instructions, cooking times, serving suggestions, and nutritional information.
- **Visual Elements**: Plan for the inclusion of high-quality photographs of finished dishes to enhance the cookbook's visual appeal.
- **Index**: Create a detailed index that allows readers to easily find recipes based on ingredients, dishes, or cooking techniques.
- **Appendix (Optional)**: Include an appendix with additional information, such as conversion charts, substitution guides, or tips for meal planning.
'''
        return base_prompt + cookbook_additions

    @classmethod
    def get_character_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_character_prompt(**kwargs)
        
        cookbook_additions = '''
## Cookbook-Specific Character Development
- **Culinary Persona**: While cookbooks don't typically feature fictional characters, consider the persona of the author or chef. What is their culinary background, expertise, and passion?
- **Target Audience**: Define the characteristics of your ideal reader. Are they beginner cooks, experienced chefs, or individuals with specific dietary needs?
- **Voice and Tone**: Develop a consistent voice and tone that reflects the author's personality and culinary philosophy. Are they informative, humorous, or inspirational?
- **Expertise and Authority**: Establish the author's credibility and expertise in the culinary field through their writing style, recipe selection, and culinary knowledge.
- **Relatability**: Make the author relatable to readers by sharing personal anecdotes, cooking tips, and insights into their culinary journey.
- **Inspiration**: Position the author as an inspiration to readers, encouraging them to explore new flavors, techniques, and cuisines.
'''
        return base_prompt + cookbook_additions

    @classmethod
    def get_chapter_prompt(cls, **kwargs) -> str:
        base_prompt = super().get_chapter_prompt(**kwargs)
        
        cookbook_additions = '''
## Cookbook-Specific Chapter Writing
- **Recipe Selection**: Choose recipes that align with the chapter's theme or category and offer a variety of flavors, techniques, and difficulty levels.
- **Recipe Headnotes**: Write engaging and informative headnotes that provide context, inspiration, and personal anecdotes for each recipe.
- **Ingredient Lists**: Create detailed and accurate ingredient lists with precise measurements and clear descriptions.
- **Step-by-Step Instructions**: Write clear, concise, and easy-to-follow instructions that guide readers through each step of the recipe.
- **Cooking Times and Temperatures**: Specify accurate cooking times and temperatures for optimal results.
- **Serving Suggestions**: Offer creative and appealing serving suggestions that enhance the presentation of each dish.
- **Nutritional Information**: Include nutritional information for each recipe, including calorie counts, macronutrient breakdowns, and allergen information.
- **Visual Elements**: Incorporate high-quality photographs of finished dishes to enhance the chapter's visual appeal and inspire readers.
- **Tips and Techniques**: Share helpful tips and techniques that improve cooking skills and ensure successful results.
- **Variations and Substitutions**: Provide variations and substitutions for ingredients to accommodate dietary restrictions or personal preferences.
'''
        return base_prompt + cookbook_additions

    @classmethod
    def get_series_plan_prompt(cls, **kwargs) -> str:
        """Generate a cookbook-specific series planning prompt."""
        base_prompt = super().get_series_plan_prompt(**kwargs)

        cookbook_series_additions = """

## Cookbook Series-Specific Planning Elements

### Educational Progression for Cookbook
- **Knowledge Building**: Structure learning progression appropriate for cookbook topics
- **Expertise Development**: Guide readers from basic to advanced understanding of cookbook subjects
- **Practical Applications**: Include actionable insights specific to cookbook throughout the series
- **Research Depth**: Plan comprehensive research appropriate for cookbook authority
- **Reader Value**: Ensure each book provides significant cookbook value while building series knowledge

### Cookbook Series Continuity
- **Subject Consistency**: Maintain consistent approach to cookbook topics across books
- **Authority Building**: Establish and maintain credibility in cookbook throughout the series
- **Information Architecture**: Structure information flow appropriate for cookbook learning
- **Cross-References**: Create meaningful connections between cookbook concepts across books
- **Updated Knowledge**: Plan for incorporating new cookbook research and developments

Create a cookbook series that provides comprehensive education with authoritative, well-researched content.
"""

        return base_prompt + cookbook_series_additions

    @classmethod
    def get_series_book_prompt(cls, **kwargs) -> str:
        """Generate a cookbook-specific individual book prompt within series context."""
        base_prompt = super().get_series_book_prompt(**kwargs)

        ```python
        class CookbookBackCover:

    @classmethod
    def get_back_cover_prompt(cls, **kwargs):
        """
        Generates a detailed prompt for creating a compelling cookbook back cover description.

        Args:
        **kwargs:  Keyword arguments to pass parameters to the prompt.

        Returns:
        str: A detailed prompt string tailored for cookbook back cover descriptions.
        """
        title = kwargs.get('title', '[Book Title]')
        author = kwargs.get('author', '[Author Name]')
        target_audience = kwargs.get('target_audience', '[Target Audience e.g., busy weeknight cooks, aspiring bakers]')
        cuisine_type = kwargs.get('cuisine_type', '[Cuisine Type e.g., Italian, Vegan, Paleo]')
        unique_selling_point = kwargs.get('unique_selling_point', '[Unique Selling Point e.g., 30-minute meals, budget-friendly recipes, family-friendly twists]')
        number_of_recipes = kwargs.get('number_of_recipes', '[Number of Recipes]')
        key_features = kwargs.get('key_features', '[Key Features e.g., step-by-step photos, nutritional information, dietary modifications]')
        emotional_hook = kwargs.get('emotional_hook', '[Emotional Hook e.g., rediscover the joy of cooking, impress your friends and family, nourish your body]')
        author_credentials = kwargs.get('author_credentials', '[Author Credentials e.g., award-winning chef, food blogger, registered dietitian]')

        prompt = f"""
        Write a compelling and enticing back cover description for the cookbook '{title}' by {author}.

        The target audience is {target_audience}. The cookbook focuses on {cuisine_type} cuisine and its unique selling point is {unique_selling_point}.

        The description should:

        *   Highlight the core benefits for the reader. What problems does this cookbook solve? How will it improve their cooking experience and their life?
        *   Clearly state that the cookbook contains {number_of_recipes} recipes.
        *   Showcase key features like {key_features}.
        *   Use evocative language related to food, taste, and cooking.  Think about sensory details (smell, texture, sight).
        *   Incorporate the emotional hook: {emotional_hook}.  Connect with the reader's desires and aspirations.
        *   Mention the author's credentials: {author_credentials}.  Establish credibility and expertise.
        *   End with a strong call to action, encouraging the reader to buy the book.

        Guidelines specific to cookbooks:

        *   Emphasize the ease of use and accessibility of the recipes.  Avoid overly technical language.
        *   Highlight any dietary considerations (e.g., gluten-free, vegetarian, vegan).
        *   If applicable, mention any beautiful photography or illustrations within the book.
        *   Focus on the practical benefits: saving time, saving money, improving health, etc.
        *   Consider including a tantalizing description of one or two signature recipes.
        *   Use active voice and vivid verbs.
        *   Keep the tone enthusiastic and inviting.

        Example Structure:

        [Opening sentence capturing the essence of the cookbook]

        [Expand on the unique selling point and benefits for the reader]

        [Highlight key features and recipe variety]

        [Mention author credentials and establish expertise]

        [Concluding sentence with a strong call to action]
        """
        return prompt

    @classmethod
    def get_short_description_prompt(cls, **kwargs):
        """
        Generates a prompt for a short, 2-3 line description for cookbook recommendations.

        Args:
        **kwargs: Keyword arguments to pass parameters to the prompt.

        Returns:
        str: A prompt string for a concise cookbook description.
        """
        title = kwargs.get('title', '[Book Title]')
        author = kwargs.get('author', '[Author Name]')
        cuisine_type = kwargs.get('cuisine_type', '[Cuisine Type e.g., Italian, Vegan, Paleo]')
        unique_selling_point = kwargs.get('unique_selling_point', '[Unique Selling Point e.g., 30-minute meals, budget-friendly recipes, family-friendly twists]')
        target_audience = kwargs.get('target_audience', '[Target Audience e.g., busy weeknight cooks, aspiring bakers]')

        prompt = f"""
        Write a short, 2-3 line description for recommending the cookbook '{title}' by {author}.

        The cookbook focuses on {cuisine_type} cuisine and is designed for {target_audience}. Its unique selling point is {unique_selling_point}.

        The description should:

        *   Be concise and impactful.
        *   Highlight the key benefit for the reader.
        *   Use enticing language related to food and cooking.
        *   Focus on the most appealing aspect of the cookbook.

        Example:

        "Craving authentic Italian flavors without the fuss? '{title}' delivers delicious, easy-to-follow recipes that bring the taste of Italy to your kitchen in under 30 minutes."
        """
        return prompt

    @classmethod
    def get_marketing_tagline_prompt(cls, **kwargs):
        """
        Generates a prompt for a punchy marketing tagline for a cookbook.

        Args:
        **kwargs: Keyword arguments to pass parameters to the prompt.

        Returns:
        str: A prompt string for generating cookbook taglines.
        """
        title = kwargs.get('title', '[Book Title]')
        cuisine_type = kwargs.get('cuisine_type', '[Cuisine Type e.g., Italian, Vegan, Paleo]')
        unique_selling_point = kwargs.get('unique_selling_point', '[Unique Selling Point e.g., 30-minute meals, budget-friendly recipes, family-friendly twists]')
        target_audience = kwargs.get('target_audience', '[Target Audience e.g., busy weeknight cooks, aspiring bakers]')
        key_ingredient = kwargs.get('key_ingredient', '[Key Ingredient or Theme e.g., Chocolate, Family Dinners, Healthy Eating]')

        prompt = f"""
        Create a punchy and memorable marketing tagline for the cookbook '{title}'.

        The cookbook focuses on {cuisine_type} cuisine, is designed for {target_audience}, and its unique selling point is {unique_selling_point}. It also emphasizes {key_ingredient}.

        The tagline should:

        *   Be short and catchy (ideally under 10 words).
        *   Highlight the key benefit or unique selling point.
        *   Use strong verbs and evocative language.
        *   Be memorable and easily shareable.
        *   Create a sense of excitement and anticipation.

        Examples:

        *   "{cuisine_type} Made Easy: Delicious Recipes, Effortless Cooking."
        *   "Unlock the Secrets to Perfect {key_ingredient} Every Time."
        *   "{title}: Your Kitchen, Your {cuisine_type} Adventure."
        """
        return prompt

    @classmethod
    def get_visual_style_preferences(cls, **kwargs):
        """
        Generates a prompt for describing visual style preferences for a cookbook's back cover.

        Args:
        **kwargs: Keyword arguments to pass parameters to the prompt.

        Returns:
        str: A prompt string for defining visual style preferences.
        """
        cuisine_type = kwargs.get('cuisine_type', '[Cuisine Type e.g., Italian, Vegan, Paleo]')
        target_audience = kwargs.get('target_audience', '[Target Audience e.g., busy weeknight cooks, aspiring bakers]')
        mood = kwargs.get('mood', '[Desired Mood e.g., warm, inviting, sophisticated, playful]')
        key_ingredient = kwargs.get('key_ingredient', '[Key Ingredient or Theme e.g., Chocolate, Family Dinners, Healthy Eating]')
        color_palette = kwargs.get('color_palette', '[Preferred Color Palette e.g., earthy tones, vibrant colors, minimalist black and white]')

        prompt = f"""
        Describe the desired visual style for the back cover of a cookbook focusing on {cuisine_type} cuisine for {target_audience}.

        The overall mood should be {mood}. The cookbook emphasizes {key_ingredient}. The preferred color palette is {color_palette}.

        The description should consider:

        *   Imagery: What kind of images would be most appealing? (e.g., close-ups of food, lifestyle shots of people cooking, ingredient displays)
        *   Typography: What font styles would be appropriate? (e.g., classic, modern, handwritten)
        *   Layout: How should the text and images be arranged? (e.g., clean and minimalist, layered and textured, full-bleed photography)
        *   Overall aesthetic: What is the overall feeling the back cover should evoke? (e.g., warmth, sophistication, playfulness, health-consciousness)
        *   Consider the visual representation of {cuisine_type} and how to best convey its essence.
        *   Think about how to visually represent the key ingredient or theme: {key_ingredient}.

        Examples:

        *   "Warm and inviting, with close-up shots of rustic Italian dishes. Use earthy tones and a classic serif font."
        *   "Clean and modern, with minimalist black and white photography of vegan ingredients. Use a sans-serif font and a simple layout."
        *   "Playful and colorful, with vibrant images of chocolate desserts. Use a handwritten font and a layered layout."
        """
        return prompt
        ```
        cookbook_book_additions = """

## Cookbook Series Book Integration

### Cookbook Knowledge Continuity
- **Building on Previous Learning**: Reference and build upon cookbook concepts from earlier books
- **Consistent Methodology**: Maintain research and presentation standards established in the series
- **Cross-References**: Include appropriate references to previous cookbook books when relevant
- **Knowledge Progression**: Advance reader understanding of cookbook topics appropriately
- **Authority Maintenance**: Continue the authoritative voice established in the cookbook series

### Book-Specific Cookbook Focus
- **Educational Objectives**: What specific cookbook knowledge will readers gain from this book?
- **Practical Applications**: What actionable cookbook insights will be provided?
- **Research Integration**: How will new cookbook research be incorporated?
- **Series Advancement**: How does this book advance the overall cookbook education series?
- **Reader Value**: What unique cookbook value does this book add to the series?

Ensure this book provides comprehensive cookbook education while serving as an integral part of the learning series.
"""

        return base_prompt + cookbook_book_additions

def get_writer_profile_prompt(**kwargs) -> str:
    return CookbookPrompts.get_writer_profile_prompt(**kwargs)

def get_outline_prompt(**kwargs) -> str:
    return CookbookPrompts.get_outline_prompt(**kwargs)

def get_character_prompt(**kwargs) -> str:
    return CookbookPrompts.get_character_prompt(**kwargs)

def get_chapter_prompt(**kwargs) -> str:
    return CookbookPrompts.get_chapter_prompt(**kwargs)

def get_enhancement_prompt(**kwargs) -> str:
    return CookbookPrompts.get_enhancement_prompt(**kwargs)
def get_series_plan_prompt(**kwargs) -> str:
    return CookbookPrompts.get_series_plan_prompt(**kwargs)

def get_back_cover_prompt(**kwargs) -> str:
    return {class_name}.get_back_cover_prompt(**kwargs)

def get_short_description_prompt(**kwargs) -> str:
    return {class_name}.get_short_description_prompt(**kwargs)

def get_marketing_tagline_prompt(**kwargs) -> str:
    return {class_name}.get_marketing_tagline_prompt(**kwargs)

def get_visual_style_preferences(**kwargs) -> str:
    return {class_name}.get_visual_style_preferences(**kwargs)


def get_series_book_prompt(**kwargs) -> str:
    return CookbookPrompts.get_series_book_prompt(**kwargs)
