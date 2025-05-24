"""
Profile Image Manager for Writer Profiles

This module manages the integration of writer profile images into the EPUB generation system,
including image validation, path resolution, and EPUB embedding.
"""

import os
import base64
from pathlib import Path
from typing import Dict, Any, Optional, Tuple, List
import json

class ProfileImageManager:
    """
    Manages writer profile images for EPUB integration.
    """

    def __init__(self):
        """Initialize the profile image manager."""
        self.portraits_dir = Path("src/writer_profiles/portraits")
        self.image_data_file = Path("writer_profile_images/image_generation_prompts.json")
        self._image_mapping = None

    def _load_image_mapping(self) -> Dict[str, Dict[str, Any]]:
        """Load the image mapping data from the JSON file."""
        if self._image_mapping is not None:
            return self._image_mapping

        try:
            if self.image_data_file.exists():
                with open(self.image_data_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Create mapping by writer name
                    self._image_mapping = {
                        writer['name']: writer
                        for writer in data.get('writers', [])
                    }
            else:
                self._image_mapping = {}
        except Exception as e:
            print(f"Warning: Could not load image mapping: {e}")
            self._image_mapping = {}

        return self._image_mapping

    def get_profile_image_path(self, writer_name: str) -> Optional[Path]:
        """
        Get the file path for a writer's profile image.

        Args:
            writer_name: Name of the writer

        Returns:
            Path to the image file or None if not found
        """
        image_mapping = self._load_image_mapping()

        if writer_name in image_mapping:
            file_name = image_mapping[writer_name]['file_name']
            image_path = self.portraits_dir / file_name

            if image_path.exists():
                return image_path

        return None

    def get_profile_image_data(self, writer_name: str) -> Optional[Tuple[bytes, str]]:
        """
        Get the binary data and MIME type for a writer's profile image.

        Args:
            writer_name: Name of the writer

        Returns:
            Tuple of (image_bytes, mime_type) or None if not found
        """
        image_path = self.get_profile_image_path(writer_name)

        if image_path and image_path.exists():
            try:
                with open(image_path, 'rb') as f:
                    image_bytes = f.read()

                # Determine MIME type based on file extension
                ext = image_path.suffix.lower()
                if ext == '.jpg' or ext == '.jpeg':
                    mime_type = 'image/jpeg'
                elif ext == '.png':
                    mime_type = 'image/png'
                else:
                    mime_type = 'image/jpeg'  # Default fallback

                return image_bytes, mime_type
            except Exception as e:
                print(f"Warning: Could not read image file {image_path}: {e}")

        return None

    def get_profile_image_base64(self, writer_name: str) -> Optional[str]:
        """
        Get the base64-encoded image data for embedding in HTML.

        Args:
            writer_name: Name of the writer

        Returns:
            Base64-encoded image string or None if not found
        """
        image_data = self.get_profile_image_data(writer_name)

        if image_data:
            image_bytes, mime_type = image_data
            base64_data = base64.b64encode(image_bytes).decode('utf-8')
            return f"data:{mime_type};base64,{base64_data}"

        return None

    def get_writer_image_info(self, writer_name: str) -> Dict[str, Any]:
        """
        Get complete image information for a writer.

        Args:
            writer_name: Name of the writer

        Returns:
            Dictionary with image information
        """
        image_mapping = self._load_image_mapping()

        result = {
            'has_image': False,
            'file_name': None,
            'file_path': None,
            'base64_data': None,
            'cultural_background': '',
            'era': '',
            'primary_genres': []
        }

        if writer_name in image_mapping:
            writer_data = image_mapping[writer_name]
            image_path = self.get_profile_image_path(writer_name)

            result.update({
                'has_image': image_path is not None and image_path.exists(),
                'file_name': writer_data.get('file_name'),
                'file_path': str(image_path) if image_path else None,
                'cultural_background': writer_data.get('cultural_background', ''),
                'era': writer_data.get('era', ''),
                'primary_genres': writer_data.get('primary_genres', [])
            })

            if result['has_image']:
                result['base64_data'] = self.get_profile_image_base64(writer_name)

        return result

    def validate_all_images(self) -> Dict[str, Any]:
        """
        Validate all profile images and return a status report.

        Returns:
            Dictionary with validation results
        """
        image_mapping = self._load_image_mapping()

        results = {
            'total_writers': len(image_mapping),
            'images_found': 0,
            'images_missing': 0,
            'missing_writers': [],
            'found_writers': [],
            'validation_errors': []
        }

        for writer_name, writer_data in image_mapping.items():
            image_path = self.get_profile_image_path(writer_name)

            if image_path and image_path.exists():
                try:
                    # Try to read the file to validate it
                    with open(image_path, 'rb') as f:
                        f.read(100)  # Read first 100 bytes to check accessibility

                    results['images_found'] += 1
                    results['found_writers'].append(writer_name)
                except Exception as e:
                    results['images_missing'] += 1
                    results['missing_writers'].append(writer_name)
                    results['validation_errors'].append(f"{writer_name}: {e}")
            else:
                results['images_missing'] += 1
                results['missing_writers'].append(writer_name)

        return results

    def list_available_images(self) -> List[Dict[str, Any]]:
        """
        List all available profile images with their metadata.

        Returns:
            List of dictionaries with image information
        """
        image_mapping = self._load_image_mapping()
        available_images = []

        for writer_name in image_mapping:
            image_info = self.get_writer_image_info(writer_name)
            if image_info['has_image']:
                available_images.append({
                    'name': writer_name,
                    'file_name': image_info['file_name'],
                    'cultural_background': image_info['cultural_background'],
                    'era': image_info['era'],
                    'primary_genres': image_info['primary_genres']
                })

        return available_images

    def get_epub_image_item(self, writer_name: str, epub_book) -> Optional[Any]:
        """
        Create an EPUB image item for a writer's profile picture.

        Args:
            writer_name: Name of the writer
            epub_book: The EPUB book object

        Returns:
            EPUB image item or None if image not found
        """
        image_data = self.get_profile_image_data(writer_name)

        if image_data:
            image_bytes, mime_type = image_data
            image_mapping = self._load_image_mapping()

            if writer_name in image_mapping:
                file_name = image_mapping[writer_name]['file_name']

                # Import here to avoid circular imports
                from ebooklib import epub

                # Create EPUB image item
                image_item = epub.EpubItem(
                    uid=f"profile_image_{writer_name.lower().replace(' ', '_')}",
                    file_name=f"images/profiles/{file_name}",
                    media_type=mime_type,
                    content=image_bytes
                )

                return image_item

        return None
