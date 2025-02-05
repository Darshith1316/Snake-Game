from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake it!!")
screen.tracer(0)

snake = Snake()
food=Food()
score=Score()


#from keyboard now convert to phone
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")

on=True

while on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    score.update_score()


    #detect collision between food and the snake
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


    #detect collision with wall
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-295 or snake.segments[0].ycor()>295 or snake.segments[0].ycor()<-295:
        food.remove()
        score.reset()
        snake.reset()


    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment)<5:
            score.reset()
            snake.reset()


screen.exitonclick()