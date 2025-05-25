---
layout: default
title: Troubleshooting
nav_order: 9
description: 'Solutions for common issues encountered when using the Ebook Generator'
permalink: /troubleshooting
---

# Troubleshooting

{: .no_toc }

This guide provides solutions for common issues encountered when using the Ebook Generator.
{: .fs-6 .fw-300 }

## Table of Contents

{: .no_toc .text-delta }

1. TOC
   {:toc}

---

## API Key Issues

### Invalid API Key

**Symptoms:**

- Error message: "Invalid API key"
- Generation fails immediately
- API key status shows as invalid

**Solutions:**

1. Verify that your API key is correctly copied from the Google AI Studio
2. Check for extra spaces or line breaks in your `.env` file
3. Ensure your API key has not expired
4. Try generating a new API key from the Google AI Studio

### Rate Limit Exceeded

**Symptoms:**

- Error message: "Rate limit exceeded"
- Generation pauses or fails after several chapters
- API key status shows as rate-limited

**Solutions:**

1. Configure multiple API keys as described in [Multiple API Keys](./multiple-api-keys.html)
2. Wait for the rate limit cooldown period (usually 60 seconds to a few minutes)
3. Reduce the generation frequency by adding delays between API calls
4. Consider upgrading to a paid API tier for higher rate limits

### Quota Exceeded

**Symptoms:**

- Error message: "Quota exceeded"
- Generation fails completely
- API key status shows as quota exceeded

**Solutions:**

1. Wait until your quota resets (typically at the start of the next day)
2. Use alternative API keys from different accounts
3. Upgrade to a paid API tier with higher quotas
4. Reduce the size of your generation requests

## Generation Issues

### Inconsistent Characters

**Symptoms:**

- Characters behave differently across chapters
- Character traits or backgrounds change
- Relationships between characters are inconsistent

**Solutions:**

1. Check that the Memory Manager is properly initialized
2. Ensure character extraction is working correctly after each chapter
3. Verify that the context provided to each chapter includes character information
4. Try regenerating the problematic chapters with more explicit character context

### Plot Holes

**Symptoms:**

- Plot threads are introduced but never resolved
- Events contradict earlier established facts
- Character motivations don't align with their actions

**Solutions:**

1. Review the narrative tracking in the Memory Manager
2. Check that plot points are being properly extracted and tracked
3. Provide more explicit plot guidance in the generation options
4. Consider regenerating problematic chapters with more context

### Short Chapters

**Symptoms:**

- Chapters are consistently shorter than the target length
- The system frequently needs to extend chapters
- Final word count is below the target

**Solutions:**

1. Increase the `min_chapter_length` setting in your generation options
2. Modify the chapter generation prompt to request more detailed descriptions
3. Adjust the `temperature` setting to encourage more verbose output
4. Check that the genre defaults are appropriate for your content

### Generation Timeouts

**Symptoms:**

- Generation process hangs or times out
- Error message: "Request timed out"
- Incomplete chapters or books

**Solutions:**

1. Check your internet connection
2. Increase the timeout settings in your configuration
3. Try generating smaller chunks of content at a time
4. Verify that the Gemini API service is operational

## EPUB Formatting Issues

### Missing Cover

**Symptoms:**

- EPUB file has no cover image
- Cover page is blank or missing

**Solutions:**

1. Verify that a cover path was provided to the EPUB formatter
2. Check that the cover file exists and is a valid image format
3. Ensure the cover generator is working correctly
4. Try generating a new cover with explicit dimensions

### Formatting Problems

**Symptoms:**

- Text formatting is inconsistent
- Paragraphs are not properly separated
- Special characters appear as gibberish

**Solutions:**

1. Check that the content is properly converted to HTML
2. Verify that the CSS styling is correctly applied
3. Ensure the content is encoded in UTF-8
4. Try regenerating the EPUB with simpler formatting

### E-reader Compatibility

**Symptoms:**

- EPUB works in some e-readers but not others
- Strange formatting on certain devices
- Navigation issues in the EPUB

**Solutions:**

1. Validate your EPUB using the [EPUB Validator](https://validator.idpf.org/)
2. Simplify the CSS styling for better compatibility
3. Ensure you're using EPUB 3.0 standard features
4. Test with multiple e-readers and adjust formatting as needed

## Installation Issues

### Dependency Errors

**Symptoms:**

- Error messages during installation
- Missing dependencies
- Import errors when running the application

**Solutions:**

1. Ensure you're using Python 3.8 or higher
2. Install dependencies with `pip install -r requirements.txt`
3. Check for conflicting package versions
4. Try creating a fresh virtual environment

### Permission Issues

**Symptoms:**

- Permission denied errors
- Cannot write to output directory
- Cannot access API key file

**Solutions:**

1. Run the application with appropriate permissions
2. Check file and directory permissions
3. Ensure the output directory exists and is writable
4. Verify that the `.env` file is readable

## Memory Issues

**Symptoms:**

- Application crashes with memory errors
- System becomes unresponsive during generation
- Out of memory errors

**Solutions:**

1. Reduce the size of the context window
2. Generate fewer chapters at a time
3. Close other memory-intensive applications
4. Increase available system memory or swap space

## Common Error Messages

### "No module named 'src'"

**Solution:**
Run the application from the project root directory or install the package with `pip install -e .`

### "Could not find a valid Gemini API key"

**Solution:**
Ensure your `.env` file contains a valid `GEMINI_API_KEY` entry

### "Failed to generate content after multiple retries"

**Solution:**
Check API key status, internet connection, and try with different generation parameters

### "Memory Manager not initialized"

**Solution:**
Ensure you call `initialize_novel()` before attempting to generate content

## Getting Additional Help

If you're experiencing issues not covered in this guide:

1. Check the [GitHub Issues](https://github.com/mosadd1X/novelforge-ai/issues) for similar problems
2. Search the [Discussions](https://github.com/mosadd1X/novelforge-ai/discussions) for community solutions
3. Open a new issue with detailed information about your problem
4. Include relevant error messages, system information, and steps to reproduce the issue

## Related Documentation

- [Getting Started](./getting-started.html): Basic setup instructions
- [Configuration Options](./configuration.html): Customizing the generation process
- [API Documentation](./api.html): Reference for the project's API
