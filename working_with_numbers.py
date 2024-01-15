# Working with numbers
pi = 3.14159
print(pi)
print()

first_num = 6
second_num = 2
print(first_num + second_num) # addition
print(first_num - second_num) # subtraction 
print(first_num / second_num) # Division always results in a float 
print(first_num * second_num) # multiplication
print(first_num ** second_num) # Exponent 
print()


# Data type conversion: 

# Use str() for data type conversion

# When displaying a string that contains numbers you must convert the numbers into strings because Python does not concatenate int and str
days_in_feb = 28
print(str(days_in_feb) + ' days in February') # convert number into string literal using str()
print()

# Alternatively, you store a number as a string using quotation marks
first_num = '5' # stored as a string that contains the number 5
second_num = '6' # sotred as a string that contains the number 6
print(first_num + second_num) # the problem here it will concatenate 5 and 6 to 56 
print()

# Becareful : with input() function because it always returns a string

first_num = input('Enter first number ') # returns a string of the 'number'
second_num = input('Enter second number ')
print(type(first_num))
print()

# Use int() function for data type convertion

print(int(first_num) + int(second_num)) # both numbers will be concatenated and you cannot perform mathematical operation on them unless you convert the string numbers into integers using int() function
print()

# You can use float() function for data type conversion 
print(float(first_num) + float(second_num))
print()
