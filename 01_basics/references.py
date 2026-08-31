# Object References in Python

# Example 1: Two variables referring to the same object
n = [1, 2, 3]
m = n

print(n)
print(m)

print(n == m)  # True: same values
print(n is m)  # True: same object

# Changing m also changes n
m.append(4)

print(n)  # [1, 2, 3, 4]
print(m)  # [1, 2, 3, 4]


# Example 2: Two different objects with the same values
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)  # True: same values
print(x is y)  # False: different objects

# Changing y does not change x
y.append(4)

print(x)  # [1, 2, 3]
print(y)  # [1, 2, 3, 4]


# Example 3: Immutable object
a = 5
b = 2

a = a + 2

print(a)  # 7
print(b)  # 2