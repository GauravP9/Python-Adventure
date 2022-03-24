from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('cyan')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.x_move = 10
        self.y_move = 10
        self.move_speed=0.1


    def move(self):
        new_x = self.xcor() + self.x_move # everytime move by 10 pix
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        # return self.goto(new_x, new_y)

    def bounce_y(self): # Logic : Decrement by the same amount when first added
        self.y_move *= -1 # Making bounce the ball from top and bottom screen

    def bounce_x(self):
        self.x_move *= -1

    def border(self):  # Draw border
        border = Turtle()
        border.forward(150)
        border.color('red')
        border.pensize(5)
        border.penup()
        border.goto(320, 320)
        for square in range(0, 10):
            border.pendown()
            border.right(90)
            border.forward(640)
        border.hideturtle()

    def reset(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move()
        self.move_speed =0.1

    def Speed_Up(self):
        self.move_speed *= 0.9





