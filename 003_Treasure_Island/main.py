import os
from time import sleep
import visual_art
import tressure_island


if __name__ == '__main__':
    heading, treasure_box = visual_art.ascii_art() 
    print(heading+"\n")
    print(treasure_box+"\n")

    print("\nWELCOME TO TREASURE ISLAND")
    print("Your MISSION is to find the Treasure")

    tressure_island.island()
    
    print("\n================= Thank You for visiting My Island =================")

    sleep(5)

    os.system('clear')




