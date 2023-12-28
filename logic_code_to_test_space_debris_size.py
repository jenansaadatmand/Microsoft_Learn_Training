# Exercise: Use logic to examine an object's size
# Code to test the size of the object. 
# start your project by creating the code to determine if a piece of space debris is of a dangerous size. 
# For this exercise we will use an arbitrary 
# size of 5 meters cubed (5m3); anything larger is a potentially dangerous object.
# Add a variable named object_size and 
# set it to 10 to represent 10m3. 
# Then add an if statement to test if object_size is greater than 5. 
# If it is, display a message saying We need to keep an eye on this object. 
# Otherwise, display a message saying Object poses no threat.


object_size = 10
if object_size > 5:
    print("We need to keep an eye on this object")
else:
    print("Object poses no threat")
    