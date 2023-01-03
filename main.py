import time
from turtle import Turtle,Screen
from breakout import Pedal
from ball import Ball
from blocks import Blocks
s1=Screen()
s1.bgcolor("black")
tur=Turtle(shape="circle")
tur.color("white")
tur.hideturtle()
tur.pu()
tur.goto(0,300)
tur.pd()
s1.setup(850,700)
s1.title("Breakout Game")
ped=Pedal()
s1.listen()
s1.onkey(ped.left,"Left")
s1.onkey(ped.right,"Right")
s1.tracer(0)
bl=Blocks()
b1=Ball()
game_on=True
while(game_on):
    s1.update()
    time.sleep(0.04)
    b1.move()
    if (b1.bal.position()[1]-ped.p1.position()[1]<24 and (b1.bal.position()[0]-ped.p1.position()[0]<85 and b1.bal.position()[0]-ped.p1.position()[0]>-60) and b1.bal.position()[1]-ped.p1.position()[1]>0):
        b1.reflect("x")
    elif(b1.bal.position()[0]<-400 or b1.bal.position()[0]>400 )  :
        b1.reflect("y")
    elif( b1.bal.position()[1]>270)    :
        b1.reflect("x")
    elif(b1.bal.position()[1]<-270):
        game_on=False

    flag=bl.updateblocs(b1.bal.position()[0],b1.bal.position()[1])
    if(flag):
        b1.reflect("x")
    win=bl.winornot()
    tur.clear()
    tur.write(arg=f"Score : {win}", font=('Arial', 20, "normal"), align="center")
    if(win==72):
        tur.write(arg=f"YOU WON", font=('Arial', 30, "normal"), align="center")
s1.exitonclick()