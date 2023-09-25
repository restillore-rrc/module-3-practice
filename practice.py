"""
Description: Python Module 3 Follow along
Author: Raymund Estillore
Date: 2023/09/23
Usage: Practice and Notes  
"""

# Boolean Literals
print(True)
print(False)

# Boolean Variables
is_raining_today = True
print(is_raining_today)

# Boolean Functions - Return a boolean value
name = "Raymund"

is_alpha = name.isalpha()
print(is_alpha)
print(name.isdigit())

# Boolean Operators 
# Synatx
# Operand Operator Operand
age = 21

print(age == 21) # True
print(age != 20) # True
print(age <= 21) # True
print(age < 30) # True
print(age > 30) # False 

# Synatx 
# if boolean_expression:
#       statement(s)
# else:
#       statement(s)

if age == 21:
    print(f"Age is {age} years old.")
    print("This is part of the block.")

print("This is not part of the block.")

age = 69

if age > 25:
    print("Age is greater than 25")
else:
    print("Age is less than 25")

age = 40 

if age == 30:
    print("You are 30 years old")
elif age == 40:
    print("You are 40 years old")
else:
    print("Age is not a value")

# Syntax operand and operand
if age >= 21 and name == "Raymund":
    print("Both statements are True")

if age >= 25 or name == "Raymund":
    print("One of the statments was True")

# Conditional Operator 
# Syntax: operand if operand else operand 
age_description = "Old" if age < 30 else "Young"

print(age_description)

abc = ["A", "B", "C", "D", "E", "F", "G"]
single_char = "C"
single_char2 = "H"

# Synatx: Operand in operand, operand not in operand 
if single_char in abc:
    print(f"Letter '{single_char}' is in the list")
else:
    print(f"Letter '{single_char}' is not in the list")

if single_char2 not in abc:
    print(f"Letter '{single_char2}' is not in the list")
else:
    print(f"Letter '{single_char2}' is in the list")