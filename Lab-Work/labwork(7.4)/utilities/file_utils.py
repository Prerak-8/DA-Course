def file_func():
    write_input = input("Enter text to add in file: ")

    with open("Testing.txt", "w") as file:
        file.write(write_input)

    with open("Testing.txt", "r") as file:
        print("File content:", file.read())