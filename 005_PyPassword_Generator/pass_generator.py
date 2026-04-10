# Here keep the all backend working functionality so that the project runs smotther and reusable 

def passGenerator(letters , symbols, numbers,pass_length):
    
    return "This is PassGenerator Function"

def requireInputs():
    letters = int(input("How many letters would you like in your password?\n=>\t"))
    symbols = int(input("How many symbols would you like?\n=>\t"))
    digits = int(input("How many numbers would you like?\n=>\t"))

    pass_length= letters+symbols+digits

    return passGenerator(letters, symbols, digits, pass_length)