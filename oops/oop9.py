#public attributes:we can access/can chnage the attributes
#we can
class Bank:
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.name=name
        self.branch=branch
        self.balance=balance
b1=Bank(123,"yousuf","opdrl",900)

print(b1.an)

b1.an=1111111
print(b1.an)

b1.name="hi"
print(b1.__dict__)
#with public attributes we can update the data easily to avoid that wemake attributes private