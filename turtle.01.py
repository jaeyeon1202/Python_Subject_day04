import turtle
turtle.shape("turtle")

for i in range(5):
    x=int(input("x좌표:"))
    y=int(input("y좌표:"))
    turtle.up()
    turtle.goto(x,y)
    turtle.stamp()
 


turtle.done()