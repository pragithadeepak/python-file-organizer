"""
Project 1: Industry-Oriented Python Automation System for Business Operations
-------------------------------------------------------------------------------
What this script does:
    Scans a target folder, sorts files into subfolders based on their file
    type (e.g., .pdf -> PDFs, .jpg -> Images), logs every action, and
    generates a summary report at the end.

This is intentionally simple to start with. Once it works, you can add
more features (scheduling, more file types, command-line arguments, etc.)
to match all the requirements listed in the brief.
"""

import os
import shutil
import logging
from datetime import datetime

# -----------------------------
# 1. SETUP: folders & logging
# -----------------------------

# Folder you want to organize. CHANGE THIS to a real folder path on your PC.
SOURCE_FOLDER = "sample_files"

# Maps file extensions to the folder name they should go into.
FILE_TYPE_MAP = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Spreadsheets",
    ".csv": "Spreadsheets",
    ".mp4": "Videos",
    ".zip": "Archives",
}

# Logging setup -> writes to a file called automation.log
logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# -----------------------------
# 2. CORE FUNCTIONS
# -----------------------------

def create_folder_if_missing(folder_path):
    """Create a folder if it doesn't already exist."""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logging.info(f"Created folder: {folder_path}")


def organize_files(source_folder):
    """
    Walks through source_folder, moves each file into a subfolder
    based on its extension, and keeps count of what was moved.
    Returns a dictionary summary: {folder_name: number_of_files_moved}
    """
    summary = {}

    if not os.path.exists(source_folder):
        logging.error(f"Source folder not found: {source_folder}")
        print(f"ERROR: Folder '{source_folder}' does not exist. Check the path.")
        return summary

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip folders, only process files
        if os.path.isdir(file_path):
            continue

        # Get extension, e.g. ".pdf"
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Decide destination folder name
        dest_folder_name = FILE_TYPE_MAP.get(ext, "Others")
        dest_folder_path = os.path.join(source_folder, dest_folder_name)

        try:
            create_folder_if_missing(dest_folder_path)
            shutil.move(file_path, os.path.join(dest_folder_path, filename))
            logging.info(f"Moved '{filename}' -> '{dest_folder_name}/'")

            summary[dest_folder_name] = summary.get(dest_folder_name, 0) + 1

        except Exception as e:
            # Error handling: log it, but keep going with other files
            logging.error(f"Failed to move '{filename}': {e}")
            print(f"Could not move {filename}: {e}")

    return summary


def generate_report(summary):
    """Prints and saves a simple summary report of what was done."""
    report_lines = ["----- Automation Report -----",
                     f"Run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"]

    if not summary:
        report_lines.append("No files were organized.")
    else:
        for folder, count in summary.items():
            report_lines.append(f"{folder}: {count} file(s) moved")

    report_text = "\n".join(report_lines)

    print(report_text)

    with open("report.txt", "w") as f:
        f.write(report_text)

    logging.info("Report generated: report.txt")


# -----------------------------
# 3. MAIN ENTRY POINT
# -----------------------------

if __name__ == "__main__":
    logging.info("Automation script started.")
    result_summary = organize_files(SOURCE_FOLDER)
    generate_report(result_summary)
    logging.info("Automation script finished.")
