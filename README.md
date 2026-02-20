# File Organizer Pro

A desktop application that automatically organizes files into folders based on customizable rules.  
Built with Python, Tkinter, and JSON configuration.

## Features
- Clean graphical user interface
- Customizable file-type rules (via config.json)
- Automatic folder creation
- Logging system (logs/app.log)
- Error handling and progress messages
- Modular and scalable architecture

## How It Works
1. Select a folder using the GUI.
2. The app reads `config.json` to determine how to sort files.
3. Files are moved into their corresponding folders.
4. All actions are logged in `logs/app.log`.

## Updates
- Added status label that shows progress during organization (Feb 2026)
