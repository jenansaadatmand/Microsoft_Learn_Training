# Complex conditional logic or workflow (if elif elif else)
# elif: # else if to add multiple test expressions, run in the order in which they are written


a = 27
b = 93

if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

# Syntax of if elif else conditional statement
# if test expression:
    # indented statement to be Run
# elif expression:
    # indented statement to be run
# elif expression:
    # indented statement to be run
# else no test expression is needed, it the left over:
    # indented statement to be run 
     
        
# nested conditional logic:
# You can nest if, elif, else statements to create even more complex programs
# To nest conditions, indent the inner conditions
# Everything in at the same level of indentation will be run in the same code block

a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print("a is greater than b and b is greater than c")

elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")
            
