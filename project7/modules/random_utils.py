import random

# Random data generation functions.

def random_num():
    start_range = int(input("Enter number for starting a range: "))
    end_range = int(input("Enter number for ending a range: "))

    random_num = random.randint(start_range, end_range)

    print("The random number from your range is: ", random_num)
    print("--------------------------\n")

def random_list():
    words_list = []

    for i in range(1, 11):
        words = input("Enter words to create a random list: ")
        words_list.append(words)

    random_words = random.sample(words_list, len(words_list))

    print("List of random words: ", random_words)
    print("--------------------------\n")

def random_password():
    cha_pass = "aqwertyuioplsdfghjkmnbvcxz1234567890"

    lenght_pass = int(input("Enter password length: "))

    password = []

    for i in range(lenght_pass):
        random_ch = random.choice(cha_pass)
        password.append(random_ch)

    print("Generated Password:", "".join(password))
    print("--------------------------\n")

def random_otp():
    ch_num = "1234567890"

    otp = []
    
    for i in range(6):
        random_ch = random.choice(ch_num)
        otp.append(random_ch)

    print("Generated OTP:", "".join(otp))
    print("--------------------------\n")