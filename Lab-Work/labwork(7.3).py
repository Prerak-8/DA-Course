# Q1

from functools import reduce
import uuid

print(uuid.uuid4())

namespace = uuid.NAMESPACE_DNS
print(uuid.uuid5(namespace, "Zack"))

# Q2

student1 = uuid.uuid4()
student2 = uuid.uuid4()
student3 = uuid.uuid4()

students = {
    "Student1": student1,
    "Student2": student2,
    "Student3": student3
}

print("Student IDs and UUIDs:")

for student_id, student_uuid in students.items():
    print(student_id, ":", student_uuid)

if len(set(students.values())) == len(students):
    print("All UUIDs are unique.")
else:
    print("Duplicate UUID found.")

# Q3

id_1 = uuid.uuid4()
id_2 = uuid.uuid4()

print("UUID 1:", id_1)
print("UUID 2:", id_2)

if id_1 == id_2:
    print("The UUIDs are equal.")
else:
    print("The UUIDs are not equal.")

# Q4

order1 = uuid.uuid4()
order2 = uuid.uuid4()
order3 = uuid.uuid4()

orders = {
    order1: "Laptop",
    order2: "Headphones",
    order3: "Keyboard"
}

print("E-commerce orders:")

for order_id, product in orders.items():
    print("Order ID:", order_id, "- Product:", product)

# Q5

num_list = [23, 58, 37, 48, 94, 18, 4, 7, 39]

ascending = sorted(num_list)
descending = sorted(num_list, reverse = True)

print("Ascending", ascending)
print("Descending", descending)

# Q6

words = ["Phone", "Car", "Switch", "Cable", "Balcony", "Window"]

word_sort = sorted(words, key = len)

print("Sorted by length:", word_sort)

letter_sort = sorted(words, key = lambda x: x[-1])

print("Sorted by last letter:", letter_sort)

# Q7

employees = [
    {"name": "Jacob", "age": 24},
    {"name": "Arthur", "age": 35},
    {"name": "Judas", "age": 21}
]

employees_sort = sorted(employees, key = lambda employee: employee["age"])

print("Employees sorted by age:")

for employee in employees_sort:
    print(employee)

# Q8

words = ["Phone", "Car", "Switch", "Cable", "Balcony", "Window"]

words_upper = list(map(lambda x: x.upper(), words))

print("Uppercase words:", words_upper)

# Q9

num_list = [23, 58, 37, 48, 94, 18, 4, 7, 39]

nums_square = list(map(lambda x: x * x, num_list))

print("Squared nums:", nums_square)

# Q10

prices = [5, 6.5, 13, 9, 2.8, 100]

prices_tax = list(map(lambda x: round(x * 1.18, 2), prices))

print("Final prices:", prices_tax)

# Q11

num_list = [23, 58, 37, 48, 94, 18, 4, 7, 39, 33, 38, 92]

num_even = list(filter(lambda x: x % 2 == 0, num_list))

print("Even nums:", num_even)

# Q12

words = ["Phone", "Car", "Switch", "Cable", "Balcony", "Window"]

words_filter = list(filter(lambda x: len(x) > 5, words))

print("Words with more than 5 characters:", words_filter)

# Q13

scores = [23, 58, 37, 40, 48, 94, 18, 4, 7, 39, 33, 38, 92]

scores_pass = list(filter(lambda x: x >= 40, scores))

print("Students passed with scores: ", scores_pass)

# Q14

nums = [23, 18, 4, 7]

nums_product = reduce(lambda x, y: x * y, nums)

print("Product of all nums:", nums_product)

# Q15

words = ["Phone", "Car", "Switch", "Cable", "Balcony", "Window"]

longest_word = reduce(lambda x, y: x if len(x) > len(y) else y, words)

print("Longest word:", longest_word)

# Q16

sentence = ["I", "am", "working", "on", "a", "project."]

sentence_join = reduce(lambda x, y: x + " " + y,sentence)

print("Whole sentence:", sentence_join)