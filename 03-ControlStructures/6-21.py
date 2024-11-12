amount = int(input("Enter the amount in PLN: "))

five_pln = 0
two_pln = 0
one_pln = 0

five_pln = amount // 5
amount = amount % 5 

two_pln = amount // 2
amount = amount % 2 

one_pln = amount

print(f"The amount of PLN in coins:")
print(f"5 PLN coins: {five_pln}")
print(f"2 PLN coins: {two_pln}")
print(f"1 PLN coins: {one_pln}")
