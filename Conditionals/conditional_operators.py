# The and keyword is a logical operator, and is used to combine conditional statements
x = 5
y = 6
z =7
if x < y and y < z:
    print("Both consitions are true")
    
# The or keyword is a logical operator, and is used to combine conditional statements
if x<y or z<x:
    print("either one is true")
    
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement
if not x<y:
    print("x is not greater than y")