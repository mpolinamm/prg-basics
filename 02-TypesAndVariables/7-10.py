import random
computer = random.randint(1,6)
you = int(input('Enter number from 1 to 6: '))
number = you == computer 
print(computer)
print(f'You won: {number}')