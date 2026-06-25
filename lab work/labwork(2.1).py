# Q1

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("It's an even number")
else: 
    print("It's an odd number")
print()

# Q2

age = int(input("Enter your age: "))

if age <= 12:
    print("You are a Child")
else:
    if age <= 19:
        print("You are a Teenager")
    else:
        if age <= 59:
            print("You are Adult")
        else:
            print("You are a Senior")
print()

# Q3

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)

elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)

else:
    print("Largest number is:", num3)   
print()
# Q4 

num = int(input("Enter a number: "))

if num > 0:
    print("It is a positive number")
elif num < 0:
    print("It is a negative number")
else:
    print("It is a neutral number")