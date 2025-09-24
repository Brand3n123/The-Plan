def multiply_all(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply_all(1, 8, 9, 17))