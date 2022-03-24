from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(width=1000,height=500)

y=[-70,-190,-30,-150,50,120,40,180,0]
colors=['red','green','blue','yellow','orange','pink']



t_list=[]
race_on=False

def turtle():
    for x in range(0,6):
        t = Turtle(shape='turtle')
        t.penup()
        t.color(colors[x])
        t.setposition(x=-500,y=(y[x]))
        t_list.append(t)
        t.speed('fastest')


def game():
    user_bet = screen.textinput(title='RACE', prompt='Who will win ?')
    if user_bet:
        race_on = True

    turtle()
    race_on = False
    if user_bet:
        race_on = True
    while race_on:
        race_on_1=True
        while race_on_1:
            for x in t_list:
                if x.xcor() > 480:
                    print(f'won {x.pencolor()}')
                    race_on = False

                    if x.pencolor()==user_bet:
                        print('You won the bet')

                    else:
                        print("better luck next time")

                    user_in=screen.textinput(title="RESTART",prompt='Wanna Resart Type y or n')
                    if user_in=='y':
                        screen.clear()
                        race_on_1 = True
                        game()
                        # input=screen.textinput(title='RACE', prompt='Who will win ?')

                    else:
                        race_on_1=False
                random_no = random.randint(0, 10)
                x.forward(random_no)

game()
screen.exitonclick()