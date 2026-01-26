class school:
    name="xyz"
    _sclid="123454"
    def start(self,teacher1,teacher2):
        self._teacher1=teacher1
        self._teacher2=teacher2
        self.hm="abcd"
    def get_mth1(self):
        return self._teacher1
    def _get_mth2(self):
        return self._teacher2
out=school()
out.start("ravi","kiran")

print(out._teacher1)

print(out._get_mth2())

print(out._sclid)#protected class attributes calling method