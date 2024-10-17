import math

def distance_to_horizon(height):
    return 3.57 * math.sqrt(height)
height = float(input("Введіть висоту спостерігача в метрах: "))
height_on_beach = height
distance_beach = distance_to_horizon(height_on_beach)
print(f"Відстань до горизонту: {distance_to_horizon:.2f} км")
height_hotel_window = 20
distance_hotel_window = distance_to_horizon(height_hotel_window)

distance_beach, distance_hotel_window
