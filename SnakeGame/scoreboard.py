from turtle import Turtle

# Contains all the writing
FONT = ('Courier ', 24, 'italic')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt', mode="r") as data:  # Reading the data from txt file
            self.high_score = int(data.read())

        self.score = 0
        self.goto(0, 320)
        self.penup()
        self.color('white')
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score :{self.score},   High Score {self.high_score}", align='center', font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open('data.txt', mode="w") as data:  # Writing the high score in txt file
                data.write(str(self.high_score))

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
        self.write(f"Score :{self.score}", align='center', font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.color('red')
    #     self.write(f"Game Over", align='center', font=FONT)
