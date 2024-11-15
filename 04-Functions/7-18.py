def f(number):
    number_str = str(number)
    digit_count = {}
    for digit in number_str:
        digit_count[digit] = digit_count.get(digit, 0) + 1
    repeated_sum = sum(int(digit) * count for digit, count in digit_count.items() if count > 1)
    return repeated_sum
if __name__ == "__main__":
    print(f(230335))