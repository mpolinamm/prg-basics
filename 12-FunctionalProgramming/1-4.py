speed = int(input("Enter speed in m/s: "))
ms_to_kmh = lambda ms: ms*3.6
result = ms_to_kmh(speed)
print(f'{speed} m/s is {result} k/h')