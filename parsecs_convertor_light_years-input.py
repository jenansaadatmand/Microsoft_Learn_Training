# Having a program with hard coded values limits its flexibility.
# add the ability to specify a value for variable, eg. parsecs
# Create a program which can accept user input
# program unit convertor : parsecs convert to lightyears
# turn into str to be able to concatinate 
# start by creating a variable named parsecs_input & setting it to the result of input
# Which should prompt the user to enter the number of parsecs
# convert parsecs_input to an integer by using int() & storing it in parsecs
# finish by performing the calculation & displaying the result


# Accepting user input:

parsecs_input = input("Enter number of parsecs: ") 
parsecs = int(parsecs_input)
lightyears = parsecs * 3.26156
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")


