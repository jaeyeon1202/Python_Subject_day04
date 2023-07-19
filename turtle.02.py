import turtle
import random

turtle.shape("turtle")

for i in range(30):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    turtle.stamp()
    turtle.up()
    turtle.goto(x,y)

turtle.done()