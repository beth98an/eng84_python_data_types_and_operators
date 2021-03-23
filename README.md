# Introduction to data types and operators

-  Strings
- numbers integers > floats, longs
- boolean (True or false)

### Arithmetic operators

- Arithmetic operators
```python
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

### Let's have a look at some string methods
```python
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

```