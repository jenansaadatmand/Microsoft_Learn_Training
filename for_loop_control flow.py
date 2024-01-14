# Use a 'for' loop with lists, to iterate repeatedly over every item in the list
# Lists can store any type of value (strings, numbers)
planets = ["Mercury", "Venus", "Earth", "Jupyter", "Saturn", "Uranus", "Neptune"]

# You can access any item in a list by enclosing the index in brackets eg. [0] after the variable name. 
# Indexes start from 0, always think -1 from the index you want 

print(planets[0])
print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])
print("The last planet is", planets[-1]) # to access the last item in the list
print()

# Determine the number of items in a list by using len. 
print(len(planets))
print()

# So you could use a while loop and a counter to loop or iterate over each item in the list. Because this operation is so common, Python provides for loops, which you can use to iterate over lists.
# Python has many types that can be looped over. These types are known as iterables.
# Lists are iterable, and they can be used with a for loop. You use a for loop with iterables where you loop a known number of times, once for each item in the iterable.




# using a while loop and a counter to iterate over each item in a list:

counter = 0  # initialize the counter and set it to start at 0

# use a while loop to iterate over the list 
# while counter is less then the length of the list (i.e. 7 in our program)
while counter < len(planets): 
    print(planets[counter])  # print(my_list[counter])
    counter += 1             # Step or increment by 1   
print()

# The `counter` variable is used to keep track of the current index while the while loop continues to execute as long as the counter is less than the length of the list. Inside the loop, the code accesses the element at the current index using `my_list[counter]` and then increments the counter.
# why need to set a counter to iterate a known number of time, because a while is iterating unknown numbers of times. 

# Syntax of while, len(), and counter for iteration: 
    
# First: Initialize counter
counter = 0
# Second: Use a while loop to iterate over the list and len(), set the counter increment

while counter < len(planets):
    print(planets[counter])
    counter += 1

print()
print()



# Better to use a for loop to iterate over lists: for looping a known number of times
for planet in planets:
    print(planet) # prints each item in the list in a good formate that is not a list
# for item in my_list:  # item is the name to create for each value in the sequence
#    print(item)
print()

# Example: of a for loop that counts down from 1 to 4:
countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")  # added an emoji that I copied from the online lesson in the browser

