# Here is the proper functional game based on randomization and conditional operations (if,elif,else)
import random 
import visual_arts

# 0 for Rock 
# 1 for Paper
# 2 for Scissor

art = {0: visual_arts.rock,
       1: visual_arts.paper,
       2: visual_arts.scissor}

def computer_choice(user,comp):
    if comp == 0 and user == 2: # Rock beats Scissor
        return True
    elif comp == 1 and user == 0 : # Paper beats Rock
        return True
    elif comp == 2 and user == 1: # Scissor beats Paper
        True
    else:
        return False
    


def user_choice(user, comp):
    if user == 0 and comp == 2: # Rock beats Scissor
        return True
    elif user == 1 and comp == 0: # Paper beats Rock
        return True
    elif user == 2 and comp == 1: # Scissor beats Paper
        return True
    else:
        return False
   
def score(user, comp):
    if user == comp:
       return "It's a Draw!"
    elif user_choice(user,comp) == True:
        return "You Win!"
    elif computer_choice(user,comp) == True:
        return "You Lose"
    else:
        return "You typed an invalid number, You lose!"










