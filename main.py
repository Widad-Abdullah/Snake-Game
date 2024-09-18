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
        score.score_update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on=False
        score.over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_on = False
            score.over()




screen.exitonclick()











