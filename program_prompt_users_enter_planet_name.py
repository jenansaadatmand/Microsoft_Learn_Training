# A program to prompt users to enter a list of planet names and display the planets one by one. 

new_planet = ' '
planets = []
while new_planet.lower() != 'done':
    if new_planet:  # Check if there is a value in new_planet variable
        planets.append(new_planet)
    new_planet = input("Enter a new value or done if done: ")


# Display the list of planets using a for loop: 
        
for new_planet in planets:   
    print(new_planet)

