# Building a unit convertor utility, parsecs convert to lightyears
# Converting parsecs to lightyears
# The parsec (symbol: pc) is a unit of length used to measure the large distances to astronomical objects outside the Solar System, approximately equal to 3.26 light-years or 206,265 astronomical units (AU)
# One parsed is 3.26 lightyears
# So you will multiply parsecs by that value to determine lightyears
# create a variable named parsecs and set it to 11
# Then add the code to perform the appropriate calculation and
# Store the result in a variable named lightyears 
# Finally print the result on the screen with print 
# So it displays a message which resembles the following: 
# 11 parsecs is ----lightyears
#  Remember to you can use str to convert numbers to strings
# turn into str to be able to concatenate 

parsecs_input = input("Enter number of parsecs: ")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs
print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")
