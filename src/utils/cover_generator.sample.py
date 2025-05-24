"""
Cover Generation Module for ebook generation.

This module creates book covers using programmatic elements with techniques like
dynamic typography, color gradients, patterns, and embossed effects.
"""
import os
import numpy as np
from typing import Tuple, Optional, List, Dict
from PIL import Image, ImageDraw, ImageFont, ImageChops
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CoverGenerator:
    """
    Generates book covers using programmatic techniques without external images.
    """
    def __init__(self, output_dir: str = None):
        """
        Initialize the cover generator.

        Args:
            output_dir: Directory where cover images will be saved
        """
        self.output_dir = output_dir or "covers"
        os.makedirs(self.output_dir, exist_ok=True)

        # Default cover dimensions (6x9 inches at 300 DPI)
        self.width = 1800
        self.height = 2700

        # Try to load fonts
        self.title_font = self._load_font("title", 120)
        self.author_font = self._load_font("author", 80)
        self.subtitle_font = self._load_font("subtitle", 60)

        # Color palettes by genre
        self.genre_palettes = {
            "thriller": [(30, 30, 30), (220, 20, 60), (200, 200, 200)],  # Dark gray, crimson, light gray
            "mystery": [(25, 25, 45), (120, 90, 170), (220, 220, 240)],  # Dark blue, purple, light lavender
            "science fiction": [(0, 20, 60), (0, 200, 255), (50, 0, 80)],
            "fantasy": [(50, 0, 80), (150, 100, 200), (20, 0, 40)],
            "romance": [(150, 50, 80), (240, 150, 180), (100, 20, 50)],
            "literary fiction": [(50, 50, 50), (200, 200, 200), (100, 100, 100)],
            "historical fiction": [(100, 70, 30), (200, 170, 120), (60, 40, 20)],
            "horror": [(10, 10, 10), (120, 0, 0), (40, 0, 0)],
            "young adult": [(50, 100, 200), (200, 100, 200), (100, 200, 100)],
            "self help": [(0, 100, 100), (100, 200, 200), (0, 50, 100)],
            "business": [(0, 50, 100), (100, 150, 200), (50, 100, 150)],
            "biography": [(50, 50, 0), (150, 150, 100), (100, 100, 50)],
            "academic": [(50, 50, 100), (150, 150, 200), (100, 100, 150)]
        }

    def _load_font(self, font_type: str, size: int) -> Optional[ImageFont.FreeTypeFont]:
        """
        Load a font for the cover.

        Args:
            font_type: Type of font (title, author, or subtitle)
            size: Font size

        Returns:
            Font object or None if default fonts are used
        """
        # List of common fonts to try
        font_names = [
            "Arial.ttf", "Verdana.ttf", "Georgia.ttf", "Times.ttf",
            "TimesNewRoman.ttf", "Calibri.ttf", "Cambria.ttf"
        ]

        # Common font directories
        font_dirs = [
            "/usr/share/fonts/truetype",
            "/usr/share/fonts/TTF",
            "C:/Windows/Fonts",
            "/Library/Fonts"
        ]

        # Try to find and load a font
        for font_dir in font_dirs:
            if os.path.exists(font_dir):
                for font_name in font_names:
                    font_path = os.path.join(font_dir, font_name)
                    if os.path.exists(font_path):
                        try:
                            return ImageFont.truetype(font_path, size)
                        except OSError:
                            continue

        # If no font found, use default
        return ImageFont.load_default()

    def _wrap_text(self, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> List[str]:
        """
        Wrap text to fit within a specified width.

        Args:
            text: Text to wrap
            font: Font to use for measuring text
            max_width: Maximum width in pixels

        Returns:
            List of text lines
        """
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            # Try adding the word to the current line
            test_line = ' '.join(current_line + [word])
            bbox = ImageDraw.Draw(Image.new('RGB', (1, 1))).textbbox((0, 0), test_line, font=font)
            text_width = bbox[2] - bbox[0]

            if text_width <= max_width or not current_line:
                # Word fits or is the first word on the line
                current_line.append(word)
            else:
                # Word doesn't fit, start a new line
                lines.append(' '.join(current_line))
                current_line = [word]

        # Add the last line
        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def _create_color_gradient(self, width: int, height: int, color1: Tuple[int, int, int],
                              color2: Tuple[int, int, int], direction: str = "vertical") -> Image.Image:
        """
        Create a gradient image.

        Args:
            width: Image width
            height: Image height
            color1: Start color (RGB)
            color2: End color (RGB)
            direction: Gradient direction ("vertical", "horizontal", "diagonal", "radial")

        Returns:
            PIL Image with gradient
        """
        # Create gradient array using numpy for efficiency
        if direction == "vertical":
            gradient = np.linspace(0, 1, height)[:, np.newaxis] * np.ones((height, width))
        elif direction == "horizontal":
            gradient = np.linspace(0, 1, width)[np.newaxis, :] * np.ones((height, width))
        elif direction == "diagonal":
            gradient = np.linspace(0, 1, width + height)
            gradient = np.array([gradient[i:i+width] for i in range(height)])
            gradient = gradient / np.max(gradient)
        elif direction == "radial":
            x = np.linspace(-1, 1, width)
            y = np.linspace(-1, 1, height)
            xx, yy = np.meshgrid(x, y)
            gradient = np.sqrt(xx**2 + yy**2)
            gradient = gradient / np.max(gradient)
        else:
            # Default to vertical
            gradient = np.linspace(0, 1, height)[:, np.newaxis] * np.ones((height, width))

        # Create RGB array
        r = np.array(color1[0] * (1 - gradient) + color2[0] * gradient, dtype=np.uint8)
        g = np.array(color1[1] * (1 - gradient) + color2[1] * gradient, dtype=np.uint8)
        b = np.array(color1[2] * (1 - gradient) + color2[2] * gradient, dtype=np.uint8)

        # Stack RGB channels
        rgb = np.dstack((r, g, b))

        # Create PIL Image
        return Image.fromarray(rgb, 'RGB')

    def _create_noise_texture(self, width: int, height: int, opacity: float = 0.2) -> Image.Image:
        """
        Create a noise texture background.

        Args:
            width: Image width
            height: Image height
            opacity: Texture opacity

        Returns:
            PIL Image with texture
        """
        # Create random noise
        noise = np.random.rand(height, width)

        # Scale noise to 0-255 and convert to uint8
        noise_img = (noise * 255).astype(np.uint8)

        # Create PIL image
        texture = Image.fromarray(noise_img, mode='L')

        # Convert to RGBA with specified opacity
        texture_rgba = Image.new('RGBA', (width, height), (255, 255, 255, 0))
        texture_rgba.putalpha(ImageChops.multiply(texture, Image.new('L', texture.size, int(opacity * 255))))

        return texture_rgba

    def generate_cover(self, title: str, author: str, genre: str = "fantasy",
                      output_path: Optional[str] = None) -> str:
        """
        Generate a cover for a book.

        Args:
            title: Book title
            author: Author name
            genre: Book genre (used for color palette selection)
            output_path: Path to save the cover image, if None generates a path

        Returns:
            Path to the generated cover image
        """
        logger.info(f"Generating cover for '{title}' by {author}")

        # Get color palette based on genre
        genre_lower = genre.lower()
        if genre_lower in self.genre_palettes:
            palette = self.genre_palettes[genre_lower]
        else:
            # Default to fantasy palette
            palette = self.genre_palettes["fantasy"]

        # Create base image with gradient background
        base_img = self._create_color_gradient(
            self.width, self.height,
            color1=palette[0],
            color2=palette[1],
            direction="vertical"
        )

        # Add noise texture
        texture = self._create_noise_texture(
            self.width, self.height,
            opacity=0.2
        )

        # Convert base image to RGBA for compositing
        base_rgba = base_img.convert('RGBA')

        # Composite texture onto base image
        result = Image.alpha_composite(base_rgba, texture)

        # Convert back to RGB
        result = result.convert('RGB')

        # Draw title
        title_width = self.width - 200  # Margin
        title_lines = self._wrap_text(title, self.title_font, title_width)
        title_y = self.height // 3

        # Create a drawing surface
        draw = ImageDraw.Draw(result)

        # Draw each line of the title
        for line in title_lines:
            title_bbox = draw.textbbox((0, 0), line, font=self.title_font)
            title_width = title_bbox[2] - title_bbox[0]

            # Draw title with shadow effect
            shadow_offset = 5
            draw.text(((self.width - title_width) // 2 + shadow_offset, title_y + shadow_offset),
                     line, font=self.title_font, fill=(0, 0, 0, 128))
            draw.text(((self.width - title_width) // 2, title_y),
                     line, font=self.title_font, fill=(255, 255, 255))

            title_y += title_bbox[3] - title_bbox[1] + 20

        # Draw author
        author_text = f"by {author}"
        author_bbox = draw.textbbox((0, 0), author_text, font=self.author_font)
        author_width = author_bbox[2] - author_bbox[0]

        # Draw author with shadow effect
        shadow_offset = 3
        draw.text(((self.width - author_width) // 2 + shadow_offset, title_y + 100 + shadow_offset),
                 author_text, font=self.author_font, fill=(0, 0, 0, 128))
        draw.text(((self.width - author_width) // 2, title_y + 100),
                 author_text, font=self.author_font, fill=(255, 255, 255))

        # Add border
        border_width = 20
        draw.rectangle(
            [(border_width, border_width),
             (self.width - border_width, self.height - border_width)],
            outline=(255, 255, 255, 100),
            width=2
        )

        # Determine output path if not provided
        if not output_path:
            output_filename = f"{title.lower().replace(' ', '_')}_cover.jpg"
            output_path = os.path.join(self.output_dir, output_filename)

        # Save the image
        result.save(output_path, quality=95)
        logger.info(f"Cover saved to {output_path}")

        return output_path
