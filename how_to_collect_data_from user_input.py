# Programs operate on data and data come from somewhere
# How to collect input from the command line and from user input

# command line input and command line arguments using sys module

# When you start a program by using python3, you give it the name of the file to start
# you can also give it a set of arguments: date that the program will have access to when running
# eg. python2 backup.py 2023-01-01  , (python, file name, command line argument)
# the string "2023-01-01" can be used as instruction to the program backup.py 
# to start a backup from that date
# How are these commands captured on the coding side of things?
# By using the sys module, you can retrieve the command-line arguments
# and use them in your program
# import sys
#print(sys.argv)
#print(sys.argv[0]) # program name
#print(sys.argv[1]) # first argument
# sys.argv is an array or a data structure that contains many items
# the first position, denoted as 0 in the array, contains the program name
# the second position, 1 contains your first argument.
# Assume that the program backup.py contains the sample code and you run it like this:
#python3 backup.py 2023-01-01
#the program then yields the following result:output
#['backup.py' , '2023-01-01']  , [array with position 0 as program name, position 1 as first argument]
#backup.py
#2023-01-01

# User input : another way to pass data to the program through entering data at the console 
# code it so the program tells the user to enter information
# you save that entered data in the program and then act on it
# use input() function to capture information from user


print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name.title())
print()

# Working with numbers:
# the input() function stores a result as string, 
# so you might need to convert str to number (int or float) for calculations
# calculator program:

print("Calculator program")
first_number = input("first number: ")
second_number = input("Second number: ")
print(first_number + second_number) # semantic error
# you meant for the program to unser a number but it returned a string
# because input() stores values as string, str
# explanation: first_number and second_number are strings. 
# for calculation to work correctly,
# change those strings to numbers by using the int() function
# by modifying the last line to use int() you can resolve the problem

print(int(first_number) + int(second_number))