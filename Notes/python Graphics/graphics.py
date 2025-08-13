import turtle

pen = turtle.Turtle()
pen.speed(0.8)
pen.color('red')
pen.pensize(3)

pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)
pen.left(90)
pen.forward(100)

pen.penup()
pen.goto(-500, 0)
pen.pendown()

pen.circle(50, 180)

turtle.done()
