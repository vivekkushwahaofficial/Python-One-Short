# Accepts multiple arguments
def sum_all(*args):
    print(args) # Arguments are stored in a tuple
    for i in args:
        print(i * 2)
    return sum(args) # Returns total

print(sum_all(1, 2, 3, 4))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8))
# print(sum_all(1, 2, 3, 4, 5, 43, 65, 76, 86, 34, 54))

"""
*args → accepts variable number of positional arguments
args  → stores them as a tuple
for   → iterates through each argument
sum() → calculates the total
"""