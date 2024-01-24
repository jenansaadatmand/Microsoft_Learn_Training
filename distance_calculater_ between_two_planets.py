# Create a program that calculates the distance between two planets
# using two planet distances: Earth (149,597,870 km) and Jupiter (778,547,200 km)
# Remove the commas when you're using the values 

first_planet = 149597870
second_planet = 778547200

# You have two variables which store the distance between each planet and a common point: the sun. You can subtract these two values to determine the distance between the planets.

distance_km = second_planet - first_planet
print(distance_km, "km")
distance_mi = distance_km / 1.609344  # convert distance_km to miles by dividing it by 1.609344 
print(distance_mi)
