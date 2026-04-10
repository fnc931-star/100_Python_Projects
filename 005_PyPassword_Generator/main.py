import os 
from time import sleep
import visual_art
import pass_generator


if __name__ == "__main__":
    print(visual_art.heading)
    print("\nWELCOME TO THE PYPASSWORD GENERATOR!\n")


    output = pass_generator.requireInputs()

    print(f"Password: {output}")

