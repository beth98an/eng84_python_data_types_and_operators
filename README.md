# Introduction to data types and operators

-  Strings
- numbers integers > floats, longs
- boolean (True or false)

### Arithmetic operators

- Arithmetic operators are
```
+, -, *, /
```
 - Modulus
```%``` It gives the remainder of the two numbers
   
### Comparison operators
- Comparison operators
- `>` greater than
- `<` less than
- `==` equal to
- `!=` not equal to
- `>=` greater than and equal to
- `<=` less than and equal to

### Strings and casting

- indexing in Python starts from 0
- `H e l l o   w o r l d  !`
- `0 1 2 3 4 5 6 7 8 9 10 11`

- Reverse indexing starts with -1
- `H e l l o   w o r l d  !`

### String methods
- `.strip()` helps us delete all white spaces
```
white_space = "lot's of space at the end                   "
print(len(white_space))
print(len(white_space.strip()))
```
- `.count()`Counts the number of times the word is mentioned in the statement.
```
Example_text = "here's some text with lot's of text"
print(Example_text.count("text"))
```
- `.upper()` converts to upper case.
- `.lower()` converts to lower case.
- `.capitalize()` capitalises first letter of string.
- `.replace(item, new item)` will replace the item with the new item.
  In the case below "with" is replaced with a comma.
```
print(Example_text.upper())
print(Example_text.lower())
print(Example_text.capitalize())
print(Example_text.replace("with", ","))
```
### Concatenation
To concatenate two strings together use the `+` between them.
It will not automatically add a space between them, so you will have to add it in manually.
```
first_name = "Harry"
last_name = "Potter"
age = 35  # int
print(first_name + " " + last_name)
print(first_name + " " + last_name + " " + str(age))
```
- str() converts integer to string in the above case.

### F - String

- f-string is a faster, more readable, more concise,
  and less error prone way of formatting a string.
- f-strings have the f prefix and use {} brackets to evaluate values.
```
print(f"{first_name} {last_name} is {age} years old")
```