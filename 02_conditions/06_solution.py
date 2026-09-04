distance = int(input("Enter a number: "))

if distance < 3:
    transMode = "Walk"
elif distance <= 15:
    transMode = "Bike"
else:
    transMode = "Car"
print("Mode of transportation: ", transMode)