#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastint = abs(number) % 10
if number < 0:
    lastint = lastint * -1
if lastint > 5:
    print(f"Last digit of {number} is {lastint} and is greater than 5")
if lastint == 0:
    print(f"Last digit of {number} is {lastint} and is 0")
if lastint < 6 and lastint != 0:
    print(f"Last digit of {number} is {lastint} and is less than 6 and not 0")