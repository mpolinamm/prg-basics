previous_price = float(input("Enter the previous price of the product: "))
current_price = float(input("Enter the current price of the product: "))

price_reduction = ((previous_price - current_price) / previous_price) * 100

if price_reduction >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {price_reduction:.2f}%")
else:
    print("No purchase recommendation.")
    print(f"Product price reduced by {price_reduction:.2f}%")