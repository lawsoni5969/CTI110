import turtle
turtleScreen = turtle.Screen()
t = turtle.Turtle()
x = 0

while(x < 4):
    t.forward(50)
    t.left(90)
    x = x + 1

t.penup()
t.forward(100)
t.pendown()

for i in range(3):
    t.forward(50)
    t.left(120)

