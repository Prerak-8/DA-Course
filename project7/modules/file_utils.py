# File handling utility functions.

def create_file():
    file = input("Enter file name: ")

    try:
        with open(file, "x") as f:
            f.write("")
        print("File created successfully!")

    except FileExistsError:
        print("File already exists!")

    print("--------------------------\n")

def write_file():
    file = input("Enter file name: ")
    write_int = input("Enter data to write: ")

    try:
        with open(file, "w") as f:
            f.write(write_int)
        print("Data written successfully!")

    except PermissionError:
        print("Permission denied.")

    print("--------------------------\n")

def read_file():
    file = input("Enter file name: ")

    try:
        with open(file, "r") as f:
            content = f.read()
        print("File content:", content)

    except FileNotFoundError:
        print("File not found.")
    
    print("--------------------------\n")

def append_file():
    file = input("Enter file name: ")
    
    append_int = input("Enter data to append: ")

    try:
        with open(file, "a") as f:
            f.write(append_int + "\n")
        print("Data appended successfully!")

    except PermissionError:
        print("Permission denied.")
    
    print("--------------------------\n")