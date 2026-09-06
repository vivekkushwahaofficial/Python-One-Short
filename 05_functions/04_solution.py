import math


# 1. Calculate area and format output to 2 decimal places
def circle_area(radius):
    return math.pi * radius ** 2


radius = float(input("Enter radius: "))
print(f"Area: {circle_area(radius):.2f}")


# 2. Calculate area rounded to 3 decimal places
def circle_area_rounded(radius):
    return round(math.pi * radius ** 2, 3)


radius = float(input("Enter radius: "))
print("Rounded Area:", circle_area_rounded(radius))


# 3. Return multiple values
def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius

    return area, circumference  # returns a tuple


area, circumference = circle_stats(2)  # tuple unpacking

# print("Area:", area, "\nCircumference:", circumference)

print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")


# Quick Reference
"""
input()       → gets input as a string
float()       → converts input to float
** 2          → square
return        → sends a value back
round(..., 3) → rounds to 3 decimal places
:.2f          → displays 2 decimal places
return a, b   → returns a tuple
a, b = ...    → tuple unpacking
"""