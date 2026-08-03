from modules.datetime_utils import current_time_date, diff_bet_dates, format_date, stopwatch, countdown_timer
from modules.math_utils import cal_factorial, compound_interest, trigo_cal, area_geo
from modules.random_utils import random_num, random_list, random_password, random_otp
from modules.uuid_utils import generate_uuid
from modules.file_utils import create_file, write_file, read_file, append_file
import modules.datetime_utils as datetime_utils
import modules.math_utils as math_utils
import modules.random_utils as random_utils
import modules.uuid_utils as uuid_utils
import modules.file_utils as file_utils

# Main menu-driven program for the Multi-Utility Toolkit.

def main():
    print("********************************")
    print("Welcome to Multi-Utility Toolkit")
    print("********************************")

    def explore_attributes():
        print("Explore Module Attributes:")

        mod_name = input("Enter module name to explore: ").lower()

        modules = {
            "datetime": datetime_utils,
            "math": math_utils,
            "random": random_utils,
            "uuid": uuid_utils,
            "file": file_utils
        }

        if mod_name in modules:
            print("Available Attributes:", dir(modules[mod_name]))
        else:
            print("Module not found.")

        print("--------------------------\n")


    while True:
        print("Choose an option:") 
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit\n")

        choice_main = int(input("Enter your choice: "))
        print()

        match choice_main:
            case 1:
                while True:
                    print("Datetime and Time Operations:")
                    print("1. Display current date and time")
                    print("2. Calculate difference between two dates/ times")
                    print("3. Format date into custom format")
                    print("4. Stopwatch")
                    print("5. Countdown Timer")
                    print("6. Back to Main menu\n")

                    date_choice = int(input("Enter your choice: "))
                    print()

                    match date_choice:
                        case 1:
                            current_time_date()

                        case 2:
                            diff_bet_dates()

                        case 3:
                            format_date()

                        case 4:
                            stopwatch()

                        case 5:
                            countdown_timer()

                        case 6:
                            break

                        case _:
                            print("Invalid choice entered. Please enter a valid choice.\n")

            case 2:
                while True:
                    print("Mathematical Operations:")
                    print("1. Calculate Factorial")
                    print("2. Solve Compound Interest")
                    print("3. Trigonometric Calculations")
                    print("4. Area of Geometric Shapes")
                    print("5. Back to Main menu\n")

                    math_choice = int(input("Enter your choice: "))
                    print()

                    match math_choice:
                        case 1:
                            cal_factorial()

                        case 2:
                            compound_interest()

                        case 3:
                            trigo_cal()

                        case 4:
                            area_geo()
                            
                        case 5:
                            break

                        case _:
                            print("Invalid choice entered. Please enter a valid choice.\n")

            case 3:
                while True:
                    print("Random Data Generation :")
                    print("1. Generate Random Number")
                    print("2. Generate Random List")
                    print("3. Create Random password")
                    print("4. Generate Random OTP")
                    print("5. Back to Main menu\n")

                    random_choice = int(input("Enter your choice: "))
                    print()

                    match random_choice:
                        case 1:
                            random_num()

                        case 2:
                            random_list()

                        case 3:
                            random_password()

                        case 4:
                            random_otp()
                            
                        case 5:
                            break

                        case _:
                            print("Invalid choice entered. Please enter a valid choice.\n")

            case 4:
                generate_uuid()

            case 5:
                while True:
                    print("File Operations:")
                    print("1. Create a new file")
                    print("2. Write to a file")
                    print("3. Read from a file")
                    print("4. Append to a file")
                    print("5. Back to Main menu\n")

                    file_choice = int(input("Enter your choice: "))
                    print()

                    match file_choice:
                        case 1:
                            create_file()

                        case 2:
                            write_file()

                        case 3:
                            read_file()

                        case 4:
                            append_file()
                            
                        case 5:
                            break

                        case _:
                            print("Invalid choice entered. Please enter a valid choice.\n")

            case 6:
                explore_attributes()

            case 7:
                break

            case _:
                print("Invalid choice. Please select valid option.")

    print("**********************************************")
    print("Thank you for using the Multi-Utility Toolkit!")
    print("**********************************************")

if __name__ == "__main__":
    main()