"""
Poetry Collection Content Validator

This module provides validation functions to ensure poetry collections
contain authentic poetic content rather than narrative prose.
"""

import re
from typing import Dict, List, Tuple, Any


def validate_poetry_content(content: str, genre: str) -> Dict[str, Any]:
    """
    Validate that content is appropriate for poetry collections.

    Args:
        content: The generated content to validate
        genre: The genre (should contain "poetry")

    Returns:
        Dictionary with validation results and recommendations
    """
    if "poetry" not in genre.lower():
        return {"is_poetry_genre": False, "validation_skipped": True}

    # Analyze content structure
    lines = content.split('\n')
    total_lines = len(lines)

    if total_lines == 0:
        return {
            "is_valid": False,
            "error": "Empty content",
            "recommendations": ["Generate content for the poetry section"]
        }

    # Count line types
    short_lines = sum(1 for line in lines if 0 < len(line.strip()) < 50)
    medium_lines = sum(1 for line in lines if 50 <= len(line.strip()) < 100)
    long_lines = sum(1 for line in lines if len(line.strip()) >= 100)
    empty_lines = sum(1 for line in lines if len(line.strip()) == 0)

    # Calculate percentages
    short_line_percentage = (short_lines / total_lines) * 100 if total_lines > 0 else 0

    # Count stanza breaks
    stanza_breaks = content.count('\n\n')

    # Detect poem titles
    poem_titles = []
    for line in lines:
        stripped = line.strip()
        # Look for various title formats
        if (stripped.startswith('**') and stripped.endswith('**') and len(stripped) > 4) or \
           (stripped.startswith('*') and stripped.endswith('*') and len(stripped) > 2) or \
           (stripped.startswith('#') and len(stripped) > 2) or \
           (re.match(r'^[A-Z][^.!?]*$', stripped) and len(stripped.split()) <= 5):
            poem_titles.append(stripped)

    # Check for poetic vs narrative indicators
    content_lower = content.lower()

    # Positive indicators (poetry)
    poetry_indicators = [
        'stanza', 'verse', 'rhyme', 'meter', 'poem', 'imagery', 'metaphor',
        'alliteration', 'sonnet', 'haiku', 'free verse', 'rhythm', 'line break'
    ]

    # Negative indicators (narrative/story)
    narrative_indicators = [
        'character development', 'plot', 'protagonist', 'antagonist', 'scene',
        'dialogue', 'chapter', 'story arc', 'conflict resolution', 'narrative',
        'he said', 'she said', 'walked to', 'went to the'
    ]

    # Strong negative indicators (definitely narrative)
    strong_narrative_indicators = [
        'once upon a time', 'the end', 'character walked', 'plot twist',
        'story begins', 'main character', 'love interest', 'climax of the story',
        'he walked to', 'she went to', 'they traveled', 'the protagonist'
    ]

    poetry_score = sum(content_lower.count(indicator) for indicator in poetry_indicators)
    narrative_score = sum(content_lower.count(indicator) for indicator in narrative_indicators)
    strong_narrative_score = sum(content_lower.count(indicator) for indicator in strong_narrative_indicators)

    # Validation criteria
    validation_results = {
        "is_valid": True,
        "warnings": [],
        "recommendations": [],
        "metrics": {
            "total_lines": total_lines,
            "short_lines": short_lines,
            "short_line_percentage": short_line_percentage,
            "stanza_breaks": stanza_breaks,
            "poem_titles_count": len(poem_titles),
            "poetry_score": poetry_score,
            "narrative_score": narrative_score,
            "strong_narrative_score": strong_narrative_score
        },
        "detected_poems": poem_titles[:10]  # First 10 titles
    }

    # Check for critical failures (only if strong indicators are clearly narrative)
    if strong_narrative_score > 1:  # Require multiple strong indicators
        validation_results["is_valid"] = False
        validation_results["warnings"].append(
            f"CRITICAL: Found {strong_narrative_score} strong narrative indicators. "
            "This appears to be story content, not poetry."
        )
        validation_results["recommendations"].append(
            "Regenerate content with explicit poetry requirements"
        )
    elif strong_narrative_score == 1:
        validation_results["warnings"].append(
            f"Found 1 potential narrative indicator. Please verify content is poetic."
        )

    # Check for structural issues
    if short_line_percentage < 30:
        validation_results["warnings"].append(
            f"Low percentage of short lines ({short_line_percentage:.1f}%). "
            "Poetry typically has more short lines for rhythm and emphasis."
        )
        validation_results["recommendations"].append(
            "Use more line breaks and shorter lines for poetic effect"
        )

    if stanza_breaks < 2:
        validation_results["warnings"].append(
            f"Few stanza breaks ({stanza_breaks}). Poetry should have clear stanza structure."
        )
        validation_results["recommendations"].append(
            "Add stanza breaks (empty lines) to separate poem sections"
        )

    if len(poem_titles) < 2:
        validation_results["warnings"].append(
            f"Few poem titles detected ({len(poem_titles)}). "
            "A poetry section should contain multiple distinct poems."
        )
        validation_results["recommendations"].append(
            "Include multiple poems with clear titles in each section"
        )

    # Check content focus
    if narrative_score > poetry_score and narrative_score > 0:
        validation_results["warnings"].append(
            f"More narrative indicators ({narrative_score}) than poetry indicators ({poetry_score}). "
            "Content may be too narrative-focused."
        )
        validation_results["recommendations"].append(
            "Focus on poetic expression rather than storytelling"
        )

    # Set overall validity (more lenient for poetry collections)
    critical_warnings = [w for w in validation_results["warnings"] if "CRITICAL" in w]
    if len(critical_warnings) > 0 or strong_narrative_score > 1:
        validation_results["is_valid"] = False
    elif len(validation_results["warnings"]) > 4:  # Allow more warnings for poetry
        validation_results["is_valid"] = False

    return validation_results


def get_poetry_quality_score(content: str) -> float:
    """
    Calculate a quality score for poetry content (0.0 to 1.0).

    Args:
        content: The poetry content to score

    Returns:
        Quality score between 0.0 (poor) and 1.0 (excellent)
    """
    validation = validate_poetry_content(content, "Poetry Collection")

    if not validation.get("is_poetry_genre", True):
        return 0.5  # Neutral score for non-poetry

    metrics = validation["metrics"]
    score = 0.0

    # Short line percentage (0.3 weight)
    short_line_score = min(metrics["short_line_percentage"] / 60.0, 1.0)
    score += short_line_score * 0.3

    # Stanza structure (0.2 weight)
    stanza_score = min(metrics["stanza_breaks"] / 5.0, 1.0)
    score += stanza_score * 0.2

    # Multiple poems (0.2 weight)
    poem_score = min(metrics["poem_titles_count"] / 5.0, 1.0)
    score += poem_score * 0.2

    # Poetry vs narrative focus (0.2 weight)
    if metrics["poetry_score"] + metrics["narrative_score"] > 0:
        focus_score = metrics["poetry_score"] / (metrics["poetry_score"] + metrics["narrative_score"])
    else:
        focus_score = 0.5
    score += focus_score * 0.2

    # Penalty for strong narrative indicators (0.1 weight)
    narrative_penalty = min(metrics["strong_narrative_score"] / 3.0, 1.0)
    score += (1.0 - narrative_penalty) * 0.1

    return min(score, 1.0)


def suggest_poetry_improvements(content: str) -> List[str]:
    """
    Suggest specific improvements for poetry content.

    Args:
        content: The poetry content to analyze

    Returns:
        List of specific improvement suggestions
    """
    validation = validate_poetry_content(content, "Poetry Collection")
    suggestions = []

    # Add recommendations from validation
    suggestions.extend(validation.get("recommendations", []))

    # Add specific structural suggestions
    metrics = validation["metrics"]

    if metrics["short_line_percentage"] < 50:
        suggestions.append(
            "Break long lines into shorter ones for better poetic rhythm"
        )

    if metrics["stanza_breaks"] < 3:
        suggestions.append(
            "Add more stanza breaks to create clear poem structure"
        )

    if metrics["poem_titles_count"] < 3:
        suggestions.append(
            "Include 3-8 distinct poems per section with clear titles"
        )

    # Check for specific poetic elements
    content_lower = content.lower()

    if 'metaphor' not in content_lower and 'like' not in content_lower:
        suggestions.append(
            "Add metaphors and similes for richer poetic imagery"
        )

    if not any(word in content_lower for word in ['rhythm', 'rhyme', 'alliteration']):
        suggestions.append(
            "Consider adding sound devices like alliteration or rhyme"
        )

    if len(set(suggestions)) == 0:
        suggestions.append("Content appears to meet poetry quality standards")

    return list(set(suggestions))  # Remove duplicates


def is_valid_poetry_section(content: str, genre: str) -> bool:
    """
    Quick validation check for poetry sections.

    Args:
        content: Content to validate
        genre: Genre name

    Returns:
        True if content appears to be valid poetry
    """
    if "poetry" not in genre.lower():
        return True  # Not a poetry genre, skip validation

    validation = validate_poetry_content(content, genre)
    return validation["is_valid"]
