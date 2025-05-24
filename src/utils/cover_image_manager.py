"""
Cover image manager for handling user-provided cover images and integration.
"""
import os
from typing import Dict, Any, List, Optional
from rich.console import Console
from rich.table import Table
from rich import box
import questionary

from src.utils.cover_folder_manager import CoverFolderManager
from src.utils.file_handler import load_novel_json
from src.formatters.epub_formatter import EpubFormatter
from src.ui.terminal_ui import custom_style

console = Console(markup=True)


class CoverImageManager:
    """
    Manages user-provided cover images and their integration into ebooks.
    """
    
    def __init__(self):
        """Initialize the cover image manager."""
        self.folder_manager = CoverFolderManager()
    
    def manage_book_cover_images(self, book_info: Dict[str, Any]) -> None:
        """
        Manage cover images for a single book.
        
        Args:
            book_info: Book information dictionary
        """
        console.print(f"\n[bold cyan]Managing Cover Images for '{book_info['title']}'[/bold cyan]")
        
        # Load novel data
        try:
            novel_data = load_novel_json(book_info["json_path"])
        except Exception as e:
            console.print(f"[bold red]Error loading book data: {str(e)}[/bold red]")
            return
        
        # Get cover folder information
        folder_info = self.folder_manager.get_cover_folder_structure_info(
            book_info["directory"], 
            book_info["title"]
        )
        
        # Display current status
        self._display_cover_status(folder_info, book_info)
        
        # Show management options
        while True:
            choices = [
                "View Cover Prompt",
                "Check for Cover Images",
                "Apply Cover to EPUB",
                "Show Folder Structure",
                "Show Naming Convention",
                "← Back"
            ]
            
            selected = questionary.select(
                "What would you like to do?",
                choices=choices,
                style=custom_style
            ).ask()
            
            if selected == "View Cover Prompt":
                self._view_cover_prompt(book_info["directory"])
            
            elif selected == "Check for Cover Images":
                self._check_for_cover_images(book_info, folder_info)
            
            elif selected == "Apply Cover to EPUB":
                self._apply_cover_to_epub(book_info, novel_data, folder_info)
            
            elif selected == "Show Folder Structure":
                self._show_folder_structure(folder_info)
            
            elif selected == "Show Naming Convention":
                self._show_naming_convention(folder_info)
            
            elif selected == "← Back":
                break
            
            input("\nPress Enter to continue...")
    
    def manage_series_cover_images(self, series_manager, book_info: Dict[str, Any]) -> None:
        """
        Manage cover images for a book in a series.
        
        Args:
            series_manager: SeriesManager instance
            book_info: Book information dictionary
        """
        console.print(f"\n[bold cyan]Managing Cover Images for Series Book '{book_info['title']}'[/bold cyan]")
        
        # Get series information
        series_info = {
            'series_title': series_manager.series_title,
            'book_number': book_info.get('book_number', 1)
        }
        
        # Load novel data
        try:
            novel_data = load_novel_json(book_info["json_path"])
        except Exception as e:
            console.print(f"[bold red]Error loading book data: {str(e)}[/bold red]")
            return
        
        # Get cover folder information
        folder_info = self.folder_manager.get_cover_folder_structure_info(
            book_info["directory"], 
            book_info["title"],
            series_info
        )
        
        # Display current status
        self._display_cover_status(folder_info, book_info, series_info)
        
        # Show management options
        while True:
            choices = [
                "View Cover Prompt",
                "Check for Cover Images",
                "Apply Cover to EPUB",
                "Show Folder Structure",
                "Show Naming Convention",
                "← Back"
            ]
            
            selected = questionary.select(
                "What would you like to do?",
                choices=choices,
                style=custom_style
            ).ask()
            
            if selected == "View Cover Prompt":
                self._view_cover_prompt(book_info["directory"])
            
            elif selected == "Check for Cover Images":
                self._check_for_cover_images(book_info, folder_info, series_info)
            
            elif selected == "Apply Cover to EPUB":
                self._apply_cover_to_epub(book_info, novel_data, folder_info, series_info)
            
            elif selected == "Show Folder Structure":
                self._show_folder_structure(folder_info, series_info)
            
            elif selected == "Show Naming Convention":
                self._show_naming_convention(folder_info)
            
            elif selected == "← Back":
                break
            
            input("\nPress Enter to continue...")
    
    def _display_cover_status(self, folder_info: Dict[str, Any], book_info: Dict[str, Any],
                            series_info: Optional[Dict[str, Any]] = None) -> None:
        """Display the current cover status."""
        console.print("\n[bold cyan]Current Cover Status[/bold cyan]")
        
        status_table = Table(box=box.ROUNDED, show_header=False)
        status_table.add_column("Item", style="cyan", width=20)
        status_table.add_column("Status", style="white")
        
        # Check for cover prompt
        prompt_path = os.path.join(book_info["directory"], "cover_prompt.md")
        prompt_status = "✓ Available" if os.path.exists(prompt_path) else "✗ Not found"
        status_table.add_row("Cover Prompt", prompt_status)
        
        # Check for cover folder
        folder_status = "✓ Exists" if folder_info["folder_exists"] else "✗ Not created"
        status_table.add_row("Cover Folder", folder_status)
        
        # Check for cover images
        found_images = self.folder_manager.scan_for_cover_images(
            book_info["directory"], 
            book_info["title"], 
            series_info
        )
        image_status = f"✓ {len(found_images)} found" if found_images else "✗ No images found"
        status_table.add_row("Cover Images", image_status)
        
        # Check for EPUB file
        epub_files = [f for f in os.listdir(book_info["directory"]) if f.endswith(".epub")]
        epub_status = "✓ Available" if epub_files else "✗ No EPUB found"
        status_table.add_row("EPUB File", epub_status)
        
        console.print(status_table)
    
    def _view_cover_prompt(self, book_dir: str) -> None:
        """View the cover prompt file."""
        prompt_path = os.path.join(book_dir, "cover_prompt.md")
        
        if not os.path.exists(prompt_path):
            console.print("[yellow]No cover prompt found. Generate a book first to create the prompt.[/yellow]")
            return
        
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                prompt_content = f.read()
            
            console.print(f"\n[bold cyan]Cover Prompt ({prompt_path})[/bold cyan]")
            console.print("[dim]" + "="*80 + "[/dim]")
            console.print(prompt_content)
            console.print("[dim]" + "="*80 + "[/dim]")
            
        except Exception as e:
            console.print(f"[bold red]Error reading cover prompt: {str(e)}[/bold red]")
    
    def _check_for_cover_images(self, book_info: Dict[str, Any], folder_info: Dict[str, Any],
                              series_info: Optional[Dict[str, Any]] = None) -> None:
        """Check for existing cover images."""
        found_images = self.folder_manager.scan_for_cover_images(
            book_info["directory"], 
            book_info["title"], 
            series_info
        )
        
        if not found_images:
            console.print("[yellow]No cover images found.[/yellow]")
            console.print("\n[bold cyan]To add a cover image:[/bold cyan]")
            console.print(f"1. Create the folder: [bold cyan]{folder_info['cover_folder']}[/bold cyan]")
            console.print(f"2. Place your image as: [bold cyan]{folder_info['expected_path']}[/bold cyan]")
            console.print(f"3. Supported formats: {', '.join(folder_info['supported_formats'])}")
            return
        
        console.print(f"\n[bold green]Found {len(found_images)} cover image(s):[/bold green]")
        
        images_table = Table(box=box.ROUNDED)
        images_table.add_column("File", style="white", width=40)
        images_table.add_column("Size", style="yellow", width=10)
        images_table.add_column("Status", style="green", width=15)
        
        for image_path in found_images:
            filename = os.path.basename(image_path)
            
            # Get file size
            try:
                size = os.path.getsize(image_path)
                if size < 1024 * 1024:
                    size_str = f"{size / 1024:.1f} KB"
                else:
                    size_str = f"{size / (1024 * 1024):.1f} MB"
            except:
                size_str = "Unknown"
            
            # Validate image
            is_valid, message = self.folder_manager.validate_cover_image(image_path)
            status = "✓ Valid" if is_valid else f"✗ {message}"
            
            images_table.add_row(filename, size_str, status)
        
        console.print(images_table)
    
    def _apply_cover_to_epub(self, book_info: Dict[str, Any], novel_data: Dict[str, Any],
                           folder_info: Dict[str, Any], series_info: Optional[Dict[str, Any]] = None) -> None:
        """Apply a cover image to the EPUB file."""
        # Check for EPUB file
        epub_files = [f for f in os.listdir(book_info["directory"]) if f.endswith(".epub")]
        if not epub_files:
            console.print("[yellow]No EPUB file found. Generate the book first.[/yellow]")
            return
        
        # Find cover images
        found_images = self.folder_manager.scan_for_cover_images(
            book_info["directory"], 
            book_info["title"], 
            series_info
        )
        
        if not found_images:
            console.print("[yellow]No cover images found. Add a cover image first.[/yellow]")
            return
        
        # Select cover image if multiple found
        selected_image = None
        if len(found_images) == 1:
            selected_image = found_images[0]
        else:
            image_choices = [os.path.basename(img) for img in found_images]
            image_choices.append("← Cancel")
            
            selected = questionary.select(
                "Select a cover image:",
                choices=image_choices,
                style=custom_style
            ).ask()
            
            if selected == "← Cancel":
                return
            
            # Find the full path
            for img in found_images:
                if os.path.basename(img) == selected:
                    selected_image = img
                    break
        
        if not selected_image:
            console.print("[bold red]Error: Could not select cover image.[/bold red]")
            return
        
        # Validate the selected image
        is_valid, message = self.folder_manager.validate_cover_image(selected_image)
        if not is_valid:
            console.print(f"[bold red]Invalid cover image: {message}[/bold red]")
            return
        
        try:
            console.print(f"[bold cyan]Applying cover to EPUB...[/bold cyan]")
            
            # Update EPUB with the cover
            formatter = EpubFormatter(novel_data)
            epub_path = formatter.save_epub(book_info["directory"], selected_image)
            
            console.print(f"[bold green]✓[/bold green] Cover applied successfully!")
            console.print(f"[bold green]✓[/bold green] EPUB updated: [bold cyan]{epub_path}[/bold cyan]")
            
        except Exception as e:
            console.print(f"[bold red]Error applying cover: {str(e)}[/bold red]")
    
    def _show_folder_structure(self, folder_info: Dict[str, Any], 
                             series_info: Optional[Dict[str, Any]] = None) -> None:
        """Show the folder structure information."""
        console.print("\n[bold cyan]Cover Folder Structure[/bold cyan]")
        
        structure_table = Table(box=box.ROUNDED, show_header=False)
        structure_table.add_column("Item", style="cyan", width=20)
        structure_table.add_column("Path", style="white")
        
        structure_table.add_row("Cover Folder", folder_info["cover_folder"])
        structure_table.add_row("Expected Image", folder_info["expected_path"])
        
        console.print(structure_table)
        
        if series_info:
            console.print(f"\n[bold yellow]Note:[/bold yellow] This is book {series_info['book_number']} in the '{series_info['series_title']}' series.")
    
    def _show_naming_convention(self, folder_info: Dict[str, Any]) -> None:
        """Show the naming convention information."""
        naming_info = folder_info["naming_convention"]
        
        console.print("\n[bold cyan]Cover Image Naming Convention[/bold cyan]")
        console.print(f"[bold yellow]Type:[/bold yellow] {naming_info['type'].title()}")
        console.print(f"[bold yellow]Required Filename:[/bold yellow] {naming_info['filename']}")
        console.print(f"[bold yellow]Pattern:[/bold yellow] {naming_info['pattern']}")
        console.print(f"[bold yellow]Description:[/bold yellow] {naming_info['description']}")
        
        console.print(f"\n[bold cyan]Supported Formats:[/bold cyan]")
        for fmt in folder_info["supported_formats"]:
            console.print(f"  • {fmt.upper()}")
        
        console.print(f"\n[bold cyan]Recommendations:[/bold cyan]")
        console.print("  • Use high resolution images (300 DPI minimum)")
        console.print("  • Maintain 6:9 aspect ratio (standard book cover)")
        console.print("  • Keep file size under 10MB for best performance")
        console.print("  • Use JPG format for photographs, PNG for graphics with transparency")
