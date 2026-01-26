#for set metthod also call like this way
#we need to use another  @get_name.setter



class bank:
    def __init__(self,an,name):
        self.__an=an
        self.__name=name
    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def set_name(self,new_name):
        if type(new_name) == str:
            print(f"setting name to {new_name}")
            self.__name=new_name
        else:
            print(f"error,cant set {new_name}")
b1=bank(123,"name1")
print(b1.get_name)
b1.set_name="name2"
print(b1.get_name)

b1.set_name=999

print(b1.__dict__)