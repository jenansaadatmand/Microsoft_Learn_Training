# Exercise: Use complex logic to determine possible evasive maneuvers.
# You will test both the object's size and proximity. 
# You will use the threshold for size of 5m3. 
# If the object is both larger than the threshold 
# and within 1000km of the ship evasive maneuvers will be required.
#  Create two variables: object_size and proximity. 
#Set object_size to 10 to represent 10m3. Set proximity to 9000.
# Then add the code to display a message saying Evasive maneuvers required 
# if both object_size is greater than 5 and proximity is less than 1000. 
# Otherwise display a message saying Object poses no threat.


object_size = 10
proximity = 9000
if object_size > 5 and proximity < 1000:
    print('Evasive maneuvers required')
else:
    print('Object poses no threat')

