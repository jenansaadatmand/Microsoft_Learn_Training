# Creating functions
# A function contains code that always returns a value(s)
# A function can be with no argument or in some cases a function has optional or required inputs/arguments/parameters to be passed into the function
# functions prevent code duplications, limit the size of code by extracting parts out into smaller more readible functions, improve readibility 
# TO create a function, you use the def keyword, followed by a name, parenthesis, and the body with the function code
# To use the function, you must call it by its name by using parenthesis

# Creating a function that doesn't take any argument and prints a statement about gravity

def rocket_parts(): 
    print("payload, propellant, structure")
rocket_parts() # when calling a function, it prints the output on the screen if it includes a print() function
print()

# If you need to use a value that a function is returning, you can assign the function output to a variable

output = rocket_parts() # assigning a variable to contain the output of the function to be used later in the program

print(output) # printing a statement is not returning a value
print()

# It might seem surprising that the value for the output variable is None. This is because the rocket_parts() function didn't explicitly return a value. In Python, if a function doesn't explicitly return a value, it implicitly returns None. 
print(output is None) 
print()



# If you need to use the value of a function, that function must return explicitly. Otherwise, None is returned.
# You don't need to always assign the return of a function. In most cases where a function doesn't return a value (or values) explicitly, it means that you don't need to assign or use the implicit None that's returned.

# Updating the function to return the string instead of printing it causes the output variable to have a different value:

def rocket_parts(): # create and define a function
    return "payload, propellant, structure" # return a value to be used later on
output = rocket_parts() # create a variable and call function
print(output)
print(output is None)
print()

# Creating a function with a required and optional arguments
# In Python several built-in functions require arguments, some built-in functions make arguments optional
# Built-in functions are immediately availble so you don't need to import them explicitly 

# An example of a built-in function that requires an argument is any(). 
# This function takes an iterable (for example, a list) and returns True if any item in the iterable is True. Otherwise, it returns False.

any([True, False, False]) # a list is passed as an argument
output1 = any # calling the function
print(output1)
print()
print(any) # lets you know its a built-in function
print(type(any)) # lets you know its a built-in function
print() 

# any() function returns True if any item in an iterable object is true
A = any(["dog", 3, 4])
print(any("dog"))
print()
# If you call any() without any arguments, a helpful exception is raised. The error message explains that you need at least one argument:
#Traceback (most recent call last): File "<stdin>", line 1, in <module> TypeError: any() takes exactly one argument (0 given)

# You can verify that some functions allow the use of optional arguments by using another built-in function called str(). This function creates a string from an argument. If no argument is passed in, it returns an empty string:


print(str())  # str() takes an optional argument, in the terminal, should return empty string '' when there is no argument passed
print(str(15)) # 15 is passed as an argument 
print()

# Use function arguments in Python, more flexible functions 
# Create functions that require an argument
# To require an argument, put it within the parentheses

def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else: # catch-all condition
        return "Unable to compute that destination"
    
# Try calling the distance_from_earth() function without any arguments using:   
#distance_from_earth() # uncomment this code
    
# Python raises TypeError: distance_from_earth() missing 1 required positional argument: 'destination'

# Example code has two paths for a response, one for the Moon and the other one for anything else. Use the Moon as input to get an answer:
print(distance_from_earth("Moon")) # Including "Moon" as an argument
# Because there's a catch-all condition, try using any other string as the destination to check that behavior:
print(distance_from_earth("Saturn")) 
print()

# Multiple required arguments:
# To use multiple arguments, you must separate them by using a comma. 
# Create a function that calculates how many days it takes to reach a destination, given distance and a constant speed: 
# destination = speed * hours
def days_to_complete(distance, speed):
    hours = distance/speed # calculate how long it takes? 
    return hours/24 # convert to days

# use the distance from Earth to the Moon to calculate how many days it would take to get to the Moon at a speed limit of 75 miles per hour: distance to moon = 238855
print(days_to_complete(238855, 75)) 
print()

# functions as arguments:
# You can use the value of the days_to_complete() function and assign it to a variable, and then pass it to round() (a built-in function that rounds to the closest whole number) to get a whole number:
total_days = days_to_complete(238855, 75)
print(round(total_days))
print()

# A useful pattern is to pass functions to other functions instead of assigning the returned value

print(round(days_to_complete(238855, 75))) # here we didn't create a variable and then round(), we passed the days_to_complete(two arguments) function as an argument for the round() function, passing functions directly into other functions aas input 
print()


