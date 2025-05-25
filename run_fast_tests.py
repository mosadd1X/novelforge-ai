#!/usr/bin/env python3
"""
Fast Test Runner for NovelForge AI

This script provides a simple command-line interface to run the fast testing
system for NovelForge AI. It can be used independently for development
and debugging purposes.

Usage:
    python run_fast_tests.py                    # Run all tests with real API
    python run_fast_tests.py --mock-api         # Run all tests with mock API (fastest)
    python run_fast_tests.py --minimal          # Run minimal tests only
    python run_fast_tests.py --series           # Run series tests only
    python run_fast_tests.py --benchmark        # Run performance benchmarks only
    python run_fast_tests.py --help             # Show help information
"""

import sys
import argparse
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from rich.console import Console
from rich.panel import Panel

console = Console(markup=True)

def main():
    """Main entry point for the fast test runner."""
    parser = argparse.ArgumentParser(
        description="Fast Testing System for Ebook Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_fast_tests.py                    # Run all tests with real API
  python run_fast_tests.py --mock-api         # Run all tests with mock API (fastest)
  python run_fast_tests.py --minimal          # Run minimal tests only
  python run_fast_tests.py --series           # Run series tests only
  python run_fast_tests.py --benchmark        # Run performance benchmarks only
        """
    )

    # Test mode options
    parser.add_argument(
        "--mock-api",
        action="store_true",
        help="Use mock API calls for maximum speed (recommended for development)"
    )

    # Test type options (mutually exclusive)
    test_group = parser.add_mutually_exclusive_group()
    test_group.add_argument(
        "--minimal",
        action="store_true",
        help="Run minimal tests only (fastest, ~1-2 minutes)"
    )
    test_group.add_argument(
        "--series",
        action="store_true",
        help="Run series generation tests only (~3-4 minutes)"
    )
    test_group.add_argument(
        "--benchmark",
        action="store_true",
        help="Run performance benchmarks only (~30 seconds)"
    )
    test_group.add_argument(
        "--single",
        action="store_true",
        help="Run single book tests only (~2-3 minutes)"
    )

    # Output options
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress non-essential output"
    )

    args = parser.parse_args()

    # Display header
    if not args.quiet:
        console.print(Panel.fit(
            "[bold cyan]Fast Testing System - Ebook Generator[/bold cyan]\n"
            "Rapid testing for development and debugging",
            border_style="cyan"
        ))

        console.print(f"[bold]Configuration:[/bold]")
        console.print(f"  Mock API: {'Enabled' if args.mock_api else 'Disabled'}")

        if args.minimal:
            test_type = "Minimal Tests"
            estimated_time = "1-2 minutes"
        elif args.series:
            test_type = "Series Tests"
            estimated_time = "3-4 minutes"
        elif args.benchmark:
            test_type = "Performance Benchmarks"
            estimated_time = "30 seconds"
        elif args.single:
            test_type = "Single Book Tests"
            estimated_time = "2-3 minutes"
        else:
            test_type = "All Tests"
            estimated_time = "5-10 minutes"

        console.print(f"  Test Type: {test_type}")
        console.print(f"  Estimated Time: {estimated_time}")
        console.print()

    try:
        # Import the fast testing system
        from src.testing.fast_test_system import FastTestSystem

        # Initialize the test system
        test_system = FastTestSystem(use_mock_api=args.mock_api)

        if not args.quiet:
            console.print("[bold yellow]Starting tests...[/bold yellow]\n")

        # Run the appropriate tests
        if args.minimal:
            result = test_system._test_single_book_minimal()
            results = {"Minimal Test": result} if result else {}
        elif args.series:
            result = test_system._test_series_generation()
            results = {"Series Test": result} if result else {}
        elif args.benchmark:
            result = test_system._test_performance_benchmarks()
            results = {"Benchmark Test": result} if result else {}
        elif args.single:
            result = test_system._test_single_book_standard()
            results = {"Single Book Test": result} if result else {}
        else:
            # Run comprehensive tests
            results = test_system.run_comprehensive_tests()

        # Display results summary
        if not args.quiet:
            console.print(f"\n[bold green]Testing completed![/bold green]")

            if results:
                # Handle both TestResult objects and dictionaries
                passed_tests = 0
                for r in results.values():
                    if hasattr(r, 'success'):
                        # TestResult object
                        if r.success:
                            passed_tests += 1
                    elif isinstance(r, dict):
                        # Dictionary result
                        if r.get('passed', False):
                            passed_tests += 1

                total_tests = len(results)
                success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0

                console.print(f"Success Rate: {success_rate:.1f}% ({passed_tests}/{total_tests})")
                console.print("Check the test_reports directory for detailed results.")

        # Exit with appropriate code
        if results:
            failed_tests = []
            for name, result in results.items():
                if hasattr(result, 'success'):
                    # TestResult object
                    if not result.success:
                        failed_tests.append(name)
                elif isinstance(result, dict):
                    # Dictionary result
                    if not result.get('passed', False):
                        failed_tests.append(name)
            if failed_tests:
                if args.verbose:
                    console.print(f"\n[bold red]Failed tests:[/bold red]")
                    for test_name in failed_tests:
                        console.print(f"  - {test_name}")
                sys.exit(1)
            else:
                sys.exit(0)
        else:
            console.print("[bold red]No test results available[/bold red]")
            sys.exit(1)

    except ImportError as e:
        console.print(f"[bold red]Error: Fast testing system not available[/bold red]")
        console.print(f"[red]{e}[/red]")
        console.print("\n[yellow]Make sure you're running from the project root directory.[/yellow]")
        sys.exit(1)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Testing interrupted by user[/bold yellow]")
        sys.exit(130)
    except Exception as e:
        console.print(f"[bold red]Error during testing: {e}[/bold red]")
        if args.verbose:
            import traceback
            console.print(f"[dim]{traceback.format_exc()}[/dim]")
        sys.exit(1)

if __name__ == "__main__":
    main()
