import random

def pin_generator(length):
    pin = ""
    for i in range(length):
        digit = random.randint(0, 9)
        pin = pin + str(digit)
    return pin

print(pin_generator(5))