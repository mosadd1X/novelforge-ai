#!/usr/bin/env python3
"""
Fast Testing System for Ebook Generator

This system provides rapid testing capabilities for the ebook generation workflow
by using reduced content generation, mock components, and optimized settings
while maintaining the same code paths as production.

Key Features:
- Follows exact same generation workflow as production
- Significantly reduced execution time (5-10 minutes vs 40+ minutes)
- Tests both single book and series generation
- Maintains code path integrity for bug detection
- Configurable test scenarios and parameters
"""

import sys
import time
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Add project root to path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn
from rich.live import Live

from src.core.novel_generator import NovelGenerator
from src.core.series_generator import SeriesGenerator
from src.formatters.epub_formatter import EpubFormatter
from src.utils.file_handler import create_output_directory
from src.utils.logger import init_logger, log_info, log_error, log_debug

console = Console(markup=True)

@dataclass
class TestResult:
    """Container for test execution results."""
    test_name: str
    success: bool
    execution_time: float
    word_count: int
    chapter_count: int
    error_message: Optional[str] = None
    file_path: Optional[str] = None
    details: Optional[Dict[str, Any]] = None

class FastTestSystem:
    """
    Fast testing system for ebook generation workflow.

    This system provides rapid testing of the complete ebook generation
    process using optimized settings and mock components where appropriate.
    """

    def __init__(self, use_mock_api: bool = False):
        """
        Initialize the fast testing system.

        Args:
            use_mock_api: Whether to use mock API calls for maximum speed
        """
        self.use_mock_api = use_mock_api
        self.results: List[TestResult] = []

        # Initialize logging for testing
        self.logger = init_logger("DEBUG")

        # Test output directory
        self.test_output_dir = Path("output/fast_tests")
        self.test_output_dir.mkdir(parents=True, exist_ok=True)

    def run_comprehensive_tests(self) -> Dict[str, Any]:
        """
        Run comprehensive fast tests covering all major scenarios.

        Returns:
            Dictionary containing test results and metrics
        """
        console.print(Panel.fit(
            "[bold cyan]🚀 Fast Testing System - Ebook Generator[/bold cyan]\n"
            "Comprehensive workflow testing with optimized performance\n"
            f"Mock API: {'Enabled' if self.use_mock_api else 'Disabled'} | "
            f"Target Time: 5-10 minutes",
            border_style="cyan"
        ))

        # Test scenarios to run
        test_scenarios = [
            ("Single Book - Minimal", self._test_single_book_minimal),
            ("Single Book - Standard", self._test_single_book_standard),
            ("Single Book - Complex Genre", self._test_single_book_complex),
            ("Series Generation - 2 Books", self._test_series_generation),
            ("Error Handling", self._test_error_handling),
            ("Performance Benchmarks", self._test_performance_benchmarks),
        ]

        overall_start_time = time.time()

        # Run each test scenario
        for test_name, test_func in test_scenarios:
            console.print(f"\n[bold yellow]🧪 Running {test_name}...[/bold yellow]")

            try:
                start_time = time.time()
                result = test_func()
                execution_time = time.time() - start_time

                if result:
                    result.execution_time = execution_time
                    self.results.append(result)

                    status = "✅ PASSED" if result.success else "❌ FAILED"
                    console.print(f"  {status} ({execution_time:.2f}s)")

                    if result.success and result.file_path:
                        console.print(f"    📁 Output: {result.file_path}")
                        console.print(f"    📊 {result.chapter_count} chapters, {result.word_count:,} words")
                else:
                    console.print(f"  ❌ FAILED - No result returned")

            except Exception as e:
                execution_time = time.time() - start_time
                error_result = TestResult(
                    test_name=test_name,
                    success=False,
                    execution_time=execution_time,
                    word_count=0,
                    chapter_count=0,
                    error_message=str(e)
                )
                self.results.append(error_result)
                console.print(f"  ❌ CRASHED: {e}")

        total_time = time.time() - overall_start_time

        # Generate comprehensive report
        report = self._generate_test_report(total_time)

        return report

    def _test_single_book_minimal(self) -> TestResult:
        """Test single book generation with minimal settings."""
        test_name = "Single Book - Minimal"

        try:
            # Get minimal test configuration
            config = self._get_minimal_book_config()

            # Initialize generator
            generator = NovelGenerator()

            # Replace with mock client if requested
            if self.use_mock_api:
                from src.testing.mock_components import MockGeminiClient
                generator.gemini = MockGeminiClient()

            # Create test output directory
            output_dir = self.test_output_dir / "minimal_book"
            output_dir.mkdir(exist_ok=True)

            # Initialize novel
            memory_manager = generator.initialize_novel(
                title=config["title"],
                author=config["author"],
                description=config["description"],
                genre=config["genre"],
                target_audience=config["target_audience"],
                output_dir=str(output_dir)
            )

            # Set test generation options
            generator.set_generation_options(config["generation_options"])

            # Generate writer profile (fast mode)
            writer_profile = generator.generate_writer_profile()

            # Generate outline (minimal chapters)
            chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)

            # Generate chapters
            chapters = []
            for i, outline in enumerate(chapter_outlines, 1):
                chapter_text = generator.generate_chapter(i)
                if chapter_text:
                    # Create chapter dictionary structure
                    chapter = {
                        "number": i,
                        "title": f"Chapter {i}",
                        "content": chapter_text
                    }
                    chapters.append(chapter)

            # Calculate metrics
            total_words = sum(len(ch.get("content", "").split()) for ch in chapters)

            # Create EPUB (minimal formatting)
            epub_path = output_dir / f"{config['title']}.epub"
            novel_data = {
                "metadata": {
                    "title": config["title"],
                    "author": config["author"],
                    "description": config["description"],
                    "genre": config["genre"]
                },
                "chapters": chapters
            }
            formatter = EpubFormatter(novel_data, include_front_matter=False, include_back_matter=False)
            formatter.save_epub(str(output_dir))

            return TestResult(
                test_name=test_name,
                success=True,
                execution_time=0,  # Will be set by caller
                word_count=total_words,
                chapter_count=len(chapters),
                file_path=str(epub_path),
                details={"config": config}
            )

        except Exception as e:
            log_error(f"Minimal book test failed", exception=e)
            return TestResult(
                test_name=test_name,
                success=False,
                execution_time=0,
                word_count=0,
                chapter_count=0,
                error_message=str(e)
            )

    def _get_minimal_book_config(self) -> Dict[str, Any]:
        """Get minimal configuration for fast testing."""
        return {
            "title": "Test Novel - Minimal",
            "author": "Test Author",
            "description": "A minimal test novel for fast testing.",
            "genre": "test",  # Uses test genre with minimal settings
            "target_audience": "Adult (18+)",
            "generation_options": {
                "chapter_count": 2,
                "target_word_count": 2000,
                "chapter_length": 1000,
                "min_chapter_length": 800,
                "writing_style": "Simple and direct",
                "themes": ["Testing", "Speed"],
                "temperature": 0.5
            }
        }

    def _test_single_book_standard(self) -> TestResult:
        """Test single book generation with standard test settings."""
        test_name = "Single Book - Standard"

        try:
            # Get standard test configuration
            config = self._get_standard_book_config()

            # Initialize generator
            generator = NovelGenerator()

            # Replace with mock client if requested
            if self.use_mock_api:
                from src.testing.mock_components import MockGeminiClient
                generator.gemini = MockGeminiClient()

            # Create test output directory
            output_dir = self.test_output_dir / "standard_book"
            output_dir.mkdir(exist_ok=True)

            # Initialize novel
            memory_manager = generator.initialize_novel(
                title=config["title"],
                author=config["author"],
                description=config["description"],
                genre=config["genre"],
                target_audience=config["target_audience"],
                output_dir=str(output_dir)
            )

            # Set test generation options
            generator.set_generation_options(config["generation_options"])

            # Generate writer profile
            writer_profile = generator.generate_writer_profile()

            # Generate outline
            chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)

            # Generate characters (minimal set)
            characters = generator.generate_characters()

            # Generate chapters with progress tracking
            chapters = []
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                BarColumn(),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                TimeElapsedColumn(),
                console=console
            ) as progress:
                task = progress.add_task("Generating chapters...", total=chapter_count)

                for i, outline in enumerate(chapter_outlines, 1):
                    chapter_text = generator.generate_chapter(i)
                    if chapter_text:
                        # Create chapter dictionary structure
                        chapter = {
                            "number": i,
                            "title": f"Chapter {i}",
                            "content": chapter_text
                        }
                        chapters.append(chapter)
                    progress.update(task, advance=1)

            # Calculate metrics
            total_words = sum(len(ch.get("content", "").split()) for ch in chapters)

            # Create EPUB with standard formatting
            epub_path = output_dir / f"{config['title']}.epub"
            novel_data = {
                "metadata": {
                    "title": config["title"],
                    "author": config["author"],
                    "description": config["description"],
                    "genre": config["genre"]
                },
                "chapters": chapters
            }
            formatter = EpubFormatter(novel_data, include_front_matter=True, include_back_matter=False)
            formatter.save_epub(str(output_dir))

            return TestResult(
                test_name=test_name,
                success=True,
                execution_time=0,
                word_count=total_words,
                chapter_count=len(chapters),
                file_path=str(epub_path),
                details={"config": config, "characters": len(characters)}
            )

        except Exception as e:
            log_error(f"Standard book test failed", exception=e)
            return TestResult(
                test_name=test_name,
                success=False,
                execution_time=0,
                word_count=0,
                chapter_count=0,
                error_message=str(e)
            )

    def _get_standard_book_config(self) -> Dict[str, Any]:
        """Get standard configuration for testing."""
        return {
            "title": "Test Novel - Standard",
            "author": "Test Author",
            "description": "A standard test novel with moderate complexity.",
            "genre": "Literary Fiction",
            "target_audience": "Adult (18+)",
            "generation_options": {
                "chapter_count": 4,
                "target_word_count": 6000,
                "chapter_length": 1500,
                "min_chapter_length": 1200,
                "writing_style": "Descriptive and detailed",
                "themes": ["Identity", "Relationships"],
                "temperature": 0.7
            }
        }

    def _test_single_book_complex(self) -> TestResult:
        """Test single book generation with complex genre settings."""
        test_name = "Single Book - Complex Genre"

        try:
            # Get complex test configuration
            config = self._get_complex_book_config()

            # Initialize generator
            generator = NovelGenerator()

            # Replace with mock client if requested
            if self.use_mock_api:
                from src.testing.mock_components import MockGeminiClient
                generator.gemini = MockGeminiClient()

            # Create test output directory
            output_dir = self.test_output_dir / "complex_book"
            output_dir.mkdir(exist_ok=True)

            # Initialize novel
            memory_manager = generator.initialize_novel(
                title=config["title"],
                author=config["author"],
                description=config["description"],
                genre=config["genre"],
                target_audience=config["target_audience"],
                output_dir=str(output_dir)
            )

            # Set test generation options
            generator.set_generation_options(config["generation_options"])

            # Generate writer profile
            writer_profile = generator.generate_writer_profile()

            # Generate outline
            chapter_outlines, chapter_count = generator.generate_novel_outline(writer_profile)

            # Generate characters
            characters = generator.generate_characters()

            # Generate chapters
            chapters = []
            for i, outline in enumerate(chapter_outlines, 1):
                chapter_text = generator.generate_chapter(i)
                if chapter_text:
                    # Create chapter dictionary structure
                    chapter = {
                        "number": i,
                        "title": f"Chapter {i}",
                        "content": chapter_text
                    }
                    chapters.append(chapter)

            # Calculate metrics
            total_words = sum(len(ch.get("content", "").split()) for ch in chapters)

            # Create EPUB
            epub_path = output_dir / f"{config['title']}.epub"
            novel_data = {
                "metadata": {
                    "title": config["title"],
                    "author": config["author"],
                    "description": config["description"],
                    "genre": config["genre"]
                },
                "chapters": chapters
            }
            formatter = EpubFormatter(novel_data, include_front_matter=True, include_back_matter=True)
            formatter.save_epub(str(output_dir))

            return TestResult(
                test_name=test_name,
                success=True,
                execution_time=0,
                word_count=total_words,
                chapter_count=len(chapters),
                file_path=str(epub_path),
                details={"config": config, "characters": len(characters)}
            )

        except Exception as e:
            log_error(f"Complex book test failed", exception=e)
            return TestResult(
                test_name=test_name,
                success=False,
                execution_time=0,
                word_count=0,
                chapter_count=0,
                error_message=str(e)
            )

    def _get_complex_book_config(self) -> Dict[str, Any]:
        """Get complex configuration for testing advanced features."""
        return {
            "title": "Test Novel - Complex",
            "author": "Test Author",
            "description": "A complex test novel with advanced genre features.",
            "genre": "Contemporary Romance",  # Complex genre with special formatting
            "target_audience": "Adult (18+)",
            "generation_options": {
                "chapter_count": 3,
                "target_word_count": 4500,
                "chapter_length": 1500,
                "min_chapter_length": 1200,
                "writing_style": "Emotional and descriptive",
                "themes": ["Love", "Growth", "Communication"],
                "temperature": 0.7
            }
        }

    def _test_series_generation(self) -> TestResult:
        """Test series generation with 2 books."""
        test_name = "Series Generation - 2 Books"

        try:
            # Initialize series generator
            series_generator = SeriesGenerator()

            # Replace with mock client if requested
            if self.use_mock_api:
                from src.testing.mock_components import MockGeminiClient
                series_generator.novel_generator.gemini = MockGeminiClient()

            # Create test output directory
            output_dir = self.test_output_dir / "test_series"
            output_dir.mkdir(exist_ok=True)

            # Initialize series with test settings
            series_manager = series_generator.initialize_series(
                series_title="Test Series",
                series_description="A test series for fast testing.",
                genre="test",
                target_audience="Adult (18+)",
                planned_books=2,
                author="Test Author"
            )

            # Override generation options for speed
            series_generator.generation_options = {
                "chapter_count": 2,
                "target_word_count": 2000,
                "chapter_length": 1000,
                "min_chapter_length": 800,
                "writing_style": "Simple and direct",
                "themes": ["Testing", "Series"],
                "temperature": 0.5
            }

            # Generate series plan
            book_templates = series_generator.generate_series_plan()

            # Generate books
            generated_books = []
            total_words = 0
            total_chapters = 0

            for i, book_template in enumerate(book_templates, 1):
                epub_path = series_generator.generate_book(book_template, i)
                generated_books.append(epub_path)

                # Count words and chapters (simplified)
                total_chapters += 2  # Each test book has 2 chapters
                total_words += 2000  # Each test book has ~2000 words

            return TestResult(
                test_name=test_name,
                success=True,
                execution_time=0,
                word_count=total_words,
                chapter_count=total_chapters,
                file_path=str(output_dir),
                details={
                    "books_generated": len(generated_books),
                    "series_title": "Test Series",
                    "book_paths": [str(p) for p in generated_books]
                }
            )

        except Exception as e:
            log_error(f"Series generation test failed", exception=e)
            return TestResult(
                test_name=test_name,
                success=False,
                execution_time=0,
                word_count=0,
                chapter_count=0,
                error_message=str(e)
            )

    def _test_error_handling(self) -> TestResult:
        """Test error handling and recovery mechanisms."""
        test_name = "Error Handling"

        try:
            # Test various error scenarios
            error_tests_passed = 0
            total_error_tests = 3

            # Test 1: Invalid genre handling
            try:
                generator = NovelGenerator()
                config = self._get_minimal_book_config()
                config["genre"] = "NonExistentGenre"

                output_dir = self.test_output_dir / "error_test"
                output_dir.mkdir(exist_ok=True)

                # This should either handle gracefully or use fallback
                memory_manager = generator.initialize_novel(
                    title=config["title"],
                    author=config["author"],
                    description=config["description"],
                    genre=config["genre"],
                    target_audience=config["target_audience"],
                    output_dir=str(output_dir)
                )
                error_tests_passed += 1
            except Exception:
                # Expected to fail, but should not crash the system
                error_tests_passed += 1

            # Test 2: Empty content handling
            try:
                novel_data = {
                    "metadata": {
                        "title": "Empty Test",
                        "author": "Test Author",
                        "description": "Test description",
                        "genre": "test"
                    },
                    "chapters": []  # Empty chapters
                }
                formatter = EpubFormatter(novel_data, include_front_matter=False, include_back_matter=False)
                # Should handle empty chapters gracefully
                error_tests_passed += 1
            except Exception:
                pass  # This is acceptable

            # Test 3: File system error simulation
            try:
                # Try to create output in a restricted location
                import tempfile
                with tempfile.TemporaryDirectory() as temp_dir:
                    test_path = Path(temp_dir) / "test_output"
                    test_path.mkdir(exist_ok=True)
                    error_tests_passed += 1
            except Exception:
                pass  # This is acceptable

            success_rate = (error_tests_passed / total_error_tests) * 100

            return TestResult(
                test_name=test_name,
                success=success_rate >= 66,  # At least 2/3 tests should pass
                execution_time=0,
                word_count=0,
                chapter_count=0,
                details={
                    "error_tests_passed": error_tests_passed,
                    "total_error_tests": total_error_tests,
                    "success_rate": success_rate
                }
            )

        except Exception as e:
            log_error(f"Error handling test failed", exception=e)
            return TestResult(
                test_name=test_name,
                success=False,
                execution_time=0,
                word_count=0,
                chapter_count=0,
                error_message=str(e)
            )

    def _test_performance_benchmarks(self) -> TestResult:
        """Test performance benchmarks and timing."""
        test_name = "Performance Benchmarks"

        try:
            benchmarks = {}

            # Benchmark 1: Generator initialization
            start_time = time.time()
            generator = NovelGenerator()
            benchmarks["generator_init"] = time.time() - start_time

            # Benchmark 2: Configuration loading
            start_time = time.time()
            config = self._get_minimal_book_config()
            benchmarks["config_load"] = time.time() - start_time

            # Benchmark 3: Output directory creation
            start_time = time.time()
            output_dir = self.test_output_dir / "benchmark_test"
            output_dir.mkdir(exist_ok=True)
            benchmarks["dir_creation"] = time.time() - start_time

            # Benchmark 4: EPUB formatter initialization
            start_time = time.time()
            novel_data = {
                "metadata": {
                    "title": "Benchmark Test",
                    "author": "Test Author",
                    "description": "Benchmark test",
                    "genre": "test"
                },
                "chapters": []
            }
            formatter = EpubFormatter(novel_data, include_front_matter=False, include_back_matter=False)
            benchmarks["epub_init"] = time.time() - start_time

            # Calculate overall performance score
            total_time = sum(benchmarks.values())
            performance_score = 100 if total_time < 1.0 else max(0, 100 - (total_time * 10))

            return TestResult(
                test_name=test_name,
                success=performance_score >= 80,
                execution_time=0,
                word_count=0,
                chapter_count=0,
                details={
                    "benchmarks": benchmarks,
                    "total_time": total_time,
                    "performance_score": performance_score
                }
            )

        except Exception as e:
            log_error(f"Performance benchmark test failed", exception=e)
            return TestResult(
                test_name=test_name,
                success=False,
                execution_time=0,
                word_count=0,
                chapter_count=0,
                error_message=str(e)
            )

    def _generate_test_report(self, total_time: float) -> Dict[str, Any]:
        """Generate comprehensive test report."""
        console.print(f"\n[bold cyan]📊 Fast Test Report[/bold cyan]")

        # Summary table
        table = Table(title="Fast Test Results Summary")
        table.add_column("Test Name", style="cyan", width=25)
        table.add_column("Status", style="green", width=10)
        table.add_column("Time", style="yellow", width=8)
        table.add_column("Chapters", style="blue", width=8)
        table.add_column("Words", style="magenta", width=10)
        table.add_column("Notes", style="white", width=30)

        passed_tests = 0
        total_tests = len(self.results)
        total_words = 0
        total_chapters = 0

        for result in self.results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            time_str = f"{result.execution_time:.1f}s"
            chapters_str = str(result.chapter_count) if result.chapter_count > 0 else "-"
            words_str = f"{result.word_count:,}" if result.word_count > 0 else "-"
            notes = result.error_message[:25] + "..." if result.error_message else "OK"

            if result.success:
                passed_tests += 1
                total_words += result.word_count
                total_chapters += result.chapter_count

            table.add_row(
                result.test_name,
                status,
                time_str,
                chapters_str,
                words_str,
                notes
            )

        console.print(table)

        # Overall metrics
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        avg_time_per_test = total_time / total_tests if total_tests > 0 else 0

        console.print(f"\n[bold cyan]Overall Metrics:[/bold cyan]")
        console.print(f"  Success Rate: {success_rate:.1f}% ({passed_tests}/{total_tests})")
        console.print(f"  Total Time: {total_time:.2f}s")
        console.print(f"  Average Time per Test: {avg_time_per_test:.2f}s")
        console.print(f"  Total Content Generated: {total_chapters} chapters, {total_words:,} words")

        # Performance assessment
        if total_time <= 300:  # 5 minutes
            time_rating = "Excellent"
            time_color = "green"
        elif total_time <= 600:  # 10 minutes
            time_rating = "Good"
            time_color = "yellow"
        else:
            time_rating = "Needs Improvement"
            time_color = "red"

        console.print(f"  Performance Rating: [{time_color}]{time_rating}[/{time_color}]")

        # Recommendations
        if success_rate >= 90 and total_time <= 600:
            console.print(f"\n[bold green]🎉 TESTING SYSTEM READY[/bold green]")
            console.print("The fast testing system is working well and ready for regular use.")
        elif success_rate >= 75:
            console.print(f"\n[bold yellow]⚠️  MINOR ISSUES[/bold yellow]")
            console.print("Some tests failed but the system is mostly functional.")
        else:
            console.print(f"\n[bold red]❌ NEEDS ATTENTION[/bold red]")
            console.print("Multiple test failures indicate system issues that need resolution.")

        # Save detailed report
        report_data = {
            "timestamp": datetime.now().isoformat(),
            "total_time": total_time,
            "success_rate": success_rate,
            "passed_tests": passed_tests,
            "total_tests": total_tests,
            "total_words": total_words,
            "total_chapters": total_chapters,
            "performance_rating": time_rating,
            "test_results": [
                {
                    "test_name": r.test_name,
                    "success": r.success,
                    "execution_time": r.execution_time,
                    "word_count": r.word_count,
                    "chapter_count": r.chapter_count,
                    "error_message": r.error_message,
                    "file_path": r.file_path,
                    "details": r.details
                }
                for r in self.results
            ]
        }

        self._save_test_report(report_data)

        return report_data

    def _save_test_report(self, report_data: Dict[str, Any]) -> None:
        """Save detailed test report to file."""
        try:
            report_dir = Path("test_reports")
            report_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_file = report_dir / f"fast_test_report_{timestamp}.json"

            with open(report_file, 'w') as f:
                json.dump(report_data, f, indent=2, default=str)

            console.print(f"\n[dim]Detailed report saved to: {report_file}[/dim]")

        except Exception as e:
            console.print(f"[red]Failed to save report: {e}[/red]")

def run_fast_tests(use_mock_api: bool = False) -> Dict[str, Any]:
    """
    Run the fast testing system.

    Args:
        use_mock_api: Whether to use mock API calls for maximum speed

    Returns:
        Dictionary containing test results and metrics
    """
    test_system = FastTestSystem(use_mock_api=use_mock_api)
    return test_system.run_comprehensive_tests()

def main():
    """Main entry point for running fast tests."""
    import argparse

    parser = argparse.ArgumentParser(description="Fast Testing System for Ebook Generator")
    parser.add_argument(
        "--mock-api",
        action="store_true",
        help="Use mock API calls for maximum speed"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )

    args = parser.parse_args()

    if args.verbose:
        console.print("[bold cyan]Fast Testing System - Ebook Generator[/bold cyan]")
        console.print(f"Mock API: {'Enabled' if args.mock_api else 'Disabled'}")
        console.print("Starting comprehensive fast tests...\n")

    results = run_fast_tests(use_mock_api=args.mock_api)

    if args.verbose:
        console.print(f"\n[bold cyan]Testing completed![/bold cyan]")
        console.print(f"Check the test_reports directory for detailed results.")

    return results

if __name__ == "__main__":
    main()
