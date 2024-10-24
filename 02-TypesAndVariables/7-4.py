circumference = int(input('Enter tree circumference in cm: '))
import math
pi_value = math.pi
diameter = circumference / pi_value
cut_down = diameter >= 50
print(f'Tree can be cut down: {cut_down}')