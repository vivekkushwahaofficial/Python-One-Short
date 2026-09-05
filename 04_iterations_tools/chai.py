import time

print("chai is here")

username = "Vivek"
print(username)

# ----------------------------------------- #

# Open the file
f = open("chai.py")

# Get the next line
print(f.readline())

# Create an iterator
my_list = [1, 2, 3]
I = iter(my_list)

# Get values one by one
print(next(I))
print(next(I))
print(next(I))