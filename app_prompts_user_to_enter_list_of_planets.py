# while loops let you run code an unknown number of times. 
# The loops examine a Boolean condition and, as long as the condition is true, the code inside the loop will run. 
# This is very useful for situations like prompting a user for values.
# Creating an application that prompts a user to enter a list of planets. In a later exercise, you'll add code that displays the list

# Create two variables: one for the input from the user, named new_planet, and another variable for the list of planets, named planets.

# Starting with the variables you've just created, create a while loop. The while loop will run while new_planet is not set to done.
# Inside the loop, check to see whether the new_planet variable contains a value, which should be the name of a planet. This is a quick way to see whether the user has entered a value. If they have, your code will append that value to the planets variable.
# Complete the while loop by using input to prompt the user to enter a new planet name or done if they're done entering planet names. You'll store the value from input in the new_planet variable.
# Finally, outside of the while loop, print the list of planets by using print.
# As you complete this part of the exercise, pay attention to tab levels to ensure code is run at the correct time.

new_planet = ' '
planets = []
while new_planet.lower() != 'done':
    if new_planet: # To check if user has entered a value
        planets.append(new_planet) # first time it checks the value is empty ' '
    new_planet = input('Enter a new planet or done if done: ')
print(planets) # presents the list of entered planets including the empty string for the first check due to the if statement 

