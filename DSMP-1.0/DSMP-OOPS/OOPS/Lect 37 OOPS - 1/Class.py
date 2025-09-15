class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def createPin(self):
        user_pin = int(input("Enter Pin Please "))
        self.pin = user_pin
        user_balance = int(input("Enter Balance "))
        self.balance = user_balance        
        print("Pin Created Successfully ")


    def changePin(self):
        oldPin = int(input("Enter Old Pin "))
        if oldPin == self.pin:
            newPin = int(input("Enter New Pin "))
            self.pin = newPin
            print("Pin Changes Successfully ")
            self.menu()
        else:
            print("Sorry")
            self.menu()

    def checkBalance(self):
        oldPin = int(input("Enter Pin : "))
        userPin = self.pin
        if oldPin == userPin:
            print("Balance is : ", self.balance)
            self.menu()
        else:
            print("Enter Correct Pin ")
            self.menu()



    def withDraw(self):
        inputPin = int(input("Enter Pin : "))
        amount = int(input("Enter Amount To Withdrwal "))

        if inputPin == self.pin:
            if self.balance > 0 and amount <= self.balance:
                self.balance-=amount
                print("Balance Left is : ", self.balance)
                self.menu()
            else:
                print("Insufficent Balance ! ")
                self.menu()
        else:
            print("Theif")
            self.menu()

    def menu(self):
        
        while True:
            a = int(input("Enter a number between 1 and 4 : "))    
            if a == 1:
                self.createPin()
            elif a == 2:
                self.changePin()
            elif a == 3:
                self.checkBalance()
                print("Option 3 selected")
            elif a == 4:
                self.withDraw()
                print("Exiting...")
                # break
            else:
                exit()



c1 = Atm()
