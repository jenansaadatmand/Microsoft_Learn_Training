# Scenario for this module, you want to accept input from a user
# The input will be a string rather than a number, 
# so you'll need to convert it to a number
# Also, the user might enter values that give you a negative answer,
# which you won't want to display. 
# You might need to convert the answer to the absolute value. An absolute value in math is the non-negative number without its sign.
# Fortunately, Python provides utilities for these operations.


user_input = int(input("Enter a number: "))
if user_input >=0:
    print(user_input)
else:
    print(abs(user_input))   # Use the abs() function to convert a negative number to a positive, e.g. abs(number). The abs() function returns the absolute value of a number, which is guaranteed to be positive.

# other python function:
# round() used to round up the answer. It is use to round up to the nearest integer if the decimal value is greater than 0.5, or if it's less than 0.5.
# if the decimal value is equal to 0.5, the function rounds up or down to the nearest even integer.
     
print(round(2.54))  
print(round(2.43))
print()


# Python has libraries to provide more advanced operations and calculations. One of the most common is the math library. math allows you to perform rounding with floor and ceil, provide the value of pi, and numerous other operations.

# use python math library for rounding up or down.

# Rounding numbers enables you to remove the decimal portion of a float. 

# You can choose to always round up to the nearest whole number 
# by using ceil, or down by using floor.

from math import ceil, floor


round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
print()

print(ceil(13.45))
print(floor(13.45))
