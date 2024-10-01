#Banking System
class Account:
    def __init__(self,balance,account):
        self.balance = balance
        self.account_no = account

    #debit method
    def debit(self, ammount):
        self.balance -= ammount
        print('Rs.', ammount, 'was debited')
        print('Now the Total balance is : ', self.get_balance())
        
    #credit method
    def credit(self, ammount):
        self.balance += ammount
        print('Rs.', ammount, 'was crebited')
        print('Now the Total balance is : ', self.get_balance())

    #get_balance
    def get_balance(self):
        return self.balance
    
debit = int(input("How much money you want to withdraw: "))
credit = int(input("How much money you want to diposit: "))

bal = 73000   
acc1 = Account(bal, 12345)
print('The Account no is:', acc1.account_no)
print('The total balance is:', acc1.balance)
acc1.debit(debit)
acc1.credit(credit)


