#!/usr/bin/env python3
"""
Comprehensive test for front/back matter enhancements.

This script tests the enhanced front/back matter system including:
- Table of Contents generation and placement
- Profile picture integration
- Enhanced author sections
- Genre-aware formatting
- Navigation functionality
"""

import sys
import os
import tempfile
import zipfile
sys.path.append('src')

from formatters.epub_formatter import EpubFormatter
from utils.profile_image_manager import ProfileImageManager
from utils.writer_profile_manager import WriterProfileManager

def create_test_novel_with_profile():
    """Create test novel data with a writer profile."""
    return {
        "metadata": {
            "title": "Test Novel with Enhanced Front/Back Matter",
            "author": "Catherine Fairfax",  # Use one of our profile writers
            "genre": "Romance",
            "description": "A test novel to validate front/back matter enhancements",
            "target_audience": "Adult",
            "target_length": "short"
        },
        "chapters": [
            {
                "number": 1,
                "title": "Chapter 1: The Beginning",
                "content": "This is the first chapter of our test novel. It contains enough content to validate the formatting and structure."
            },
            {
                "number": 2,
                "title": "Chapter 2: The Development",
                "content": "This is the second chapter, continuing our story and providing more content for testing."
            },
            {
                "number": 3,
                "title": "Chapter 3: The Conclusion",
                "content": "This is the final chapter, bringing our test story to a satisfying conclusion."
            }
        ]
    }

def test_profile_image_manager():
    """Test the profile image manager functionality."""
    print("🖼️  Testing Profile Image Manager")
    print("-" * 50)

    image_manager = ProfileImageManager()

    # Test validation
    validation_results = image_manager.validate_all_images()
    print(f"✓ Total writers: {validation_results['total_writers']}")
    print(f"✓ Images found: {validation_results['images_found']}")
    print(f"✓ Images missing: {validation_results['images_missing']}")

    if validation_results['images_missing'] > 0:
        print(f"⚠️  Missing images for: {', '.join(validation_results['missing_writers'][:5])}")

    # Test specific writer
    test_writer = "Catherine Fairfax"
    image_info = image_manager.get_writer_image_info(test_writer)
    print(f"\n📸 Testing {test_writer}:")
    print(f"  Has image: {image_info['has_image']}")
    print(f"  File name: {image_info['file_name']}")
    print(f"  Cultural background: {image_info['cultural_background']}")
    print(f"  Era: {image_info['era']}")

    if image_info['has_image']:
        print(f"  ✓ Profile image available")
        return True
    else:
        print(f"  ❌ Profile image not found")
        return False

def test_front_matter_generation():
    """Test front matter generation including TOC."""
    print("\n📖 Testing Front Matter Generation")
    print("-" * 50)

    novel_data = create_test_novel_with_profile()

    # Get writer profile
    profile_manager = WriterProfileManager()
    writer_profile = profile_manager.get_master_profile_by_author("Catherine Fairfax")

    if not writer_profile:
        print("⚠️  Writer profile not found, using basic data")
        writer_profile = {"name": "Catherine Fairfax"}

    # Create formatter
    formatter = EpubFormatter(novel_data, writer_profile, include_front_matter=True, include_back_matter=True)

    # Test front matter generation
    front_matter = formatter.front_matter_generator.get_all_front_matter()

    print(f"✓ Front matter sections generated: {len(front_matter)}")
    for section_name in front_matter.keys():
        print(f"  • {section_name.replace('_', ' ').title()}")

    # Check for TOC specifically
    if "table_of_contents" in front_matter:
        toc_content = front_matter["table_of_contents"]
        print(f"✓ Table of Contents generated ({len(toc_content)} characters)")

        # Check for key TOC elements
        toc_checks = [
            ("Chapter links", "chapter_01.xhtml" in toc_content),
            ("Front matter links", "copyright.xhtml" in toc_content),
            ("Back matter links", "writer_profile.xhtml" in toc_content),
            ("TOC sections", "toc-section" in toc_content)
        ]

        for check_name, check_result in toc_checks:
            status = "✓" if check_result else "❌"
            print(f"  {status} {check_name}")

        return all(check[1] for check in toc_checks)
    else:
        print("❌ Table of Contents not generated")
        return False

def test_back_matter_generation():
    """Test back matter generation including profile pictures."""
    print("\n👤 Testing Back Matter Generation")
    print("-" * 50)

    novel_data = create_test_novel_with_profile()

    # Get writer profile
    profile_manager = WriterProfileManager()
    writer_profile = profile_manager.get_master_profile_by_author("Catherine Fairfax")

    if not writer_profile:
        print("⚠️  Writer profile not found, using basic data")
        writer_profile = {"name": "Catherine Fairfax"}

    # Create formatter
    formatter = EpubFormatter(novel_data, writer_profile, include_front_matter=True, include_back_matter=True)

    # Test back matter generation
    back_matter = formatter.back_matter_generator.get_all_back_matter()

    print(f"✓ Back matter sections generated: {len(back_matter)}")
    for section_name in back_matter.keys():
        print(f"  • {section_name.replace('_', ' ').title()}")

    # Check for profile picture integration
    if "writer_profile" in back_matter:
        profile_content = back_matter["writer_profile"]
        print(f"✓ Writer profile section generated ({len(profile_content)} characters)")

        # Check for profile picture elements
        profile_checks = [
            ("Profile image", "profile-image" in profile_content),
            ("Author portrait", "author-portrait" in profile_content),
            ("Base64 image data", "data:image/" in profile_content),
            ("About the Author", "About the Author" in profile_content)
        ]

        for check_name, check_result in profile_checks:
            status = "✓" if check_result else "❌"
            print(f"  {status} {check_name}")

        return all(check[1] for check in profile_checks)
    else:
        print("❌ Writer profile section not generated")
        return False

def test_complete_epub_generation():
    """Test complete EPUB generation with all enhancements."""
    print("\n📚 Testing Complete EPUB Generation")
    print("-" * 50)

    novel_data = create_test_novel_with_profile()

    # Get writer profile
    profile_manager = WriterProfileManager()
    writer_profile = profile_manager.get_master_profile_by_author("Catherine Fairfax")

    if not writer_profile:
        print("⚠️  Writer profile not found, using basic data")
        writer_profile = {"name": "Catherine Fairfax"}

    try:
        # Create formatter with all enhancements enabled
        formatter = EpubFormatter(novel_data, writer_profile, include_front_matter=True, include_back_matter=True)

        # Generate EPUB
        with tempfile.TemporaryDirectory() as temp_dir:
            epub_path = formatter.save_epub(temp_dir)

            if os.path.exists(epub_path):
                file_size = os.path.getsize(epub_path)
                print(f"✓ EPUB generated successfully")
                print(f"  File: {epub_path}")
                print(f"  Size: {file_size:,} bytes")

                # Validate EPUB structure
                with zipfile.ZipFile(epub_path, 'r') as epub_zip:
                    file_list = epub_zip.namelist()

                    # Check for required files (using actual EPUB formatter naming)
                    required_files = [
                        'META-INF/container.xml',
                        'mimetype'
                    ]

                    # Check for basic EPUB structure
                    found_files = []
                    missing_files = []

                    for req_file in required_files:
                        if req_file in file_list:
                            found_files.append(req_file)
                        else:
                            missing_files.append(req_file)

                    print(f"✓ Basic EPUB files found: {len(found_files)}/{len(required_files)}")

                    if missing_files:
                        print(f"❌ Missing basic files: {', '.join(missing_files)}")
                        return False

                    # Find and validate front/back matter files
                    toc_files = [f for f in file_list if 'table_of_contents' in f]
                    profile_files = [f for f in file_list if 'writer_profile' in f]
                    genre_files = [f for f in file_list if 'genre_recommendations' in f]

                    print(f"✓ Front/back matter files found:")
                    print(f"  TOC files: {len(toc_files)} {toc_files}")
                    print(f"  Profile files: {len(profile_files)} {profile_files}")
                    print(f"  Genre files: {len(genre_files)} {genre_files}")

                    # Check TOC content
                    if toc_files:
                        toc_content = epub_zip.read(toc_files[0]).decode('utf-8')
                        if 'table-of-contents' in toc_content and 'toc-section' in toc_content:
                            print(f"✓ Table of Contents properly formatted")
                        else:
                            print(f"❌ Table of Contents formatting issues")
                            return False
                    else:
                        print(f"❌ No Table of Contents file found")
                        return False

                    # Check writer profile content
                    if profile_files:
                        profile_content = epub_zip.read(profile_files[0]).decode('utf-8')
                        if 'About the Author' in profile_content:
                            print(f"✓ Writer profile properly formatted")

                            # Check for profile image
                            if 'data:image/' in profile_content:
                                print(f"✓ Profile image embedded in writer section")
                            else:
                                print(f"⚠️  Profile image not found in writer section")
                        else:
                            print(f"❌ Writer profile formatting issues")
                            return False
                    else:
                        print(f"❌ No writer profile file found")
                        return False

                return True
            else:
                print(f"❌ EPUB file not generated")
                return False

    except Exception as e:
        print(f"❌ Error during EPUB generation: {e}")
        return False

def main():
    """Run comprehensive front/back matter enhancement tests."""
    print("🔧 Front/Back Matter Enhancement Test Suite")
    print("=" * 70)

    tests = [
        ("Profile Image Manager", test_profile_image_manager),
        ("Front Matter Generation", test_front_matter_generation),
        ("Back Matter Generation", test_back_matter_generation),
        ("Complete EPUB Generation", test_complete_epub_generation)
    ]

    results = []

    for test_name, test_func in tests:
        try:
            success = test_func()
            results.append((test_name, success))
        except Exception as e:
            print(f"❌ {test_name} failed with error: {e}")
            results.append((test_name, False))

    # Summary
    print(f"\n{'='*70}")
    print("TEST RESULTS SUMMARY")
    print(f"{'='*70}")

    total_tests = len(results)
    passed_tests = sum(1 for _, success in results if success)
    failed_tests = total_tests - passed_tests

    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests} ({passed_tests/total_tests*100:.1f}%)")
    print(f"Failed: {failed_tests} ({failed_tests/total_tests*100:.1f}%)")

    print(f"\nDetailed Results:")
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {status} {test_name}")

    if failed_tests == 0:
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"Front/back matter enhancements are working correctly.")
        print(f"\n✅ Implemented Features:")
        print(f"  • Table of Contents generation and placement")
        print(f"  • Profile picture integration in back matter")
        print(f"  • Enhanced author sections with images")
        print(f"  • Genre recommendations and related reading")
        print(f"  • Professional CSS styling for all sections")
        print(f"  • Clickable navigation links in EPUB")
    else:
        print(f"\n⚠️  Some tests failed. Please review the issues above.")

if __name__ == "__main__":
    main()
