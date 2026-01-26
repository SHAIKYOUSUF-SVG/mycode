#protected attributes are accessed in parent and cjild cls also but no in outside
class bank:
    def __init__(self,an,name):
        self._an=an
        self._name=name
    def get_an(self):
        return self._an
    def get_name(self):
        print("from main bank")
        return self._name
class salarybank(bank):
    def get_name(self):
        print("from cjhjild bank")
        super().get_an()
        return self._name

s1=salarybank(1234,"rajesh")

print(s1.get_name())

print(s1._an)