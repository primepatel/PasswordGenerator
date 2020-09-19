import random

LOWER_CASES = [chr(i) for i in range(65, 91)]
UPPER_CASES = [chr(i) for i in range(97, 123)]
SPECIAL_CHARS = ['!', '@', '#', '$', '&', '?', '.']
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def pass_generator(length = 12, type="d"):
    if type == "d":
        SET = [LOWER_CASES, UPPER_CASES, SPECIAL_CHARS, NUMBERS]
    elif type == "an":
        SET = [LOWER_CASES, UPPER_CASES, NUMBERS]
    elif type == "p":
        SET = [NUMBERS]
    password = ""
    for i in range(length):
        lst = random.choice(SET)
        char = random.choice(lst)
        password = password + char
    return password

# Password Generator
# print(pass_generator(8))
# print(pass_generator(8, "an"))
# print(pass_generator(8, "p"))