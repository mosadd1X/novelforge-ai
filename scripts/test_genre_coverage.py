#!/usr/bin/env python3
"""
Test Script: Check Genre Coverage for Back Cover Methods

This script checks all 38 genres to verify:
1. Which genre files exist
2. Which have back cover methods implemented
3. Which are missing or need updates
4. Investigates the "40 vs 38" genre discrepancy
"""

import sys
import os
from pathlib import Path
from typing import Dict, List, Set

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.utils.genre_defaults import get_all_genres
from rich.console import Console
from rich.table import Table

console = Console()


class GenreCoverageChecker:
    """
    Checks genre coverage for back cover methods.
    """
    
    def __init__(self):
        """Initialize the checker."""
        self.prompts_dir = project_root / "src" / "prompts"
        self.results = {
            "total_genres": 0,
            "existing_files": 0,
            "with_back_cover_methods": 0,
            "missing_files": [],
            "missing_methods": [],
            "successful_updates": [],
            "genre_file_mapping": {}
        }
    
    def check_all_genres(self) -> Dict:
        """
        Check all genres for back cover method coverage.
        
        Returns:
            Dictionary with detailed results
        """
        try:
            console.print("[bold cyan]🔍 Checking Genre Coverage for Back Cover Methods[/bold cyan]")
            console.print(f"📁 Prompts directory: {self.prompts_dir}")
            
            # Get all genres
            all_genres = get_all_genres()
            self.results["total_genres"] = len(all_genres)
            
            console.print(f"📚 Total genres to check: {len(all_genres)}")
            
            # Check each genre
            for genre in all_genres:
                if genre.lower() == "test":
                    continue
                    
                self._check_genre(genre)
            
            # Generate summary
            self._generate_summary()
            
            return self.results
            
        except Exception as e:
            console.print(f"❌ Error checking genre coverage: {e}")
            return self.results
    
    def _check_genre(self, genre: str) -> None:
        """
        Check a specific genre for back cover methods.
        
        Args:
            genre: Genre name to check
        """
        try:
            # Convert genre name to filename
            filename = self._genre_to_filename(genre)
            file_path = self.prompts_dir / f"{filename}.py"
            
            self.results["genre_file_mapping"][genre] = {
                "filename": filename,
                "file_path": str(file_path),
                "exists": file_path.exists(),
                "has_back_cover_methods": False,
                "methods_found": []
            }
            
            if file_path.exists():
                self.results["existing_files"] += 1
                
                # Check for back cover methods
                has_methods = self._check_back_cover_methods(file_path, genre)
                
                if has_methods:
                    self.results["with_back_cover_methods"] += 1
                    self.results["successful_updates"].append(genre)
                else:
                    self.results["missing_methods"].append(genre)
            else:
                self.results["missing_files"].append(genre)
                
        except Exception as e:
            console.print(f"❌ Error checking {genre}: {e}")
    
    def _genre_to_filename(self, genre: str) -> str:
        """Convert genre name to filename format."""
        import re
        # Convert to lowercase and replace spaces/special chars with underscores
        filename = re.sub(r'[^a-zA-Z0-9\s]', '', genre.lower())
        filename = re.sub(r'\s+', '_', filename)
        return filename
    
    def _check_back_cover_methods(self, file_path: Path, genre: str) -> bool:
        """
        Check if a genre file has back cover methods.
        
        Args:
            file_path: Path to the genre file
            genre: Genre name
            
        Returns:
            True if back cover methods are found
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for required methods
            required_methods = [
                'get_back_cover_prompt',
                'get_short_description_prompt', 
                'get_marketing_tagline_prompt',
                'get_visual_style_preferences'
            ]
            
            found_methods = []
            for method in required_methods:
                if method in content:
                    found_methods.append(method)
            
            self.results["genre_file_mapping"][genre]["methods_found"] = found_methods
            self.results["genre_file_mapping"][genre]["has_back_cover_methods"] = len(found_methods) >= 3
            
            return len(found_methods) >= 3  # At least 3 out of 4 methods
            
        except Exception as e:
            console.print(f"❌ Error reading {file_path}: {e}")
            return False
    
    def _generate_summary(self) -> None:
        """Generate and display summary results."""
        console.print("\n" + "=" * 60)
        console.print("[bold green]📊 GENRE COVERAGE SUMMARY[/bold green]")
        console.print("=" * 60)
        
        # Overall stats
        console.print(f"📚 Total Genres: {self.results['total_genres']}")
        console.print(f"📄 Existing Files: {self.results['existing_files']}")
        console.print(f"✅ With Back Cover Methods: {self.results['with_back_cover_methods']}")
        console.print(f"⚠️ Missing Methods: {len(self.results['missing_methods'])}")
        console.print(f"❌ Missing Files: {len(self.results['missing_files'])}")
        
        # Coverage percentage
        if self.results['total_genres'] > 0:
            coverage = (self.results['with_back_cover_methods'] / self.results['total_genres']) * 100
            console.print(f"📈 Coverage: {coverage:.1f}%")
        
        # Detailed tables
        self._show_successful_updates()
        self._show_missing_methods()
        self._show_missing_files()
        self._show_genre_file_mapping()
    
    def _show_successful_updates(self) -> None:
        """Show successfully updated genres."""
        if self.results['successful_updates']:
            console.print(f"\n[bold green]✅ Successfully Updated ({len(self.results['successful_updates'])} genres):[/bold green]")
            
            table = Table(show_header=True, header_style="bold green")
            table.add_column("Genre", style="green")
            table.add_column("Filename", style="dim")
            table.add_column("Methods Found", style="cyan")
            
            for genre in self.results['successful_updates']:
                mapping = self.results['genre_file_mapping'][genre]
                methods = ", ".join(mapping['methods_found'])
                table.add_row(genre, mapping['filename'], methods)
            
            console.print(table)
    
    def _show_missing_methods(self) -> None:
        """Show genres missing back cover methods."""
        if self.results['missing_methods']:
            console.print(f"\n[bold yellow]⚠️ Missing Back Cover Methods ({len(self.results['missing_methods'])} genres):[/bold yellow]")
            
            table = Table(show_header=True, header_style="bold yellow")
            table.add_column("Genre", style="yellow")
            table.add_column("Filename", style="dim")
            table.add_column("Methods Found", style="cyan")
            
            for genre in self.results['missing_methods']:
                mapping = self.results['genre_file_mapping'][genre]
                methods = ", ".join(mapping['methods_found']) if mapping['methods_found'] else "None"
                table.add_row(genre, mapping['filename'], methods)
            
            console.print(table)
    
    def _show_missing_files(self) -> None:
        """Show genres with missing files."""
        if self.results['missing_files']:
            console.print(f"\n[bold red]❌ Missing Genre Files ({len(self.results['missing_files'])} genres):[/bold red]")
            
            table = Table(show_header=True, header_style="bold red")
            table.add_column("Genre", style="red")
            table.add_column("Expected Filename", style="dim")
            table.add_column("Status", style="red")
            
            for genre in self.results['missing_files']:
                mapping = self.results['genre_file_mapping'][genre]
                table.add_row(genre, mapping['filename'] + ".py", "File Not Found")
            
            console.print(table)
    
    def _show_genre_file_mapping(self) -> None:
        """Show complete genre to file mapping."""
        console.print(f"\n[bold blue]📋 Complete Genre File Mapping:[/bold blue]")
        
        table = Table(show_header=True, header_style="bold blue")
        table.add_column("Genre", style="blue")
        table.add_column("Filename", style="dim")
        table.add_column("Exists", style="green")
        table.add_column("Has Methods", style="cyan")
        table.add_column("Method Count", style="magenta")
        
        for genre, mapping in self.results['genre_file_mapping'].items():
            exists = "✅" if mapping['exists'] else "❌"
            has_methods = "✅" if mapping['has_back_cover_methods'] else "❌"
            method_count = str(len(mapping['methods_found']))
            
            table.add_row(genre, mapping['filename'], exists, has_methods, method_count)
        
        console.print(table)


def investigate_genre_count_discrepancy():
    """Investigate why the script reported 40 genres instead of 38."""
    console.print("\n[bold magenta]🔍 Investigating Genre Count Discrepancy[/bold magenta]")
    
    try:
        all_genres = get_all_genres()
        console.print(f"📊 get_all_genres() returns: {len(all_genres)} genres")
        
        # Show all genres
        console.print("\n📋 All genres from get_all_genres():")
        for i, genre in enumerate(all_genres, 1):
            console.print(f"  {i:2d}. {genre}")
        
        # Check for duplicates
        unique_genres = set(all_genres)
        if len(unique_genres) != len(all_genres):
            console.print(f"\n⚠️ Found duplicates! Unique: {len(unique_genres)}, Total: {len(all_genres)}")
            duplicates = []
            seen = set()
            for genre in all_genres:
                if genre in seen:
                    duplicates.append(genre)
                seen.add(genre)
            console.print(f"🔄 Duplicates: {duplicates}")
        else:
            console.print(f"\n✅ No duplicates found. All {len(all_genres)} genres are unique.")
        
        # Check for test genres or special entries
        special_genres = [g for g in all_genres if g.lower() in ['test', 'example', 'template']]
        if special_genres:
            console.print(f"\n🧪 Special/Test genres found: {special_genres}")
        
    except Exception as e:
        console.print(f"❌ Error investigating genre count: {e}")


def main():
    """Main function to check genre coverage."""
    console.print("[bold blue]🧪 Genre Coverage Test Suite[/bold blue]")
    console.print("=" * 50)
    
    # Check genre coverage
    checker = GenreCoverageChecker()
    results = checker.check_all_genres()
    
    # Investigate genre count discrepancy
    investigate_genre_count_discrepancy()
    
    # Final recommendations
    console.print("\n" + "=" * 60)
    console.print("[bold cyan]📋 RECOMMENDATIONS[/bold cyan]")
    console.print("=" * 60)
    
    if results['missing_files']:
        console.print(f"🔧 Create {len(results['missing_files'])} missing genre files")
    
    if results['missing_methods']:
        console.print(f"🔧 Add back cover methods to {len(results['missing_methods'])} existing files")
    
    if results['with_back_cover_methods'] == results['total_genres']:
        console.print("🎉 All genres have back cover methods implemented!")
    else:
        missing_total = len(results['missing_files']) + len(results['missing_methods'])
        console.print(f"⚠️ {missing_total} genres still need back cover methods")
    
    console.print(f"\n✅ Coverage: {results['with_back_cover_methods']}/{results['total_genres']} genres")
    
    return results


if __name__ == "__main__":
    results = main()
    
    # Exit with appropriate code
    if results['with_back_cover_methods'] == results['total_genres']:
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Some work still needed
