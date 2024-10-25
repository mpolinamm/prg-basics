import math
def triangle_area(a,b,c):
    s = (a + b + c) / 2
    formula = math.sqrt(s*((s-a)*(s-b)*(s-c)))
    return formula
triangle1 = triangle_area(3, 4, 5)
triangle2 = triangle_area(5, 12, 13)
triangle3 = triangle_area(7, 24, 25)
print(f'The area of ​​a triangle with sides 3, 4, 5 is {triangle1}')
print(f'The area of ​​a triangle with sides 5, 12, 13 is {triangle2}')
print(f'The area of ​​a triangle with sides 7, 24, 25 is {triangle3}')