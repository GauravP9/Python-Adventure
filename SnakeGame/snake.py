from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 10

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segements = []
        self.create_snake()
        self.head = self.segements[0]

    def create_snake(self):  # always put self in when defining method . This allows us to use the previously declared variable inside the new method
        for turtle_index in START_POSITIONS:
            self.add_segemnt(turtle_index)

    def move(self):
        for new_seg in range((len(self.segements) - 1), 0, -1):  # len will give no of segments and -1 is step that will decrease after each loop
            # this will start reverse counting so that the last segment will follow the second last and so on.
            new_x = self.segements[new_seg - 1].xcor()  # provides x & y co-ordinate for the segment above the selected segment
            new_y = self.segements[new_seg - 1].ycor()
            self.segements[new_seg].goto(new_x, new_y)  # Provide address to last segment where to move

        self.head.forward(DISTANCE)  # Important as this makes the snake moving , If not mentioned then all square stack up and make one square only

    def up(self):
        if self.head.heading() != DOWN:  # Not allowing to go back in exactly opposite direction
            self.segements[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segements[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segements[0].setheading(LEFT)
        # self.segements[0].fd(10)

    def right(self):
        if self.head.heading() != LEFT:
            self.segements[0].setheading(RIGHT)

    def add_segemnt(self, turtle_index):
        x = Turtle(shape='square')
        x.penup()
        x.color('white')
        x.goto(turtle_index)
        self.segements.append(x)

    def extend(self):
        self.add_segemnt(self.segements[-1].position())

    def reset(self):
        for seg in self.segements:
            seg.goto(1000, 1000)
        self.segements.clear()  # Initialize snake in center again in order to restart the game
        self.create_snake()
        self.head = self.segements[0]

    def border(self):  # For user interface to know the boundaries
        border = Turtle()
        border.color('green')
        border.width(20)
        border.penup()
        border.goto(300, 300)
        for x in range(0, 4):
            border.right(90)
            border.pendown()
            border.forward(600)
