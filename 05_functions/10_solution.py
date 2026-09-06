# Calculates factorial using recursion
def factorial(n):

    if n == 0:
        return 1  # Base case

    else:
        return n * factorial(n - 1)  # Recursive call


print(factorial(5))

"""
recursion → a function calls itself
base case → condition that stops recursion
factorial → n * (n - 1) * ... * 1
"""