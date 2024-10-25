def sum_digits(number):
    number = abs(number)
    number_str = str(number)
    sum = 0  
    for digit in number_str:
        sum += int(digit)
    return sum
users_number = int(input('Enter integer number: '))
result = sum_digits(users_number)
print(f'The sum of the digits in the number {users_number} is {result}')
