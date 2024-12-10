numbers = [15, 8, 31, 47, 2, 19]
print("Array:", " ".join(map(str, numbers)))
sum_numbers = 0
for num in numbers:
    sum_numbers += num
arithmetic_mean = sum_numbers / len(numbers)
print(f"Arithmetic mean: {arithmetic_mean:.2f}")