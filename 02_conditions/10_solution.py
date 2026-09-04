pet = input("Enter pet species: ")
age = int(input("Enter pet age: "))

if age < 2 and pet == "Dog":
    food = "Puppy food"

elif age > 5 and pet == "Cat":
    food = "Senior cat food"

else:
    food = "Regular food"