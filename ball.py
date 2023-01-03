from turtle import Turtle
import random
class Ball:
    def __init__(self):
        self.bal=Turtle(shape="circle")
        self.bal.color("white")
        self.bal.pu()
        self.bal.goto(0,20)
        l=random.randint(0,1)
        if l==0:
            self.xmove=-random.randint(7,10)
        else:
            self.xmove=random.randint(7,10)
        self.ymove=-random.randint(7,10)
    def move(self):
        x=self.bal.xcor()+self.xmove
        y=self.bal.ycor()+self.ymove
        self.bal.goto(x,y)
    def reflect(self,dir):
        if(dir=="x"):
            self.ymove=-self.ymove
        elif(dir=="y"):
            self.xmove=-self.xmove


