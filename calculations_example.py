# Calculations examples:

print('Combine two piles of space rocks ?')
print(2 + 6)
print()
print('Lose three units of oxygen')
print(15-3)
print()
print('Find how far a rocket has gone by multiplying speed by time traveling)
print(17000*2)
print()
print('Determine number of rocks per pile if we separate 100 space rocks in 4 even piles')
print(100/4)
print()
print('Precedence of operations, parenthesis first')
print(2 + 5 * 3)
print()
print('How many rocks remain when we divide 10 rocks into 3 even piles ?')
print(10%3)
print()
print('Calculate exponential operator 10^ 5.37 using **, two asterisks)
print(10**3.527)
print()
print("How many even piles of 2 we can make with 5 rocks, leave off the remainder value when doing division using // floored quotient")
print(5//2)
print()

# Variables are containers that you can store data in and use at different times.

# There are four main types of data variables:

# Integers (int): Whole numbers, like 1, 4, 10, -5.
# Floats (float): Decimal numbers, like 0.3, 1.6, 17.4, -3.5.
# Strings (str): Chains of characters that are surrounded by single or double quotes, like "hi", "NASA", "Space Rocks", "54321".
# Booleans (bool): Represents either True or False.

print('integer variable:')
number0fRocks = 5 
print(number0fRocks)

print('Float Varaible:')
temInspace = -457.87
print(temInspace)
print('String variable:')
roverName = "Artemis Rover"
print(roverName)
print('Boolean Variable:')
rocketOn = False
print(rocketOn)


# Creating a variable & performing operations on it or changing its content:
# This can be useful if we want to inform the computer that 
# We've found three rocks so far and we've just found another.

basaltRockCount = 0
print(basaltRockCount)
basaltRockCount = 3 # changing its content
print(basaltRockCount)
basaltRockCount = basaltRockCount +1 # incrementing by 1
print(basaltRockCount)


# An easy way to perform an operation on a variable is 
# to use the operation you want to apply and then 
# add an equal sign after it. 
# This will perform the action and set the variable to the new value. For example:

basaltRockCount = 5
basaltRockCount += 3   # Add 3 
basaltRockCount -= 2  # Remove 2
# These two codes are the same 
basaltRockCount += 1  # take the variable, increment by 1, and then reset it
basaltRockCount = basaltRockCount +1 
