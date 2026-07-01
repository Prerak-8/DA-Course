# Q1

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"Hello, {last_name}, {first_name}!")

# Q2

sentence = "The price of {item} is {price} dollars."

sentence = sentence.replace("{item}", "apple")
sentence = sentence.replace("{price}", "5.50")

print(sentence)

# Q3

user_input = input("Enter a string: ")
reverse = user_input[::-1]

print(reverse)

if user_input == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

# Q4

user_input = input("Enter a string: ")

print(user_input.upper())

print(user_input.lower())

print(user_input.title())

# Q5

sentence_1 = "Machine Learning and AI are trending."

print(sentence_1.find("AI"))

replace = sentence_1.replace("AI", "Artificial Intelligence")

print(replace)

sentence_2 = "data data mining and big data"

count = sentence_2.count("data")
print(count)

# Q6

fruits = "apple,banana,grapes"

print(fruits.split(","))

words = ["Python", "is", "awesome"] 

print(" ".join(words))

multiline = "I am in park. The park has many trees. The benches here are comfortable."

print(multiline.split("."))

# Q7

string = "Hello World"

if string.startswith("Hello") and string.endswith("World"):
    print("Yes")
else:
    print("No")

word = "Data123#Science!"

result = ""

for ch in word:
    if ch.isalpha():
        result += ch

print(result)

word_1 = "Python"

print(word_1[::-1])