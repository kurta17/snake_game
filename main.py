from turtle import Screen
import turtle as t
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard
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
#Board
score_board = ScoreBoard()

def check_body():
    head_pos = snake.head.position()
    for i in snake.segments[::-1]:
        if head_pos  == i.position:
            score_board.game_over()
            break

while True: 
    time.sleep(0.1)
    check_body()
    snake.move()
    if snake.head.distance(food) < 20:
        snake.extend_snake()
        score_board.increase_score()
        food.food_pos()    
        screen.update()
    
    
    score_board.print_score()
    score_board.print_record()

    if snake.head.xcor()<-290 or snake.head.ycor() <-290 or snake.head.xcor() >290 or snake.head.ycor() > 290:
        
        score_board.game_over()
        score_board.print_score()
        score_board.print_record()
        time.sleep(1)
        snake.go_back()
        
        screen.update()
    
    screen.update()
    

t.done()
t.mainloop()
screen.exitonclick()