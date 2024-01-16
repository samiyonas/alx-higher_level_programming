#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tmp = number
if tmp < 0:
    tmp = tmp * -1
last_digit = tmp % 10
if number < 0:
    print(f"Last digit of {number} is -{last_digit} and "
          f"is less than 6 and not 0")
elif number > 0 and last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and "
          f"is greater than 5")
elif number > 0 and last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and "
          f"is less than 6 and not 0")
else:
    print("Last digit of {} is {} and is zero".format(number, last_digit))
