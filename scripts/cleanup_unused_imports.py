#!/usr/bin/env python3
"""
Script to detect and remove unused imports from Python files.

This script analyzes Python files to find imports that are not used
and provides options to automatically remove them.
"""

import ast
import os
import sys
import argparse
from typing import Dict, List, Set, Tuple
from pathlib import Path


class ImportAnalyzer(ast.NodeVisitor):
    """AST visitor to analyze imports and their usage."""
    
    def __init__(self):
        self.imports = {}  # name -> (node, line_number)
        self.from_imports = {}  # name -> (module, node, line_number)
        self.used_names = set()
        self.import_lines = set()  # Track which lines have imports
    
    def visit_Import(self, node):
        """Visit import statements."""
        for alias in node.names:
            name = alias.asname or alias.name.split('.')[0]  # Handle dotted imports
            self.imports[name] = (node, node.lineno)
            self.import_lines.add(node.lineno)
    
    def visit_ImportFrom(self, node):
        """Visit from...import statements."""
        for alias in node.names:
            name = alias.asname or alias.name
            self.from_imports[name] = (node.module, node, node.lineno)
            self.import_lines.add(node.lineno)
    
    def visit_Name(self, node):
        """Visit name references."""
        self.used_names.add(node.id)
        self.generic_visit(node)
    
    def visit_Attribute(self, node):
        """Visit attribute access (e.g., module.function)."""
        if isinstance(node.value, ast.Name):
            self.used_names.add(node.value.id)
        self.generic_visit(node)
    
    def get_unused_imports(self) -> Dict[str, Tuple]:
        """Get unused imports with their details."""
        unused = {}
        
        # Check regular imports
        for name, (node, line_no) in self.imports.items():
            if name not in self.used_names:
                unused[name] = ('import', node, line_no)
        
        # Check from imports
        for name, (module, node, line_no) in self.from_imports.items():
            if name not in self.used_names:
                unused[name] = ('from_import', node, line_no, module)
        
        return unused


def analyze_file(file_path: str) -> Tuple[Dict, Set, List[str]]:
    """
    Analyze a Python file for unused imports.
    
    Args:
        file_path: Path to the Python file
        
    Returns:
        Tuple of (unused_imports, import_lines, file_lines)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.splitlines()
        
        # Parse the AST
        tree = ast.parse(content)
        analyzer = ImportAnalyzer()
        analyzer.visit(tree)
        
        unused = analyzer.get_unused_imports()
        return unused, analyzer.import_lines, lines
        
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
        return {}, set(), []


def remove_unused_imports(file_path: str, unused_imports: Dict, dry_run: bool = True) -> bool:
    """
    Remove unused imports from a file.
    
    Args:
        file_path: Path to the Python file
        unused_imports: Dictionary of unused imports
        dry_run: If True, only show what would be removed
        
    Returns:
        True if changes were made (or would be made)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Group unused imports by line number
        lines_to_remove = set()
        lines_to_modify = {}  # line_no -> new_content
        
        for name, details in unused_imports.items():
            if details[0] == 'import':
                # Simple import - remove entire line
                line_no = details[2]
                lines_to_remove.add(line_no)
            elif details[0] == 'from_import':
                # From import - might need to modify line if multiple imports
                node = details[1]
                line_no = details[2]
                
                # Check if this is the only import on the line
                if len(node.names) == 1:
                    lines_to_remove.add(line_no)
                else:
                    # Multiple imports - remove just this one
                    original_line = lines[line_no - 1]  # line numbers are 1-based
                    # This is a simplified approach - in practice, you'd want more robust parsing
                    if f", {name}" in original_line:
                        new_line = original_line.replace(f", {name}", "")
                    elif f"{name}, " in original_line:
                        new_line = original_line.replace(f"{name}, ", "")
                    else:
                        new_line = original_line.replace(name, "")
                    
                    lines_to_modify[line_no] = new_line
        
        if not lines_to_remove and not lines_to_modify:
            return False
        
        if dry_run:
            print(f"\nWould remove from {file_path}:")
            for line_no in sorted(lines_to_remove):
                print(f"  Line {line_no}: {lines[line_no - 1].strip()}")
            for line_no, new_content in lines_to_modify.items():
                print(f"  Line {line_no}: {lines[line_no - 1].strip()} -> {new_content.strip()}")
            return True
        
        # Apply changes
        new_lines = []
        for i, line in enumerate(lines, 1):
            if i in lines_to_remove:
                continue  # Skip this line
            elif i in lines_to_modify:
                new_lines.append(lines_to_modify[i])
            else:
                new_lines.append(line)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print(f"✓ Cleaned up imports in {file_path}")
        return True
        
    except Exception as e:
        print(f"Error removing imports from {file_path}: {e}")
        return False


def find_python_files(directory: str) -> List[str]:
    """Find all Python files in a directory."""
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Skip virtual environment and cache directories
        dirs[:] = [d for d in dirs if d not in ['.venv', '__pycache__', '.git', 'node_modules']]
        
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    return python_files


def main():
    """Main function to run the import cleanup."""
    parser = argparse.ArgumentParser(description='Clean up unused imports in Python files')
    parser.add_argument('path', nargs='?', default='.', help='Path to file or directory to analyze')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be removed without making changes')
    parser.add_argument('--fix', action='store_true', help='Actually remove the unused imports')
    
    args = parser.parse_args()
    
    if os.path.isfile(args.path):
        files_to_analyze = [args.path]
    elif os.path.isdir(args.path):
        files_to_analyze = find_python_files(args.path)
    else:
        print(f"Error: {args.path} is not a valid file or directory")
        return 1
    
    print(f"Analyzing {len(files_to_analyze)} Python files...")
    
    total_unused = 0
    files_with_unused = 0
    
    for file_path in files_to_analyze:
        unused_imports, import_lines, file_lines = analyze_file(file_path)
        
        if unused_imports:
            files_with_unused += 1
            total_unused += len(unused_imports)
            
            print(f"\n📁 {file_path}")
            print(f"   Found {len(unused_imports)} unused imports:")
            
            for name, details in unused_imports.items():
                if details[0] == 'import':
                    print(f"     • import {name} (line {details[2]})")
                else:
                    module = details[3] if len(details) > 3 else "unknown"
                    print(f"     • from {module} import {name} (line {details[2]})")
            
            # Remove unused imports if requested
            if args.fix:
                remove_unused_imports(file_path, unused_imports, dry_run=False)
            elif not args.dry_run:
                remove_unused_imports(file_path, unused_imports, dry_run=True)
    
    print(f"\n📊 Summary:")
    print(f"   Files analyzed: {len(files_to_analyze)}")
    print(f"   Files with unused imports: {files_with_unused}")
    print(f"   Total unused imports: {total_unused}")
    
    if total_unused > 0 and not args.fix:
        print(f"\n💡 To remove unused imports, run with --fix flag")
    elif args.fix and total_unused > 0:
        print(f"\n✅ Removed {total_unused} unused imports from {files_with_unused} files")
    elif total_unused == 0:
        print(f"\n✅ No unused imports found!")
    
    return 0


if __name__ == "__main__":
    exit(main())
