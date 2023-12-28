# Exercise: Formatting strings:
# Knowing how to format strings is essential when you're presenting information from a program. There are a few different ways to accomplish this in Python. In this exercise, 
# you use variables that hold key facts about gravity on various moons and then use them to format and print the information.

# Create the variables
# Start by creating three variables, name, gravity, and planet, and set them to the following values:
# name: Ganymede
# planet: Mars
# gravity: 1.43

name = "Ganymede"
planet = 'Mars'
gravity = '1.43'
print()

## Create the template

# Now you will create the template to display the information about the moon. You want the output to look like the following:

# ```
#Gravity Facts about {name}
#--------------------------
#Planet Name: {planet}
#Gravity on {name}: {gravity} m/s2
#```

# Create a variable named `template`, and set it to the template you create.

template = '''
Gravity Facts about {name}
--------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2'''

# Use the template: 
# With the template created, it's time to use it to display information about the moon! 
# Use the format function on template to use the template and print the information. 
# Set name, planet, and gravity to the appropriate values.


print(template.format(name=name, planet=planet, gravity=gravity))

