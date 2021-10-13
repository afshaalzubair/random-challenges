"""
import random

numbers = [random.randint(-500,500),random.randint(-500,500),random.randint(-500,500),random.randint(-500,500),random.randint(-500,500),]
big = numbers[0]
print(numbers)

for i in numbers:
    if i < big:
        small = i
    if i > big:
        big = i
print("The smallest number in the list is " + str(small))
"""
# Above one is broken.
# Better version:

import random
numbers = [random.randint(-500,500),random.randint(-500,500),random.randint(-500,500),random.randint(-500,500),random.randint(-500,500)]
print(numbers)
print("Sorting...")
numbers.sort()
print(numbers)
print("The smallest number in the list is ", numbers[0])
