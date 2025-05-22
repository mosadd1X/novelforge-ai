"""
Enhanced Cover Generator for ebook generation.

This module creates professional-looking book covers using programmatic elements with techniques like
dynamic typography, color gradients, patterns, geometric shapes, and embossed effects.
No external images are required.
"""
import os
import math
import random
import numpy as np
from typing import Tuple, Optional, List, Dict, Any
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, ImageOps
from rich.console import Console
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up console for rich output
console = Console()

class CoverGenerator:
    """
    Generates professional book covers using programmatic techniques without external images.
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
        self.series_font = self._load_font("series", 70)

        # Color palettes by genre
        self.genre_palettes = {
            "test": [(50, 50, 50), (100, 100, 100), (200, 200, 200)],  # Grayscale for testing
            "thriller": [(30, 30, 30), (220, 20, 60), (200, 200, 200)],  # Dark gray, crimson, light gray
            "mystery": [(25, 25, 45), (120, 90, 170), (220, 220, 240)],  # Dark blue, purple, light lavender
            "mystery/thriller": [(20, 20, 40), (180, 30, 80), (220, 220, 240)],  # Dark blue, red-purple, light gray
            "science fiction": [(0, 20, 60), (0, 200, 255), (50, 0, 80)],  # Deep blue, cyan, dark purple
            "fantasy": [(50, 0, 80), (150, 100, 200), (20, 0, 40)],  # Purple, lavender, dark purple
            "romance": [(150, 50, 80), (240, 150, 180), (100, 20, 50)],  # Rose, pink, burgundy
            "literary fiction": [(50, 50, 50), (200, 200, 200), (100, 100, 100)],  # Grayscale
            "commercial fiction": [(40, 70, 100), (180, 200, 220), (80, 110, 140)],  # Blue-gray tones
            "historical fiction": [(100, 70, 30), (200, 170, 120), (60, 40, 20)],  # Brown, tan, dark brown
            "horror": [(10, 10, 10), (120, 0, 0), (40, 0, 0)],  # Black, blood red, dark red
            "young adult": [(50, 100, 200), (200, 100, 200), (100, 200, 100)],  # Blue, purple, green
            "middle grade": [(100, 200, 100), (200, 220, 100), (100, 180, 200)],  # Green, yellow, blue
            "children's book": [(255, 100, 100), (100, 200, 255), (255, 200, 100)],  # Red, blue, yellow
            "self-help": [(0, 100, 100), (100, 200, 200), (0, 50, 100)],  # Teal, light blue, dark teal
            "memoir": [(100, 50, 0), (200, 150, 100), (50, 25, 0)],  # Brown, tan, dark brown
            "biography": [(50, 50, 0), (150, 150, 100), (100, 100, 50)],  # Olive, tan, dark olive
            "other": [(80, 80, 120), (180, 180, 220), (40, 40, 80)]  # Purple-blue tones
        }

        # Cover design styles
        self.design_styles = [
            "gradient",
            "geometric",
            "minimalist",
            "textured",
            "abstract",
            "classic"
        ]

    def _load_font(self, font_type: str, size: int) -> Optional[ImageFont.FreeTypeFont]:
        """
        Load a font for the cover.

        Args:
            font_type: Type of font (title, author, subtitle, or series)
            size: Font size

        Returns:
            Font object or None if default fonts are used
        """
        # List of common fonts to try
        font_names = [
            "Arial.ttf", "Verdana.ttf", "Georgia.ttf", "Times.ttf",
            "TimesNewRoman.ttf", "Calibri.ttf", "Cambria.ttf",
            "Garamond.ttf", "BookAntiqua.ttf", "Palatino.ttf",
            "Tahoma.ttf", "TrebuchetMS.ttf", "Impact.ttf"
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
        try:
            return ImageFont.truetype("arial.ttf", size)
        except:
            return ImageFont.load_default()

    def _title_case(self, text: str) -> str:
        """
        Convert text to title case (capitalize first letter of each word except for small words).

        Args:
            text: Text to convert

        Returns:
            Text in title case
        """
        small_words = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at',
                      'to', 'from', 'by', 'of', 'in', 'with', 'as'}

        # Split the text into words
        words = text.split()

        # Always capitalize the first and last word, and capitalize other words
        # unless they're small words
        for i in range(len(words)):
            if i == 0 or i == len(words) - 1 or words[i].lower() not in small_words:
                words[i] = words[i].capitalize()
            else:
                words[i] = words[i].lower()

        # Rejoin the words
        return ' '.join(words)

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

    def _create_geometric_pattern(self, width: int, height: int, color1: Tuple[int, int, int],
                                 color2: Tuple[int, int, int], pattern_type: str = "triangles") -> Image.Image:
        """
        Create a geometric pattern background.

        Args:
            width: Image width
            height: Image height
            color1: Primary color (RGB)
            color2: Secondary color (RGB)
            pattern_type: Type of pattern ("triangles", "squares", "circles", "lines")

        Returns:
            PIL Image with pattern
        """
        # Create base image
        img = Image.new('RGB', (width, height), color1)
        draw = ImageDraw.Draw(img)

        # Create pattern based on type
        if pattern_type == "triangles":
            # Create triangular pattern
            triangle_size = 200
            for x in range(-triangle_size, width + triangle_size, triangle_size):
                for y in range(-triangle_size, height + triangle_size, triangle_size * 2):
                    offset_y = triangle_size if (x // triangle_size) % 2 == 0 else 0
                    points = [
                        (x, y + offset_y),
                        (x + triangle_size, y + offset_y),
                        (x + triangle_size // 2, y + triangle_size + offset_y)
                    ]
                    draw.polygon(points, fill=color2)

        elif pattern_type == "squares":
            # Create square pattern
            square_size = 100
            for x in range(0, width, square_size * 2):
                for y in range(0, height, square_size * 2):
                    draw.rectangle([(x, y), (x + square_size, y + square_size)], fill=color2)
                    draw.rectangle([(x + square_size, y + square_size),
                                   (x + square_size * 2, y + square_size * 2)], fill=color2)

        elif pattern_type == "circles":
            # Create circle pattern
            circle_size = 100
            for x in range(0, width, circle_size * 2):
                for y in range(0, height, circle_size * 2):
                    draw.ellipse([(x, y), (x + circle_size, y + circle_size)], fill=color2)
                    draw.ellipse([(x + circle_size, y + circle_size),
                                 (x + circle_size * 2, y + circle_size * 2)], fill=color2)

        elif pattern_type == "lines":
            # Create line pattern
            line_spacing = 50
            for y in range(0, height, line_spacing * 2):
                draw.line([(0, y), (width, y)], fill=color2, width=line_spacing // 2)

        return img

    def _add_text_with_effects(self, img: Image.Image, text: str, font: ImageFont.FreeTypeFont,
                              position: Tuple[int, int], color: Tuple[int, int, int] = (255, 255, 255),
                              shadow: bool = True, emboss: bool = False) -> None:
        """
        Add text to an image with optional effects.

        Args:
            img: PIL Image to draw on
            text: Text to add
            font: Font to use
            position: (x, y) position for text
            color: Text color (RGB)
            shadow: Whether to add shadow effect
            emboss: Whether to add emboss effect

        Returns:
            None (modifies img in place)
        """
        draw = ImageDraw.Draw(img)
        x, y = position

        if emboss:
            # Create emboss effect
            for offset in range(1, 4):
                # Draw darker outline
                draw.text((x - offset, y - offset), text, font=font, fill=(0, 0, 0, 100))
                # Draw lighter highlight
                draw.text((x + offset, y + offset), text, font=font, fill=(255, 255, 255, 100))

        if shadow:
            # Create shadow effect
            shadow_offset = 5
            shadow_color = (0, 0, 0, 128)
            draw.text((x + shadow_offset, y + shadow_offset), text, font=font, fill=shadow_color)

        # Draw main text
        draw.text((x, y), text, font=font, fill=color)

    def generate_cover(self, title: str, author: str, genre: str = "fantasy",
                      subtitle: str = None, series_info: Dict[str, Any] = None,
                      design_style: str = None, output_path: Optional[str] = None) -> str:
        """
        Generate a cover for a book.

        Args:
            title: Book title
            author: Author name
            genre: Book genre (used for color palette selection)
            subtitle: Book subtitle (optional)
            series_info: Series information (optional) - dict with keys 'series_title' and 'book_number'
            design_style: Cover design style (optional) - one of 'gradient', 'geometric', 'minimalist', 'textured', 'abstract', 'classic'
            output_path: Path to save the cover image, if None generates a path

        Returns:
            Path to the generated cover image
        """
        console.print(f"[bold cyan]Generating cover for '[/bold cyan][bold yellow]{title}[/bold yellow][bold cyan]' by {author}[/bold cyan]")

        # Get color palette based on genre
        genre_lower = genre.lower()
        if genre_lower in self.genre_palettes:
            palette = self.genre_palettes[genre_lower]
        else:
            # Default to fantasy palette
            palette = self.genre_palettes["fantasy"]
            console.print(f"[yellow]Genre '{genre}' not found in palettes, using default.[/yellow]")

        # Choose design style if not specified
        if not design_style:
            design_style = random.choice(self.design_styles)

        # Create base image based on design style
        if design_style == "gradient":
            # Create gradient background
            gradient_direction = random.choice(["vertical", "horizontal", "diagonal", "radial"])
            base_img = self._create_color_gradient(
                self.width, self.height,
                color1=palette[0],
                color2=palette[1],
                direction=gradient_direction
            )
        elif design_style == "geometric":
            # Create geometric pattern background
            pattern_type = random.choice(["triangles", "squares", "circles", "lines"])
            base_img = self._create_geometric_pattern(
                self.width, self.height,
                color1=palette[0],
                color2=palette[1],
                pattern_type=pattern_type
            )
        elif design_style == "minimalist":
            # Create solid color background with minimal elements
            base_img = Image.new('RGB', (self.width, self.height), palette[0])

            # Add a simple accent element
            draw = ImageDraw.Draw(base_img)
            accent_size = min(self.width, self.height) // 4
            accent_pos = (self.width - accent_size - 100, 100)
            draw.rectangle(
                [accent_pos, (accent_pos[0] + accent_size, accent_pos[1] + accent_size)],
                fill=palette[1]
            )
        elif design_style == "textured":
            # Create textured background
            base_img = self._create_color_gradient(
                self.width, self.height,
                color1=palette[0],
                color2=palette[1],
                direction="vertical"
            )

            # Add strong texture
            texture = self._create_noise_texture(
                self.width, self.height,
                opacity=0.4
            )

            # Convert base image to RGBA for compositing
            base_rgba = base_img.convert('RGBA')

            # Composite texture onto base image
            base_img = Image.alpha_composite(base_rgba, texture).convert('RGB')
        elif design_style == "abstract":
            # Create abstract design with shapes
            base_img = Image.new('RGB', (self.width, self.height), palette[0])
            draw = ImageDraw.Draw(base_img)

            # Add random shapes
            for _ in range(20):
                shape_type = random.choice(["circle", "rectangle", "polygon"])
                color = random.choice([palette[1], palette[2]])
                x = random.randint(0, self.width)
                y = random.randint(0, self.height)
                size = random.randint(100, 500)

                if shape_type == "circle":
                    draw.ellipse([(x, y), (x + size, y + size)], fill=color)
                elif shape_type == "rectangle":
                    draw.rectangle([(x, y), (x + size, y + size)], fill=color)
                elif shape_type == "polygon":
                    points = [(x, y)]
                    for _ in range(5):
                        points.append((x + random.randint(-size, size), y + random.randint(-size, size)))
                    draw.polygon(points, fill=color)
        else:  # "classic" or default
            # Create classic design with gradient and subtle texture
            base_img = self._create_color_gradient(
                self.width, self.height,
                color1=palette[0],
                color2=palette[1],
                direction="vertical"
            )

            # Add subtle texture
            texture = self._create_noise_texture(
                self.width, self.height,
                opacity=0.1
            )

            # Convert base image to RGBA for compositing
            base_rgba = base_img.convert('RGBA')

            # Composite texture onto base image
            base_img = Image.alpha_composite(base_rgba, texture).convert('RGB')

            # Add border
            draw = ImageDraw.Draw(base_img)
            border_width = 20
            draw.rectangle(
                [(border_width, border_width),
                 (self.width - border_width, self.height - border_width)],
                outline=(255, 255, 255, 100),
                width=2
            )

        # Format title with proper capitalization
        formatted_title = self._title_case(title)

        # Draw title
        title_width = self.width - 200  # Margin
        title_lines = self._wrap_text(formatted_title, self.title_font, title_width)

        # Calculate title position (centered, upper third of cover)
        title_y = self.height // 4

        # Draw each line of the title
        for line in title_lines:
            title_bbox = ImageDraw.Draw(base_img).textbbox((0, 0), line, font=self.title_font)
            title_width = title_bbox[2] - title_bbox[0]
            title_x = (self.width - title_width) // 2

            # Add text with effects
            self._add_text_with_effects(
                base_img, line, self.title_font,
                (title_x, title_y),
                color=(255, 255, 255),
                shadow=True, emboss=True
            )

            title_y += title_bbox[3] - title_bbox[1] + 20

        # Draw subtitle if provided
        if subtitle:
            # Format subtitle with proper capitalization
            formatted_subtitle = self._title_case(subtitle)

            subtitle_lines = self._wrap_text(formatted_subtitle, self.subtitle_font, self.width - 200)
            subtitle_y = title_y + 40

            for line in subtitle_lines:
                subtitle_bbox = ImageDraw.Draw(base_img).textbbox((0, 0), line, font=self.subtitle_font)
                subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
                subtitle_x = (self.width - subtitle_width) // 2

                # Add text with effects
                self._add_text_with_effects(
                    base_img, line, self.subtitle_font,
                    (subtitle_x, subtitle_y),
                    color=(255, 255, 255),
                    shadow=True, emboss=False
                )

                subtitle_y += subtitle_bbox[3] - subtitle_bbox[1] + 10

            # Update title_y to account for subtitle
            title_y = subtitle_y + 20

        # Draw series info if provided
        if series_info and 'series_title' in series_info and 'book_number' in series_info:
            # Format series title with proper capitalization
            formatted_series_title = self._title_case(series_info['series_title'])

            # Create series text with formatted title
            series_text = f"{formatted_series_title} - Book {series_info['book_number']}"
            series_bbox = ImageDraw.Draw(base_img).textbbox((0, 0), series_text, font=self.series_font)
            series_width = series_bbox[2] - series_bbox[0]
            series_x = (self.width - series_width) // 2
            series_y = self.height - 300  # Near bottom

            # Add text with effects
            self._add_text_with_effects(
                base_img, series_text, self.series_font,
                (series_x, series_y),
                color=(255, 255, 255),
                shadow=True, emboss=False
            )

        # Draw author
        author_text = f"by {author}"
        author_bbox = ImageDraw.Draw(base_img).textbbox((0, 0), author_text, font=self.author_font)
        author_width = author_bbox[2] - author_bbox[0]
        author_x = (self.width - author_width) // 2
        author_y = self.height - 200  # Near bottom

        # Add text with effects
        self._add_text_with_effects(
            base_img, author_text, self.author_font,
            (author_x, author_y),
            color=(255, 255, 255),
            shadow=True, emboss=False
        )

        # Determine output path if not provided
        if not output_path:
            sanitized_title = title.lower().replace(' ', '_').replace("'", "").replace('"', '')
            output_filename = f"{sanitized_title}_cover.jpg"
            output_path = os.path.join(self.output_dir, output_filename)

        # Save the image
        base_img.save(output_path, quality=95)
        console.print(f"[bold green]✓[/bold green] Cover saved to {output_path}")

        return output_path
