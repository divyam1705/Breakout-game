from turtle import Turtle,Screen
import time
class Pedal:
    def __init__(self):
        self.p1= Turtle(shape="square")
        self.p1.color("white")
        self.p1.hideturtle()
        self.p1.pu()
        self.p1.goto(-425,300)
        self.p1.pd()
        self.p1.goto(425,300)
        self.p1.goto(425,-300)
        self.p1.goto(-425,-300)
        self.p1.goto(-425, 300)
        self.p1.pu()
        self.p1.goto(0, -250)
        self.p1.showturtle()
        self.p1.shapesize(1, 6)

    def right(self):
        if(self.p1.position()[0]<325):
            self.p1.setheading(0)
            self.p1.forward(80)

    def left(self):
        if (self.p1.position()[0] > -325):
            self.p1.setheading(180)
            self.p1.forward(80)

