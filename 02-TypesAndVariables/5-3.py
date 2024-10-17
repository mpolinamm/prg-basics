a = float(input('a='))  
b = float(input('b='))
c = float(input('c='))
cuboid_volume = a * b * c
cuboid_surface_area = 2 * (a * b + b * c + a * c)
print(f'The volume of a cuboid with given sides is {cuboid_volume}')
print(f'The surface area of a cuboid with given sides is {cuboid_surface_area}')