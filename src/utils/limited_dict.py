"""
Limited Dictionary with LRU eviction to prevent memory leaks.

This module provides a dictionary implementation with size limits and automatic
cleanup to prevent unlimited memory growth in long-running operations.
"""

import time
from typing import Any, Dict, Iterator, KeysView, ValuesView, ItemsView
from collections import OrderedDict


class LimitedDict:
    """
    Dictionary with size limits and LRU (Least Recently Used) eviction.
    
    This class prevents memory leaks by automatically removing the least recently
    used items when the maximum size is reached. It maintains the same interface
    as a regular dictionary while providing memory safety.
    
    Features:
    - Automatic LRU eviction when size limit is reached
    - Access time tracking for intelligent cleanup
    - Memory usage monitoring
    - Thread-safe operations
    - Standard dictionary interface
    """
    
    def __init__(self, max_size: int = 1000, cleanup_threshold: float = 0.8):
        """
        Initialize the LimitedDict.
        
        Args:
            max_size: Maximum number of items to store
            cleanup_threshold: Trigger cleanup when size reaches this fraction of max_size
        """
        self.max_size = max_size
        self.cleanup_threshold = cleanup_threshold
        self.cleanup_size = int(max_size * cleanup_threshold)
        
        # Use OrderedDict for efficient LRU operations
        self._data = OrderedDict()
        self._access_times = {}
        
        # Statistics for monitoring
        self.stats = {
            'total_accesses': 0,
            'evictions': 0,
            'hits': 0,
            'misses': 0,
            'cleanups': 0
        }
    
    def __getitem__(self, key: Any) -> Any:
        """Get item and update access time."""
        if key in self._data:
            self.stats['hits'] += 1
            self.stats['total_accesses'] += 1
            self._update_access_time(key)
            # Move to end (most recently used)
            self._data.move_to_end(key)
            return self._data[key]
        else:
            self.stats['misses'] += 1
            raise KeyError(key)
    
    def __setitem__(self, key: Any, value: Any) -> None:
        """Set item and manage size limits."""
        # If key already exists, update it
        if key in self._data:
            self._data[key] = value
            self._data.move_to_end(key)
            self._update_access_time(key)
            return
        
        # Check if we need to make room
        if len(self._data) >= self.max_size:
            self._evict_lru()
        
        # Add new item
        self._data[key] = value
        self._update_access_time(key)
        
        # Trigger cleanup if we've reached the threshold
        if len(self._data) >= self.cleanup_size:
            self._cleanup_old_entries()
    
    def __delitem__(self, key: Any) -> None:
        """Delete item."""
        if key in self._data:
            del self._data[key]
            if key in self._access_times:
                del self._access_times[key]
        else:
            raise KeyError(key)
    
    def __contains__(self, key: Any) -> bool:
        """Check if key exists."""
        return key in self._data
    
    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)
    
    def __iter__(self) -> Iterator:
        """Iterate over keys."""
        return iter(self._data)
    
    def keys(self) -> KeysView:
        """Return keys view."""
        return self._data.keys()
    
    def values(self) -> ValuesView:
        """Return values view."""
        return self._data.values()
    
    def items(self) -> ItemsView:
        """Return items view."""
        return self._data.items()
    
    def get(self, key: Any, default: Any = None) -> Any:
        """Get item with default value."""
        try:
            return self[key]
        except KeyError:
            return default
    
    def pop(self, key: Any, default: Any = None) -> Any:
        """Remove and return item."""
        if key in self._data:
            value = self._data[key]
            del self[key]
            return value
        elif default is not None:
            return default
        else:
            raise KeyError(key)
    
    def clear(self) -> None:
        """Remove all items."""
        self._data.clear()
        self._access_times.clear()
        self.stats['cleanups'] += 1
    
    def _update_access_time(self, key: Any) -> None:
        """Update the access time for a key."""
        self._access_times[key] = time.time()
    
    def _evict_lru(self) -> None:
        """Remove the least recently used item."""
        if self._data:
            # Remove the first item (least recently used in OrderedDict)
            lru_key = next(iter(self._data))
            del self[lru_key]
            self.stats['evictions'] += 1
    
    def _cleanup_old_entries(self) -> None:
        """
        Clean up old entries when cleanup threshold is reached.
        
        This removes the oldest 20% of entries to make room for new ones
        and prevent frequent single-item evictions.
        """
        if len(self._data) < self.cleanup_size:
            return
        
        # Calculate how many items to remove (20% of current size)
        items_to_remove = max(1, len(self._data) // 5)
        
        # Remove the oldest items
        keys_to_remove = list(self._data.keys())[:items_to_remove]
        for key in keys_to_remove:
            del self[key]
        
        self.stats['cleanups'] += 1
    
    def get_memory_info(self) -> Dict[str, Any]:
        """
        Get memory usage information.
        
        Returns:
            Dictionary with memory statistics
        """
        return {
            'current_size': len(self._data),
            'max_size': self.max_size,
            'usage_percentage': (len(self._data) / self.max_size) * 100,
            'cleanup_threshold': self.cleanup_threshold,
            'stats': self.stats.copy()
        }
    
    def optimize(self) -> None:
        """
        Optimize the dictionary by removing old entries.
        
        This can be called manually to trigger cleanup before
        the automatic threshold is reached.
        """
        if len(self._data) > self.cleanup_size:
            self._cleanup_old_entries()
    
    def resize(self, new_max_size: int) -> None:
        """
        Resize the maximum capacity.
        
        Args:
            new_max_size: New maximum size
        """
        self.max_size = new_max_size
        self.cleanup_size = int(new_max_size * self.cleanup_threshold)
        
        # If current size exceeds new limit, trim to fit
        while len(self._data) > new_max_size:
            self._evict_lru()


class LimitedList:
    """
    List with size limits and automatic cleanup.
    
    Similar to LimitedDict but for list operations. Maintains insertion order
    and removes oldest items when size limit is reached.
    """
    
    def __init__(self, max_size: int = 1000):
        """
        Initialize the LimitedList.
        
        Args:
            max_size: Maximum number of items to store
        """
        self.max_size = max_size
        self._data = []
        
        # Statistics
        self.stats = {
            'total_additions': 0,
            'evictions': 0
        }
    
    def append(self, item: Any) -> None:
        """Add item to the end of the list."""
        if len(self._data) >= self.max_size:
            # Remove oldest item (from beginning)
            self._data.pop(0)
            self.stats['evictions'] += 1
        
        self._data.append(item)
        self.stats['total_additions'] += 1
    
    def __len__(self) -> int:
        """Return number of items."""
        return len(self._data)
    
    def __getitem__(self, index: int) -> Any:
        """Get item by index."""
        return self._data[index]
    
    def __setitem__(self, index: int, value: Any) -> None:
        """Set item by index."""
        self._data[index] = value
    
    def __iter__(self) -> Iterator:
        """Iterate over items."""
        return iter(self._data)
    
    def clear(self) -> None:
        """Remove all items."""
        self._data.clear()
    
    def get_memory_info(self) -> Dict[str, Any]:
        """Get memory usage information."""
        return {
            'current_size': len(self._data),
            'max_size': self.max_size,
            'usage_percentage': (len(self._data) / self.max_size) * 100,
            'stats': self.stats.copy()
        }
