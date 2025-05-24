#!/usr/bin/env python3
"""
Generate Fictional Master Writer Profiles

This script automatically generates 25-30 fictional master writer profiles
inspired by real literary masters but with original fictional identities.
Each profile covers 2-4 genres to ensure complete coverage of all 38 genres.
"""

import sys
import time
from pathlib import Path
from typing import Dict, Any

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.core.gemini_client import GeminiClient
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.panel import Panel

console = Console(markup=True)

# Fictional Master Writer Profiles Configuration
FICTIONAL_MASTER_PROFILES = [
    {
        "name": "Elena Thornfield",
        "inspiration": "Virginia Woolf",
        "cultural_background": "British",
        "era": "Modernist",
        "primary_genres": ["Literary Fiction", "Memoir"],
        "secondary_genres": ["Essay Collection", "Creative Non-Fiction"],
        "style_tags": ["stream_of_consciousness", "psychological_realism", "experimental", "feminist"],
        "bio_context": "Born into an intellectual Victorian family, largely self-educated with access to extensive libraries. Pioneered experimental narrative techniques."
    },
    {
        "name": "Marcus Steele",
        "inspiration": "Ernest Hemingway",
        "cultural_background": "American",
        "era": "Modern",
        "primary_genres": ["Literary Fiction", "Historical Fiction"],
        "secondary_genres": ["Short Story Collection", "War Literature"],
        "style_tags": ["minimalist", "iceberg_theory", "understated", "masculine"],
        "bio_context": "Former journalist and war correspondent. Known for spare prose and exploration of courage under pressure."
    },
    {
        "name": "Rajesh Malhotra",
        "inspiration": "R.K. Narayan",
        "cultural_background": "Indian",
        "era": "Modern",
        "primary_genres": ["Literary Fiction", "Short Story Collection"],
        "secondary_genres": ["Contemporary Fiction", "Humor"],
        "style_tags": ["gentle_humor", "everyday_life", "regional_fiction", "universal_themes"],
        "bio_context": "Created the fictional town of Malgudi. Master of gentle irony and observation of middle-class Indian life."
    },
    {
        "name": "Victoria Blackwood",
        "inspiration": "Agatha Christie",
        "cultural_background": "British",
        "era": "Golden Age",
        "primary_genres": ["Mystery", "Mystery/Thriller"],
        "secondary_genres": ["Novella", "Crime Fiction"],
        "style_tags": ["puzzle_plots", "fair_play", "ingenious_mysteries", "logical_deduction"],
        "bio_context": "Former nurse with knowledge of poisons. Created memorable detectives and impossible crime scenarios."
    },
    {
        "name": "Dr. Samuel Voss",
        "inspiration": "Isaac Asimov",
        "cultural_background": "Russian-American",
        "era": "Golden Age",
        "primary_genres": ["Science Fiction", "Popular Science"],
        "secondary_genres": ["Academic", "Short Story Collection"],
        "style_tags": ["hard_sf", "scientific", "educational", "galactic_scope"],
        "bio_context": "Biochemist turned writer. Pioneer of robotics fiction and galactic civilization narratives."
    },
    {
        "name": "Priya Sharma",
        "inspiration": "Toni Morrison",
        "cultural_background": "Indian-American",
        "era": "Contemporary",
        "primary_genres": ["Literary Fiction", "Historical Fiction"],
        "secondary_genres": ["Contemporary Fiction", "Cultural Literature"],
        "style_tags": ["magical_realism", "cultural_identity", "trauma", "lyrical"],
        "bio_context": "Explores themes of cultural displacement and identity through lyrical, emotionally powerful narratives."
    },
    {
        "name": "Arjun Krishnamurthy",
        "inspiration": "Mulk Raj Anand",
        "cultural_background": "Indian",
        "era": "Modern",
        "primary_genres": ["Literary Fiction", "Historical Fiction"],
        "secondary_genres": ["Social Commentary", "Political Fiction"],
        "style_tags": ["social_realism", "progressive", "humanist", "class_consciousness"],
        "bio_context": "Social reformer and writer focused on caste system and social justice themes."
    },
    {
        "name": "Kavya Nair",
        "inspiration": "Kamala Das",
        "cultural_background": "Indian",
        "era": "Contemporary",
        "primary_genres": ["Memoir", "Poetry Collection"],
        "secondary_genres": ["Creative Non-Fiction", "Autobiography"],
        "style_tags": ["confessional", "feminist", "intimate", "bold"],
        "bio_context": "Pioneering voice in confessional writing, exploring themes of sexuality and female identity."
    },
    {
        "name": "Ananya Desai",
        "inspiration": "Arundhati Roy",
        "cultural_background": "Indian",
        "era": "Contemporary",
        "primary_genres": ["Literary Fiction", "Contemporary Fiction"],
        "secondary_genres": ["Creative Non-Fiction", "Environmental Literature"],
        "style_tags": ["lyrical", "environmental", "political", "sensuous"],
        "bio_context": "Environmental activist and writer known for lush, politically engaged narratives."
    },
    {
        "name": "Vikram Chandra",
        "inspiration": "Vikram Seth",
        "cultural_background": "Indian",
        "era": "Contemporary",
        "primary_genres": ["Literary Fiction", "Poetry Collection"],
        "secondary_genres": ["Historical Fiction", "Epic Fiction"],
        "style_tags": ["versatile", "epic_scope", "detailed", "classical"],
        "bio_context": "Versatile writer capable of both intimate poetry and sweeping historical epics."
    },
    {
        "name": "Rohan Mehta",
        "inspiration": "Chetan Bhagat",
        "cultural_background": "Indian",
        "era": "Contemporary",
        "primary_genres": ["Contemporary Fiction", "Commercial Fiction"],
        "secondary_genres": ["Young Adult", "Romance"],
        "style_tags": ["accessible", "youth_culture", "contemporary_issues", "popular"],
        "bio_context": "Former engineer turned bestselling author, voice of modern Indian youth culture."
    },
    {
        "name": "Devika Ghosh",
        "inspiration": "Amitav Ghosh",
        "cultural_background": "Indian",
        "era": "Contemporary",
        "primary_genres": ["Historical Fiction", "Literary Fiction"],
        "secondary_genres": ["Travel", "Cultural Studies"],
        "style_tags": ["historical", "colonial", "migration", "scholarly"],
        "bio_context": "Scholar-writer exploring themes of migration, colonialism, and cultural intersection."
    },
    {
        "name": "Sebastian Darkmore",
        "inspiration": "Stephen King",
        "cultural_background": "American",
        "era": "Contemporary",
        "primary_genres": ["Horror", "Thriller"],
        "secondary_genres": ["Supernatural Fiction", "Contemporary Fiction"],
        "style_tags": ["supernatural", "psychological_horror", "prolific", "accessible"],
        "bio_context": "Master of psychological horror and supernatural fiction, exploring the dark side of small-town America."
    },
    {
        "name": "Professor Aldrich Quantum",
        "inspiration": "J.R.R. Tolkien",
        "cultural_background": "British",
        "era": "Modern",
        "primary_genres": ["Fantasy", "Epic Fantasy"],
        "secondary_genres": ["Middle Grade", "Mythology"],
        "style_tags": ["high_fantasy", "world_building", "linguistic", "mythological"],
        "bio_context": "Philologist and linguist who created detailed fantasy worlds with their own languages and mythologies."
    },
    {
        "name": "Catherine Fairfax",
        "inspiration": "Jane Austen",
        "cultural_background": "British",
        "era": "Regency",
        "primary_genres": ["Romance", "Historical Fiction"],
        "secondary_genres": ["Commercial Fiction", "Social Commentary"],
        "style_tags": ["wit", "social_commentary", "irony", "marriage_plots"],
        "bio_context": "Sharp observer of social manners and romantic relationships in changing society."
    },
    {
        "name": "Gabriel Montoya",
        "inspiration": "Gabriel García Márquez",
        "cultural_background": "Colombian",
        "era": "Contemporary",
        "primary_genres": ["Literary Fiction", "Speculative Fiction"],
        "secondary_genres": ["Short Story Collection", "Magical Realism"],
        "style_tags": ["magical_realism", "latin_american", "political", "lyrical"],
        "bio_context": "Master of magical realism, blending fantastical elements with political and social commentary."
    },
    {
        "name": "Hiroshi Nakamura",
        "inspiration": "Haruki Murakami",
        "cultural_background": "Japanese",
        "era": "Contemporary",
        "primary_genres": ["Contemporary Fiction", "Speculative Fiction"],
        "secondary_genres": ["Urban Fantasy", "Surreal Fiction"],
        "style_tags": ["surreal", "pop_culture", "alienation", "dreamlike"],
        "bio_context": "Explores themes of alienation and identity in modern urban life through surreal, dreamlike narratives."
    },
    {
        "name": "Grace Washington",
        "inspiration": "Maya Angelou",
        "cultural_background": "African American",
        "era": "Contemporary",
        "primary_genres": ["Memoir", "Biography"],
        "secondary_genres": ["Poetry Collection", "Inspirational"],
        "style_tags": ["autobiographical", "resilience", "lyrical", "empowering"],
        "bio_context": "Civil rights activist and memoirist known for powerful autobiographical works exploring resilience and identity."
    },
    {
        "name": "Dr. Malcolm Sterling",
        "inspiration": "Malcolm Gladwell",
        "cultural_background": "Canadian",
        "era": "Contemporary",
        "primary_genres": ["Popular Science", "Business"],
        "secondary_genres": ["Self-Help", "Psychology"],
        "style_tags": ["analytical", "accessible", "research_based", "storytelling"],
        "bio_context": "Journalist and social scientist known for making complex research accessible through compelling narratives."
    },
    {
        "name": "Anthony Rivers",
        "inspiration": "Anthony Bourdain",
        "cultural_background": "American",
        "era": "Contemporary",
        "primary_genres": ["Travel", "Memoir"],
        "secondary_genres": ["Cookbook", "Cultural Commentary"],
        "style_tags": ["culinary", "travel", "irreverent", "authentic"],
        "bio_context": "Chef and travel writer known for authentic, irreverent exploration of food and culture around the world."
    },
    {
        "name": "Dr. Patricia Blackwell",
        "inspiration": "Malcolm Gladwell + business expertise",
        "cultural_background": "American",
        "era": "Contemporary",
        "primary_genres": ["Business", "Self-Help"],
        "secondary_genres": ["How-To", "Philosophy"],
        "style_tags": ["analytical", "practical", "accessible", "research_based"],
        "bio_context": "Business consultant and researcher who makes complex concepts accessible through storytelling and practical examples."
    },
    {
        "name": "Luna Brightwater",
        "inspiration": "Roald Dahl + modern children's literature",
        "cultural_background": "British",
        "era": "Contemporary",
        "primary_genres": ["Children's Chapter Books", "Middle Grade"],
        "secondary_genres": ["Graphic Novel", "Young Adult"],
        "style_tags": ["whimsical", "imaginative", "age_appropriate", "engaging"],
        "bio_context": "Former teacher turned children's author, known for creating magical worlds that inspire young readers."
    },
    {
        "name": "Professor Elena Vasquez",
        "inspiration": "Academic writing + essay tradition",
        "cultural_background": "Spanish",
        "era": "Contemporary",
        "primary_genres": ["Academic", "Essay Collection"],
        "secondary_genres": ["Philosophy", "History"],
        "style_tags": ["scholarly", "analytical", "thoughtful", "rigorous"],
        "bio_context": "Philosophy professor and essayist who bridges academic rigor with accessible intellectual discourse."
    },
    {
        "name": "Detective Marcus Kane",
        "inspiration": "True crime + police procedural",
        "cultural_background": "American",
        "era": "Contemporary",
        "primary_genres": ["True Crime", "Mystery/Thriller"],
        "secondary_genres": ["Thriller", "Crime Fiction"],
        "style_tags": ["investigative", "detailed", "procedural", "authentic"],
        "bio_context": "Retired detective turned true crime writer, bringing authentic police experience to crime narratives."
    },
    {
        "name": "Dr. Sophia Chronos",
        "inspiration": "Historical scholarship + narrative history",
        "cultural_background": "Greek-American",
        "era": "Contemporary",
        "primary_genres": ["History", "Alternate History"],
        "secondary_genres": ["Academic", "Historical Fiction"],
        "style_tags": ["scholarly", "narrative", "detailed", "engaging"],
        "bio_context": "Historian who brings academic rigor to popular history writing, making the past accessible to general readers."
    },
    {
        "name": "Raven Nightshade",
        "inspiration": "Paranormal romance + urban fantasy",
        "cultural_background": "American",
        "era": "Contemporary",
        "primary_genres": ["Paranormal Romance", "Urban Fantasy"],
        "secondary_genres": ["Fantasy", "Romance"],
        "style_tags": ["supernatural", "romantic", "atmospheric", "sensual"],
        "bio_context": "Writer specializing in supernatural romance, creating immersive worlds where magic and love intertwine."
    },
    {
        "name": "Zara Blackthorn",
        "inspiration": "Dystopian fiction + social commentary",
        "cultural_background": "Canadian",
        "era": "Contemporary",
        "primary_genres": ["Dystopian", "Speculative Fiction"],
        "secondary_genres": ["Science Fiction", "Young Adult"],
        "style_tags": ["dystopian", "social_commentary", "thought_provoking", "atmospheric"],
        "bio_context": "Speculative fiction writer exploring themes of social control, resistance, and human resilience in imagined futures."
    }
]

def create_profile_generation_prompt(profile_config: Dict[str, Any]) -> str:
    """Create a detailed prompt for generating a fictional master writer profile."""

    prompt = f"""
Create a comprehensive fictional master writer profile for "{profile_config['name']}", a fictional author inspired by the writing style and techniques of {profile_config['inspiration']} but with a completely original fictional identity.

**IMPORTANT GUIDELINES:**
- This is a FICTIONAL author with an invented biography and identity
- Do NOT use any real author names or claim this is a real person
- Create original biographical details that feel authentic but are entirely fictional
- The writing style should be inspired by {profile_config['inspiration']} but adapted for this fictional persona
- Maintain the sophisticated literary analysis while keeping the fictional nature clear

**Profile Configuration:**
- Name: {profile_config['name']} (FICTIONAL AUTHOR)
- Cultural Background: {profile_config['cultural_background']}
- Era: {profile_config['era']}
- Primary Genres: {', '.join(profile_config['primary_genres'])}
- Secondary Genres: {', '.join(profile_config['secondary_genres'])}
- Style Tags: {', '.join(profile_config['style_tags'])}
- Biographical Context: {profile_config['bio_context']}

Generate a complete Python module with the following structure:

```python
\"\"\"
{profile_config['name']} - Fictional Master Writer Profile

{profile_config['name']} is a fictional author created for AI-generated literature.
This profile is inspired by the writing techniques and style of literary masters
but represents an entirely original fictional persona.

[Include 2-3 paragraphs describing the fictional author's background and approach]
\"\"\"

from typing import Dict, Any, List

# Enhanced Writer Profile Data Structure
WRITER_PROFILE = {{
    "name": "{profile_config['name']}",
    "description": "[3-4 sentences describing this fictional author's unique approach and philosophy]",
    "primary_genres": {profile_config['primary_genres']},
    "secondary_genres": {profile_config['secondary_genres']},
    "cultural_background": "{profile_config['cultural_background']}",
    "era": "{profile_config['era']}",
    "profile_data": {{
        "writing_style": "[Detailed 4-5 sentence analysis of prose style, inspired by {profile_config['inspiration']} but adapted for this fictional author]",
        "literary_influences": [
            "[List 5-6 real literary influences with explanations of how they shaped this fictional author's style]"
        ],
        "thematic_focuses": [
            "[List 4-6 sophisticated themes this fictional author explores, with detailed explanations]"
        ],
        "narrative_techniques": "[Detailed description of storytelling methods and structural approaches]",
        "character_development": "[Description of how this fictional author creates and develops characters]",
        "world_building": "[Approach to creating settings and atmospheres]",
        "prose_characteristics": "[Distinctive features of the fictional author's prose style]",
        "genre_expertise": "[Explanation of mastery in their specialized genres]",
        "strengths": "[Key writing strengths and specializations]",
        "signature_elements": "[Unique identifying features of this fictional author's work]"
    }},
    "biographical_context": "[2-3 sentences of FICTIONAL biographical background that influences writing style]",
    "tags": {profile_config['style_tags']}
}}

[Include all the standard helper functions: get_profile(), get_writing_style(), etc.]
```

Make this fictional author feel authentic and well-developed while maintaining clear fictional status. The literary analysis should be sophisticated and detailed, worthy of a master-level writer profile.
"""

    return prompt

def generate_profile_file(gemini: GeminiClient, profile_config: Dict[str, Any]) -> bool:
    """Generate a single fictional master writer profile file."""

    profile_name = profile_config['name']
    filename = profile_config['name'].lower().replace(' ', '_').replace('.', '') + '.py'

    console.print(f"  📝 Generating {profile_name}...")

    try:
        # Create the prompt
        prompt = create_profile_generation_prompt(profile_config)

        # Generate the content
        response = gemini.generate_content(prompt, temperature=0.7, max_tokens=4000)

        if not response or len(response.strip()) < 1000:
            console.print(f"    ❌ Generated content too short for {profile_name}")
            return False

        # Create the file content
        file_content = response.strip()

        # Ensure the file starts with proper docstring
        if not file_content.startswith('"""'):
            file_content = f'"""\n{profile_name} - Fictional Master Writer Profile\n"""\n\n' + file_content

        # Save the file
        output_path = Path("src/writer_profiles/master_profiles") / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(file_content)

        console.print(f"    ✅ Generated {filename}")
        return True

    except Exception as e:
        console.print(f"    ❌ Failed to generate {profile_name}: {e}")
        return False

def main():
    """Generate all fictional master writer profiles."""

    console.print(Panel.fit(
        "[bold cyan]🎭 Fictional Master Writer Profile Generator[/bold cyan]\n"
        f"Generating {len(FICTIONAL_MASTER_PROFILES)} fictional author profiles\n"
        "Each profile inspired by literary masters but with original fictional identities",
        border_style="cyan"
    ))

    # Initialize Gemini client
    try:
        gemini = GeminiClient()
        console.print("[green]✅ Gemini client initialized[/green]")
    except Exception as e:
        console.print(f"[red]❌ Failed to initialize Gemini client: {e}[/red]")
        return

    # Generate profiles
    successful_profiles = 0
    failed_profiles = 0

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console
    ) as progress:

        task = progress.add_task("Generating profiles...", total=len(FICTIONAL_MASTER_PROFILES))

        for profile_config in FICTIONAL_MASTER_PROFILES:
            if generate_profile_file(gemini, profile_config):
                successful_profiles += 1
            else:
                failed_profiles += 1

            progress.advance(task)
            time.sleep(1)  # Rate limiting

    # Summary
    console.print(f"\n[bold cyan]Generation Summary:[/bold cyan]")
    console.print(f"  ✅ Successful: {successful_profiles}")
    console.print(f"  ❌ Failed: {failed_profiles}")
    console.print(f"  📊 Success Rate: {(successful_profiles/len(FICTIONAL_MASTER_PROFILES))*100:.1f}%")

    if successful_profiles > 0:
        console.print(f"\n[green]🎉 Generated {successful_profiles} fictional master writer profiles![/green]")
        console.print("[cyan]Files created in: src/writer_profiles/master_profiles/[/cyan]")
    else:
        console.print("[red]❌ No profiles were generated successfully.[/red]")

if __name__ == "__main__":
    main()
