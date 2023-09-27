"""
Description: Python Module 3 Python Loops
Author: Raymund Estillore
Date: 2023/09/26
Usage: Practice and Notes  
"""

# # Question 1 - Use while loop to print ints
# even = 0
# odd = 0
# natural = 1
# whole = 0

# # Prints all even ints from 1-10
# while even <= 10:
#     if even % 2 == 0:
#         print(even)
#     even += 1

# # Prints all odd ints from 1-10
# while odd <= 10:
#     if odd % 3 == 0:
#         print(odd)
#     odd += 1

# # Prints all natural ints from 1-10
# while natural <= 10:
#     print(natural)
#     natural += 1

# # Prints all whole ints from 1-10
# while natural <= 10:
#     print(natural)
#     natural += 1


# # Question 2 - Use while loop to square 1-10 ints 
# squared_ints = 0

# while squared_ints <= 10:
#     print(squared_ints ** 2)
#     squared_ints += 1

# # Question 3 - Use for and while loop to print ints
# random_ints = [10, 20, 30, 300]
# ints_by_ten = 10

# for ints in random_ints:
#     print(ints)

# while ints_by_ten <= 300:
#     print(ints_by_ten)
#     ints_by_ten += 10

# # Question 4 - Use while loop to print ints
# initial_int = 105 

# while not initial_int == 0:
#     print(initial_int)
#     initial_int -= 7

# # Question 5 - Print first 10 natural numbers in reverse 
# first_ten_natural = 10

# while not first_ten_natural == 0:
#     print(first_ten_natural)
#     first_ten_natural -= 1
    
# # Question 6 - Write a program to print the sum of first 10 natural numbers
# question_six_inc = 0
# question_six_sum = 0

# while question_six_inc <= 10:
#     question_six_sum += question_six_inc
#     question_six_inc += 1
# print(f"Sum of first 10 digits: {question_six_sum}")

# Question 7 - Write the sum of first 10 even numbers 
# question_seven_sum = 0
# question_seven_inc = 0

# while question_seven_inc <= 10:
#     if question_seven_inc % 2 == 0:
#         question_seven_sum += question_seven_inc
#     question_seven_inc += 1
# print(question_seven_sum)

# # Question 8 - Write a program to print a table of numbers 

# enter_number = int(input("Enter a number: "))
# inc = 1

# while inc <= 10:
#     print(f"{enter_number * inc}")
#     inc += 1

# Question 9 - Print all even numbers between two numbers entered 
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

# check first int is less than second int
# else check the second int is less than first int 
if first_number <= second_number:
    while first_number <= second_number:
        if first_number % 2 == 0:
            print(first_number)
        first_number += 1
else:
    while second_number <= first_number:
        if second_number % 2 == 0:
            print(second_number)
        second_number += 1

# Question 10 - Check if entered int is a prime number 
prime = int(input("Enter a value: "))

# Question 11 - Make a program to find the sum of digits entered from the user.
entered_number = int(input("Enter a value to get the sum of digits: "))
digit = 0
sum = 0

while entered_number != 0: # number not equal to zero = true
    digit = entered_number % 10 # remainder op to get the last digit
    sum += digit # add the sum of each digits
    entered_number //= 10 # floor division to remove last digit
    # Will keep looping back until entered_number is zero

print("The sum is", sum)
