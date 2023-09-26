"""
Description: Python Module 3 Import Statements and Built-in Functions 
Author: Raymund Estillore
Date: 2023/09/26
Usage: Practice and Notes  
"""

"""
Module:
- A file containing code you want to add in your program.
- Use 'import' to include a pre-build module or you can make your own. 
"""

print(help("modules"))
print(help("math"))

# math module will provide mathematical functions and constants 
import math 
print(math.sqrt(16)) # 4.0

from math import sqrt
print(sqrt(16)) # 4.0

# Random Function 
import random 

# random() function creates a random float value between 0-1
print(random.random())

# randint() function creates a random int between two values inclusive 
print(random.randint(1, 10))

fruits = ["banana", "apple", "oranges"]

# choice() function picks a random element from a list
print(random.choice(fruits))

# shuffle() function shuffles the elements into a new order
random.shuffle(fruits)
print(fruits)


