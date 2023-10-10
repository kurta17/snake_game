from turtle import Screen
import turtle as t
import time
from snake import Snake
from food import Food
#screen 
screen = Screen()
screen.title("Snake Game")
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

#food

food = Food()
while True: 
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)< 20:
        food.food_pos()
    screen.update()
    



screen.exitonclick()