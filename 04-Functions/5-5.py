import turtle
from figures2 import draw_square, draw_triangle, draw_rectangle
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw first square at initial position
pen.penup()
pen.goto(-100, 100)  # Move the turtle to (-100, 100)
pen.pendown()
draw_square(100)

# Draw second square at a different position
pen.penup()
pen.goto(100, 100)  # Move to a new position (100, 100)
pen.pendown()
draw_square(100)

# Draw first rectangle at initial position
pen.penup()
pen.goto(-100, -100)  # Move to (-100, -100) for rectangle
pen.pendown()
draw_rectangle(150, 100)

# Draw second rectangle at a different position
pen.penup()
pen.goto(100, -100)  # Move to a new position (100, -100)
pen.pendown()
draw_rectangle(150, 100)

# Draw first isosceles triangle at initial position
pen.penup()
pen.goto(-200, 200)  # Move to (-200, 200) for triangle
pen.pendown()
draw_triangle(100)

# Draw second isosceles triangle at a different position
pen.penup()
pen.goto(200, 200)  # Move to a new position (200, 200)
pen.pendown()
draw_triangle(100)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
