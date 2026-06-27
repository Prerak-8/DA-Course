# Q1

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_1 >= num_2:
    if num_1 >= num_3:
        max = num_1
    else: 
        max = num_3
else:
    if num_2 >= num_3:
        max = num_2
    else:
        max = num_3

print("Maximum number is: ", max)
print()

# Q2

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_1 <= num_2:
    if num_1 <= num_3:
        min = num_1
    else: 
        min = num_3
else:
    if num_2 <= num_3:
        min = num_2
    else:
        min = num_3

print("Minimum number is: ", min)
print()

# Q3

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
num_4 = int(input("Enter fourth number: "))

if num_1 >= num_2:
    if num_1 >= num_3:
        if num_1 >= num_4:
            max = num_1
        else:
            max = num_4
    else: 
        if num_3 >= num_4:
            max = num_3
        else:
            max = num_4
else:
    if num_2 >= num_3:
        if num_2 >= num_4:
            max = num_2
        else:
            max = num_4
    else:
        if num_3 >= num_4:
            max = num_3
        else:
            max = num_4

print("Maximum number is: ", max)
print()

# Q4

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter a mathematical operator: ")

match operator:
    case "+":
       result = num1 + num2
    case "-":
       result = num1 - num2
    case "*":
       result = num1 * num2
    case "/":
       result = num1 / num2
    case _:
        print("Enter a valid operator")
        result = None

print("Result =", result)
print()

# Q5

print("------ MENU ------")
print("1. Pizza")
print("2. Sandwich")
print("3. Burger")

order = int(input("Select your food item: "))

match order:
    case 1:
        print("\nPizza Menu")
        print("1. Thin Crust")
        print("2. Cheese Burst")
        print("3. Fresh Dough")

        pizza = int(input("Select Pizza Type: "))

        match pizza:
            case 1:
                print("You have ordered a Thin Crust Pizza.")
            case 2:
                print("You have ordered a Cheese Burst Pizza.")
            case 3:
                print("You have ordered a Fresh Dough Pizza.")
            case _:
                print("Invalid Pizza choice.")

    case 2:
        print("\nSandwich Menu")
        print("1. Grilled Cheese")
        print("2. Grilled Vegetable")
        print("3. Grilled Club")

        sandwich = int(input("Select Sandwich Type: "))

        match sandwich:
            case 1:
                print("You have ordered a Grilled Cheese Sandwich.")
            case 2:
                print("You have ordered a Grilled Vegetable Sandwich.")
            case 3:
                print("You have ordered a Grilled Club Sandwich.")
            case _:
                print("Invalid Sandwich choice.")

    case 3:
        print("\nBurger Menu")
        print("1. Spicy Burger")
        print("2. Cheesy Burger")
        print("3. Mexican Burger")

        burger = int(input("Select Burger Type: "))

        match burger:
            case 1:
                print("You have ordered a Spicy Burger.")
            case 2:
                print("You have ordered a Cheesy Burger.")
            case 3:
                print("You have ordered a Mexican Burger.")
            case _:
                print("Invalid Burger choice.")

    case _:
        print("Invalid food item selection.")
print()

# Q6

print("--- Telecom calling language options ---")
print("1. English")
print("2. Hindi")
print("3. Gujarati")

language = int(input("Select your prefered language: "))

match language:
    case 1:
        print("1. New Product details")
        print("2. Complaints")
        print("3. delivery update")

        english = int(input("Select: "))

        match english:
            case 1:
                print("You have contacted for New Product details.")
            case 2:
                print("You have contacted for Complaints")
            case 3:
                print("You have contacted for delivery update")
            case _:
                print("Invalid choice.")

    case 2:
        print("1. नए उत्पाद की जानकारी")
        print("2. शिकायतें")
        print("3. डिलीवरी अपडेट")

        hindi = int(input("चुनें: "))

        match hindi:
            case 1:
                print("आपने नए उत्पाद की जानकारी के लिए संपर्क किया है।")
            case 2:
                print("आपने शिकायत दर्ज करने के लिए संपर्क किया है।")
            case 3:
                print("आपने डिलीवरी अपडेट के लिए संपर्क किया है।")
            case _:
                print("अमान्य विकल्प।")

    case 3:
        print("1. નવી પ્રોડક્ટની માહિતી")
        print("2. ફરિયાદો")
        print("3. ડિલિવરી અપડેટ")

        gujarati = int(input("પસંદ કરો: "))

        match gujarati:
            case 1:
                print("તમે નવી પ્રોડક્ટની માહિતી માટે સંપર્ક કર્યો છે.")
            case 2:
                print("તમે ફરિયાદ માટે સંપર્ક કર્યો છે.")
            case 3:
                print("તમે ડિલિવરી અપડેટ માટે સંપર્ક કર્યો છે.")
            case _:
                print("અમાન્ય પસંદગી.")
    case _:
        print("Invalid language selection.")