class User:
    def init(self, name, email):
        self.name=name
        self.email=email
        self.account=Bankaccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)


        return self

    def make_withdrawal(self, amount):
        if  self.account.balance >= amount:
             self.account.withdrawal(amount)

    def account_info(self):
        print(f"name : {self.name} account balance : ${self.account.balance}")

    def transfare_money(self, other_users, amount):
        if amount <= self.account.balance:
            self.account.balance -= amount
            other_users.account.balance += amount


class Bankaccount:
    def init(self, intrate=0.02, balance=0):
        self.intrate=intrate
        self.balance=balance


    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdrawal(self, amount):

            self.balance-=amount


    def yield_interest(self):
        self.balance=self.balance + (self.balance*self.intrate)



yousef = User("yousef", "hi")
ahmad =User("ahmad","hello")
yousef.make_deposit(5000).make_withdrawal(4000)
yousef.transfare_money(ahmad, 500)
yousef.account_info()
ahmad.account_info()