"""
Genre Recommendations System

This module provides genre-specific writer profile variants with different styles
(Master, Innovator, Storyteller, etc.) for enhanced author selection.

Each genre module provides specialized profile variants that offer different
approaches to writing within that genre, allowing users to select the style
that best matches their vision.
"""

from typing import Dict, Any, Optional, List
import importlib
from pathlib import Path

def get_available_genres() -> List[str]:
    """
    Get list of all genres with available recommendations.
    
    Returns:
        List of genre keys that have recommendation modules
    """
    genre_dir = Path(__file__).parent
    genre_files = [f.stem for f in genre_dir.glob("*.py") if f.stem != "__init__"]
    return sorted(genre_files)

def get_profile_by_genre_and_style(genre: str, style: str) -> Optional[Dict[str, Any]]:
    """
    Get a profile variant for a specific genre and style.
    
    Args:
        genre: Genre name (normalized)
        style: Style variant (Master, Innovator, Storyteller, etc.)
        
    Returns:
        Profile data or None if not found
    """
    try:
        # Normalize genre name
        genre_key = genre.lower().replace(" ", "_").replace("-", "_").replace("/", "_")
        
        # Import the genre module
        module_name = f"src.writer_profiles.genre_recommendations.{genre_key}"
        module = importlib.import_module(module_name)
        
        # Get profile by style
        if hasattr(module, 'get_profile_by_style'):
            return module.get_profile_by_style(style)
        
        return None
        
    except ImportError:
        return None
    except Exception:
        return None

def get_available_styles_for_genre(genre: str) -> List[str]:
    """
    Get available style variants for a specific genre.
    
    Args:
        genre: Genre name
        
    Returns:
        List of available style names
    """
    try:
        # Normalize genre name
        genre_key = genre.lower().replace(" ", "_").replace("-", "_").replace("/", "_")
        
        # Import the genre module
        module_name = f"src.writer_profiles.genre_recommendations.{genre_key}"
        module = importlib.import_module(module_name)
        
        # Get available styles
        if hasattr(module, 'get_available_styles'):
            return module.get_available_styles()
        
        # Default styles if not specified
        return ["Master", "Innovator", "Storyteller"]
        
    except ImportError:
        return []
    except Exception:
        return []

# Style definitions for consistency across genres
STYLE_DEFINITIONS = {
    "Master": {
        "description": "Established, authoritative approach with proven techniques",
        "characteristics": ["Traditional mastery", "Refined technique", "Proven methods"]
    },
    "Innovator": {
        "description": "Experimental, boundary-pushing approach with fresh perspectives",
        "characteristics": ["Creative experimentation", "New techniques", "Fresh voice"]
    },
    "Storyteller": {
        "description": "Narrative-focused approach emphasizing compelling stories",
        "characteristics": ["Strong narrative", "Engaging plots", "Reader connection"]
    },
    "Craftsperson": {
        "description": "Technical excellence with attention to literary craft",
        "characteristics": ["Technical precision", "Literary quality", "Artistic merit"]
    },
    "Commercial": {
        "description": "Market-aware approach optimized for broad appeal",
        "characteristics": ["Popular appeal", "Accessible style", "Commercial viability"]
    }
}
