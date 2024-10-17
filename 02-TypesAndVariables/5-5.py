product_price = float(input("Enter price: "))
discount_percentage = float(input("Enter discount %: "))
discount_amount = (discount_percentage / 100) * product_price
discounted_price = product_price - discount_amount
difference = product_price - discounted_price
print(f"\nProduct price: {product_price:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Discounted product price: ${discounted_price:.2f}")
print(f"Reduction: ${difference:.2f}")


