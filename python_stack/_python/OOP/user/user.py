class user:

    def __init__(self,name):
        self.name =name
        self.account_balance =0
    def make__withdrawal(self,amount):
        self.account_balance-=amount

    def __display_user_balance(self,name):
        print("name:",self.name,"acount_balance:",self.acount_balance)

    def make__deposit__(self,amount):
        self.account_balance +=amount

yousef=user("yousef")
karmel=user("karmel")
ahmad=user("ahmad")

yousef.make__deposit__(100)
yousef.make__deposit__(500)
yousef.make__deposit__(600)
yousef.make__withdrawal(100)

karmel.make__deposit__(100)
karmel.make__deposit__(500)
karmel.make__withdrawal(400)
karmel.make__withdrawal(50)

ahmad.make__withdrawal(50)
ahmad.make__deposit__(100)
print(ahmad.account_balance)