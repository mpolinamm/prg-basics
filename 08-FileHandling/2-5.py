shopping_list = 'shopping_list.txt'

def add_product(file_name, product_name):
   with open(shopping_list,'a') as file:
      file.write(product_name + '\n')

product = ""
while product != "0":
   product = input('Enter product name (0 stops): ')
   if product == '0':
      break
   else:
      add_product(shopping_list, product)

print(f"Your shopping list has been saved to {shopping_list}.")