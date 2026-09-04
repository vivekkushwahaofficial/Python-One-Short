while True:
    number = int(input("Enter a number between 1 and 10: "))

    if 1 <= number <= 10:
        print("Number is between 1 to 10")
        break
    else:
        print("Invalid number, try again")