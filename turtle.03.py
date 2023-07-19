import turtle
import random

turtle.shape("turtle")

for i in range(30):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    r=random.randint(1,300)
    turtle.circle(r)
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

turtle.done()