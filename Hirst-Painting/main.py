import random
import turtle as t
from turtle import Turtle, Screen
import colorgram

timmy = Turtle()
timmy.pensize(5)
timmy.speed('fastest')

t.colormode(255)

def random_color():
    r=random.randint(0,255)
    y = random.randint(0, 255)
    b = random.randint(0, 255)
    tuple=(r,y,b)
    return tuple
# color = ('red', 'pink', 'yellow', 'green', 'blue', 'brown')

direction=[0,90,180,270]

def random_walk():
    for _ in range (1000):
        timmy.pencolor(random_color())
#       # RANDOM MOVEMENT CHALLENGE
#          timmy.forward(20)
#          timmy.setheading(random.choice(direction))

        # RANDOM CIRCLE CHALLENGE
        # timmy.circle(100)
        # timmy.setheading(timmy.heading()+random.randint(0,10))
# def draw(side):
#     c = random.choice(color)
#     timmy.color(c)
#     angle=360/side
#     for _ in range(side):
#         timmy.forward(100)
#         timmy.right(angle)
#
#     for _ in range(side):
#         timmy.left(angle)
#         timmy.forward(100)

timmy.shape('turtle')

for side in range (1):
    random_walk()
# for side in range(3,11):
#     draw(side)





screen = Screen()
screen.exitonclick()
