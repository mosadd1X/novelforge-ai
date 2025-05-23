"""
Debug the History matching issue.
"""

def debug_should_generate_characters(genre: str) -> bool:
    """Debug version to see what's happening."""
    fiction_genres = [
        "literary fiction", "commercial fiction", "mystery", "mystery thriller", 
        "thriller", "romance", "fantasy", "epic fantasy", "science fiction", 
        "historical fiction", "horror", "young adult", "middle grade", 
        "children's chapter books", "speculative fiction", "alternate history", 
        "contemporary fiction", "paranormal romance", "urban fantasy", "dystopian",
        "test"
    ]
    
    genre_normalized = genre.lower().strip()
    print(f"\nTesting genre: '{genre}' (normalized: '{genre_normalized}')")
    
    # Check if it's a fiction genre that needs characters
    # First check for exact matches
    print("Checking exact matches...")
    for fiction_genre in fiction_genres:
        if fiction_genre.lower() == genre_normalized:
            print(f"  ✅ Exact match found: '{fiction_genre}' == '{genre_normalized}'")
            return True
        else:
            print(f"  ❌ No exact match: '{fiction_genre}' != '{genre_normalized}'")
    
    # Then check for partial matches, but be very careful
    print("Checking partial matches...")
    for fiction_genre in fiction_genres:
        # Only allow partial matches if the genre is clearly contained
        if genre_normalized in fiction_genre.lower() and len(genre_normalized) > 3:
            print(f"  🔍 Potential match: '{genre_normalized}' in '{fiction_genre.lower()}'")
            # Avoid false positives like "history" matching "historical fiction"
            if genre_normalized == "history" and fiction_genre.lower() == "historical fiction":
                print(f"    ⏭️ Skipping false positive: history vs historical fiction")
                continue
            if genre_normalized == "science" and fiction_genre.lower() == "science fiction":
                print(f"    ⏭️ Skipping false positive: science vs science fiction")
                continue
            print(f"    ✅ Valid partial match found!")
            return True
        else:
            if genre_normalized in fiction_genre.lower():
                print(f"  ❌ Rejected (too short): '{genre_normalized}' in '{fiction_genre.lower()}' but len={len(genre_normalized)} <= 3")
            else:
                print(f"  ❌ No match: '{genre_normalized}' not in '{fiction_genre.lower()}'")
    
    # All other genres (non-fiction and special formats) don't need characters
    print("  ❌ No matches found - this is non-fiction/special format")
    return False

# Test the problematic case
result = debug_should_generate_characters("History")
print(f"\nFinal result for 'History': {result}")
print(f"Expected: False")
print(f"Status: {'✅ CORRECT' if result == False else '❌ INCORRECT'}")
