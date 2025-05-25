# Critical Fixes Implementation Guide

## 🚨 Priority 1: Memory Leak Fix (CRITICAL)

### Problem

The `MemoryManager` class in `src/core/memory_manager.py` has unlimited growth in narrative tracking dictionaries, causing memory leaks during long series generation.

### Location

```python
# Lines 84-123 in src/core/memory_manager.py
self.narrative_tracking = {
    "character_arcs": {},           # Grows indefinitely
    "character_emotions": {},       # Per-chapter data accumulates
    "character_knowledge": {},      # Exponential growth possible
    # ... 20+ more dictionaries
}
```

### Solution

Implement size limits and cleanup routines:

```python
class MemoryManager:
    def __init__(self, novel_title: str, max_memory_items: int = 1000):
        self.max_memory_items = max_memory_items
        self.narrative_tracking = {
            "character_arcs": LimitedDict(max_memory_items),
            "character_emotions": LimitedDict(max_memory_items),
            "character_knowledge": LimitedDict(max_memory_items),
            # ... use LimitedDict for all tracking
        }

class LimitedDict(dict):
    """Dictionary with size limits and LRU eviction"""
    def __init__(self, max_size: int = 1000):
        super().__init__()
        self.max_size = max_size
        self.access_order = []

    def __setitem__(self, key, value):
        if key in self:
            self.access_order.remove(key)
        elif len(self) >= self.max_size:
            # Remove least recently used item
            oldest_key = self.access_order.pop(0)
            del self[oldest_key]

        super().__setitem__(key, value)
        self.access_order.append(key)
```

### Implementation Steps

1. Create `src/utils/limited_dict.py` with the LimitedDict class
2. Modify `MemoryManager.__init__()` to use LimitedDict
3. Add memory usage monitoring
4. Test with long series generation

## 🚨 Priority 2: Standardize Error Handling (HIGH)

### Problem

Inconsistent error handling patterns throughout the codebase lead to poor user experience and difficult debugging.

### Current Issues

```python
# Mixed patterns found:
print(f"Error generating content: {error_str}")  # Plain print
console.print(f"[bold red]Error: {e}[/bold red]")  # Rich formatting
log_error("Failed to generate", exception=e)  # Logging only
return f"Error: {str(e)}"  # Return error string
```

### Solution

Create a unified exception hierarchy and error handling system:

```python
# src/core/exceptions.py
class NovelForgeError(Exception):
    """Base exception for NovelForge AI with user-friendly messages"""

    def __init__(self, message: str, user_message: str = None,
                 details: dict = None, recovery_suggestions: list = None):
        super().__init__(message)
        self.user_message = user_message or message
        self.details = details or {}
        self.recovery_suggestions = recovery_suggestions or []

class NetworkError(NovelForgeError):
    """Network-related errors"""
    pass

class GenerationError(NovelForgeError):
    """Content generation errors"""
    pass

class ValidationError(NovelForgeError):
    """Input validation errors"""
    pass

# src/utils/error_handler.py
class ErrorHandler:
    """Centralized error handling and user feedback"""

    @staticmethod
    def handle_error(error: Exception, context: str = None) -> None:
        """Handle any error with appropriate user feedback"""
        if isinstance(error, NovelForgeError):
            ErrorHandler._handle_known_error(error, context)
        else:
            ErrorHandler._handle_unknown_error(error, context)

    @staticmethod
    def _handle_known_error(error: NovelForgeError, context: str) -> None:
        """Handle known application errors"""
        console.print(f"[bold red]❌ {error.user_message}[/bold red]")

        if error.recovery_suggestions:
            console.print("\n[bold cyan]💡 Suggestions:[/bold cyan]")
            for suggestion in error.recovery_suggestions:
                console.print(f"• {suggestion}")

        # Log technical details
        logger.error(f"Error in {context}",
                    error=str(error),
                    details=error.details)
```

### Implementation Steps

1. Create `src/core/exceptions.py` with exception hierarchy
2. Create `src/utils/error_handler.py` with centralized handling
3. Replace error handling patterns throughout codebase
4. Add recovery suggestions for common errors

## 🚨 Priority 3: Remove Unused Imports (QUICK WIN)

### Problem

Multiple files have unused imports that increase memory usage and reduce code clarity.

### Critical Files to Fix

#### `src/main.py`

```python
# Remove these unused imports:
from typing import Dict, List, Any, Optional  # Remove List, Optional
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn  # Remove most
from rich.live import Live  # Remove
from src.utils.file_handler import create_output_directory, save_novel_json, create_series_directory  # Remove create_series_directory
```

#### `run.py`

```python
# Remove:
import os  # Not used
```

### Automated Solution

Create a script to find and remove unused imports:

```python
# scripts/cleanup_imports.py
import ast
import os
from typing import Set, List

class ImportAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.imports = {}
        self.used_names = set()

    def visit_Import(self, node):
        for alias in node.names:
            name = alias.asname or alias.name
            self.imports[name] = node

    def visit_ImportFrom(self, node):
        for alias in node.names:
            name = alias.asname or alias.name
            self.imports[name] = node

    def visit_Name(self, node):
        self.used_names.add(node.id)

    def get_unused_imports(self) -> List[str]:
        return [name for name in self.imports if name not in self.used_names]

def cleanup_file(filepath: str) -> None:
    """Remove unused imports from a Python file"""
    with open(filepath, 'r') as f:
        content = f.read()

    tree = ast.parse(content)
    analyzer = ImportAnalyzer()
    analyzer.visit(tree)

    unused = analyzer.get_unused_imports()
    if unused:
        print(f"File: {filepath}")
        print(f"Unused imports: {unused}")
        # Remove unused imports (implementation needed)
```

## 🚨 Priority 4: Migrate to ResilientGeminiClient (MEDIUM)

### Problem

Many modules still use the old `GeminiClient` directly, missing network resilience benefits.

### Files to Update

1. `src/core/novel_generator.py`
2. `src/core/series_generator.py`
3. `src/ui/book_menu.py`
4. Any other files with `from src.core.gemini_client import GeminiClient`

### Migration Pattern

```python
# Replace this pattern:
from src.core.gemini_client import GeminiClient

class NovelGenerator:
    def __init__(self):
        self.gemini = GeminiClient()

# With this pattern:
from src.core.resilient_gemini_client import ResilientGeminiClient

class NovelGenerator:
    def __init__(self):
        self.gemini = ResilientGeminiClient()
        # All existing code works the same!
```

### Benefits

- Automatic network resilience
- Request queuing during outages
- Enhanced error messages
- Response caching
- Circuit breaker protection

## 🛠️ Implementation Timeline

### Day 1 (4 hours)

- [ ] **Morning**: Fix memory leak in MemoryManager (2 hours)
- [ ] **Afternoon**: Remove unused imports (1 hour)
- [ ] **Afternoon**: Create exception hierarchy (1 hour)

### Day 2 (4 hours)

- [ ] **Morning**: Implement ErrorHandler class (2 hours)
- [ ] **Afternoon**: Migrate to ResilientGeminiClient (2 hours)

### Day 3 (2 hours)

- [ ] **Testing**: Comprehensive testing of all fixes
- [ ] **Validation**: Memory usage and performance testing

## 🧪 Testing Strategy

### Memory Leak Testing

```python
# Test script for memory usage
import psutil
import os

def test_memory_usage():
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss

    # Generate a long series
    # ... generation code ...

    final_memory = process.memory_info().rss
    memory_growth = final_memory - initial_memory

    assert memory_growth < 100 * 1024 * 1024  # Less than 100MB growth
```

### Error Handling Testing

```python
def test_error_handling():
    # Test network errors
    # Test validation errors
    # Test generation errors
    # Verify user-friendly messages
    # Verify recovery suggestions
```

## 📊 Success Metrics

### Before Fixes

- Memory usage grows indefinitely during series generation
- Inconsistent error messages confuse users
- Network failures not handled gracefully
- Unused imports waste memory

### After Fixes

- Memory usage stays constant during long operations
- All errors provide clear, helpful messages
- Network issues handled automatically
- Clean, efficient codebase

## 🚀 Quick Implementation Commands

```bash
# 1. Create new files
touch src/core/exceptions.py
touch src/utils/error_handler.py
touch src/utils/limited_dict.py
touch scripts/cleanup_imports.py

# 2. Run tests
python test_memory_usage.py
python test_error_handling.py

# 3. Validate improvements
python -m memory_profiler src/main.py
python scripts/check_unused_imports.py
```

These critical fixes will immediately improve the stability and user experience of NovelForge AI, building on the network resilience foundation we established.
