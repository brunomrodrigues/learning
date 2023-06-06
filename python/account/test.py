from account import Account

account = Account(123, "Bruno Rodrigues", 5000, 500)

account.withdraw(5000)
account.get_balance()
account.deposit(4500)
account.get_balance()
account.withdraw(5000)
account.withdraw(5000)


