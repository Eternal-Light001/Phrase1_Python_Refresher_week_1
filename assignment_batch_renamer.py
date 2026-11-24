# STEP 1
# Create a function to rename files in folder

import os

# TEST TABLE
# Scenario 1 — 3 files, prefix "report_", no conflicts:
#   → Renamed 3 | Skipped 0 | Errors 0
#   → b.txt → report_b.txt, c.txt → report_c.txt
#
# Scenario 2 — report_a.txt already exists:
#   → a.txt SKIPPED (target exists)
#   → Renamed 2 | Skipped 1 | Errors 0
#
# Scenario 3 — folder path invalid:
#   → "Folder not found" message, no crash
#   → exit early
#
# Scenario 4 — dry_run=True:
#   → Prints [DRY RUN] lines, no files renamed

def batch_renamer(folder_path, prefix, dry_run=False):
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    renamed = 0
    skipped = 0
    errors = 0

    for name in os.listdir(folder_path):            
        old_path = os.path.join(folder_path, name) 

        if not os.path.isfile(old_path):
            continue                              

        new_name = prefix + name               
        new_path = os.path.join(folder_path, new_name)

        if os.path.exists(new_path):
            print(f"⚠️  Skipped (target exists): {name} → {new_name}")
            skipped += 1
            continue

        try:
            if dry_run:
                print(f"[DRY RUN] Would rename: {name} → {new_name}")
            else:
                os.rename(old_path, new_path)
                print(f"✅ Renamed: {name} → {new_name}")
            renamed += 1
        except FileNotFoundError:
            print(f"⚠️  Skipped (vanished): {name}")
            skipped += 1
        except OSError as e:
            print(f"❌ Error: {name}: {e}")
            errors += 1

    print(f"\nSummary: Renamed: {renamed} | Skipped: {skipped} | Errors: {errors}")


if __name__ == "__main__":
    folder = input("Folder path: ").strip()
    prefix = input("Prefix: ").strip()
    dry = input("Dry run? (y/n): ").strip().lower() == "y"
    batch_renamer(folder, prefix, dry_run=dry)