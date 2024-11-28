categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_index = expenses.index(max(expenses))

most_expensive_category = categories[max_index]

print(f"The most expensive category is: {most_expensive_category} with an expense of {expenses[max_index]}.")
