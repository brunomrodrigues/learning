def create_account(number, owner, balance, limit):
    account = {"number":number, "owner": owner, "balance": balance, "limit": limit}
    return account

def deposit(account, value):
    account['balance']+= value

def withdraw(account, value):
    account['balance']-= value

def show_balance(account):
    print("Your balance is {}".format(account['balance']))



account = create_account(123456, "Bruno", 10000, 5000)

show_balance(account)
deposit(account, 12000)
show_balance(account)
withdraw(account, 5000)
show_balance(account)


