# Q1

def factorial(num):
    if num < 0:
        print("Invalid number")
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(6))

# Q2

def fibonnaci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonnaci(num - 1) + fibonnaci(num - 2)
    
print(fibonnaci(5))
print(fibonnaci(7))
print(fibonnaci(8))
print(fibonnaci(10))

# Q3

string_input = input("Enter a string: ")

def reverse(word):
    if word == "":
        return ""
    else:
        return word[-1] + reverse(word[:-1])
    
print(reverse(string_input))

# Q4

num = int(input("Enter a number: "))

def sum_digits(num):
    if num < 0:
        print("Invalid input")
        return

    elif num < 10:
        return num

    total = (num % 10) + sum_digits(num // 10)

    if total < 10:
        return total
    else:
        return sum_digits(total)

print("Single digit sum:", sum_digits(num))

# Q5

start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))

def is_prime(num, divisor = 2):
    if num < 2:
        return False

    if divisor == num:
        return True

    if num % divisor == 0:
        return False

    return is_prime(num, divisor + 1)


def prime_num(start, end):
    if start > end:
        return

    if is_prime(start):
        print(start)

    prime_num(start + 1, end)

print("Prime numbers: ")
prime_num(start_num, end_num)

# Q6

num_list = [3, 5, 7, 9, 11]

square = list(map(lambda x: x ** 2, num_list))

print(square)

# Q7

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

odd_filter = list(filter(lambda x: x % 2 == 1, numbers))

print(odd_filter)

# Q8

largest = lambda a, b, c: max(a, b, c)

print(largest(4, 7, 9))

# Q9

count = 0

def word():
    global count

    print("hello")
    count += 1

word()
word()
word()

print(count)

# Q10

total = 0

def total_sum(*numbers):
    global total 
    for num in numbers:
        total += num

total_sum(1, 5, 7)

print(total)

# Q11

username = "knight_23"

def update_username():
    global username  
    username = input("Enter a username: ") 

print("Current username:", username)

update_username()
print("Updated username:", username)

# Q12

count = 0

def default_count():
    global count
    count = 5

def increase_count():
    global count
    inc_in_count = int(input("Enter number: "))
    count += inc_in_count

default_count()
increase_count()

print("Updated count: ", count)

# Q13

value = 2

def test():
    value = 4
    print("Inside value:", value)

test()
print("Outside value:", value)

# Q14

num_list = [5, 8, 11, 15, 18, 20]

def calculation(numbers):
    sum = 0

    for num in numbers:
        sum += num
    print("Sum:", sum)

    maximum = max(numbers)
    print("Maximum:", maximum)

    minimum = min(numbers)
    print("Minimum:", minimum)

calculation(num_list)

# Q15

def rectangle():
    length = 5
    breadth = 6

    area = length * breadth
    perimeter = 2 * (length + breadth)

    return area, perimeter

area, perimeter = rectangle()

print("Area:", area)
print("Perimeter:", perimeter)

# Q16

def caluclation():
    num = 5

    square = num ** 2
    cube = num ** 3

    return square, cube

square, cube = caluclation()

print("Square:", square)
print("Cube:", cube)

# Q17

def split_string(text):
    vowels = ""
    remaining = ""

    for ch in text:
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            remaining += ch

    return vowels, remaining

vowel_part, remaining_part = split_string("Programming")

print("Vowels:", vowel_part)
print("Remaining:", remaining_part)

# Q18

def separate_words(words):
    vowel_words = []
    consonant_words = []

    for word in words:
        if word[0].lower() in "aeiou":
            vowel_words.append(word)
        else:
            consonant_words.append(word)

    return vowel_words, consonant_words

word_list = ["Apple", "Call", "Orange", "Cat", "Umbrella", "Dog"]

vowels, consonants = separate_words(word_list)

print("Words starting with vowels:", vowels)
print("Words starting with consonants:", consonants)