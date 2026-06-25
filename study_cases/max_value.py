numbers = [-5, 170, 999, 123, -10000, 128, 3, 4, 5]

maximum = numbers[0]
for number in numbers:
    if number > maximum:
        maximum = number

print(f"Максимум: {maximum}")
print("Максимум: " + str(maximum))
