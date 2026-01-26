class bank:
    def __init__(self,an,name,balance):
        self.__an=an
        self.__name=name
        self._balance=balance
    def get_an(self):
        return self.__an
    def __get_name(self):
        return self.__name
    def _get_balance(self):
        return self._balance
b=bank(123,'aa',200)
print(b._bank__an)

print(b._bank__get_name())

print(b._balance)

print(b._get_balance())