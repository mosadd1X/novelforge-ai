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

def get_series_book_prompt(**kwargs) -> str:
    return CookbookPrompts.get_series_book_prompt(**kwargs)
