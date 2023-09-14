

class BankAccount:

 def __init__(self,account_number,account_holder_name,initial_balance = 0):
   self.__account_number = account_number
   self.__account_holder_name = account_holder_name
   self.__account_balance = initial_balance

def deposit(self, amount):
  if amount > 0:
    self.__account_balance += amount
    print(f"Deposited ${amount}. new balance: ${self.__account_balance}")
  else:
    print("invalid deposit amount.please deposit a positive amount. ")

def withdraw(self,amount):
  if  0 < amount <=  self.__account_balance:
    self.__account_balance -= amount
    print(f"withdraw ${amount}. new balance: {self.__account_balance}")
  else:
    print("invalid withdrawal amount or insufficient balance.")

def display_balance(self):
  print(f"account  holder: {self.__account_holder_name}")
  print(f"account number: {self.__account_number}")
  print(f"account balance: {self.__account_balance}")

#create an instance of BankAccount
account1 = BankAccount("123456789","dinesh",5000.0)

#text deposite and withdrawal functionality
account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.display_balance()

  
     
    
  