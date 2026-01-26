class bank:
    def __init__(self,an,name,branch,balance): #how we sotre values  inside b1 similary we need to store inside self
        #that is attribue crestion
        #we can store values inside obj[self] usong attributes
        self.an=an  #b1.an=123
        self.name=name
        self.branch=branch
        self.balance=balance

    def test1(self):
        print("a")

b1=bank(123,"ramesh","hsr",5000)

print(b1.an)






#lets had another acc
b2=bank(124,"yousuf","pdrl",9000)

print(b2.balance) #synatx is print(objname.atrributename)












































b3=bank(111,"abida","oldguntur",10000)
out=b3.branch
print(out)