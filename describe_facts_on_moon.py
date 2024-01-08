# Create a program to describe facts (some measurements & other information) about the Moon
# Use various string operations to create the output
# Use special string methods
# Use variables to introduce values in text
# Apply other advanced formatting techniques to change how text is presented

# Assign a single fact about the Moon to a variable

fact = "The Moon has no atmosphere."
print(fact)
print()

# Immutability of strings: strings can't change. Python does not give an error when you alter strings

# Add another fact (sentence) to the single fact that's assigned to a variable.  It seems as though adding the second fact would alter the variable. You might expect the output to be: The Moon has no atmosphere. No sound can be heard on the Moon.
# Although it might look as though we've modified the variable fact, a quick check of the value reveals that the original value is unchanged: 


fact = "The Moon has no atmosphere."
fact + " No sound can be heard on the Moon" # This is a new strin returned by python
print(fact)
print()

# Operations on strings always produce new strings as a result.
# The trick is that you must use a return value. When you add strings, Python doesn't modify any string but returns a new string as a result. To keep this new result, assign it to a new variable:

two_facts = fact + " No sound can be heard on the Moon"   # New string assigned to a new variable
print(two_facts)
print()


# You can enclose Python strings in single, double, or triple quotation marks.Use one type consistently within a project. 

moon_radius = """The Moon has a radius of 1,080 miles."""
print(moon_radius)

# However, when a string contains words, numbers, or special characters (a substring) that are also enclosed in quotation marks, you should use a different style. For example, if a substring uses double quotation marks, enclose the entire string in single quotation marks

print('The "near side" is the part of the Moon that faces the earth.')

# Similarly, if there are single quotation marks (or an apostrophe, as in Moon's in the following example) anywhere within the string, enclose the entire string in double quotation marks:

print("We only see about 60% of the Moon's surface.")

# Failure to alternate single and double quotation marks can cause the Python interpreter to raise a syntax error
# print('We only see about 60% of the Moon's surface.')
# output: SyntaxError: unterminated string literal (detected at line 46)

# When the text has a combination of single and double quotation marks, you can use triple quotation marks to prevent problems with the interpreter:
print("""We only see about 60% of the Moon's surface this is known as the "near side".""")      
print()


# Multiline text:
# There are a few different ways to define multiple lines of text as a single variable
# use a newline character (\n)
# Use triple quotation marks (""")

# Newline characters separate the text into multiple lines when you print the output:

multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
print()

# You can achieve the same result by using triple quotation marks:

multiline = """Facts about the Moon:
 There is no atmosphere. 
 There is no sound."""
print(multiline)
print()

# String methods in Python : title(), upper(), lower(), capital()
# You'll often need to manipulate strings to extract information or fit a certain format. Python includes several string methods that are designed to do the most common and useful transformations.
# String methods are part of the str type. This means that the methods exist as string variables, or part of the string directly. For example, the method .title() returns the string in initial caps and can be used with a string directly:

print("temperature and facts about the moon".title())
print("jenan and jimmy".title())


# The same behavior and usage happens on a variable:

heading = "temperature and facts about the moon"
heading_upper = heading.title()
print(heading_upper)
print()

# split a string: .split() creates a list output
# Without arguments, the method will separate the string at every space. This would create a list of every word or number that's separated by a space:

temperatures = "Daylight: 260 F Nighttime: -280 F"
temperature_list = temperatures.split()
print(temperature_list)

print("jenan and jimmy".split())
print()

# In this example, you're dealing with multiple lines, so the (implicit) newline character can be used to split the string at the end of each line, creating single lines:
# This type of splitting becomes handy when you need a loop to process or extract information, or when you're loading data from a text file.

temperatures = "Daylight: 260 F\n Nighttime: -280 F" # two lines 
temperatures_list = temperatures.split('\n') # pass an argument in the split() method, split at lines not words.
print(temperatures_list)
print()

# Search for a string: use the in operator 

# Some string methods can look for content before processing, without using a loop. Let's assume that you have two sentences that discuss temperatures on various planets and moons. However, you're interested only in temperatures that are related to our Moon. That is, if the sentences aren't talking about the Moon, they shouldn't be processed to extract information.

# The simplest way to discover whether a given word, character, or group of characters exists in a string is to use the in operator:

print("Moon" in "This text will describe facts and challanges with space travel") # will return false
print("Moon" in "This text will describe facts about the Moon") # will return True
print("J" in "Jimmy") # will return True

# Finding the position of a specific word in a string, using .find() method:

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon")) # returns -1 word isn't found

# The .find() method returns a -1 when the word isn't found, or it returns the index (the number representing the place in the string). This is how it would behave if you're searching for the word Mars:
print(temperatures.find("Mars")) # returns the index/place in the string

print("Jenan Jimmy".find("y"))
print()

# Another way to search for content is to use the .count() method, which returns the total number of occurrences of a certain word in a string:

temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Mars"))
print(temperatures.find("Moon"))

print("Jenan Jimmy".count("J"))
print()

# Strings in Python are case-sensitive, which means that Moon and moon are considered different words. To do a case-insensitive comparison, you can convert a string to all lowercase letters by using the .lower() method:

# Strings in Python are case-sensitive, which means that Moon and moon are considered different words. 
# To do a case-insensitive comparison, you can convert a string to all lowercase letters by using the .lower() method:

print("The Moon And The Earth".lower())

# Similar to the .lower() method, strings have an .upper() method that does the opposite, converting every character to uppercase:

print("The Moon And The Earth".upper())


# When you're searching for and checking content, a more robust approach is to lowercase a string so that casing doesn't prevent a match. For example, if you're counting the number of times the word the appears, the method wouldn't count the times where The appears, even though they're both the same word. You can use the .lower() method to change all characters to lowercase.

example = "This is an example where we have the and The"
print(example.find("the"))
print(example.count("the"))
example = example.lower() # convert to lower case then search with find() or count() to avoid case sensitivity in strings
print(example.count("the"))
print()

# Check content: 
# structured string: use split() method to extract information
# There are times when you'll process text to extract information that's irregular in its presentation. For example, the following string is simpler to process than an unstructured paragraph:
temperatures = "Mars Average Temperature: -60 C"

# To extract the average temperature on Mars, you can do well with the following methods:

parts = temperatures.split(':') # ":" argument in split() for the position of splitting like when we used \n

print(parts)
print(parts[-1]) # provide index -1 as an argument in split() to retrive last item in the splited list
print()

# Spliting at a word, removes the word:
print("spliting at another the word 'average':")
print(temperatures.split('Average'))

# The preceding code trusts that everything after the colon (:) is a temperature. The string is split at :, which produces a list of two items. Using [-1] on the list returns the last item, which is the temperature in this example.

# unstructured text, Irregular text: use a loop to check values of certain types.
# If the text is irregular, you can't use the same splitting methods to get the value. You must loop over the items and check to see whether the values are of a certain type. Python has methods that help check the type of string:

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split(): # first use a loop, then make a list to search in it
    if item.isnumeric(): # use string isnumeric() method 
        print(item)

# Like the .isnumeric() method, 
# .isdecimal() can check for strings that look like decimals.
# .isdigit() can check for strings that look like integers.

print()

# It might be surprising to learn that "-70".isnumeric() would return False. This is because all characters in the string would need to be numeric, and the dash (-) isn't numeric. If you need to check negative numbers in a string, the .isnumeric() method wouldn't work.

x = "-70"
print(x.isnumeric()) # negative number, returns false because character - is in a string is not a number.
print()


# There are extra validations that you can apply on strings to check for values. 
# For negative numbers, the dash is prefixed to the number, and 
# that can be detected with the   .startswith() method:

print("-60".startswith('-')) # detects negative values in strings.
print("-70".startswith('-'))

print("Jenan Saadatmand".startswith('J')) # you can find if a string starts with a specific character/letter
print()


# similarly, the .endswith() method help with verifying the last character of a string
if "30 C".endswith("C"):
    print("This temperature is in Celsius")
print()



# Transform text into somthing else:



# Other methods that help in situations where text needs to be transformed into something else. So far, you've seen strings that can use C for Celsius and F for Fahrenheit. 
# You can use the .replace() method to find and replace occurrences of a character or group of characters:
print("Saturn has a daytime temperature of -70 degrees Celsius, while Mars has -28 Celsius".replace("Celsius", "C")) # .replace() takes two arguments
print()

# As mentioned earlier, .lower() is a good way to normalize text to do a case-insensitive search. Let's quickly check to see whether some text discusses temperatures:

text = "Temperatures on the Moon can vary widely."
print("temperatures" in text) # will return False because strings are case sensitive
print()
print("temperatures" in text.lower()) # convert string into lowercase and then search
print() 

# You might not need to do case-insensitive verification all the time, but lowercasing every letter is a good approach when the text uses mixed casing.

# After you've split the text and performed the transformations/changes, you might need to put all the parts back together again. Just as the .split() method can separate characters, 
# the .join() method can put them back together.

# The .join() method requires an iterable (such as a Python list) as an argument, so its usage looks different from other string methods:

moon_facts = ["The Moon is drifting away from the Earth."," On average, the Moon is moving away from earth about 4cm every year."]
print(' '.join(moon_facts))   
# In this example, ' ' is used to join every item in the list.
print()


# Next unit: String format in Python
# Besides transforming text and performing basic operations, such as matching and searching, it's essential to format the text when you're presenting information. 

# The simplest way to present text information with Python is to use the print() function. You'll find it critical to get information in variables and other data structures into strings that print() can use.

# In this unit, you'll learn several valid ways to include variable values in text by using Python.

# Percent sign (%) formatting

# The placeholder for the variable in the string is %s. 
# After the string, use another % character followed by the variable name. The following example shows how to format by using the % character:

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." %mass_percentage)

# Using multiple values changes the syntax, because it requires parentheses to surround the variables that are passed in:

print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates arounc its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
print()


#Although this method is still a valid way to format strings, it can lead to errors and decreased clarity in code when you're dealing with multiple variables. Either of the other two formatting options described in this unit would be better suited to this purpose.

# The format() method:
# The .format() method uses braces ({}) as placeholders within a string, and it uses variable assignment for replacing text.

mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
print()

# You don't need to assign repeated variables multiple times, making it less verbose because fewer variables need to be assigned:
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
mass_percentage = "1/6"
print()

# Instead of empty braces, the substitution is to use numbers. The {0} means to use the first (index of zero) argument to .format(), which in this case is Moon. For simple repetition {0} works well, but it reduces readability. To improve readability, use keyword arguments in .format() and then reference the same arguments within braces:
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weigh on Earth.""".format(moon="Moon", mass=mass_percentage)) # using key arguments
print()

# About f-strings
# As of Python version 3.6, it's possible to use f-strings. These strings look like templates and use the variable names from your code. Using f-strings in the preceding example would look like this:

print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
print()



# The variables go within braces, and the string must use the f prefix.

# Aside from f-strings being less verbose than any other formatting option, it's possible to use expressions within the braces. These expressions can be functions or direct operations. For example, if you want to represent the 1/6 value as a percentage with one decimal place, you can use the round() function directly:
print(round(100/6, 1)) # round(number, decimal points) takes two arguments 16.666 = 16.7
print()

# With f-strings, you don't need to assign a value to a variable beforehand:

print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")
print()

# Using an expression doesn't require a function call. Any of the string methods are valid as well. For example, the string could enforce a specific casing for creating a heading:

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)
print()







    
    
        

