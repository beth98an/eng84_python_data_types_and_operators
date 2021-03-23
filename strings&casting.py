# Strings and Casting

# Let's have a look at some industry practices

# single and double quotes

single_quotes = 'single quotes \'wow\''
double_quotes = "double quotes 'wow'"
print(single_quotes)
print(double_quotes)

# String slicing
greetings = "Hello world!"  # string
# indexing in Python starts from 0
# H e l l o   w o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
# how can we find out the length of this statement/string
print(len(greetings))
# we have a method called len() to find out the total length of the statement
print(greetings[0:5])  # outputs Hello from 0 to 4
print(greetings[6:11])

# reverse indexing starts with -1
print(greetings[-1])
print(greetings[-6:])

# Let's have a look at some string methods
white_space = "lot's of space at the end                   "
# strip() helps us delete all white spaces
print(len(white_space))
print(len(white_space.strip()))

Example_text = "here's some text with lot's of text"
print(Example_text.count("text"))
# Counts the number of times the word is mentioned in the statement
print(Example_text)
print(Example_text.upper())  # converts to upper case
print(Example_text.lower())  # converts to lower case
print(Example_text.capitalize())  # capitalises first letter of string
print(Example_text.replace("with", ","))  # will replace the word "with" with a , in this case

# Concatenation and casting

first_name = "Harry"
last_name = "Potter"
age = 35  # int
print(first_name + " " + last_name)
print(first_name + " " + last_name + " " + str(age))
# str() converts integer to string in this case

# F-String is an amazing Magical formatting f
print(f"{first_name} {last_name} is {age} years old")
