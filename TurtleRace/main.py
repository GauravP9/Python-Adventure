import turtle
from turtle import Turtle,Screen

tim=Turtle()

# def move():
def forward():
    tim.forward(100)


def left():
    tim.left(10)
    # tim.forward(100)


def back():
    # tim.left(180)
    tim.bk(100)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def right():
    tim.right(10)

# forward()

# def move():
#     turtle.fd(100)



screen=Screen()
screen.listen()
screen.onkey(fun=forward,key="w")
screen.onkey(fun=back,key="s")
screen.onkey(fun=left,key="a")
screen.onkey(fun=right,key="d")
screen.onkey(fun=clear,key="c")
screen.onkey(fun=right,key="d")
screen.exitonclick()
