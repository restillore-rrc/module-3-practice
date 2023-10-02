"""
Description: Python Module 3 Follow along
Author: Raymund Estillore
Date: 2023/09/29
Usage: Practice and Notes  
"""

from random import randint
from math import pow
from math import pi

# # Question 1: Print lowest of random int
# value_one = randint(0, 100)
# value_two = randint(0, 100)

# if value_one < value_two:
#     print(value_one)
# else:
#     print(value_two)

# # Question 2: Print power of input value using math module
# question_two_input = pow(float(input("Question 2: ")), 3)

# print(question_two_input)

# # Question 3: Print area and circ using math module
# question_three_radius = float(input("Question 3: "))
# question_three_area = pi * question_three_radius ** 2
# question_three_circ = 2 * pi * question_three_radius

# print(question_three_area)
# print(question_three_circ)

# # Question 4: Generate three random ints and calc the smallest of five numbers
# question_four_int_list = [randint(60, 100),
#                           randint(60, 100),
#                           randint(60, 100),
#                           randint(60, 100),
#                           randint(60, 100)]

# print(question_four_int_list)
# print(min(question_four_int_list))

# # Question 5: Make 3 random ints and calc the average
# random_ints = [randint(0, 50), randint(0, 50), randint(0, 50)]
# sum = 0
# average = 0

# for ints in random_ints:
#     sum += ints
#     average = sum / len(random_ints)

# print(average)

# # Question 6:
# input = [int(input("Hits: ")), int(input("At bats: "))]
# percentage = input[0] / input[1] * 100

# if percentage > 30:
#     print("Eligible")
# else:
#     print("Not eligible")

# Question 7:


# # Question 8:
# input = input("Enter a sentence: ")

# if input.endswith('.'):
#     print("Declarative")
# elif input.endswith('?'):
#     print("Interrogative")
# elif input.endswith('!'):
#     print("Exclamatory")
# else:
#     print("Other")

# # Question 9:
# input = input("Enter an email: ")

# if '@' in input:
#     print("Valid email")
# else:
#     print("Enter valid email")

# # Question 10:
# input = [input("Enter new password: "), input("Re-enter password: ")]

# if input[0] == input[1]:
#     print("New password confirmed")
# else:
#     print("Incorrect password")

# Question 11:
