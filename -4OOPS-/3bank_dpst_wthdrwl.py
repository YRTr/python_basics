#For this challenge, create a bank account class that has two attributes:

    #owner
    #balance
#and two methods:

    #deposit
    #withdraw
#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
class Account():

    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,add):
        self.add=add
        self.balance=self.balance+self.add
        return 'Deposit Successful'

    def withdraw(self,sub):
        self.sub=sub
        if self.balance>self.sub:
            self.balance=self.balance-self.sub
        else:
            return 'No sufficient funds'
own=input("Account Holder: ")
bal=float(input("Initial Balance: "))
acct1=Account(own,bal)
print("The account holder name: {}".format(acct1.owner))
print("The account balance: {}".format(acct1.balance))
print('Choose 1 to deposit -or- 2 to withdrawal')
choice=int(input("Choose: "))
if choice==1:
    a=int(input('Amount for deposit: '))
    dep=acct1.deposit(a)
    print(dep)
    print("Deposited amount: {}".format(a))
    print("Total Balance: {}".format(acct1.balance))
else:
    s=int(input('Withdrawal Amount: '))
    wit=acct1.withdraw(s)
    print(wit)
    print('Remaining balance: {}'.format(acct1.balance))
    print('Withdrawal amount: {}'.format(s))
