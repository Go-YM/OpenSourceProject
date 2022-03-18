import turtle

guguLine=""
swidth,sheight=1200,300

turtle.title('거북이로 구구단 출력하기')
turtle.setup(width = swidth+50,height = sheight +50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.shape('turtle')
##2019038003 고영민##
for i in range(1,10):
    for j in range(2,10):
        guguLine=guguLine+str("%dX%d=%2d "%(j,i,j*i))
    turtle.goto(-600,150-i*30)
    turtle.write(guguLine,move = True,font=("",15))
    guguLine=""
