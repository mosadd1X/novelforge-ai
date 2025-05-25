"""
Genre-specific CSS styles for EPUB formatting.

This module provides specialized CSS styles for different genres and format types
to ensure optimal presentation and readability for each content type.
"""

def get_base_css() -> str:
    """Get the base CSS that applies to all genres."""
    return """
        @namespace epub "http://www.idpf.org/2007/ops";

        body {
            font-family: Cambria, Liberation Serif, Bitstream Vera Serif, Georgia, Times, Times New Roman, serif;
            margin: 0 5%;
            text-align: justify;
            line-height: 1.5;
        }

        h1, h2, h3, h4, h5, h6 {
            text-align: center;
            line-height: 1.3;
            font-weight: bold;
            margin: 1em 0;
        }

        h1 {
            font-size: 2em;
            margin: 2em 0 1em;
        }

        h2 {
            font-size: 1.5em;
            margin: 1.5em 0 0.8em;
        }

        p {
            margin: 0.5em 0;
            text-indent: 1.5em;
        }

        .chapter-title {
            margin: 3em 0 2em;
            text-align: center;
            font-size: 2em;
            font-weight: bold;
        }

        .no-indent {
            text-indent: 0;
        }

        .centered {
            text-align: center;
            text-indent: 0;
        }

        .scene-break {
            text-align: center;
            text-indent: 0;
            margin: 1.5em auto;
        }

        .scene-break::before {
            content: "* * *";
        }

        .cover {
            text-align: center;
            padding: 0;
            margin: 0;
        }

        .cover img {
            max-width: 100%;
            max-height: 100%;
            padding: 0;
            margin: 0;
        }

        .series-info {
            font-style: italic;
            color: #666;
            margin-top: 2em;
            font-size: 1.1em;
        }

        /* Front Matter and Back Matter Styles */
        .title-page {
            text-align: center;
            padding-top: 20%;
        }

        .title-content {
            margin: 0 auto;
            max-width: 80%;
        }

        .book-title {
            font-size: 3em;
            margin-bottom: 0.5em;
            font-weight: bold;
        }

        .author-name {
            font-size: 2em;
            margin-top: 1em;
            font-weight: normal;
        }

        .ai-attribution {
            font-style: italic;
            margin-top: 2em;
            font-size: 0.9em;
            color: #666;
        }

        /* Table of Contents Styles */
        .table-of-contents {
            margin: 2em 0;
        }

        .table-of-contents h1 {
            text-align: center;
            margin-bottom: 2em;
            font-size: 2.5em;
        }

        .toc-section {
            margin: 2em 0;
        }

        .toc-section h2 {
            font-size: 1.3em;
            margin-bottom: 0.8em;
            color: #333;
            border-bottom: 1px solid #ddd;
            padding-bottom: 0.3em;
        }

        .toc-section ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
        }

        .toc-section li {
            margin: 0.5em 0;
            padding-left: 1em;
        }

        .toc-section a {
            text-decoration: none;
            color: #333;
            display: block;
            padding: 0.3em 0;
            border-bottom: 1px dotted #ccc;
        }

        .toc-section a:hover {
            color: #0066cc;
            background-color: #f5f5f5;
        }

        /* Profile Image Styles */
        .profile-image {
            float: right;
            margin: 0 0 1em 2em;
            text-align: center;
            max-width: 200px;
        }

        .author-portrait {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .image-caption {
            font-size: 0.9em;
            color: #666;
            font-style: italic;
            margin-top: 0.5em;
            text-indent: 0;
        }

        /* Enhanced Writer Profile Styles */
        .writer-profile h2 {
            color: #2c3e50;
            margin-top: 1.5em;
        }

        .fictional-author-notice {
            background-color: #f8f9fa;
            border-left: 4px solid #6c757d;
            padding: 1em;
            margin: 1.5em 0;
            font-size: 0.95em;
        }

        .fictional-author-notice p {
            margin: 0;
            text-indent: 0;
        }

        /* Enhanced Author Section Layout */
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

        .author-biography {
            margin-bottom: 25px;
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
            text-indent: 0;
        }

        .current-book-description strong {
            color: #2c3e50;
            font-style: normal;
        }

        .other-books-section {
            margin-top: 40px;
            padding-top: 30px;
            border-top: 2px solid #e8e8e8;
        }

        .other-books-section h3 {
            font-size: 1.6em;
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
        }

        .other-books-gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 20px;
            justify-content: center;
        }

        .other-book-item {
            display: flex;
            gap: 12px;
            padding: 15px;
            background-color: #f8f9fa;
            border-radius: 8px;
            border: 1px solid #e8e8e8;
            max-width: 400px;
            width: 100%;
            min-width: 250px;
        }

        .other-book-cover {
            flex-shrink: 0;
            width: 60px;
        }

        .other-book-thumbnail {
            width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .other-book-info {
            flex: 1;
        }

        .other-book-info h4 {
            font-size: 1.1em;
            color: #2c3e50;
            margin: 0 0 8px 0;
            line-height: 1.3;
            text-indent: 0;
        }

        .other-book-desc {
            font-size: 0.9em;
            color: #666;
            margin: 0;
            line-height: 1.4;
            text-indent: 0;
        }

        /* Fallback for e-readers that don't support flexbox */
        @media not all and (min-resolution: .001dpcm) {
            .author-content-wrapper {
                display: block;
            }

            .profile-image-enhanced {
                float: right;
                margin: 0 0 1em 2em;
                width: 150px;
            }

            .other-books-gallery {
                display: block;
            }

            .other-book-item {
                display: block;
                margin-bottom: 1em;
            }

            .other-book-cover {
                float: left;
                margin-right: 1em;
            }
        }

        /* General list styles */
        .writer-profile ul,
        .series-information ul,
        .genre-recommendations ul,
        .technical-details ul,
        .about-generation ul {
            list-style-type: disc;
            margin-left: 2em;
        }

        .writer-profile li,
        .series-information li,
        .genre-recommendations li,
        .technical-details li,
        .about-generation li {
            margin-bottom: 0.5em;
        }

        /* Genre Recommendations Styles */
        .genre-recommendations h2 {
            color: #2c3e50;
            margin-top: 1.5em;
        }

        .genre-recommendations ul {
            background-color: #f8f9fa;
            padding: 1em;
            border-radius: 5px;
        }

        /* Series Cover Gallery Styles */
        .series-covers {
            margin: 2em 0;
            text-align: center;
        }

        .cover-gallery {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 1em;
            margin: 1em 0;
        }

        .series-cover-item {
            text-align: center;
            margin: 0.5em;
            max-width: 120px;
        }

        .series-cover-thumbnail {
            width: 100px;
            height: 150px;
            object-fit: cover;
            border: 2px solid #ddd;
            border-radius: 4px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        }

        .series-cover-thumbnail:hover {
            transform: scale(1.05);
            border-color: #999;
        }

        .cover-caption {
            font-size: 0.8em;
            margin: 0.5em 0 0 0;
            text-indent: 0;
            color: #666;
            font-weight: bold;
        }

        /* Fallback for older e-readers that don't support flexbox */
        @media not all and (min-resolution: .001dpcm) {
            .cover-gallery {
                display: block;
                text-align: center;
            }

            .series-cover-item {
                display: inline-block;
                vertical-align: top;
                margin: 0.5em;
            }
        }
    """

def get_poetry_css() -> str:
    """Get CSS styles specific to poetry collections."""
    return """
        /* Poetry Collection Specific Styles */
        .poetry-section {
            margin: 2em 0;
        }

        .poem {
            margin: 2em 0;
            page-break-inside: avoid;
        }

        .poem-title {
            text-align: center;
            font-weight: bold;
            font-size: 1.3em;
            margin: 1.5em 0 1em;
            text-indent: 0;
        }

        .poem-content {
            text-align: left;
            text-indent: 0;
            line-height: 1.6;
            margin: 1em 0;
        }

        .poem-content p {
            text-indent: 0;
            margin: 0.3em 0;
            text-align: left;
        }

        .stanza {
            margin: 1em 0;
        }

        .stanza-break {
            margin: 1.5em 0;
        }

        .poem-separator {
            text-align: center;
            margin: 2em 0;
            font-size: 1.2em;
        }

        .poem-separator::before {
            content: "***";
        }

        .section-divider {
            text-align: center;
            margin: 3em 0;
            font-size: 1.5em;
            font-weight: bold;
        }

        /* Preserve line breaks in poetry */
        .poetry-line {
            display: block;
            margin: 0.2em 0;
            text-indent: 0;
        }

        .indented-line {
            margin-left: 2em;
        }

        .centered-line {
            text-align: center;
        }
    """

def get_cookbook_css() -> str:
    """Get CSS styles specific to cookbooks."""
    return """
        /* Cookbook Specific Styles */
        .recipe {
            margin: 2em 0;
            page-break-inside: avoid;
        }

        .recipe-title {
            font-size: 1.4em;
            font-weight: bold;
            margin: 1.5em 0 0.5em;
            text-align: center;
            text-indent: 0;
        }

        .recipe-description {
            font-style: italic;
            text-align: center;
            margin: 0.5em 0 1em;
            text-indent: 0;
        }

        .ingredients {
            margin: 1em 0;
        }

        .ingredients-title {
            font-weight: bold;
            margin: 1em 0 0.5em;
            text-indent: 0;
        }

        .ingredients ul {
            list-style-type: disc;
            margin-left: 2em;
        }

        .instructions {
            margin: 1em 0;
        }

        .instructions-title {
            font-weight: bold;
            margin: 1em 0 0.5em;
            text-indent: 0;
        }

        .instructions ol {
            margin-left: 2em;
        }

        .cooking-tip {
            background-color: #f9f9f9;
            border-left: 4px solid #ccc;
            padding: 0.5em 1em;
            margin: 1em 0;
            font-style: italic;
        }

        .prep-time, .cook-time, .servings {
            display: inline-block;
            margin: 0.5em 1em 0.5em 0;
            font-weight: bold;
        }
    """

def get_travel_css() -> str:
    """Get CSS styles specific to travel guides."""
    return """
        /* Travel Guide Specific Styles */
        .destination {
            margin: 2em 0;
        }

        .destination-title {
            font-size: 1.4em;
            font-weight: bold;
            margin: 1.5em 0 0.5em;
            text-indent: 0;
        }

        .location-info {
            background-color: #f0f8ff;
            border: 1px solid #ddd;
            padding: 1em;
            margin: 1em 0;
        }

        .practical-info {
            background-color: #fff8dc;
            border-left: 4px solid #ffd700;
            padding: 0.5em 1em;
            margin: 1em 0;
        }

        .travel-tip {
            background-color: #f0fff0;
            border-left: 4px solid #90ee90;
            padding: 0.5em 1em;
            margin: 1em 0;
            font-style: italic;
        }

        .rating {
            font-weight: bold;
            color: #ff6347;
        }

        .address, .hours, .price {
            font-family: monospace;
            background-color: #f5f5f5;
            padding: 0.2em 0.5em;
            margin: 0.2em 0;
        }
    """

def get_self_help_css() -> str:
    """Get CSS styles specific to self-help books."""
    return """
        /* Self-Help Book Specific Styles */
        .exercise {
            background-color: #f0f8ff;
            border: 2px solid #4682b4;
            padding: 1em;
            margin: 1.5em 0;
            border-radius: 5px;
        }

        .exercise-title {
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 0.5em;
            text-indent: 0;
        }

        .key-point {
            background-color: #fffacd;
            border-left: 4px solid #ffd700;
            padding: 0.5em 1em;
            margin: 1em 0;
        }

        .action-item {
            background-color: #f0fff0;
            border-left: 4px solid #32cd32;
            padding: 0.5em 1em;
            margin: 1em 0;
        }

        .reflection-question {
            font-style: italic;
            text-align: center;
            margin: 1.5em 0;
            padding: 1em;
            background-color: #f5f5f5;
        }

        .chapter-summary {
            background-color: #e6e6fa;
            border: 1px solid #dda0dd;
            padding: 1em;
            margin: 2em 0;
        }

        .summary-title {
            font-weight: bold;
            margin-bottom: 0.5em;
            text-indent: 0;
        }
    """

def get_biography_css() -> str:
    """Get CSS styles specific to biographies and memoirs."""
    return """
        /* Biography/Memoir Specific Styles */
        .timeline {
            margin: 1.5em 0;
            border-left: 3px solid #ccc;
            padding-left: 1em;
        }

        .timeline-event {
            margin: 1em 0;
            position: relative;
        }

        .timeline-date {
            font-weight: bold;
            color: #666;
            margin-bottom: 0.3em;
            text-indent: 0;
        }

        .timeline-event::before {
            content: "•";
            position: absolute;
            left: -1.3em;
            color: #666;
            font-weight: bold;
        }

        .quote {
            font-style: italic;
            text-align: center;
            margin: 1.5em 0;
            padding: 1em;
            background-color: #f9f9f9;
            border-left: 4px solid #ccc;
        }

        .quote-attribution {
            text-align: right;
            font-weight: bold;
            margin-top: 0.5em;
            text-indent: 0;
        }

        .life-stage {
            margin: 2em 0;
            border-top: 2px solid #ddd;
            padding-top: 1em;
        }

        .life-stage-title {
            font-size: 1.3em;
            font-weight: bold;
            margin-bottom: 1em;
            text-indent: 0;
        }
    """

def get_business_css() -> str:
    """Get CSS styles specific to business books."""
    return """
        /* Business Book Specific Styles */
        .case-study {
            background-color: #f8f8f8;
            border: 1px solid #ddd;
            padding: 1em;
            margin: 1.5em 0;
        }

        .case-study-title {
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 0.5em;
            text-indent: 0;
        }

        .strategy {
            background-color: #e6f3ff;
            border-left: 4px solid #0066cc;
            padding: 0.5em 1em;
            margin: 1em 0;
        }

        .best-practice {
            background-color: #f0fff0;
            border-left: 4px solid #32cd32;
            padding: 0.5em 1em;
            margin: 1em 0;
        }

        .warning {
            background-color: #fff0f0;
            border-left: 4px solid #ff4444;
            padding: 0.5em 1em;
            margin: 1em 0;
        }

        .metrics {
            font-family: monospace;
            background-color: #f5f5f5;
            padding: 1em;
            margin: 1em 0;
            border: 1px solid #ddd;
        }

        .framework {
            border: 2px solid #666;
            padding: 1em;
            margin: 1.5em 0;
        }

        .framework-title {
            font-weight: bold;
            font-size: 1.2em;
            margin-bottom: 0.5em;
            text-indent: 0;
        }
    """

def get_academic_css() -> str:
    """Get CSS styles specific to academic and educational books."""
    return """
        /* Academic/Educational Book Specific Styles */
        .definition {
            background-color: #f0f8ff;
            border: 1px solid #b0c4de;
            padding: 1em;
            margin: 1em 0;
        }

        .definition-term {
            font-weight: bold;
            font-size: 1.1em;
            margin-bottom: 0.5em;
            text-indent: 0;
        }

        .theorem, .principle {
            background-color: #fff8dc;
            border: 2px solid #daa520;
            padding: 1em;
            margin: 1.5em 0;
        }

        .example {
            background-color: #f5f5f5;
            border-left: 4px solid #888;
            padding: 0.5em 1em;
            margin: 1em 0;
        }

        .example-title {
            font-weight: bold;
            margin-bottom: 0.5em;
            text-indent: 0;
        }

        .footnote {
            font-size: 0.9em;
            color: #666;
            border-top: 1px solid #ddd;
            padding-top: 0.5em;
            margin-top: 2em;
        }

        .bibliography {
            font-size: 0.9em;
            margin-left: 2em;
            text-indent: -2em;
        }

        .chapter-objectives {
            background-color: #e6ffe6;
            border: 1px solid #90ee90;
            padding: 1em;
            margin: 1em 0;
        }

        .objectives-title {
            font-weight: bold;
            margin-bottom: 0.5em;
            text-indent: 0;
        }
    """

def get_essay_css() -> str:
    """Get CSS styles specific to essay collections."""
    return """
        /* Essay Collection Specific Styles */
        .essay {
            margin: 2em 0;
            page-break-before: always;
        }

        .essay-title {
            font-size: 1.4em;
            font-weight: bold;
            text-align: center;
            margin: 2em 0 1em;
            text-indent: 0;
        }

        .essay-subtitle {
            font-style: italic;
            text-align: center;
            margin: 0.5em 0 1.5em;
            text-indent: 0;
        }

        .essay-epigraph {
            font-style: italic;
            text-align: center;
            margin: 1em 0 2em;
            font-size: 0.9em;
            color: #666;
        }

        .essay-separator {
            text-align: center;
            margin: 3em 0;
            font-size: 1.5em;
        }

        .essay-separator::before {
            content: "◊ ◊ ◊";
        }

        .reflection {
            font-style: italic;
            margin: 1.5em 0;
            padding: 1em;
            background-color: #f9f9f9;
        }
    """

def get_short_story_css() -> str:
    """Get CSS styles specific to short story collections."""
    return """
        /* Short Story Collection Specific Styles */
        .story {
            margin: 2em 0;
            page-break-before: always;
        }

        .story-title {
            font-size: 1.4em;
            font-weight: bold;
            text-align: center;
            margin: 2em 0 1em;
            text-indent: 0;
        }

        .story-separator {
            text-align: center;
            margin: 3em 0;
            font-size: 1.2em;
        }

        .story-separator::before {
            content: "~ ~ ~";
        }

        .story-epigraph {
            font-style: italic;
            text-align: center;
            margin: 1em 0 2em;
            font-size: 0.9em;
        }
    """

def get_graphic_novel_css() -> str:
    """Get CSS styles specific to graphic novels."""
    return """
        /* Graphic Novel Specific Styles */
        .panel-description {
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            padding: 0.5em;
            margin: 0.5em 0;
            font-style: italic;
        }

        .dialogue {
            font-weight: bold;
            margin: 0.3em 0;
            text-indent: 0;
        }

        .character-name {
            font-weight: bold;
            text-transform: uppercase;
            margin: 0.5em 0 0.2em;
            text-indent: 0;
        }

        .sound-effect {
            font-weight: bold;
            font-style: italic;
            text-align: center;
            margin: 0.5em 0;
            text-indent: 0;
        }

        .page-break {
            page-break-after: always;
            text-align: center;
            margin: 2em 0;
        }

        .visual-description {
            color: #666;
            font-style: italic;
            margin: 0.5em 0;
            text-indent: 0;
        }
    """

def get_genre_specific_css(format_type: str) -> str:
    """
    Get CSS styles for a specific format type.

    Args:
        format_type: The format type (poetry, cookbook, travel, etc.)

    Returns:
        str: CSS styles for the format type
    """
    css_functions = {
        "poetry": get_poetry_css,
        "cookbook": get_cookbook_css,
        "travel": get_travel_css,
        "self_help": get_self_help_css,
        "biography": get_biography_css,
        "business": get_business_css,
        "academic": get_academic_css,
        "essay": get_essay_css,
        "short_story": get_short_story_css,
        "graphic_novel": get_graphic_novel_css
    }

    if format_type in css_functions:
        return css_functions[format_type]()
    else:
        return ""

def get_complete_css(format_type: str = "standard") -> str:
    """
    Get complete CSS including base styles and format-specific styles.

    Args:
        format_type: The format type for specialized styling

    Returns:
        str: Complete CSS content
    """
    base_css = get_base_css()
    genre_css = get_genre_specific_css(format_type)

    return base_css + "\n" + genre_css
