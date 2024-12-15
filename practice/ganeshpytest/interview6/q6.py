#for even private methdos alo we use @property decorator


class bank:
    def __init__(self,an,name):
        self.__an=an
        self.__name=name
    #@property
    def get_an(self):
        return self.__an
    @property
    def get_name(self):
        return self.__name
    def set_name(self,new_name):
        self.name=new_name

b1 = bank(123, "sachin")
print(b1.get_name)
print(b1.get_an())

print(b1._bank__an)