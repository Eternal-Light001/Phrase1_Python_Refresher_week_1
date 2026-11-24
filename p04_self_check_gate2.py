# STEP 1
# Create a function that receives a filename.
# Find and open the file in the same folder as this Python script.
# Print the first line of the file.
# Show a helpful message if the filename is blank or cannot be read.

# TEST TABLE (expected)
# Missing file "Aqua.csv"       -> File not found
# Existing file "run.txt"       -> I Like Running
# Existing file "tol.txt"       -> I am a girl
# Empty filename ""             -> No filename given
# Folder path "."               -> The path is a directory or cannot be read

import os
print("Current folder:", os.getcwd())

def file_reader(filename):
    if filename == "":
        print("No filename given")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            files = f.readline()
            print(files.strip())

    except FileNotFoundError:
        print("!!! File not found")
    except OSError:
        print("The path is a directory or cannot be read")

if __name__ == "__main__":
    file_reader("Aqua.csv")
    file_reader("run.txt")
    file_reader("tol.txt")
    file_reader("")
    file_reader(".")