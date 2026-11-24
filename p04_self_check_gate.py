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

def file_reader(file_name):
    if file_name == "":
        print("No filename given")
        return

    script_folder = __file__.rsplit("\\", 1)[0]
    file_path = script_folder + "\\" + file_name

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            first_line = file.readline()
            print(first_line.rstrip("\r\n"))
    except FileNotFoundError:
        print("File not found")
    except IsADirectoryError:
        print("The path is a directory, not a file")
    except PermissionError:
        print("The path is a directory or cannot be read")
    except OSError:
        print("Could not read the file")


if __name__ == "__main__":
    file_reader("Aqua.csv")
    file_reader("run.txt")
    file_reader("tol.txt")
    file_reader("")
    file_reader(".")
