number = int(input("Enter a number: "))

is_even = lambda number: number % 2 == 0

if is_even(number):
    print(f"Number {number} is even")
else:
    print(f"Number {number} is odd")