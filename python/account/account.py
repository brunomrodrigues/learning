class Account:

    def __init__(self, number, owner, balance, limit):
        self.number  = number
        self.owner   = owner
        self.balance = balance
        self.limit   = limit
    
    def show_balance(self):
        print("The {} account balance is {}".format(self.owner, self.balance))
    
    def deposit(self, value):
        self.balance+= value

    def withdraw(self, value):
        self.balance -= value
