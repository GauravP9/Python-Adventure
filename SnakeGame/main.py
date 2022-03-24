import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(300, 300)
screen.bgcolor('black')
screen.title('snake game')
screen.tracer(0)

game = True

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)
# screen.
snake.border()
while game:
    screen.update()
    time.sleep(.1)
    snake.move()
    score.update_score()
    # Detect contact with food.
    if snake.head.distance(food) < 10:
        food.food_refresh()
        snake.extend()
        score.increase_score()

    # Detect contact with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect contact with itself
    # If head collide with body segment , Game Over
    for segement in snake.segements[1:]: # Using slicing to skip head position to detect collison
        if snake.head.distance(segement) < 5:
            score.reset()
screen.exitonclick()
