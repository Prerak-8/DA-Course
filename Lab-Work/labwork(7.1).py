# Q1

import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Q2

import time

current_time = time.time()
print("Current Time (Epoch):", current_time)

# Q3

now = datetime.datetime.now()

print("DD-MM-YYYY:", now.strftime("%d-%m-%Y"))
print("MM/DD/YYYY:", now.strftime("%m/%d/%Y"))

print("24-hour time:", now.strftime("%H:%M:%S"))
print("12-hour time:", now.strftime("%I:%M:%S %p"))

# Q4 

date1 = datetime.datetime(2025, 4, 1)
date2 = datetime.datetime(2025, 4, 10)

days = date2 - date1
print("Days between:", days.days)

now = datetime.datetime.now()
new_date = now + datetime.timedelta(days=7)

print("Current date:", now)
print("Date after 7 days:", new_date)

# Q5

date_str = "15-02-2026"

convert_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")

print("Converted to datetime object:", convert_obj)

now = datetime.datetime.now()

convert_str = now.strftime("%Y-%m-%d %H:%M:%S")

print("Converted to string:", convert_str)

# Q6

start_time = time.time()

for i in range(1, 1000):
    pass

end_time = time.time()

execution_time = end_time - start_time

print("Execution time:", execution_time, "seconds")

# Q7

local_time = datetime.datetime.now()
utc_time = datetime.datetime.now(datetime.UTC)

print("Local time:", local_time)
print("UTC time:", utc_time)

# Q8

elapsed_time = 0
start_time = None

while True:
    choice = input("\nEnter start, stop, reset or exit: ").lower()

    if choice == "start":
        if start_time is None:
            start_time = time.time()
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    elif choice == "stop":
        if start_time is not None:
            end_time = time.time()
            elapsed_time += end_time - start_time
            start_time = None

            print("Stopwatch stopped.")
            print("Elapsed time:", elapsed_time, "seconds")
        else:
            print("Stopwatch is not running.")

    elif choice == "reset":
        elapsed_time = 0
        start_time = None
        print("Stopwatch reset.")

    elif choice == "exit":
        print("Stopwatch closed.")
        break

    else:
        print("Invalid choice.")

# Q9

seconds = int(input("Enter countdown time in seconds: "))

while seconds > 0:
    print(seconds)
    time.sleep(1)
    seconds -= 1

print("Time's up!")

# Q10

year = int(input("Enter a year: "))

try:
    datetime.datetime(year, 2, 29)
    print(year, "is a leap year.")

except ValueError:
    print(year, "is not a leap year.")

# Q11

date_str = input("Enter date in DD-MM-YYYY format: ")

date_obj = datetime.datetime.strptime(date_str, "%d-%m-%Y")

day_name = date_obj.strftime("%A")

print("Day of the week:", day_name)

# Q12

message = input("Enter reminder message: ")
seconds = int(input("Enter reminder time in seconds: "))

print("Reminder has been set.")

time.sleep(seconds)

print("Reminder:", message)