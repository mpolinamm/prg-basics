import turtle
def draw_square(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(4):
        pen.forward(length)
        pen.right(90)
    pen.hideturtle()
def draw_triangle(length):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(3):
        pen.forward(length)
        pen.right(120)
    pen.hideturtle()
def draw_rectangle(lenght_a, lenght_b):
    pen = turtle.Turtle()
    pen.speed(5)
    for _ in range(2):
        pen.forward(lenght_a)
        pen.right(90)
        pen.forward(lenght_b)
        pen.right(90)
    pen.hideturtle()