from abc import ABC, abstractmethod

class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass

class BankATM(ATM):

    def withdraw(self):
        print("Cash Drawn Successfully")

# Testing the Class
atm = BankATM()
atm.withdraw()