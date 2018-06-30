class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name=name

    def __repr__(self):
        return "%s's account. Balance: $%.2f" % (self.name, self.balance)
    def show_balance(self):
        print("%s's account. Balance: $%.2f" % (self.name, self.balance))

    def deposit(self, amount):
        if amount <= 0:
            print( "Some error message here")
        else:
            print("正在增加金额 $%.2f" %(amount))
            self.balance += amount
            self.show_balance()
    def withdraw(self, amount):
        if amount <= 0:
            print( "Some error message here")
        else:
            print("正在提取金额 $%.2f" %(amount))
            self.balance -= amount
            self.show_balance()


my_account = BankAccount("a")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(10)
print(my_account)
