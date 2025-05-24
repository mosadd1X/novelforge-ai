"""
Gemini-enhanced cover prompt generator for creating detailed AI cover prompts.
"""
import os
import json
from typing import Dict, Any, List, Optional
from datetime import datetime
from rich.console import Console

console = Console(markup=True)


class CoverPromptGenerator:
    """
    Generates detailed AI cover prompts using Gemini AI analysis of book content.
    """

    def __init__(self):
        """Initialize the Gemini-enhanced cover prompt generator."""
        self.gemini_client = None
        self._initialize_gemini_client()

        # Typography and design guidelines for prompt generation
        self.typography_styles = {
            "serif": "classic serif fonts like Times New Roman, Garamond, or Baskerville for traditional elegance",
            "sans_serif": "clean sans-serif fonts like Helvetica, Arial, or Futura for modern appeal",
            "display": "bold display fonts like Impact, Bebas Neue, or Oswald for dramatic impact",
            "script": "elegant script fonts like Brush Script or Dancing Script for romantic or artistic feel",
            "decorative": "ornate decorative fonts like Cinzel or Playfair Display for fantasy or historical themes"
        }

        # Visual style categories for prompt enhancement
        self.visual_styles = {
            "photorealistic": "photorealistic, highly detailed, professional photography style",
            "digital_art": "digital art, concept art style, polished and refined",
            "illustration": "artistic illustration, hand-drawn style, creative interpretation",
            "painterly": "painterly style, brushstroke textures, artistic rendering",
            "cinematic": "cinematic composition, dramatic lighting, movie poster style"
        }

    def _initialize_gemini_client(self):
        """Initialize the Gemini client for AI analysis."""
        try:
            from src.core.resilient_gemini_client import ResilientGeminiClient
            self.gemini_client = ResilientGeminiClient()
            console.print("[dim]Gemini client initialized for cover prompt generation[/dim]")
        except Exception as e:
            console.print(f"[yellow]Warning: Could not initialize Gemini client: {str(e)}[/yellow]")
            self.gemini_client = None

    def generate_cover_prompt(self, novel_data: Dict[str, Any], output_dir: str,
                            series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a detailed cover prompt using Gemini AI analysis of book content.

        Args:
            novel_data: Dictionary containing novel data
            output_dir: Directory where the prompt will be saved
            series_info: Optional series information

        Returns:
            Path to the saved cover prompt file
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")
        author = metadata.get("author", "Unknown Author")
        genre = metadata.get("genre", "fiction")

        console.print("[bold cyan]Analyzing book content with Gemini AI...[/bold cyan]")

        # Create series cover folders if this is a series book
        if series_info:
            self._create_series_cover_folders(series_info)

        if self.gemini_client:
            try:
                # Use Gemini AI to create the complete prompt document with exact response
                prompt_document = self._create_gemini_prompt_document(novel_data, series_info)

                console.print("[bold green]✓[/bold green] Gemini AI analysis complete")

            except Exception as e:
                console.print(f"[yellow]Warning: Gemini analysis failed, using enhanced fallback: {str(e)}[/yellow]")
                prompt_document = self._create_enhanced_fallback_prompt(novel_data, series_info)
        else:
            console.print("[yellow]Gemini client not available, using enhanced fallback method[/yellow]")
            prompt_document = self._create_enhanced_fallback_prompt(novel_data, series_info)

        # Save the prompt to file
        prompt_path = self._save_prompt_to_file(prompt_document, output_dir, title)

        console.print(f"[bold green]✓[/bold green] AI-enhanced cover prompt generated: [bold cyan]{prompt_path}[/bold cyan]")

        return prompt_path



    def _prepare_book_content_for_analysis(self, novel_data: Dict[str, Any]) -> str:
        """
        Prepare book content for Gemini analysis, including key information.

        Args:
            novel_data: Complete novel data

        Returns:
            Formatted string containing book content for analysis
        """
        content_parts = []

        # Add metadata
        metadata = novel_data.get("metadata", {})
        content_parts.append(f"TITLE: {metadata.get('title', 'Untitled')}")
        content_parts.append(f"AUTHOR: {metadata.get('author', 'Unknown')}")
        content_parts.append(f"GENRE: {metadata.get('genre', 'Fiction')}")
        content_parts.append(f"DESCRIPTION: {metadata.get('description', '')}")
        content_parts.append("")

        # Add character information
        characters = novel_data.get("characters", [])
        if characters:
            content_parts.append("MAIN CHARACTERS:")
            for char in characters[:5]:  # Limit to top 5 characters
                if isinstance(char, dict):
                    name = char.get("name", "Unknown")
                    role = char.get("role", "")
                    appearance = char.get("appearance", "")
                    personality = char.get("personality", "")
                    background = char.get("background", "")

                    char_info = f"- {name}"
                    if role:
                        char_info += f" ({role})"
                    if appearance:
                        char_info += f": {appearance}"
                    if personality:
                        char_info += f" | Personality: {personality}"
                    if background:
                        char_info += f" | Background: {background}"

                    content_parts.append(char_info)
            content_parts.append("")

        # Add chapter summaries (first few chapters for context)
        chapters = novel_data.get("chapters", [])
        if chapters:
            content_parts.append("STORY CONTENT (Key Chapters):")

            # Include first chapter, middle chapter, and last chapter for story arc
            key_chapters = []
            if len(chapters) >= 1:
                key_chapters.append(chapters[0])  # First chapter
            if len(chapters) >= 3:
                key_chapters.append(chapters[len(chapters)//2])  # Middle chapter
            if len(chapters) >= 2:
                key_chapters.append(chapters[-1])  # Last chapter

            for i, chapter in enumerate(key_chapters):
                if isinstance(chapter, dict):
                    title = chapter.get("title", f"Chapter {i+1}")
                    content = chapter.get("content", "")

                    # Limit content length for analysis
                    if len(content) > 2000:
                        content = content[:2000] + "..."

                    content_parts.append(f"\n{title}:")
                    content_parts.append(content)
                    content_parts.append("")

        return "\n".join(content_parts)

    def _get_series_visual_guidelines(self, series_info: Dict[str, Any]) -> str:
        """
        Generate series visual consistency guidelines for Gemini AI.

        Args:
            series_info: Series information including title and book number

        Returns:
            Formatted series guidelines for consistent visual design
        """
        if not series_info:
            return ""

        series_title = series_info.get('series_title', 'Unknown Series')
        book_number = series_info.get('book_number', 1)

        # Load existing series data if available
        series_data = self._load_series_data(series_title)

        guidelines = f"""
        SERIES VISUAL CONSISTENCY REQUIREMENTS:
        - Series: {series_title} (Book {book_number})
        - This cover must maintain visual consistency with other books in the series
        - Use consistent color palette, typography style, and composition approach
        - Ensure covers work together as a cohesive set while maintaining individual identity

        SERIES DESIGN STANDARDS:
        """

        if series_data and book_number > 1:
            # Add specific consistency requirements based on previous books
            guidelines += f"""
        - Maintain the established visual theme from previous books
        - Use consistent character positioning and perspective approaches
        - Keep similar lighting techniques and atmospheric mood
        - Ensure typography style matches the series standard
        - Use complementary colors that work with the series palette
        - Maintain consistent symbolic elements and thematic motifs
        """
        else:
            # First book - establish series visual standards
            guidelines += f"""
        - Establish the visual foundation for the entire series
        - Create a distinctive color palette that can be adapted across books
        - Set typography standards that will work for all series titles
        - Define composition and lighting approaches for series consistency
        - Establish symbolic elements and visual themes for the series
        """

        return guidelines

    def _load_series_data(self, series_title: str) -> Optional[Dict[str, Any]]:
        """
        Load existing series data for visual consistency.

        Args:
            series_title: Title of the series

        Returns:
            Series data dictionary or None if not found
        """
        try:
            series_file = f"output/series/series_{series_title}.json"
            if os.path.exists(series_file):
                with open(series_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            console.print(f"[dim]Could not load series data: {str(e)}[/dim]")
        return None

    def _create_gemini_prompt_document(self, novel_data: Dict[str, Any],
                                     series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Create a prompt document using Gemini's exact response with minimal processing.

        Args:
            novel_data: Novel data
            series_info: Optional series information

        Returns:
            Complete prompt document with Gemini's exact markdown
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")
        author = metadata.get("author", "Unknown Author")
        genre = metadata.get("genre", "Fiction")
        description = metadata.get("description", "")

        # Prepare book content for Gemini analysis
        book_content = self._prepare_book_content_for_analysis(novel_data)

        # Get series visual consistency guidelines if this is part of a series
        series_guidelines = self._get_series_visual_guidelines(series_info) if series_info else ""

        # Create comprehensive analysis prompt for Gemini to generate ONE ultra-detailed cover prompt
        analysis_prompt = f"""
        You are a world-class book cover designer and AI prompt engineer. Analyze this complete book and create ONE comprehensive, ultra-detailed cover design prompt that contains every visual detail needed for perfect cover creation.

        BOOK CONTENT:
        {book_content}

        BOOK METADATA:
        - Title: {title}
        - Author: {author}
        - Genre: {genre}
        - Description: {description}

        {series_guidelines}

        IMPORTANT: Your response should be formatted in clean markdown WITHOUT code blocks. Create a single, comprehensive cover design prompt that includes every minute visual detail.

        ## ULTRA-DETAILED COVER DESIGN PROMPT

        Create ONE extremely detailed prompt (minimum 800 words) that includes ALL of the following elements with maximum descriptiveness:

        ### VISUAL COMPOSITION & LAYOUT
        - Exact positioning of every element using specific measurements or proportional descriptions
        - Detailed composition style (rule of thirds, golden ratio, dynamic symmetry, etc.)
        - Precise foreground, middle ground, and background element placement
        - Visual flow and eye movement patterns across the cover
        - Negative space usage and breathing room specifications
        - Exact margins, padding, and spatial relationships

        ### CHARACTER DESCRIPTIONS (if applicable)
        - Extremely detailed physical appearances: exact age, precise build, specific height proportions
        - Comprehensive facial features: eye shape, color, and expression; nose characteristics; lip fullness and color; jawline definition; cheekbone prominence
        - Complete hair descriptions: exact color, texture, length, styling, movement, and lighting effects
        - Detailed skin characteristics: tone, texture, any marks, lighting effects, and shadows
        - Comprehensive clothing descriptions: fabric types, colors, patterns, fit, wrinkles, textures, accessories
        - Precise body language: posture, gesture details, hand positions, stance, weight distribution
        - Specific facial expressions: micro-expressions, emotional nuances, eye direction, mouth position
        - Exact positioning and spatial relationships between characters
        - Camera angle and perspective relative to characters

        ### ENVIRONMENTAL & SETTING DETAILS
        - Comprehensive background descriptions with architectural or natural elements
        - Specific time of day with exact lighting conditions and atmospheric qualities
        - Detailed weather conditions and their visual effects
        - Precise depth of field specifications: what's in sharp focus vs. artistic blur
        - Exact perspective and viewing angle with specific camera positioning
        - Environmental storytelling elements with their precise placement and significance
        - Texture details for all surfaces: rough, smooth, weathered, polished, etc.
        - Atmospheric particles: dust, moisture, light rays, shadows

        ### COMPREHENSIVE COLOR PALETTE
        - Primary colors with specific names, saturation levels, and brightness values
        - Secondary and accent colors with exact usage areas and proportions
        - Detailed color temperature specifications and emotional impact
        - Specific gradient descriptions: direction, transition points, blending techniques
        - Color harmony relationships and psychological effects
        - Highlight and shadow color variations
        - Reflective color interactions between surfaces

        ### ADVANCED LIGHTING & ATMOSPHERE
        - Multiple light source descriptions: primary, secondary, and ambient lighting
        - Exact light direction, intensity, and quality (hard/soft, warm/cool)
        - Specific shadow characteristics: length, opacity, color, and edge quality
        - Advanced lighting techniques: rim lighting, backlighting, side lighting, dramatic chiaroscuro
        - Atmospheric effects: fog density, mist patterns, particle lighting, volumetric effects
        - Reflective lighting on different surfaces and materials
        - Color temperature variations across different light sources

        ### TYPOGRAPHY & TEXT INTEGRATION
        - Exact title placement with specific positioning coordinates or proportional descriptions
        - Detailed font characteristics: weight, style, spacing, kerning
        - Text color specifications with contrast ratios and readability considerations
        - Text effects: shadows, outlines, embossing, transparency, gradients
        - Author name positioning with size relationships to title
        - Text integration with background elements and visual harmony
        - Hierarchy and visual flow between text elements

        ### SYMBOLIC & THEMATIC ELEMENTS
        - Specific symbolic objects with detailed descriptions of appearance and placement
        - Thematic visual metaphors with exact visual treatment
        - Cultural or genre-specific elements with authentic details
        - Emotional symbolism through color, composition, and imagery
        - Story-specific motifs with precise visual representation
        - Subtle background elements that enhance narrative themes

        ### ARTISTIC STYLE & QUALITY
        - Specific art style: photorealistic, illustrated, digital painting, mixed media
        - Rendering quality specifications: ultra-high detail, commercial grade
        - Texture and surface quality descriptions for all elements
        - Artistic techniques: brushwork style, digital effects, traditional media simulation
        - Professional publishing standards and market positioning

        CRITICAL: Focus entirely on visual descriptiveness. Do NOT include technical specifications like aspect ratios, pixel dimensions, or file formats in this prompt. The goal is maximum visual detail for AI image generation.

        Provide this as ONE complete, ready-to-use visual prompt that contains every possible descriptive detail an AI image generator needs to create the perfect cover.
        """

        try:
            # Get Gemini's analysis
            gemini_response = self.gemini_client.generate_content(analysis_prompt, temperature=0.7, max_tokens=4000)
            cleaned_response = self.gemini_client.clean_response(gemini_response)

            # Create the complete document with header and Gemini's exact response
            sections = []

            # Header
            sections.append("# Gemini AI-Enhanced Cover Prompt Generator")
            sections.append("")
            sections.append(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            sections.append("**Powered by:** Gemini AI Analysis")
            sections.append("")
            sections.append("---")
            sections.append("")

            # Book Information
            sections.append("## 📚 Book Information")
            sections.append("")
            sections.append(f"- **Title:** {title}")
            sections.append(f"- **Author:** {author}")
            sections.append(f"- **Genre:** {genre}")
            if series_info:
                sections.append(f"- **Series:** {series_info.get('series_title', 'Unknown Series')}")
                sections.append(f"- **Book Number:** {series_info.get('book_number', 1)}")
            sections.append("")
            sections.append("### Description")
            sections.append(description)
            sections.append("")
            sections.append("---")
            sections.append("")

            # Check if Gemini provided the ultra-detailed cover design prompt
            has_comprehensive_prompt = "## ULTRA-DETAILED COVER DESIGN PROMPT" in cleaned_response

            if has_comprehensive_prompt:
                # Gemini provided the comprehensive prompt, use it directly
                sections.append("## 🤖 Gemini AI Ultra-Detailed Cover Design")
                sections.append("")
                sections.append("**This is a single, comprehensive cover design prompt that contains every visual detail needed for perfect cover creation.**")
                sections.append("")
                sections.append(cleaned_response)
                sections.append("")

                # Extract the ultra-detailed visual prompt from Gemini's response
                visual_prompt = self._extract_ultra_detailed_prompt(cleaned_response)
                if visual_prompt:
                    sections.append("## 🎨 Ultra-Detailed Visual Prompt")
                    sections.append("")
                    sections.append("**Copy this complete visual prompt to your AI image generator:**")
                    sections.append("")
                    sections.append("```")
                    sections.append(visual_prompt)
                    sections.append("```")
                    sections.append("")
                    sections.append(f"*Prompt length: {len(visual_prompt)} characters*")
                    sections.append("")
                    sections.append("**Note:** This prompt focuses entirely on visual descriptiveness for optimal AI image generation. Technical specifications are provided separately below.")
                    sections.append("")
            else:
                # Fallback: Generate our own comprehensive prompt
                sections.append("## 🤖 Gemini AI Analysis")
                sections.append("")
                sections.append(cleaned_response)
                sections.append("")
                sections.append("---")
                sections.append("")

                # Generate a single comprehensive prompt instead of three
                comprehensive_prompt = self._generate_single_comprehensive_prompt(cleaned_response, novel_data, series_info)
                sections.append("## 🎨 Ultra-Detailed Cover Design Prompt")
                sections.append("")
                sections.append("**Single comprehensive prompt containing every visual detail needed:**")
                sections.append("")
                sections.append("### Copy This Complete Prompt:")
                sections.append("```")
                sections.append(comprehensive_prompt)
                sections.append("```")
                sections.append("")
                sections.append(f"*Prompt length: {len(comprehensive_prompt)} characters*")
                sections.append("")

            sections.append("---")
            sections.append("")

            # Technical Specifications
            sections.append("## ⚙️ Technical Specifications")
            sections.append("")
            sections.append("### Image Requirements:")
            sections.append("- **Aspect Ratio:** 6:9 (standard book cover proportions)")
            sections.append("- **Recommended Dimensions:**")
            sections.append("  - **Minimum:** 1200x1800 pixels")
            sections.append("  - **Recommended:** 1800x2700 pixels")
            sections.append("  - **High Quality:** 2400x3600 pixels")
            sections.append("- **Resolution:** Minimum 300 DPI for print quality")
            sections.append("- **Format:** JPG (for photos) or PNG (for graphics)")
            sections.append("- **File Size:** Under 10MB for optimal performance")
            sections.append("")
            sections.append("### Size Guidelines:")
            sections.append("- **For Digital Only:** 1200x1800 pixels is sufficient")
            sections.append("- **For Print:** Use 1800x2700 pixels or higher")
            sections.append("- **Professional Print:** Use 2400x3600 pixels at 300 DPI")
            sections.append("")

            # Usage Instructions
            sections.append("## 📋 Usage Instructions")
            sections.append("")
            sections.append("1. **Copy the comprehensive prompt above**")
            sections.append("2. **Paste it into your preferred AI image generator (DALL-E, Midjourney, Stable Diffusion, etc.)**")
            sections.append("3. **Generate the cover image - the prompt contains all necessary details**")
            sections.append("4. **Download the image in high resolution (minimum 1800x2700 pixels)**")
            sections.append("5. **Save with the correct filename:**")

            if series_info:
                book_num = series_info.get('book_number', 1)
                sections.append(f"   - **Filename:** `Book{book_num}.jpg`")
                sections.append(f"   - **Location:** `covers/{series_info.get('series_title', 'Series')}/`")
            else:
                sections.append(f"   - **Filename:** `Cover.jpg`")
                sections.append(f"   - **Location:** `covers/{title}/`")

            sections.append("")
            sections.append("6. **Use the 'Manage Cover Images' menu option to apply the cover**")
            sections.append("")
            sections.append("### 💡 Pro Tips:")
            sections.append("- The prompt is designed to be complete - avoid adding extra instructions")
            sections.append("- If the result isn't perfect, try regenerating with the same prompt")
            sections.append("- For series books, maintain visual consistency across covers")
            sections.append("- Test how the cover looks as a thumbnail (small size)")
            sections.append("")

            sections.append("---")
            sections.append("")
            sections.append("*Generated by Gemini AI Ultra-Detailed Cover Prompt System*")
            sections.append("")
            sections.append("**This system creates a single, comprehensive prompt containing every visual detail needed for perfect cover reproduction.**")

            return "\n".join(sections)

        except Exception as e:
            console.print(f"[yellow]Error in Gemini analysis: {str(e)}[/yellow]")
            raise

    def _generate_enhanced_ai_prompts(self, gemini_analysis: str, novel_data: Dict[str, Any],
                                    series_info: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Generate enhanced AI image prompts based on Gemini's analysis.

        Args:
            gemini_analysis: Gemini's analysis response
            novel_data: Novel data
            series_info: Optional series information

        Returns:
            List of enhanced prompt dictionaries
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")
        genre = metadata.get("genre", "Fiction")

        # Extract key elements from Gemini's analysis
        analysis_data = self._parse_analysis_for_prompts(gemini_analysis)

        # Get typography recommendations for the genre
        typography_style = self._get_typography_recommendation(genre)

        # Generate three enhanced prompts
        prompts = [
            self._create_character_focused_prompt(analysis_data, title, genre, typography_style, series_info, novel_data),
            self._create_scene_based_prompt(analysis_data, title, genre, typography_style, series_info, novel_data),
            self._create_atmospheric_prompt(analysis_data, title, genre, typography_style, series_info, novel_data)
        ]

        return prompts

    def _extract_ultra_detailed_prompt(self, gemini_response: str) -> str:
        """
        Extract the ultra-detailed visual prompt from Gemini's response, removing technical specifications.

        Args:
            gemini_response: Full Gemini response containing the analysis

        Returns:
            Clean visual prompt without technical specifications
        """
        try:
            # Find the start of the ultra-detailed prompt
            prompt_start = gemini_response.find("## ULTRA-DETAILED COVER DESIGN PROMPT")
            if prompt_start == -1:
                return ""

            # Extract everything after the prompt header
            prompt_section = gemini_response[prompt_start:]
            lines = prompt_section.split('\n')

            # Collect all descriptive content, excluding headers and technical specs
            visual_elements = []
            current_section = ""

            for line in lines:
                line = line.strip()

                # Skip empty lines and headers
                if not line or line.startswith('#'):
                    continue

                # Skip technical specification sections
                if any(tech_term in line.lower() for tech_term in [
                    'aspect ratio', 'pixels', 'dpi', 'resolution', 'file format',
                    'technical', 'specifications', 'dimensions'
                ]):
                    continue

                # Skip bullet points and collect descriptive content
                if line.startswith('-') or line.startswith('*'):
                    # Clean up bullet point and add to visual elements
                    clean_line = line.lstrip('-* ').strip()
                    if clean_line and len(clean_line) > 10:  # Only substantial descriptions
                        visual_elements.append(clean_line)
                elif len(line) > 20 and not line.startswith('###'):  # Paragraph content
                    visual_elements.append(line)

            # Join all visual elements into a comprehensive prompt
            if visual_elements:
                # Create a flowing, descriptive prompt
                visual_prompt = "Ultra-detailed professional book cover design featuring "
                visual_prompt += ", ".join(visual_elements[:50])  # Limit to prevent overly long prompts

                # Clean up the prompt
                visual_prompt = visual_prompt.replace('  ', ' ')  # Remove double spaces
                visual_prompt = visual_prompt.replace(' ,', ',')  # Fix spacing around commas

                return visual_prompt

        except Exception as e:
            console.print(f"[dim]Error extracting visual prompt: {str(e)}[/dim]")

        return ""

    def _generate_single_comprehensive_prompt(self, gemini_analysis: str, novel_data: Dict[str, Any],
                                            series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Generate a single comprehensive cover design prompt based on Gemini's analysis.

        Args:
            gemini_analysis: Gemini's analysis response
            novel_data: Novel data
            series_info: Optional series information

        Returns:
            Single comprehensive prompt string
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")
        author = metadata.get("author", "Unknown Author")
        genre = metadata.get("genre", "Fiction")

        # Extract key elements from Gemini's analysis
        analysis_data = self._parse_analysis_for_prompts(gemini_analysis)

        # Get typography recommendations for the genre
        typography_style = self._get_typography_recommendation(genre)

        # Build ultra-detailed visual prompt parts (no technical specifications)
        prompt_parts = []

        # Base description focusing on visual quality
        prompt_parts.append("Ultra-detailed professional book cover design featuring")

        # Character details with maximum descriptiveness
        if analysis_data.get("characters"):
            char_desc = analysis_data["characters"][0][:400] if analysis_data["characters"] else ""
            if char_desc:
                prompt_parts.append(f"main characters with precise physical details: {char_desc.lower()}")
                prompt_parts.append("extremely detailed facial expressions showing subtle emotional nuances")
                prompt_parts.append("specific body language and posture conveying character relationships")
                prompt_parts.append("authentic clothing with fabric textures, wrinkles, and realistic fit")

        # Scene and setting with comprehensive environmental details
        if analysis_data.get("scenes"):
            scene_desc = analysis_data["scenes"][0][:350] if analysis_data["scenes"] else ""
            if scene_desc:
                prompt_parts.append(f"immersive scene composition: {scene_desc.lower()}")
                prompt_parts.append("detailed environmental storytelling elements")

        if analysis_data.get("atmosphere"):
            atmosphere = analysis_data["atmosphere"][:300]
            prompt_parts.append(f"atmospheric setting with rich environmental details: {atmosphere.lower()}")
            prompt_parts.append("specific weather conditions and time-of-day lighting effects")

        # Comprehensive color specifications
        if analysis_data.get("colors"):
            colors = ", ".join(analysis_data["colors"][:5])
            prompt_parts.append(f"sophisticated color palette featuring {colors.lower()}")
            prompt_parts.append("precise color temperature gradients and saturation levels")
            prompt_parts.append("subtle color interactions and reflective lighting effects")

        # Advanced lighting and atmospheric details
        if analysis_data.get("lighting"):
            lighting = analysis_data["lighting"][:200]
            prompt_parts.append(f"advanced lighting setup: {lighting.lower()}")

        prompt_parts.append("dramatic chiaroscuro lighting with multiple light sources")
        prompt_parts.append("specific shadow characteristics including length, opacity, and edge quality")
        prompt_parts.append("atmospheric effects such as volumetric lighting, particle effects, and depth")

        # Composition and visual flow
        prompt_parts.append("sophisticated composition using rule of thirds and golden ratio principles")
        prompt_parts.append("clear visual hierarchy guiding eye movement across the cover")
        prompt_parts.append("precise negative space usage creating breathing room and focus")

        # Symbolic and thematic elements
        if analysis_data.get("symbols"):
            symbols = ", ".join(analysis_data["symbols"][:4])
            prompt_parts.append(f"meaningful symbolic elements: {symbols.lower()}")
            prompt_parts.append("thematic visual metaphors seamlessly integrated into the composition")

        # Emotional and atmospheric tone
        if analysis_data.get("emotional_tone"):
            tone = analysis_data["emotional_tone"][:200]
            prompt_parts.append(f"emotional atmosphere conveying: {tone.lower()}")

        # Typography integration (visual aspects only) - with clear author name emphasis
        prompt_parts.append(f"elegant typography style: {typography_style}.")
        prompt_parts.append(f'Book title "{title}" prominently displayed with perfect visual hierarchy.')
        prompt_parts.append(f'IMPORTANT: Author name "{author}" must be clearly visible and properly positioned on the cover.')
        prompt_parts.append(f'Display "{author}" as the author name - do NOT use character names from the story.')
        prompt_parts.append("Text elements seamlessly blended with background imagery.")
        prompt_parts.append("High contrast text treatment ensuring maximum visual impact.")

        # Artistic quality and style specifications
        prompt_parts.append("Photorealistic rendering with ultra-high detail and texture definition.")
        prompt_parts.append("Commercial-grade artistic quality with professional finishing.")
        prompt_parts.append("Genre-appropriate visual conventions and market positioning.")
        prompt_parts.append("Sophisticated artistic techniques creating depth and visual interest.")
        prompt_parts.append("Masterful use of texture, lighting, and color to create compelling visual narrative.")

        # Join with proper spacing and formatting
        formatted_prompt = " ".join(prompt_parts)

        # Clean up any double periods and ensure proper spacing
        formatted_prompt = formatted_prompt.replace("..", ".").replace("  ", " ")

        return formatted_prompt

    def _parse_analysis_for_prompts(self, analysis: str) -> Dict[str, Any]:
        """
        Parse Gemini's analysis to extract key elements for prompt generation.

        Args:
            analysis: Gemini's analysis text

        Returns:
            Dictionary with extracted elements
        """
        # Simple extraction of key sections
        data = {
            "characters": [],
            "scenes": [],
            "colors": [],
            "symbols": [],
            "atmosphere": "",
            "lighting": "",
            "emotional_tone": ""
        }

        # Extract sections (basic parsing)
        lines = analysis.split('\n')
        current_section = None

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Identify sections
            if "## Character Descriptions" in line:
                current_section = "characters"
            elif "## Visual Scenes" in line:
                current_section = "scenes"
            elif "## Color Palette" in line:
                current_section = "colors"
            elif "## Symbolic Elements" in line:
                current_section = "symbols"
            elif "## Setting & Atmosphere" in line:
                current_section = "atmosphere"
            elif "## Lighting & Composition" in line:
                current_section = "lighting"
            elif "## Emotional Tone" in line:
                current_section = "emotional_tone"
            elif line.startswith("## "):
                current_section = None
            elif current_section and (line.startswith("-") or line.startswith("*") or line.startswith("1.") or line.startswith("2.") or line.startswith("3.")):
                # Extract list items
                clean_line = line.lstrip("-*123456789. ").strip()
                if clean_line:
                    if current_section in ["characters", "scenes", "colors", "symbols"]:
                        data[current_section].append(clean_line)
            elif current_section in ["atmosphere", "lighting", "emotional_tone"] and line and not line.startswith("#"):
                # Extract paragraph content
                if data[current_section]:
                    data[current_section] += " " + line
                else:
                    data[current_section] = line

        return data

    def _create_character_focused_prompt(self, analysis_data: Dict[str, Any], title: str, genre: str,
                                       typography_style: str, series_info: Optional[Dict[str, Any]] = None,
                                       novel_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a character-focused AI image prompt."""

        prompt_parts = []

        # Base description
        prompt_parts.append("Professional book cover design featuring main characters,")

        # Character descriptions
        if analysis_data.get("characters"):
            char_desc = analysis_data["characters"][0][:200] if analysis_data["characters"] else ""
            if char_desc:
                prompt_parts.append(f"showing {char_desc.lower()},")

        # Setting and atmosphere
        if analysis_data.get("atmosphere"):
            atmosphere = analysis_data["atmosphere"][:150]
            prompt_parts.append(f"set in {atmosphere.lower()},")

        # Color palette
        if analysis_data.get("colors"):
            colors = ", ".join(analysis_data["colors"][:3])
            prompt_parts.append(f"using color palette of {colors.lower()},")

        # Emotional tone
        if analysis_data.get("emotional_tone"):
            tone = analysis_data["emotional_tone"][:100]
            prompt_parts.append(f"conveying {tone.lower()},")

        # Lighting
        if analysis_data.get("lighting"):
            lighting = analysis_data["lighting"][:100]
            prompt_parts.append(f"with {lighting.lower()},")

        # Typography specifications with actual title and author
        prompt_parts.append(f"typography: {typography_style},")
        prompt_parts.append(f'book title "{title}" prominently displayed at top in large readable text,')

        # Get author name from metadata
        metadata = novel_data.get("metadata", {}) if hasattr(novel_data, 'get') else {}
        author = metadata.get("author", "Unknown Author")
        prompt_parts.append(f'IMPORTANT: author name "{author}" must be clearly visible and elegantly placed,')
        prompt_parts.append(f'display "{author}" as the author name - do NOT use character names,')

        # Technical specifications
        prompt_parts.append("text must be clearly readable and integrated into design,")
        prompt_parts.append("high quality digital art, 6:9 aspect ratio, 1800x2700 pixels,")
        prompt_parts.append("professional book cover layout, complete with title and author text,")
        prompt_parts.append("detailed artwork, vibrant colors, commercial quality, ready for publication")

        full_prompt = " ".join(prompt_parts)

        return {
            "name": "Character-Focused",
            "description": "Emphasizes main characters with detailed character descriptions and emotional connection",
            "prompt": full_prompt
        }

    def _create_scene_based_prompt(self, analysis_data: Dict[str, Any], title: str, genre: str,
                                 typography_style: str, series_info: Optional[Dict[str, Any]] = None,
                                 novel_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a scene-based AI image prompt."""

        prompt_parts = []

        # Base description
        prompt_parts.append("Professional book cover design depicting a key scene,")

        # Scene description
        if analysis_data.get("scenes"):
            scene_desc = analysis_data["scenes"][0][:200] if analysis_data["scenes"] else ""
            if scene_desc:
                prompt_parts.append(f"showing {scene_desc.lower()},")

        # Symbolic elements
        if analysis_data.get("symbols"):
            symbols = ", ".join(analysis_data["symbols"][:2])
            prompt_parts.append(f"incorporating symbolic elements: {symbols.lower()},")

        # Setting and atmosphere
        if analysis_data.get("atmosphere"):
            atmosphere = analysis_data["atmosphere"][:150]
            prompt_parts.append(f"atmospheric setting: {atmosphere.lower()},")

        # Color palette
        if analysis_data.get("colors"):
            colors = ", ".join(analysis_data["colors"][:3])
            prompt_parts.append(f"color scheme: {colors.lower()},")

        # Lighting and composition
        if analysis_data.get("lighting"):
            lighting = analysis_data["lighting"][:120]
            prompt_parts.append(f"lighting and composition: {lighting.lower()},")

        # Typography specifications with actual title and author
        prompt_parts.append(f"typography: {typography_style},")
        prompt_parts.append(f'book title "{title}" integrated into scene composition in large readable text,')

        # Get author name from metadata
        metadata = novel_data.get("metadata", {}) if novel_data and hasattr(novel_data, 'get') else {}
        author = metadata.get("author", "Unknown Author")
        prompt_parts.append(f'IMPORTANT: author name "{author}" must be clearly visible and readable against background,')
        prompt_parts.append(f'display "{author}" as the author name - do NOT use character names,')

        # Technical specifications
        prompt_parts.append("text must be clearly readable and part of the design,")
        prompt_parts.append("cinematic composition, dramatic lighting, high detail,")
        prompt_parts.append("6:9 aspect ratio, 1800x2700 pixels, professional quality,")
        prompt_parts.append("book cover layout, commercial artwork, complete with title and author text")

        full_prompt = " ".join(prompt_parts)

        return {
            "name": "Scene-Based",
            "description": "Features a pivotal scene from the story with dramatic composition and symbolic elements",
            "prompt": full_prompt
        }

    def _create_atmospheric_prompt(self, analysis_data: Dict[str, Any], title: str, genre: str,
                                 typography_style: str, series_info: Optional[Dict[str, Any]] = None,
                                 novel_data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create an atmospheric AI image prompt."""

        prompt_parts = []

        # Base description
        prompt_parts.append("Professional book cover design with atmospheric focus,")

        # Symbolic elements as main focus
        if analysis_data.get("symbols"):
            symbols = ", ".join(analysis_data["symbols"][:3])
            prompt_parts.append(f"featuring symbolic elements: {symbols.lower()},")

        # Emotional tone and mood
        if analysis_data.get("emotional_tone"):
            tone = analysis_data["emotional_tone"][:120]
            prompt_parts.append(f"evoking emotional atmosphere: {tone.lower()},")

        # Setting and environment
        if analysis_data.get("atmosphere"):
            atmosphere = analysis_data["atmosphere"][:150]
            prompt_parts.append(f"environmental mood: {atmosphere.lower()},")

        # Color palette emphasis
        if analysis_data.get("colors"):
            colors = ", ".join(analysis_data["colors"][:4])
            prompt_parts.append(f"rich color palette: {colors.lower()},")

        # Lighting for mood
        if analysis_data.get("lighting"):
            lighting = analysis_data["lighting"][:120]
            prompt_parts.append(f"atmospheric lighting: {lighting.lower()},")

        # Typography specifications with actual title and author
        prompt_parts.append(f"typography: {typography_style},")
        prompt_parts.append(f'book title "{title}" artistically integrated as design element in large readable text,')

        # Get author name from metadata
        metadata = novel_data.get("metadata", {}) if novel_data and hasattr(novel_data, 'get') else {}
        author = metadata.get("author", "Unknown Author")
        prompt_parts.append(f'IMPORTANT: author name "{author}" must be clearly visible and harmoniously placed,')
        prompt_parts.append(f'display "{author}" as the author name - do NOT use character names,')

        # Technical specifications
        prompt_parts.append("text must be clearly readable and artistically integrated,")
        prompt_parts.append("abstract composition, mood-focused design, artistic interpretation,")
        prompt_parts.append("6:9 aspect ratio, 1800x2700 pixels, premium quality,")
        prompt_parts.append("sophisticated book cover, gallery-worthy artwork, complete with title and author text")

        full_prompt = " ".join(prompt_parts)

        return {
            "name": "Atmospheric",
            "description": "Emphasizes mood, symbolism, and emotional atmosphere with artistic composition",
            "prompt": full_prompt
        }

    def _generate_detailed_prompts_from_analysis(self, analysis: Dict[str, Any],
                                               series_info: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Generate multiple detailed image prompts based on Gemini analysis.

        Args:
            analysis: Structured analysis from Gemini
            series_info: Optional series information

        Returns:
            List of detailed prompt variations
        """
        prompts = []

        # Generate 3 different prompt variations
        prompt_styles = [
            {
                "name": "Character-Focused",
                "description": "Emphasizes main characters and their interactions",
                "style": "character-centric composition"
            },
            {
                "name": "Scene-Based",
                "description": "Features a key scene or moment from the story",
                "style": "dramatic scene composition"
            },
            {
                "name": "Atmospheric",
                "description": "Focuses on mood, setting, and symbolic elements",
                "style": "atmospheric and symbolic composition"
            }
        ]

        for prompt_style in prompt_styles:
            prompt = self._create_single_detailed_prompt(analysis, prompt_style, series_info)
            prompts.append(prompt)

        return prompts

    def _create_single_detailed_prompt(self, analysis: Dict[str, Any], prompt_style: Dict[str, str],
                                     series_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a single detailed prompt based on analysis and style.

        Args:
            analysis: Gemini analysis data
            prompt_style: Style configuration for this prompt
            series_info: Optional series information

        Returns:
            Detailed prompt dictionary
        """
        prompt_parts = []

        # Start with base description
        prompt_parts.append("Professional book cover design,")

        # Add style-specific focus
        if prompt_style["name"] == "Character-Focused":
            # Focus on characters
            if analysis.get("character_descriptions"):
                char_desc = analysis["character_descriptions"][0] if analysis["character_descriptions"] else ""
                if char_desc:
                    prompt_parts.append(f"featuring {char_desc.lower()},")

        elif prompt_style["name"] == "Scene-Based":
            # Focus on a key scene
            if analysis.get("visual_scenes"):
                scene_desc = analysis["visual_scenes"][0] if analysis["visual_scenes"] else ""
                if scene_desc:
                    prompt_parts.append(f"depicting {scene_desc.lower()},")

        elif prompt_style["name"] == "Atmospheric":
            # Focus on mood and symbols
            if analysis.get("symbolic_elements"):
                symbol_desc = analysis["symbolic_elements"][0] if analysis["symbolic_elements"] else ""
                if symbol_desc:
                    prompt_parts.append(f"incorporating {symbol_desc.lower()},")

        # Add setting and atmosphere
        if analysis.get("setting_atmosphere"):
            prompt_parts.append(f"set in {analysis['setting_atmosphere'].lower()},")

        # Add color palette
        if analysis.get("color_palette"):
            colors = ", ".join(analysis["color_palette"][:3])
            prompt_parts.append(f"using a color palette of {colors.lower()},")

        # Add emotional tone
        if analysis.get("emotional_tone"):
            prompt_parts.append(f"conveying {analysis['emotional_tone'].lower()},")

        # Add lighting and composition
        if analysis.get("lighting_composition"):
            prompt_parts.append(f"with {analysis['lighting_composition'].lower()},")

        # Add technical specifications
        prompt_parts.append("high quality, detailed artwork, professional book cover design, 6:9 aspect ratio, space for title text")

        # Join all parts
        full_prompt = " ".join(prompt_parts)

        return {
            "name": prompt_style["name"],
            "description": prompt_style["description"],
            "style": prompt_style["style"],
            "prompt": full_prompt,
            "length": len(full_prompt)
        }

    def _create_comprehensive_prompt_document(self, novel_data: Dict[str, Any],
                                            analysis: Dict[str, Any], detailed_prompts: List[Dict[str, Any]],
                                            series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Create a comprehensive prompt document with Gemini analysis and multiple prompt options.

        Args:
            novel_data: Original novel data
            analysis: Gemini analysis results
            detailed_prompts: List of generated prompt variations
            series_info: Optional series information

        Returns:
            Complete prompt document as string
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")
        author = metadata.get("author", "Unknown Author")
        genre = metadata.get("genre", "Fiction")
        description = metadata.get("description", "")

        sections = []

        # Header
        sections.append("# Gemini AI-Enhanced Cover Prompt Generator")
        sections.append("")
        sections.append(f"**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        sections.append("**Powered by:** Gemini AI Analysis")
        sections.append("")

        # Book Information
        sections.append("## 📚 Book Information")
        sections.append("")
        sections.append(f"- **Title:** {title}")
        sections.append(f"- **Author:** {author}")
        sections.append(f"- **Genre:** {genre}")
        if series_info:
            sections.append(f"- **Series:** {series_info.get('series_title', 'Unknown Series')}")
            sections.append(f"- **Book Number:** {series_info.get('book_number', 1)}")
        sections.append("")
        sections.append("### Description")
        sections.append(description)
        sections.append("")

        # Gemini AI Analysis
        sections.append("## 🤖 Gemini AI Analysis")
        sections.append("")

        if analysis.get("visual_scenes"):
            sections.append("### Key Visual Scenes")
            for i, scene in enumerate(analysis["visual_scenes"][:3], 1):
                sections.append(f"{i}. {scene}")
            sections.append("")

        if analysis.get("character_descriptions"):
            sections.append("### Character Descriptions")
            for i, char in enumerate(analysis["character_descriptions"][:3], 1):
                sections.append(f"- {char}")
            sections.append("")

        if analysis.get("setting_atmosphere"):
            sections.append("### Setting & Atmosphere")
            sections.append(analysis["setting_atmosphere"])
            sections.append("")

        if analysis.get("color_palette"):
            sections.append("### Recommended Colors")
            for color in analysis["color_palette"][:5]:
                sections.append(f"- {color}")
            sections.append("")

        if analysis.get("symbolic_elements"):
            sections.append("### Symbolic Elements")
            for symbol in analysis["symbolic_elements"][:3]:
                sections.append(f"- {symbol}")
            sections.append("")

        if analysis.get("emotional_tone"):
            sections.append("### Emotional Tone")
            sections.append(analysis["emotional_tone"])
            sections.append("")

        if analysis.get("lighting_composition"):
            sections.append("### Lighting & Composition")
            sections.append(analysis["lighting_composition"])
            sections.append("")

        # AI Image Generation Prompts
        sections.append("## 🎨 AI Image Generation Prompts")
        sections.append("")
        sections.append("Choose from these AI-generated prompt variations:")
        sections.append("")

        for i, prompt_data in enumerate(detailed_prompts, 1):
            sections.append(f"### Option {i}: {prompt_data['name']}")
            sections.append("")
            sections.append(f"**Description:** {prompt_data['description']}")
            sections.append(f"**Style:** {prompt_data['style']}")
            sections.append("")
            sections.append("#### Copy This Prompt:")
            sections.append("```")
            sections.append(prompt_data['prompt'])
            sections.append("```")
            sections.append(f"*Prompt Length: {prompt_data['length']} characters*")
            sections.append("")

        # Typography Recommendations
        sections.append("## 📝 Typography Recommendations")
        sections.append("")

        # Determine best typography style based on genre
        typography_rec = self._get_typography_recommendation(genre)
        sections.append(f"**Recommended Typography Style:** {typography_rec}")
        sections.append("")
        sections.append("### Typography Guidelines:")
        sections.append("- Title should be large and prominent")
        sections.append("- Author name should be smaller but clearly readable")
        sections.append("- Leave adequate white space around text")
        sections.append("- Ensure high contrast between text and background")
        sections.append("- Consider the genre's typical typography conventions")
        sections.append("")

        # Technical Specifications
        sections.append("## ⚙️ Technical Specifications")
        sections.append("")
        sections.append("### Image Requirements:")
        sections.append("- **Aspect Ratio:** 6:9 (standard book cover proportions)")
        sections.append("- **Recommended Dimensions:**")
        sections.append("  - **Minimum:** 1200x1800 pixels")
        sections.append("  - **Recommended:** 1800x2700 pixels")
        sections.append("  - **High Quality:** 2400x3600 pixels")
        sections.append("- **Resolution:** Minimum 300 DPI for print quality")
        sections.append("- **Format:** JPG (for photos) or PNG (for graphics)")
        sections.append("- **File Size:** Under 10MB for optimal performance")
        sections.append("- **Color Space:** RGB for digital, CMYK for print")
        sections.append("")
        sections.append("### Size Guidelines:")
        sections.append("- **For Digital Only:** 1200x1800 pixels is sufficient")
        sections.append("- **For Print:** Use 1800x2700 pixels or higher")
        sections.append("- **Professional Print:** Use 2400x3600 pixels at 300 DPI")
        sections.append("")

        # Usage Instructions
        sections.append("## 📋 Usage Instructions")
        sections.append("")
        sections.append("1. **Choose one of the AI prompts above**")
        sections.append("2. **Copy the prompt text to your preferred AI image generator:**")
        sections.append("   - DALL-E 3 (OpenAI)")
        sections.append("   - Midjourney")
        sections.append("   - Stable Diffusion")
        sections.append("   - Adobe Firefly")
        sections.append("   - Any other AI image generator")
        sections.append("")
        sections.append("3. **Generate multiple variations and select the best one**")
        sections.append("4. **Download the image in high resolution**")
        sections.append("5. **Save with the correct filename:**")

        if series_info:
            book_num = series_info.get('book_number', 1)
            sections.append(f"   - **Filename:** `Book{book_num}.jpg`")
            sections.append(f"   - **Location:** `covers/{series_info.get('series_title', 'Series')}/`")
        else:
            sections.append(f"   - **Filename:** `Cover.jpg`")
            sections.append(f"   - **Location:** `covers/{title}/`")

        sections.append("")
        sections.append("6. **Use the 'Manage Cover Images' menu option to apply the cover**")
        sections.append("")

        # Tips for Best Results
        sections.append("## 💡 Tips for Best Results")
        sections.append("")
        sections.append("- Try multiple prompts to see different interpretations")
        sections.append("- Experiment with adding style modifiers like 'digital art', 'photorealistic', or 'illustration'")
        sections.append("- If characters look wrong, try regenerating with more specific descriptions")
        sections.append("- For series books, maintain visual consistency across covers")
        sections.append("- Consider your target audience and genre expectations")
        sections.append("- Test how the cover looks as a thumbnail (small size)")
        sections.append("")

        sections.append("---")
        sections.append("")
        sections.append("*Generated by Gemini AI-Enhanced Cover Prompt System*")

        return "\n".join(sections)

    def _get_typography_recommendation(self, genre: str) -> str:
        """
        Get typography recommendation based on genre.

        Args:
            genre: Book genre

        Returns:
            Typography recommendation string
        """
        genre_lower = genre.lower()

        if any(word in genre_lower for word in ["fantasy", "medieval", "historical"]):
            return self.typography_styles["decorative"]
        elif any(word in genre_lower for word in ["science fiction", "sci-fi", "futuristic", "cyberpunk"]):
            return self.typography_styles["sans_serif"]
        elif any(word in genre_lower for word in ["horror", "thriller", "mystery"]):
            return self.typography_styles["display"]
        elif any(word in genre_lower for word in ["romance", "literary"]):
            return self.typography_styles["script"]
        else:
            return self.typography_styles["serif"]

    def _create_enhanced_fallback_prompt(self, novel_data: Dict[str, Any],
                                       series_info: Optional[Dict[str, Any]] = None) -> str:
        """
        Create an enhanced fallback prompt when Gemini is not available.

        Args:
            novel_data: Novel data
            series_info: Optional series information

        Returns:
            Enhanced fallback prompt document
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")
        author = metadata.get("author", "Unknown Author")
        genre = metadata.get("genre", "Fiction")
        description = metadata.get("description", "")

        sections = []

        # Header
        sections.append("=" * 80)
        sections.append("AI COVER PROMPT GENERATOR (ENHANCED FALLBACK)")
        sections.append("=" * 80)
        sections.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        sections.append("Note: Gemini AI analysis not available - using enhanced content analysis")
        sections.append("")

        # Book Information
        sections.append("📚 BOOK INFORMATION")
        sections.append("-" * 40)
        sections.append(f"Title: {title}")
        sections.append(f"Author: {author}")
        sections.append(f"Genre: {genre}")
        if series_info:
            sections.append(f"Series: {series_info.get('series_title', 'Unknown Series')}")
            sections.append(f"Book Number: {series_info.get('book_number', 1)}")
        sections.append("")
        sections.append("Description:")
        sections.append(description)
        sections.append("")

        # Generate basic prompts based on available data
        basic_prompts = self._generate_basic_prompts(novel_data, series_info)

        sections.append("🎨 AI IMAGE GENERATION PROMPTS")
        sections.append("-" * 40)
        sections.append("Generated prompts based on book content analysis:")
        sections.append("")

        for i, prompt_data in enumerate(basic_prompts, 1):
            sections.append(f"OPTION {i}: {prompt_data['name']}")
            sections.append(f"Description: {prompt_data['description']}")
            sections.append("")
            sections.append("COPY THIS PROMPT:")
            sections.append("─" * 60)
            sections.append(prompt_data['prompt'])
            sections.append("─" * 60)
            sections.append("")

        # Add the same technical specs and instructions as the full version
        sections.append("⚙️ TECHNICAL SPECIFICATIONS")
        sections.append("-" * 40)
        sections.append("Image Requirements:")
        sections.append("• Aspect Ratio: 6:9 (standard book cover proportions)")
        sections.append("• Resolution: Minimum 300 DPI for print quality")
        sections.append("• Format: JPG or PNG")
        sections.append("• File Size: Under 10MB for optimal performance")
        sections.append("")

        sections.append("📋 USAGE INSTRUCTIONS")
        sections.append("-" * 40)
        sections.append("1. Choose one of the prompts above")
        sections.append("2. Copy to your preferred AI image generator")
        sections.append("3. Generate and download the image")
        sections.append("4. Save with correct filename:")

        if series_info:
            book_num = series_info.get('book_number', 1)
            sections.append(f"   • Filename: Book{book_num}.jpg")
        else:
            sections.append(f"   • Filename: Cover.jpg")

        sections.append("5. Use 'Manage Cover Images' menu to apply")
        sections.append("")

        sections.append("=" * 80)
        sections.append("Enhanced Fallback Cover Prompt System")
        sections.append("=" * 80)

        return "\n".join(sections)

    def _generate_basic_prompts(self, novel_data: Dict[str, Any],
                              series_info: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Generate basic prompts when Gemini analysis is not available.

        Args:
            novel_data: Novel data
            series_info: Optional series information

        Returns:
            List of basic prompt variations
        """
        metadata = novel_data.get("metadata", {})
        title = metadata.get("title", "Untitled")
        genre = metadata.get("genre", "Fiction")
        description = metadata.get("description", "")

        # Extract basic elements from description
        genre_elements = self._get_genre_visual_elements(genre)

        prompts = [
            {
                "name": "Genre-Based Design",
                "description": f"Classic {genre} cover design with genre-appropriate elements",
                "prompt": f"Professional book cover for '{title}', {genre} novel, {genre_elements}, high quality, detailed artwork, 6:9 aspect ratio, space for title text"
            },
            {
                "name": "Minimalist Design",
                "description": "Clean, minimalist approach focusing on typography and simple imagery",
                "prompt": f"Minimalist book cover design for '{title}', clean composition, elegant typography, simple but striking imagery, professional quality, 6:9 aspect ratio"
            },
            {
                "name": "Atmospheric Design",
                "description": "Mood-focused design emphasizing atmosphere and emotion",
                "prompt": f"Atmospheric book cover for '{title}', {genre} mood, dramatic lighting, emotional composition, professional book cover design, 6:9 aspect ratio, space for text"
            }
        ]

        return prompts

    def _get_genre_visual_elements(self, genre: str) -> str:
        """Get visual elements description for a genre."""
        genre_lower = genre.lower()

        if "fantasy" in genre_lower:
            return "mystical landscapes, magical elements, fantasy creatures, ethereal lighting"
        elif "science fiction" in genre_lower or "sci-fi" in genre_lower:
            return "futuristic elements, space scenes, advanced technology, sci-fi atmosphere"
        elif "mystery" in genre_lower or "thriller" in genre_lower:
            return "mysterious atmosphere, dramatic shadows, suspenseful mood, noir elements"
        elif "romance" in genre_lower:
            return "romantic atmosphere, elegant design, warm colors, emotional imagery"
        elif "horror" in genre_lower:
            return "dark atmosphere, gothic elements, ominous mood, dramatic shadows"
        elif "historical" in genre_lower:
            return "period-appropriate elements, vintage atmosphere, historical details"
        else:
            return "professional design, genre-appropriate atmosphere, compelling imagery"

    def _save_prompt_to_file(self, prompt: str, output_dir: str, title: str) -> str:
        """Save the prompt to a markdown file and create necessary folders."""
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Create filename with .md extension
        filename = "cover_prompt.md"
        file_path = os.path.join(output_dir, filename)

        # Save the prompt
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(prompt)

        return file_path

    def _create_series_cover_folders(self, series_info: Dict[str, Any]) -> str:
        """
        Create cover folders for series books if they don't exist.

        Args:
            series_info: Series information containing series_title

        Returns:
            Path to the created cover folder
        """
        if not series_info:
            return ""

        series_title = series_info.get('series_title', 'Unknown Series')

        # Create the covers directory structure
        covers_base = "covers"
        series_cover_dir = os.path.join(covers_base, series_title)

        # Create directories if they don't exist
        os.makedirs(series_cover_dir, exist_ok=True)

        console.print(f"[dim]Created cover folder: {series_cover_dir}[/dim]")

        return series_cover_dir
