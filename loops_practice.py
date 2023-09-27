"""
Description: Python Module 3 Python Loops
Author: Raymund Estillore
Date: 2023/09/26
Usage: Practice and Notes  
"""

# Question 1 - Use while loop to print ints
even = 0
odd = 0
natural = 1
whole = 0

# Prints all even ints from 1-10
while even <= 10:
    if even % 2 == 0:
        print(even)
    even += 1

# Prints all odd ints from 1-10
while odd <= 10:
    if odd % 3 == 0:
        print(odd)
    odd += 1

# Prints all natural ints from 1-10
while natural <= 10:
    print(natural)
    natural += 1

# Prints all whole ints from 1-10
while natural <= 10:
    print(natural)
    natural += 1


# Question 2 - Use while loop to square 1-10 ints 
squared_ints = 0

while squared_ints <= 10:
    print(squared_ints ** 2)
    squared_ints += 1

# Question 3 - Use for and while loop to print ints
random_ints = [10, 20, 30, 300]
ints_by_ten = 10

for ints in random_ints:
    print(ints)

while ints_by_ten <= 300:
    print(ints_by_ten)
    ints_by_ten += 10

# Question 4 - Use while loop to print ints
initial_int = 105 

while not initial_int == 0:
    print(initial_int)
    initial_int -= 7

# Question 5 - Print first 10 natural numbers in reverse 
first_ten_natural = 10

while not first_ten_natural == 0:
    print(first_ten_natural)
    first_ten_natural -= 1
    
