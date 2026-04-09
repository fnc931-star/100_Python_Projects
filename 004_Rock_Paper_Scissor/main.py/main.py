# main file 
import os
from time import sleep
import random
import visual_arts
import rocking_game


if __name__ == "__main__":
    print(f"\t\t {visual_arts.heading}")

    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor.\n"))
    comp = random.randint(0,2)

    print(rocking_game.art[user])
    print("\nComputer Chose:\n",rocking_game.art[comp])

    result = rocking_game.score(user,comp)

    print(f"\n\t\t\t\t{result}\n")
    print("\t\tThankYou For Playing My Rocking Game!😎🥰🤗")

    sleep(5)
    os.system('clear')


