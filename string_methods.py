"""
Description: Python Module 3 String Methods
Author: Raymund Estillore
Date: 2023/09/22
Usage: Practice Notes  
"""

#################### String Methods ##############################

# capitalize()
original_string = "hello_world"
capitalized_string = original_string.capitalize()

print(capitalized_string)

# center()
original_string2 = "Python"
width = 15
fillchar = "-"

centered_string = original_string2.center(width, fillchar)

print(centered_string)

# startswith()
original_string3 = "Hello, World"

boolean_variable = original_string3.startswith("World")
print(boolean_variable)

boolean_variable = original_string3.startswith("Hello")
print(boolean_variable)

# endswith()
boolean_variable = original_string3.endswith("Hello")
print(boolean_variable)

boolean_variable = original_string3.endswith("World")
print(boolean_variable)

# len()
length = len(original_string3)
print(length)

# upper()
uppercase_string = original_string.upper()
print(uppercase_string)

# lower()
lowercase_string = original_string.lower()
print(lowercase_string)

# replace()
replaced_string = original_string.replace("hello", "Hi")
print(replaced_string)

# str()
integer_value = 12345
converted_string = str(integer_value)
print(converted_string)

# split()
new_string = "Nike,Jordan,Adidas"

string_list = new_string.split(",")
print(string_list)

new_string2 = "Nike*8"

key, value = new_string2.split("*")
print("Key:", key, "Value:", value)

# strip()
new_string2 = "   Hello, World!   "
stripped_string = new_string2.strip()

print("|" + stripped_string + "|")

# lstrip()
left_stripped = new_string2.lstrip()
print("|" + left_stripped + "|")

# rstrip() 
right_stripped = new_string2.rstrip()
print("|" + right_stripped + "|")






