import turtle as t
import random 
class Food(t.Turtle):
    def __init__(self):
        super().__init__()  
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0,100)
        self.food_pos()

    def food_pos(self):
        self.goto(random.randint(-290,290),random.randint(-290,290))




