# Generates even numbers up to the limit
def even_generator(limit):

    for i in range(2, limit + 1, 2):
        yield i  # Produces one value at a time


for num in even_generator(10):
    print(num)


"""
yield   → gives a value and pauses the function
return  → gives a value and ends the function
generator → remembers its state between values
"""