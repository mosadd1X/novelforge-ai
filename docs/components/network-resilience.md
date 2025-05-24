---
layout: default
title: Network Resilience System
parent: Core Components
nav_order: 7
description: "Documentation of the Network Resilience System for robust API handling and error recovery"
---

# Network Resilience System
{: .no_toc }

The Network Resilience System provides robust error handling, automatic recovery, and intelligent retry mechanisms to ensure reliable book generation even under challenging network conditions.
{: .fs-6 .fw-300 }

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Overview

The Network Resilience System is a critical component that ensures the Ebook Generator can handle network issues, API failures, and rate limiting gracefully. It provides multiple layers of protection and recovery mechanisms to maintain generation reliability.

### Key Features

- **Automatic Retry Logic**: Intelligent retry mechanisms with exponential backoff
- **Multiple API Key Support**: Automatic failover between multiple API keys
- **Rate Limit Handling**: Smart detection and handling of API rate limits
- **Network Error Recovery**: Robust handling of network connectivity issues
- **Progress Preservation**: Maintains generation progress during failures
- **Graceful Degradation**: Continues operation with reduced functionality when needed

## Architecture

### Resilient Gemini Client

The core of the system is the `ResilientGeminiClient` which wraps the standard Gemini API client:

```python
from src.core.resilient_gemini_client import ResilientGeminiClient

# Initialize with multiple API keys
client = ResilientGeminiClient(
    api_keys=["key1", "key2", "key3"],
    max_retries=3,
    base_delay=1.0,
    max_delay=60.0
)

# Generate content with automatic resilience
response = client.generate_content(prompt, temperature=0.7)
```

### Error Handling Layers

The system provides multiple layers of error handling:

1. **Network Layer**: Handles connection timeouts and network errors
2. **API Layer**: Manages API-specific errors and rate limits
3. **Application Layer**: Preserves generation state and progress
4. **User Layer**: Provides clear feedback and recovery options

## Features in Detail

### Automatic Retry Logic

The system implements intelligent retry mechanisms:

```python
# Exponential backoff with jitter
retry_delays = [1, 2, 4, 8, 16, 32, 60]  # seconds

# Automatic retry for transient errors
for attempt in range(max_retries):
    try:
        response = api_call()
        break
    except TransientError:
        wait_time = min(base_delay * (2 ** attempt), max_delay)
        time.sleep(wait_time + random.uniform(0, 1))
```

### Rate Limit Management

Sophisticated rate limit handling:

- **Detection**: Automatically detects rate limit responses
- **Key Rotation**: Switches to alternative API keys when rate limited
- **Backoff**: Implements appropriate waiting periods
- **Recovery**: Automatically resumes when limits reset

### API Key Failover

Seamless switching between multiple API keys:

```python
# Automatic key rotation on failure
if current_key_rate_limited:
    switch_to_next_available_key()
    retry_request_with_new_key()

# Key status tracking
key_status = {
    "key1": {"available": True, "rate_limited_until": None},
    "key2": {"available": False, "rate_limited_until": "2024-01-01T12:00:00Z"},
    "key3": {"available": True, "rate_limited_until": None}
}
```

### Progress Preservation

The system preserves generation progress during failures:

- **Chapter Checkpoints**: Saves progress after each completed chapter
- **State Recovery**: Resumes from last successful checkpoint
- **Partial Content**: Preserves partially generated content
- **Memory Consistency**: Maintains character and plot consistency across recoveries

## Configuration

### Resilience Settings

Configure resilience behavior in your settings:

```python
RESILIENCE_SETTINGS = {
    "max_retries": 3,
    "base_delay": 1.0,
    "max_delay": 60.0,
    "exponential_backoff": True,
    "jitter": True,
    "rate_limit_backoff": 300,  # 5 minutes
    "network_timeout": 30,
    "preserve_progress": True
}
```

### API Key Management

Configure multiple API keys for failover:

```python
# In .env file
GEMINI_API_KEY=primary_key_here
GEMINI_API_KEY_1=backup_key_1_here
GEMINI_API_KEY_2=backup_key_2_here
GEMINI_API_KEY_3=backup_key_3_here

# Automatic detection and rotation
ENABLE_KEY_ROTATION=true
MAX_KEYS_TO_USE=5
```

### Error Handling Policies

Configure how different errors are handled:

```python
ERROR_POLICIES = {
    "network_errors": "retry_with_backoff",
    "rate_limits": "switch_key_and_retry",
    "authentication_errors": "fail_immediately",
    "quota_exceeded": "switch_key_or_fail",
    "server_errors": "retry_with_exponential_backoff"
}
```

## Usage Examples

### Basic Resilient Generation

```python
from src.core.novel_generator import NovelGenerator

# The generator automatically uses resilient client
generator = NovelGenerator()
generator.initialize_novel(
    title="The Quantum Garden",
    author="Dr. Elise Moreau",
    description="A physicist discovers...",
    genre="Science Fiction"
)

# Generation will automatically handle network issues
generator.generate_novel()
```

### Custom Resilience Configuration

```python
# Configure custom resilience settings
resilience_config = {
    "max_retries": 5,
    "base_delay": 2.0,
    "max_delay": 120.0,
    "rate_limit_backoff": 600  # 10 minutes
}

generator = NovelGenerator(resilience_config=resilience_config)
```

### Manual Error Handling

```python
from src.core.resilient_gemini_client import ResilientGeminiClient
from src.core.exceptions import RateLimitError, NetworkError

client = ResilientGeminiClient()

try:
    response = client.generate_content(prompt)
except RateLimitError as e:
    print(f"Rate limited. Retry after: {e.retry_after}")
except NetworkError as e:
    print(f"Network error: {e.message}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Monitoring and Diagnostics

### Real-Time Status

The system provides real-time status information:

```python
# Check API key status
status = client.get_key_status()
print(f"Available keys: {status['available_keys']}")
print(f"Rate limited keys: {status['rate_limited_keys']}")

# Monitor retry attempts
print(f"Current retry attempt: {client.current_retry}")
print(f"Next retry in: {client.next_retry_delay} seconds")
```

### Logging and Metrics

Comprehensive logging for troubleshooting:

```python
# Enable detailed logging
import logging
logging.getLogger('resilient_client').setLevel(logging.DEBUG)

# Metrics collection
metrics = client.get_metrics()
print(f"Total requests: {metrics['total_requests']}")
print(f"Failed requests: {metrics['failed_requests']}")
print(f"Retry attempts: {metrics['retry_attempts']}")
print(f"Key switches: {metrics['key_switches']}")
```

## Best Practices

### API Key Management

- **Multiple Keys**: Use 3-5 API keys for optimal resilience
- **Key Rotation**: Regularly rotate API keys for security
- **Monitoring**: Monitor key usage and rate limit status
- **Backup Strategy**: Always have backup keys available

### Error Handling

- **Graceful Degradation**: Design for partial functionality during issues
- **User Communication**: Provide clear feedback about issues and recovery
- **Progress Preservation**: Always save progress at logical checkpoints
- **Timeout Management**: Set appropriate timeouts for different operations

### Performance Optimization

- **Efficient Retries**: Use exponential backoff to avoid overwhelming servers
- **Smart Key Selection**: Prefer keys with better performance history
- **Caching**: Cache successful responses when appropriate
- **Batch Operations**: Group related operations to reduce API calls

## Troubleshooting

### Common Issues

**Frequent Rate Limiting**
- Add more API keys to the rotation
- Increase rate limit backoff time
- Reduce generation speed/frequency

**Network Timeouts**
- Increase network timeout settings
- Check internet connection stability
- Consider using a VPN if regional issues exist

**Authentication Failures**
- Verify API key validity
- Check API key permissions
- Ensure keys are properly configured in .env

**Generation Interruptions**
- Enable progress preservation
- Use checkpoint-based recovery
- Monitor system resources

### Diagnostic Commands

```bash
# Check API key status
python -c "from src.utils.api_key_manager import check_all_keys; check_all_keys()"

# Test network resilience
python -c "from src.core.resilient_gemini_client import test_resilience; test_resilience()"

# Monitor real-time status
python -c "from src.core.resilient_gemini_client import monitor_status; monitor_status()"
```

## Related Documentation

- [API Key Management](../api-key-management.html): Managing multiple API keys
- [Configuration Options](../configuration.html): Configuring resilience settings
- [Troubleshooting](../troubleshooting.html): General troubleshooting guide
- [Novel Generator](./novel-generator.html): How resilience integrates with generation

---

The Network Resilience System ensures that your book generation process is robust, reliable, and capable of handling real-world network conditions and API limitations.
