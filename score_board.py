import turtle

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.record = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.print_score()
        self.print_record()
        
        
    def print_score(self):
        self.clear()  
        self.goto(-150,260)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_record(self):
        self.goto(150,260)
        self.write(f"Record: {self.record}", align="center", font=("Arial", 24, "normal"))    

    def game_over(self):
        if self.score > self.record:
            self.record = self.score
        self.goto(0,0)
        self.score = 0
        self.write(f"Game Over", align="center", font=("Arial", 24, "normal"))


