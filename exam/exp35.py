#Create a Bank account with members account number, name, type of account and balance.
# Write constructor and methods to deposit at the bank and withdraw an amount from the bank.

class Bank:
    def __init__(self,accno,name,type,bal):
        self.accno=accno
        self.name=name
        self.type=type
        self.bal=bal
    def withdraw(self,amt):
        if(amt<=self.bal):
            self.bal=self.bal-amt
            return self.bal
        else:
            print("Error")
    def deposit(self,amt):
        self.bal=self.bal+amt
        return self.bal

accno=int(input("Enter the account number : "))
name=input("Name :")
type=input("type :")
o=Bank(accno,name,type,10000)
c=1
while(c!=4):
    c=int(input("1.Deposit\n2.Withdraw\n3.Balance\n4.Exit\nEnter your choice"))
    if(c==1):
        amt=int(input("Enter the amount :"))
        b=o.deposit(amt)
    elif(c==2):
        amt = int(input("Enter the amount :"))
        b=o.withdraw(amt)
    elif(c==3):
        print(b)