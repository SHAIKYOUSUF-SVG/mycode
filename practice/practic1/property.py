class animal:
    def __init__(self,wild,domestic):
        self.wild=wild
        self.__domestic=domestic
    @property
    def get_wild(self):
        return self.wild
    @property
    def get_domestic(self):
        return self.__domestic

a=animal('lion','dog')

print(a.get_wild)
print(a.get_domestic)