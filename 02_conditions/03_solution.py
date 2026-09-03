mark = int(input("Enter a marks: "))
if mark > 100 or mark < 0:
    print("Please verify your grade again")
else:
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)
