class BankAccount:
    def __init__(self,accno,balance=0): # this ia a constructor
        self.__accno = accno
        self.__balance = balance
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Amount : ${amount}.\n New Balance : ${self.__balance}")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}.\n New balance: ${self.__balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount")
    def get_balance(self):
        return self.__balance
    
account1 = BankAccount("123456",1000)
account1.deposit(2000)
account1.withdraw(500)
print(f"Current balance: ${account1.get_balance()}")
        