from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-270, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.level += 1
        self.goto(-270, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.goto(-100, 0)
        self.write("Game Over", align="left", font=FONT)

