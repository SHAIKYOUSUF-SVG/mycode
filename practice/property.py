#what is @property decorator:
#used to call method like attributes
#ex.s1.get_an

class bank:
    def __init__(self,an,name,balance):
        self.an=an
        self.name=name
        self.balance=balance
    def get_an(self):
        return self.an
    @property
    def get_name(self):
        return self.name

b1=bank(123,"rajesh",900)
#print(b1.get_an)
print("without property decorator",b1.get_an())
print("with property decorator",b1.get_name)


#we can also write for setter method also
#syntax :@methodname.setter
#with this

class bank:
    def __init__(self,an,name,balance):
        self.an=an
        self.name=name
        self.balance=balance
    def get_an(self):
        return self.an
    @property
    def get_name(self):
        return self.name
    @get_name.setter
    def set_name(self,new_name):
        self.name=new_name
b1=bank(123,"a",900)
b1.set_name="b"
print(b1.get_name)
b1.set_name="ab"