# Q1 

while True:
    num = int(input("Enter a number: "))

    if num == 0:
        break
print()

# Q2

for number in range(1, 11):
    square = number * number
    print(f"Square of {number} is: {square}")
print()

# Q3

num = 1

while num <= 50:
    if num % 2 == 0:
        print(num)
    num += 1

# Q4

for num in range(1, 21):
    if num % 2 == 1:
        print(num)

# Q5

for multiple in range(5, 51, 5):
    print(multiple)

# Q6 

for num in range(10, 0, -1):
    print(num)

# Q7

for num in range(1, 51):
    if num % 2 == 0 and num % 3 == 0:
        print("Divisible by both:", num)
    elif num % 2 == 0:
        print("Divisible by 2:", num)
    elif num % 3 == 0:
        print("Divisible by 3:", num)