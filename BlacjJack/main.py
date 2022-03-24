import random 

def deal_card(): # generating random card out of the given list of variables
  cards=[11,2,3,4,5,6,7,8,9,10,10,10]
  return random.choice(cards)

user_card=[]    #start out the list as empty list. 
computer_card=[]    #start out the list as empty list.

for _ in range(0,2):    # dealing first 2 cards to user and computer
  user_card.append(deal_card())
  computer_card.append(deal_card())

def calculate_score(cards):   # Function for calculating sum and evaluate different condition for same.
  '''Calculate score of the random variable that are generated previously'''
  if sum(cards)==21 and len(cards)==2:
    return 0 
  
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

is_game_over=True

while is_game_over==True:
    user_score=calculate_score(user_card)   
    print(f"Your cards : {user_card}, current score {user_score}")   #checking total sum of users card

    computer_score=calculate_score(computer_card)   
    print((f"Your Computer's first cards is : {computer_card[0]}")  )    #checking comp cards sum

    if user_score==0 or computer_score==0 or user_score>=21:    #game over condition
        is_game_over=False
    else:
        next_card = input("Type 'y' to put another card and 'n' for pass ")
        if next_card == "y":
            user_card.append(deal_card())
        else:
            is_game_over=True
