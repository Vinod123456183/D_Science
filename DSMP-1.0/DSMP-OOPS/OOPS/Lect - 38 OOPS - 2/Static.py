class Atm:


    __counter = 0  

    def __init__(self):
        self.pin = ""
        self.balance = 0
 
        Atm.__counter += 1
        print(f"[INFO] Total ATM objects created: {Atm.get_counter()}")
        self.menu()

    @staticmethod
    def get_counter(): 
        return Atm.__counter

    def createPin(self):
        user_pin = int(input("Enter Pin Please: "))
        self.pin = user_pin
        user_balance = int(input("Enter Balance: "))
        self.balance = user_balance        
        print("Pin Created Successfully")

    def changePin(self):
        oldPin = int(input("Enter Old Pin: "))
        if oldPin == self.pin:
            newPin = int(input("Enter New Pin: "))
            self.pin = newPin
            print("Pin Changed Successfully")
        else:
            print("Incorrect Old Pin")

    def checkBalance(self):
        oldPin = int(input("Enter Pin: "))
        if oldPin == self.pin:
            print("Balance is:", self.balance)
        else:
            print("Enter Correct Pin")

    def withDraw(self):
        inputPin = int(input("Enter Pin: "))
        amount = int(input("Enter Amount To Withdraw: "))

        if inputPin == self.pin:
            if self.balance > 0 and amount <= self.balance:
                self.balance -= amount
                print("Balance Left is:", self.balance)
            else:
                print("Insufficient Balance!")
        else:
            print("Incorrect Pin")

    def menu(self):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Create Pin")
            print("2. Change Pin")
            print("3. Check Balance")
            print("4. Withdraw")
            print("5. Exit")
            
            a = int(input("Enter a number between 1 and 5: "))    
            if a == 1:
                self.createPin()
            elif a == 2:
                self.changePin()
            elif a == 3:
                self.checkBalance()
            elif a == 4:
                self.withDraw()
            elif a == 5:
                print("Exiting ATM...")
                break
            else:
                print("Invalid choice. Try again.")


# 🏁 Creating ATM instances and testing counter
c1 = Atm()
 
print("ATM objects created:", Atm.get_counter())
