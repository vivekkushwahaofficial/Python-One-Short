def cube(num):
    return num ** 3
print(cube(3))

print("====")
cube = lambda x: x ** 3
print(cube(3))

"""
Normal function:

def → function name → parameters → return

Lambda:

lambda → parameters → expression

Lambda → small, one-expression anonymous function
"""