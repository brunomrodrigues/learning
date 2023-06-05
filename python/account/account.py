class Account:

    def __init__(self, number, owner, balance, limit):
        self.__number  = number
        self.__owner   = owner
        self.__balance = balance
        self.__limit   = limit
    
    def show_balance(self):
        print("The {} account balance is {}".format(self.__owner, self.__balance))
    
    def deposit(self, value):
        self.__balance+= value

    def withdraw(self, value):
        self.__balance -= value

    def transfer(self, value, destiny):
        self.withdraw(value)
        destiny.deposit(value)

    def get_balance(self):
        print(self.__balance)

    @property
    def limit(self):
        print(self.__limit)
    
    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit