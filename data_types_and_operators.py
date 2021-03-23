# Let's see the data types in action

a = 24
b = 16
c = 5.5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a + c)

# Let's check the boolean values
print(a > b)
print(a < b)

# Let's look at some built in methods for boolean
greetings = "Hello world!"
# isalpha() helps us find if the variable holding letters
print(greetings.isalpha())

# islower() checks if the statement is in lower case
print(greetings.islower())

# endswith() checks what the last character is
print(greetings.endswith("!"))

# startswith checks what the first character is
print(greetings.startswith("H"))

# In SQL we have seen Null but in Python we have None which is a key word in python
x = None
print(type(x))

