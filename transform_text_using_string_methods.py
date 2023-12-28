# Exercise - Transform text by using string methods
# Exercise: Transform/manipulating strings
# There are several operations you can perform on strings when you manipulate them. In this exercise, 
# you'll use string methods to modify text with facts about the Moon 
# and then extract information to create a short summary.
# Parsing interesting facts about the moon:
# Start by storing the following paragraph in a variable named text:
# Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.

text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.""" # use triple """ for long paragraphs to keep format the same

print(text)
print()

## Separate the paragraph into sentences: .split()

# In English each sentence ends with a period. You will use this to break the paragraph into difference sentences. 
# Using the `split` method to split the text into sentences by looking for the string `. ` (a period followed by a space). Store the result in a variable named `sentences`. Print the result.

print("Spliting sentences into a list:")

sentences = text.split(". ")  # This will look for '. ', a period followed by space, and remove the period and split sentences at period. 
print(sentences)
print()


# Find keywords:
# You will finish your program by adding the code to find any sentences which mention temperature. Add code to loop through the sentences variable. For each sentence, search for the word temperature. If the word is found, print the sentence.

print("Looping through list to find 'temperature': ")

# Solution # 1:
for sentence in sentences:
    if 'temperature' in sentence:
        print(sentence)
print() 

# Solution # 2:
for sentence in sentences:
    sentence.find('temperature')
print(sentence)
print() 




# Solution # 3:
for i in sentences:
    i.find('temperature')
print(i)
print()
    