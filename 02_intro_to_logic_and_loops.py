"""
Description: Python Module 3 Intro to logic and loops
Author: Raymund Estillore
Date: 2023/09/23
Usage: Practice and Notes  
"""

""" 
Control Structures:
- Basically the building blocks of a language.
- Allows the flow of code being read.

Boolean Expressions:
- Boolean Literal
- Boolean Variable
- Use of an operator
- Function return value 

Three Main Types:
- Sequential: (Line by line) How statements are executed the way they are written.
- Selection: (if-else) Based on the conditions.
- Iteration: (loops) Executed repeatedly.

In Python conditional statements are the primary control structure
(if, elif, else) and (for and while loops)
"""
# Example of control structure
number = 10

if number > 0:
    print("Number is positive")
elif number == 0:
    print("Number is zero")
else:
    print("Number is negative")

"""
Importance of Logic and Loops in Programming 
- Conditional statements helps you make the right decision based on specific conditions  
- Loops helps you automate repetitive tasks/code and perform multiple operations at the same time 
- Implement complex algorithms 
"""
# Code example of loops
for number in range(10):
    print(number)

"""
Indentation - Python heavily relies on indentation 

Key Points:
- Consistency: Use same number of tabs for each character of each line 
- Required: Indentation determines the scope of code blocks
- Readability: Indentation makes code readable and easier to understand and maintain 
"""
# Example of indentation
new_number = 6

if new_number > 0:
    print("Number is a positive")
if new_number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
