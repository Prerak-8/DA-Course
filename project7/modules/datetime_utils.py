import datetime
import time

# Date and time utility functions.

def current_time_date():
    now = datetime.datetime.now()

    print("Current Date and Time:", now)
    print("--------------------------\n")

def diff_bet_dates():
    d1 = input("Enter the first date (YYYY-MM-DD): ")
    d2 = input("Enter the second date (YYYY-MM-DD): ")

    date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

    diff_dates = abs(date1 - date2)

    print("Difference:", diff_dates)
    print("--------------------------\n")

def format_date():
    time_now = datetime.datetime.now()

    custom_format = time_now.strftime("%d/%m/%Y %H:%M:%S")

    print("Custom formatted date:", custom_format)
    print("--------------------------\n")

def stopwatch():
    elapsed_time = 0
    start_time = None

    while True:
        options = input("Type start, stop, reset and exit to operate stopwatch: ")

        if options == "start":
            if start_time is None:
                start_time = time.time()
                print("Stopwatch started.")
            else:
                print("Stopwatch is already running.")

        elif options == "stop":
            if start_time is not None:
                end_time = time.time()
                elapsed_time += end_time - start_time
                start_time = None

                print("Stopwatch stopped!")
                print("Elapsed time:", elapsed_time, "seconds")
            else:
                print("Stopwatch is not running.")
        elif options == "reset":
            elapsed_time = 0
            start_time = None
            print("Stopwatch reset complete.")
        elif options == "exit":
            break
        else:
            print("Invalid option.")
        print("--------------------------\n")

def countdown_timer():
    count_duration = int(input("Enter time in seconds for countdown: "))

    while count_duration >= 0:
        print(count_duration)
        if count_duration == 0:
            break
        time.sleep(1)
        count_duration -= 1

    print("Time's up.")
    print("--------------------------\n")