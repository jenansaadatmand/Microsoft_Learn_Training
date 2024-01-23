# Creating a list by assigning a sequence of values to a variable, each variable is separated by a comma and surrounded by brackets []
# Example a list of all planets

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)
# Accessing items in a list using index
# Because all indexes start from 0, [1] is the second item, [2] is the third, and so forth
print("The first planet is", planets[0])
print("The second item is", planets[1])
print("The third item is", planets[2])
print("The last item is", planets[-1])
print()

# Modifying a value in a list using its index
planets[3] = "Red planet"
print(planets)
print("Mars is also known as", planets[3])
print()


print(len(planets))

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system")
print()

# Adding and removing values to a list
# To add a value use the method .append(value)
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system")
print()
print(planets)
print()

# To remove the last value from the list use the pop() method
planets.pop() # Goodbye, Pluto, which is the last item 
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system")

# Use negative indexes to fetch an individual item in a list
# Indexes start at zero and increase. Negative indexes start at the end of the list and work backward 
# Index -1 will return the last item and index -2 will return the the second to last item

print("The first planet is", planets[0])
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])
print()

# Find a value in a list, and determine where in a list a value is stored using the index method, which searches for a value and returns the index of that item in the list.  If it does not find a match, it returns -1

jupiter_index = planets.index("Jupiter") 
print("Jupiter is the", jupiter_index + 1, "planet from the sun") # Because indexing starts with 0, you need to add 1 to display the proper number
print()
print(planets)
print()

Mercury_index = planets.index("Mercury")
print("Mercury is the", Mercury_index + 1, "planet from the sun")
print()

# Create and use Python lists
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print(planets)
# Display the number of planets
print(len(planets))
# Add a planet to the list
planets.append("Pluto")
print("Actually, there are", len(planets), "planets")
print(planets[-1], "is the last planet")
print()

# Work with other data types such as numbers in a list
# To store numbers with decimal places in Python, use the float type
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166


gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12] # relative to earth 

# In this list, gravity_on_planets[0] is the gravity on Mercury (0.378 G), gravity_on_planets[1] is the gravity on Venus (0.907 G), and so on

# On Earth, a double-decker bus weighs 124,054 Newtons (N). On Mercury, where the gravity is 0.378 G, the same bus weighs 124,054 Newtons multiplied by 0.378. In Python, to multiply two values, you use the * symbol.

gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054  # in Newton, on earth
print("On Earth, a double-decker bus weighs", bus_weight, "N")

print("On Mercury, a double-decker bus weigh", round(bus_weight * gravity_on_planets[0]), "N") # used round() 
print()

# Use min() and max() with lists to calculate the biggest and smallest number in the list
print(min(gravity_on_planets))
print()

print("On Earth, a double-decker bus weighs", bus_weight, "N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")

print()

# Manipulating list data: working with portions of lists via slicing and sorting
# retrieve a portion of a list using a slice, use brackets, with the starting and ending indexes(does not include the ending index)

# The list of planets has eight items. Earth is the third in the list. To get the planets before Earth, use a slice to get items starting at 0 and ending at 2

print(planets)
planets_before_earth = planets[0:2] # does not include index 2, Earth
print(planets_before_earth)
print()

# A slice creates a new list. It doesn't modify the current list
# To get all planets after Earth, start at the third and go to the eighth
planets_after_earth = planets[3:8]
print(planets_after_earth) # Neptune is displayed. The reason is that the index for Neptune is 7, because indexing starts at 0. Because the ending index was 8, it includes the last value

# If you do not put the stopping index in the slice, Python assumes you want to go to the end
planets_after_earth = planets[3:]
print(planets_after_earth) # pluto is printed
print()

# Join lists after splitting them: use the operator (+) with two lists to return a new list

# Create two lists. Populate the first list with four Amalthea moons and the second list with the four Galilean moons.
# Join them together by using + to make a new list:
# Joining lists creates a new list. It doesn't modify the current list

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"] 
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]
regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

print()
# Using sort modifies the current list

# Sort lists: using .sort() method, Python sorts a list of strings in alphabetical order and a list of numbers in numeric order
print(amalthea_group)
print(galilean_moons)
# regular_satellite_moons = amalthea_group + galilean_moons
print(regular_satellite_moons)
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
print()
# To sort a list in reverse order use .sort(reverse=True) method

regular_satellite_moons.sort(reverse=True)
print("The regulsr satellite moons of Jupitor are", regular_satellite_moons)
print()


# Working with lists
# using slices to retrieve portions of a list
# Create a list of planets
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Prompt the user for the reference planet 
user_planet = input("Please enter the name of a planet(with a capital letter to start)")

# Find the location of the selected planet
planet_index = planets.index(user_planet)

# Display planets closer to the sun
print("Here are the planets closer than " + user_planet)
print(planets[0:planet_index])
print()

# Display the planets farther from the sun
# Since the starting index is included when you're using a slice, as a result, you'll have to add 1 to the value. 
print("Here are the planets farther than " + user_planet)
print(planets[planet_index + 1:])  # add +1 to exclude the user_planet index
print()

