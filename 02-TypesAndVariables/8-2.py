import math
pi_value = math.pi
radius = int(input('Enter radius: '))
circumference = 2 * pi_value * radius
area = pi_value * radius**2
print(f'The circumference of circle: {circumference:.2f}')
print(f'The area of circle: {area:.2f}')