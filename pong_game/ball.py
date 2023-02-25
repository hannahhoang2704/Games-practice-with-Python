from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1


    def move(self):
        newx = self.xcor() + self.xmove
        newy = self.ycor() + self.ymove
        self.goto(newx,newy)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0,0)          #set the ball back to original position
        #let the other player start the turn
        self.bounce_x()




