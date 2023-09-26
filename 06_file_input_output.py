"""
Description: Python Module 3 File Input/Output (File I/O)
Author: Raymund Estillore
Date: 2023/09/26
Usage: Practice and Notes  
"""

"""
Opening and Closing Files
- Use the open() function to open a file and return a file object.
- Takes two arguments: The file's path and an optimal mode.

Common modes includes:
- "r": Read mode - default
- "w": Write mode - overwrites the file, then creates a new one
- "a": Append mode - appends data to the file, then creates a new one 
- "x": Exclusive creation mode - creates a new file, error if file exists
- "b": Binary mode - used for non text-files like images

To close a file use close() method.
"""

# Opening the file
file = open("example.txt, r")

# Perform file operatons here

# Close the file when done with file operations 
file.close()

"""
Reading and Writing Files:
- read() - read the entire content of the file as a string.
- readline() - reads a single line from the file.
- readlines() - reads all line of the file and retruns as a list of strings.
- write(string) - writes a specified string to the file.
"""

file = open("example.txt", "r")

content = file.read()

print(content)

file.close()

