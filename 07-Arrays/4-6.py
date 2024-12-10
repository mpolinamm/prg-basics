numbers = [-15, 8, -31, 47, -2, 19]
max_number = numbers[0]
min_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
    if num < min_number:
        min_number = num
print("The maximum number in array:", max_number)
print("The minimum number in array:", min_number)