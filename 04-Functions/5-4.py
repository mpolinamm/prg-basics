import turtle
from figures import draw_square

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Side length
side_length = 21

# Call the draw_square function from figures.py
draw_square(side_length)

# Finish
window.mainloop()
