def ms_to_kmh(ms):
    return ms*3.6

speed = int(input("Enter speed in m/s: "))

result = ms_to_kmh(speed)

print(f'{speed} m/s is {result} k/h')