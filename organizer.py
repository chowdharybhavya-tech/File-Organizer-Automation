import os
import shutil
from datetime import datetime


# Function to write logs
def write_log(message):
    with open("logs.txt", "a") as log:
        log.write(f"{datetime.now()} - {message}\n")


# Function to organize files
def organize_files(folder_path):
    try:
        # Check if folder exists
        if not os.path.exists(folder_path):
            print("Folder does not exist!")
            return

        print("Folder found!")

        # Get all files/folders
        files = os.listdir(folder_path)

        for file in files:

            file_path = os.path.join(folder_path, file)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            # Get file extension
            extension = file.split(".")[-1].lower()

            # Create destination folder name
            destination_folder = os.path.join(
                folder_path,
                extension.upper() + "_Files"
            )

            # Create folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                print(destination_folder, "created")

            # Move file
            shutil.move(
                file_path,
                os.path.join(destination_folder, file)
            )

            # Log operation
            write_log(f"Moved {file} to {destination_folder}")

            print(file, "moved")

        print("Files organized successfully!")

    except Exception as e:
        write_log(f"Error: {e}")
        print("Error:", e)


# User input
folder = input("Enter folder path: ")

# Run function
organize_files(folder)