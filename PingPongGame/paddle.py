from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        # Initialize turtle class for creating turtle
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)  # Sending them to required position

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)
        if self.ycor() > 260: # Lock paddle not to go out of border
            self.goto(x=self.xcor(), y=260)

    def go_down(self):
        new_y = self.ycor() + -20
        self.goto(x=self.xcor(), y=new_y)
        if self.ycor() < -260: # Lock paddle not to go out of border
            self.goto(x=self.xcor(), y=-260)




