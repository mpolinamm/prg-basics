def f(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    first_three_digits = product_code[:3]
    control_digit = int(product_code[3])
    sum_of_digits = sum(int(digit) for digit in first_three_digits)
    return control_digit == sum_of_digits % 7
if __name__ == "__main__":
    print(f("2035")) 
    print(f("7071")) 