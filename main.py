import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")  
screen.tracer(0)



snake=Snake()
food=Food()
score=ScoreBoard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.re()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            snake.reset()
            score.reset()





screen.exitonclick()











