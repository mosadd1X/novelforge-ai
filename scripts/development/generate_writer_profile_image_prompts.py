#!/usr/bin/env python3
"""
Writer Profile Image Generation System

This script analyzes all writer profiles and generates detailed AI image generation prompts
for creating professional profile pictures. It also creates specifications for naming
conventions, folder structure, and image requirements.
"""

import sys
import os
import json
import importlib
from pathlib import Path
from typing import Dict, List, Any, Optional
sys.path.append('src')

from src.core.resilient_gemini_client import ResilientGeminiClient

def get_all_writer_profiles() -> List[Dict[str, Any]]:
    """Get all writer profiles from the master_profiles directory."""
    profiles = []
    profiles_dir = Path("src/writer_profiles/master_profiles")

    # Get all Python files in the directory
    for py_file in profiles_dir.glob("*.py"):
        if py_file.name.startswith("__"):
            continue

        module_name = py_file.stem
        try:
            # Import the module
            full_module_name = f"src.writer_profiles.master_profiles.{module_name}"
            module = importlib.import_module(full_module_name)

            # Get the profile data
            if hasattr(module, 'get_profile'):
                profile_data = module.get_profile()
                profile_data['module_name'] = module_name
                profiles.append(profile_data)
                print(f"✓ Loaded profile: {profile_data.get('name', module_name)}")
            else:
                print(f"⚠️  Skipped {module_name}: No get_profile function")

        except Exception as e:
            print(f"❌ Error loading {module_name}: {e}")
            continue

    return profiles

def load_existing_prompts() -> Dict[str, Any]:
    """Load existing prompts from JSON file if it exists."""
    prompts_file = Path("writer_profile_images/image_generation_prompts.json")
    if prompts_file.exists():
        try:
            with open(prompts_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Error loading existing prompts: {e}")
    return {"writers": []}

def is_valid_prompt(prompt: str) -> bool:
    """Check if a prompt is valid (not an error message)."""
    if not prompt or len(prompt.strip()) < 100:
        return False
    error_indicators = [
        "Error generating content",
        "429 You exceeded your current quota",
        "Please try again",
        "rate limit"
    ]
    return not any(indicator in prompt for indicator in error_indicators)

def create_image_generation_prompt(profile: Dict[str, Any], gemini_client) -> Optional[str]:
    """Create a detailed image generation prompt for a writer profile using Gemini AI."""

    # Extract key information
    name = profile.get('name', 'Unknown Writer')
    description = profile.get('description', '')
    cultural_background = profile.get('cultural_background', '')
    era = profile.get('era', '')
    biographical_context = profile.get('biographical_context', '')

    # Create a comprehensive prompt for Gemini to analyze
    analysis_prompt = f"""
    Analyze this fictional writer profile and create a detailed AI image generation prompt for their professional portrait:

    **Writer Profile:**
    Name: {name}
    Cultural Background: {cultural_background}
    Era: {era}
    Description: {description}
    Biographical Context: {biographical_context}

    **Requirements:**
    Create a single, comprehensive AI image generation prompt that includes:
    1. Physical appearance details (age range, facial features, expression)
    2. Clothing and style appropriate to their era and cultural background
    3. Setting/background that reflects their writing environment
    4. Lighting and mood that captures their literary personality
    5. Professional portrait composition
    6. Historical accuracy for their time period
    7. Cultural authenticity for their background

    **Format:** Provide ONLY the image generation prompt as a single paragraph, maximum 200 words, with vivid visual details that an AI image generator can understand. Do not include explanations or additional text.
    """

    try:
        response = gemini_client.generate_content(analysis_prompt)
        if response and response.strip():
            return response.strip()
        else:
            print(f"⚠️  Empty response for {name}")
            return None
    except Exception as e:
        print(f"❌ Error generating prompt for {name}: {e}")
        return None

def create_naming_convention_guide() -> str:
    """Create a guide for naming conventions and specifications."""
    return """
# Writer Profile Picture Specifications

## Image Requirements
- **Format**: JPG (preferred) or PNG
- **Size**: 800x800 pixels (square format)
- **Resolution**: 300 DPI minimum
- **Quality**: High quality, professional portrait style
- **Orientation**: Square (1:1 aspect ratio)

## Folder Structure
```
writer_profile_images/
├── portraits/
│   ├── writer_001_catherine.jpg
│   ├── writer_002_hiroshi.jpg
│   ├── writer_003_patricia.jpg
│   └── ...
└── specifications.txt (this file)
```

## Naming Convention
**Format**: `writer_[ID]_[shortname].jpg`

Where:
- **ID**: 3-digit number (001, 002, 003, etc.)
- **shortname**: First name in lowercase, max 10 characters
- **Extension**: .jpg (preferred) or .png

## Examples
- Catherine Fairfax → `writer_001_catherine.jpg`
- Hiroshi Nakamura → `writer_002_hiroshi.jpg`
- Dr. Patricia Blackwell → `writer_003_patricia.jpg`
- Professor Aldrich Quantum → `writer_004_aldrich.jpg`

## Style Guidelines
- Professional portrait style
- Clear, well-lit face
- Appropriate period clothing/styling
- Neutral or contextual background
- Serious or thoughtful expression
- High contrast and clarity
- Suitable for book back matter inclusion

## Cultural Sensitivity
- Ensure accurate representation of cultural backgrounds
- Respect historical periods and contexts
- Avoid stereotypes or caricatures
- Maintain dignity and professionalism

## Technical Notes
- Images will be resized to fit EPUB back matter sections
- Should look good at both full size and thumbnail
- Consider how they'll appear in black and white
- Ensure good contrast for accessibility
"""

def generate_short_name(full_name: str) -> str:
    """Generate a short name for file naming."""
    # Extract first name or title
    parts = full_name.lower().split()

    # Handle titles and prefixes
    if parts[0] in ['dr.', 'dr', 'professor', 'prof.', 'prof']:
        if len(parts) > 1:
            return parts[1][:10]

    # Use first name
    first_name = parts[0]

    # Remove common prefixes
    if first_name.startswith('dr.'):
        first_name = first_name[3:]

    return first_name[:10]

def main():
    """Generate image prompts for all writer profiles."""
    print("🎨 Writer Profile Image Generation System")
    print("=" * 60)

    # Initialize Gemini client
    try:
        gemini = ResilientGeminiClient()
        print("✓ Gemini AI client initialized")
    except Exception as e:
        print(f"❌ Failed to initialize Gemini client: {e}")
        return

    # Load all writer profiles
    print("\n📚 Loading writer profiles...")
    profiles = get_all_writer_profiles()
    print(f"✓ Loaded {len(profiles)} writer profiles")

    if not profiles:
        print("❌ No profiles found!")
        return

    # Create output directory
    output_dir = Path("writer_profile_images")
    output_dir.mkdir(exist_ok=True)
    (output_dir / "portraits").mkdir(exist_ok=True)

    # Load existing prompts
    print("\n🔍 Checking for existing prompts...")
    existing_data = load_existing_prompts()
    existing_writers = {w['name']: w for w in existing_data.get('writers', [])}

    # Filter out writers with valid existing prompts
    writers_to_process = []
    writers_with_valid_prompts = []

    for profile in profiles:
        name = profile.get('name', 'Unknown Writer')
        if name in existing_writers and is_valid_prompt(existing_writers[name].get('image_prompt', '')):
            writers_with_valid_prompts.append(name)
        else:
            writers_to_process.append(profile)

    print(f"✓ Found {len(writers_with_valid_prompts)} writers with valid existing prompts")
    print(f"📝 Need to generate prompts for {len(writers_to_process)} writers")

    if writers_with_valid_prompts:
        print(f"   Skipping: {', '.join(writers_with_valid_prompts[:5])}" +
              (f" and {len(writers_with_valid_prompts)-5} more..." if len(writers_with_valid_prompts) > 5 else ""))

    if not writers_to_process:
        print("🎉 All writers already have valid prompts! No generation needed.")
        return

    # Generate naming convention guide
    print("\n📋 Creating specifications file...")
    spec_content = create_naming_convention_guide()
    with open(output_dir / "specifications.txt", 'w', encoding='utf-8') as f:
        f.write(spec_content)
    print("✓ Specifications file created")

    # Start with existing data
    prompts_data = existing_data if existing_data.get('writers') else {
        "metadata": {
            "total_profiles": len(profiles),
            "generated_at": "2024-12-19",
            "specifications": {
                "image_size": "800x800 pixels",
                "format": "JPG preferred",
                "resolution": "300 DPI minimum",
                "style": "Professional portrait"
            }
        },
        "writers": []
    }

    # Update metadata
    prompts_data["metadata"]["total_profiles"] = len(profiles)
    prompts_data["metadata"]["last_updated"] = "2024-12-19"

    # Generate image prompts for missing writers only
    print(f"\n🎭 Generating image prompts for {len(writers_to_process)} remaining writers...")

    # Create a mapping of all profiles with their original IDs
    all_profiles_map = {profile.get('name'): (i+1, profile) for i, profile in enumerate(profiles)}

    for i, profile in enumerate(writers_to_process, 1):
        name = profile.get('name', f'Writer {i}')
        original_id = all_profiles_map[name][0]  # Get original ID from full list

        print(f"\n[{i}/{len(writers_to_process)}] Processing: {name} (ID: {original_id:03d})")

        # Check if this writer already exists in our data
        existing_writer = next((w for w in prompts_data["writers"] if w["name"] == name), None)

        if existing_writer and is_valid_prompt(existing_writer.get('image_prompt', '')):
            print(f"  ✓ Already has valid prompt, skipping...")
            continue

        # Generate short name for file naming
        short_name = generate_short_name(name)
        file_name = f"writer_{original_id:03d}_{short_name}.jpg"

        print(f"  📝 Generating AI prompt...")
        image_prompt = create_image_generation_prompt(profile, gemini)

        if image_prompt and is_valid_prompt(image_prompt):
            writer_data = {
                "id": original_id,
                "name": name,
                "short_name": short_name,
                "file_name": file_name,
                "cultural_background": profile.get('cultural_background', ''),
                "era": profile.get('era', ''),
                "primary_genres": profile.get('primary_genres', []),
                "image_prompt": image_prompt,
                "module_name": profile.get('module_name', '')
            }

            # Remove existing entry if it exists and add new one
            prompts_data["writers"] = [w for w in prompts_data["writers"] if w["name"] != name]
            prompts_data["writers"].append(writer_data)
            print(f"  ✓ Prompt generated ({len(image_prompt)} characters)")
        else:
            print(f"  ❌ Failed to generate valid prompt")
            if image_prompt:
                print(f"      Reason: Invalid prompt content")

            # If we hit rate limit, stop processing
            if "429" in str(image_prompt) or "quota" in str(image_prompt):
                print(f"  🛑 Rate limit detected, stopping generation...")
                break

    # Save all prompts to JSON file
    prompts_file = output_dir / "image_generation_prompts.json"
    with open(prompts_file, 'w', encoding='utf-8') as f:
        json.dump(prompts_data, f, indent=2, ensure_ascii=False)

    # Create a readable text file with prompts
    text_file = output_dir / "image_prompts_readable.txt"
    with open(text_file, 'w', encoding='utf-8') as f:
        f.write("WRITER PROFILE IMAGE GENERATION PROMPTS\n")
        f.write("=" * 50 + "\n\n")

        for writer in prompts_data["writers"]:
            f.write(f"Writer #{writer['id']:03d}: {writer['name']}\n")
            f.write(f"File Name: {writer['file_name']}\n")
            f.write(f"Cultural Background: {writer['cultural_background']}\n")
            f.write(f"Era: {writer['era']}\n")
            f.write(f"Genres: {', '.join(writer['primary_genres'])}\n")
            f.write(f"\nIMAGE PROMPT:\n{writer['image_prompt']}\n")
            f.write("\n" + "-" * 50 + "\n\n")

    # Sort writers by ID for consistent ordering
    prompts_data["writers"].sort(key=lambda x: x["id"])

    # Summary
    total_writers = len(profiles)
    valid_prompts = len([w for w in prompts_data["writers"] if is_valid_prompt(w.get('image_prompt', ''))])
    processed_this_run = len(writers_to_process)

    print(f"\n{'='*60}")
    print("GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"📊 Total writers: {total_writers}")
    print(f"✅ Writers with valid prompts: {valid_prompts}")
    print(f"📝 Processed this run: {processed_this_run}")
    print(f"🎯 Completion rate: {valid_prompts/total_writers*100:.1f}%")

    remaining = total_writers - valid_prompts
    if remaining > 0:
        print(f"⏳ Remaining to generate: {remaining}")
        print(f"💡 Run the script again when rate limits reset to continue")

    print(f"\n📁 Files created:")
    print(f"  📋 {output_dir}/specifications.txt - Image requirements and naming guide")
    print(f"  📄 {output_dir}/image_generation_prompts.json - Complete data (JSON)")
    print(f"  📝 {output_dir}/image_prompts_readable.txt - Human-readable prompts")

    print(f"\n🎯 Next Steps:")
    print(f"  1. Review the prompts in image_prompts_readable.txt")
    print(f"  2. Use your AI image generator with each prompt")
    print(f"  3. Save images with the specified file names")
    print(f"  4. Place images in writer_profile_images/portraits/ folder")
    print(f"  5. Ensure images meet the specifications (800x800px, JPG, 300 DPI)")

    if valid_prompts > 0:
        print(f"\n🎉 Ready for image generation! {valid_prompts} detailed prompts available.")
    else:
        print(f"\n⚠️  No prompts were generated successfully. Check Gemini API connection.")

if __name__ == "__main__":
    main()
