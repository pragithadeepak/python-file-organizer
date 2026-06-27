# Python File Organizer Automation Tool

## Overview
A Python script that automates the organization of files in a folder.
It scans a target directory, sorts files into subfolders based on file
type (PDFs, Images, Documents, Spreadsheets, etc.), logs every action,
and generates a summary report.

This project was built as part of the RISE Internship Python Programming
track — **Project 1: Industry-Oriented Python Automation System for
Business Operations**.

## Problem Statement
Many organizations rely on manual file handling for repetitive tasks.
This is time-consuming and error-prone. This script automates that
process for a single use case: organizing files by type.

## Features
- Automatically detects file type by extension
- Creates destination folders if they don't exist
- Moves files into the correct folder
- Logs every action (and any errors) to `automation.log`
- Generates a summary report (`report.txt`) after each run

## Tools / Libraries Used
- Python 3
- Standard libraries only: `os`, `shutil`, `logging`, `datetime`

## How to Run
1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/python-file-organizer.git
   cd python-file-organizer
   ```
2. Update the `SOURCE_FOLDER` variable in `organizer.py` to point to the
   folder you want to organize.
3. Run the script:
   ```bash
   python organizer.py
   ```
4. Check `automation.log` for a detailed log and `report.txt` for a
   summary of what was moved.

## Example Output
```
----- Automation Report -----
Run time: 2026-06-26 14:32:10
PDFs: 3 file(s) moved
Images: 5 file(s) moved
Documents: 2 file(s) moved
```

## Possible Improvements
- Add command-line arguments (so you don't have to edit the script each time)
- Add scheduling (run automatically every day using `schedule` or cron)
- Support more file types
- Add unit tests

## Author
Pragitha Deepak
