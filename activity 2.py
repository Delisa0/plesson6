import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,400)
star = turtle.Turtle()

star.pencolor("pink")
for i in range(5):
    star.forward(70)
    star.right(145)


turtle.done()