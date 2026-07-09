# Q1

numbers = [10, 15, 20, 25, 30]

print("Maximum:", max(numbers))
print("Type:", type(numbers))
print("Length:", len(numbers))
print("Sorted:", sorted(numbers))
print("Sum:", sum(numbers))

# Q2

number = int(input("Enter a number for it's factorial: "))

def factorial(number):
    fact = 1
    for num in range(1, number + 1):
        fact = fact * num
    print("Factorial: ", fact)

factorial(number)

# Q3

num_list = [12, 4, 8, 16, 9]

def square(numbers):
    square_nums = [num**2 for num in numbers] 
    print(square_nums)

square(num_list)

# Q4

text = input("Enter a string: ")

def frequency(string):
    count = {}

    for ch in string:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    return count

print(frequency(text))

# Q5

def cube(num):
    return num ** 3

def calculate(function, numbers):
    cube_nums = [function(num) for num in numbers]
    print(cube_nums)

nums = [4, 6, 7, 9]

calculate(cube, nums)

# Q6

def calculate(*numbers):
    sum = 0
    multiplication = 1

    for num in numbers:
        sum += num
        multiplication *= num 

    print("Sum: ", sum)
    print("Multiplication: ", multiplication)

calculate(4, 6, 2)

# Q7

def students(*students):
    if not students:
        print("There are no students in list")
    else:
        for name in students:
            print(name)

students("Vir", "Kishor", "Dev", "Aryan")

# Q8

def check(*text):
    string = []
    numbers = []

    for character in text:
        if type(character) == str:
            string.append(character)
        elif type(character) == int:
            numbers.append(character)

    return tuple(string), tuple(numbers)

string, numbers = check("Street", 15, "Python", "Cobra", 123)

print("Strings:", string)
print("Numbers:", numbers)

# Q9

def person(**information):
    name = information["name"]
    age = information["age"]
    city = information["city"]
    occupation = information["occupation"]

    print("Name:", name)
    print("Age:", age)
    print("City:", city)
    print("Occupation:", occupation)

person(
    name = "Gopal",
    age = 19,
    city = "Delhi",
    occupation = "Unemployed"
    )

# Q10

def product(**details):
    name = details["name"]
    cost = details["cost"]
    quantity = details["quantity"]
    
    total_cost = cost * quantity

    return f"Product: {name}, Total Cost: {total_cost}"

print(product(
    name = "Biscuit",
    cost = 3.5,
    quantity = 2
))

# Q11

def employee(**info):
    if "name" not in info or "department" not in info or "salary" not in info:
        print("Required fields are missing.")
    else:
        name = info["name"]
        department = info["department"]
        salary = info["salary"]

        print("Name:", info["name"])
        print("Department:", info["department"])
        print("Salary:", info["salary"])

employee(
    name = "Aleck",
    department = "Sales",
    salary = 20000
)

# Q12

def area(length, breadth):
    """
    Calculates the area of a rectangle.

    Parameters:
    length : Length of the rectangle.
    breadth : Breadth of the rectangle.

    Returns:
    Area of the rectangle.
    """
    return length * breadth

print("Area:", area(5, 7))

print(area.__doc__)

# Q13

def fibonacci(num):
    """
    Returns the Fibonacci number using recursion.

    Parameter:
    num (int): Position in the Fibonacci sequence.

    Returns:
    int: Fibonacci number.
    """

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

number = int(input("Enter a number: "))

for digit in range(number):
    print(fibonacci(digit), end=" ")

print()
print(fibonacci.__doc__)