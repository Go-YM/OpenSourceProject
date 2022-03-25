import turtle
import random

myTurtle, tX, tY, tColor, tSize, tShape = [None]*6
playerTurtles = []
tSizeList = []
swidth, sheight =500,500
i = 0

turtle.title('거북이 정렬')
turtle.setup(width = swidth +50,height = sheight+50)
turtle.screensize(swidth,sheight)

##고영민 2019038003##

for i in range(0,5):
    tSize = random.uniform(1,10)
    tSizeList.append(tSize)
    tSizeList = sorted(tSizeList)

for i in range(0,5):
    tX=random.randrange(-swidth / 2, swidth / 2)
    tY=random.randrange(-sheight / 2, sheight / 2)
    r = random.random()
    g = random.random()
    b = random.random()
    playerTurtles.append([tX,tY,r,g,b,tSizeList[i]])
    
myTurtle = turtle.Turtle('turtle')
myTurtle.penup()
myTurtle.goto(playerTurtles[0][0],playerTurtles[0][1])
myTurtle.pendown()


for tList in playerTurtles:
    myTurtle.color((tList[2],tList[3],tList[4]))
    myTurtle.pencolor((tList[2],tList[3],tList[4]))               
    myTurtle.turtlesize(tList[5])
    myTurtle.goto(tList[0],tList[1])
    myTurtle.stamp()
    tX=tList[0]
    tY=tList[1]

turtle.done()
