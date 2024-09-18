from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}",False,"center",font=('Arial', 20, 'normal'))
        self.score += 1

    def over(self):
        self.goto(0,0)
        self.write("GAME OVER!", False, "center", font=('Arial', 16, 'normal'))


