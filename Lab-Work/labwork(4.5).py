# Q1

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Tabular format:")

for row in arr:
    for num in row:
        print(num, end = " ")
    print()

# Q2

arr = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Transpose 3x2 matrix:")

for j in range(3):          
    for i in range(2):      
        print(arr[i][j], end=" ")
    print()

# Q3

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_sum = 0

for row in arr:
    for num in row:
        matrix_sum += num
        
print("Sum:", matrix_sum)

# Q4

arr = [
    [16, 12, 31],
    [19, 51, 64],
    [21, 17, 95]
]

maximum = arr[0][0]
minimum = arr[0][0]

for row in arr:
    for num in row:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

print("Maximum:", maximum)
print("Minimum:", minimum)

# Q5

arr = [16, 2, 14, 9, 1, 4, 11, 7, 5]

arr.sort()

print(arr)

# Q6

tuple_list = [
    (3, 11, 9),
    (2, 5, 15),
    (17, 3, 8)
    ]

sorting = sorted(tuple_list, key=lambda x: x[1])

print(sorting)

# Q7

students = [
    {"name": "Rahul", "marks": 82},
    {"name": "Amit", "marks": 65},
    {"name": "Raj", "marks": 91}
]

sorting = sorted(students, key=lambda x: x["marks"])

print(sorting)

# Q8

numbers = [7, 3, 9, 2, 5]

print("Original List:", numbers)

new_list = sorted(numbers)
print("Using sorted():", new_list)
print("Original after sorted():", numbers)

numbers.sort()
print("Using sort():", numbers)