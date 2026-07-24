# Q1

file = open("sample.txt", "w")
file.write("Python is a versatile programming language.")
file.close()

# Q2

file = open("sample.txt", "r")
print(file.read())
file.close()

file = open("sample.txt", "w")
file.write("Learning file handling in Python is fun!")
file.close()

# Q3

file = open("sample.txt", "r")

for line in file:
    print(line, end = "")

file.close()

# Q4

file = open("notes.txt", "w")
file.write("Line1: Python is easy to learn.\n")
file.write("Line2: It has numerous libraries.\n")
file.write("Line3: File handling is one of its features.")
file.close()

# Q5

file = open("notes.txt", "a")
file.write("\nLine 4: Python supports multiple modes of file handling.")
file.close()

# Q6

file = open("image2.png", "rb")
print(file.read())
file.close()

# Q7

count_lines = 0
count_words = 0
count_chars = 0

file = open("sample.txt", "r")

for line in file:
    count_lines += 1
    count_words += len(line.split())
    count_chars += len(line)

file.close()

print("Lines:", count_lines)
print("Words:", count_words)
print("Characters:", count_chars)

# Q8

file = open("sample.txt", "r")
print(file.read())
file.close()

file = open("sample.txt", "a")
file.write("\nThis file was last modified by adding this sentence.")
file.close()

# Q9

file = open("sample.txt", "r")

word = input("Enter word to find: ")

line_no = 1

for line in file:
    if word in line:
        print("Found at line:", line_no)
    line_no += 1

file.close()

# Q10

file = open("source.txt", "r")
content = file.read()
file.close()

file = open("backup.txt", "w")
file.write(content)
file.close()

# Q11

file = open("sample.txt", "r")
print(file.read())
file.close()

file = open("sample.txt", "w")
file.write("Hello World")
file.close()

file = open("sample.txt", "a")
file.write("\nNew Line")
file.close()

file = open("sample.txt", "r+")
print(file.read())
file.close()

file = open("sample.txt", "w+")
file.write("Python")
file.close()

file = open("sample.txt", "a+")
file.write("\nFile Handling")
file.close()