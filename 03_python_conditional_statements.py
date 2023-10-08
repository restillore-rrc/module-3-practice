"""
Description: Python Module 3 Intro to logic and loops
Author: Raymund Estillore
Date: 2023/09/24
Usage: Practice and Notes  
"""

"""
if, elif, and else statements

if: Evaluates the first condition and executes the next code block if True.
elif: Evaluates the next condition if previous was false.
else: Executes the final code block if the previous conditions were false.
"""
# Define a variable if the person is over 21
age = 20

if age < 21:
    print("Person is not old enough")
elif age < 17:
    print("Person is not even 18")
else:
    print("Print person is old enough")

"""
Nested Conditions 
- Conditional statements inside other conditional statements
"""
# Nested Conditions Example
horizontal_position = 3
vertical_position = 5

if horizontal_position > 0:
    if vertical_position > 0:
        print("Both horizontal_position and vertical_position are positive")
    else:
        print("horizontal_position is positive, but vertical_position is not")
else:
    if vertical_position > 0:
        print("vertical_position is positive, but horizontal_position is not")
    else:
        print("Both horizontal_position and vertical_position are not positive")

"""
Comparison Operators:
- Used to compare two values and return a boolean result
"""
# Common Python comparison operators
age1 = 5
age2 = 10

print(age1 == age2)  # False
print(age1 != age2)  # True
print(age1 < age2)  # True
print(age1 > age2)  # False
print(age1 <= age2)  # True
print(age1 >= age2)  # False

"""
Logical Operators (and, or, not):
- and: Returns True if both conditions are True
- or: Returns True if one of the two conditions are True
- not: Returns True if false and Returns False if True
"""
# Logical Operator Example:
age1 = 5
age2 = 10

# Check whether both ages are positive
if age1 > 0 and age2 > 0:
    print("Both age1 and age2 are positive")

# Check whether at least one age is greater than 9
if age1 > 9 or age2 > 9:
    print("At least one of age1 or age2 is greater than 9")

# Check whether age1 is not greater than 10
if not age1 > 10:
    print("age1 is not greater than 10")

"""
Ternary Expressions (Conditional Expressions):
- Another way of writing conditional statements by in a simple way.

syntax:
value_if_true if condition else value_if_false
"""
# Example of a Ternary Expressions
number = 5

result = "Even" if number % 2 == 0 else "Odd"
print(result)

"""
Membership Operators:
- in: True when a value is in the object
- not in: True when a value is not in the object
"""
