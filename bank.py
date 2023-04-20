from user import User


#Child class

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
       
    def deposit(self,amount):
        self.balance+=amount
        print(f'Amount Deposited:{amount}')
        print(f'Balance:{self.balance}')
    
    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance")
        else:
            self.balance-=amount
            print(f'Amount Withdrawn:{amount}')
            print(f'Balance:{self.balance}')   
       
       
    def deatils(self):
        super().deatils()
        print(f'Balance:{self.balance}')