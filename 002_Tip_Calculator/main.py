import os
from time import sleep
import tip_calculator


print("============================= WELCOME TO THE TIP CALCULATOR =============================\n\n")

if __name__ == "__main__":
    bill_to_each_pay = tip_calculator.tipCalculator()
    print(bill_to_each_pay+"\n")
    print("Thank You For Using Our Calculator")

    sleep(5)

    os.system('clear')