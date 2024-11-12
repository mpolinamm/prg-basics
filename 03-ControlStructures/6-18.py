x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x == 0 and y == 0:
    print("The point P(0, 0) is located at the origin.")
elif x == 0:
    print(f"The point P({x}, {y}) is located on the y-axis.")
elif y == 0:
    print(f"The point P({x}, {y}) is located on the x-axis.")
elif x > 0 and y > 0:
    print(f"The point P({x}, {y}) is located in the first quadrant.")
elif x < 0 and y > 0:
    print(f"The point P({x}, {y}) is located in the second quadrant.")
elif x < 0 and y < 0:
    print(f"The point P({x}, {y}) is located in the third quadrant.")
elif x > 0 and y < 0:
    print(f"The point P({x}, {y}) is located in the fourth quadrant.")
