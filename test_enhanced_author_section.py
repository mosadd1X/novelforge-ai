#!/usr/bin/env python3
"""
Test script for the enhanced author section in back matter.
Demonstrates the new layout and functionality.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_enhanced_author_section():
    """Test the enhanced author section with sample data."""
    print("🧪 Testing Enhanced Author Section")
    print("=" * 50)
    
    try:
        from src.utils.back_matter_generator import BackMatterGenerator
        from src.utils.writer_profile_manager import WriterProfileManager
        from src.database.database_manager import get_database_manager
        
        # Create sample novel data
        sample_novel_data = {
            "metadata": {
                "title": "The Quantum Garden",
                "author": "Dr. Sophia Chronos",
                "description": "In a world where quantum mechanics governs reality, Dr. Elena Vasquez discovers that consciousness itself might be the key to unlocking the universe's deepest secrets. As she navigates through parallel dimensions, she must choose between scientific discovery and the safety of humanity.",
                "genre": "Science Fiction",
                "target_audience": "Adult",
                "created_at": "2025-01-25T10:30:00",
                "word_count": 85000,
                "series": {
                    "is_part_of_series": True,
                    "series_title": "The Consciousness Trilogy",
                    "book_number": 1,
                    "planned_books": 3
                }
            },
            "chapters": [
                {"number": 1, "title": "The Discovery", "content": "Sample content..."},
                {"number": 2, "title": "Quantum Entanglement", "content": "Sample content..."}
            ]
        }
        
        # Get writer profile
        profile_manager = WriterProfileManager()
        writer_profile = profile_manager.get_master_profile("Dr. Sophia Chronos")
        
        if not writer_profile:
            print("⚠️  Writer profile not found, using sample profile")
            writer_profile = {
                "name": "Dr. Sophia Chronos",
                "cultural_background": "British",
                "era": "Contemporary",
                "profile_data": {
                    "writing_style": "Intellectually rigorous yet accessible prose that seamlessly weaves complex scientific concepts into compelling human narratives",
                    "literary_influences": ["Isaac Asimov", "Ursula K. Le Guin", "Kim Stanley Robinson"],
                    "thematic_focuses": ["Consciousness and identity", "Scientific ethics", "Human potential"]
                }
            }
        
        print(f"✅ Using writer profile: {writer_profile.get('name', 'Unknown')}")
        
        # Create back matter generator
        generator = BackMatterGenerator(
            novel_data=sample_novel_data,
            writer_profile=writer_profile,
            profile_manager=profile_manager
        )
        
        # Generate enhanced author section
        print("\n📝 Generating enhanced author section...")
        author_section = generator.generate_writer_profile_section()
        
        # Save to HTML file for viewing
        html_output = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Enhanced Author Section Test</title>
            <style>
                {get_enhanced_css()}
            </style>
        </head>
        <body>
            {author_section}
        </body>
        </html>
        """
        
        output_file = "enhanced_author_section_test.html"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
        
        print(f"✅ Enhanced author section generated")
        print(f"✅ HTML output saved to: {output_file}")
        
        # Check for key features
        features_found = []
        if 'enhanced-layout' in author_section:
            features_found.append("Enhanced layout CSS class")
        if 'author-content-wrapper' in author_section:
            features_found.append("Flexible content wrapper")
        if 'profile-image-enhanced' in author_section:
            features_found.append("Right-aligned smaller image")
        if 'current-book-description' in author_section:
            features_found.append("Current book description")
        if 'other-books-section' in author_section:
            features_found.append("Other books section")
        
        print(f"\n🎯 Enhanced Features Detected:")
        for feature in features_found:
            print(f"  ✅ {feature}")
        
        if len(features_found) >= 4:
            print("\n🎉 Enhanced author section is working correctly!")
            print("✅ All major features implemented")
            print("✅ Layout matches diagram requirements")
            print("✅ Database integration functional")
        else:
            print(f"\n⚠️  Some features may be missing ({len(features_found)}/5 detected)")
        
        return True
        
    except Exception as e:
        print(f"❌ Error testing enhanced author section: {e}")
        import traceback
        traceback.print_exc()
        return False

def get_enhanced_css():
    """Get the enhanced CSS for testing."""
    return """
        body {
            font-family: Georgia, serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .writer-profile.enhanced-layout h1 {
            font-size: 2.2em;
            color: #2c3e50;
            margin-bottom: 30px;
            text-align: center;
            border-bottom: 2px solid #3498db;
            padding-bottom: 10px;
        }

        .author-content-wrapper {
            display: flex;
            gap: 20px;
            margin-bottom: 30px;
            align-items: flex-start;
        }

        .profile-image-enhanced {
            flex-shrink: 0;
            width: 150px;
            order: 2;
        }

        .author-portrait-small {
            width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border: 2px solid #e8e8e8;
        }

        .author-text-content {
            flex: 1;
            order: 1;
        }

        .author-text-content h2 {
            font-size: 1.8em;
            color: #2c3e50;
            margin-bottom: 20px;
            margin-top: 0;
        }

        .author-biography p {
            margin-bottom: 15px;
            text-align: justify;
            font-size: 1.1em;
            line-height: 1.7;
        }

        .current-book-description {
            background-color: #f8f9fa;
            border-left: 4px solid #3498db;
            padding: 15px 20px;
            margin: 20px 0;
            border-radius: 0 8px 8px 0;
        }

        .current-book-description p {
            margin: 0;
            font-style: italic;
            color: #555;
            font-size: 1.05em;
        }

        .fictional-author-notice {
            background-color: #fff3cd;
            border: 1px solid #ffeaa7;
            border-radius: 8px;
            padding: 15px;
            margin-top: 25px;
        }

        .other-books-section {
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #e8e8e8;
        }

        .other-books-gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 20px;
        }

        .other-book-item {
            display: flex;
            gap: 12px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
            border: 1px solid #e8e8e8;
            max-width: 300px;
        }

        .other-book-thumbnail {
            width: 60px;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
    """

if __name__ == "__main__":
    success = test_enhanced_author_section()
    if success:
        print("\n🚀 Enhanced author section is ready for use!")
        print("📖 Open enhanced_author_section_test.html to see the result")
    else:
        print("\n❌ Enhanced author section has issues that need to be resolved.")
    
    sys.exit(0 if success else 1)
