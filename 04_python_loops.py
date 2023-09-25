"""
Description: Python Module 3 Python Loops
Author: Raymund Estillore
Date: 2023/09/24
Usage: Practice and Notes  
"""

"""
For Loops:
- In python for loops are used to iterate over a sequence such as lists,
tuples, dictionaries, or strings to execute a block of code multiple times.
"""
# Example loops
car_brands = ["Ferrari", "Bentley", "Pagani", "Aston Martin"]

for brands in car_brands:
    print(brands)

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Iterating through lists, dict, and other iterable objects

# List
numbers = [1, 2, 3, 4, 5]

for int in numbers:
    print(int * 5)

# Dictionaries 
me = {"Name": "Raymund", "Age": 21, "Grades": "A+"}

for key, value in me.items():
    print(key, value)

# Strings 
text = "Lorem ipsum dolor"

for char in text:
    print(char.upper())

# Using the range() function
for num in range(5):
    print(num)

for num in range(3, 10):
    print(num)

for num in range(2, 20, 2):
    print(num)

# Enumerate function, index and iterate
colors = ["Red", "Blue", "Green", "Purple"]

for index, color in enumerate(colors):
    print(index, color) # Ouput will be the index with element

# List comprehensions with conditions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = [number ** 2 for number in numbers if number % 2 == 1]
print(squares) # Output [1, 9, 25, 49, 81]

# While loops
