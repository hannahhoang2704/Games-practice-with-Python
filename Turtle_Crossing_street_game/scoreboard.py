from turtle import Turtle
FONT = ("Courier", 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(-280, 250)
        self.level_number = 1
        self.level_status()

    def level_status(self):
        self.clear()
        self.write(f"Level: {self.level_number}", False, align="left", font=FONT)

    def lvl_increase(self):
        self.level_number += 1
        self.level_status()

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align='center', font=FONT)

