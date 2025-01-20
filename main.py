
import os
import shutil
from difPy import build, search
from multiprocessing import freeze_support

def move_duplicates_recursive(input_folder, output_folder):
    """
    Identify duplicate images from a root folder (including subfolders), keep the original based on creation date,
    and move duplicates to a specified folder.

    Args:
        input_folder (str): Path to the root folder containing images.
        output_folder (str): Path to the folder where duplicates will be moved.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Use difPy to find duplicates
    dif = build(input_folder)
    search_result = search(dif)

    for original, duplicates in search_result.result.items():
        if duplicates:  # If duplicates exist for the original image
            # Filter out missing files and sort by creation date
            paths = [original] + [dup[0] for dup in duplicates]
            paths = [path for path in paths if os.path.exists(path)]

            if not paths:
                continue

            paths.sort(key=lambda x: os.path.getctime(x))

            # Keep the oldest image and move the rest to the output folder
            for duplicate in paths[1:]:
                relative_path = os.path.relpath(duplicate, input_folder)
                duplicate_target_path = os.path.join(output_folder, relative_path)
                os.makedirs(os.path.dirname(duplicate_target_path), exist_ok=True)
                shutil.move(duplicate, duplicate_target_path)

if __name__ == "__main__":
    freeze_support()  # Required for executables

    input_folder = "./"  # Replace with your input folder path
    output_folder = f"{input_folder}/MCB_duplicate"  # Replace with your output folder path

    move_duplicates_recursive(input_folder, output_folder)

    print("Finished processing duplicates.")

