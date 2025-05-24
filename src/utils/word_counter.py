"""
Utility functions for counting words in text.
"""
import re


def count_words(text: str) -> int:
    """
    Count the number of words in a text.
    
    Args:
        text: The text to count words in
        
    Returns:
        The number of words in the text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text.strip())
    
    # Split by whitespace and count
    words = text.split()
    
    return len(words)


def estimate_reading_time(word_count: int, words_per_minute: int = 250) -> int:
    """
    Estimate reading time in minutes based on word count.
    
    Args:
        word_count: Number of words
        words_per_minute: Average reading speed (default: 250 wpm)
        
    Returns:
        Estimated reading time in minutes
    """
    return round(word_count / words_per_minute)
