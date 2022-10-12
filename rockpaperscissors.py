import random

def play():
    user = input("What's your choice? 'r' for rock 'p' for paper, 's' for scissors: ")
    computer  = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'
    
    if is_win(user,computer):
        return("You won!")

    return("You lost")



def is_win(player, oppponent):
    if(player=='r'and oppponent=='s' or player=='s' and oppponent=='p' or player=='p' and oppponent=='r'):
        return True

print(play())
