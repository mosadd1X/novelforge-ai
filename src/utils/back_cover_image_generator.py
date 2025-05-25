"""
Back Cover Image Generator for Ebook Generation System.

This module creates professional back cover images with descriptions,
author information, and genre-appropriate styling.
"""

import os
import base64
from typing import Dict, Any, Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import textwrap
from datetime import datetime


class BackCoverImageGenerator:
    """
    Generates back cover images with text, styling, and layout.
    """
    
    def __init__(self):
        """Initialize the back cover image generator."""
        self.default_width = 1600
        self.default_height = 2400
        self.margin = 80
        self.line_spacing = 1.4
    
    def generate_back_cover(self, book_data: Dict[str, Any], 
                          descriptions: Dict[str, str]) -> Optional[str]:
        """
        Generate a complete back cover image.
        
        Args:
            book_data: Book metadata and information
            descriptions: Generated descriptions (short, back_cover, tagline)
            
        Returns:
            Base64 encoded image data or None if failed
        """
        try:
            # Create base image
            img = Image.new('RGB', (self.default_width, self.default_height), 
                          color=self._get_genre_background_color(book_data.get("genre", "Fiction")))
            
            draw = ImageDraw.Draw(img)
            
            # Get fonts
            fonts = self._load_fonts()
            
            # Layout the back cover
            y_position = self.margin
            
            # 1. Add tagline at top
            if descriptions.get("tagline"):
                y_position = self._add_tagline(draw, descriptions["tagline"], 
                                             fonts["tagline"], y_position)
            
            # 2. Add main description
            if descriptions.get("back_cover_description"):
                y_position = self._add_description(draw, descriptions["back_cover_description"],
                                                 fonts["body"], y_position)
            
            # 3. Add author information
            author = book_data.get("author", "Unknown Author")
            y_position = self._add_author_section(draw, author, fonts["author"], y_position)
            
            # 4. Add genre badge
            genre = book_data.get("genre", "Fiction")
            self._add_genre_badge(draw, genre, fonts["genre"])
            
            # 5. Add ISBN/barcode area (placeholder)
            self._add_isbn_area(draw, book_data, fonts["isbn"])
            
            # Convert to base64
            return self._image_to_base64(img)
            
        except Exception as e:
            print(f"Error generating back cover: {e}")
            return None
    
    def _get_genre_background_color(self, genre: str) -> Tuple[int, int, int]:
        """
        Get background color based on genre.
        
        Args:
            genre: Book genre
            
        Returns:
            RGB color tuple
        """
        genre_lower = genre.lower()
        
        if "romance" in genre_lower:
            return (25, 25, 35)  # Deep romantic dark
        elif "mystery" in genre_lower or "thriller" in genre_lower:
            return (15, 15, 25)  # Dark mysterious
        elif "fantasy" in genre_lower:
            return (20, 25, 40)  # Deep magical blue
        elif "science fiction" in genre_lower or "sci-fi" in genre_lower:
            return (10, 20, 30)  # Tech dark blue
        elif "horror" in genre_lower:
            return (25, 15, 15)  # Dark red
        else:
            return (20, 20, 25)  # Default dark
    
    def _load_fonts(self) -> Dict[str, ImageFont.ImageFont]:
        """
        Load fonts for different text elements.
        
        Returns:
            Dictionary of fonts
        """
        fonts = {}
        
        try:
            # Try to load system fonts
            fonts["tagline"] = ImageFont.truetype("arial.ttf", 48)
            fonts["body"] = ImageFont.truetype("arial.ttf", 32)
            fonts["author"] = ImageFont.truetype("arialbd.ttf", 40)
            fonts["genre"] = ImageFont.truetype("arial.ttf", 24)
            fonts["isbn"] = ImageFont.truetype("arial.ttf", 20)
        except:
            # Fallback to default font
            fonts["tagline"] = ImageFont.load_default()
            fonts["body"] = ImageFont.load_default()
            fonts["author"] = ImageFont.load_default()
            fonts["genre"] = ImageFont.load_default()
            fonts["isbn"] = ImageFont.load_default()
        
        return fonts
    
    def _add_tagline(self, draw: ImageDraw.Draw, tagline: str, 
                    font: ImageFont.ImageFont, y_position: int) -> int:
        """
        Add tagline to the back cover.
        
        Args:
            draw: ImageDraw object
            tagline: Tagline text
            font: Font to use
            y_position: Current Y position
            
        Returns:
            New Y position after adding tagline
        """
        # Center the tagline
        text_width = draw.textlength(tagline, font=font)
        x_position = (self.default_width - text_width) // 2
        
        # Add text with outline for visibility
        outline_color = (255, 255, 255)
        text_color = (200, 200, 255)
        
        # Draw outline
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                if dx != 0 or dy != 0:
                    draw.text((x_position + dx, y_position + dy), tagline, 
                            font=font, fill=outline_color)
        
        # Draw main text
        draw.text((x_position, y_position), tagline, font=font, fill=text_color)
        
        return y_position + 100
    
    def _add_description(self, draw: ImageDraw.Draw, description: str,
                        font: ImageFont.ImageFont, y_position: int) -> int:
        """
        Add main description text to the back cover.
        
        Args:
            draw: ImageDraw object
            description: Description text
            font: Font to use
            y_position: Current Y position
            
        Returns:
            New Y position after adding description
        """
        # Wrap text to fit width
        max_width = self.default_width - (2 * self.margin)
        wrapped_lines = self._wrap_text(description, font, max_width)
        
        text_color = (220, 220, 220)
        line_height = int(font.size * self.line_spacing)
        
        for line in wrapped_lines:
            # Center each line
            text_width = draw.textlength(line, font=font)
            x_position = (self.default_width - text_width) // 2
            
            draw.text((x_position, y_position), line, font=font, fill=text_color)
            y_position += line_height
        
        return y_position + 60
    
    def _add_author_section(self, draw: ImageDraw.Draw, author: str,
                           font: ImageFont.ImageFont, y_position: int) -> int:
        """
        Add author information section.
        
        Args:
            draw: ImageDraw object
            author: Author name
            font: Font to use
            y_position: Current Y position
            
        Returns:
            New Y position after adding author section
        """
        # Add "About the Author" or author name
        author_text = f"by {author}"
        text_width = draw.textlength(author_text, font=font)
        x_position = (self.default_width - text_width) // 2
        
        text_color = (255, 255, 200)
        draw.text((x_position, y_position), author_text, font=font, fill=text_color)
        
        return y_position + 80
    
    def _add_genre_badge(self, draw: ImageDraw.Draw, genre: str, 
                        font: ImageFont.ImageFont) -> None:
        """
        Add genre badge to the back cover.
        
        Args:
            draw: ImageDraw object
            genre: Genre text
            font: Font to use
        """
        # Position in top-right corner
        badge_text = genre.upper()
        text_width = draw.textlength(badge_text, font=font)
        
        x_position = self.default_width - text_width - self.margin
        y_position = self.margin
        
        # Draw badge background
        badge_color = self._get_genre_accent_color(genre)
        padding = 10
        
        draw.rectangle([
            x_position - padding, y_position - padding,
            x_position + text_width + padding, y_position + font.size + padding
        ], fill=badge_color)
        
        # Draw badge text
        draw.text((x_position, y_position), badge_text, font=font, fill=(255, 255, 255))
    
    def _add_isbn_area(self, draw: ImageDraw.Draw, book_data: Dict[str, Any],
                      font: ImageFont.ImageFont) -> None:
        """
        Add ISBN/barcode area at bottom.
        
        Args:
            draw: ImageDraw object
            book_data: Book metadata
            font: Font to use
        """
        # Add placeholder ISBN
        isbn_text = "ISBN 978-0-000000-00-0"
        y_position = self.default_height - self.margin - 40
        
        text_color = (150, 150, 150)
        draw.text((self.margin, y_position), isbn_text, font=font, fill=text_color)
        
        # Add website or publisher info
        website_text = "Generated by AI Book Creator"
        text_width = draw.textlength(website_text, font=font)
        x_position = self.default_width - text_width - self.margin
        
        draw.text((x_position, y_position), website_text, font=font, fill=text_color)
    
    def _get_genre_accent_color(self, genre: str) -> Tuple[int, int, int]:
        """
        Get accent color for genre badge.
        
        Args:
            genre: Book genre
            
        Returns:
            RGB color tuple
        """
        genre_lower = genre.lower()
        
        if "romance" in genre_lower:
            return (180, 50, 100)  # Deep pink
        elif "mystery" in genre_lower or "thriller" in genre_lower:
            return (100, 50, 50)  # Dark red
        elif "fantasy" in genre_lower:
            return (80, 50, 150)  # Purple
        elif "science fiction" in genre_lower or "sci-fi" in genre_lower:
            return (50, 100, 150)  # Blue
        elif "horror" in genre_lower:
            return (150, 50, 50)  # Red
        else:
            return (100, 100, 100)  # Gray
    
    def _wrap_text(self, text: str, font: ImageFont.ImageFont, max_width: int) -> list:
        """
        Wrap text to fit within specified width.
        
        Args:
            text: Text to wrap
            font: Font being used
            max_width: Maximum width in pixels
            
        Returns:
            List of wrapped lines
        """
        words = text.split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = font.getlength(test_line)
            
            if test_width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                    current_line = [word]
                else:
                    # Word is too long, force break
                    lines.append(word)
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def _image_to_base64(self, img: Image.Image) -> str:
        """
        Convert PIL Image to base64 string.
        
        Args:
            img: PIL Image object
            
        Returns:
            Base64 encoded image data
        """
        import io
        
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=90)
        img_data = buffer.getvalue()
        
        return base64.b64encode(img_data).decode('utf-8')
