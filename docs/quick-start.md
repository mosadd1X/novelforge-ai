---
layout: default
title: Quick Start Guide
nav_order: 3
description: "A quick guide to generating your first book with the Ebook Generator"
---

# Quick Start Guide
{: .no_toc }

This guide will walk you through generating your first book with the Ebook Generator.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Generating a Single Book

### Step 1: Launch the Application

Start the application using the run script:

```bash
python run.py
```

### Step 2: Select "Generate a Book"

From the main menu, select option 1: "Generate a Book"

### Step 3: Enter Book Information

You'll be prompted to enter basic information about your book:

1. **Title**: Enter a title for your book
   ```
   Enter a title for your book: The Quantum Garden
   ```

2. **Author**: Enter an author name
   ```
   Enter the author name: Dr. Elise Moreau
   ```

3. **Genre**: Select a genre from the list or enter a custom genre
   ```
   Select a genre: Science Fiction
   ```

4. **Target Audience**: Select the intended audience
   ```
   Select target audience: Adult (18+)
   ```

5. **Description**: Enter a brief description of your book
   ```
   Enter a description: A physicist discovers a way to manipulate quantum
   particles to accelerate plant growth, creating a garden where time
   flows differently.
   ```

### Step 4: Customize Generation Options (Optional)

You'll be asked if you want to customize generation options:

```
Would you like to customize generation options? (y/n): y
```

If you select "yes," you can customize:
- Chapter count
- Target word count
- Writing style
- Point of view
- Themes
- And more...

For your first book, you can select "no" to use the default options for your chosen genre.

### Step 5: Confirm Generation

Review the information and confirm to start generation:

```
Ready to generate "The Quantum Garden"? (y/n): y
```

### Step 6: Monitor Generation Progress

The system will now:
1. Generate a writer profile
2. Create a novel outline
3. Develop characters
4. Generate chapters one by one
5. Format the final EPUB

Progress will be displayed in the terminal with colorful indicators.

### Step 7: Get Your Book

Once generation is complete, you'll see a success message with the location of your generated book:

```
Book generation complete!
EPUB file saved to: output/The_Quantum_Garden/The_Quantum_Garden.epub
```

Congratulations! You've generated your first book.

## Generating a Series

### Step 1: Launch the Application

Start the application:

```bash
python run.py
```

### Step 2: Select "Generate a Series"

From the main menu, select option 2: "Generate a Series"

### Step 3: Enter Series Information

You'll be prompted to enter information about your series:

1. **Series Title**: Enter a title for your series
   ```
   Enter a title for your series: The Elemental Chronicles
   ```

2. **Author**: Enter an author name
   ```
   Enter the author name: Aria Flameheart
   ```

3. **Genre**: Select a genre
   ```
   Select a genre: Fantasy
   ```

4. **Target Audience**: Select the intended audience
   ```
   Select target audience: Young Adult
   ```

5. **Description**: Enter a brief description of your series
   ```
   Enter a description: A sweeping fantasy saga where four young mages,
   each wielding one of the primal elements, must unite to prevent an
   ancient darkness from consuming their world.
   ```

6. **Planned Books**: Enter the number of books in the series
   ```
   Enter the number of books in the series: 4
   ```

### Step 4: Generate Series Plan

The system will generate a plan for the entire series, including:
- Overarching plot arc
- Character development across books
- Individual book outlines

### Step 5: Generate Books

You'll be asked if you want to generate the first book:

```
Would you like to generate Book 1: "The Flame Awakens"? (y/n): y
```

The generation process for each book is similar to generating a single book.

### Step 6: Continue Series Generation

After each book is generated, you'll be asked if you want to continue with the next book:

```
Would you like to generate Book 2: "Tides of Change"? (y/n): y
```

You can generate all books in one session or return later to continue the series.

### Step 7: Zip Your Series (Optional)

Once you have generated multiple books in your series, you can create a zip archive for easy sharing:

1. From the series management menu, select "Zip Series Books"
2. Choose which file formats to include (EPUB only, all ebook formats, or everything)
3. Select where to save the zip file (series directory, Desktop, Downloads, or custom location)
4. Enter a filename for the zip archive
5. The system will create a compressed archive with all your books organized in folders

The zip file will contain:
- Series information file
- Each book in its own numbered folder (Book_01, Book_02, etc.)
- All selected file formats for each book

This makes it easy to share your complete series with others or backup your work.

## Using Book and Series Ideas

The Ebook Generator comes with pre-defined book and series ideas that you can use for testing or inspiration.

### Using a Pre-defined Book Idea

1. When prompted for book information, select "Use a pre-defined book idea"
2. Browse and select from the available ideas
3. The system will fill in the title, author, genre, and description automatically
4. You can still customize these values if desired

### Using a Pre-defined Series Idea

1. When prompted for series information, select "Use a pre-defined series idea"
2. Browse and select from the available series ideas
3. The system will fill in all the necessary information
4. You can still customize the values if desired

## Next Steps

Now that you've generated your first book or series, you might want to:

- Learn about [Configuration Options](./configuration.html) to customize the generation process
- Explore [Memory Management](./components/memory-management.html) to understand how consistency is maintained
- Check out [Cover Generation](./components/cover-generator.html) to create custom covers
- Read about [EPUB Formatting](./components/epub-formatting.html) to customize the output format

For more advanced usage, see the [API Documentation](./api.html) to integrate the Ebook Generator into your own applications.
