# Accepts multiple keyword arguments
def print_kwargs(**kwargs):

    for key, value in kwargs.items():
        print(f"{key}: {value}")  # Print key and value


print_kwargs(name="shaktiman", power="lazer")

print_kwargs(name="shaktiman")

print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jackaal")

"""
**kwargs → accepts variable number of keyword arguments
kwargs   → stores them as a dictionary
.items() → returns key-value pairs
"""