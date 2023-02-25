import turtle
from turtle import Turtle
import random

turtle.colormode(255)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed(0)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

    def new_food(self):
        r = random.randint(1,250)
        g = random.randint(1, 250)
        b = random.randint(1, 250)
        self.color(r,g,b)
