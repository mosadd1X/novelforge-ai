"""
Responsive Terminal Separator Utility for NovelForge AI

This module provides dynamic, width-responsive separators that automatically
adjust to the current terminal width. Replaces static equal sign separators
with intelligent, responsive alternatives.
"""

import os
import shutil
from typing import Optional, Union


class ResponsiveSeparator:
    """
    A utility class for creating responsive terminal separators that automatically
    adjust to the current terminal width.
    """
    
    def __init__(self, min_width: int = 40, max_width: int = 120, padding: int = 0):
        """
        Initialize the responsive separator.
        
        Args:
            min_width: Minimum separator width (default: 40)
            max_width: Maximum separator width (default: 120) 
            padding: Padding to subtract from terminal width (default: 0)
        """
        self.min_width = min_width
        self.max_width = max_width
        self.padding = padding
    
    def get_terminal_width(self) -> int:
        """
        Get the current terminal width with fallback handling.
        
        Returns:
            Current terminal width or fallback value
        """
        try:
            # Try to get terminal size using shutil (most reliable)
            terminal_size = shutil.get_terminal_size()
            width = terminal_size.columns
        except (OSError, AttributeError):
            try:
                # Fallback to os.get_terminal_size()
                terminal_size = os.get_terminal_size()
                width = terminal_size.columns
            except (OSError, AttributeError):
                # Final fallback to environment variable or default
                width = int(os.environ.get('COLUMNS', 80))
        
        # Apply constraints and padding
        width = max(self.min_width, min(self.max_width, width - self.padding))
        return width
    
    def create_separator(self, char: str = "=", style: str = "full") -> str:
        """
        Create a responsive separator line.
        
        Args:
            char: Character to use for separator (default: "=")
            style: Separator style - "full", "centered", "padded" (default: "full")
            
        Returns:
            Responsive separator string
        """
        width = self.get_terminal_width()
        
        if style == "full":
            return char * width
        elif style == "centered":
            # Create centered separator with spaces on sides
            separator_width = max(20, width - 20)  # Leave 10 chars on each side
            padding_width = (width - separator_width) // 2
            return " " * padding_width + char * separator_width + " " * padding_width
        elif style == "padded":
            # Create separator with 4 spaces on each side
            separator_width = max(10, width - 8)
            return "    " + char * separator_width + "    "
        else:
            return char * width
    
    def create_title_separator(self, title: str, char: str = "=", 
                             title_padding: int = 2) -> str:
        """
        Create a separator with a centered title.
        
        Args:
            title: Title text to center in separator
            char: Character to use for separator (default: "=")
            title_padding: Spaces around title (default: 2)
            
        Returns:
            Separator with centered title
        """
        width = self.get_terminal_width()
        title_with_padding = f"{' ' * title_padding}{title.upper()}{' ' * title_padding}"
        title_length = len(title_with_padding)
        
        if title_length >= width - 4:
            # Title too long, just return title
            return title_with_padding
        
        # Calculate separator lengths on each side
        remaining_width = width - title_length
        left_width = remaining_width // 2
        right_width = remaining_width - left_width
        
        return char * left_width + title_with_padding + char * right_width
    
    def create_section_separator(self, section_name: str = "", 
                               char: str = "-", style: str = "simple") -> str:
        """
        Create a section separator, optionally with section name.
        
        Args:
            section_name: Optional section name
            char: Character to use (default: "-")
            style: Style - "simple", "boxed", "spaced" (default: "simple")
            
        Returns:
            Section separator string
        """
        width = self.get_terminal_width()
        
        if not section_name:
            if style == "simple":
                return char * width
            elif style == "spaced":
                return char * (width // 2)
            else:
                return char * width
        
        # With section name
        if style == "simple":
            return f"{char * 4} {section_name} {char * (width - len(section_name) - 6)}"
        elif style == "boxed":
            padding = 2
            section_with_padding = f"{' ' * padding}{section_name}{' ' * padding}"
            remaining = width - len(section_with_padding)
            left_chars = remaining // 2
            right_chars = remaining - left_chars
            return char * left_chars + section_with_padding + char * right_chars
        elif style == "spaced":
            return f"\n{char * 4} {section_name}\n"
        else:
            return f"{char * 4} {section_name} {char * (width - len(section_name) - 6)}"


# Global instance for easy access
_responsive_separator = ResponsiveSeparator()


def separator(char: str = "=", style: str = "full") -> str:
    """
    Quick function to create a responsive separator.
    
    Args:
        char: Character to use for separator (default: "=")
        style: Separator style (default: "full")
        
    Returns:
        Responsive separator string
    """
    return _responsive_separator.create_separator(char, style)


def title_separator(title: str, char: str = "=") -> str:
    """
    Quick function to create a title separator.
    
    Args:
        title: Title text
        char: Character to use (default: "=")
        
    Returns:
        Separator with centered title
    """
    return _responsive_separator.create_title_separator(title, char)


def section_separator(section_name: str = "", char: str = "-", style: str = "simple") -> str:
    """
    Quick function to create a section separator.
    
    Args:
        section_name: Optional section name
        char: Character to use (default: "-")
        style: Style (default: "simple")
        
    Returns:
        Section separator string
    """
    return _responsive_separator.create_section_separator(section_name, char, style)


def get_terminal_width() -> int:
    """
    Quick function to get current terminal width.
    
    Returns:
        Current terminal width
    """
    return _responsive_separator.get_terminal_width()


# Convenience functions for common separators
def equals_separator() -> str:
    """Create a full-width equals separator."""
    return separator("=", "full")


def dash_separator() -> str:
    """Create a full-width dash separator."""
    return separator("-", "full")


def star_separator() -> str:
    """Create a full-width star separator."""
    return separator("*", "full")


def double_separator() -> str:
    """Create a double-line separator."""
    return separator("=", "full") + "\n" + separator("=", "full")


# Test function to demonstrate responsive behavior
def test_responsive_separators():
    """Test function to demonstrate responsive separator behavior."""
    print("Testing Responsive Separators")
    print(f"Terminal width: {get_terminal_width()}")
    print()
    
    print("Full equals separator:")
    print(equals_separator())
    print()
    
    print("Title separator:")
    print(title_separator("Test Results"))
    print()
    
    print("Section separator:")
    print(section_separator("Configuration", "-", "simple"))
    print()
    
    print("Centered separator:")
    print(separator("=", "centered"))
    print()
    
    print("Padded separator:")
    print(separator("-", "padded"))
    print()


if __name__ == "__main__":
    test_responsive_separators()
