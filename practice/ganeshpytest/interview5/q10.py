#multiple inheritance?


class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    def get_name(self):
        print("from bank")
        return self.name
    def get_an(self):
        print("from bank")
        return self.an

class savingsbank(bank):
    def get_an(self):
        print("from savings bank")
        super().get_an()  #super() used to set search order
        return self.an

s1=savingsbank(123,"kiran")
print(s1.get_an())
print(s1.get_name())