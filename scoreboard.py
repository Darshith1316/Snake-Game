from turtle import Turtle
ALIGNMENT= "center"
FONT=('Press Start 2P', 10, "normal")
FONTGO=('Press Start 2P', 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0,275)
        self.score=0

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER!\n  Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

