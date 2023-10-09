from turtle import Screen
import turtle as t
import time
from snake import Snake
#screen 
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)

#animation
screen.tracer(0)

#move snake
snake = Snake()
screen.listen()
screen.onkey(snake.up, key="Up") 
screen.onkey(snake.left, key="Left") 
screen.onkey(snake.right, key="Right") 
screen.onkey(snake.down, key="Down") 

while True: 
    time.sleep(0.25)
    snake.move()
    screen.update()



screen.exitonclick()