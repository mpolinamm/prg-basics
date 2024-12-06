price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Products and prices:")
for product, price in price_list.items():
    print(f"{product}: {price}$")
total_price = sum(price_list.values())
print(f"The total value of the products before the discount: {total_price}$")

print("Products and prices after the 10% discount:")
for product, price in price_list.items():
    price_list[product] = price * 0.9
    print(f"{product}: {price}$")

total_price_discount = sum(price_list.values())
print(f"The total value of the products after the discount: {total_price_discount:.2f}$")