from turtle import Turtle
ALIGNMENT= "center"
FONT=('Press Start 2P', 10, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0,275)
        self.score=0
        with open("data.txt") as file:
            self.highscore=int(file.read())

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score>int(self.highscore):
            self.highscore=self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score=0
        self.clear()
        self.update_score()

    def increase_score(self):
        self.score+=1
        self.update_score()
    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER!\n  Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

