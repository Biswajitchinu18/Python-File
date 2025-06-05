from datetime import datetime,timedelta

class BankAccount:
    def __init__(self,account_holder,initial_amount=100):
        self.account_holder = account_holder
        self.balance = initial_amount

    def credit(self,amount):
        self.balance +=amount
        print(f'account_holder:- {self.account_holder},credit:- {amount},NewBalance:- {self.balance}')

    def debit(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'account_holder:- {self.account_holder},credit:- {amount},NewBalance:- {self.balance}')
        else:
            print('insufficient fund')

    def calculate_interest(self,transaction_date):
        today = datetime.now().date()
        print(today,type(today))
        delta_days = (today-transaction_date).days

        if delta_days > 150:
            interest_rate = 0.25
            interest = self.balance * interest_rate
            self.balance += interest
            print(f'interest of 25% {interest} applied after {delta_days} days, Current balance:- {self.balance}')


obj1 = BankAccount('274858000367173',1000)
obj1.credit(100)
obj1.debit(450)
obj1.credit(540)
obj1.debit(1400)

#int man

old_date = datetime.now().date()-timedelta(days=160)
obj1.calculate_interest(old_date)



