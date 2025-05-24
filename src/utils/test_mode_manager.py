#!/usr/bin/env python3
"""
Test Mode Manager for Ebook Generator

This module manages test mode configuration and settings to enable
fast testing while maintaining production code paths.

Key Features:
- Global test mode state management
- Test-specific configuration overrides
- Seamless switching between test and production modes
- Environment variable integration
"""

import os
import json
from typing import Dict, Any, Optional
from pathlib import Path


class TestModeManager:
    """
    Manages test mode configuration and state.
    
    This class provides centralized management of test mode settings,
    allowing the system to switch between fast testing and production
    modes while maintaining the same code paths.
    """
    
    _instance = None
    _test_mode_active = False
    _test_mode_level = None
    _test_overrides = {}
    
    def __new__(cls):
        """Singleton pattern to ensure consistent state across the application."""
        if cls._instance is None:
            cls._instance = super(TestModeManager, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        """Initialize the test mode manager."""
        if not hasattr(self, '_initialized'):
            self._initialized = True
            self._load_test_configurations()
    
    def enable_test_mode(self, level: str = "standard") -> None:
        """
        Enable test mode with specified level.
        
        Args:
            level: Test mode level ("minimal", "standard", "comprehensive")
        """
        TestModeManager._test_mode_active = True
        TestModeManager._test_mode_level = level
        TestModeManager._test_overrides = self._get_test_overrides(level)
        
        # Set environment variable for other components
        os.environ["EBOOK_GENERATOR_TEST_MODE"] = level
    
    def disable_test_mode(self) -> None:
        """Disable test mode and restore production settings."""
        TestModeManager._test_mode_active = False
        TestModeManager._test_mode_level = None
        TestModeManager._test_overrides = {}
        
        # Remove environment variable
        if "EBOOK_GENERATOR_TEST_MODE" in os.environ:
            del os.environ["EBOOK_GENERATOR_TEST_MODE"]
    
    @classmethod
    def is_test_mode_active(cls) -> bool:
        """Check if test mode is currently active."""
        return cls._test_mode_active or os.getenv("EBOOK_GENERATOR_TEST_MODE") is not None
    
    @classmethod
    def get_test_mode_level(cls) -> Optional[str]:
        """Get the current test mode level."""
        return cls._test_mode_level or os.getenv("EBOOK_GENERATOR_TEST_MODE")
    
    @classmethod
    def get_test_override(cls, key: str, default: Any = None) -> Any:
        """
        Get a test mode override value.
        
        Args:
            key: Configuration key to override
            default: Default value if no override exists
            
        Returns:
            Override value or default
        """
        return cls._test_overrides.get(key, default)
    
    @classmethod
    def apply_test_overrides(cls, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply test mode overrides to a configuration dictionary.
        
        Args:
            config: Original configuration
            
        Returns:
            Configuration with test overrides applied
        """
        if not cls.is_test_mode_active():
            return config
        
        # Create a copy to avoid modifying the original
        test_config = config.copy()
        
        # Apply overrides
        for key, value in cls._test_overrides.items():
            if key in test_config:
                test_config[key] = value
        
        return test_config
    
    def _load_test_configurations(self) -> None:
        """Load test configurations from file or set defaults."""
        self.test_configs = {
            "minimal": {
                "chapter_count": 2,
                "target_word_count": 2000,
                "chapter_length": 1000,
                "min_chapter_length": 800,
                "max_tokens": 4000,
                "temperature": 0.5,
                "skip_enhancement": True,
                "skip_character_generation": True,
                "minimal_epub_formatting": True
            },
            "standard": {
                "chapter_count": 4,
                "target_word_count": 6000,
                "chapter_length": 1500,
                "min_chapter_length": 1200,
                "max_tokens": 8000,
                "temperature": 0.7,
                "skip_enhancement": False,
                "skip_character_generation": False,
                "minimal_epub_formatting": False
            },
            "comprehensive": {
                "chapter_count": 6,
                "target_word_count": 9000,
                "chapter_length": 1500,
                "min_chapter_length": 1200,
                "max_tokens": 12000,
                "temperature": 0.7,
                "skip_enhancement": False,
                "skip_character_generation": False,
                "minimal_epub_formatting": False
            }
        }
    
    def _get_test_overrides(self, level: str) -> Dict[str, Any]:
        """Get test overrides for the specified level."""
        return self.test_configs.get(level, self.test_configs["standard"])
    
    def get_test_genre_defaults(self, genre: str) -> Dict[str, Any]:
        """
        Get test-optimized genre defaults.
        
        Args:
            genre: Genre name
            
        Returns:
            Test-optimized genre configuration
        """
        if not self.is_test_mode_active():
            return {}
        
        level = self.get_test_mode_level()
        base_overrides = self._get_test_overrides(level)
        
        # Genre-specific test optimizations
        genre_optimizations = {
            "test": {
                "chapter_count": 2,
                "target_word_count": 2000,
                "chapter_length": 1000,
                "min_chapter_length": 800
            },
            "Literary Fiction": {
                "chapter_count": base_overrides.get("chapter_count", 4),
                "target_word_count": base_overrides.get("target_word_count", 6000),
                "chapter_length": base_overrides.get("chapter_length", 1500)
            },
            "Contemporary Romance": {
                "chapter_count": base_overrides.get("chapter_count", 3),
                "target_word_count": base_overrides.get("target_word_count", 4500),
                "chapter_length": base_overrides.get("chapter_length", 1500)
            }
        }
        
        return genre_optimizations.get(genre, base_overrides)


# Global instance for easy access
test_mode_manager = TestModeManager()


def is_test_mode() -> bool:
    """Convenience function to check if test mode is active."""
    return TestModeManager.is_test_mode_active()


def get_test_mode_level() -> Optional[str]:
    """Convenience function to get test mode level."""
    return TestModeManager.get_test_mode_level()


def apply_test_mode_optimizations(config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply test mode optimizations to configuration.
    
    Args:
        config: Original configuration
        
    Returns:
        Optimized configuration for testing
    """
    if not is_test_mode():
        return config
    
    return TestModeManager.apply_test_overrides(config)


def get_test_api_settings() -> Dict[str, Any]:
    """Get API settings optimized for testing."""
    if not is_test_mode():
        return {}
    
    level = get_test_mode_level()
    
    settings = {
        "minimal": {
            "max_tokens": 4000,
            "temperature": 0.5,
            "timeout": 30,
            "max_retries": 2
        },
        "standard": {
            "max_tokens": 8000,
            "temperature": 0.7,
            "timeout": 60,
            "max_retries": 3
        },
        "comprehensive": {
            "max_tokens": 12000,
            "temperature": 0.7,
            "timeout": 90,
            "max_retries": 3
        }
    }
    
    return settings.get(level, settings["standard"])


def should_skip_enhancement() -> bool:
    """Check if content enhancement should be skipped in test mode."""
    if not is_test_mode():
        return False
    
    return TestModeManager.get_test_override("skip_enhancement", False)


def should_skip_character_generation() -> bool:
    """Check if character generation should be skipped in test mode."""
    if not is_test_mode():
        return False
    
    return TestModeManager.get_test_override("skip_character_generation", False)


def should_use_minimal_epub_formatting() -> bool:
    """Check if minimal EPUB formatting should be used in test mode."""
    if not is_test_mode():
        return False
    
    return TestModeManager.get_test_override("minimal_epub_formatting", False)


def get_test_output_directory() -> str:
    """Get the test output directory path."""
    return "output/fast_tests"


def log_test_mode_status() -> None:
    """Log current test mode status for debugging."""
    if is_test_mode():
        level = get_test_mode_level()
        print(f"Test mode active: {level}")
        print(f"Test overrides: {TestModeManager._test_overrides}")
    else:
        print("Test mode inactive - using production settings")
