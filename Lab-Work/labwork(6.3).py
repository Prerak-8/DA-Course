# Q1

try:
    num_user = int(input("Enter a number: "))

    if num_user < 0:
        raise ValueError("Number cannot be negative.")

    print("Number added successfully.")

except ValueError as e:
    print(e)

# Q2

def check_even(value):

    if type(value) != int:
            raise TypeError("The input is incorrect. Please enter a number.")
    
    elif value % 2 != 0:
        raise ValueError("Number is odd")

    else:
        print(f"Number {value} is even.")

try:
    check_even(21)
except Exception as e:
    print(e)

try:
    check_even("Abc")
except Exception as e:
    print(e)

try:
    check_even(14)
except Exception as e:
    print(e)

# Q3

try:
    age = int(input("Enter your age: "))

    assert age > 18, "Age must be above 18."

    print(f"{age} is valid.")

except AssertionError as e:
    print(e)

except ValueError:
    print("Invalid age.")

# Q4

def check_palindrome(text):

    assert text != "", "Input text cannot be empty."

    rev_text = text[::-1]

    if rev_text == text:
        print(f"The word {text} is a palindrome.")

    else:
        print(f"The word {text} is not a palindrome.")

try:
    check_palindrome("level")
except Exception as e:
    print(e)

try:
    check_palindrome("Laser")
except Exception as e:
    print(e)

try:
    check_palindrome("")
except AssertionError as e:
    print(e)

# Q5

class InsufficientBalanceError(Exception):
    pass

class Bank:

    def withdraw(self, amount):

        balance = 600

        if amount > balance:
            raise InsufficientBalanceError("You don't have enough balance to withdraw.")

        else:
            rem_balance = balance - amount
            print("Remaining balance:", rem_balance)

try:
    obj1 = Bank()
    obj1.withdraw(800)

except InsufficientBalanceError as e:
    print(e)

try:
    obj1 = Bank()
    obj1.withdraw(300)

except InsufficientBalanceError as e:
    print(e)

# Q6

class InvalidEmailError(Exception):
    pass

class Email:

    def validate_email(self, email):

        if "@" not in email:
            raise InvalidEmailError("Invalid email.")

        elif ".com" not in email and ".org" not in email:
            raise InvalidEmailError("Invalid email.")

        else:
            print(f"{email} is valid.")

try:
    obj1 = Email()
    obj1.validate_email("BlazingImpala@gmail.com")

except InvalidEmailError as e:
    print(e)

try:
    obj1 = Email()
    obj1.validate_email("FordMustang")

except InvalidEmailError as e:
    print(e)

# Q7

class InvalidGradeError(Exception):
    pass

try:
    grade = input("Enter grade: ")

    assert grade != "", "Grade cannot be empty."

    grade = int(grade)

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")

    if grade < 40:
        raise InvalidGradeError("Student has failed.")

    print("Student has passed.")

except (AssertionError, ValueError, InvalidGradeError) as e:
    print(e)

# Q8

class HighTemperatureError(Exception):
    pass

temp = input("Enter temperature: ")

try:
    try:
        temp = float(temp)
    except ValueError:
        raise TypeError("Temperature must be a number.")

    assert -273 <= temp <= 10000, "Temperature out of range."

    if temp > 1000:
        raise HighTemperatureError("Temperature is too high.")

    print("Temperature is valid.")

except (TypeError, AssertionError, HighTemperatureError) as e:
    print(e)