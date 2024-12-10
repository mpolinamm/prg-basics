numbers = [8, 2, 5, 1, 9]

print("Array::", " ".join(map(str, numbers)))

squared_numbers = [num ** 2 for num in numbers]

print("2nd power:", " ".join(map(str, squared_numbers)))
