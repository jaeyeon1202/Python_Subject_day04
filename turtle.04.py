import turtle
import random

turtle.shape("turtle")
a=["red","yellow","pink","black","gray","blue","green","purple"]

for i in range(30):
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    r=random.randint(30,70)
    turtle.pencolor(random.choice(a))
    turtle.pensize(random.randint(1,10))
    turtle.circle(r,steps=random.randint(3,7))
    turtle.up()
    turtle.goto(x,y)
    turtle.down()

turtle.done()