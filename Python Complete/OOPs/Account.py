class Account:
    def __init__(self, accountNum, balance):
           self.accountNum = accountNum
           self.balance = balance
    def deposit(self, amount):
            self.balance+=amount
            print("Your balance : ", self.balance)
    def withdrawl(self, amount):
           if(self.balance <= 0 | amount>self.balance):
                  print("Balance not available")
           else:
                self.balance = self.balance - amount
                print("Your balance : ", self.balance)
    def display(self):
           return self.balance

acc1 = Account(12321, 500)
acc1.deposit(500)
acc1.withdrawl(1200)
acc1.display()