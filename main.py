from turtle import Screen
import turtle as t
import time

#create snake
segments = []
positions = [(0,0), (20,0), (40,0)]
for pos in positions:
    snake = t.Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(pos)
    segments.append(snake)


    


#screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)

#animation
screen.tracer(0)

#move snake

# def go_right():
    # for i in segments:
    #     i.setheading(0)
    #     i.forward(20)

while True: 
    time.sleep(1)
    for i in segments:
        i.setheading(0)
        i.forward(20)
        snake.penup()
    screen.update()


screen.exitonclick()