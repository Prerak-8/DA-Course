# Q1 

num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))

try:
    division = num1 / num2
    print("Division:", division)

except ZeroDivisionError:
    print("Division by zero is not possible.")

# Q2

num_list = [12, 3, 5, 71, 43, 36]

try:
    print("Element:", num_list[10])

except IndexError:
    print("Index not found.")

# Q3

file_input = input("Enter file: ")

try:
    file = open(f"{file_input}", "r")

except FileNotFoundError:
    print("File not found.")

else:
    print(file.read())
    file.close()

# Q4

text = "Python"

try:
    ch = text[10]

except IndexError:
    print("Index not found.")

else:
    print("Character:", ch)

# Q5

file = None

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    if file:
        file.close()
        print("File closed.")

# Q6

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    division = num1 / num2
    print("Division:", division)

except ZeroDivisionError:
    print("Division by zero is not possible.")

except ValueError:
    print("Invalid input.")

finally:
    print("Calculation complete.")

try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    if num >= 0:
        print("Square root:", num ** 0.5)
    else:
        print("Square root of a negative number is not possible.")

finally:
    print("Execution complete.")