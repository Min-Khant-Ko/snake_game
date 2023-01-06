from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_scores = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.scoreboard_update()

    def scoreboard_update(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score:{self.high_scores}", align=ALIGNMENT, font=FONT)

    def high_score(self):
        if self.score > self.high_scores:
            self.high_scores = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_scores}")
        self.score = 0
        self.scoreboard_update()

    def score_increase(self):
        self.score += 1
        self.scoreboard_update()
