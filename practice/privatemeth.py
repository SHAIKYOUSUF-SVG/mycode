
class bank:
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.__name=name
        self.__branch=branch
        self._balance=balance
    def __get_branch(self):
        return self.__branch
    def _get_an(self):
        return self.an


out=bank(123,"ajay","hdfc1","10")

print(out._bank__get_branch())

print(out._get_an())
print(out._bank__name)