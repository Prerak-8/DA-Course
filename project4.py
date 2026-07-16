print("Welcome to Data Analyzer and Transformer Program")

while True:
    print("Main Menu:")
    print("1. Input Data")
    print("2. Display Data Summary (Built-in functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program\n")
    choice = int(input("Enter your choice: "))
    print()

    match choice:
        case 1:
            data_1D = list(map(int, input("Enter data for a 1D array (separated by spaces): ").split()))
            print()

            print("Data has been stored successfully!\n")

        case 2:
            print("Data Summary:")
            print("Total elements:", len(data_1D))
            print("Minimum:", min(data_1D))
            print("Maximum:", max(data_1D))
            print("Sum:", sum(data_1D))
            print("Average:", sum(data_1D) / len(data_1D))
            print()

        case 3:
            def factorial(n):
                """Returns factorial using recursion."""
                if n == 0 or n == 1:
                    return 1
                return n * factorial(n - 1)
            fact_num = int(input("Enter a number to calculate factorial: "))
            print()
            print(f"Factorial of {fact_num} is: {factorial(fact_num)}\n")
        
        case 4:
            threshold = int(input("Enter a threshold value to filter out data above this value: "))
            print()

            filter_value = list(filter(lambda x: x >= threshold, data_1D))
            print(f"Filtered Data (values >= {threshold}):")
            print(", ".join(map(str, filter_value)))
            print()

        case 5:
            print("choose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            print()

            sort_choice = int(input("Enter your choice: "))

            if sort_choice == 1:
                data_1D.sort()
                print(data_1D)
                print()

            elif sort_choice == 2:
                print(sorted(data_1D, reverse=True))
                print()
            
            else:
                print("invalid option.\n")
        
        case 6:
            print("Dataset Statistics:")

            def statistics(data):
                """Returns minimum, maximum, total and average."""
                minimum = min(data)
                maximum = max(data)
                total = sum(data)
                average = total / len(data)
                return minimum, maximum, total, average
            
            minimum, maximum, total, average = statistics(data_1D)

            print(f"Minimum value: {minimum}")
            print(f"Maximum value: {maximum}")
            print(f"Sum of all values: {total}")
            print(f"Average value: {average:.2f}")
            print()
        
        case 7:
            break

        case _:
            print("invalid choice.\n")

print("Thank you for using Data Analyzer and Transformer Program.\nGoodbye.\nHave a nice day!")