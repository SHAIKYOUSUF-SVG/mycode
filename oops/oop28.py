#wrote get method for get class attributes

class bank:
    counter=0
    def __init__(self,an):
        self.an=an
        bank.counter=bank.counter+1
    def get_method(self):
        return bank.counter
b1=bank(123)
b2=bank(123)
print(b1.get_method())

fw=open("methods.txt","w")
fw.close()