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
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops, ImageEnhance
from rich.console import Console
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set up console for rich output
console = Console(markup=True)

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

        # Enhanced color palettes by genre with multiple variations
        self.genre_palettes = {
            "test": {
                "classic": [(50, 50, 50), (100, 100, 100), (200, 200, 200)],
                "modern": [(40, 40, 40), (120, 120, 120), (220, 220, 220)],
                "vibrant": [(60, 60, 60), (140, 140, 140), (240, 240, 240)]
            },
            "thriller": {
                "dark": [(30, 30, 30), (220, 20, 60), (200, 200, 200)],
                "noir": [(15, 15, 25), (180, 0, 40), (160, 160, 180)],
                "urban": [(40, 40, 50), (255, 69, 0), (220, 220, 230)],
                "psychological": [(25, 35, 45), (139, 69, 19), (205, 205, 215)]
            },
            "mystery": {
                "classic": [(25, 25, 45), (120, 90, 170), (220, 220, 240)],
                "cozy": [(60, 45, 30), (160, 120, 80), (240, 230, 220)],
                "gothic": [(20, 15, 30), (100, 60, 120), (180, 170, 200)],
                "modern": [(30, 40, 60), (100, 140, 200), (200, 220, 250)]
            },
            "mystery/thriller": {
                "classic": [(20, 20, 40), (180, 30, 80), (220, 220, 240)],
                "gritty": [(35, 25, 25), (160, 40, 40), (200, 180, 180)],
                "sleek": [(25, 30, 40), (120, 150, 200), (210, 220, 240)]
            },
            "science fiction": {
                "space": [(0, 20, 60), (0, 200, 255), (50, 0, 80)],
                "cyberpunk": [(10, 0, 30), (0, 255, 150), (100, 0, 150)],
                "dystopian": [(40, 40, 40), (200, 100, 0), (120, 120, 120)],
                "utopian": [(20, 60, 100), (100, 200, 255), (200, 240, 255)]
            },
            "fantasy": {
                "epic": [(50, 0, 80), (150, 100, 200), (20, 0, 40)],
                "dark": [(30, 10, 40), (100, 50, 120), (60, 30, 70)],
                "magical": [(80, 20, 100), (200, 150, 255), (40, 10, 50)],
                "nature": [(20, 60, 20), (100, 200, 100), (40, 120, 40)]
            },
            "romance": {
                "passionate": [(150, 50, 80), (240, 150, 180), (100, 20, 50)],
                "sweet": [(200, 150, 170), (255, 200, 220), (150, 100, 120)],
                "elegant": [(120, 80, 100), (200, 160, 180), (80, 50, 70)],
                "modern": [(180, 100, 120), (250, 180, 200), (120, 60, 80)]
            },
            "paranormal romance": {
                "dark": [(80, 20, 60), (180, 100, 140), (40, 10, 30)],
                "mystical": [(60, 40, 80), (160, 120, 180), (30, 20, 40)],
                "supernatural": [(40, 60, 80), (120, 180, 200), (20, 30, 40)]
            },
            "literary fiction": {
                "classic": [(50, 50, 50), (200, 200, 200), (100, 100, 100)],
                "modern": [(80, 80, 100), (160, 160, 180), (40, 40, 60)],
                "minimalist": [(120, 120, 140), (200, 200, 220), (80, 80, 100)]
            },
            "commercial fiction": {
                "urban": [(40, 70, 100), (180, 200, 220), (80, 110, 140)],
                "contemporary": [(100, 120, 140), (180, 200, 220), (50, 60, 70)],
                "artistic": [(120, 100, 140), (200, 180, 220), (70, 50, 90)]
            },
            "historical fiction": {
                "vintage": [(100, 70, 30), (200, 170, 120), (60, 40, 20)],
                "elegant": [(80, 60, 40), (160, 140, 100), (40, 30, 20)],
                "war": [(60, 50, 40), (120, 100, 80), (30, 25, 20)],
                "renaissance": [(120, 100, 60), (220, 200, 140), (60, 50, 30)]
            },
            "horror": {
                "classic": [(10, 10, 10), (120, 0, 0), (40, 0, 0)],
                "psychological": [(30, 30, 40), (100, 100, 120), (60, 60, 80)],
                "gothic": [(20, 10, 30), (80, 40, 60), (120, 100, 140)],
                "modern": [(50, 30, 30), (120, 80, 80), (180, 160, 160)]
            },
            "young adult": {
                "vibrant": [(50, 100, 200), (200, 100, 200), (100, 200, 100)],
                "contemporary": [(150, 100, 200), (220, 180, 255), (80, 50, 120)],
                "adventure": [(200, 100, 50), (255, 180, 120), (120, 60, 30)]
            },
            "middle grade": {
                "colorful": [(100, 200, 100), (200, 220, 100), (100, 180, 200)],
                "adventure": [(150, 180, 100), (220, 240, 150), (100, 140, 80)],
                "magical": [(180, 100, 200), (240, 180, 255), (120, 60, 140)]
            },
            "children's book": {
                "bright": [(255, 100, 100), (100, 200, 255), (255, 200, 100)],
                "playful": [(200, 150, 255), (150, 255, 200), (255, 200, 150)],
                "gentle": [(200, 180, 255), (180, 255, 220), (255, 220, 180)]
            },
            "self-help": {
                "professional": [(0, 100, 100), (100, 200, 200), (0, 50, 100)],
                "inspiring": [(100, 150, 200), (200, 220, 255), (50, 80, 120)],
                "calming": [(100, 120, 150), (180, 200, 230), (60, 80, 110)]
            },
            "memoir": {
                "warm": [(100, 50, 0), (200, 150, 100), (50, 25, 0)],
                "nostalgic": [(120, 80, 60), (220, 180, 140), (70, 50, 30)],
                "reflective": [(80, 70, 60), (160, 150, 130), (40, 35, 30)]
            },
            "biography": {
                "formal": [(50, 50, 0), (150, 150, 100), (100, 100, 50)],
                "inspiring": [(80, 100, 60), (160, 200, 120), (40, 60, 30)],
                "historical": [(100, 80, 60), (180, 160, 120), (60, 50, 30)]
            },
            "other": {
                "neutral": [(80, 80, 120), (180, 180, 220), (40, 40, 80)],
                "creative": [(120, 80, 140), (220, 180, 240), (60, 40, 80)],
                "professional": [(60, 80, 100), (140, 160, 180), (30, 40, 60)]
            }
        }

        # Enhanced cover design styles
        self.design_styles = [
            "gradient",
            "geometric",
            "minimalist",
            "textured",
            "abstract",
            "classic",
            "modern",
            "artistic",
            "dramatic",
            "elegant",
            "vintage",
            "bold",
            "sophisticated",
            "cinematic",
            "editorial"
        ]

        # Theme-based visual elements
        self.theme_elements = {
            "love": ["hearts", "roses", "intertwined"],
            "magic": ["stars", "mystical_symbols", "swirls"],
            "mystery": ["shadows", "keys", "magnifying_glass"],
            "adventure": ["compass", "mountains", "paths"],
            "war": ["swords", "shields", "banners"],
            "nature": ["trees", "leaves", "vines"],
            "technology": ["circuits", "gears", "digital"],
            "horror": ["skulls", "ravens", "thorns"],
            "space": ["planets", "stars", "galaxies"],
            "historical": ["ornate_borders", "vintage_frames", "scrolls"]
        }

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

    def _select_palette_variation(self, genre: str, title: str = "", description: str = "") -> List[Tuple[int, int, int]]:
        """
        Select a palette variation based on genre and content analysis.

        Args:
            genre: Book genre
            title: Book title for content analysis
            description: Book description for content analysis

        Returns:
            List of RGB color tuples
        """
        genre_lower = genre.lower()

        # Get genre palettes or default
        if genre_lower in self.genre_palettes:
            genre_palettes = self.genre_palettes[genre_lower]
        else:
            genre_palettes = self.genre_palettes["other"]

        # Analyze content for mood/theme
        content_text = f"{title} {description}".lower()

        # Content-based palette selection
        if any(word in content_text for word in ["dark", "shadow", "night", "death", "evil", "black"]):
            # Prefer darker variations
            preferred_variations = ["dark", "noir", "gothic", "psychological", "classic"]
        elif any(word in content_text for word in ["bright", "light", "hope", "joy", "happy", "love"]):
            # Prefer lighter/brighter variations
            preferred_variations = ["sweet", "vibrant", "modern", "inspiring", "bright"]
        elif any(word in content_text for word in ["war", "battle", "fight", "conflict", "struggle"]):
            # Prefer dramatic variations
            preferred_variations = ["gritty", "war", "dramatic", "urban", "classic"]
        elif any(word in content_text for word in ["magic", "mystical", "supernatural", "fantasy"]):
            # Prefer magical variations
            preferred_variations = ["magical", "mystical", "supernatural", "epic"]
        else:
            # Default to any variation
            preferred_variations = list(genre_palettes.keys())

        # Select variation based on preference
        for variation in preferred_variations:
            if variation in genre_palettes:
                return genre_palettes[variation]

        # Fallback to first available variation
        return list(genre_palettes.values())[0]

    def _analyze_content_themes(self, title: str, description: str = "") -> List[str]:
        """
        Analyze content to identify themes for visual elements.

        Args:
            title: Book title
            description: Book description

        Returns:
            List of identified themes
        """
        content_text = f"{title} {description}".lower()
        identified_themes = []

        # Theme keyword mapping
        theme_keywords = {
            "love": ["love", "romance", "heart", "passion", "relationship", "wedding", "kiss"],
            "magic": ["magic", "magical", "wizard", "witch", "spell", "enchant", "mystical"],
            "mystery": ["mystery", "detective", "clue", "secret", "hidden", "investigate"],
            "adventure": ["adventure", "journey", "quest", "explore", "travel", "discover"],
            "war": ["war", "battle", "fight", "soldier", "conflict", "army", "weapon"],
            "nature": ["forest", "tree", "mountain", "river", "nature", "wild", "garden"],
            "technology": ["technology", "robot", "cyber", "digital", "future", "machine"],
            "horror": ["horror", "scary", "fear", "ghost", "demon", "nightmare", "terror"],
            "space": ["space", "star", "planet", "galaxy", "alien", "cosmic", "universe"],
            "historical": ["historical", "ancient", "medieval", "victorian", "period", "past"]
        }

        # Identify themes based on keywords
        for theme, keywords in theme_keywords.items():
            if any(keyword in content_text for keyword in keywords):
                identified_themes.append(theme)

        return identified_themes

    def _process_provided_themes(self, themes: List[str]) -> List[str]:
        """
        Process provided themes to extract visual theme keywords.

        Args:
            themes: List of theme strings from novel data or genre defaults

        Returns:
            List of processed theme keywords for visual elements
        """
        if not themes:
            return []

        processed_themes = []

        # Map complex theme descriptions to visual theme keywords
        theme_mapping = {
            # Romance themes
            "love": ["love", "romance", "hearts"],
            "relationships": ["love", "romance", "hearts"],
            "unspoken love": ["love", "romance", "mystery"],
            "emotional sacrifice": ["love", "drama"],
            "communication beyond words": ["love", "mystery"],
            "cultural identity": ["historical", "family"],
            "family expectations": ["family", "historical"],
            "personal growth": ["nature", "adventure"],
            "modern love": ["love", "contemporary"],
            "career vs relationships": ["love", "contemporary"],

            # Fantasy themes
            "good vs evil": ["magic", "war"],
            "power": ["magic", "war"],
            "magic": ["magic"],
            "supernatural": ["magic"],

            # Mystery/Thriller themes
            "secrets": ["mystery"],
            "deception": ["mystery"],
            "justice": ["mystery", "war"],

            # General themes
            "identity": ["adventure"],
            "self-discovery": ["adventure", "nature"],
            "survival": ["adventure", "war"],
            "technology": ["technology"],
            "space": ["space"],
            "historical": ["historical"],
            "nature": ["nature"],
            "horror": ["horror"],
        }

        for theme in themes:
            theme_lower = theme.lower()

            # Check for direct matches or partial matches
            for key, visual_themes in theme_mapping.items():
                if key in theme_lower or any(word in theme_lower for word in key.split()):
                    processed_themes.extend(visual_themes)

        # Remove duplicates while preserving order
        seen = set()
        unique_themes = []
        for theme in processed_themes:
            if theme not in seen:
                seen.add(theme)
                unique_themes.append(theme)

        return unique_themes

    def _get_genre_default_themes(self, genre: str) -> List[str]:
        """
        Get default themes for a genre as fallback.

        Args:
            genre: Book genre

        Returns:
            List of default visual themes for the genre
        """
        genre_theme_defaults = {
            "romance": ["love", "romance"],
            "contemporary romance": ["love", "romance"],
            "fantasy": ["magic", "adventure"],
            "mystery": ["mystery"],
            "thriller": ["mystery", "adventure"],
            "science fiction": ["technology", "space"],
            "historical fiction": ["historical"],
            "horror": ["horror"],
            "adventure": ["adventure"],
            "literary fiction": ["nature"],
        }

        genre_lower = genre.lower()
        for key, themes in genre_theme_defaults.items():
            if key in genre_lower or genre_lower in key:
                return themes

        return []

    def _create_advanced_gradient(self, width: int, height: int, colors: List[Tuple[int, int, int]],
                                  style: str = "linear") -> Image.Image:
        """Create sophisticated gradient backgrounds."""
        if style == "radial":
            # Create radial gradient with multiple color stops
            center_x, center_y = width // 2, height // 2
            max_radius = math.sqrt(center_x ** 2 + center_y ** 2)

            gradient = np.zeros((height, width, 3), dtype=np.uint8)

            for y in range(height):
                for x in range(width):
                    distance = math.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
                    ratio = min(distance / max_radius, 1.0)

                    # Interpolate between colors
                    if len(colors) >= 3:
                        if ratio < 0.5:
                            t = ratio * 2
                            r = int(colors[0][0] * (1 - t) + colors[1][0] * t)
                            g = int(colors[0][1] * (1 - t) + colors[1][1] * t)
                            b = int(colors[0][2] * (1 - t) + colors[1][2] * t)
                        else:
                            t = (ratio - 0.5) * 2
                            r = int(colors[1][0] * (1 - t) + colors[2][0] * t)
                            g = int(colors[1][1] * (1 - t) + colors[2][1] * t)
                            b = int(colors[1][2] * (1 - t) + colors[2][2] * t)
                    else:
                        r = int(colors[0][0] * (1 - ratio) + colors[1][0] * ratio)
                        g = int(colors[0][1] * (1 - ratio) + colors[1][1] * ratio)
                        b = int(colors[0][2] * (1 - ratio) + colors[1][2] * ratio)

                    gradient[y, x] = [r, g, b]

            return Image.fromarray(gradient, 'RGB')

        elif style == "angular":
            # Create angular/diamond gradient
            gradient = np.zeros((height, width, 3), dtype=np.uint8)
            center_x, center_y = width // 2, height // 2

            for y in range(height):
                for x in range(width):
                    # Calculate angular distance
                    dx = abs(x - center_x) / (width / 2)
                    dy = abs(y - center_y) / (height / 2)
                    ratio = min(max(dx, dy), 1.0)

                    r = int(colors[0][0] * (1 - ratio) + colors[1][0] * ratio)
                    g = int(colors[0][1] * (1 - ratio) + colors[1][1] * ratio)
                    b = int(colors[0][2] * (1 - ratio) + colors[1][2] * ratio)

                    gradient[y, x] = [r, g, b]

            return Image.fromarray(gradient, 'RGB')

        elif style == "conic":
            # Create conic/spiral gradient
            gradient = np.zeros((height, width, 3), dtype=np.uint8)
            center_x, center_y = width // 2, height // 2

            for y in range(height):
                for x in range(width):
                    angle = math.atan2(y - center_y, x - center_x)
                    ratio = (angle + math.pi) / (2 * math.pi)  # Normalize to 0-1

                    # Create smooth color transitions
                    color_index = ratio * (len(colors) - 1)
                    idx = int(color_index)
                    t = color_index - idx

                    if idx >= len(colors) - 1:
                        color = colors[-1]
                    else:
                        color1, color2 = colors[idx], colors[idx + 1]
                        r = int(color1[0] * (1 - t) + color2[0] * t)
                        g = int(color1[1] * (1 - t) + color2[1] * t)
                        b = int(color1[2] * (1 - t) + color2[2] * t)
                        color = (r, g, b)

                    gradient[y, x] = color

            return Image.fromarray(gradient, 'RGB')

        else:  # linear gradient (default)
            gradient = np.linspace(0, 1, max(width, height))
            if len(colors) >= 3:
                # Multi-stop gradient
                r = np.interp(gradient, [0, 0.5, 1], [colors[0][0], colors[1][0], colors[2][0]])
                g = np.interp(gradient, [0, 0.5, 1], [colors[0][1], colors[1][1], colors[2][1]])
                b = np.interp(gradient, [0, 0.5, 1], [colors[0][2], colors[1][2], colors[2][2]])
            else:
                r = np.interp(gradient, [0, 1], [colors[0][0], colors[1][0]])
                g = np.interp(gradient, [0, 1], [colors[0][1], colors[1][1]])
                b = np.interp(gradient, [0, 1], [colors[0][2], colors[1][2]])

            gradient_img = np.zeros((height, width, 3), dtype=np.uint8)
            for i in range(height):
                idx = int(i * len(gradient) / height)
                gradient_img[i, :] = [r[idx], g[idx], b[idx]]

            return Image.fromarray(gradient_img, 'RGB')

    def _create_sophisticated_shapes(self, width: int, height: int, colors: List[Tuple[int, int, int]],
                                     shape_type: str = "flowing") -> Image.Image:
        """Create sophisticated geometric and organic shapes."""
        img = Image.new('RGB', (width, height), colors[0])

        if shape_type == "flowing":
            # Create flowing, organic shapes using Bezier-like curves
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)

            num_shapes = random.randint(8, 15)
            for _ in range(num_shapes):
                # Generate organic blob shapes
                center_x = random.randint(width // 4, 3 * width // 4)
                center_y = random.randint(height // 4, 3 * height // 4)

                points = []
                num_points = random.randint(6, 12)
                base_radius = random.randint(100, 300)

                for i in range(num_points):
                    angle = (2 * math.pi * i) / num_points
                    # Add organic variation to radius
                    variation = random.uniform(0.6, 1.4)
                    radius = base_radius * variation

                    x = center_x + int(radius * math.cos(angle))
                    y = center_y + int(radius * math.sin(angle))
                    points.append((x, y))

                color = random.choice(colors[1:])
                alpha = random.randint(30, 120)
                draw.polygon(points, fill=(*color, alpha))

            # Apply blur for smoother shapes
            overlay = overlay.filter(ImageFilter.GaussianBlur(radius=8))
            img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

        elif shape_type == "crystalline":
            # Create crystalline/faceted shapes
            draw = ImageDraw.Draw(img)

            num_crystals = random.randint(12, 25)
            for _ in range(num_crystals):
                center_x = random.randint(0, width)
                center_y = random.randint(0, height)

                # Create angular crystal shapes
                points = []
                num_sides = random.randint(5, 8)
                base_size = random.randint(80, 200)

                for i in range(num_sides):
                    angle = (2 * math.pi * i) / num_sides + random.uniform(-0.3, 0.3)
                    distance = base_size * random.uniform(0.7, 1.3)

                    x = center_x + int(distance * math.cos(angle))
                    y = center_y + int(distance * math.sin(angle))
                    points.append((x, y))

                color = random.choice(colors[1:])
                draw.polygon(points, fill=color)

        elif shape_type == "waves":
            # Create wave patterns
            draw = ImageDraw.Draw(img)

            num_waves = random.randint(5, 10)
            for wave in range(num_waves):
                y_base = (height * wave) // num_waves
                amplitude = random.randint(50, 150)
                frequency = random.uniform(0.005, 0.02)
                phase = random.uniform(0, 2 * math.pi)

                points = []
                for x in range(0, width, 10):
                    y = y_base + int(amplitude * math.sin(frequency * x + phase))
                    points.append((x, y))

                # Create wave shape
                wave_points = [(0, height)] + points + [(width, height)]
                color = colors[1] if wave % 2 == 0 else colors[2]
                draw.polygon(wave_points, fill=color)

        elif shape_type == "spiral":
            # Create spiral patterns
            draw = ImageDraw.Draw(img)

            center_x, center_y = width // 2, height // 2
            max_radius = min(width, height) // 3

            for spiral in range(3):
                points = []
                color = colors[1 + spiral % 2]

                for t in range(0, 720, 5):  # Two full rotations
                    angle = math.radians(t)
                    radius = (max_radius * t) / 720

                    x = center_x + int(radius * math.cos(angle + spiral * math.pi / 3))
                    y = center_y + int(radius * math.sin(angle + spiral * math.pi / 3))
                    points.append((x, y))

                # Draw thick spiral line
                for i in range(len(points) - 1):
                    draw.line([points[i], points[i + 1]], fill=color, width=8)

        return img

    def _add_sophisticated_texture(self, img: Image.Image, texture_type: str = "paper") -> Image.Image:
        """Add sophisticated texture overlays."""
        width, height = img.size

        if texture_type == "paper":
            # Create paper-like texture
            noise = np.random.rand(height, width) * 0.4 + 0.8
            paper_texture = (noise * 255).astype(np.uint8)

            # Add paper grain pattern
            grain_size = 3
            for y in range(0, height, grain_size):
                for x in range(0, width, grain_size):
                    if random.random() < 0.1:  # Sparse grain
                        end_y = min(y + grain_size, height)
                        end_x = min(x + grain_size, width)
                        paper_texture[y:end_y, x:end_x] = (paper_texture[y:end_y, x:end_x] * 0.9).astype(np.uint8)

            texture_img = Image.fromarray(paper_texture, 'L')
            texture_img = texture_img.convert('RGB')

            # Blend with original
            blended = ImageChops.multiply(img, texture_img)
            return Image.blend(img, blended, 0.3)

        elif texture_type == "canvas":
            # Create canvas texture
            canvas = np.ones((height, width), dtype=np.float32)

            # Add canvas weave pattern
            weave_size = 4
            for y in range(0, height, weave_size):
                for x in range(0, width, weave_size):
                    if (x // weave_size + y // weave_size) % 2:
                        canvas[y:y + weave_size, x:x + weave_size] *= 0.95

            # Add random variations
            canvas += np.random.normal(0, 0.02, (height, width))
            canvas = np.clip(canvas, 0.8, 1.0)

            canvas_img = Image.fromarray((canvas * 255).astype(np.uint8), 'L').convert('RGB')
            blended = ImageChops.multiply(img, canvas_img)
            return Image.blend(img, blended, 0.4)

        elif texture_type == "metallic":
            # Create metallic texture
            metallic = np.random.rand(height, width) * 0.3 + 0.85

            # Add metallic streaks
            for _ in range(height // 20):
                y = random.randint(0, height - 1)
                streak_length = random.randint(width // 4, width)
                streak_start = random.randint(0, width - streak_length)
                intensity = random.uniform(0.9, 1.1)

                metallic[y, streak_start:streak_start + streak_length] *= intensity

            metallic_img = Image.fromarray((metallic * 255).astype(np.uint8), 'L').convert('RGB')

            # Add metallic tint
            enhancer = ImageEnhance.Brightness(metallic_img)
            metallic_img = enhancer.enhance(1.2)

            blended = ImageChops.screen(img, metallic_img)
            return Image.blend(img, blended, 0.25)

        else:  # subtle texture
            # Create subtle noise texture
            noise = np.random.rand(height, width) * 0.1 + 0.95
            texture_img = Image.fromarray((noise * 255).astype(np.uint8), 'L').convert('RGB')
            blended = ImageChops.multiply(img, texture_img)
            return Image.blend(img, blended, 0.15)

    def _create_advanced_background(self, width: int, height: int, palette: List[Tuple[int, int, int]],
                                   style: str, themes: List[str] = None) -> Image.Image:
        """
        Create advanced background with theme-based elements.

        Args:
            width: Image width
            height: Image height
            palette: Color palette
            style: Design style
            themes: Identified themes

        Returns:
            PIL Image with advanced background
        """
        themes = themes or []

        if style == "modern":
            # Modern design with advanced gradients
            gradient_style = random.choice(["angular", "linear", "radial"])
            base_img = self._create_advanced_gradient(width, height, palette, gradient_style)

            # Add modern geometric elements
            draw = ImageDraw.Draw(base_img)
            for i in range(3):
                x = random.randint(width//4, 3*width//4)
                y = random.randint(height//4, 3*height//4)
                size = random.randint(50, 200)
                draw.rectangle([(x, y), (x + size, y + size//4)], fill=palette[2])

        elif style == "artistic":
            # Artistic design with sophisticated flowing shapes
            shape_type = random.choice(["flowing", "waves", "spiral"])
            base_img = self._create_sophisticated_shapes(width, height, palette, shape_type)

            # Add sophisticated texture
            texture_type = random.choice(["canvas", "paper"])
            base_img = self._add_sophisticated_texture(base_img, texture_type)

        elif style == "dramatic":
            # Dramatic design with advanced gradients and crystalline shapes
            base_img = self._create_advanced_gradient(width, height, palette, "radial")

            # Add crystalline dramatic elements
            crystalline_overlay = self._create_sophisticated_shapes(width, height, palette, "crystalline")
            base_img = Image.blend(base_img, crystalline_overlay, 0.3)

            # Add metallic texture for drama
            base_img = self._add_sophisticated_texture(base_img, "metallic")

        elif style == "elegant":
            # Elegant design with conic gradients and paper texture
            base_img = self._create_advanced_gradient(width, height, palette, "conic")

            # Add elegant paper texture
            base_img = self._add_sophisticated_texture(base_img, "paper")

            # Add elegant border
            draw = ImageDraw.Draw(base_img)
            border_width = 30
            for i in range(5):
                draw.rectangle(
                    [(border_width + i*2, border_width + i*2),
                     (width - border_width - i*2, height - border_width - i*2)],
                    outline=palette[2], width=2
                )

        elif style == "vintage":
            # Vintage design with sophisticated textures
            base_img = self._create_advanced_gradient(width, height, palette, "linear")

            # Add vintage canvas texture
            base_img = self._add_sophisticated_texture(base_img, "canvas")

            # Add vintage frame
            draw = ImageDraw.Draw(base_img)
            frame_width = 40
            draw.rectangle(
                [(frame_width, frame_width), (width - frame_width, height - frame_width)],
                outline=palette[2], width=8
            )

        elif style == "bold":
            # Bold design with crystalline shapes
            base_img = self._create_sophisticated_shapes(width, height, palette, "crystalline")

            # Add bold geometric overlays
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            draw = ImageDraw.Draw(overlay)

            for _ in range(5):
                x = random.randint(0, width)
                y = random.randint(0, height)
                size = random.randint(100, 300)
                color = (*random.choice([palette[1], palette[2]]), 120)

                shape_type = random.choice(["rectangle", "ellipse"])
                if shape_type == "rectangle":
                    draw.rectangle([(x, y), (x + size, y + size//2)], fill=color)
                else:
                    draw.ellipse([(x, y), (x + size, y + size)], fill=color)

            base_img = Image.alpha_composite(base_img.convert('RGBA'), overlay).convert('RGB')

        elif style == "sophisticated":
            # Sophisticated design with multiple advanced techniques
            base_img = self._create_advanced_gradient(width, height, palette, "conic")

            # Add flowing shapes overlay
            flowing_overlay = self._create_sophisticated_shapes(width, height, palette, "flowing")
            base_img = Image.blend(base_img, flowing_overlay, 0.4)

            # Add sophisticated paper texture
            base_img = self._add_sophisticated_texture(base_img, "paper")

        elif style == "cinematic":
            # Cinematic design with dramatic lighting
            base_img = self._create_advanced_gradient(width, height, palette, "radial")

            # Add wave patterns for cinematic feel
            wave_overlay = self._create_sophisticated_shapes(width, height, palette, "waves")
            base_img = Image.blend(base_img, wave_overlay, 0.3)

            # Add metallic texture for cinematic sheen
            base_img = self._add_sophisticated_texture(base_img, "metallic")

        elif style == "editorial":
            # Editorial design with clean, professional look
            base_img = self._create_advanced_gradient(width, height, palette, "angular")

            # Add subtle canvas texture
            base_img = self._add_sophisticated_texture(base_img, "canvas")

            # Add clean geometric elements
            draw = ImageDraw.Draw(base_img)
            for i in range(2):
                x = width // 4 + i * (width // 2)
                y = height // 6
                width_rect = width // 8
                height_rect = height // 3
                draw.rectangle([(x, y), (x + width_rect, y + height_rect)], fill=palette[2])

        else:
            # Fallback to advanced gradient
            gradient_style = random.choice(["linear", "radial", "angular"])
            base_img = self._create_advanced_gradient(width, height, palette, gradient_style)

        return base_img

    def generate_cover(self, title: str, author: str, genre: str = "fantasy",
                      subtitle: str = None, series_info: Dict[str, Any] = None,
                      design_style: str = None, output_path: Optional[str] = None,
                      description: str = "", themes: List[str] = None) -> str:
        """
        Generate an enhanced cover for a book with advanced variations.

        Args:
            title: Book title
            author: Author name
            genre: Book genre (used for color palette selection)
            subtitle: Book subtitle (optional)
            series_info: Series information (optional) - dict with keys 'series_title' and 'book_number'
            design_style: Cover design style (optional) - one of the enhanced styles
            output_path: Path to save the cover image, if None generates a path
            description: Book description for content analysis (optional)
            themes: List of themes from novel data, genre defaults, or series config (optional)

        Returns:
            Path to the generated cover image
        """
        console.print(f"[bold cyan]Generating enhanced cover for '[/bold cyan][bold yellow]{title}[/bold yellow][bold cyan]' by {author}[/bold cyan]")

        # Use provided themes or analyze content for intelligent palette and style selection
        if themes:
            # Use provided themes (from genre defaults, series config, or novel data)
            detected_themes = self._process_provided_themes(themes)
            console.print(f"[dim]Using provided themes: {', '.join(detected_themes) if detected_themes else 'None'}[/dim]")
        else:
            # Fallback to content analysis
            detected_themes = self._analyze_content_themes(title, description)
            console.print(f"[dim]Detected themes from content: {', '.join(detected_themes) if detected_themes else 'None'}[/dim]")

        # If no themes detected, try to get genre default themes as final fallback
        if not detected_themes:
            detected_themes = self._get_genre_default_themes(genre)
            if detected_themes:
                console.print(f"[dim]Using genre default themes: {', '.join(detected_themes)}[/dim]")
            else:
                console.print(f"[dim]No themes available for cover generation[/dim]")

        # Select palette variation based on content analysis
        palette = self._select_palette_variation(genre, title, description)
        console.print(f"[dim]Selected palette variation for {genre}[/dim]")

        # Choose design style if not specified, with content-aware selection
        if not design_style:
            # Content-aware style selection
            content_text = f"{title} {description}".lower()

            if any(word in content_text for word in ["modern", "contemporary", "urban", "city"]):
                style_preferences = ["modern", "bold", "geometric", "minimalist"]
            elif any(word in content_text for word in ["historical", "vintage", "classic", "period"]):
                style_preferences = ["vintage", "elegant", "classic", "textured"]
            elif any(word in content_text for word in ["art", "creative", "beautiful", "aesthetic"]):
                style_preferences = ["artistic", "elegant", "abstract", "gradient"]
            elif any(word in content_text for word in ["dark", "intense", "dramatic", "powerful"]):
                style_preferences = ["dramatic", "bold", "abstract", "textured"]
            else:
                style_preferences = self.design_styles

            design_style = random.choice(style_preferences)
            console.print(f"[dim]Auto-selected style: {design_style}[/dim]")

        # Create base image using enhanced background generation
        if design_style in ["modern", "artistic", "dramatic", "elegant", "vintage", "bold"]:
            # Use advanced background creation for new styles
            base_img = self._create_advanced_background(
                self.width, self.height, palette, design_style, detected_themes
            )
        elif design_style == "gradient":
            # Enhanced gradient with more variation
            gradient_direction = random.choice(["vertical", "horizontal", "diagonal", "radial"])
            base_img = self._create_color_gradient(
                self.width, self.height,
                color1=palette[0],
                color2=palette[1],
                direction=gradient_direction
            )

            # Add subtle overlay for more depth
            if random.choice([True, False]):
                overlay = self._create_noise_texture(self.width, self.height, opacity=0.1)
                base_img = Image.alpha_composite(base_img.convert('RGBA'), overlay).convert('RGB')

        elif design_style == "geometric":
            # Enhanced geometric patterns with more variety
            pattern_types = ["triangles", "squares", "circles", "lines", "hexagons", "diamonds"]
            pattern_type = random.choice(pattern_types)

            if pattern_type in ["hexagons", "diamonds"]:
                # Create custom patterns for new types
                base_img = Image.new('RGB', (self.width, self.height), palette[0])
                draw = ImageDraw.Draw(base_img)

                if pattern_type == "hexagons":
                    # Create hexagonal pattern
                    hex_size = 80
                    for x in range(-hex_size, self.width + hex_size, hex_size * 2):
                        for y in range(-hex_size, self.height + hex_size, int(hex_size * 1.5)):
                            offset_x = hex_size if (y // int(hex_size * 1.5)) % 2 == 0 else 0
                            center_x, center_y = x + offset_x, y

                            # Draw hexagon
                            points = []
                            for angle in range(0, 360, 60):
                                px = center_x + int(hex_size * 0.5 * np.cos(np.radians(angle)))
                                py = center_y + int(hex_size * 0.5 * np.sin(np.radians(angle)))
                                points.append((px, py))

                            if len(points) >= 3:
                                draw.polygon(points, fill=palette[1])

                elif pattern_type == "diamonds":
                    # Create diamond pattern
                    diamond_size = 100
                    for x in range(0, self.width, diamond_size):
                        for y in range(0, self.height, diamond_size):
                            center_x, center_y = x + diamond_size//2, y + diamond_size//2
                            points = [
                                (center_x, center_y - diamond_size//2),
                                (center_x + diamond_size//2, center_y),
                                (center_x, center_y + diamond_size//2),
                                (center_x - diamond_size//2, center_y)
                            ]
                            draw.polygon(points, fill=palette[1])
            else:
                # Use existing geometric pattern method
                base_img = self._create_geometric_pattern(
                    self.width, self.height,
                    color1=palette[0],
                    color2=palette[1],
                    pattern_type=pattern_type
                )

        elif design_style == "minimalist":
            # Enhanced minimalist with more sophisticated elements
            base_img = Image.new('RGB', (self.width, self.height), palette[0])
            draw = ImageDraw.Draw(base_img)

            # Add sophisticated minimal elements
            element_type = random.choice(["line", "circle", "rectangle", "triangle"])

            if element_type == "line":
                # Add elegant lines
                for i in range(3):
                    y_pos = self.height // 4 + i * (self.height // 6)
                    draw.line([(100, y_pos), (self.width - 100, y_pos)], fill=palette[1], width=3)
            elif element_type == "circle":
                # Add elegant circle
                circle_size = min(self.width, self.height) // 6
                center_x, center_y = self.width - 150, 150
                draw.ellipse(
                    [(center_x - circle_size, center_y - circle_size),
                     (center_x + circle_size, center_y + circle_size)],
                    outline=palette[1], width=5
                )
            else:
                # Add geometric accent
                accent_size = min(self.width, self.height) // 4
                accent_pos = (self.width - accent_size - 100, 100)
                draw.rectangle(
                    [accent_pos, (accent_pos[0] + accent_size, accent_pos[1] + accent_size)],
                    fill=palette[1]
                )

        elif design_style == "textured":
            # Enhanced textured background
            base_img = self._create_color_gradient(
                self.width, self.height,
                color1=palette[0],
                color2=palette[1],
                direction=random.choice(["vertical", "diagonal"])
            )

            # Add varied texture intensity
            texture_opacity = random.uniform(0.2, 0.5)
            texture = self._create_noise_texture(
                self.width, self.height,
                opacity=texture_opacity
            )

            base_img = Image.alpha_composite(base_img.convert('RGBA'), texture).convert('RGB')

        elif design_style == "abstract":
            # Enhanced abstract with more sophisticated shapes
            base_img = Image.new('RGB', (self.width, self.height), palette[0])
            draw = ImageDraw.Draw(base_img)

            # Add varied abstract shapes
            num_shapes = random.randint(15, 25)
            for _ in range(num_shapes):
                shape_type = random.choice(["circle", "rectangle", "polygon", "arc", "bezier"])
                color = random.choice([palette[1], palette[2]])
                x = random.randint(-100, self.width + 100)
                y = random.randint(-100, self.height + 100)
                size = random.randint(50, 300)

                alpha = random.randint(100, 255)
                color_with_alpha = (*color, alpha)

                if shape_type == "circle":
                    draw.ellipse([(x, y), (x + size, y + size)], fill=color)
                elif shape_type == "rectangle":
                    angle = random.randint(0, 45)
                    draw.rectangle([(x, y), (x + size, y + size//2)], fill=color)
                elif shape_type == "arc":
                    start_angle = random.randint(0, 180)
                    end_angle = start_angle + random.randint(90, 180)
                    draw.arc([(x, y), (x + size, y + size)], start_angle, end_angle, fill=color, width=10)
                else:
                    # Polygon
                    points = [(x, y)]
                    for _ in range(random.randint(3, 6)):
                        points.append((x + random.randint(-size, size), y + random.randint(-size, size)))
                    if len(points) >= 3:
                        draw.polygon(points, fill=color)

        else:  # "classic" or default
            # Enhanced classic design
            base_img = self._create_color_gradient(
                self.width, self.height,
                color1=palette[0],
                color2=palette[1],
                direction="vertical"
            )

            # Add sophisticated texture
            texture = self._create_noise_texture(
                self.width, self.height,
                opacity=0.15
            )

            base_img = Image.alpha_composite(base_img.convert('RGBA'), texture).convert('RGB')

            # Add elegant border
            draw = ImageDraw.Draw(base_img)
            border_width = 25
            for i in range(3):
                draw.rectangle(
                    [(border_width + i*5, border_width + i*5),
                     (self.width - border_width - i*5, self.height - border_width - i*5)],
                    outline=palette[2],
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
