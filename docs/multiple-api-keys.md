---
layout: default
title: Multiple API Key Support
nav_order: 6
description: "Documentation for the multiple API key rotation feature that handles rate limits"
permalink: /multiple-api-keys
---

# Multiple API Key Support
{: .no_toc }

The Ebook Generator supports using multiple Google Gemini API keys to handle rate limits during long generations.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

Generating a complete novel or series requires many API calls to the Gemini API, which can quickly hit rate limits with a single API key. The multiple API key support feature allows you to:

1. Configure multiple API keys in your environment
2. Automatically rotate between keys when rate limits are encountered
3. Monitor the status and usage of each key
4. Continue generation without interruption even when individual keys are rate-limited

## Configuration

### Setting Up Multiple API Keys

To configure multiple API keys, add them to your `.env` file:

```
# Main API key (required)
GEMINI_API_KEY=your_main_api_key_here

# Additional API keys (optional)
GEMINI_API_KEY_1=your_second_api_key_here
GEMINI_API_KEY_2=your_third_api_key_here
GEMINI_API_KEY_3=your_fourth_api_key_here
```

You can add as many additional keys as needed, using sequential numbering (GEMINI_API_KEY_1, GEMINI_API_KEY_2, etc.).

### Key Rotation Strategy

The system uses the following strategy for key rotation:

1. Start with the main API key (`GEMINI_API_KEY`)
2. If a rate limit is encountered, automatically switch to the next available key
3. If all keys are rate-limited, wait for the cooldown period on the first key to expire
4. Continue rotating through keys as needed

## Usage

### Checking API Key Status

You can check the status of your API keys from the main menu:

```bash
python run.py
```

Then select "API Key Status" from the menu.

### Programmatic Access

You can also access the API key management programmatically:

```python
from src.core.gemini_client import GeminiClient

# Create a client instance
client = GeminiClient()

# Check the status of all keys
key_status = client.get_api_key_status()
for key_id, status in key_status.items():
    print(f"Key {key_id}: {'Valid' if status['valid'] else 'Invalid'}")
    
# Manually rotate to the next key
client.rotate_api_key()

# Generate content (will automatically rotate keys if needed)
response = client.generate_content("Your prompt here")
```

## Rate Limit Handling

### Detection

The system detects rate limits through:

1. HTTP 429 responses from the API
2. Error messages indicating quota exceeded
3. Specific error codes in the API response

### Automatic Recovery

When a rate limit is detected:

1. The current operation is paused
2. The system rotates to the next available API key
3. The operation is retried with the new key
4. If successful, generation continues without user intervention

### Manual Intervention

If all keys are rate-limited, the system will:

1. Display a warning message
2. Wait for the cooldown period on the first key
3. Automatically retry when the cooldown expires
4. Provide options for the user to pause or continue

## Best Practices

For optimal use of multiple API keys:

1. **Use Different Accounts**: Obtain API keys from different Google Cloud accounts for true isolation of rate limits
2. **Monitor Usage**: Regularly check key status to ensure you have sufficient capacity
3. **Stagger Usage**: For very large projects, consider manually alternating between keys
4. **Increase Key Count**: For generating multiple books or series, add more API keys
5. **Consider Paid Tiers**: Upgrade to paid API tiers for higher rate limits on critical keys

## Troubleshooting

Common issues and solutions:

- **Invalid Keys**: Ensure all API keys are correctly formatted and valid
- **Persistent Rate Limits**: Check if you've exceeded daily quotas rather than just rate limits
- **Inconsistent Behavior**: Verify that keys are from different accounts to avoid shared limits
- **Missing Keys**: Check that your `.env` file is properly formatted and loaded

## Related Documentation

- [API Documentation](./api.html): Details on the GeminiClient class
- [Getting Started](./getting-started.html): Initial setup including API keys
- [Troubleshooting](./troubleshooting.html): General troubleshooting guidance
