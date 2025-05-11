# single quotes
print('hello')

# double quotes
print("hello")

# we can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("It's alright")
print('He is called "Thandup"')

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string
a = "hello"
print(a)

# We assign a multiline string to a variable by using three quotes
print(''' Lorem ipsum dolor sit amet,  
      consectetur adipiscing elit,
      sed do eiusmod tempor incididunt   
      ut labore et dolore magna aliqua.
      ''')
# Note: in the result, the line breaks are inserted at the same position as in the code.

# Looping through a string
for x in "banana":
    print(x)
    
# To get the length of a string, we the len() function.
a = "thandup"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in
a = "chai with code is best"
print("chai" in a)

# not in 
print("kitkat" not in a)
