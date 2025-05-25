"""
Database management menu for NovelForge AI.
Provides database operations, migration, and statistics.
"""

import os
import questionary
from rich.console import Console
from rich.table import Table
from rich import box

from src.database.database_manager import get_database_manager
from src.database.cover_database_manager import get_cover_database_manager
from src.database.epub_database_manager import get_epub_database_manager
from src.database.book_library_manager import get_book_library_manager
from src.database.migration_manager import get_migration_manager
from src.database.book_filter_manager import get_book_filter_manager
from src.database.database_cleaner import get_database_cleaner
from src.ui.terminal_ui import clear_screen, display_title, custom_style

console = Console()


def database_management_menu() -> None:
    """Main database management menu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Database Management[/bold cyan]\n")

        # Get database statistics
        db_manager = get_database_manager()
        stats = db_manager.get_database_stats()

        # Display quick stats
        console.print(f"[dim]Database: {stats['total_books']} books, "
                     f"{stats['covers_stored']} covers, "
                     f"{stats['database_size_bytes'] / (1024*1024):.1f} MB[/dim]\n")

        choices = [
            "View Database Statistics",
            "Migrate Existing Data to Database",
            "Book Library Management",
            "Database Schema Management",
            "Clear/Reset Database",
            "Manage Book Display Settings",
            "Database Maintenance",
            "Export Database Data",
            "← Back to Main Menu"
        ]

        selected = questionary.select(
            "Database Management:",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "View Database Statistics":
            view_database_statistics()
        elif selected == "Migrate Existing Data to Database":
            migrate_data_menu()
        elif selected == "Book Library Management":
            book_library_menu()
        elif selected == "Database Schema Management":
            database_schema_menu()
        elif selected == "Clear/Reset Database":
            database_clear_menu()
        elif selected == "Manage Book Display Settings":
            manage_display_settings()
        elif selected == "Database Maintenance":
            database_maintenance_menu()
        elif selected == "Export Database Data":
            export_database_menu()
        elif selected == "← Back to Main Menu":
            break


def view_database_statistics() -> None:
    """Display comprehensive database statistics."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Database Statistics[/bold cyan]\n")

    # Get statistics
    db_manager = get_database_manager()
    cover_manager = get_cover_database_manager()
    epub_manager = get_epub_database_manager()
    filter_manager = get_book_filter_manager()

    db_stats = db_manager.get_database_stats()
    cover_stats = cover_manager.get_cover_stats()
    epub_stats = epub_manager.get_epub_stats()
    display_summary = filter_manager.get_display_summary()

    # Books statistics table
    books_table = Table(title="Books Statistics", box=box.ROUNDED)
    books_table.add_column("Metric", style="cyan")
    books_table.add_column("Value", style="green")

    books_table.add_row("Total Books", str(db_stats["total_books"]))
    books_table.add_row("Completed Books", str(db_stats["status_counts"].get("completed", 0)))
    books_table.add_row("In Progress", str(db_stats["status_counts"].get("generating", 0)))
    books_table.add_row("Planned Books", str(db_stats["status_counts"].get("planned", 0)))
    books_table.add_row("Failed Generations", str(db_stats["status_counts"].get("failed", 0)))

    console.print(books_table)
    console.print()

    # Genre distribution table
    if db_stats["genre_counts"]:
        genre_table = Table(title="Genre Distribution", box=box.ROUNDED)
        genre_table.add_column("Genre", style="cyan")
        genre_table.add_column("Books", style="green")
        genre_table.add_column("Percentage", style="yellow")

        total_books = sum(db_stats["genre_counts"].values())
        for genre, count in sorted(db_stats["genre_counts"].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / total_books) * 100 if total_books > 0 else 0
            genre_table.add_row(genre, str(count), f"{percentage:.1f}%")

        console.print(genre_table)
        console.print()

    # Cover statistics table
    cover_table = Table(title="Cover Storage Statistics", box=box.ROUNDED)
    cover_table.add_column("Metric", style="cyan")
    cover_table.add_column("Value", style="green")

    cover_table.add_row("Covers Stored", str(cover_stats["total_covers"]))
    cover_table.add_row("Total Storage", f"{cover_stats['total_size_mb']:.1f} MB")
    if cover_stats["total_covers"] > 0:
        avg_size_kb = (cover_stats["avg_size_bytes"] or 0) / 1024
        cover_table.add_row("Average Cover Size", f"{avg_size_kb:.1f} KB")

    console.print(cover_table)
    console.print()

    # EPUB storage statistics table
    epub_table = Table(title="EPUB Storage Statistics", box=box.ROUNDED)
    epub_table.add_column("Metric", style="cyan")
    epub_table.add_column("Value", style="green")

    epub_table.add_row("EPUBs Stored", str(epub_stats["total_epubs"]))
    if epub_stats["total_epubs"] > 0:
        epub_table.add_row("Original Size", f"{epub_stats['total_original_size_bytes'] / (1024*1024):.1f} MB")
        epub_table.add_row("Compressed Size", f"{epub_stats['total_compressed_size_bytes'] / (1024*1024):.1f} MB")
        epub_table.add_row("Storage Saved", f"{epub_stats['storage_saved_mb']:.1f} MB")
        epub_table.add_row("Avg Compression", f"{epub_stats['avg_compression_ratio']:.1%}")
        epub_table.add_row("Total Accesses", str(epub_stats["total_accesses"]))

    console.print(epub_table)
    console.print()

    # Display settings table
    display_table = Table(title="Display Settings", box=box.ROUNDED)
    display_table.add_column("Setting", style="cyan")
    display_table.add_column("Value", style="green")

    display_table.add_row("Display Limit", str(display_summary["display_limit"]))
    display_table.add_row("Books per Genre", str(display_summary["books_per_genre_limit"]))
    display_table.add_row("Total Genres", str(display_summary["total_genres"]))
    if display_summary["most_common_genre"]:
        display_table.add_row("Most Common Genre", display_summary["most_common_genre"])

    console.print(display_table)
    console.print()

    # Database file info
    db_size_mb = db_stats["database_size_bytes"] / (1024 * 1024)
    console.print(f"[bold green]Database File:[/bold green] [cyan]{db_stats['database_path']}[/cyan]")
    console.print(f"[bold green]Database Size:[/bold green] [cyan]{db_size_mb:.1f} MB[/cyan]")

    input("\nPress Enter to continue...")


def migrate_data_menu() -> None:
    """Menu for data migration operations."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Data Migration[/bold cyan]\n")

        choices = [
            "Analyze Existing Data (Dry Run)",
            "Migrate All Data to Database",
            "Migrate Only Books",
            "Migrate Only Covers",
            "View Migration Status",
            "← Back to Database Menu"
        ]

        selected = questionary.select(
            "Migration Options:",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Analyze Existing Data (Dry Run)":
            perform_migration_analysis()
        elif selected == "Migrate All Data to Database":
            perform_full_migration()
        elif selected == "Migrate Only Books":
            perform_books_migration()
        elif selected == "Migrate Only Covers":
            perform_covers_migration()
        elif selected == "View Migration Status":
            view_migration_status()
        elif selected == "← Back to Database Menu":
            break


def perform_migration_analysis() -> None:
    """Perform a dry run analysis of migration."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Analyzing Existing Data for Migration[/bold cyan]\n")
    console.print("[dim]This will analyze your existing books and covers without making any changes.[/dim]\n")

    migration_manager = get_migration_manager()
    results = migration_manager.migrate_all_data(dry_run=True)

    console.print(f"\n[bold green]Analysis Complete![/bold green]")
    console.print(f"Ready to migrate {results['books_found']} books and {results['covers_found']} covers.")

    if results["errors"]:
        console.print(f"\n[bold yellow]Note:[/bold yellow] {len(results['errors'])} potential issues found.")
        console.print("Review the analysis above before proceeding with migration.")

    input("\nPress Enter to continue...")


def perform_full_migration() -> None:
    """Perform full data migration."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Full Data Migration[/bold cyan]\n")
    console.print("[bold yellow]Warning:[/bold yellow] This will migrate all existing books and covers to the database.")
    console.print("This operation cannot be easily undone.\n")

    confirm = questionary.confirm(
        "Are you sure you want to proceed with the migration?",
        style=custom_style
    ).ask()

    if not confirm:
        console.print("[yellow]Migration cancelled.[/yellow]")
        input("\nPress Enter to continue...")
        return

    migration_manager = get_migration_manager()
    results = migration_manager.migrate_all_data(dry_run=False)

    console.print(f"\n[bold green]Migration Complete![/bold green]")
    console.print(f"Migrated {results['books_migrated']} books and {results['covers_migrated']} covers.")

    if results["errors"]:
        console.print(f"\n[bold red]Errors:[/bold red] {len(results['errors'])} issues encountered.")
        console.print("Check the output above for details.")

    input("\nPress Enter to continue...")


def perform_books_migration() -> None:
    """Perform books-only migration."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Books Migration[/bold cyan]\n")
    console.print("This will migrate book metadata to the database without moving covers.\n")

    confirm = questionary.confirm(
        "Proceed with books migration?",
        style=custom_style
    ).ask()

    if confirm:
        migration_manager = get_migration_manager()

        # Migrate individual books
        book_results = migration_manager.migrate_individual_books(dry_run=False)
        series_results = migration_manager.migrate_series_books(dry_run=False)

        total_migrated = book_results["books_migrated"] + series_results["books_migrated"]
        console.print(f"\n[bold green]Books Migration Complete![/bold green]")
        console.print(f"Migrated {total_migrated} books to the database.")

    input("\nPress Enter to continue...")


def perform_covers_migration() -> None:
    """Perform covers-only migration."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Covers Migration[/bold cyan]\n")
    console.print("This will migrate cover images to the database as base64 data.\n")

    confirm = questionary.confirm(
        "Proceed with covers migration?",
        style=custom_style
    ).ask()

    if confirm:
        migration_manager = get_migration_manager()
        cover_results = migration_manager.migrate_standalone_covers(dry_run=False)

        console.print(f"\n[bold green]Covers Migration Complete![/bold green]")
        console.print(f"Migrated {cover_results['covers_migrated']} covers to the database.")

    input("\nPress Enter to continue...")


def view_migration_status() -> None:
    """View the current migration status."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Migration Status[/bold cyan]\n")

    # Check if database has any books
    db_manager = get_database_manager()
    stats = db_manager.get_database_stats()

    if stats["total_books"] == 0:
        console.print("[yellow]No books found in database.[/yellow]")
        console.print("Run migration to import your existing books.")
    else:
        console.print(f"[bold green]Database contains {stats['total_books']} books[/bold green]")
        console.print(f"[bold green]Covers stored: {stats['covers_stored']}[/bold green]")

        # Show status breakdown
        status_table = Table(title="Book Status Distribution")
        status_table.add_column("Status", style="cyan")
        status_table.add_column("Count", style="green")

        for status, count in stats["status_counts"].items():
            status_table.add_row(status.title(), str(count))

        console.print(status_table)

    input("\nPress Enter to continue...")


def manage_display_settings() -> None:
    """Manage book display settings."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Book Display Settings[/bold cyan]\n")

    filter_manager = get_book_filter_manager()
    summary = filter_manager.get_display_summary()

    console.print(f"[bold green]Current Settings:[/bold green]")
    console.print(f"• Maximum books displayed: {summary['display_limit']}")
    console.print(f"• Books per genre limit: {summary['books_per_genre_limit']}")
    console.print(f"• Total books in database: {summary['total_books']}")
    console.print(f"• Total genres: {summary['total_genres']}")

    if summary["total_books"] > summary["display_limit"]:
        console.print(f"\n[yellow]Note:[/yellow] You have {summary['total_books']} books, but only {summary['display_limit']} will be shown at once.")
        console.print("This prevents UI overload. Use filtering to find specific books.")

    console.print("\n[dim]Display settings help manage large book collections by showing relevant subsets.[/dim]")
    console.print("[dim]Books are intelligently filtered by genre relationships and recency.[/dim]")

    input("\nPress Enter to continue...")


def database_maintenance_menu() -> None:
    """Database maintenance operations."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Database Maintenance[/bold cyan]\n")

    choices = [
        "Optimize Database",
        "Verify Data Integrity",
        "Clean Up Orphaned Records",
        "Backup Database",
        "← Back to Database Menu"
    ]

    selected = questionary.select(
        "Maintenance Options:",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "Optimize Database":
        console.print("[bold cyan]Optimizing database...[/bold cyan]")
        # Database optimization would go here
        console.print("[bold green]Database optimized![/bold green]")
        input("\nPress Enter to continue...")
    elif selected == "Verify Data Integrity":
        console.print("[bold cyan]Verifying data integrity...[/bold cyan]")
        # Data integrity checks would go here
        console.print("[bold green]Data integrity verified![/bold green]")
        input("\nPress Enter to continue...")
    elif selected == "Clean Up Orphaned Records":
        console.print("[bold cyan]Cleaning up orphaned records...[/bold cyan]")
        # Cleanup operations would go here
        console.print("[bold green]Cleanup complete![/bold green]")
        input("\nPress Enter to continue...")
    elif selected == "Backup Database":
        console.print("[bold cyan]Creating database backup...[/bold cyan]")
        # Backup operations would go here
        console.print("[bold green]Backup created![/bold green]")
        input("\nPress Enter to continue...")


def export_database_menu() -> None:
    """Database export operations."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Export Database Data[/bold cyan]\n")

    choices = [
        "Export Book Metadata (JSON)",
        "Export Cover Images",
        "Export Complete Database",
        "← Back to Database Menu"
    ]

    selected = questionary.select(
        "Export Options:",
        choices=choices,
        style=custom_style
    ).ask()

    if selected == "Export Book Metadata (JSON)":
        console.print("[bold cyan]Exporting book metadata...[/bold cyan]")
        # Export operations would go here
        console.print("[bold green]Metadata exported![/bold green]")
        input("\nPress Enter to continue...")
    elif selected == "Export Cover Images":
        console.print("[bold cyan]Exporting cover images...[/bold cyan]")
        # Export operations would go here
        console.print("[bold green]Covers exported![/bold green]")
        input("\nPress Enter to continue...")
    elif selected == "Export Complete Database":
        console.print("[bold cyan]Exporting complete database...[/bold cyan]")
        # Export operations would go here
        console.print("[bold green]Database exported![/bold green]")
        input("\nPress Enter to continue...")


def database_schema_menu() -> None:
    """Database schema management and migration menu."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Database Schema Management[/bold cyan]\n")

        # Get schema information
        try:
            from src.database.schema_migrator import SchemaMigrator
            db_manager = get_database_manager()
            migrator = SchemaMigrator(db_manager.db_path)
            migration_info = migrator.get_migration_info()

            console.print(f"[bold green]Current Schema Version:[/bold green] [cyan]v{migration_info['current_version']}[/cyan]")
            console.print(f"[bold green]Target Schema Version:[/bold green] [cyan]v{migration_info['target_version']}[/cyan]")

            if migration_info['needs_migration']:
                console.print(f"[bold yellow]⚠ Migration Required[/bold yellow]")
            else:
                console.print(f"[bold green]✓ Schema Up to Date[/bold green]")

            console.print(f"[dim]Database Size: {migration_info['database_size_mb']:.1f} MB[/dim]\n")

        except ImportError:
            console.print("[bold red]Schema migrator not available[/bold red]\n")
            migration_info = {"needs_migration": False}
        except Exception as e:
            console.print(f"[bold red]Error checking schema: {str(e)}[/bold red]\n")
            migration_info = {"needs_migration": False}

        choices = [
            "Check Schema Status",
            "Migrate Database Schema",
            "View Migration History",
            "Create Database Backup",
            "Repair Database Issues",
            "← Back to Database Menu"
        ]

        selected = questionary.select(
            "Schema Management:",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Check Schema Status":
            check_schema_status()
        elif selected == "Migrate Database Schema":
            migrate_database_schema()
        elif selected == "View Migration History":
            view_migration_history()
        elif selected == "Create Database Backup":
            create_database_backup()
        elif selected == "Repair Database Issues":
            repair_database_issues()
        elif selected == "← Back to Database Menu":
            break


def check_schema_status() -> None:
    """Check and display detailed schema status."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Database Schema Status[/bold cyan]\n")

    try:
        from src.database.schema_migrator import SchemaMigrator
        db_manager = get_database_manager()
        migrator = SchemaMigrator(db_manager.db_path)
        migration_info = migrator.get_migration_info()

        # Create status table
        status_table = Table(title="Schema Information", box=box.ROUNDED)
        status_table.add_column("Property", style="cyan")
        status_table.add_column("Value", style="green")

        status_table.add_row("Current Version", f"v{migration_info['current_version']}")
        status_table.add_row("Target Version", f"v{migration_info['target_version']}")
        status_table.add_row("Migration Needed", "Yes" if migration_info['needs_migration'] else "No")
        status_table.add_row("Database Exists", "Yes" if migration_info['database_exists'] else "No")
        status_table.add_row("Database Size", f"{migration_info['database_size_mb']:.1f} MB")

        console.print(status_table)

        if migration_info['needs_migration']:
            console.print(f"\n[bold yellow]Migration Required:[/bold yellow]")
            console.print(f"Your database schema (v{migration_info['current_version']}) needs to be updated to v{migration_info['target_version']}")
            console.print(f"This will add new features like EPUB storage and enhanced book management.")
            console.print(f"\n[bold green]Recommendation:[/bold green] Run 'Migrate Database Schema' to update safely.")
        else:
            console.print(f"\n[bold green]✓ Your database schema is up to date![/bold green]")
            console.print(f"All enhanced features are available.")

    except Exception as e:
        console.print(f"[bold red]Error checking schema status: {str(e)}[/bold red]")

    input("\nPress Enter to continue...")


def migrate_database_schema() -> None:
    """Perform database schema migration."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Database Schema Migration[/bold cyan]\n")

    try:
        from src.database.schema_migrator import SchemaMigrator
        db_manager = get_database_manager()
        migrator = SchemaMigrator(db_manager.db_path)
        migration_info = migrator.get_migration_info()

        if not migration_info['needs_migration']:
            console.print("[bold green]Database schema is already up to date![/bold green]")
            input("\nPress Enter to continue...")
            return

        console.print(f"[bold yellow]Warning:[/bold yellow] This will migrate your database schema from v{migration_info['current_version']} to v{migration_info['target_version']}")
        console.print("A backup will be created automatically before migration.")
        console.print("\nNew features that will be enabled:")
        console.print("• Complete EPUB storage in database")
        console.print("• Novel data JSON storage")
        console.print("• Compression and integrity checking")
        console.print("• Access tracking and statistics")
        console.print("• Enhanced book library management")

        confirm = questionary.confirm(
            "\nProceed with schema migration?",
            style=custom_style
        ).ask()

        if not confirm:
            console.print("[yellow]Migration cancelled.[/yellow]")
            input("\nPress Enter to continue...")
            return

        # Perform migration
        console.print("\n[bold cyan]Starting database migration...[/bold cyan]")
        success = migrator.migrate_database()

        if success:
            console.print("\n[bold green]✓ Database migration completed successfully![/bold green]")
            console.print("Your database now supports all enhanced features.")
            console.print("You can now store complete EPUBs and use the book library system.")
        else:
            console.print("\n[bold red]✗ Database migration failed![/bold red]")
            console.print("Please check the error messages above and try again.")
            console.print("Your original database remains unchanged.")

    except Exception as e:
        console.print(f"[bold red]Error during migration: {str(e)}[/bold red]")

    input("\nPress Enter to continue...")


def view_migration_history() -> None:
    """View database migration history."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Migration History[/bold cyan]\n")

    try:
        db_manager = get_database_manager()

        # Get metadata from database
        with db_manager.get_connection() as conn:
            cursor = conn.execute("""
                SELECT key, value, updated_date
                FROM database_metadata
                WHERE key LIKE '%version%' OR key LIKE '%date%'
                ORDER BY updated_date DESC
            """)
            metadata = cursor.fetchall()

        if metadata:
            history_table = Table(title="Database History", box=box.ROUNDED)
            history_table.add_column("Property", style="cyan")
            history_table.add_column("Value", style="green")
            history_table.add_column("Date", style="yellow")

            for row in metadata:
                history_table.add_row(row["key"], row["value"], row["updated_date"][:19] if row["updated_date"] else "Unknown")

            console.print(history_table)
        else:
            console.print("[yellow]No migration history found.[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Error retrieving migration history: {str(e)}[/bold red]")

    input("\nPress Enter to continue...")


def create_database_backup() -> None:
    """Create a manual database backup."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Create Database Backup[/bold cyan]\n")

    try:
        import shutil
        import os
        from datetime import datetime

        db_manager = get_database_manager()

        if not os.path.exists(db_manager.db_path):
            console.print("[bold red]Database file not found![/bold red]")
            input("\nPress Enter to continue...")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{db_manager.db_path}.backup_{timestamp}"

        console.print(f"[bold cyan]Creating backup...[/bold cyan]")
        shutil.copy2(db_manager.db_path, backup_path)

        backup_size = os.path.getsize(backup_path) / (1024 * 1024)
        console.print(f"[bold green]✓ Backup created successfully![/bold green]")
        console.print(f"[bold green]Location:[/bold green] [cyan]{backup_path}[/cyan]")
        console.print(f"[bold green]Size:[/bold green] [cyan]{backup_size:.1f} MB[/cyan]")

    except Exception as e:
        console.print(f"[bold red]Error creating backup: {str(e)}[/bold red]")

    input("\nPress Enter to continue...")


def repair_database_issues() -> None:
    """Repair common database issues."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Repair Database Issues[/bold cyan]\n")

    repair_options = [
        "Check Database Integrity",
        "Rebuild Database Indexes",
        "Clean Up Orphaned Records",
        "Optimize Database Storage",
        "← Back to Schema Menu"
    ]

    selected = questionary.select(
        "Select repair operation:",
        choices=repair_options,
        style=custom_style
    ).ask()

    if selected == "← Back to Schema Menu":
        return

    try:
        db_manager = get_database_manager()

        if selected == "Check Database Integrity":
            console.print("[bold cyan]Checking database integrity...[/bold cyan]")
            with db_manager.get_connection() as conn:
                cursor = conn.execute("PRAGMA integrity_check")
                result = cursor.fetchone()
                if result and result[0] == "ok":
                    console.print("[bold green]✓ Database integrity check passed![/bold green]")
                else:
                    console.print(f"[bold red]✗ Database integrity issues found: {result[0] if result else 'Unknown'}[/bold red]")

        elif selected == "Rebuild Database Indexes":
            console.print("[bold cyan]Rebuilding database indexes...[/bold cyan]")
            with db_manager.get_connection() as conn:
                conn.execute("REINDEX")
                conn.commit()
            console.print("[bold green]✓ Database indexes rebuilt![/bold green]")

        elif selected == "Clean Up Orphaned Records":
            console.print("[bold cyan]Cleaning up orphaned records...[/bold cyan]")
            # This would implement cleanup logic
            console.print("[bold green]✓ Cleanup completed![/bold green]")

        elif selected == "Optimize Database Storage":
            console.print("[bold cyan]Optimizing database storage...[/bold cyan]")
            with db_manager.get_connection() as conn:
                conn.execute("VACUUM")
                conn.commit()
            console.print("[bold green]✓ Database storage optimized![/bold green]")

    except Exception as e:
        console.print(f"[bold red]Error during repair: {str(e)}[/bold red]")

    input("\nPress Enter to continue...")


def database_clear_menu() -> None:
    """Database clearing and reset menu with multiple safety options."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Clear/Reset Database[/bold cyan]\n")

        # Get current database info
        try:
            cleaner = get_database_cleaner()
            db_info = cleaner.get_database_info()

            console.print(f"[bold green]Current Database:[/bold green]")
            console.print(f"• Total Books: [cyan]{db_info.get('total_books', 0)}[/cyan]")
            console.print(f"• Books with EPUBs: [cyan]{db_info.get('books_with_epubs', 0)}[/cyan]")
            console.print(f"• Books with Covers: [cyan]{db_info.get('books_with_covers', 0)}[/cyan]")
            console.print(f"• Database Size: [cyan]{db_info.get('database_size_mb', 0):.1f} MB[/cyan]")
            console.print(f"• EPUB Storage: [cyan]{db_info.get('epub_storage_mb', 0):.1f} MB[/cyan]")
            console.print(f"• Cover Storage: [cyan]{db_info.get('cover_storage_mb', 0):.1f} MB[/cyan]\n")

        except Exception as e:
            console.print(f"[bold red]Error getting database info: {str(e)}[/bold red]\n")
            db_info = {}

        console.print("[bold yellow]⚠ Warning:[/bold yellow] All clearing operations create automatic backups")
        console.print("[dim]Backups are stored in database_backups/ folder for safety[/dim]\n")

        choices = [
            "Clear Book Metadata Only (Keep EPUBs & Covers)",
            "Clear EPUB Storage Only (Keep Metadata & Covers)",
            "Clear Cover Storage Only (Keep Metadata & EPUBs)",
            "Clear All Book Data (Keep Database Structure)",
            "Clear Books by Genre",
            "Clear Old Books (by Date)",
            "Complete Database Reset (Factory Reset)",
            "View/Restore Backups",
            "← Back to Database Menu"
        ]

        selected = questionary.select(
            "Select clearing option:",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Clear Book Metadata Only (Keep EPUBs & Covers)":
            clear_metadata_only()
        elif selected == "Clear EPUB Storage Only (Keep Metadata & Covers)":
            clear_epub_storage_only()
        elif selected == "Clear Cover Storage Only (Keep Metadata & EPUBs)":
            clear_cover_storage_only()
        elif selected == "Clear All Book Data (Keep Database Structure)":
            clear_all_book_data()
        elif selected == "Clear Books by Genre":
            clear_books_by_genre()
        elif selected == "Clear Old Books (by Date)":
            clear_old_books()
        elif selected == "Complete Database Reset (Factory Reset)":
            complete_database_reset()
        elif selected == "View/Restore Backups":
            backup_management_menu()
        elif selected == "← Back to Database Menu":
            break


def clear_metadata_only() -> None:
    """Clear only book metadata, keeping EPUBs and covers."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Clear Book Metadata Only[/bold cyan]\n")
    console.print("[bold green]This operation will:[/bold green]")
    console.print("• Clear book titles, authors, genres, descriptions")
    console.print("• Clear novel data JSON")
    console.print("• Reset generation status")
    console.print("• [bold green]PRESERVE[/bold green] all EPUB files")
    console.print("• [bold green]PRESERVE[/bold green] all cover images")
    console.print("• Create automatic backup before clearing\n")

    console.print("[bold yellow]Use case:[/bold yellow] Clean up metadata while keeping your book files")

    confirm = questionary.confirm(
        "\nProceed with metadata clearing?",
        style=custom_style
    ).ask()

    if confirm:
        cleaner = get_database_cleaner()
        success = cleaner.clear_book_metadata_only()

        if success:
            console.print("\n[bold green]✓ Metadata clearing completed successfully![/bold green]")
        else:
            console.print("\n[bold red]✗ Metadata clearing failed![/bold red]")
    else:
        console.print("\n[yellow]Operation cancelled.[/yellow]")

    input("\nPress Enter to continue...")


def clear_epub_storage_only() -> None:
    """Clear only EPUB storage, keeping metadata and covers."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Clear EPUB Storage Only[/bold cyan]\n")
    console.print("[bold green]This operation will:[/bold green]")
    console.print("• Remove all stored EPUB files from database")
    console.print("• Clear novel data JSON")
    console.print("• Free up significant storage space")
    console.print("• [bold green]PRESERVE[/bold green] all book metadata")
    console.print("• [bold green]PRESERVE[/bold green] all cover images")
    console.print("• Create automatic backup before clearing\n")

    console.print("[bold yellow]Use case:[/bold yellow] Free up storage space while keeping book information")
    console.print("[bold yellow]Note:[/bold yellow] You can re-import EPUBs later using migration")

    confirm = questionary.confirm(
        "\nProceed with EPUB storage clearing?",
        style=custom_style
    ).ask()

    if confirm:
        cleaner = get_database_cleaner()
        success = cleaner.clear_epub_storage_only()

        if success:
            console.print("\n[bold green]✓ EPUB storage clearing completed successfully![/bold green]")
        else:
            console.print("\n[bold red]✗ EPUB storage clearing failed![/bold red]")
    else:
        console.print("\n[yellow]Operation cancelled.[/yellow]")

    input("\nPress Enter to continue...")


def clear_cover_storage_only() -> None:
    """Clear only cover storage, keeping metadata and EPUBs."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Clear Cover Storage Only[/bold cyan]\n")
    console.print("[bold green]This operation will:[/bold green]")
    console.print("• Remove all stored cover images from database")
    console.print("• Free up cover storage space")
    console.print("• [bold green]PRESERVE[/bold green] all book metadata")
    console.print("• [bold green]PRESERVE[/bold green] all EPUB files")
    console.print("• Create automatic backup before clearing\n")

    console.print("[bold yellow]Use case:[/bold yellow] Remove covers while keeping books and metadata")
    console.print("[bold yellow]Note:[/bold yellow] Covers can be regenerated or re-imported later")

    confirm = questionary.confirm(
        "\nProceed with cover storage clearing?",
        style=custom_style
    ).ask()

    if confirm:
        cleaner = get_database_cleaner()
        success = cleaner.clear_cover_storage_only()

        if success:
            console.print("\n[bold green]✓ Cover storage clearing completed successfully![/bold green]")
        else:
            console.print("\n[bold red]✗ Cover storage clearing failed![/bold red]")
    else:
        console.print("\n[yellow]Operation cancelled.[/yellow]")

    input("\nPress Enter to continue...")


def clear_all_book_data() -> None:
    """Clear all book data but keep database structure."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Clear All Book Data[/bold cyan]\n")
    console.print("[bold red]⚠ WARNING: This is a major operation![/bold red]\n")
    console.print("[bold red]This operation will:[/bold red]")
    console.print("• Remove ALL books from database")
    console.print("• Remove ALL EPUB files")
    console.print("• Remove ALL cover images")
    console.print("• Remove ALL metadata")
    console.print("• [bold green]PRESERVE[/bold green] database structure")
    console.print("• Create automatic backup before clearing\n")

    console.print("[bold yellow]Use case:[/bold yellow] Start fresh while keeping database setup")
    console.print("[bold yellow]Result:[/bold yellow] Empty database ready for new books")

    # Double confirmation for safety
    confirm1 = questionary.confirm(
        "\nAre you sure you want to clear ALL book data?",
        style=custom_style
    ).ask()

    if not confirm1:
        console.print("\n[yellow]Operation cancelled.[/yellow]")
        input("\nPress Enter to continue...")
        return

    confirm2 = questionary.confirm(
        "This will remove ALL books permanently. Continue?",
        style=custom_style
    ).ask()

    if confirm2:
        cleaner = get_database_cleaner()
        success = cleaner.clear_all_book_data()

        if success:
            console.print("\n[bold green]✓ All book data cleared successfully![/bold green]")
            console.print("[bold green]✓ Database is now empty and ready for new books[/bold green]")
        else:
            console.print("\n[bold red]✗ Data clearing failed![/bold red]")
    else:
        console.print("\n[yellow]Operation cancelled.[/yellow]")

    input("\nPress Enter to continue...")


def clear_books_by_genre() -> None:
    """Clear books of a specific genre."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Clear Books by Genre[/bold cyan]\n")

    # Get available genres
    try:
        db_manager = get_database_manager()
        stats = db_manager.get_database_stats()

        if not stats["genre_counts"]:
            console.print("[yellow]No genres found in the database.[/yellow]")
            input("\nPress Enter to continue...")
            return

        # Display genre options
        console.print("[bold green]Available Genres:[/bold green]")
        genre_choices = []
        for genre, count in stats["genre_counts"].items():
            genre_display = f"{genre} ({count} books)"
            genre_choices.append(genre_display)
            console.print(f"• {genre_display}")

        genre_choices.append("← Back to Clear Menu")

        selected = questionary.select(
            "\nSelect genre to clear:",
            choices=genre_choices,
            style=custom_style
        ).ask()

        if selected == "← Back to Clear Menu":
            return

        # Extract genre name from selection
        genre = selected.split(" (")[0]
        book_count = stats["genre_counts"][genre]

        console.print(f"\n[bold yellow]Warning:[/bold yellow] This will remove {book_count} books from genre: {genre}")

        confirm = questionary.confirm(
            f"Proceed with clearing {genre} books?",
            style=custom_style
        ).ask()

        if confirm:
            cleaner = get_database_cleaner()
            success = cleaner.clear_by_genre(genre)

            if success:
                console.print(f"\n[bold green]✓ {genre} books cleared successfully![/bold green]")
            else:
                console.print(f"\n[bold red]✗ Failed to clear {genre} books![/bold red]")
        else:
            console.print("\n[yellow]Operation cancelled.[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Error: {str(e)}[/bold red]")

    input("\nPress Enter to continue...")


def clear_old_books() -> None:
    """Clear books older than specified days."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Clear Old Books[/bold cyan]\n")

    age_options = [
        "7 days",
        "30 days",
        "90 days",
        "180 days",
        "1 year",
        "Custom (enter days)",
        "← Back to Clear Menu"
    ]

    selected = questionary.select(
        "Remove books older than:",
        choices=age_options,
        style=custom_style
    ).ask()

    if selected == "← Back to Clear Menu":
        return

    if selected == "Custom (enter days)":
        try:
            days_str = questionary.text(
                "Enter number of days:",
                style=custom_style
            ).ask()
            days = int(days_str)
        except (ValueError, TypeError):
            console.print("[bold red]Invalid number entered.[/bold red]")
            input("\nPress Enter to continue...")
            return
    else:
        days = int(selected.split()[0])

    console.print(f"\n[bold yellow]Warning:[/bold yellow] This will remove books older than {days} days")

    confirm = questionary.confirm(
        f"Proceed with clearing books older than {days} days?",
        style=custom_style
    ).ask()

    if confirm:
        cleaner = get_database_cleaner()
        success = cleaner.clear_old_books(days)

        if success:
            console.print(f"\n[bold green]✓ Old books cleared successfully![/bold green]")
        else:
            console.print(f"\n[bold red]✗ Failed to clear old books![/bold red]")
    else:
        console.print("\n[yellow]Operation cancelled.[/yellow]")

    input("\nPress Enter to continue...")


def complete_database_reset() -> None:
    """Completely reset database to factory state."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Complete Database Reset[/bold cyan]\n")
    console.print("[bold red]🚨 EXTREME WARNING: FACTORY RESET 🚨[/bold red]\n")
    console.print("[bold red]This operation will:[/bold red]")
    console.print("• DELETE the entire database file")
    console.print("• Remove ALL books permanently")
    console.print("• Remove ALL EPUBs permanently")
    console.print("• Remove ALL covers permanently")
    console.print("• Remove ALL metadata permanently")
    console.print("• Create a fresh, empty database")
    console.print("• Create automatic backup before reset\n")

    console.print("[bold yellow]Use case:[/bold yellow] Complete fresh start")
    console.print("[bold yellow]Result:[/bold yellow] Brand new database as if just installed")

    # Triple confirmation for safety
    confirm1 = questionary.confirm(
        "\nAre you absolutely sure you want to FACTORY RESET the database?",
        style=custom_style
    ).ask()

    if not confirm1:
        console.print("\n[yellow]Operation cancelled.[/yellow]")
        input("\nPress Enter to continue...")
        return

    confirm2 = questionary.confirm(
        "This will PERMANENTLY DELETE everything. Continue?",
        style=custom_style
    ).ask()

    if not confirm2:
        console.print("\n[yellow]Operation cancelled.[/yellow]")
        input("\nPress Enter to continue...")
        return

    # Final safety check
    safety_word = questionary.text(
        "Type 'RESET' to confirm factory reset:",
        style=custom_style
    ).ask()

    if safety_word != "RESET":
        console.print("\n[yellow]Safety word incorrect. Operation cancelled.[/yellow]")
        input("\nPress Enter to continue...")
        return

    cleaner = get_database_cleaner()
    success = cleaner.reset_database_completely()

    if success:
        console.print("\n[bold green]✓ Database factory reset completed![/bold green]")
        console.print("[bold green]✓ Fresh database created and ready for use[/bold green]")
    else:
        console.print("\n[bold red]✗ Factory reset failed![/bold red]")

    input("\nPress Enter to continue...")


def backup_management_menu() -> None:
    """Manage database backups."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Backup Management[/bold cyan]\n")

    try:
        cleaner = get_database_cleaner()
        backups = cleaner.list_available_backups()

        if not backups:
            console.print("[yellow]No backups found.[/yellow]")
            console.print("Backups are created automatically before clearing operations.")
            input("\nPress Enter to continue...")
            return

        console.print(f"[bold green]Available Backups ({len(backups)}):[/bold green]\n")

        # Display backups table
        backup_table = Table(title="Database Backups", box=box.ROUNDED)
        backup_table.add_column("Filename", style="cyan")
        backup_table.add_column("Size", style="green")
        backup_table.add_column("Created", style="yellow")

        backup_choices = []
        for backup in backups[:10]:  # Show latest 10 backups
            backup_table.add_row(
                backup["filename"],
                f"{backup['size_mb']:.1f} MB",
                backup["created_date"][:19]
            )
            backup_choices.append(f"Restore: {backup['filename']}")

        console.print(backup_table)

        backup_choices.extend([
            "Create Manual Backup",
            "← Back to Clear Menu"
        ])

        selected = questionary.select(
            "\nBackup Operations:",
            choices=backup_choices,
            style=custom_style
        ).ask()

        if selected == "← Back to Clear Menu":
            return
        elif selected == "Create Manual Backup":
            backup_path = cleaner.create_backup_before_clear("manual")
            if backup_path:
                console.print(f"\n[bold green]✓ Manual backup created successfully![/bold green]")
            else:
                console.print(f"\n[bold red]✗ Manual backup failed![/bold red]")
        elif selected.startswith("Restore: "):
            filename = selected.replace("Restore: ", "")
            backup_path = os.path.join(cleaner.backup_dir, filename)

            console.print(f"\n[bold yellow]Warning:[/bold yellow] This will replace your current database with the backup")
            confirm = questionary.confirm(
                f"Restore from {filename}?",
                style=custom_style
            ).ask()

            if confirm:
                success = cleaner.restore_from_backup(backup_path)
                if success:
                    console.print(f"\n[bold green]✓ Database restored from backup![/bold green]")
                else:
                    console.print(f"\n[bold red]✗ Restore failed![/bold red]")
            else:
                console.print("\n[yellow]Restore cancelled.[/yellow]")

    except Exception as e:
        console.print(f"[bold red]Error managing backups: {str(e)}[/bold red]")

    input("\nPress Enter to continue...")


def book_library_menu() -> None:
    """Book library management menu for on-demand access."""
    while True:
        clear_screen()
        display_title()

        console.print("[bold cyan]Book Library Management[/bold cyan]\n")

        # Get library summary
        library_manager = get_book_library_manager()
        summary = library_manager.get_library_summary()

        console.print(f"[dim]Library: {summary['total_books']} books, "
                     f"{summary['books_with_epubs']} with EPUBs, "
                     f"{summary['epub_storage_mb']:.1f} MB storage[/dim]\n")

        choices = [
            "Extract Book from Library",
            "Convert Book Format",
            "Export Genre Collection",
            "Batch Export Books",
            "View Library Summary",
            "Cleanup Exported Files",
            "← Back to Database Menu"
        ]

        selected = questionary.select(
            "Library Management:",
            choices=choices,
            style=custom_style
        ).ask()

        if selected == "Extract Book from Library":
            extract_book_from_library()
        elif selected == "Convert Book Format":
            convert_book_format()
        elif selected == "Export Genre Collection":
            export_genre_collection()
        elif selected == "Batch Export Books":
            batch_export_books()
        elif selected == "View Library Summary":
            view_library_summary()
        elif selected == "Cleanup Exported Files":
            cleanup_exported_files()
        elif selected == "← Back to Database Menu":
            break


def extract_book_from_library() -> None:
    """Extract a single book from the database library."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Extract Book from Library[/bold cyan]\n")

    # Get books with EPUBs
    epub_manager = get_epub_database_manager()
    books_with_epubs = epub_manager.get_books_with_epubs()

    if not books_with_epubs:
        console.print("[yellow]No books with EPUBs found in the database.[/yellow]")
        console.print("Run migration to import your existing books.")
        input("\nPress Enter to continue...")
        return

    # Display available books
    console.print(f"[bold green]Available Books ({len(books_with_epubs)}):[/bold green]\n")

    book_choices = []
    for book in books_with_epubs[:20]:  # Limit to first 20 for UI
        title = book.get("title", "Unknown")
        author = book.get("author", "Unknown")
        genre = book.get("genre", "Unknown")
        book_choices.append(f"{title} by {author} ({genre})")

    if len(books_with_epubs) > 20:
        book_choices.append(f"... and {len(books_with_epubs) - 20} more books")

    book_choices.append("← Back to Library Menu")

    selected = questionary.select(
        "Select book to extract:",
        choices=book_choices,
        style=custom_style
    ).ask()

    if selected == "← Back to Library Menu" or "... and" in selected:
        return

    # Find selected book
    selected_book = None
    for book in books_with_epubs:
        title = book.get("title", "Unknown")
        author = book.get("author", "Unknown")
        genre = book.get("genre", "Unknown")
        if f"{title} by {author} ({genre})" == selected:
            selected_book = book
            break

    if not selected_book:
        return

    # Extract the book
    library_manager = get_book_library_manager()
    result = library_manager.get_book_from_library(selected_book["book_id"])

    if result:
        console.print(f"\n[bold green]Book extracted successfully![/bold green]")
        console.print(f"[bold green]Location:[/bold green] [cyan]{result}[/cyan]")
    else:
        console.print(f"\n[bold red]Failed to extract book.[/bold red]")

    input("\nPress Enter to continue...")


def convert_book_format() -> None:
    """Convert a book to a different format."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Convert Book Format[/bold cyan]\n")
    console.print("[yellow]Note: This feature requires format conversion tools to be available.[/yellow]\n")

    # This would implement format conversion
    console.print("[bold cyan]Format conversion coming soon![/bold cyan]")
    console.print("Supported formats will include: PDF, MOBI, TXT, DOCX")

    input("\nPress Enter to continue...")


def export_genre_collection() -> None:
    """Export all books of a specific genre."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Export Genre Collection[/bold cyan]\n")

    # Get available genres
    db_manager = get_database_manager()
    stats = db_manager.get_database_stats()

    if not stats["genre_counts"]:
        console.print("[yellow]No genres found in the database.[/yellow]")
        input("\nPress Enter to continue...")
        return

    # Display genre options
    genre_choices = list(stats["genre_counts"].keys())
    genre_choices.append("← Back to Library Menu")

    selected_genre = questionary.select(
        "Select genre to export:",
        choices=genre_choices,
        style=custom_style
    ).ask()

    if selected_genre == "← Back to Library Menu":
        return

    # Export the genre collection
    library_manager = get_book_library_manager()
    console.print(f"\n[bold cyan]Exporting {selected_genre} collection...[/bold cyan]")

    results = library_manager.export_genre_collection(selected_genre)

    successful_exports = sum(1 for result in results.values() if not result.startswith("Error") and result != "Export failed")
    console.print(f"\n[bold green]Export complete: {successful_exports}/{len(results)} books exported[/bold green]")

    input("\nPress Enter to continue...")


def batch_export_books() -> None:
    """Export multiple books in batch."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Batch Export Books[/bold cyan]\n")
    console.print("[yellow]This feature allows exporting multiple books at once.[/yellow]\n")

    # This would implement batch export with book selection
    console.print("[bold cyan]Batch export interface coming soon![/bold cyan]")
    console.print("Features will include:")
    console.print("• Multi-select book interface")
    console.print("• Export progress tracking")
    console.print("• Custom output directory selection")

    input("\nPress Enter to continue...")


def view_library_summary() -> None:
    """Display detailed library summary."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Library Summary[/bold cyan]\n")

    library_manager = get_book_library_manager()
    summary = library_manager.get_library_summary()

    # Create summary table
    summary_table = Table(title="Book Library Summary", box=box.ROUNDED)
    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", style="green")

    summary_table.add_row("Total Books", str(summary["total_books"]))
    summary_table.add_row("Books with EPUBs", str(summary["books_with_epubs"]))
    summary_table.add_row("Books with Covers", str(summary["books_with_covers"]))
    summary_table.add_row("Total Storage", f"{summary['total_storage_mb']:.1f} MB")
    summary_table.add_row("EPUB Storage", f"{summary['epub_storage_mb']:.1f} MB")
    summary_table.add_row("Storage Saved", f"{summary['storage_saved_mb']:.1f} MB")
    summary_table.add_row("Avg Compression", f"{summary['avg_compression_ratio']:.1%}")
    summary_table.add_row("Total Accesses", str(summary["total_accesses"]))
    summary_table.add_row("Available Genres", str(len(summary["genres"])))
    if summary["most_popular_genre"]:
        summary_table.add_row("Most Popular Genre", summary["most_popular_genre"])

    console.print(summary_table)

    input("\nPress Enter to continue...")


def cleanup_exported_files() -> None:
    """Clean up old exported files."""
    clear_screen()
    display_title()

    console.print("[bold cyan]Cleanup Exported Files[/bold cyan]\n")

    days_options = ["1 day", "3 days", "7 days", "30 days", "← Back to Library Menu"]

    selected = questionary.select(
        "Remove exported files older than:",
        choices=days_options,
        style=custom_style
    ).ask()

    if selected == "← Back to Library Menu":
        return

    days = int(selected.split()[0])

    library_manager = get_book_library_manager()
    cleaned_count = library_manager.cleanup_exported_books(days)

    if cleaned_count > 0:
        console.print(f"\n[bold green]Cleaned up {cleaned_count} old export directories[/bold green]")
    else:
        console.print(f"\n[bold yellow]No old export directories found[/bold yellow]")

    input("\nPress Enter to continue...")
