import turtle as t

positions = [(0,0), (20,0), (40,0)]

up = 90
down = 270
left = 180
right = 0
#create snake
class Snake:
    def __init__(self):
        self.segments = []
        for pos in positions:
            snake = t.Turtle()
            snake.shape("square")
            snake.color("white")
            snake.penup()
            snake.goto(pos)
            self.segments.append(snake)
        self.head = self.segments[-1]

    def move(self):
        for i in range(0 , len(self.segments) - 1):
            current = self.segments[i]
            next_one = self.segments[i +1]
            next_pos = next_one.pos()
            current.goto(next_pos)
        self.head.forward(20)
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
    
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)