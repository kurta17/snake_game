from turtle import Screen
import turtle as t
segments = []
positions = [(0,0), (20,0), (40,0)]
for pos in positions:
    snake = t.Turtle()
    snake.shape("square")
    snake.color("white")
    snake.goto(pos)
    segments.append(snake)


#screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)

screen.exitonclick()
