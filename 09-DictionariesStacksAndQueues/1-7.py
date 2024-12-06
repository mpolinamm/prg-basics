inventory = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}
print("Product list:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")
total_products = sum(inventory.values())
print(f"The total number of products in the store: {total_products}")