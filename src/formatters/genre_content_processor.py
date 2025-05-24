"""
Genre-specific content processing for EPUB formatting.

This module provides specialized content processing functions for different genres
to ensure proper structure and formatting in the final EPUB output.
"""

import re
from typing import Dict, Any, List
from bs4 import BeautifulSoup
import markdown2


class GenreContentProcessor:
    """Processes content based on genre-specific requirements."""
    
    def __init__(self, format_type: str):
        """
        Initialize the content processor.
        
        Args:
            format_type: The format type for specialized processing
        """
        self.format_type = format_type
    
    def process_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """
        Process content based on the format type.
        
        Args:
            content: Raw content to process
            chapter_data: Chapter metadata
            
        Returns:
            str: Processed HTML content
        """
        # Convert markdown to HTML if needed
        if "```" in content or "#" in content or "*" in content:
            html_content = markdown2.markdown(content)
        else:
            # Basic paragraph wrapping
            paragraphs = content.split("\n\n")
            html_content = "".join([f"<p>{p}</p>" for p in paragraphs if p.strip()])
        
        # Apply format-specific processing
        if self.format_type == "poetry":
            return self._process_poetry_content(html_content, chapter_data)
        elif self.format_type == "cookbook":
            return self._process_cookbook_content(html_content, chapter_data)
        elif self.format_type == "travel":
            return self._process_travel_content(html_content, chapter_data)
        elif self.format_type == "self_help":
            return self._process_self_help_content(html_content, chapter_data)
        elif self.format_type == "biography":
            return self._process_biography_content(html_content, chapter_data)
        elif self.format_type == "business":
            return self._process_business_content(html_content, chapter_data)
        elif self.format_type == "academic":
            return self._process_academic_content(html_content, chapter_data)
        elif self.format_type == "essay":
            return self._process_essay_content(html_content, chapter_data)
        elif self.format_type == "short_story":
            return self._process_short_story_content(html_content, chapter_data)
        elif self.format_type == "graphic_novel":
            return self._process_graphic_novel_content(html_content, chapter_data)
        else:
            return self._process_standard_content(html_content, chapter_data)
    
    def _process_poetry_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for poetry collections."""
        soup = BeautifulSoup(content, "html.parser")
        
        # Find poem titles (usually in ** or bold formatting)
        for element in soup.find_all(['strong', 'b']):
            if element.get_text().strip():
                # Convert to poem title
                element.name = 'h3'
                element['class'] = 'poem-title'
                element.clear()
                element.string = element.get_text().strip('*')
        
        # Process poem content - preserve line breaks
        processed_content = str(soup)
        
        # Convert line breaks to proper poetry formatting
        processed_content = re.sub(r'\n\s*\n', '</div><div class="stanza-break"></div><div class="stanza">', processed_content)
        processed_content = re.sub(r'\n', '<br class="poetry-line">', processed_content)
        
        # Wrap in poetry section
        return f'<div class="poetry-section">{processed_content}</div>'
    
    def _process_cookbook_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for cookbooks."""
        soup = BeautifulSoup(content, "html.parser")
        
        # Look for recipe patterns
        processed_content = str(soup)
        
        # Convert ingredient lists
        processed_content = re.sub(
            r'(?i)(ingredients?:?\s*)(.*?)(?=instructions?:?|directions?:?|method:?|\n\n)',
            r'<div class="ingredients"><h4 class="ingredients-title">Ingredients</h4><ul>\2</ul></div>',
            processed_content,
            flags=re.DOTALL
        )
        
        # Convert instruction lists
        processed_content = re.sub(
            r'(?i)(instructions?:?|directions?:?|method:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="instructions"><h4 class="instructions-title">Instructions</h4><ol>\2</ol></div>',
            processed_content,
            flags=re.DOTALL
        )
        
        # Add recipe wrapper
        return f'<div class="recipe">{processed_content}</div>'
    
    def _process_travel_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for travel guides."""
        soup = BeautifulSoup(content, "html.parser")
        
        processed_content = str(soup)
        
        # Look for practical information patterns
        processed_content = re.sub(
            r'(?i)(address:?\s*)(.*?)(?=\n|$)',
            r'<div class="address">\1\2</div>',
            processed_content
        )
        
        processed_content = re.sub(
            r'(?i)(hours?:?\s*)(.*?)(?=\n|$)',
            r'<div class="hours">\1\2</div>',
            processed_content
        )
        
        processed_content = re.sub(
            r'(?i)(price:?\s*)(.*?)(?=\n|$)',
            r'<div class="price">\1\2</div>',
            processed_content
        )
        
        # Add destination wrapper
        return f'<div class="destination">{processed_content}</div>'
    
    def _process_self_help_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for self-help books."""
        soup = BeautifulSoup(content, "html.parser")
        
        processed_content = str(soup)
        
        # Look for exercise patterns
        processed_content = re.sub(
            r'(?i)(exercise:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="exercise"><h4 class="exercise-title">Exercise</h4>\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        # Look for key points
        processed_content = re.sub(
            r'(?i)(key point:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="key-point">\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        # Look for action items
        processed_content = re.sub(
            r'(?i)(action:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="action-item">\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        return processed_content
    
    def _process_biography_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for biographies and memoirs."""
        soup = BeautifulSoup(content, "html.parser")
        
        processed_content = str(soup)
        
        # Look for date patterns and convert to timeline
        processed_content = re.sub(
            r'(?i)(\d{4}):?\s*(.*?)(?=\n|$)',
            r'<div class="timeline-event"><div class="timeline-date">\1</div>\2</div>',
            processed_content
        )
        
        # Look for quotes
        processed_content = re.sub(
            r'"([^"]+)"',
            r'<div class="quote">"\1"</div>',
            processed_content
        )
        
        return processed_content
    
    def _process_business_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for business books."""
        soup = BeautifulSoup(content, "html.parser")
        
        processed_content = str(soup)
        
        # Look for case study patterns
        processed_content = re.sub(
            r'(?i)(case study:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="case-study"><h4 class="case-study-title">Case Study</h4>\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        # Look for strategy patterns
        processed_content = re.sub(
            r'(?i)(strategy:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="strategy">\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        # Look for best practices
        processed_content = re.sub(
            r'(?i)(best practice:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="best-practice">\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        return processed_content
    
    def _process_academic_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for academic books."""
        soup = BeautifulSoup(content, "html.parser")
        
        processed_content = str(soup)
        
        # Look for definition patterns
        processed_content = re.sub(
            r'(?i)(definition:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="definition"><h4 class="definition-term">Definition</h4>\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        # Look for examples
        processed_content = re.sub(
            r'(?i)(example:?\s*)(.*?)(?=\n\n|$)',
            r'<div class="example"><h4 class="example-title">Example</h4>\2</div>',
            processed_content,
            flags=re.DOTALL
        )
        
        return processed_content
    
    def _process_essay_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for essay collections."""
        soup = BeautifulSoup(content, "html.parser")
        
        # Add essay wrapper and title
        chapter_title = chapter_data.get('title', 'Essay')
        processed_content = f'<div class="essay"><h2 class="essay-title">{chapter_title}</h2>{str(soup)}</div>'
        
        return processed_content
    
    def _process_short_story_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for short story collections."""
        soup = BeautifulSoup(content, "html.parser")
        
        # Add story wrapper and title
        chapter_title = chapter_data.get('title', 'Story')
        processed_content = f'<div class="story"><h2 class="story-title">{chapter_title}</h2>{str(soup)}</div>'
        
        return processed_content
    
    def _process_graphic_novel_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for graphic novels."""
        soup = BeautifulSoup(content, "html.parser")
        
        processed_content = str(soup)
        
        # Look for panel descriptions
        processed_content = re.sub(
            r'(?i)(panel:?\s*)(.*?)(?=\n|$)',
            r'<div class="panel-description">\2</div>',
            processed_content
        )
        
        # Look for dialogue
        processed_content = re.sub(
            r'"([^"]+)"',
            r'<div class="dialogue">"\1"</div>',
            processed_content
        )
        
        # Look for sound effects
        processed_content = re.sub(
            r'(?i)(sound:?\s*)(.*?)(?=\n|$)',
            r'<div class="sound-effect">\2</div>',
            processed_content
        )
        
        return processed_content
    
    def _process_standard_content(self, content: str, chapter_data: Dict[str, Any]) -> str:
        """Process content for standard formatting."""
        soup = BeautifulSoup(content, "html.parser")
        return str(soup)
