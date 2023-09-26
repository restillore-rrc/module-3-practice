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
# for - pre-determined number of iterations 
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

# While loops - undetermined unmber of iterations 
count = 0

while count <= 10:
    print(count)
    count += 2

"""
Loop control statements (break, continue)
- break: Stops the loops and exists
- continue: Skips the remaining code in current iteration and starts the next iteration 
"""

# Example
for number in range(1, 10):
    if number % 3 == 0:
        continue
    print(number)

for number in range(1, 10):
    if number > 5:
        break
    print(number)

"""
How to avoid infinite loops:
- Make sure that theres and end point where to loops turns false
"""

# Example
int = 1

while int > 0:
    print(int)
    int += 1
    if int > 5:
        break

# Else with while loop
while int <= 5:
    print(int)
    int += 1
else:
    print("Loop finished")

# Nested Loops
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

"""
Common Loop Pattterns
- Loop counters
- Accumulators 
- Searching and Filtering
"""

# Loop counters 
count = 0

for number in range(1, 11):
    if number % 2 ==0:
        count += 1

print("There are", count, "even numbers betwenn 1 and 10")

# Accumulators 
sum = 0

for number in range(1 ,6):
    sum += number

print("The sum of numbers from 1 to 5 is", sum)

# Searching 
numbers = [1, 5, 8, 12, 15, 21]
target = 12

for number in numbers:
    if number == target:
        print("Found", target)
        break

# Filtering 
numbers = [1, 5, 8, 12, 15, 21]

filtered_numbers = [number for number in numbers if number % 2 == 0]

print("Even numbers:", filtered_numbers)
