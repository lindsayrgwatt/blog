import os
import re

# Paths to your markdown and image directories
markdown_dir = '/Users/lindsayrgwatt/Documents/lindsayrgwatt/blog/content'
image_dir = '/Users/lindsayrgwatt/Documents/lindsayrgwatt/blog/content/images'

# Regex pattern to find image references in markdown files and extract the full path
image_pattern = re.compile(r'(?:src|href)="\{static\}/images([^"]+?\.(?:png|jpg|jpeg|gif|bmp|svg))"') # used in src
link_pattern =  re.compile(r'\]\(\{static\}/images(/[^)]+?\.(?:png|jpg|jpeg|gif|bmp|svg))\)') # used in links

# Set to store all image paths found in markdown files
referenced_images = set()

# Function to collect all image references from markdown files
def find_referenced_images(markdown_dir):
    for root, _, files in os.walk(markdown_dir):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = link_pattern.findall(content)
                    for match in matches:
                        referenced_images.add(match)
                    
                    matches = image_pattern.findall(content)
                    for match in matches:
                        referenced_images.add(match)
                

# Set to store all image files present in the image directory (with full relative paths)
image_files = set()

# Function to collect all image files from the image directory with full paths
def find_image_files(image_dir):
    for root, _, files in os.walk(image_dir):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.svg')):
                # Get the relative path from the image_dir to the file
                relative_path = os.path.relpath(os.path.join(root, file), image_dir)
                # Convert to UNIX-style path for consistency
                relative_path = '/' + relative_path.replace(os.sep, '/')
                image_files.add(relative_path)

# Run the functions to populate the sets
find_referenced_images(markdown_dir)
find_image_files(image_dir)

# Find images that are in the image directory but not referenced in markdown files
unused_images = image_files - referenced_images

# Delete the unused images
print("\nDeleting images in the image directory that are not referenced in markdown files:")
for image in sorted(unused_images):
    # Construct the full path to the image file
    full_image_path = os.path.join(image_dir, image[1:])  # Remove the leading '/' for os.path.join to work correctly
    try:
        os.remove(full_image_path)
        print(f"Deleted: {full_image_path}")
    except FileNotFoundError:
        print(f"File not found (already deleted?): {full_image_path}")
    except Exception as e:
        print(f"Error deleting {full_image_path}: {e}")