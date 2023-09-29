"""
Description: Python Module 3 Import Statements and Built-in Functions 
Author: Raymund Estillore
Date: 2023/09/26
Usage: Practice and Notes  
"""

"""
Module:
- A file containing code you want to add in your program.
- Use 'import' to include a pre-built module or you can make your own. 
"""

# print(help("modules"))
# print(help("math"))

# math module will provide mathematical functions and constants 
import math 
print(math.sqrt(64)) # 8.0

from math import sqrt
print(sqrt(64)) # 8.0

print(math.floor(1.4)) # 8
print(math.ceil(1.4)) # 2

# Random Function 
import random 
from random import choice, randint, random, shuffle, uniform

# random() function creates a random float value between 0-1
print(random())

# randint() function creates a random int between two values inclusive 
print(randint(1, 10))

fruits = ["banana", "apple", "oranges"]

# choice() function picks a random element from a list
print(choice(fruits))

# shuffle() function shuffles the elements into a new order
shuffle(fruits)
print(fruits)

# uniform() random float number between two floats
print(uniform(9.9, 6.6))



