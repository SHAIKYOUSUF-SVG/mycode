class bank:
    def __init__(self,an,name,branch,balance):
        self.an=an
        self.__name=name
        self.__branch=branch
        self._balance=balance
    def get_branch(self):
        return self.__branch

out=bank(123,"ajay","hdfc1","10")
print(out.an)
print(out._bank__name)
print(out._balance)

print(out.get_branch())



class animals:
    def __init__(self,wild,domestic,sea):
        self.__wild=wild
        self.__domestic=domestic
        self._sea=sea
    def get_wild(self):
        return self.__wild
    def __get_domestic(self):
        return self.__domestic
    def _get_sea(self):
        return self._sea
out=animals('lionn','cow','fish')
print(out._animals__wild)


print(out._animals__get_domestic())

print(out._sea)
print(out._get_sea())