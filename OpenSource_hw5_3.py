import turtle
import random
from tkinter.simpledialog import*
import math

inStr = ''
swidth,sheight = 500,500
radius,angle,radian = 200,0,0
txtSize = 20
tX,tY = [0]*2

turtle.title('거북이 글자쓰기')
turtle.shape('turtle')
turtle.setup(width = swidth + 50, height = sheight + 50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr=askstring('문자열 입력', '거북이 쓸 문자열을 입력')

angle = 360/len(inStr)

##2019038003 고영민##

for ch in inStr:
    radian = 3.14*angle/180
    tX = radius*math.cos(radian)
    tY = radius*math.sin(radian)
    r = random.random()
    g = random.random()
    b = random.random()

    turtle.goto(tX,tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font=('맑은고딕',txtSize,'bold'))
    angle += 360/len(inStr)
    radius -= radius/len(inStr)

turtle.done()
