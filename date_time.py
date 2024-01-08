# To work with date: means both calendar date and time in a program

from datetime import date  # Use datetime library, import date object from datetime library
date.today() # Use today() function to get today's date
print(date.today())

# data type conversion, date is a number, cannot be concatenated with a str, 
# so you need to convert it to str using str()
print("Today's date is: " + str(date.today()))  


