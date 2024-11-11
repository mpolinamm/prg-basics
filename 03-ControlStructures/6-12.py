products = int(input('Number of products purchased: '))
price = float(input('Product price: '))
if products > 2:
    total_price = (price * 2) + ((products - 2) * (price * 0.75))
else:
    total_price = products * price
print(f'Amount to pay: {total_price}')