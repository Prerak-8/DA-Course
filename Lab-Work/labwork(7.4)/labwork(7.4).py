# Q1

from math_utils import add, subtract, multiply, divide

print("Addition:", add(11, 3))
print("Subtraction:", subtract(22, 7))
print("Multiplication:", multiply(4, 7))
print("Division:", divide(15, 5))

# Q2

import math as m 

print("Square root of 49: ", m.sqrt(49))

print("Value of sin(90°)", m.sin(m.radians(90)))

# Q3

from string_utils import count

result = count("Fountain")

print("Number of vowels in string:", result)

# Q4

from greeting import greet

greet("Amir")

# Q5
# This question is completed using two separate files:
# 1. main_program.py
# 2. helper.py

# Q6

from shapes.circle import circle
from shapes.rectangle import rectangle

circle_area, circumference = circle(5)
rectangle_area, perimeter = rectangle(3, 7)

print("Circle area:", circle_area)
print("Circle circumference:", circumference)

print("Rectangle area:", rectangle_area)
print("Rectangle perimeter:", perimeter)

# Q7

from utilities.file_utils import file_func
from utilities.date_utils import date_diff

file_func()

first_date = input("Enter first date in DD-MM-YYYY format: ")
second_date = input("Enter second date in DD-MM-YYYY format: ")

days = date_diff(first_date, second_date)

print("The number of days between the dates is:", days)

# Q8

import math

print("Attributes and methods of math module:")
print(dir(math))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


person1 = Person("Amir", 20)

print("\nAttributes and methods of Person object:")
print(dir(person1))

# Q9

from geometry import (circle_area, circle_circumference, triangle_area, triangle_perimeter)

print("Circle area:", circle_area(5))
print("Circle circumference:", circle_circumference(5))

print("Triangle area:", triangle_area(10, 6))
print("Triangle perimeter:", triangle_perimeter(3, 4, 5))