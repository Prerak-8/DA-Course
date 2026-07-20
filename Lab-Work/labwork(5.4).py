# Q1

def add(a, b):
    return a + b

print("Numbers:", add(10, 20))
print("Strings:", add("Hello ", "World"))

# Q2

class Shape:
    def area(self):
        print("Area of any shape")

class Circle(Shape):
    def __init__(self, radius):
        self.r = radius

    def area(self):
        print("Area of Circle:", 3.14 * self.r * self.r)

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area(self):
        print("Area of Rectangle:", self.l * self.b)

c = Circle(5)
r = Rectangle(3, 6)

c.area()
r.area()

# Q3

class Demo:

    def show_length(self, obj):
        print("Length:", len(obj))

d = Demo()

d.show_length("Python")
d.show_length([10, 20, 30, 40])
d.show_length({"Name": "Rudra", "Age": 20})

# Q4

class Transport:

    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        print("Train is moving on tracks.")

class Plane(Transport):
    def travel(self):
        print("Plane is flying at very high speed.")

t = Train()
p = Plane()

t.travel()
p.travel()

# Q5

class Calculator:

    def multiply(self, a, b, c=None):
        if c is None:
            return a * b
        return a * b * c

obj = Calculator()

print(obj.multiply(5, 3))
print(obj.multiply(4, 4, 2))

# Q6

class Animal():
    
    def speak(self):
        pass

class Dog(Animal):

    def speak(self):
        print("Woof!")

class Cat(Animal):

    def speak(self):
        print("Meow!")

d = Dog()
c = Cat()

d.speak()
c.speak()

# Q7

class Shape:

    @staticmethod
    def area(shape, a, b=None):
        if shape == "circle":
            print("Area of Circle:", 3.14 * a * a)
        elif shape == "rectangle":
            print("Area of Rectangle:", a * b)

Shape.area("circle", 3)
Shape.area("rectangle", 5, 6)

# Q8

class Vehicle:

    def start(self):
        print("Vehicle is starting.")

class Bike(Vehicle):

    def start(self):
        print("Bike starts with a key.")

class Car(Vehicle):

    def start(self):
        print("Car starts with a push button.")

bike = Bike()
car = Car()

bike.start()
car.start()

# Q9

class Printer:

    def print_data(self, text, number=None):

        if number is None:
            print(text)
        else:
            print(text, number)

obj = Printer()

obj.print_data("Hello")
obj.print_data(100)
obj.print_data("Age:", 20)

# Q10

class Person:
    pass

class Student(Person):
    pass

print(issubclass(Student, Person))

# Q11

class employee:

    def __init__(self, name, amount):
        self.name = name
        self.salary = amount

class Manager(employee):
    
    def __init__(self, name, amount):
        super().__init__(name, amount)
        
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


manager1 = Manager("Marko", 1200)

manager1.display()

# Q12

class Grandparent():

    def buys(self):
        print("He bought a cake.")

class Parent(Grandparent):

    def buys(self):
        print("He bought flowers.")

class Child(Parent):

    def buys(self):
        print("He buys chocolate.")

child1 = Child()

child1.buys()

print(issubclass(Child, Parent))
print(issubclass(Child, Grandparent))

# Q13

class Base:

    def display(self):
        print("This is Base class")


class Derived(Base):

    def display(self):
        super().display()
        print("This is Derived class")


obj = Derived()

obj.display()

# Q14

class User:

    def __init__(self, availability):
        self.availability = availability

class Admin(User):

    def __init__(self, availability):
        super().__init__(availability)

    def display(self):
        print(self.availability)

admin1 = Admin("User is online.")

admin1.display()