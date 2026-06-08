# Here keep the all backend working functionality so that the project runs smotther and reusable 
import random 
import string # which is helpfull for alphabets 


def passGenerator(letters , symbols, numbers, pass_length):

    if pass_length < 5:
        return "Sorry! the password length is short, try to increase the Password Length."

    alphabets_ = ''.join(random.choices(string.ascii_letters, k=letters))
    punctuations_ = ''.join(random.choices(string.punctuation, k=symbols))
    digits_ =  ''.join(random.choices(string.digits, k=numbers))

    password = alphabets_ + punctuations_ + digits_ 
    password = list(password)
    random.shuffle(password)
    
    return f"Here's the Password: {''.join(password)}"


def requireInputs():
    try:

        letters = int(input("How many letters would you like in your password?\n=>\t"))
        symbols = int(input("How many symbols would you like?\n=>\t"))
        digits = int(input("How many numbers would you like?\n=>\t"))

        pass_length= letters+symbols+digits 

        return passGenerator(letters, symbols, digits, pass_length)

    except ValueError as e:
        print(f"Exception: {e}")

