class Bank:
    def info(self):
        print("bank Name SBI")

class SavingsAccount(Bank):
    def savingaccountinfo(self):
        print("Saving Account has --- money")

class CurrentAccount(Bank):
    def currentaccountinfo(self):
        print("Current Account Details")

s= SavingsAccount()
s.info()
s.savingaccountinfo()
print("")
c= CurrentAccount()
c.info()
c.currentaccountinfo()