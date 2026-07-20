# Q1

class person:

    def __init__(self, name):
        self.name = name
        print(self.name)

    def __del__(self):
        print(self.name, "object deleted")

person1 = person("Zack")
person2 = person("John")

del person1
del person2

# Q2

class Animal:

    def __init__(self, name):
        self.name = name

    def display_name(self):
        print("Animal Name:", self.name)

animal_1 = Animal("Dog")
animal_2 = Animal("Cat")

animal_1.display_name()
animal_2.display_name()

# Q3

class rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_rec(self):
        area = self.length * self.width
        print("Area:",area)

measurement_1 = rectangle(5, 7)

measurement_1.area_rec()

# Q4

class Employee:

    def __init__(self):
        self.name = "kabir"

    def __del__(self):
        print("Employee" , self.name, "has been fired.")

employee_1 = Employee()
employee_2 = Employee()

employee_1.name = "Zack"
employee_2.name = "John"

del employee_1
del employee_2

# Q5

class Student:

    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll no:", self.roll_no)

student_1 = Student("Jayesh", 20, 2341)
student_2 = Student("Pradip", 18, 2731)

student_1.display()
student_2.display()