import random
dice_roll = random.randint(1,6)
special_number = dice_roll == 1 or dice_roll == 6
print(f'Dice rolled: {dice_roll}')
print(f'Special number (1 or 6): {special_number}')