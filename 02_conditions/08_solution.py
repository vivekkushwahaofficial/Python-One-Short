password = input("Enter password: ")
# password = "sec"

if len(password) < 6:
    strength = "Weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Strength: ", strength)
