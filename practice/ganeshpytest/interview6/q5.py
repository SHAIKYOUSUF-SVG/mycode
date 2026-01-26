#what is @property decorater?
#used to call methods in aclass as we cal attroibutes
#calling methods without()


class bank:
    def __init__(self,an,name):
        self.an=an
        self.name=name
    @property
    def get_an(self):
        return self.an
    def get_name(self):
        return self.name
    def set_name(self,new_name):
        self.name=new_name
b1=bank(123,"sachin")
print(b1.get_name)
print(b1.get_an)