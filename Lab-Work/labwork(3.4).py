# Q1

students =[
{"id": 101, "name": "Alice", "score": 85},
{"id": 102, "name": "Bob", "score": 78},
{"id": 103, "name": "Charlie", "score": 92}
]

for student in students:
    print(student["name"])

total = 0

for student in students:
    total += student["score"]

avg_score = total / len(students)

print(avg_score)

students.append({"id": 104, "name": "Tom", "score": 91})
print(students)

for student in students:
    if student["id"] == 102:
        student["score"] = 88
print(students)

for student in students:
    if student["name"] == "Charlie":
        students.remove(student)
        break
print(students)

for student in students:
    if student["score"] > 80:
        print(student["name"])

students.sort(key=lambda x: x["score"], reverse=True)
print(students)

highest = max(students, key=lambda x: x["score"])

print(highest)

for student in students:

    if student["score"] >= 90:
        grade = "A"
    elif student["score"] >= 80:
        grade = "B"
    else:
        grade = "C"

    print("Name:", student["name"],
          "| Score:", student["score"],
          "| Grade:", grade)

gradeA = 0
gradeB = 0
gradeC = 0

for student in students:

    if student["score"] >= 90:
        grade = "A"
        gradeA += 1

    elif student["score"] >= 80:
        grade = "B"
        gradeB += 1

    else:
        grade = "C"
        gradeC += 1

print("Grade A:", gradeA)
print("Grade B:", gradeB)
print("Grade C:", gradeC)

# dont understand panda frame what?

# csv not explained maybe

# re import?