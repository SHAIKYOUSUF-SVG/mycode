class animal:
    def __init__(self,sea):
        self.sea=sea
    def get_aa(self):
        return self.sea
class animal1:
    def __init__(self,wild):
        self.wild=wild
    def get_aa(self):
        return self.wild
a=animal('fish')
b=animal1('lion')
print(a.get_aa())
print(b.get_aa())