# Q1

import math

print(math.sqrt(9))
print(math.factorial(5))
print(math.pow(2, 2))

# Q2

r = int(input("Enter radius: "))
area_circle = math.pi * math.pow(r, 2)

print("Area of circle:", area_circle)

log_num = int(input("Enter a positive number for natural log: "))
nat_log = math.log(log_num)

print("Natural log:", nat_log)

# Q3

angle = 30
ladder_length = 10

height = ladder_length * math.sin(math.radians(angle))
distance = ladder_length * math.cos(math.radians(angle))
ratio = math.tan(math.radians(angle))

print("Height reached on wall:", height)
print("Distance from wall:", distance)
print("Height-to-distance ratio:", ratio)

# Q4

ceiling_val = math.ceil(4.6)
floor_val = math.floor(4.8)
absolute_val = math.fabs(-11)

print("Ceiling value:", ceiling_val)
print("Floor value:", floor_val)
print("Absolute:", absolute_val)

# Q5

import random 

num_list = []

for i in range(10):
    num = random.randint(1, 100)
    num_list.append(num)

print(num_list)

# Q6

die_roll = random.randint(1, 6)

print("Die rolled num:", die_roll)

num = [23, 55, 63, 86, 49 ,90, 26, 58, 29]

random.shuffle(num)

print(num)

# Q7

list_games = ["Football", "Tennis", "Chess", "Basketball", "Pool"]

print(random.choice(list_games))

# Q8

move_list = ["rock", "paper", "scissor"]

computer_played = random.choice(move_list)

player_played = input("Enter your move: ")

print(f"Computer played {computer_played}")

if computer_played == player_played:
    print("Tie.")
elif player_played == "rock" and computer_played == "scissor":
    print("You win.")
elif player_played == "paper" and computer_played == "rock":
    print("You win.")
elif player_played == "scissor" and computer_played == "paper":
    print("You win.")
else:
    print("you lose.")