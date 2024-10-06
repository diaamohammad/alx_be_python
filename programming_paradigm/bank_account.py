class BankAccount:

    def __init__(self,account_balance=0):
        self.account_balance=account_balance

    def deposit(self,amount):
        if amount >  0:
            self.account_balance+=amount

            print(f" Deposited: ${amount}")

        else:
            print("Please enter a valid amount")

    def withdraw(self,amount):

        if amount > self.account_balance: 
            print("Insufficient funds.")
            return False

        elif amount < self.account_balance:
            self.account_balance-=amount
            return True
    def display_balance(self):

        print(f"Current Balance: {self.account_balance}")
MyAccount=BankAccount()
MyAccount.deposit()
MyAccount.withdraw()
MyAccount.display_balance()
            
           

   