"""
Description: Python Module 3 Follow along
Author: Raymund Estillore
Date: 2023/09/29
Usage: Practice and Notes  
"""

from random import randint
from math import pow
from math import pi
from math import sqrt

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

# # Question 11:
# question_eleven_input = input("Enter your username: ")

# if len(question_eleven_input) >= 6 and len(question_eleven_input):
#     print(f"Welcome, {question_eleven_input}")
# else:
#     print("Invalid username")

# # Question 12:
# input = input("enter domain name: ")
# split = input.split('.')

# if split[2] == "gov":
#     print("Government")
# elif split[2] == "edu":
#     print("University")
# elif split[2] == "com":
#     print("Business")
# elif split[2] == "org":
#     print("Organization")
# else:
#     print("Other")

# # Question 13:
# input = int(input("Enter a temperature: "))

# if input >= 90 and input < 110:
#     print("Summer")
# elif input >= 70 and input < 90:
#     print("Spring")
# elif input >= 50 and input < 70:
#     print("Fall")
# elif input > 110 or input < -5:
#     print("Invalid")
# else:
#     print("Winter")

# # Question 14:
# input = input("Enter a year: ")

# if len(input) == 2:
#     print(int(input) + 2000)
# elif len(input) == 4:
#     print(input)
# else:
#     print("Invalid")

# # Question 15:
# valid_inputs = ["admin", "open"]
# input = [input("Enter username: "), input("Enter password: ")]

# if input[0] == valid_inputs[0] and input[1] == valid_inputs[1]:
#     print("Welcome.")
# elif input[0] == valid_inputs[0] and not input[1] == valid_inputs[1]:
#     print("Correct username, incorrect password.")
# elif not input[0] == valid_inputs[0] and input[1] == valid_inputs[1]:
#     print("Incorrect username, correct password.")
# else:
#     print("Incorrect username and password.")

# # Question 16: Re-do
# value = 0
# inc = 0
# sum = 0
# number = 0

# while value < 10:
#     value = float(input("Enter a value: "))

# while sqrt(value) >= 1.01:
#     number = sqrt(value)
#     print(number)
#     sum = sqrt(number)
#     print(sum)
#     inc += 1

# print(inc)

# # Question 17:
# valid_email = False

# while not valid_email:
#     email = input("Enter email: ")
#     if '@' not in email:
#         print("Invalid email")
#     else:
#         valid_email = True
#         print(email)


# # Question 18:
# file_path = "input.txt"

# with open(file_path) as file:
#     for data in file:
#         int_number, float_number = data.strip().split(',')
#         print(int_number, float_number)

# # Question 19:
# sum = 0

# for int in range(10, 20):
#     sum += int

# print(sum)

# # Question 20:
# sum = 1

# for numb in range(3, 8):
#     sum *= numb

# print(sum)

# # Question 21:
# inc = 0

# for numb in range(33, 97):
#     if numb % 7 == 0:
#         inc += 1

# print(inc)

# # Question 22:
# integer = False

# while not integer:
#     value = input("Enter a value: ")
#     if int(value.isnumeric()):
#         print("Hello world | " * int(value))
#         integer = True
#     else:
#         print("Invalid value")

# # Question 23: Re-do
# string_input = input("Enter a string: ")
# char_string = ''

# for char in string_input:
#     string_input.split(char)
#     char_string = char + " "

# print(char_string)

# Question 24:
int_input = int(input("Enter a value to convert into a factorial: "))
