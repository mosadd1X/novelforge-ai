"""
Script to update all genre files to use the appropriate base class
(FictionBasePrompts, NonFictionBasePrompts, or SpecialFormatBasePrompts).
"""

import os
import sys
sys.path.append('src')

# Genre categorization
FICTION_GENRES = [
    "literary_fiction", "commercial_fiction", "mystery", "mysterythriller",
    "thriller", "romance", "fantasy", "epic_fantasy", "science_fiction",
    "historical_fiction", "horror", "young_adult", "middle_grade",
    "childrens_chapter_books", "speculative_fiction", "alternate_history",
    "contemporary_fiction", "paranormal_romance", "urban_fantasy", "dystopian"
]

NON_FICTION_GENRES = [
    "memoir", "biography", "history", "selfhelp", "business",
    "popular_science", "academic", "travel", "cookbook", "howto",
    "philosophy", "true_crime", "creative_nonfiction"
]

SPECIAL_FORMAT_GENRES = [
    "short_story_collection", "novella", "graphic_novel",
    "essay_collection", "poetry_collection"
]

def get_base_class_for_genre(genre: str) -> str:
    """Determine the appropriate base class for a genre."""
    if genre in FICTION_GENRES:
        return "FictionBasePrompts"
    elif genre in NON_FICTION_GENRES:
        return "NonFictionBasePrompts"
    elif genre in SPECIAL_FORMAT_GENRES:
        return "SpecialFormatBasePrompts"
    else:
        return "BasePrompts"  # fallback

def update_genre_file(genre: str) -> bool:
    """Update a single genre file to use the correct base class."""

    file_path = f"src/prompts/{genre}.py"
    if not os.path.exists(file_path):
        print(f"  ❌ File not found: {file_path}")
        return False

    try:
        # Read the current file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine the correct base class
        base_class = get_base_class_for_genre(genre)

        # Update the import statement
        old_import = "from .base_prompts import BasePrompts"
        new_import = f"from .base_prompts import {base_class}"

        if old_import in content:
            content = content.replace(old_import, new_import)
        else:
            # Handle case where import might be different
            content = content.replace(
                "from .base_prompts import",
                f"from .base_prompts import {base_class} #"
            ).replace(f"{base_class} #", base_class)

        # Update the class inheritance
        class_name = "".join(word.capitalize() for word in genre.split("_")) + "Prompts"
        old_class_def = f"class {class_name}(BasePrompts):"
        new_class_def = f"class {class_name}({base_class}):"

        if old_class_def in content:
            content = content.replace(old_class_def, new_class_def)
        else:
            # Try to find any class definition with BasePrompts
            import re
            pattern = rf"class {class_name}\([^)]*BasePrompts[^)]*\):"
            if re.search(pattern, content):
                content = re.sub(pattern, new_class_def, content)

        # Write the updated content back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  ✅ Updated {genre} to use {base_class}")
        return True

    except Exception as e:
        print(f"  ❌ Error updating {genre}: {str(e)}")
        return False

def main():
    """Update all genre files to use appropriate base classes."""

    print("🔄 Updating Genre Files to Use Specialized Base Classes")
    print("=" * 60)

    all_genres = FICTION_GENRES + NON_FICTION_GENRES + SPECIAL_FORMAT_GENRES

    print(f"\n📊 Genre Categorization:")
    print(f"  📚 Fiction: {len(FICTION_GENRES)} genres")
    print(f"  📖 Non-Fiction: {len(NON_FICTION_GENRES)} genres")
    print(f"  🎨 Special Formats: {len(SPECIAL_FORMAT_GENRES)} genres")
    print(f"  📋 Total: {len(all_genres)} genres")

    successful = 0
    failed = 0

    # Update Fiction genres
    print(f"\n📚 Updating Fiction Genres ({len(FICTION_GENRES)}):")
    for genre in FICTION_GENRES:
        if update_genre_file(genre):
            successful += 1
        else:
            failed += 1

    # Update Non-Fiction genres
    print(f"\n📖 Updating Non-Fiction Genres ({len(NON_FICTION_GENRES)}):")
    for genre in NON_FICTION_GENRES:
        if update_genre_file(genre):
            successful += 1
        else:
            failed += 1

    # Update Special Format genres
    print(f"\n🎨 Updating Special Format Genres ({len(SPECIAL_FORMAT_GENRES)}):")
    for genre in SPECIAL_FORMAT_GENRES:
        if update_genre_file(genre):
            successful += 1
        else:
            failed += 1

    # Summary
    print("\n" + "=" * 60)
    print("📊 UPDATE SUMMARY")
    print("=" * 60)
    print(f"✅ Successfully updated: {successful}")
    print(f"❌ Failed to update: {failed}")
    print(f"📁 Total files processed: {successful + failed}")

    if failed == 0:
        print("\n🎉 All genre files successfully updated!")
        print("🔧 The prompt system now uses specialized base classes:")
        print("   📚 Fiction genres use FictionBasePrompts (narrative focus)")
        print("   📖 Non-fiction genres use NonFictionBasePrompts (informational focus)")
        print("   🎨 Special formats use SpecialFormatBasePrompts (format-specific focus)")
    else:
        print(f"\n⚠️  {failed} files failed to update. Manual review may be needed.")

    print("\n💡 Next steps:")
    print("   1. Test the updated prompt system")
    print("   2. Verify that all genres work correctly")
    print("   3. Check that prompts are now more appropriate for each content type")

if __name__ == "__main__":
    main()
