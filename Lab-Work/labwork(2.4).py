# Q1

for num in range(1, 21):
    if num % 4 == 0:
        continue
    print(num)
print()

# Q2

num = 1

while num <= 10:
    if num == 7:
        break
    print(num)
    num += 1

# Q3

vowels = "aeiouAEIOU"

string = ("Python")

for letter in string:
    if letter in vowels:
        continue
    print(letter)

# Q4

N = int(input("Enter a number for multiplication table: "))

for table in range(1, N + 1):
    for num in range(1, 11):
        multiple = table * num
        print(f"{table} * {num} = {multiple}")

# Q5

for row in range(1, 6):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()

# Q6

for row in range(1, 6):
    for num in range(5, 5 - row, -1):
        print(num, end=" ")
    print()

# Q7

for row in range(5, 0, -1):
    for num in range(row, 6):
        print(num, end=" ")
    print()

# Q8

for row in range(1, 6):
    for num in range(row, 6):
        print(num, end=" ")
    print()