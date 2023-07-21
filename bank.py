class Bank:
    def __init__(self,balance):
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=1000000


    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print( f'you could not withdraw money because {self.min_withdraw}')
        elif amount>self.max_withdraw:
            print( f'you could not able withdraw more than your {self.max_withdraw}')
        else:
            self.balance-=amount
            print( f'here is your money {amount}')
            print(f'your balance after withdraw is {self.balance}')
            print(f'your balance after withdraw is {self.get_balance()}')


brac= Bank(1500)
brac.withdraw(25)
brac.withdraw(400000000)
brac.withdraw(2500)

dbbl = Bank(300000)
dbbl.deposit(20000)
dbbl.deposit(30000)
print(dbbl.get_balance())
