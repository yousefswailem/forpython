class BankAccount:
	def __init__(self,name,int_rate, balance): 
        self.name=name
        self.int_rate=100
        self.balance=0
	def deposit(self, amount):
		self.balance+=amount
	def withdraw(self, amount):
        if balance<amount:
            print("Insufficient funds: Charging a $5 fee")
            balance-=5
            else
		self.balance-=amount
	def display_account_info(self):
		print("balance=","$",balance)
	def yield_interest(self):
        if balance >0:
		self.balance=balance+balance*int_rate
        else
        pass
yousef.deposit(500)
print(balance)