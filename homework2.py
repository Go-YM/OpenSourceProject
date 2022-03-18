import turtle
import random
import math

swidth,sheight = 300,300
angle,distance = 0,0
a=1

turtle.title('거북이 만나기')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.penup()
t2.penup()
t3.penup()
##2019038003 고영민##
t1.color('red')
t2.color('blue')
t3.color('green')

t1.shape('turtle')
t2.shape('turtle')
t3.shape('turtle')

t1.goto(-50,-50)
t2.goto(0,0)
t3.goto(50,50)

while True:
    
    angle = random.randrange(0,360)
    distance =random.randrange(1,50)
    t1.left(angle)
    t1.forward(distance)

    angle = random.randrange(0,360)
    distance =random.randrange(1,50)
    t2.left(angle)
    t2.forward(distance)

    angle = random.randrange(0,360)
    distance =random.randrange(1,50)
    t3.left(angle)
    t3.forward(distance)

    t1x=t1.xcor()
    t1y=t1.ycor()

    t2x=t2.xcor()
    t2y=t2.ycor()

    t3x=t3.xcor()
    t3y=t3.ycor()

    if math.sqrt(((t1x-t2x))**2+((t1y-t2y)**2)) <= 10 or math.sqrt(((t2x-t3x))**2+((t2y-t3y)**2)) <= 10 or math.sqrt(((t1x-t3x))**2+((t1y-t3y)**2)) <= 10 :
        a *= 3
        t1.turtlesize(a)
        t2.turtlesize(a)
        t3.turtlesize(a)

turtle.done()
    
    
    
