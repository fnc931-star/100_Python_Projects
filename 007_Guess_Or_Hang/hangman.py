# import random
# import string as str
# from vitual_arts import HANGMANPICS


# def guess_or_hang(word):

      

#     # first convert the each letter in word into underscore '_'
#     word_length = len(word) 
#     hide_word = ['_' for _ in word]   

#     left_life = len(HANGMANPICS)
    
#     while left_life > 0: 

        
#         print(f"Word to Guess: {''.join(hide_word)}")
#         guess_word =  input("Guess a letter: ").lower()

#         if guess_word in word:
#             for index in range(word_length):
#                 if guess_word == word[index]:
#                     hide_word[index] = guess_word
        
#             display = ''.join(hide_word)
#             print(f'{display}') # guessed word in places
#             print(HANGMANPICS[(len(HANGMANPICS) - left_life) - 1]) #the same Hnagman where we were at first 

#         else:
#             left_life -= 1
#             print(f"You guessed {guess_word}, that's not in the word. You lose a life.\n")
            
            
            
#         print(HANGMANPICS[(len(HANGMANPICS) - left_life) - 1])
#         print(f"****************************{left_life}/{len(HANGMANPICS)} LIVES LEFT****************************\n")

        
    
#     if left_life > 1:
#         print("***********************IT WAS pixel! YOU WIN**********************")
        
#     else:
#         print("***********************IT WAS pixel! YOU LOSE**********************")
# words = [
#     "animal", "bright", "candle", "dancer", "finger",
#     "garden", "handle", "island", "knight", "orange",
#     "planet", "pocket", "puzzle", "rabbit", "simple",
#     "silver", "spring", "statue", "sunset", "ground",
#     "hunger", "jungle", "kitten", "window", "lemon",
#     "blanket", "brother", "camping", "captain", "chicken",
#     "country", "diamond", "dolphin", "feather", "kitchen",
#     "lantern", "leopard", "library", "million", "morning",
#     "rainbow", "sandals", "october", "penguin", "shelter",
#     "spinner", "trading", "trumpet", "whisper", "scorpion"
# ]

# word = random.choice(words)

# guess_or_hang(word)




import random
from vitual_arts import HANGMANPICS


def guess_or_hang(word):

    # first convert each letter in word into underscore '_'
    word_length = len(word)
    hide_word = ['_' for _ in word]

    left_life = len(HANGMANPICS)
    won = False  # tracks whether the player guessed the whole word

    while left_life > 0:

        print(f"Word to Guess: {''.join(hide_word)}")
        guess_word = input("Guess a letter: ").lower()

        if guess_word in word:
            for index in range(word_length):
                if guess_word == word[index]:
                    hide_word[index] = guess_word

            display = ''.join(hide_word)
            print(f'{display}')  # guessed word so far

            if '_' not in hide_word:
                won = True
                break  # all letters found -> exit the loop, game is won

        else:
            left_life -= 1
            print(f"You guessed {guess_word}, that's not in the word. You lose a life.\n")

        print(HANGMANPICS[(len(HANGMANPICS) - left_life) - 1])
        print(f"****************************{left_life}/{len(HANGMANPICS)} LIVES LEFT****************************\n")

    if won:
        print(f'***********************IT WAS "{word.upper()}"! YOU WIN**********************')
    else:
        print(f'***********************IT WAS "{word.upper()}"! YOU LOSE**********************')


words = [
    "animal", "bright", "candle", "dancer", "finger",
    "garden", "handle", "island", "knight", "orange",
    "planet", "pocket", "puzzle", "rabbit", "simple",
    "silver", "spring", "statue", "sunset", "ground",
    "hunger", "jungle", "kitten", "window", "lemon",
    "blanket", "brother", "camping", "captain", "chicken",
    "country", "diamond", "dolphin", "feather", "kitchen",
    "lantern", "leopard", "library", "million", "morning",
    "rainbow", "sandals", "october", "penguin", "shelter",
    "spinner", "trading", "trumpet", "whisper", "scorpion"
]

word = random.choice(words) 


