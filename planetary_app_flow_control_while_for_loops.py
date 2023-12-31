# Scenario: Working with flow control (while and for loops) on a planetary app
# Imagine you're creating an application where users enter a list of planet names. 
# After the users enter the names, you display the results back to them. This scenario requires prompting the users multiple times to enter values, and when they're done 
# your code displays all the data in the list. In this module, we explore how you can use while and for loops to create this application.
# Run a task multiple times using a while loop
# Loop over list data by using for loop

# You want to allow a user to enter a list of planet names. 
# Unfortunately, you don't know how many names the user enters. 
# To support looping an unknown number of times, you can use a while loop.
# A while loop performs an operation while a certain condition is true. 
# You could use a while loop to:
# Check for another line in a file.
# Check if a flag has been set.
# Check if a user has finished entering values.
# Check if something else has changed to indicate that the code can stop performing the operation.
# The most important thing to remember when you create while loops is to ensure that the condition changes. 
# If the condition is always true, Python will continue to run your code until the program crashes.
# The syntax of a while loop is similar to that of an if statement. 
# You provide both a condition and the code you want to run while the condition is true.
# while <condition>:
    # code here

# You can create code to prompt users to enter values, and then allow them to enter done when they've finished entering the values. In our example, the user input is the condition that is tested at the top of the while loop.



# Solution 1:

user_input = ' '   # definig or creating a variable usr_input for user input (empty string), where values can be stored in the variable

while user_input.lower() != 'done':  
    user_input = input('Enter a new value, or done when done:')
    print(user_input) # prints the values back on the screen 


# while loop for repetitive task, & lower to convert the input to lowercase, which allows for a case-insensitive comparison.
# Each time users enter a new value they're changing the condition, which means that the while loop will exit after they've entered done.
    
print()
print()


# Solution 2: 

while True:         # while loop for repetitive task
    user_input = input("Enter a value or type 'done' when you're finished: ")
    print(user_input)
    if user_input.lower() == 'done':
        break
print()
print()



# Solution 3:
# You can use the newly entered string that's captured with input. If you want to add it to a list.
user_input = ' ' # Create the variable for user input
inputs = [] # Create the list to store values
# The while loop
while user_input.lower() != 'done': 
    if user_input: # Check if there's a value in user_input
        inputs.append(user_input) # Store the value in the list
    user_input = input("Enter a new value, or done when done: ") # Prompt for a new value
print(inputs)

# Notice the if statement inside the while loop. It tests for a string value inside user_input. If the while loop is running for the first time, there's no value, so there's nothing to store in inputs. 
# After it runs for the first time, user_input always keeps the value that the user has entered. Because while is testing to ensure that the value doesn't equal done (the word the user enters to exit the app), you know that the current value is one that you can add to the list.

print()
print()



# Solution 4: # Appending to alist and printing it at the end 

list_values = []
while True:
    user_input = input("Enter a value or type 'done' when you're finished: ")
    list_values.append(user_input)
    print(user_input)
    if user_input.lower() == 'done':
        break
print(list_values) # ask program to print the list on screen, notice this list does not have a check if the variable is empty so it does not include a ' ' empty result. 
print()
print()
