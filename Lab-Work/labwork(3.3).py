# Q1

integer = {1, 2, 3, 4, 5}

integer.add(6)
print(integer)

integer.remove(3)
print(integer)

if 2 in integer:
    print("2 is present")
else:
    print("2 is not present")

# Q2

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

Union = set_a.union(set_b)
print(Union)

Intersection = set_a.intersection(set_b)
print(Intersection)

Difference = set_a.difference(set_b)
print(Difference)

# Q3

student = {"name": "Alice", "age": 20, "grade": "A"}

print(student.keys())
print(student.values())

student.update({"city": "Delhi"})
print(student)

student.update({"age": 21})
print(student)

del student["grade"]
print(student)

# Q4

keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']

student = {}

student[keys[0]] = values[0]
student[keys[1]] = values[1]
student[keys[2]] = values[2]

print(student)

# Q5

num = '123'

integer = int(num)
print(integer)

list_num = [1, 2, 3]

tuple_convert = tuple(list_num)
print(tuple_convert)

tuple_num = (4, 5, 6)

list_convert = list(tuple_num)
print(list_convert)

pairs = [(1,'A'), (2, 'B')]

dictionary_convert = dict(pairs)
print(dictionary_convert)

# Q6

del list_num[1]
print(list_num)