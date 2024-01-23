# Create and modify a Python dictionary 
# Dictionaries are a collection of key/values pairs, related values, or data
# Managing planet data
# Create a program that will store and display information about planets in a dictionary 
# To start you will use one planet
# Create a variable named planet, store values as a dictionary, name: Mars and moons:2
planet = {'name':'Mars', 'moons':2} # dictionary
print(planet) 

# Display or retrieve data using .get() method or using square brackets  [ ] and key name. 
# Add the code to display the planet information in the following format: --- has ---- moon(s) 
# If you were working with Earth, the output would be Earth has 1 moon(s)
# Note: you can use whatever formatting option you like
print(f'{planet["name"]} has {planet["moons"]} moon(s)')
# Add circumference information
# You can update existing keys or create new ones by either using the update method or using square brackets[ ]
# When you're using update, you pass in a new dictionary object with the updated or new values. When using square brackets, you specify the key name and assign a new value.
# Add a new value to the planet with a key of 'circumference (km)'. This new value should store a dictionary with the planet's two circumferences: polar: 6752 and equatorial: 6792


# Updating using update()method and passing a new dictionary object with updated new values
planet.update({'circumference (km)':{'polar': 6752, 'equatorial':6792}}) # nested dictionaries
print(planet)
print()

# updating using brackets [ ]: you need to uncomment code 
#planet['cirumference(km)'] = {'polar': 6752, 'equatorial': 6792}
#print(planet)
#print()


# Finally, add the code to print the polar circumference of the planet. You can use whatever sentence formating you wish
print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')
print()

