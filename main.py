from turtle import Screen
from snake import Snake
from food import SnakeFood
from scoreboard import Score
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Snake game")

snake = Snake()
food = SnakeFood()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        score.increase_score()
    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
       score.reset()
       snake.reset()
    for segment in snake.segaments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            score.reset()
            snake.reset()
        
screen.exitonclick()
























