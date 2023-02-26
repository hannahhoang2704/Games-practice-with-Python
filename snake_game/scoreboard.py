from turtle import Turtle


ALIGNMENT = "center"
FONT = ('Arial', 14, 'bold')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.hideturtle()
        self.setpos(0,280)
        self.score = 0
        self.score_status()

    def score_status(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", False,align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score_status()

    """def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align=ALIGNMENT,font=FONT)"""

    def score_increase(self):
        self.score += 1
        self.score_status()
