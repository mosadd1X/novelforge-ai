"""
Quick test to verify the History genre fix.
"""

def should_generate_characters(genre: str) -> bool:
    """Copy of the fixed function for testing."""
    fiction_genres = [
        "literary fiction", "commercial fiction", "mystery", "mystery thriller",
        "thriller", "romance", "fantasy", "epic fantasy", "science fiction",
        "historical fiction", "horror", "young adult", "middle grade",
        "children's chapter books", "speculative fiction", "alternate history",
        "contemporary fiction", "paranormal romance", "urban fantasy", "dystopian",
        "test"
    ]

    genre_normalized = genre.lower().strip()

    # Check if it's a fiction genre that needs characters
    # First check for exact matches
    for fiction_genre in fiction_genres:
        if fiction_genre.lower() == genre_normalized:
            return True

    # Then check for partial matches, but be very careful
    for fiction_genre in fiction_genres:
        # Only allow partial matches if the genre is clearly contained
        if genre_normalized in fiction_genre.lower() and len(genre_normalized) > 3:
            # Avoid false positives like "history" matching fiction genres
            if genre_normalized == "history" and ("historical" in fiction_genre.lower() or "alternate" in fiction_genre.lower()):
                continue
            if genre_normalized == "science" and "science fiction" in fiction_genre.lower():
                continue
            return True

    # All other genres (non-fiction and special formats) don't need characters
    return False

# Test the problematic cases
test_cases = [
    ("History", False),
    ("Historical Fiction", True),
    ("Science Fiction", True),
    ("Fantasy", True),
    ("Self Help", False),
    ("Biography", False),
    ("Poetry Collection", False)
]

print("🧪 Testing History Genre Fix")
print("=" * 40)

all_passed = True
for genre, expected in test_cases:
    result = should_generate_characters(genre)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    if result != expected:
        all_passed = False

    char_action = "Generate" if result else "Skip"
    print(f"{status} {genre}: {char_action} characters")

print("\n" + "=" * 40)
if all_passed:
    print("🎉 ALL TESTS PASSED! History fix is working correctly.")
else:
    print("❌ Some tests failed. Review needed.")
