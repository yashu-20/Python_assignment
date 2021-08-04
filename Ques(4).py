"""
4.Consider any real time application like banking, college automation, stock market etc.,
and make use of user defined exceptions according to application and raise that exception
"""

class Insufficient_balance_Exception(Exception):
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
    # __str__ is to print() the value
    def __str__(self):
        return(repr(self.value))
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        try:
            if self.balance>=amount:
                self.balance-=amount
                print("\n You Withdrew:", amount)
            else:
                raise Insufficient_balance_Exception(amount)
        except Insufficient_balance_Exception as e:
            print("Insufficient_balance_Exception ",e.value,"is greater than the amount in account......!")
            
    def display(self):
        print("\n Net Available Balance=",self.balance)
  
# Driver code
   
# creating an object of class
s = Bank_Account()
   
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

"""
Hello!!! Welcome to the Deposit & Withdrawal Machine
Enter amount to be Deposited: 4000
 Amount Deposited: 4000.0
Enter amount to be Withdrawn: 10000
Insufficient_balance_Exception  10000.0 is greater than the amount in account......!
 Net Available Balance= 4000.0
"""
