import os
import shutil
from organizer.config_loader import load_rules
from organizer.logger import log

def organize_folder(path):
    rules = load_rules()

    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)

        if os.path.isfile(full_path):
            ext = filename.split(".")[-1].lower()

            for folder, extensions in rules.items():
                if ext in extensions:
                    target_folder = os.path.join(path, folder)
                    os.makedirs(target_folder, exist_ok=True)

                    shutil.move(full_path, os.path.join(target_folder, filename))
                    log(f"Moved {filename} → {folder}")
                    break
