# Q1 

arr = [1, 2, 3, 4, 5]

for num in arr:
    print(num)

# Q2

arr = [3, 6, 8, 9]
sum = 0

for num in arr:
    sum += num

print("Sum", sum)

# Q3

arr = [5, 6, 7, 9]

arr.insert(2, 8)

print(arr)

# Q4

arr = [5, 7, 8, 10, 12]

arr.remove(8)

print(arr)

# Q5

arr = [3, 5, 7, 10, 13]

arr[3] = 12

print(arr)

# Q6

arr = [5, 7, 8, 10, 12]

search = 10

if search in arr:
    print("Index:", arr.index(search))
else:
    print("Element not found")

# Q7

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

arr3 = arr1 + arr2

print(arr3)