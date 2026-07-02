# Q1

fruits = ["apple", "banana", "grape", "papaya", "orange"]

print(fruits[1])
print(fruits[4])

fruits.append("mango")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)

# Q2

num = (1, 2, 3, 4, 5)

third_item = num[2]
print("Third item: ", third_item)

num[1] = 7

# Tuples are immutable, so their elements cannot be modified.
# A TypeError is displayed when you try to change it.

# Q3

word_t = ("Car", "Bus", "Bike")
word_l = ["Car", "Bus", "Bike"]

word_l[0] = "Plane"
print(word_l)

word_t[0] = "Plane"
print(word_t)

# Tuples are immutable, so changing an element shows a TypeError.

# Q4

squares = [x**2 for x in range(1, 11)]
print(squares)

even_list = [x for x in range(1, 21) if x % 2 == 0]
print(even_list)

words = ["hello", "WORLD", "PyThOn"]

lower_case = [word.lower() for word in words]
print(lower_case)