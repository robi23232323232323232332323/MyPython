import turtle
t = turtle.Turtle()
t.shape("turtle");

colors=["red", "purple", "blue", "green", "yellow", "orange"]

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 5100 :
    t.forward(length)
    t.pencolor(colors[length%10])
    t.right(50)
    length +=5
