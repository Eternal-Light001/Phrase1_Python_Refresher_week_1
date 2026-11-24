# STEP 1
# Import os and shutil to organize txt files into TXT_FOLDERS
# It will move the txt files from desktop to TXT_FOLDERS that is on the desktop

# TEST TABLE 
# Import successful
# TXT_FOLDERS has txt files

import os
import shutil

def classwork_folder_organizer():
    Desktop = os.path.expanduser("~/Desktop")
    print(f"Working on:- {Desktop}")

    Direction = os.path.join(Desktop, "TXT_FOLDER")

    os.makedirs(Direction, exist_ok=True)

    moved = 0
    skipped = 0
    errors = 0

    for name in os.listdir(Desktop):
        if name.endswith(".txt"):
            try:
                shutil.move(os.path.join(Desktop, name), os.path.join(Direction, name))
                print(f"✅ Moved: {name}")
                moved += 1
            except FileNotFoundError:
                print(f"⚠️  Skipped (file vanished): {name}")
                skipped += 1
            except OSError as e:
                print(f"❌ Error moving {name}, {e}")
                errors += 1

    print(f"\nSummary: Moved:- {moved} | Skipped:- {skipped} | Errors:- {errors}")


if __name__ == "__main__":
    classwork_folder_organizer()