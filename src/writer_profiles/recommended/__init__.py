"""
Recommended Writer Profiles Collections System

This module provides curated collections of writer profiles organized by different
criteria such as commercial success, literary excellence, genre mastery, etc.

Each collection intelligently categorizes the existing master profiles to help
users find the most suitable authors for their specific goals and preferences.
"""

from typing import Dict, Any, List, Optional
import json
from pathlib import Path

def get_available_collections() -> List[str]:
    """
    Get list of all available profile collections.
    
    Returns:
        List of collection names
    """
    collections_dir = Path(__file__).parent
    collection_files = [f.stem for f in collections_dir.glob("*.json") if f.stem != "__init__"]
    return sorted(collection_files)

def load_collection(collection_name: str) -> Optional[Dict[str, Any]]:
    """
    Load a specific profile collection.
    
    Args:
        collection_name: Name of the collection to load
        
    Returns:
        Collection data or None if not found
    """
    try:
        collections_dir = Path(__file__).parent
        collection_path = collections_dir / f"{collection_name}.json"
        
        if not collection_path.exists():
            return None
            
        with open(collection_path, 'r', encoding='utf-8') as f:
            return json.load(f)
            
    except Exception:
        return None

def get_profiles_from_collection(collection_name: str) -> List[Dict[str, Any]]:
    """
    Get all profiles from a specific collection.
    
    Args:
        collection_name: Name of the collection
        
    Returns:
        List of profile data from the collection
    """
    collection = load_collection(collection_name)
    if not collection:
        return []
        
    return collection.get("profiles", [])

def get_collection_metadata(collection_name: str) -> Optional[Dict[str, Any]]:
    """
    Get metadata for a specific collection.
    
    Args:
        collection_name: Name of the collection
        
    Returns:
        Collection metadata or None if not found
    """
    collection = load_collection(collection_name)
    if not collection:
        return None
        
    return {
        "name": collection.get("collection_name", collection_name),
        "description": collection.get("description", ""),
        "category": collection.get("category", "General"),
        "profile_count": len(collection.get("profiles", [])),
        "target_audience": collection.get("target_audience", ""),
        "use_cases": collection.get("use_cases", []),
        "created_date": collection.get("created_date", ""),
        "last_updated": collection.get("last_updated", "")
    }

def search_collections_by_genre(genre: str) -> List[Dict[str, Any]]:
    """
    Find collections that contain profiles suitable for a specific genre.
    
    Args:
        genre: Genre to search for
        
    Returns:
        List of matching collections with their metadata
    """
    matching_collections = []
    
    for collection_name in get_available_collections():
        collection = load_collection(collection_name)
        if not collection:
            continue
            
        # Check if any profiles in the collection support this genre
        for profile in collection.get("profiles", []):
            profile_genres = profile.get("genres", [])
            if genre.lower() in [g.lower() for g in profile_genres]:
                metadata = get_collection_metadata(collection_name)
                if metadata:
                    matching_collections.append({
                        "collection_name": collection_name,
                        "metadata": metadata,
                        "matching_profiles": [p for p in collection.get("profiles", []) 
                                            if genre.lower() in [g.lower() for g in p.get("genres", [])]]
                    })
                break
                
    return matching_collections

def get_recommended_profile_for_goal(goal: str, genre: str = None) -> Optional[Dict[str, Any]]:
    """
    Get a recommended profile based on user goal and optional genre.
    
    Args:
        goal: User's goal (e.g., "commercial_success", "literary_excellence")
        genre: Optional genre filter
        
    Returns:
        Recommended profile or None if not found
    """
    # Map goals to collection names
    goal_to_collection = {
        "commercial_success": "commercial_success",
        "bestseller": "commercial_success",
        "popular": "commercial_success",
        "literary_excellence": "literary_masters",
        "literary": "literary_masters",
        "artistic": "literary_masters",
        "genre_mastery": "genre_specialists",
        "specialist": "genre_specialists",
        "debut": "debut_authors",
        "first_book": "debut_authors",
        "beginner": "debut_authors",
        "experimental": "innovative_voices",
        "innovative": "innovative_voices",
        "fresh": "innovative_voices"
    }
    
    collection_name = goal_to_collection.get(goal.lower())
    if not collection_name:
        return None
        
    profiles = get_profiles_from_collection(collection_name)
    if not profiles:
        return None
        
    # Filter by genre if specified
    if genre:
        genre_profiles = [p for p in profiles 
                         if genre.lower() in [g.lower() for g in p.get("genres", [])]]
        if genre_profiles:
            profiles = genre_profiles
            
    # Return the first (highest priority) profile
    return profiles[0] if profiles else None

# Collection categories for organization
COLLECTION_CATEGORIES = {
    "Success-Oriented": [
        "commercial_success",
        "bestseller_authors", 
        "award_winners"
    ],
    "Literary-Focused": [
        "literary_masters",
        "experimental_authors",
        "innovative_voices"
    ],
    "Genre-Specific": [
        "genre_specialists",
        "fiction_masters",
        "non_fiction_experts"
    ],
    "Experience-Based": [
        "debut_authors",
        "established_authors",
        "veteran_writers"
    ],
    "Cultural-Diverse": [
        "international_voices",
        "cultural_authenticity",
        "diverse_perspectives"
    ]
}
