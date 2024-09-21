from turtle import Turtle




class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} Best: {self.highscore}",False,"center",font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode='w') as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.score_update()

    def increase_score(self):
        self.score += 1
        self.score_update()



    # def over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", False, "center", font=('Arial', 16, 'normal'))


