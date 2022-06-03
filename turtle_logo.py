import turtle 

turtle.Screen().bgcolor("black")
turtle.title("microsoft logo")
t = turtle.Turtle()


t.pensize(5)


t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.left(90)
t.forward(100)
t.pendown()

t.begin_fill()
t.fillcolor("green")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()


t.begin_fill()
t.fillcolor("yellow")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.begin_fill()
t.fillcolor("blue")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()



turtle.done()
