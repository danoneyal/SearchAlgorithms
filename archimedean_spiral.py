import math
import turtle

screen = turtle.Screen()
offset_x = 0
offset_y = 0
factor = 1.0  # controls the distance between successive turnings
a = 0  # turns the spiral
smooth_factor = 20.0
for i in range(5000):
    angle = i / smooth_factor * math.pi
    x = offset_x + (angle * factor + a) * math.cos(angle)  # dx  theta * cos(theta)
    y = offset_y + (angle * factor + a) * math.sin(angle)  # dy  theta * sin(theta)

    turtle.goto(x, y)

screen.exitonclick()
