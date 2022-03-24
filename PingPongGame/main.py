import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Initialize Screen settings
screen = Screen()
screen.bgcolor('black')
screen.setup(300, 300)
screen.title('PONG')
screen.tracer(0)  # Animation off

r_paddle = Paddle((300, 0))
l_paddle = Paddle((-300, 0))
ball = Ball()
score = Scoreboard()
# score()
# Screen listen command
screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key='Up')
screen.onkeypress(fun=r_paddle.go_down, key='Down')

screen.onkeypress(fun=l_paddle.go_up, key='w')
screen.onkeypress(fun=l_paddle.go_down, key='s')

ball.border()
game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top & bottom wall
    if ball.ycor() > 310 or ball.ycor() < -310:
        ball.bounce_y()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 280:
        ball.bounce_x()
        score.r_point()
        ball.Speed_Up()

    if ball.distance(l_paddle) < 40 and ball.xcor() < -280:
        ball.bounce_x()
        score.l_point()
        ball.Speed_Up()

    # Detect when not collision
    if ball.xcor() >320:
        ball.reset()
        score.l_point()

    if ball.xcor() < -320:
        ball.reset()
        score.r_point()
screen.exitonclick()
