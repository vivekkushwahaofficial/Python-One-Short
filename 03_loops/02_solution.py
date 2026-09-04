numbers = 10

total = 0
for num in range(numbers + 1):
    if num % 2 == 0:
        total += num
print(total)