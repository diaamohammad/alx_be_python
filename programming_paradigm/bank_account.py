class BankAccount:

    def __init__(self,account_balance=0):
        self.account_balance=account_balance

    def deposit(self,amount):
        if amount >  0:
            self.account_balance+=amount

            print(f"balance now is {self.account_balance}")

        else:
            print("please enter the money")

    def withdraw(self,amount):

        if amount > self.account_balance: 
            return False

        elif amount < self.account_balance:
            self.account_balance-=amount
            return True
    def display_balance(self):

        print(f"the current balance is {self.account_balance}")
MyAccount=BankAccount()
MyAccount.deposit()
MyAccount.withdraw()
MyAccount.display_balance()
            
           

   