def count(string):
    vowels = "AEIOUaeiou"
    vowel_count = 0

    for character in string:
        if character in vowels:
            vowel_count += 1

    return vowel_count