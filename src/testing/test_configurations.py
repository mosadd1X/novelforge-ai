#!/usr/bin/env python3
"""
Test Configurations for Fast Testing System

This module provides centralized configuration management for the fast
testing system, including predefined test scenarios and optimized settings.

Key Features:
- Predefined test configurations for different scenarios
- Optimized settings for fast execution
- Realistic but minimal content parameters
- Easy configuration management
"""

from typing import Dict, Any, List
from dataclasses import dataclass


@dataclass
class TestScenario:
    """Configuration for a specific test scenario."""
    name: str
    description: str
    config: Dict[str, Any]
    expected_duration: int  # Expected duration in seconds
    complexity_level: str  # "minimal", "standard", "complex"


class TestConfigurations:
    """
    Centralized management of test configurations.
    
    This class provides predefined configurations for various testing
    scenarios, optimized for speed while maintaining realistic content.
    """
    
    def __init__(self):
        """Initialize test configurations."""
        self._load_configurations()
    
    def _load_configurations(self) -> None:
        """Load all test configurations."""
        self.scenarios = {
            "minimal_book": TestScenario(
                name="Minimal Book Test",
                description="Ultra-fast book generation with minimal content",
                config=self._get_minimal_book_config(),
                expected_duration=60,  # 1 minute
                complexity_level="minimal"
            ),
            "standard_book": TestScenario(
                name="Standard Book Test", 
                description="Standard book generation with moderate content",
                config=self._get_standard_book_config(),
                expected_duration=180,  # 3 minutes
                complexity_level="standard"
            ),
            "complex_book": TestScenario(
                name="Complex Book Test",
                description="Complex genre book with advanced features",
                config=self._get_complex_book_config(),
                expected_duration=300,  # 5 minutes
                complexity_level="complex"
            ),
            "minimal_series": TestScenario(
                name="Minimal Series Test",
                description="Fast series generation with 2 minimal books",
                config=self._get_minimal_series_config(),
                expected_duration=240,  # 4 minutes
                complexity_level="standard"
            ),
            "performance_benchmark": TestScenario(
                name="Performance Benchmark",
                description="Performance testing and timing benchmarks",
                config=self._get_benchmark_config(),
                expected_duration=30,  # 30 seconds
                complexity_level="minimal"
            )
        }
    
    def get_scenario(self, scenario_name: str) -> TestScenario:
        """Get a specific test scenario."""
        return self.scenarios.get(scenario_name)
    
    def get_all_scenarios(self) -> Dict[str, TestScenario]:
        """Get all available test scenarios."""
        return self.scenarios
    
    def get_minimal_book_config(self) -> Dict[str, Any]:
        """Get minimal book configuration for ultra-fast testing."""
        return self._get_minimal_book_config()
    
    def get_standard_book_config(self) -> Dict[str, Any]:
        """Get standard book configuration for balanced testing."""
        return self._get_standard_book_config()
    
    def get_complex_book_config(self) -> Dict[str, Any]:
        """Get complex book configuration for comprehensive testing."""
        return self._get_complex_book_config()
    
    def _get_minimal_book_config(self) -> Dict[str, Any]:
        """Minimal configuration for ultra-fast testing."""
        return {
            "title": "Test Novel - Minimal",
            "author": "Test Author",
            "description": "A minimal test novel for ultra-fast testing.",
            "genre": "test",
            "target_audience": "Adult (18+)",
            "generation_options": {
                "chapter_count": 2,
                "target_word_count": 2000,
                "chapter_length": 1000,
                "min_chapter_length": 800,
                "writing_style": "Simple and direct",
                "themes": ["Testing", "Speed"],
                "temperature": 0.5,
                "max_tokens": 4000,
                "skip_enhancement": True,
                "skip_character_generation": True,
                "minimal_formatting": True
            },
            "test_settings": {
                "use_mock_api": False,
                "fast_mode": True,
                "skip_validation": True,
                "minimal_logging": True
            }
        }
    
    def _get_standard_book_config(self) -> Dict[str, Any]:
        """Standard configuration for balanced testing."""
        return {
            "title": "Test Novel - Standard",
            "author": "Test Author",
            "description": "A standard test novel with moderate complexity.",
            "genre": "Literary Fiction",
            "target_audience": "Adult (18+)",
            "generation_options": {
                "chapter_count": 4,
                "target_word_count": 6000,
                "chapter_length": 1500,
                "min_chapter_length": 1200,
                "writing_style": "Descriptive and detailed",
                "themes": ["Identity", "Relationships"],
                "temperature": 0.7,
                "max_tokens": 8000,
                "skip_enhancement": False,
                "skip_character_generation": False,
                "minimal_formatting": False
            },
            "test_settings": {
                "use_mock_api": False,
                "fast_mode": True,
                "skip_validation": False,
                "minimal_logging": False
            }
        }
    
    def _get_complex_book_config(self) -> Dict[str, Any]:
        """Complex configuration for comprehensive testing."""
        return {
            "title": "Test Novel - Complex",
            "author": "Test Author",
            "description": "A complex test novel with advanced genre features.",
            "genre": "Contemporary Romance",
            "target_audience": "Adult (18+)",
            "generation_options": {
                "chapter_count": 3,
                "target_word_count": 4500,
                "chapter_length": 1500,
                "min_chapter_length": 1200,
                "writing_style": "Emotional and descriptive",
                "themes": ["Love", "Growth", "Communication"],
                "temperature": 0.7,
                "max_tokens": 10000,
                "skip_enhancement": False,
                "skip_character_generation": False,
                "minimal_formatting": False,
                "include_front_matter": True,
                "include_back_matter": True
            },
            "test_settings": {
                "use_mock_api": False,
                "fast_mode": False,
                "skip_validation": False,
                "minimal_logging": False,
                "test_genre_formatting": True
            }
        }
    
    def _get_minimal_series_config(self) -> Dict[str, Any]:
        """Minimal series configuration for fast testing."""
        return {
            "series_title": "Test Series - Fast",
            "series_description": "A minimal test series for fast testing.",
            "genre": "test",
            "target_audience": "Adult (18+)",
            "planned_books": 2,
            "author": "Test Author",
            "generation_options": {
                "chapter_count": 2,
                "target_word_count": 2000,
                "chapter_length": 1000,
                "min_chapter_length": 800,
                "writing_style": "Simple and direct",
                "themes": ["Testing", "Series"],
                "temperature": 0.5,
                "max_tokens": 4000,
                "skip_enhancement": True,
                "skip_character_generation": True,
                "minimal_formatting": True
            },
            "test_settings": {
                "use_mock_api": False,
                "fast_mode": True,
                "skip_validation": True,
                "minimal_logging": True,
                "auto_cover_generation": True
            }
        }
    
    def _get_benchmark_config(self) -> Dict[str, Any]:
        """Configuration for performance benchmarking."""
        return {
            "benchmark_tests": [
                {
                    "name": "Generator Initialization",
                    "description": "Time to initialize novel generator",
                    "target_time": 1.0
                },
                {
                    "name": "Configuration Loading",
                    "description": "Time to load and apply configuration",
                    "target_time": 0.5
                },
                {
                    "name": "Output Directory Creation",
                    "description": "Time to create output directories",
                    "target_time": 0.1
                },
                {
                    "name": "EPUB Formatter Initialization",
                    "description": "Time to initialize EPUB formatter",
                    "target_time": 0.5
                }
            ],
            "performance_targets": {
                "total_initialization_time": 2.0,
                "memory_usage_limit_mb": 100,
                "api_calls_per_minute": 60
            }
        }
    
    def get_test_genre_overrides(self) -> Dict[str, Dict[str, Any]]:
        """Get genre-specific test overrides."""
        return {
            "test": {
                "chapter_count": 2,
                "target_word_count": 2000,
                "chapter_length": 1000,
                "min_chapter_length": 800,
                "skip_enhancement": True
            },
            "Literary Fiction": {
                "chapter_count": 4,
                "target_word_count": 6000,
                "chapter_length": 1500,
                "min_chapter_length": 1200
            },
            "Contemporary Romance": {
                "chapter_count": 3,
                "target_word_count": 4500,
                "chapter_length": 1500,
                "min_chapter_length": 1200
            },
            "Fantasy": {
                "chapter_count": 4,
                "target_word_count": 6000,
                "chapter_length": 1500,
                "min_chapter_length": 1200
            },
            "Science Fiction": {
                "chapter_count": 4,
                "target_word_count": 6000,
                "chapter_length": 1500,
                "min_chapter_length": 1200
            }
        }
    
    def get_api_optimization_settings(self) -> Dict[str, Any]:
        """Get API optimization settings for testing."""
        return {
            "reduced_timeouts": {
                "connection_timeout": 30,
                "read_timeout": 60,
                "total_timeout": 120
            },
            "reduced_retries": {
                "max_retries": 2,
                "retry_delay": 1.0,
                "backoff_factor": 1.5
            },
            "token_limits": {
                "minimal": 4000,
                "standard": 8000,
                "complex": 12000
            },
            "temperature_settings": {
                "fast": 0.5,
                "balanced": 0.7,
                "creative": 0.8
            }
        }
    
    def get_expected_performance_metrics(self) -> Dict[str, Any]:
        """Get expected performance metrics for validation."""
        return {
            "minimal_book": {
                "max_duration_seconds": 120,
                "min_word_count": 1500,
                "max_word_count": 2500,
                "expected_chapters": 2
            },
            "standard_book": {
                "max_duration_seconds": 300,
                "min_word_count": 4500,
                "max_word_count": 7500,
                "expected_chapters": 4
            },
            "complex_book": {
                "max_duration_seconds": 450,
                "min_word_count": 3500,
                "max_word_count": 5500,
                "expected_chapters": 3
            },
            "minimal_series": {
                "max_duration_seconds": 360,
                "min_total_word_count": 3000,
                "max_total_word_count": 5000,
                "expected_books": 2
            }
        }
