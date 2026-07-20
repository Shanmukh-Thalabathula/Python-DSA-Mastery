"""
Multiple assignment and swapping variables.
"""

x = 10
y = 20

print("Before Swap")
print(x, y)

x, y = y, x

print("After Swap")
print(x, y)

a = b = c = 100

print(a, b, c)