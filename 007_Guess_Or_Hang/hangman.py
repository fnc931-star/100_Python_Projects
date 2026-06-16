import random
import string as str
from vitual_arts import HANGMANPICS


def guess_or_hang(word):

    hide_word = ['_' for _ in word]
    hide_word = ''.join(hide_word)
    
    print(f"Word to Guess: {hide_word}")
    guess_word =  input("Guess a letter: ").char().lower()

    if guess_word not in word:
        print(f"You guessed {guess_word}, that's not in the word. You lose a life.")
        
        print(f"****************************{len(hide_word)}/{len(word)} LIVES LEFT****************************")

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

guess_or_hang(word)




