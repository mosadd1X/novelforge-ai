#!/usr/bin/env python3
"""
Mock Components for Fast Testing

This module provides mock implementations of time-consuming components
to enable ultra-fast testing while maintaining the same code paths
as the production system.

Key Features:
- Mock Gemini API client with instant responses
- Configurable response patterns for different test scenarios
- Maintains same interface as real components
- Provides realistic but minimal content for testing
"""

import json
import time
import random
from typing import Dict, List, Any, Optional
from datetime import datetime


class MockGeminiClient:
    """
    Mock implementation of the Gemini API client for fast testing.
    
    This mock client provides instant responses with realistic content
    patterns while maintaining the same interface as the real client.
    """
    
    def __init__(self):
        """Initialize the mock client with predefined responses."""
        self.call_count = 0
        self.response_delay = 0.1  # Minimal delay to simulate processing
        
        # Predefined responses for different types of requests
        self.mock_responses = {
            "writer_profile": self._get_mock_writer_profile,
            "novel_outline": self._get_mock_novel_outline,
            "characters": self._get_mock_characters,
            "chapter": self._get_mock_chapter,
            "enhancement": self._get_mock_enhancement,
            "series_plan": self._get_mock_series_plan
        }
    
    def generate_content(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 16000,
        max_retries: int = 5,
        initial_retry_delay: float = 2.0
    ) -> str:
        """
        Generate mock content based on the prompt.
        
        Args:
            prompt: The prompt to analyze for response type
            temperature: Ignored in mock
            max_tokens: Used to determine response length
            max_retries: Ignored in mock
            initial_retry_delay: Ignored in mock
            
        Returns:
            Mock response appropriate for the prompt type
        """
        self.call_count += 1
        
        # Simulate minimal processing time
        time.sleep(self.response_delay)
        
        # Determine response type based on prompt content
        response_type = self._determine_response_type(prompt)
        
        # Generate appropriate mock response
        if response_type in self.mock_responses:
            return self.mock_responses[response_type](prompt, max_tokens)
        else:
            return self._get_generic_response(prompt, max_tokens)
    
    def generate_with_context(
        self,
        prompt: str,
        context: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 16000,
        priority=None,
        max_retries: int = None,
        timeout: float = None
    ) -> str:
        """Generate content with context (same as generate_content for mock)."""
        return self.generate_content(prompt, temperature, max_tokens)
    
    def check_api_connection(self, check_all_keys: bool = False) -> Dict[str, Any]:
        """Mock API connection check that always succeeds."""
        return {
            "success": True,
            "message": "Mock API connection successful",
            "available_keys": 1,
            "rate_limited_keys": 0
        }
    
    def clean_response(self, response: str) -> str:
        """Clean response (pass-through for mock)."""
        return response.strip()
    
    def _determine_response_type(self, prompt: str) -> str:
        """Determine the type of response needed based on prompt content."""
        prompt_lower = prompt.lower()
        
        if "writer profile" in prompt_lower or "fictional author" in prompt_lower:
            return "writer_profile"
        elif "novel outline" in prompt_lower or "chapter outline" in prompt_lower:
            return "novel_outline"
        elif "characters" in prompt_lower and "generate" in prompt_lower:
            return "characters"
        elif "chapter" in prompt_lower and ("write" in prompt_lower or "generate" in prompt_lower):
            return "chapter"
        elif "enhance" in prompt_lower or "improve" in prompt_lower:
            return "enhancement"
        elif "series plan" in prompt_lower or "book templates" in prompt_lower:
            return "series_plan"
        else:
            return "generic"
    
    def _get_mock_writer_profile(self, prompt: str, max_tokens: int) -> str:
        """Generate a mock writer profile."""
        profiles = [
            {
                "name": "Elena Vasquez",
                "background": "Contemporary fiction writer from Mexico",
                "writing_style": "Lyrical and emotionally resonant",
                "specialties": ["Character development", "Cultural themes"],
                "notable_works": ["The Garden of Memory", "Whispers in the Wind"],
                "writing_approach": "Character-driven narratives with rich cultural context"
            },
            {
                "name": "Marcus Chen",
                "background": "Science fiction author from Singapore",
                "writing_style": "Technical precision with human emotion",
                "specialties": ["World building", "Technology integration"],
                "notable_works": ["Digital Horizons", "The Quantum Garden"],
                "writing_approach": "Hard science fiction with philosophical depth"
            }
        ]
        
        profile = random.choice(profiles)
        return json.dumps(profile, indent=2)
    
    def _get_mock_novel_outline(self, prompt: str, max_tokens: int) -> str:
        """Generate a mock novel outline."""
        # Determine chapter count based on prompt or use default
        chapter_count = 2 if "test" in prompt.lower() else 4
        
        outline = {
            "recommended_chapter_count": chapter_count,
            "target_word_count": chapter_count * 1000,
            "chapters": []
        }
        
        for i in range(1, chapter_count + 1):
            outline["chapters"].append({
                "title": f"Chapter {i}: Test Chapter Title {i}",
                "summary": f"This is a test chapter summary for chapter {i}. It contains the basic plot points and character development needed for testing purposes."
            })
        
        return json.dumps(outline, indent=2)
    
    def _get_mock_characters(self, prompt: str, max_tokens: int) -> str:
        """Generate mock characters."""
        characters = [
            {
                "name": "Alex Thompson",
                "age": 28,
                "role": "Protagonist",
                "description": "A determined software developer facing life changes",
                "personality": "Analytical, caring, sometimes overthinks",
                "background": "Grew up in a small town, moved to the city for work"
            },
            {
                "name": "Sarah Martinez",
                "age": 26,
                "role": "Supporting Character",
                "description": "Alex's best friend and confidant",
                "personality": "Outgoing, loyal, practical",
                "background": "Local artist with strong family ties"
            }
        ]
        
        return json.dumps(characters, indent=2)
    
    def _get_mock_chapter(self, prompt: str, max_tokens: int) -> str:
        """Generate a mock chapter."""
        # Determine target length based on max_tokens
        target_words = min(max_tokens // 4, 1500)  # Rough token-to-word conversion
        
        # Generate content based on target length
        if target_words < 500:
            return self._get_short_chapter()
        elif target_words < 1000:
            return self._get_medium_chapter()
        else:
            return self._get_long_chapter()
    
    def _get_short_chapter(self) -> str:
        """Generate a short test chapter."""
        return """
        The morning sun filtered through the office windows as Alex stared at the computer screen. 
        The code wasn't working, and the deadline was approaching fast. 
        
        "Another coffee?" Sarah asked, appearing at the cubicle entrance.
        
        "Thanks, but I think I've had enough caffeine for one lifetime," Alex replied, rubbing tired eyes.
        
        The project had seemed simple enough at the start, but complications kept arising. 
        Each solution created new problems, like a digital hydra growing new heads.
        
        "Maybe it's time for a break," Sarah suggested. "Fresh air might help."
        
        Alex nodded, saving the work and standing up. Sometimes the best solutions came 
        when you stopped looking for them.
        """
    
    def _get_medium_chapter(self) -> str:
        """Generate a medium-length test chapter."""
        return """
        The morning sun filtered through the office windows as Alex stared at the computer screen. 
        The code wasn't working, and the deadline was approaching fast. Three weeks of development 
        had led to this moment, and everything seemed to be falling apart.
        
        "Another coffee?" Sarah asked, appearing at the cubicle entrance with two steaming mugs.
        
        "Thanks, but I think I've had enough caffeine for one lifetime," Alex replied, rubbing tired eyes. 
        The monitor's blue glow had become a constant companion over the past few days.
        
        The project had seemed simple enough at the start—a basic inventory management system 
        for a local bookstore. But complications kept arising like weeds in a garden. 
        Each solution created new problems, like a digital hydra growing new heads.
        
        "What's the issue this time?" Sarah pulled up a chair, her artist's eye scanning 
        the lines of code with surprising understanding.
        
        "The database integration is failing. Every time I fix one query, another breaks." 
        Alex gestured at the screen in frustration. "It's like the system has a mind of its own."
        
        Sarah studied the code for a moment, then pointed to a section near the top. 
        "What about this connection string? Looks like it might be causing conflicts."
        
        Alex leaned forward, following Sarah's finger. She was right—a small typo in the 
        configuration was cascading through the entire system. Sometimes it took fresh eyes 
        to see what had been hiding in plain sight.
        
        "You're brilliant," Alex said, making the correction. "How did you spot that?"
        
        "Same way I spot composition issues in my paintings. Sometimes you need to step back 
        and look at the whole picture instead of focusing on individual brushstrokes."
        
        The fix worked. The system came alive, data flowing smoothly between components. 
        Alex felt the familiar rush of satisfaction that came with solving a complex problem.
        
        "Lunch?" Sarah suggested. "I think this calls for a celebration."
        
        Alex nodded, saving the work and standing up. Sometimes the best solutions came 
        when you stopped looking for them, and the best friends were the ones who helped 
        you see clearly when everything seemed impossible.
        """
    
    def _get_long_chapter(self) -> str:
        """Generate a longer test chapter."""
        return self._get_medium_chapter() + """
        
        They walked to the small café down the street, the one with mismatched chairs 
        and walls covered in local artwork. Sarah's paintings hung in the corner, 
        vibrant landscapes that seemed to capture more than just scenery.
        
        "I've been thinking," Sarah said as they settled at their usual table by the window. 
        "About what you said last week, about feeling stuck."
        
        Alex looked up from the menu, though they both knew they'd order the same thing 
        they always did. "The job situation?"
        
        "Everything. The job, the city, the routine. You've been talking about change 
        for months, but you never actually do anything about it."
        
        It was true, and Alex knew it. The comfortable routine had become a comfortable prison. 
        Wake up, work, solve problems, go home, repeat. Even the satisfaction of fixing 
        today's bug felt hollow somehow.
        
        "Change is scary," Alex admitted. "What if I make the wrong choice?"
        
        "What if you make the right one?" Sarah countered. "What if staying is the wrong choice?"
        
        The waitress brought their usual orders without being asked—grilled cheese and tomato 
        soup for Alex, quinoa salad for Sarah. The familiarity was comforting and suffocating 
        at the same time.
        
        "I got an email yesterday," Alex said quietly. "From that startup in Portland. 
        They want to interview me for the senior developer position."
        
        Sarah's eyes lit up. "That's amazing! When's the interview?"
        
        "I haven't responded yet." Alex stirred the soup absently. "It would mean leaving 
        everything behind. This job, this city, this life we've built."
        
        "This life you've built," Sarah corrected gently. "I'll still be here when you get back. 
        And if you don't get back, well, Portland's not that far away."
        
        The afternoon passed quickly, filled with planning and possibilities. By the time 
        they returned to the office, Alex had made a decision. The email response was short 
        but decisive: "I'd be honored to interview for the position."
        
        Change was scary, but staying scared was scarier.
        """
    
    def _get_mock_enhancement(self, prompt: str, max_tokens: int) -> str:
        """Generate mock enhanced content."""
        return "Enhanced version: " + self._get_medium_chapter()
    
    def _get_mock_series_plan(self, prompt: str, max_tokens: int) -> str:
        """Generate a mock series plan."""
        plan = {
            "series_title": "Test Series",
            "total_books": 2,
            "books": [
                {
                    "book_number": 1,
                    "title": "Test Book One",
                    "description": "The first book in the test series",
                    "main_themes": ["Beginning", "Discovery"]
                },
                {
                    "book_number": 2,
                    "title": "Test Book Two", 
                    "description": "The second book in the test series",
                    "main_themes": ["Development", "Resolution"]
                }
            ]
        }
        
        return json.dumps(plan, indent=2)
    
    def _get_generic_response(self, prompt: str, max_tokens: int) -> str:
        """Generate a generic mock response."""
        return f"Mock response for prompt: {prompt[:100]}..."


class MockTimer:
    """Mock timer for testing time-dependent operations."""
    
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
    
    def start(self):
        """Start the timer."""
        self.start_time = time.time()
    
    def stop(self):
        """Stop the timer and calculate elapsed time."""
        if self.start_time:
            self.elapsed_time = time.time() - self.start_time
    
    def get_elapsed_time(self) -> str:
        """Get formatted elapsed time."""
        return f"{self.elapsed_time:.2f}s"
