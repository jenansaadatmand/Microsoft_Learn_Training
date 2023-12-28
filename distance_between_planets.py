# Distance between planets:
# Scenario: to create a project to determine the distance between planets.
# Imagine you're creating a program to calculate the distance between planets. 
# The program enables a user to enter the distances of two planets from the sun, 
# and calculates the distance between those two planets. 
# Additionally, you want to provide the distance in both miles and kilometers.

distance_1 = input("Enter distance to plant 1 in miles: ")
distance_2 = input("Enter distance to plant 2 in miles: ")
distance_1 = int(distance_1)
distance_2 = int(distance_2)
distance_between_two_planets = distance_1 + distance_2
distance_kilometres = distance_between_two_planets * 1.609
# 1 mile = 1.609 kilometres 
print("The distance between the two planets: ", distance_between_two_planets, " miles")
print("The distance between the two planets is: ", distance_kilometres, " kilometres")