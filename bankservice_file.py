
#Bank service

class reservebank:
    def __init__ (self):
        self.account=100
        self.balance=100000
class statebank(reservebank):
    def __init__(self):
        self.account1=80
        self.balance1=80000
        super(). __init__()
class tamilnadu(statebank):
    def __init__ (self):
        self.account2=60
        self.balance2=60000
        super(). __init__()
class thirunelveli(tamilnadu):
    def __init__ (self):
        self.account3=40
        self.balance3=40000
        super(). __init__()
        
    def deposit(self,y):
        self.balance3=(self.balance3+y)
        self.balance2=(self.balance2+y)
        self.balance1=(self.balance1+y)
        self.balance=(self.balance+y)
        print (self.balance3+y)
        
    def withdraw(self,y):
        self.balance3=(self.balance3-y)
        self.balance2=(self.balance2-y)
        self.balance1=(self.balance1-y)
        self.balance=(self.balance-y)
        print (self.balance3-y)

    def add(self):
        self.account3+1
        self.account2+1
        self.account1+1
        self.account+1
        print(self.account3+1)

    def sub(self):
        self.account3-1
        self.account2-1
        self.account1-1
        self.account-1
        print(self.account3-1)
        
s=thirunelveli()
s.deposit(70000)
s.withdraw(45000)
s.add()
s.sub()

B=open(r"C:\Users\Admin\Desktop\test_practice.txt","a+")
B.write("pythonbankserver\n")
B.write("muthu")
B.close()

A={"reservebank":[],"statebank":[],"tamilnadu":[],"thirunelveli":[]}
A["reservebank"].extend([s.account,s.balance])
A["statebank"].extend([s.account1,s.balance1])
A["tamilnadu"].extend([s.account2,s.balance2])
A["thirunelveli"].extend([s.account3,s.balance3])

B.write({"{0}\n".format(A)})
B.close()
    
