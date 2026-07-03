print("Welcome to our Company's Personal Data Collector")

name = input("Please enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in centimeters: "))
fav_num = int(input("Enter your favourite number: "))
fav_color = input("Enter your favourite color: ")

print()
print("Alright thank you for your participation. The information collected from you is displayed below: ")
print()

print(f"Name: {name} (Memory Address: {id(name)}, Type: {type(name)})")
print(f"Age: {age} (Memory Address: {id(age)}, Type: {type(age)})")
print(f"Height: {height} (Memory Address: {id(height)}, Type: {type(height)})")
print(f"Favourite Number: {fav_num} (Memory Address: {id(fav_num)}, Type: {type(fav_num)})")
print(f"Favourite Color: {fav_color} (Memory Address: {id(fav_color)}, Type: {type(fav_color)})")
print()

current_year = 2026
birth_year = (current_year) - (age)

print()
print(f"{name} your birth year is: {birth_year} (it was calculated on the basis of your age entered above)")
print()

print(f"Thank you {name} for using our Company's Personal Data Collector.")
print("Have a nice day.")
print("Bye!")