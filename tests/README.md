# Test Suite

This directory contains comprehensive tests for NovelForge AI's critical fixes and improvements.

## Test Files

### Core Functionality Tests

- **`test_memory_leak_fix.py`** - Tests the memory leak fix implementation

  - LimitedDict and LimitedList functionality
  - MemoryManager bounded growth
  - Save/load with limited containers
  - Memory optimization features

- **`test_error_handling.py`** - Tests the standardized error handling system

  - Exception hierarchy functionality
  - Error handler with Rich formatting
  - Error context manager
  - Integration with existing code patterns

- **`test_network_resilience.py`** - Tests the network resilience system
  - Basic connectivity checking
  - Resilient Gemini client functionality
  - Network status UI
  - Request queuing and circuit breaker

### Quick Tests

- **`simple_memory_test.py`** - Quick verification of memory leak fixes
  - Basic LimitedDict functionality
  - MemoryManager integration test

## Running Tests

### Individual Tests

```bash
# Test memory leak fix
python tests/test_memory_leak_fix.py

# Test error handling
python tests/test_error_handling.py

# Test network resilience
python tests/test_network_resilience.py

# Quick memory test
python tests/simple_memory_test.py
```

### All Tests

```bash
# Run all tests (from project root)
python -m pytest tests/ -v
```

## Test Requirements

Make sure you have the required dependencies:

```bash
pip install psutil rich requests
```

## Test Coverage

These tests verify the implementation of:

1. **Priority 1: Memory Leak Fix**

   - Unlimited memory growth prevention
   - LRU eviction in limited containers
   - Memory monitoring and optimization

2. **Priority 2: Standardized Error Handling**

   - User-friendly error messages
   - Recovery suggestions
   - Beautiful Rich formatting

3. **Priority 3: Unused Import Cleanup**

   - Verified through successful imports
   - No import errors after cleanup

4. **Priority 4: ResilientGeminiClient Migration**
   - All modules use resilient client
   - Network resilience features active
   - Backward compatibility maintained

## Expected Results

All tests should pass, indicating:

- ✅ Memory usage stays bounded during long operations
- ✅ Error handling provides user-friendly messages
- ✅ Network resilience handles unstable connections
- ✅ System integration works correctly
