distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter fuel consumption in liters per 100 km: '))
total_fuel_consumption = fuel_consumption * distance / 100
total_cost = total_fuel_consumption * fuel_price
print(f'Total fuel consumption is {total_fuel_consumption} liters')
print(f'Total cost is {total_cost}')