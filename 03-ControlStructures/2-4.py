number1 = int(input('Enter the first number: '))
number2 = int(input('Enter the second number: '))
operator = input('Enter an operator: ')

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
print(f'{number1} {operator} {number2} = {result}')