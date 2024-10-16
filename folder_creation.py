"""
Programmer: Steven Schuch
Purpose: To create a folder structure for University of Maryland Community College
         for personal documentation.
Date: 10/16/2024
Version: 1.0
"""

#import database for file path simplicity
import os
from typing import Union


def create_folder(base_dir: Union[str, os.PathLike],
                  class_dir: str, num_weeks: int = 8) -> None:
    # Ensure the base directory is a valid string or path
    if not isinstance(base_dir, (str, os.PathLike)):
        print(f"Error: base_dir must be a string or PathLike object, not {type(base_dir)}")
        return

    # Check if base directory exists
    if not os.path.exists(base_dir):
        print(f"Error: The base directory '{base_dir}' does not exist.")
        return

    # Construct the class folder path
    class_folder = os.path.join(base_dir, class_dir)

    try:
        os.makedirs(class_folder, exist_ok=True)
        print(f"Class folder '{class_dir}' created at '{class_folder}'.")

        week_folders = []
        for i in range(1, num_weeks + 1):
            week_folder = os.path.join(class_folder, f"Week {i}")
            os.makedirs(week_folder, exist_ok=True)
            week_folders.append(f"Week_{i} created at {week_folder}")

        print("Week folders created successfully:")
        for folder in week_folders:
            print(f"- {folder}")

    except PermissionError:
        print("Error: Insufficient permissions to create folders.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Prompt user for base directory and class name
    base_dir_input = input("Enter base directory: ").strip()
    class_dir_input = input("Enter class name: ").strip()

    # Create the folder structure
    create_folder(base_dir_input, class_dir_input)

