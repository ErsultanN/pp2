import os
import string

# 1. List only directories, files, and all directories, files in a specified path
def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll directories and files:")
    for item in os.listdir(path):
        print(item)

# 2. Check for access to a specified path
def check_access(path):
    print(f"Existence: {os.path.exists(path)}")
    print(f"Readability: {os.access(path, os.R_OK)}")
    print(f"Writability: {os.access(path, os.W_OK)}")
    print(f"Executability: {os.access(path, os.X_OK)}")

# 3. Test whether a given path exists, and if so, find the filename and directory portion
def path_info(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Filename: {os.path.basename(path)}")
        print(f"Directory: {os.path.dirname(path)}")
    else:
        print("Path does not exist.")

# 4. Count the number of lines in a text file
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return len(lines)

# 5. Write a list to a file
def write_list_to_file(filename, my_list):
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(f"{item}\n")

# 6. Generate 26 text files named A.txt, B.txt, ... Z.txt
def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"C:\\Users\\Ersultan\\Documents\\{letter}.txt", 'w') as file:
            file.write(f"This is file {letter}.txt")

# 7. Copy the contents of a file to another file
def copy_file(source, destination):
    with open(source, 'r') as src:
        content = src.read()
    with open(destination, 'w') as dest:
        dest.write(content)

# 8. Delete file by specified path, checking for access and existence
def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)
        print(f"File {path} has been deleted.")
    else:
        print("File does not exist or is not writable.")

# Example usage
path = "C:\\Users\\Ersultan\\Documents"
list_directories_files(path)
check_access(path + "\\text.txt")
path_info(path + "\\text.txt")
print(f"Number of lines: {count_lines(path + '\\text.txt')}")
write_list_to_file(path + "\\text1.txt", ["apple", "banana", "cherry"])
generate_files()
copy_file(path + "\\text.txt", path + "\\text1.txt")
delete_file(path + "\\text1.txt")