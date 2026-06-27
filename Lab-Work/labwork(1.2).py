# Q1

user_input = input("Enter value: ")

convert_to_int = int(user_input)
convert_to_float = float(user_input)
convert_to_bool = bool(user_input)

print(f"Integer value: {convert_to_int}, Type: {type(convert_to_int)}")
print(f"Float value: {convert_to_float}, Type: {type(convert_to_float)}")
print(f"Boolean value: {convert_to_bool}, Type: {type(convert_to_bool)}")
print()

# Q2

exam_percentage = float(input("Enter your exam percentage: "))

convert_int = int(exam_percentage)

print(f"Number {exam_percentage} has a decimal value and is called floating-point number, but {convert_int} does not have decimal value and is known as integer number.")
print()

# Q3

user_input1 = int(input("Do you consume milk once daily? Enter 1 for True or 0 for False: "))

milk_consumption = bool(user_input1)
boolean_to_integer = int(milk_consumption)
boolean_to_string = str(milk_consumption)

print(f"I consume milk {boolean_to_integer} times that is {boolean_to_string}")
print()

# Q4

my_int = 25
print("- Integer -")
print(f"Value: {my_int}")
print(f"Type: {type(my_int)}")
print(f"Memory Address: {id(my_int)}\n")

my_float = 9.99
print("- Float -")
print(f"Value: {my_float}")
print(f"Type: {type(my_float)}")
print(f"Memory Address: {id(my_float)}\n")

my_str = "Python"
print("- String -")
print(f"Value: '{my_str}'")
print(f"Type: {type(my_str)}")
print(f"Memory Address: {id(my_str)}\n")

my_bool = True
print("- Boolean -")
print(f"Value: {my_bool}")
print(f"Type: {type(my_bool)}")
print(f"Memory Address: {id(my_bool)}\n")

my_list = [1, 2, 3]
print("- List -")
print(f"Value: {my_list}")
print(f"Type: {type(my_list)}")
print(f"Memory Address: {id(my_list)}\n")

my_tuple = (10, 20, 30)
print("- Tuple -")
print(f"Value: {my_tuple}")
print(f"Type: {type(my_tuple)}")
print(f"Memory Address: {id(my_tuple)}\n")

my_dict = {"name": "abc", "age": 20}
print("- Dictionary -")
print(f"Value: {my_dict}")
print(f"Type: {type(my_dict)}")
print(f"Memory Address: {id(my_dict)}\n")

# Q5

No_of_fan = 1
No_of_kitchen = 1

id_fan = id(No_of_fan)
id_kitchen = id(No_of_kitchen)

print(f"Id of fan: {id_fan}")
print(f"Id of kitchen: {id_kitchen}")

if id_fan == id_kitchen:
    print("Their id's are same!")
else:
    print("Their id's are different")    
print()

print("- Modified variable -")

No_of_fan = 2

id_fan_new = id(No_of_fan)

print(f"New Id of fan: {id_fan_new}")
print(f"Id of kitchen: {id_kitchen}")

if id_fan_new == id_kitchen:
    print("Their id's are still the same!")
else:
    print("Their id's are now different!")

# done    