decimal_number = int(input("Enter decimal number: "))

original_number = decimal_number

binary_digits = []

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_digits.append(remainder)  
    decimal_number = decimal_number // 2  

binary_digits.reverse()

binary_number = ''.join(map(str, binary_digits))

print(f"{original_number}(10) = {binary_number}(2)")
