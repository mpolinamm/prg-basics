numbers = [15, 8, 31, 47, 2, 19]
print("Array:", " ".join(map(str, numbers)))
sum_numbers = 0
index = 0
while index < len(numbers):
    sum_numbers += numbers[index]
    index += 1
arithmetic_mean = sum_numbers / len(numbers)
print(f"Arithmetic mean: {arithmetic_mean:.2f}")