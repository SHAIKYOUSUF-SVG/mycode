#how to access [rivate attributes in derived class:

class bank:
    def __init__(self,name,an):
        #print("init")
        self.__name=name
        self.__an=an
    def get_name(self):
        return self.__name
class savaingsbank(bank):
    print("############")
    def get_an(self):
        return self._bank__an

s1=savaingsbank("rakesh",1234)
b1=bank("rahul",123)

print(s1.get_an()) #accessing privtae attributes of parent class from child class