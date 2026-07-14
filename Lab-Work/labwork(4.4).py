# Q1

arr = [5, 7, 3, 9, 12]
count = 0

for elements in arr:
    count += 1

print("Length of aaray:", count)

# Q2

arr = [9, 17, 13, 6, 12]
count = 0
total = 0

for elements in arr:
    count += 1
    total += elements

avg = total / count

print("Average:", avg)

# Q3

arr_1 = [4, 6, 15, 23]
arr_2 = [5, 9, 12, 34]

arr_combined = arr_1 + arr_2

print(arr_combined)

# or

arr_1 = [4, 6, 15, 23]
arr_2 = [5, 9, 12, 34]

arr_combined = []

for element in arr_1:
    arr_combined.append(element)

for element in arr_2:
    arr_combined.append(element)

print(arr_combined)

# Q4

arr = []

for num in range(1,11):
    arr.append(num)

for num in arr:
    multiply = num * 2
    print(multiply)

# Q5

arr = [3, 5, 6, 8, 11, 14, 15, 17, 19]

number = int(input("Enter a num: "))

if number in arr:
    location = arr.index(number)
    print(f"The number is found at index {location}.")
else:
    print("Number not found.")

# Q6

size = int(input("Enter array size: "))

arr = []

for i in range(size):
    arr.append(int(input(f"a[{i}] = ")))

print("Even numbers:")

for num in arr:
    if num % 2 == 0:
        print(num)

print("Odd numbers:")

for num in arr:
    if num % 2 == 1:
        print(num)

# Q7

arr = [5, 8, 11, 15, 18, 20, 25, 30]

print("First five elements:")

for i in range(5):
    print(arr[i])

print("Alternate elements:")

for i in range(0, 8, 2):
    print(arr[i])

# Q8

arr = [5, 8, 11, 15, 18, 20, 25]

first = arr[0]
last = arr[-1]
middle = arr[len(arr) // 2]

print("First element:", first)
print("Middle element:", middle)
print("Last element:", last)