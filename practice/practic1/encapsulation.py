class bank:
    def __init__(self,an,name):
        self.an=an
        self.__name=name
    def get_name(self):
        return self.__name
b=bank(123,'usuf')
print(b.an)
print(b.get_name())