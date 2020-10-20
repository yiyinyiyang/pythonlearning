class BankAccount:


    def __init__(self, account,name):
        self.account = account
        self.name= name
        self.balance = 0.0
    def __str__(self):
        msg=("账户是："+str(self.account) +"姓名是："+str(self.name))
        return msg
    
    def showbalance(self):
        print("你的账户是："+ str(self.account))
        print("你的姓名是："+ str(self.name))
        print("你的余额是："+ str(self.balance))
    def deposit(self,amount):
        self.balance +=amount
        print("你存入的金额是："+ str(amount))
        print("你现在的余额是："+ str(self.balance))
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("你取出的金额是："+ str(amount))
            print("你现在的余额是："+ str(self.balance))
        else:
            print("你的余额是"+ str(self.balance) + "余额不足")

mybankaccount1 = BankAccount(123456,"方晟")
# print("我账户余额是："+str(mybankaccount.showbalance()))
mybankaccount1.showbalance()
mybankaccount1.deposit(36)
mybankaccount1.withdraw(18)
mybankaccount1.withdraw(20)
# print("我存入36元账户的余额是"+str(mybankaccount.deposit(36)))
# print("我取出18元账户余额是:"+str(mybankaccount.withdraw(18)))
# print("我再取出20元账户余额是:"+str(mybankaccount.withdraw(20)))
        
print(mybankaccount1)


#加入利息计算
class InterestAccout(BankAccount):
    def __init__(self,account,name,rate):
        BankAccount.__init__(self,account,name)
        self.rate = rate
    def addinterest (self):
        interest = self.balance * self.rate
        self.deposit(interest)
        print("今年的利息是："+ str(interest))


mybankaccount2 = InterestAccout(456789,"徐娟",0.1)
mybankaccount2.showbalance()
mybankaccount2.deposit(40)
mybankaccount2.addinterest()

print(mybankaccount2)


    
    
  
