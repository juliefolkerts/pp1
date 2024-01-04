class Bankacc():
    def __init__(self, acc_nr,balance=0.00):
        self.acc_nr= acc_nr
        self.balance = balance

    def deposit(self,money):
        self.money = float(money)
        self.balance += float(self.money)

    def withdraw(self,moneyy):
        self.moneyy = float(moneyy)
        if self.moneyy > self.balance:
            return 'Insufficient funds on the account'
        else:
            self.balance = self.balance - self.moneyy

    def display_info(self):
        return f'Bank account no: {self.acc_nr}\n'+f'Balance: PLN{self.balance}'
