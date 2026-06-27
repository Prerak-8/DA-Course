# Q1

print("Lake", "River", "Bird", sep=" - ")
print("hi", end= "**")
print("Hello", end= ".")
print()
# Q2

name = input("Enter your name: ")
age = input("Enter your age: ")
favourite_hobby = input("Enter your favourite hobby: ")

print(f"Hello, {name}! At {age}, enjoying {favourite_hobby} sounds fun!")
print()
# Q3

num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

print(f"Addition : {addition}")
print(f"Subtraction : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")
print(f"Floor Division : {floor_division}")
print(f"Modulus : {modulus}")
print(f"Exponentiation : {exponentiation}")
print()

# Q4

age = 25
print("Value:", age, " Type:", type(age))

price = 19.99
print("Value:", price, " Type:", type(price))

name = "Alice"
print("Value:", name, " Type:", type(name))

is_active = True
print("Value:", is_active, " Type:", type(is_active))

coordinates = 3 + 4j
print("Value:", coordinates, " Type:", type(coordinates))

numbers = [1, 2, 3]
print("Value:", numbers, " Type:", type(numbers))

point = (10, 20)
print("Value:", point, "Type:", type(point))
print()

# Q5

height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

print(f"Your height is {height} cm and weight is {weight} kg")

# Q6

prefers_coffee = input("Do you prefer coffee (True or False) : ") == "True"
prefers_milk = input("Do you prefer milk (True or False) : ") == "True"

print(f"you like coffee and milk: {prefers_coffee and prefers_milk} ")
print(f"you like coffee or milk: {prefers_milk or prefers_coffee} ")
print(f"you like  not milk: {not prefers_coffee}")
print()

# Q7

variable = int(input("Enter a number: "))

print(f"value = {variable}")

variable += 8
print(f"after += : {variable}")

variable -= 6
print(f"after -= : {variable}")

variable *= 3
print(f"after *= : {variable}")

variable /= 2
print(f"after /= : {variable}")

# complete