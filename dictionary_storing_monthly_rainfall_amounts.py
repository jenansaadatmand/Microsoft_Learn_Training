# A program contains a dictionary that stores monthly rainfall amounts, with keys for each month and the associated rainfall value
# You want to add up the total rainfall

# Retrieve all keys and values using keys() method, which returns a list object that contains all the keys. Use this method to iterate through all items in the dictionary

rainfall = {'october': 3.5, 'november': 4.2, 'december':2.1}
print(rainfall) # printing the full dictionary
print()

# Display the list of all rainfall using keys() and a for loop
for key in rainfall.keys():
    print(f'{key}:{rainfall[key]}cm')
print()
  
# Note: You can still use square brackets ([ ]) with a variable name, rather than the hard-coded string literal.
print(f'october {rainfall["october"]}\nnovember {rainfall["november"]}\ndecember {rainfall["december"]}\n')

# Determine if a key exists in a dictionary
# When you update a value in a dictionary, Python will either overwrite the existing value or create a new one, if the key doesn't exist. 
# If you wish to add to a value rather than overwriting it, you can check to see if the key exists by using in. For example, add a value to December or create a new one if it doesn't exist
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1 # because december exist, the value will be 3.1
    print(rainfall['december'])
else:
    rainfall['december'] = 1
    print(rainfall['december'])

print()

# Retrieve all values using values()
# Similar to keys(), values() returns the list of all values in a dictionary without their respective keys
# determine the total rainfall amount using values()
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value
print(f'There was {total_rainfall} cm in the last quarter.')



