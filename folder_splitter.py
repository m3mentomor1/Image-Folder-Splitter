import os
import random
import shutil

def move_half_images(source_folder, destination_folder):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)
    
    # Filter out only image files (assuming common formats like jpg, png, etc.)
    image_files = [file for file in files if file.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Calculate the number of image files to move (half of the total)
    num_images_to_move = len(image_files) // 2
    
    # Randomly select half of the image files
    files_to_move = random.sample(image_files, num_images_to_move)
    
    # Move selected files to the destination folder
    for file in files_to_move:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"Moved {file} to {destination_folder}")

# Define folder paths
if __name__ == "__main__":
    source_folder = r"path\to\folder"
    destination_folder = r"path\to\folder"
    move_half_images(source_folder, destination_folder)
