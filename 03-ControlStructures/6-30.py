import random

numbers = list(range(1, 50))

random.shuffle(numbers)

for i in range(7): 
    for j in range(7):  
        print(numbers[i + j * 7], end=' ')  
    print()

