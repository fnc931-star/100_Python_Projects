# THis a file which works like a module 

def tipCalculator():
    bill = float(input("What was the total bill? $"))
    tip = float(input("How much tip would you like to give? 10, 12 or 15? $"))
    split = int(input("How many people to split the bill? "))

    tip_paisa = bill * (tip/100) 

    total_bill = bill + tip_paisa
 

    return f"Each person should pay: ${total_bill/split:.2f}"


