import os
import vitual_arts
import time 
import hangman

if __name__ == "__main__":

    heading = vitual_arts.headings 
    print(heading)

    word = hangman.word  
    hangman.guess_or_hang(word)


    print(f"ThankYou for Using my '{'guess or hang Game'.upper()}")
    time.sleep(7)
    os.system('clear')
    
