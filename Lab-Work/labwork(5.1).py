# Q1

class Person:
    name = None
    age = None

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person()
person2 = Person()

person1.name = "Mukesh"
person1.age = 32

person2.name = "Suresh"
person2.age = 27

person1.display()
person2.display()

# Q2

class Count:
    count = 0

    def increment(self):
        self.count += 1

    def display(self):
        print("Count =", self.count)

count1 = Count()
count2 = Count()

count1.increment()
count1.display()

count2.increment()
count2.display()

# Q3

class Student:
    def display():
        print("Hello")

stud1 = Student()

stud1.display()

# Error: display() takes 0 positional arguments but 1 was given

# Q4

class Book:

    def set_details(self, title, author):
        self.__title = title
        self.__author = author

    def get_details(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


book1 = Book()

book1.set_details("Python Programming", "Martin")
book1.get_details()

# Q5

class Account:
    def set_balance(self, balance):
        self.__balance = balance
    
    def withdraw(self):
        amt_withdraw = int(input("Enter amount to withdraw: "))
        self.__balance -= amt_withdraw
    
    def deposit(self):
        amt_deposit = int(input("Enter amount to deposit: "))
        self.__balance += amt_deposit
    
    def balance_show(self):
        print("Balance:", self.__balance)
    
account1 = Account()

account1.set_balance(1000)
account1.deposit()
account1.withdraw()
account1.balance_show()

# Q6

class Person:

    def get_age(self):
        self.age = int(input("Enter your age: "))

        if self.age > 0:
            print("Valid age entered")
        else:
            print("Invalid age")
            self.age = None

    def display_age(self):
        if self.age != None:
            print("Age:", self.age)

person1 = Person()

person1.get_age()
person1.display_age()

# Q7

class Student:

    def set_details(self, name, marks1, marks2, marks3):
        self.__name = name
        self.__marks1 = marks1
        self.__marks2 = marks2
        self.__marks3 = marks3

    def display_average(self):
        average = (self.__marks1 + self.__marks2 + self.__marks3) / 3
        print("Name:", self.__name)
        print("Average:", average)
        return average

    def display_grade(self):
        average = (self.__marks1 + self.__marks2 + self.__marks3) / 3

        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)

student1 = Student()

student1.set_details("Raj", 85, 78, 92)

student1.display_average()
student1.display_grade()