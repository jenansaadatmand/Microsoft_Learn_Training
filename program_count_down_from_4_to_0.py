# A program that uses a 'for' loop to count down from 4 to 0:

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
print("Blast off!! 🚀")  # added an emoji that I copied from the online lesson in the browser
print()


# Let's change the code to wait one second between each number by using the sleep() function from the time library 


from time import sleep  # import the sleep() from the time module 

countdown = [4, 3, 2, 1, 0]
for number in countdown:
    print(number)
    sleep(1)  # wait 1 second 
    
print("Blast off!! 🚀")
