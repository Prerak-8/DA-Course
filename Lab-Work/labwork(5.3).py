# Q1

class parent:

    def display(self):
        self.name = "Bob"
        print(self.name)

class child(parent):
    pass

obj = child()

obj.display()

# Q2

class Teacher:

    def job_tech(self):
        print("Teaches students.")

class Administrator:

    def job_manage(self):
        print("Handles school responsibilities.")

class Headmaster(Teacher, Administrator):

    def job(self):
        print("Holds the highest authority.")


obj = Headmaster()

obj.job()
obj.job_manage()
obj.job_tech()

# Q3

class Grandparent():

    def ownership_1(self):
        print("Grandfather:\n")
        print("Owns a house")

class Parent(Grandparent):

    def ownership_2(self):
        print("Father:\n")
        print("Owns a bike")

class Child(Parent):

    def ownership_3(self):
        print("Son:\n")
        print("Owns a toy")

obj = Child()

obj.ownership_1()
obj.ownership_2()
obj.ownership_3()

# Q4

class Animal:

    def sleep(self):
        print("Animal is sleeping.")


class Dog(Animal):

    def bark(self):
        print("Dog says: Woof!")


class Cat(Animal):

    def meow(self):
        print("Cat says: Meow!")


dog = Dog()
cat = Cat()

dog.sleep()
dog.bark()

cat.sleep()
cat.meow()

# Q5

class Building:

    def show(self):
        print("Building")


class Bank(Building):

    def show(self):
        super().show()
        print("Bank")


class Office(Building):

    def show(self):
        super().show()
        print("Office")


class CEO(Bank, Office):

    def show(self):
        super().show()
        print("CEO")


person = CEO()

person.show()

# Q6

class Student:
    pass

student1 = Student()

print(type(student1))

# Q7

class Student:

    def display(self):
        print("Hello")


student1 = Student()

print(dir(student1))

# Q8

class Animal:
    pass


dog = Animal()

print(isinstance(dog, Animal))
print(isinstance(dog, int))

# Q9

class Student:

    def display(self):
        print("Hello")


help(Student)