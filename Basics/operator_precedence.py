# operator precedence describes the order in which operations are performed

# Parentheses has the highest precedence,expressions inside parentheses must be evaluated first:
print((6+3) - (6-3))

# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(10 + 5 * 2)

# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5 + 3 - 2 + 4)