# Creating an application that prompts the user for the distances from the sun for two planets, and then calculates the difference between the two distances. using the arithmetic operators, and functions abs and int to convert values.
# Convert strings to numbers and use absolute values
# Creat an application to work with numbers and user input
# Create a project to calculate the distance between two planets based on user input
# read distance from sun for two planets, and then display the distance between the planets using input(), int() to convert integers and then abs() to convert the results into its absolute value
# start by adding the cpde to prompt the user for the distance between sun and the first planet, and then the second
# Store each result in variables named first_planet_input and second_planet_input

# Answer:
# Read values from user: 

first_planet_input = input("Enter the distance from the sun for first planet in km: ")
second_planet_input = input("Enter the distance from the sun for second planet in km: ")

# Convert to number: Because input returns string values, we need to convert them to numbers

first_planet = int(first_planet_input)
second_planet = int(second_planet_input)

# perform calculation and convert to absolute value:
# Add the code to perform the calculation, subtracting the first planet from the second. Because the second planet might be a greater number, you'll use abs to convert it to an absolute value.
# Subtract first_planet from second_planet and convert the result to its absolute value by using abs. Store the result in a variable named distance_km. Then display the result on the screen.

distance_km = second_planet - first_planet 

print(abs(distance_km))

# To test your project, run the notebook. You'll be prompted in a dialog to provide the distances. You can use the ones from the following table:

#Planet	Distance from sun
#Mercury    57900000
#Venus	    108200000
#Earth	    149600000
#Mars	    227900000
#Jupiter	778600000
#Saturn	    1433500000
#Uranus	    2872500000
#Neptune	4495100000
