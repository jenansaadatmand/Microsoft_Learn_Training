# Program asks for user name, formates it and displays it back to user with a greeting
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

print()

# alternatively, 
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
print("Hello " + first_name.capitalize() + ' ' + last_name.capitalize())
