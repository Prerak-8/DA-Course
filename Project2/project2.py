print("Welcome to the Personal Pattern Generator and Number Analyser!")

while True:
    print("Select an option: ")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        rows = int(input("Enter number of rows for the pattern: "))
        
        if rows <= 0:
                print("Please enter a positive number.")
                continue
        print()
        print("Pattern:")
        print()
        for no_of_rows in range(1, rows + 1):
            for pattern in range(no_of_rows):
                print("*", end="")
            print()
        print()

    elif choice == 2:
        start_num = int(input("Enter number for start of the range: "))
        end_num = int(input("Enter number for end of the range: "))
        if start_num > end_num:
                print("End number must be greater than or equal to the start number.")
                continue
        
        total = 0
        
        for num in range(start_num, end_num + 1):
            if num % 2 == 0:
                print(f"Number {num} is Even")
            else:
                print(f"Number {num} is Odd")
            total += num
        print(f"Sum of all numbers from {start_num} to {end_num} is: {total}")
        print()
            
    elif choice == 3:
        print("Exiting the program. Bye!")
        break
    else:
        print("Invalid option")
        continue