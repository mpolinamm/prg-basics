def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]

print("Original car fuel consumption:", car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)

print("Original bank transactions:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print("Sorted bank transactions:", sorted_bank_transactions)
