# Program asks for the user name, formates it, and displays it back to user with a greeting
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

print()

# Solution 2: 
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print("Hello " + first_name.capitalize() + ' ' + last_name.capitalize())
print()

#Solution 3:
output_1 = f'Hello, {first_name.capitalize()} {last_name.capitalize()}'    # format strings (f)
output_2 = 'Hello, ' + first_name + ' ' + last_name # using plus (+) sign operator
output_3 = 'Hello, {} {}'.format(first_name.capitalize(), last_name.capitalize()) # using place holders and format method (string.format)
output_4 = 'Hello, {0} {1}'.format(first_name, last_name) # using place holders and assigning them to index 0 and 1

print(output_1)
print(output_2)
print(output_3)
print(output_4)
