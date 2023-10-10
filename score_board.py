import turtle

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.print_score()
        
        
    def print_score(self):
        self.clear()  
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))


