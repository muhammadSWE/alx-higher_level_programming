#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number
if n > 0:
    if n % 10 > 5:
        print(f"Last digit of {n} is {n % 10} and is greater than 5")
    elif n % 10 == 0:
        print(f"Last digit of {n} is {n % 10} and is 0")
    elif n % 10 < 6 and n % 10 != 0:
        print(f"Last digit of {n} is {n % 10} and is less than 6 and not 0")
elif n < 0:
    n = -n
    if n % 10 == 0:
        print(f"Last digit of -{n} is {n % 10} and is 0")
    else:
        print(f"Last digit of -{n} is -{n % 10} and is less than 6 and not 0")
else:
    print(f"Last digit of {n} is {n % 10} and is 0")
