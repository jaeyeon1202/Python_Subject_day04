import turtle
turtle.shape("turtle")

r=int(input("반지름:"))

turtle.circle(r)
turtle.up()
turtle.goto(0,2*r)
turtle.down()
turtle.circle(r/2)

turtle.done()