import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(400,400)
polygon = turtle.Turtle()

num_sides = 4
side_length = 120
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.left(angle)


turtle.done()