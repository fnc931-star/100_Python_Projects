# Here i implement the backend working scenerio mechanism

def island():
    scenerio_1 = input('You\'re at a cross road. Where do you want to go?\n\tType "left" or "right"\n').lower()

    if scenerio_1 == 'left':
        scenerio_2 = input('You\'ve come to a lake. There is an island in the middle of the lake.\n\tType "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
        
        if scenerio_2 == 'wait':
            scenerio_3 = input('You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow or one blue. Which color do you choose?\n').lower()
            if scenerio_3 == 'yellow':
                print("You Found the Tressure. You Win! 🎊 🎉 🏆 🎉 🎊")
            elif scenerio_3 == 'red':
                print("It's room Full of Fire 🔥🔥🔥. Game Over!")
            elif scenerio_3 == 'blue':
                print("You enter a room full of beasts 🦬. Game Over!")
            else:
                print("Invalid Enrty!")

        elif scenerio_2 == 'swim':
            print("You get Attacked by an angry trout 🐠. Game Over!")
        
        else:
            print("Invalid Enrty!")

    elif scenerio_1 == 'right':
        print("You Fell into a hole 🕳️. Game Over!")
    
    else:
        print("Invalid Enrty!")

