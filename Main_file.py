import Other_Files.take_input as OT
class Calc:
    def __init__(self):
        print("Hisab Karlo India")
        starting_ask=input("Want to Start ?\n Enter Y to Continue \n Enter Q To Exit")
        while starting_ask.lower() == "q":
                print("Exiting the calculator. Goodbye!")
                break
        while starting_ask.lower()=="y":
                OT.taking_input()
if __name__ == "__main__":
    app=Calc()