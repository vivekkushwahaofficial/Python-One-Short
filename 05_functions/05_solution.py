def greet(name= "User"):
    # f-string
    return f"Hello, {name}!"

print(greet())
print(greet("Vivek"))

print("==============")

def greet(name= "User"):
    # string concatenation
    return "Hello "+ name + "!"

print(greet())
print(greet("Vivek"))

"""
,      → separates values → can create a tuple
+      → joins strings → concatenation
f"..." → inserts variables into a string → f-string
"""