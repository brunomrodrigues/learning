class Account:
    def __init__(self, code, balance):
        self.code    = code
        self.balance = balance

    def deposit(self, value):
        self.balance += value

    def __lt__(self, another):
        if self.code != another.code:
            return self.code < another.code
        else:
            return self.balance < another.balance

    def __str__(self):
        return f'Balance: {self.balance} \nCode: {self.code}'

acc1 = Account("123456", 500)
acc2 = Account("654321", 500)

def deposit_in_all_accounts(accounts):
    for acc in accounts:
        acc.deposit(100)

accs = [acc1, acc2]

deposit_in_all_accounts(accs)

for acc in accs:
    print(acc)

#Tuples
bruno   = ("Bruno", 30)
mariana = ("Mariana", 30)

#Heritage and Polymorphism
class CurrentAccount(Account):
    def next_month(self):
        self.balance -=2

class ReserveAccount(Account):
    def next_month(self):
        self.balance +=10

acc1 = CurrentAccount("1", 456)
acc1.next_month()
acc2 = ReserveAccount("2", 456)
acc2.next_month()

print(acc1)
print(acc2)

accounts = [acc1, acc2]

for account in accounts:
    account.next_month()

print(acc1)
print(acc2)


#Unpacking
list = [10, 5, 10, 20, 30]
for i, value in enumerate(list):
    print(i, value)
    
#Ordenation
lista = [10, 5, 10, 20, 30]
print(sorted(lista))
lista = [10, 5, 10, 20, 30]
lista = reversed(list)
for index, value in enumerate(lista):
    print(value)

#Object Ordenation - Remember about functools import
def get_balance(acc):
    return acc.balance

acc1 = Account("1", 460)
acc2 = Account("2", 457)
accs = [acc1, acc2]
for acc in sorted(accs):
    print(acc)