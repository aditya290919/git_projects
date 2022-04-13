import random
def game():
    user=''
    comp_player=random.choice(['Rock','paper','scissors'])

    
    user=input('Enter the player choice: ')

    if user==comp_player:
        print('Its a Tie!')

    elif is_win(user,comp_player):
        print('You Win')

    else:
        print('You Lose')



def is_win(my_player,opponent):

    if ((my_player=='Rock' and opponent=='Scissors') or (my_player=='Scissors' and opponent=='Paper') or (my_player=='paper' and opponent=='Rock')):
        return True
   
game()

