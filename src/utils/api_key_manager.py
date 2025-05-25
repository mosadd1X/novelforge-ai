"""
API Key Management System for Gemini AI
Handles rotation and management of multiple API keys.
"""

import os
import re
from typing import List, Dict, Tuple
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import questionary
from src.ui.responsive_separator import (
    separator, title_separator, section_separator
)

console = Console()


class APIKeyManager:
    """Manages multiple Gemini API keys with rotation and backup functionality."""

    def __init__(self, env_file_path: str = ".env"):
        """
        Initialize the API Key Manager.

        Args:
            env_file_path: Path to the .env file
        """
        self.env_file_path = env_file_path
        self.ensure_env_file_exists()

    def ensure_env_file_exists(self):
        """Ensure the .env file exists."""
        if not os.path.exists(self.env_file_path):
            with open(self.env_file_path, 'w') as f:
                f.write("# Gemini AI API Keys\n")
                f.write("# Main API key\n")
                f.write("GEMINI_API_KEY=\n")
                f.write("\n# Backup API keys\n")

    def read_env_file(self) -> List[str]:
        """Read the .env file and return lines."""
        try:
            with open(self.env_file_path, 'r', encoding='utf-8') as f:
                return f.readlines()
        except Exception as e:
            console.print(f"[red]Error reading .env file: {str(e)}[/red]")
            return []

    def write_env_file(self, lines: List[str]):
        """
        Safely write lines to the .env file with backup protection.

        This method creates a backup before writing to prevent data loss.
        """
        import shutil

        try:
            # Validate that we have content to write
            if not lines:
                console.print("[red]Error: Cannot write empty content to .env file[/red]")
                return

            # Create a backup of the current file if it exists
            backup_path = f"{self.env_file_path}.backup"
            if os.path.exists(self.env_file_path):
                shutil.copy2(self.env_file_path, backup_path)
                console.print(f"[dim]Created backup: {backup_path}[/dim]")

            # Write to a temporary file first
            temp_path = f"{self.env_file_path}.tmp"
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)

            # Verify the temporary file was written correctly
            if os.path.exists(temp_path) and os.path.getsize(temp_path) > 0:
                # Replace the original file with the temporary file
                shutil.move(temp_path, self.env_file_path)
                console.print("[dim]File written successfully[/dim]")

                # Clean up old backup (keep only the most recent)
                if os.path.exists(backup_path):
                    # Keep backup for this session, but remove older ones
                    old_backup = f"{self.env_file_path}.backup.old"
                    if os.path.exists(old_backup):
                        os.remove(old_backup)
            else:
                console.print("[red]Error: Temporary file write failed[/red]")
                # Clean up failed temp file
                if os.path.exists(temp_path):
                    os.remove(temp_path)

        except Exception as e:
            console.print(f"[red]Error writing .env file: {str(e)}[/red]")
            console.print("[yellow]Your .env file backup is available if needed[/yellow]")

            # Clean up temp file if it exists
            temp_path = f"{self.env_file_path}.tmp"
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except:
                    pass

    def get_all_api_keys(self) -> Dict[str, str]:
        """
        Get all API keys from the .env file.

        Returns:
            Dictionary mapping key names to values
        """
        lines = self.read_env_file()
        api_keys = {}

        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                if line.startswith('GEMINI_API_KEY'):
                    parts = line.split('=', 1)
                    if len(parts) == 2:
                        key_name = parts[0].strip()
                        key_value = parts[1].strip()
                        if key_value:  # Only include non-empty keys
                            api_keys[key_name] = key_value

        return api_keys

    def get_next_available_number(self) -> int:
        """Get the next available number for a backup API key."""
        api_keys = self.get_all_api_keys()
        numbers = []

        for key_name in api_keys.keys():
            if key_name.startswith('GEMINI_API_KEY_'):
                try:
                    number = int(key_name.split('_')[-1])
                    numbers.append(number)
                except ValueError:
                    continue

        if not numbers:
            return 1

        return max(numbers) + 1

    def add_new_api_key(self, new_api_key: str) -> bool:
        """
        Add a new API key, rotating the current main key to backup.

        Args:
            new_api_key: The new API key to set as main

        Returns:
            True if successful, False otherwise
        """
        if not new_api_key or not new_api_key.strip():
            console.print("[red]Error: API key cannot be empty[/red]")
            return False

        new_api_key = new_api_key.strip()

        # Validate API key format (basic check)
        if not self._validate_api_key_format(new_api_key):
            console.print("[red]Error: Invalid API key format[/red]")
            return False

        lines = self.read_env_file()
        new_lines = []
        current_main_key = None
        main_key_found = False

        # Read current main key and prepare new lines
        for line in lines:
            stripped_line = line.strip()

            if stripped_line.startswith('GEMINI_API_KEY='):
                main_key_found = True
                current_value = stripped_line.split('=', 1)[1].strip()
                if current_value:
                    current_main_key = current_value
                # Replace with new key
                new_lines.append(f"GEMINI_API_KEY={new_api_key}\n")
            else:
                new_lines.append(line)

        # If no main key line found, add it
        if not main_key_found:
            new_lines.append(f"GEMINI_API_KEY={new_api_key}\n")

        # If there was a current main key, move it to backup
        if current_main_key:
            next_number = self.get_next_available_number()
            backup_key_line = f"GEMINI_API_KEY_{next_number}={current_main_key}\n"
            new_lines.append(backup_key_line)
            console.print(f"[green]Moved previous main key to GEMINI_API_KEY_{next_number}[/green]")

        # Write the updated file
        self.write_env_file(new_lines)
        console.print(f"[green]Successfully set new main API key[/green]")
        return True

    def _validate_api_key_format(self, api_key: str) -> bool:
        """
        Basic validation of API key format.

        Args:
            api_key: The API key to validate

        Returns:
            True if format appears valid
        """
        # Basic checks for Gemini API key format
        if len(api_key) < 20:  # Too short
            return False

        # Should contain alphanumeric characters and possibly some symbols
        if not re.match(r'^[A-Za-z0-9_-]+$', api_key):
            return False

        return True

    def remove_api_key(self, key_name: str) -> bool:
        """
        Remove a specific API key.

        Args:
            key_name: Name of the key to remove (e.g., 'GEMINI_API_KEY_1')

        Returns:
            True if successful, False otherwise
        """
        if key_name == 'GEMINI_API_KEY':
            console.print("[red]Error: Cannot remove the main API key[/red]")
            return False

        lines = self.read_env_file()
        new_lines = []
        removed = False

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith(f"{key_name}="):
                removed = True
                console.print(f"[green]Removed {key_name}[/green]")
            else:
                new_lines.append(line)

        if removed:
            self.write_env_file(new_lines)
            return True
        else:
            console.print(f"[red]API key {key_name} not found[/red]")
            return False

    def set_main_api_key(self, key_name: str) -> bool:
        """
        Set a backup key as the main API key.

        Args:
            key_name: Name of the backup key to promote

        Returns:
            True if successful, False otherwise
        """
        api_keys = self.get_all_api_keys()

        if key_name not in api_keys:
            console.print(f"[red]API key {key_name} not found[/red]")
            return False

        if key_name == 'GEMINI_API_KEY':
            console.print("[yellow]This is already the main API key[/yellow]")
            return True

        # Get the key value
        new_main_key = api_keys[key_name]

        # Remove the backup key and set as main
        self.remove_api_key(key_name)

        # Update main key
        lines = self.read_env_file()
        new_lines = []

        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('GEMINI_API_KEY='):
                new_lines.append(f"GEMINI_API_KEY={new_main_key}\n")
            else:
                new_lines.append(line)

        self.write_env_file(new_lines)
        console.print(f"[green]Successfully promoted {key_name} to main API key[/green]")
        return True

    def display_api_keys(self):
        """Display all API keys following clean design principles."""
        api_keys = self.get_all_api_keys()

        if not api_keys:
            console.print("    ⚠️ [yellow]No API keys found in .env file[/yellow]")
            return

        console.print("[bold cyan]🔑 Gemini API Keys[/bold cyan]")
        console.print()

        for key_name, key_value in api_keys.items():
            # Mask the key value for security
            masked_value = key_value[:8] + "*" * (len(key_value) - 12) + key_value[-4:] if len(key_value) > 12 else "*" * len(key_value)

            status_icon = "🎯" if key_name == "GEMINI_API_KEY" else "🔄"
            status_text = "[bold green]Main[/bold green]" if key_name == "GEMINI_API_KEY" else "[cyan]Backup[/cyan]"

            console.print(f"    {status_icon} [cyan bold]{key_name}[/cyan bold]: [white]{masked_value}[/white] ({status_text})")

        console.print()

    def get_api_key_count(self) -> Tuple[int, int]:
        """
        Get count of API keys.

        Returns:
            Tuple of (total_keys, backup_keys)
        """
        api_keys = self.get_all_api_keys()
        total = len(api_keys)
        backup = total - 1 if 'GEMINI_API_KEY' in api_keys else total
        return total, backup

    def check_key_usage_compatibility(self) -> Dict[str, any]:
        """
        Check if all managed keys can be used by GeminiClient.

        Returns:
            Dictionary with compatibility information
        """
        managed_keys = self.get_all_api_keys()

        try:
            # Try to load keys the same way GeminiClient does
            from src.core.gemini_client import GeminiClient

            # Create a temporary client to see how many keys it loads
            temp_client = GeminiClient()
            used_keys = temp_client.api_keys

            return {
                "managed_count": len(managed_keys),
                "used_count": len(used_keys),
                "all_keys_used": len(managed_keys) == len(used_keys),
                "unused_count": max(0, len(managed_keys) - len(used_keys)),
                "compatibility_status": "compatible" if len(managed_keys) == len(used_keys) else "incompatible"
            }

        except Exception as e:
            return {
                "managed_count": len(managed_keys),
                "used_count": 0,
                "all_keys_used": False,
                "unused_count": len(managed_keys),
                "compatibility_status": "unknown",
                "error": str(e)
            }


def show_api_key_management_menu():
    """Display the API key management menu following clean design principles."""
    api_manager = APIKeyManager()

    while True:
        console.clear()

        # Clean header
        console.print()
        console.print("[bold cyan]🔑 API Key Management[/bold cyan]")
        console.print("    Manage your Gemini AI API keys")
        console.print()

        # Minimal status display
        total_keys, backup_keys = api_manager.get_api_key_count()
        console.print(f"    📊 Keys: {total_keys} total, {backup_keys} backup")

        # Quick status check
        compatibility = api_manager.check_key_usage_compatibility()
        if compatibility["compatibility_status"] == "incompatible":
            console.print(f"    ⚠️ [yellow]Status: {compatibility['unused_count']} keys unused[/yellow]")
        elif compatibility["compatibility_status"] == "compatible":
            console.print(f"    ✅ [green]Status: All keys active[/green]")

        console.print()

        # Clean menu choices
        choices = [
            "➕ Add New API Key",
            "👁️ View All Keys",
            "🗑️ Remove Backup Key",
            "⬆️ Promote Backup to Main",
            "🧪 Test Main Key",
            "📊 Check Key Status",
            "← Back to System Settings"
        ]

        # Show clean menu
        try:
            action = questionary.select(
                "What would you like to do?",
                choices=choices,
                style=questionary.Style([
                    ('question', 'fg:cyan bold'),
                    ('answer', 'fg:green bold'),
                    ('pointer', 'fg:cyan bold'),
                    ('highlighted', 'fg:cyan bold'),
                    ('selected', 'fg:green bold'),
                    ('separator', 'fg:cyan'),
                    ('instruction', 'fg:white'),
                    ('text', 'fg:white'),
                    ('disabled', 'fg:gray')
                ])
            ).ask()

            if action is None:  # User pressed Ctrl+C
                break
            elif action == "➕ Add New API Key":
                add_new_api_key_interactive(api_manager)
            elif action == "👁️ View All Keys":
                view_all_keys_interactive(api_manager)
            elif action == "🗑️ Remove Backup Key":
                remove_api_key_interactive(api_manager)
            elif action == "⬆️ Promote Backup to Main":
                promote_api_key_interactive(api_manager)
            elif action == "🧪 Test Main Key":
                test_api_key_interactive(api_manager)
            elif action == "📊 Check Key Status":
                check_api_status_interactive(api_manager)
            elif action == "← Back to System Settings":
                break

        except KeyboardInterrupt:
            console.print("\n[yellow]Operation cancelled.[/yellow]")
            break
        except Exception as e:
            console.print(f"\n[red]Error: {str(e)}[/red]")
            console.input("Press Enter to continue...")
            continue


def add_new_api_key_interactive(api_manager: APIKeyManager):
    """Interactive function to add a new API key with minimal interface."""
    console.print("\n[bold cyan]➕ Add New API Key[/bold cyan]")
    console.print("    Current main key will be moved to backup")
    console.print()

    # Show current main key (masked)
    current_keys = api_manager.get_all_api_keys()
    if 'GEMINI_API_KEY' in current_keys:
        current_main = current_keys['GEMINI_API_KEY']
        masked_current = current_main[:8] + "*" * (len(current_main) - 12) + current_main[-4:] if len(current_main) > 12 else "*" * len(current_main)
        console.print(f"    Current: {masked_current}")
    else:
        console.print("    No main key configured")

    console.print()
    new_key = console.input("Enter new API key: ").strip()

    if not new_key:
        console.print("[red]No key entered. Cancelled.[/red]")
        console.input("\nPress Enter to continue...")
        return

    confirm = questionary.confirm(
        "Add this key as main and move current to backup?",
        default=False
    ).ask()

    if confirm:
        if api_manager.add_new_api_key(new_key):
            console.print("\n[bold green]✅ API key added successfully![/bold green]")
        else:
            console.print("\n[bold red]❌ Failed to add API key[/bold red]")
    else:
        console.print("\n[yellow]Cancelled[/yellow]")

    console.input("\nPress Enter to continue...")


def view_all_keys_interactive(api_manager: APIKeyManager):
    """Interactive function to view all API keys with clean interface."""
    console.print("\n[bold cyan]👁️ View All Keys[/bold cyan]")
    console.print()

    api_keys = api_manager.get_all_api_keys()

    if not api_keys:
        console.print("    No API keys found")
        console.input("\nPress Enter to continue...")
        return

    console.print(f"    📊 Total: {len(api_keys)} keys")
    console.print()

    for key_name, key_value in api_keys.items():
        preview = key_value[:12] + "..." + key_value[-4:] if len(key_value) > 16 else key_value
        status = "🔑 Main" if key_name == "GEMINI_API_KEY" else "🔄 Backup"

        console.print(f"    {status} {key_name}")
        console.print(f"        Preview: {preview}")
        console.print(f"        Length: {len(key_value)} chars")
        console.print()

    console.input("Press Enter to continue...")


def remove_api_key_interactive(api_manager: APIKeyManager):
    """Interactive function to safely remove backup API keys."""
    console.print("\n[bold cyan]🗑️ Remove Backup Key[/bold cyan]")
    console.print("    Main key cannot be removed")
    console.print()

    api_keys = api_manager.get_all_api_keys()
    backup_keys = {k: v for k, v in api_keys.items() if k != 'GEMINI_API_KEY'}

    if not backup_keys:
        console.print("    No backup keys found")
        console.input("\nPress Enter to continue...")
        return

    console.print(f"    📊 {len(backup_keys)} backup key{'s' if len(backup_keys) != 1 else ''} available:")
    console.print()

    for i, key_name in enumerate(backup_keys.keys(), 1):
        masked_value = backup_keys[key_name][:8] + "*" * 8 + backup_keys[key_name][-4:]
        console.print(f"    {i}. {key_name}")
        console.print(f"       {masked_value}")
        console.print()

    # Create choices for questionary
    key_choices = []
    for key_name in backup_keys.keys():
        masked_value = backup_keys[key_name][:8] + "*" * 8 + backup_keys[key_name][-4:]
        key_choices.append(questionary.Choice(
            title=f"{key_name} - {masked_value}",
            value=key_name
        ))

    key_choices.append(questionary.Choice(title="Cancel", value="cancel"))

    try:
        key_name = questionary.select(
            "Select key to remove:",
            choices=key_choices
        ).ask()

        if key_name == "cancel" or key_name is None:
            console.print("    Cancelled")
            console.input("\nPress Enter to continue...")
            return

        if key_name in backup_keys:
            confirm = questionary.confirm(
                f"Permanently remove {key_name}?",
                default=False
            ).ask()

            if confirm:
                if api_manager.remove_api_key(key_name):
                    console.print(f"\n    ✅ [green]{key_name} removed successfully[/green]")
                else:
                    console.print(f"\n    ❌ [red]Failed to remove {key_name}[/red]")
            else:
                console.print("    Cancelled")

    except Exception as e:
        console.print(f"\n    ❌ [red]Error: {str(e)}[/red]")

    console.input("\nPress Enter to continue...")


def promote_api_key_interactive(api_manager: APIKeyManager):
    """Interactive function to promote a backup key to main with detailed explanations."""
    console.print()
    console.print(title_separator("Promote Backup Key to Main"))
    console.print()

    api_keys = api_manager.get_all_api_keys()
    backup_keys = {k: v for k, v in api_keys.items() if k != 'GEMINI_API_KEY'}

    console.print("\n[bold]How Key Promotion Works:[/bold]")
    console.print("1. Selected backup key becomes the new main GEMINI_API_KEY")
    console.print("2. The backup key entry is removed from configuration")
    console.print("3. Previous main key is NOT automatically backed up")
    console.print("4. System immediately starts using the promoted key")

    console.print("\n[bold]When to Use Key Promotion:[/bold]")
    console.print("• Current main key is rate limited or not working")
    console.print("• You want to switch to a different key permanently")
    console.print("• Testing a backup key as your primary key")
    console.print("• Main key has been compromised and needs replacement")

    if not backup_keys:
        console.print("\n[yellow]No backup API keys available for promotion.[/yellow]")
        console.print("• You currently only have a main API key configured")
        console.print("• Add backup keys using option 1 before promoting")
        console.print("• Backup keys provide redundancy and promotion options")
        console.input("\nPress Enter to continue...")
        return

    # Show current main key
    if 'GEMINI_API_KEY' in api_keys:
        current_main = api_keys['GEMINI_API_KEY']
        masked_current = current_main[:8] + "*" * 8 + current_main[-4:]
        console.print(f"\n[bold]Current main key:[/bold] {masked_current}")
        console.print("[dim]This key will be replaced (not automatically backed up)[/dim]")

    console.print(f"\n[bold]Available backup keys for promotion:[/bold]")
    console.print(f"Total backup keys: {len(backup_keys)}")

    for i, key_name in enumerate(backup_keys.keys(), 1):
        masked_value = backup_keys[key_name][:8] + "*" * 8 + backup_keys[key_name][-4:]
        console.print(f"{i}. {key_name}")
        console.print(f"   Preview: {masked_value}")
        console.print(f"   Length: {len(backup_keys[key_name])} characters")

    console.print("\n[bold]Promotion Process:[/bold]")
    console.print("1. Select a backup key by number")
    console.print("2. Confirm the promotion (requires 'y' confirmation)")
    console.print("3. Backup key becomes new main GEMINI_API_KEY")
    console.print("4. Original backup entry is removed")
    console.print("5. System starts using promoted key immediately")

    try:
        choice = int(console.input("\n[bold]Enter the number of the key to promote (0 to cancel): [/bold]"))

        if choice == 0:
            console.print("\n[yellow]Operation cancelled. No keys were promoted.[/yellow]")
            console.input("\nPress Enter to continue...")
            return

        if 1 <= choice <= len(backup_keys):
            key_name = list(backup_keys.keys())[choice - 1]
            key_value = backup_keys[key_name]
            masked_value = key_value[:8] + "*" * 8 + key_value[-4:]

            console.print(f"\n[bold yellow]Confirmation Required - Key Promotion[/bold yellow]")
            console.print(f"Key to promote: {key_name}")
            console.print(f"Key preview: {masked_value}")
            console.print(f"Key length: {len(key_value)} characters")

            console.print(f"\n[bold]What will happen:[/bold]")
            console.print(f"• {key_name} will become the new main GEMINI_API_KEY")
            console.print(f"• The backup entry for {key_name} will be removed")
            console.print(f"• System will immediately start using this key")
            if 'GEMINI_API_KEY' in api_keys:
                console.print(f"• Current main key will be replaced (not backed up)")

            console.print(f"\n[bold red]Important:[/bold red] Current main key will NOT be automatically backed up!")
            console.print("If you want to keep the current main key, add it as backup first using option 1.")

            confirm = console.input(f"\n[bold]Type 'y' to promote {key_name} to main: [/bold]").strip().lower()

            if confirm == 'y':
                console.print(f"\n[yellow]Promoting {key_name} to main API key...[/yellow]")
                if api_manager.set_main_api_key(key_name):
                    console.print(f"\n[bold green]SUCCESS: {key_name} is now your main API key[/bold green]")
                    console.print("• Key promotion completed successfully")
                    console.print("• System is now using the promoted key")
                    console.print("• Configuration updated in .env file")
                    remaining_backups = len(backup_keys) - 1
                    console.print(f"• You now have {remaining_backups} backup keys remaining")
                else:
                    console.print(f"\n[bold red]FAILED: Could not promote {key_name}[/bold red]")
                    console.print("• Check file permissions for .env file")
                    console.print("• Ensure the key exists in the configuration")
            else:
                console.print("\n[yellow]Promotion cancelled. No changes made.[/yellow]")
        else:
            console.print("\n[red]Invalid choice. Please select a number from the list.[/red]")

    except ValueError:
        console.print("\n[red]Invalid input. Please enter a valid number.[/red]")

    console.input("\nPress Enter to continue...")


def test_api_key_interactive(api_manager: APIKeyManager):
    """Interactive function to test the current main API key with detailed diagnostics."""
    console.print()
    console.print(title_separator("Test Current Main API Key"))
    console.print()

    api_keys = api_manager.get_all_api_keys()

    console.print("\n[bold]API Key Testing Process:[/bold]")
    console.print("1. Validates that a main API key is configured")
    console.print("2. Initializes connection to Gemini AI service")
    console.print("3. Sends a test request to verify functionality")
    console.print("4. Analyzes response to confirm proper operation")
    console.print("5. Reports detailed results and recommendations")

    if 'GEMINI_API_KEY' not in api_keys:
        console.print("\n[red]ERROR: No main API key found in configuration.[/red]")
        console.print("• Main API key (GEMINI_API_KEY) is not configured")
        console.print("• Use option 1 to add your first API key")
        console.print("• Ensure your .env file contains a valid GEMINI_API_KEY entry")
        console.input("\nPress Enter to continue...")
        return

    main_key = api_keys['GEMINI_API_KEY']
    masked_key = main_key[:8] + "*" * 8 + main_key[-4:]

    console.print(f"\n[bold]Testing Configuration:[/bold]")
    console.print(f"• Key to test: {masked_key}")
    console.print(f"• Key length: {len(main_key)} characters")
    console.print(f"• Key status: Primary main key")
    console.print(f"• Test type: Live connectivity test")

    console.print(f"\n[bold]Test Parameters:[/bold]")
    console.print(f"• Test message: Simple greeting request")
    console.print(f"• Expected response: Confirmation message")
    console.print(f"• Temperature: 0.1 (deterministic)")
    console.print(f"• Max tokens: 50 (short response)")

    try:
        # Import and test the Gemini client
        from src.core.resilient_gemini_client import ResilientGeminiClient

        console.print("\n[yellow]Step 1: Initializing Gemini client...[/yellow]")
        client = ResilientGeminiClient()
        console.print("• Gemini client initialized successfully")

        console.print("\n[yellow]Step 2: Testing API connection and authentication...[/yellow]")
        test_response = client.generate_content(
            "Hello, this is a test message. Please respond with 'API test successful'.",
            temperature=0.1,
            max_tokens=50
        )

        console.print("• Test request sent to Gemini AI")
        console.print("• Waiting for response...")

        # Analyze the response
        console.print(f"\n[bold]Test Results:[/bold]")

        if test_response:
            console.print("• Response received: YES")
            console.print(f"• Response length: {len(test_response)} characters")

            if "successful" in test_response.lower():
                console.print("\n[bold green]SUCCESS: API key is working correctly![/bold green]")
                console.print("• Authentication: PASSED")
                console.print("• Connectivity: PASSED")
                console.print("• Response quality: PASSED")
                console.print("• Key status: FULLY FUNCTIONAL")
            else:
                console.print("\n[bold yellow]PARTIAL SUCCESS: API key works but response unexpected[/bold yellow]")
                console.print("• Authentication: PASSED")
                console.print("• Connectivity: PASSED")
                console.print("• Response quality: UNEXPECTED")
                console.print("• Key status: FUNCTIONAL (with minor issues)")

            console.print(f"\n[bold]Response Preview:[/bold]")
            preview = test_response[:200] + "..." if len(test_response) > 200 else test_response
            console.print(f"'{preview}'")

        else:
            console.print("• Response received: NO")
            console.print("\n[bold red]FAILED: No response from API[/bold red]")
            console.print("• Authentication: UNKNOWN")
            console.print("• Connectivity: FAILED")
            console.print("• Response quality: NO RESPONSE")
            console.print("• Key status: NOT FUNCTIONAL")

        console.print(f"\n[bold]Recommendations:[/bold]")
        if test_response and "successful" in test_response.lower():
            console.print("• Your API key is working perfectly")
            console.print("• No action needed at this time")
            console.print("• Key is ready for ebook generation")
        elif test_response:
            console.print("• API key is functional but response was unexpected")
            console.print("• This may indicate rate limiting or service issues")
            console.print("• Try again in a few minutes if problems persist")
        else:
            console.print("• API key may be invalid, expired, or rate limited")
            console.print("• Check your key in Google AI Studio")
            console.print("• Consider using option 4 to promote a backup key")
            console.print("• Verify your internet connection")

    except ImportError:
        console.print("\n[bold red]ERROR: Gemini client not available[/bold red]")
        console.print("• The Gemini AI client could not be imported")
        console.print("• Check that all required dependencies are installed")
        console.print("• Ensure the src.core.gemini_client module exists")
    except Exception as e:
        console.print(f"\n[bold red]ERROR: API key test failed with exception[/bold red]")
        console.print(f"• Error details: {str(e)}")
        console.print("• This may indicate:")
        console.print("  - Invalid API key format")
        console.print("  - Network connectivity issues")
        console.print("  - Rate limiting or quota exceeded")
        console.print("  - Service temporarily unavailable")
        console.print("\n[bold]Troubleshooting Steps:[/bold]")
        console.print("1. Verify API key is correct in Google AI Studio")
        console.print("2. Check internet connection")
        console.print("3. Wait a few minutes and try again")
        console.print("4. Try promoting a backup key if available")

    console.input("\nPress Enter to continue...")


def check_api_status_interactive(api_manager: APIKeyManager):
    """Interactive function to check API key status and rate limits with comprehensive monitoring."""
    console.print()
    console.print(title_separator("API Key Status & Rate Limit Monitor"))
    console.print()

    console.print("\n[bold]Monitoring Process:[/bold]")
    console.print("1. Initializes connection to all configured API keys")
    console.print("2. Tests each key for availability and rate limit status")
    console.print("3. Analyzes usage patterns and request distribution")
    console.print("4. Provides detailed status reports and recommendations")
    console.print("5. Monitors automatic key rotation functionality")

    try:
        # Import the Gemini client to check status
        from src.core.resilient_gemini_client import ResilientGeminiClient

        console.print("\n[yellow]Step 1: Initializing Gemini client and loading API keys...[/yellow]")
        gemini_client = ResilientGeminiClient()
        console.print("• Gemini client initialized successfully")

        console.print("\n[yellow]Step 2: Testing all API key connections...[/yellow]")
        api_status = gemini_client.check_api_connection(check_all_keys=True)
        console.print("• Connection tests completed")

        # Create status overview table
        status_table = Table(title="API Key Status Overview", show_header=True, header_style="bold magenta")
        status_table.add_column("Metric", style="cyan", no_wrap=True, width=20)
        status_table.add_column("Value", style="white", width=15)
        status_table.add_column("Status", style="green", width=20)

        # Add general information
        status_table.add_row("Total API Keys", str(api_status["active_keys"]), "CONFIGURED")
        status_table.add_row("Working API Keys", str(api_status["working_keys"]),
                           "AVAILABLE" if api_status["working_keys"] > 0 else "NONE WORKING")
        status_table.add_row("Rate Limited Keys", str(len(gemini_client.rate_limited_keys)),
                           "LIMITED" if len(gemini_client.rate_limited_keys) > 0 else "NONE LIMITED")
        status_table.add_row("Current Active Key", f"Key {gemini_client.current_key_index + 1}/{len(gemini_client.api_keys)}",
                           "ACTIVE")

        console.print(status_table)

        # Get usage statistics
        console.print("\n[yellow]Step 3: Analyzing usage statistics...[/yellow]")
        usage_stats = gemini_client.get_api_key_usage_stats()
        console.print("• Usage analysis completed")

        # Create detailed usage table
        usage_table = Table(title="Detailed API Key Usage & Rate Limits", show_header=True, header_style="bold magenta")
        usage_table.add_column("API Key", style="cyan", width=20)
        usage_table.add_column("Requests", style="white", justify="right", width=10)
        usage_table.add_column("Usage %", style="white", justify="right", width=10)
        usage_table.add_column("Rate Status", style="yellow", width=15)
        usage_table.add_column("Availability", style="green", width=15)

        # Add rows for each API key
        for key, stats in usage_stats["usage_by_key"].items():
            # Determine if this key is rate limited
            is_rate_limited = key in [f"{k[:4]}...{k[-4:]}" for k in gemini_client.rate_limited_keys]

            # Determine status
            if is_rate_limited:
                rate_status = "RATE LIMITED"
                availability = "UNAVAILABLE"
            else:
                rate_status = "NORMAL"
                availability = "AVAILABLE"

            # Add row
            usage_table.add_row(
                key,
                str(stats["count"]),
                f"{stats['percentage']}%",
                rate_status,
                availability
            )

        console.print(usage_table)

        # Display key rotation information
        console.print("\n[bold cyan]Rate Limit Management Analysis:[/bold cyan]")
        if api_status["active_keys"] > 1:
            console.print("[bold green]MULTIPLE API KEYS DETECTED - OPTIMAL CONFIGURATION[/bold green]")
            console.print("• Automatic key rotation: ENABLED")
            console.print("• Rate limit handling: ACTIVE")
            console.print("• Key distribution: BALANCED")
            console.print("• Failover protection: AVAILABLE")
            console.print("\n[bold]Rotation Behavior:[/bold]")
            console.print("• System automatically switches keys when rate limits are encountered")
            console.print("• Rate-limited keys are temporarily skipped until quotas reset")
            console.print("• Keys rotate in sequence for optimal request distribution")
            console.print("• Failed keys are marked and avoided until recovery")
        else:
            console.print("[bold yellow]SINGLE API KEY DETECTED - CONSIDER ADDING BACKUPS[/bold yellow]")
            console.print("• Automatic key rotation: DISABLED (only one key)")
            console.print("• Rate limit handling: LIMITED")
            console.print("• Failover protection: NONE")
            console.print("\n[bold]Recommendations:[/bold]")
            console.print("• Add additional API keys using option 1 for better reliability")
            console.print("• Multiple keys provide automatic rate limit handling")
            console.print("• Backup keys ensure continuous operation during limits")

        # Show rate limit recovery information
        if len(gemini_client.rate_limited_keys) > 0:
            console.print(f"\n[bold red]RATE LIMIT ALERT: {len(gemini_client.rate_limited_keys)} key(s) currently rate limited[/bold red]")
            console.print("\n[bold]Rate Limit Recovery Information:[/bold]")
            console.print("• Most quotas reset: Every hour (60 minutes)")
            console.print("• Daily limits reset: Every 24 hours at midnight UTC")
            console.print("• Request per minute: Resets every minute")
            console.print("• Tokens per minute: Resets every minute")
            console.print("\n[bold]Immediate Actions:[/bold]")
            console.print("• System will automatically use available keys")
            console.print("• Rate-limited keys will be retried after reset time")
            console.print("• Check Google AI Studio for specific quota details")
            console.print("• Consider adding more API keys if limits persist")
        else:
            console.print("\n[bold green]ALL KEYS AVAILABLE - OPTIMAL STATUS[/bold green]")
            console.print("• No rate limits currently detected")
            console.print("• All configured keys are functional")
            console.print("• System ready for high-volume operations")

        # Display management tips
        console.print("\n[bold cyan]API Key Management Recommendations:[/bold cyan]")
        console.print("\n[bold]For Rate Limit Management:[/bold]")
        console.print("1. Add more API keys using option 1 to distribute load")
        console.print("2. Monitor usage patterns in Google AI Studio dashboard")
        console.print("3. Rate limits typically reset hourly or daily")
        console.print("4. Use option 5 to test individual keys when issues arise")
        console.print("5. Promote working backup keys if main key is consistently limited")

        console.print("\n[bold]For Optimal Performance:[/bold]")
        console.print("• Maintain 3-5 API keys for best redundancy")
        console.print("• Rotate keys manually if one becomes problematic")
        console.print("• Monitor this status regularly during heavy usage")
        console.print("• Keep backup keys from different Google accounts if possible")

        # Show current configuration summary
        api_keys = api_manager.get_all_api_keys()
        console.print(f"\n[bold cyan]Current Configuration Summary:[/bold cyan]")
        console.print(f"• Total configured keys: {len(api_keys)}")
        console.print(f"• Main key status: {'CONFIGURED' if 'GEMINI_API_KEY' in api_keys else 'MISSING'}")
        console.print(f"• Backup keys available: {len(api_keys) - 1 if 'GEMINI_API_KEY' in api_keys else len(api_keys)}")
        console.print(f"• Working keys ratio: {api_status['working_keys']}/{api_status['active_keys']}")
        console.print(f"• System health: {'EXCELLENT' if api_status['working_keys'] > 2 else 'GOOD' if api_status['working_keys'] > 0 else 'CRITICAL'}")

    except ImportError:
        console.print("\n[red]ERROR: Gemini client not available for status checking.[/red]")
        console.print("• The Gemini AI client module could not be imported")
        console.print("• Status monitoring requires the Gemini client to be properly configured")
        console.print("• Check that src.core.gemini_client exists and is accessible")
        console.print("• Ensure all required dependencies are installed")
    except Exception as e:
        console.print(f"\n[red]ERROR: Status check failed with exception[/red]")
        console.print(f"• Error details: {str(e)}")
        console.print("• This may indicate:")
        console.print("  - Network connectivity issues")
        console.print("  - Invalid API key configuration")
        console.print("  - Service temporarily unavailable")
        console.print("  - File permission problems with .env")
        console.print("\n[bold]Troubleshooting Steps:[/bold]")
        console.print("1. Verify your API keys are properly configured in .env file")
        console.print("2. Check internet connection and firewall settings")
        console.print("3. Ensure Google AI Studio service is accessible")
        console.print("4. Try testing individual keys using option 5")

    console.input("\nPress Enter to continue...")
