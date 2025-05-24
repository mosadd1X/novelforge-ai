import os
import shutil
from PIL import Image

# Directories
input_dir = "writer_profile_images/portraits/"
backup_dir = r"C:\Users\eakub\Downloads\backup"

# Ensure backup directory exists
os.makedirs(backup_dir, exist_ok=True)

# Inform user about the operation
print("Starting image conversion...")
print(f"Looking for PNG files in: {input_dir}")
print(f"Backup location for original PNGs: {backup_dir}")

# Process each PNG
for filename in os.listdir(input_dir):
    if filename.lower().endswith(".png"):
        input_path = os.path.join(input_dir, filename)
        base_name = os.path.splitext(filename)[0]
        output_filename = base_name + ".jpg"
        output_path = os.path.join(input_dir, output_filename)

        print(f"\nProcessing: {filename}")

        try:
            with Image.open(input_path) as img:
                # Convert to RGB (removes alpha channel if present)
                img = img.convert("RGB")

                # Resize to 800x800
                img = img.resize((800, 800), Image.LANCZOS)

                # Save as JPG with 300 DPI
                img.save(output_path, "JPEG", dpi=(300, 300), quality=95)
                print(f"✓ Converted and saved as: {output_filename}")

            # Move original PNG to backup
            backup_path = os.path.join(backup_dir, filename)
            shutil.move(input_path, backup_path)
            print(f"✓ Moved original PNG to backup: {backup_path}")

        except Exception as e:
            print(f"✗ Failed to process {filename}: {e}")

print("\n✅ Conversion complete!")
