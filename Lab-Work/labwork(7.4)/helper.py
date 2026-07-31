def calculation(num):
    multiply = num * 5
    divide = num / 4
    add = num + 22
    subtract = num - 7

    return multiply, divide, add, subtract


if __name__ == "__main__":
    result = calculation(25)
    print("Calculation result:", result)