# Network Resilience System

## Overview

The Network Resilience System is a comprehensive solution designed to handle unstable WiFi connections and network issues in the Ebook Generator application. It provides robust error handling, automatic retry mechanisms, request queuing, and graceful degradation to ensure the application continues functioning even with intermittent connectivity.

## Key Features

### 🌐 Real-time Network Monitoring
- Continuous monitoring of network connectivity
- Multiple connectivity test methods (DNS, HTTP, interface checks)
- Automatic detection of connection state changes
- Historical connection tracking

### 🔄 Intelligent Retry Logic
- Exponential backoff with jitter to prevent thundering herd
- Circuit breaker pattern for system protection
- Configurable retry limits and timeouts
- Enhanced error messaging with troubleshooting tips

### 📋 Request Queuing System
- Automatic queuing of failed requests
- Priority-based request handling
- Automatic retry when connection is restored
- Request lifecycle tracking and callbacks

### 🛡️ Circuit Breaker Protection
- Prevents system overload during network issues
- Three states: CLOSED (normal), OPEN (failing fast), HALF-OPEN (testing recovery)
- Configurable failure thresholds and recovery timeouts
- Automatic recovery detection

### 📊 User Feedback & Monitoring
- Real-time status displays with color coding
- Detailed network diagnostics and troubleshooting
- Live monitoring capabilities
- Connection history and performance metrics

### 💾 Graceful Degradation
- Offline mode with cached responses
- Helpful error messages with guidance
- Seamless transition between online/offline states
- Response caching for improved resilience

## Architecture

### Core Components

1. **NetworkResilienceManager** (`src/utils/network_resilience.py`)
   - Central coordinator for all network resilience features
   - Manages connectivity monitoring, request queuing, and circuit breaker
   - Provides metrics and status reporting

2. **ResilientGeminiClient** (`src/core/resilient_gemini_client.py`)
   - Enhanced wrapper around the original GeminiClient
   - Integrates network resilience features with API calls
   - Provides caching and offline mode capabilities

3. **NetworkStatusUI** (`src/ui/network_status_ui.py`)
   - User interface for network monitoring and diagnostics
   - Interactive menus and real-time status displays
   - Network troubleshooting and configuration tools

4. **Enhanced GeminiClient** (`src/core/gemini_client.py`)
   - Improved error handling and user feedback
   - Better retry logic with progress indicators
   - Enhanced troubleshooting guidance

## Installation

### Dependencies

Add the following dependencies to your environment:

```bash
pip install requests==2.31.0 psutil==5.9.8
```

These are automatically included in the updated `requirements.txt`.

### Setup

The network resilience system is automatically initialized when you:
1. Import any component that uses network functionality
2. Run the main application (`python run.py`)
3. Access the "Network Status & Diagnostics" menu

## Usage

### Basic Usage

The network resilience system works automatically in the background. When you generate content:

```python
# The system automatically handles network issues
from src.core.resilient_gemini_client import ResilientGeminiClient

client = ResilientGeminiClient()
result = client.generate_content("Your prompt here")
```

### Network Status Monitoring

Access network monitoring through the main menu:

1. Run `python run.py`
2. Select "7. Network Status & Diagnostics"
3. Choose from various monitoring options:
   - Quick status overview
   - Detailed status with metrics
   - Connection history
   - Live monitoring
   - Network diagnostics

### Manual Network Management

```python
from src.utils.network_resilience import get_network_manager

# Get the global network manager
network_manager = get_network_manager()

# Force a connectivity check
is_connected = network_manager.force_connectivity_check()

# Get detailed status
status = network_manager.get_status()

# Show status panel
network_manager.show_status_panel()
```

## Configuration

### Network Resilience Configuration

```python
config = {
    'status_check_interval': 30,  # seconds between connectivity checks
    'show_status_messages': True,  # show network status changes
    'show_retry_messages': True,   # show retry attempts
    'circuit_breaker': {
        'failure_threshold': 5,    # failures before opening circuit
        'recovery_timeout': 60,    # seconds before testing recovery
        'success_threshold': 3     # successes needed to close circuit
    }
}

from src.utils.network_resilience import NetworkResilienceManager
manager = NetworkResilienceManager(config)
```

### Resilient Client Configuration

```python
from src.core.resilient_gemini_client import ResilientGeminiClient
from src.utils.network_resilience import RequestPriority

client = ResilientGeminiClient()

# Generate content with custom settings
result = client.generate_content(
    prompt="Your prompt",
    priority=RequestPriority.HIGH,
    max_retries=10,
    timeout=180.0,
    use_cache=True
)
```

## Network Status Indicators

### Connection Status
- 🟢 **CONNECTED**: Stable network connection
- 🔴 **DISCONNECTED**: No network connectivity
- 🟡 **UNSTABLE**: Intermittent connectivity issues
- 🔵 **CHECKING**: Currently testing connectivity

### Circuit Breaker Status
- ✅ **CLOSED**: Normal operation, requests proceeding
- 🚫 **OPEN**: Failing fast to protect system
- 🔄 **HALF-OPEN**: Testing if service has recovered

## Troubleshooting

### Common Issues

#### "Network Status system not available"
- Install required dependencies: `pip install requests psutil`
- Check that all network resilience files are present
- Verify Python environment is properly configured

#### High failure rates
- Check internet connection stability
- Verify API keys are correct and not rate-limited
- Consider adjusting retry settings for slower connections

#### Circuit breaker frequently opening
- Network may be very unstable
- Adjust failure threshold in configuration
- Check for background network usage

### Network Diagnostics

Use the built-in diagnostics tool:
1. Access "Network Status & Diagnostics" from main menu
2. Select "Run Network Diagnostics"
3. Review results and follow recommendations

### Manual Testing

Run the test suite to verify functionality:

```bash
python test_network_resilience.py
```

## Performance Impact

The network resilience system is designed to be lightweight:

- **Background monitoring**: ~1% CPU usage
- **Memory overhead**: ~10-20MB for queuing and metrics
- **Network overhead**: Minimal connectivity checks every 30 seconds
- **Response time**: No impact on successful requests

## Best Practices

### For Unstable Connections
1. Enable response caching for frequently used prompts
2. Use higher priority for critical requests
3. Increase timeout values for slow connections
4. Monitor network status regularly

### For Development
1. Use the test script to verify functionality
2. Monitor network metrics during development
3. Test with simulated network issues
4. Configure appropriate retry limits

### For Production
1. Set conservative circuit breaker thresholds
2. Enable comprehensive logging
3. Monitor network health metrics
4. Have fallback procedures for extended outages

## Integration with Existing Code

The network resilience system integrates seamlessly with existing code:

### Automatic Integration
- All existing Gemini API calls automatically benefit from enhanced retry logic
- Network status is checked before major operations
- Error messages include troubleshooting guidance

### Manual Integration
Replace direct GeminiClient usage with ResilientGeminiClient for maximum benefits:

```python
# Before
from src.core.gemini_client import GeminiClient
client = GeminiClient()

# After
from src.core.resilient_gemini_client import ResilientGeminiClient
client = ResilientGeminiClient()
```

## Monitoring and Metrics

### Available Metrics
- Total requests processed
- Success/failure rates
- Average response times
- Consecutive failure/success counts
- Circuit breaker state changes
- Connection history

### Accessing Metrics
```python
from src.utils.network_resilience import get_network_manager

manager = get_network_manager()
status = manager.get_status()

print(f"Success rate: {status['metrics']['success_rate']:.1f}%")
print(f"Average response time: {status['metrics']['average_response_time']:.2f}s")
```

## Future Enhancements

Planned improvements include:
- Adaptive retry strategies based on error types
- Machine learning for connection prediction
- Integration with system network events
- Advanced caching strategies
- Performance optimization for mobile networks

## Support

For issues or questions about the network resilience system:
1. Check the troubleshooting section above
2. Run the diagnostic tools
3. Review the test script output
4. Check system logs for detailed error information
